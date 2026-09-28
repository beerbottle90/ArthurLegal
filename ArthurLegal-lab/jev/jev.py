"""Jev (TypeSafe System One) için ince istemci — gerçek ve sahte.

Jev otoregresif değildir: string üretmez, tek geçişte *tipli* karar döner.
Bu yüzden istemci de bir sohbet istemcisi gibi değil, bir RPC gibi kurulur:
durum (state) + soru haritası girer, cevap haritası çıkar.

Üç soru tipi vardır (TypeSafe "primitives"):
  noul(...)   -> olasılıklı boolean   {"noul": 0.93}
  choice(...) -> en fazla 255 seçenek {"choice": "epdk"}
  score(...)  -> sıralı ölçekte sayı  {"score": 1.4}

SahteJev, anahtar yokken tüm boru hattını uçtan uca çalıştırmak içindir.
Anahtar arayan koda dokunmadan gerçeğe geçilir. Sahte cevaplar HER ZAMAN
``sahte=True`` taşır; rapor katmanı bunu gizlemez.
"""

from __future__ import annotations

import json
import os
import re
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Sequence

__all__ = ["noul", "choice", "score", "Cevap", "Olcer", "JevHatasi",
           "SahteJev", "GercekJev", "istemci_kur", "katla"]

VARSAYILAN_MODEL = "jev-latest"
TYPESAFE_UC = "https://api.typesafe.ai/v1/systemone"

# Bilinen geçiş yolları. Hepsi aynı {model, state, questions} gövdesini alır;
# yalnız URL ve model kimliği değişir. JEV_UC / JEV_MODEL ile seçilir.
#
#   LiteLLM proxy   <PROXY>/typesafe/v1/systemone      (resmî belge)
#   OpenRouter      https://openrouter.ai/api/alpha/decisions
#                   model: typesafe/jev-1.13 | typesafe/jev-latest
#   Vercel Gateway  model: typesafe-ai/jev
#   Cloudflare      Workers AI üzerinden
#
# DÜZELTMENİN DÜZELTMESİ: bu dosyanın ilk sürümünde uydurma bir OpenRouter
# yolu vardı (/api/v1/systemone) ve onu "Jev OpenRouter'da yok" diyerek
# kaldırmıştım. İkisi de yanlıştı. Jev OpenRouter'da VARDIR ama ayrı bir
# **Decisions API**'sindedir: POST /api/alpha/decisions. Sohbet tamamlama
# SDK'ları çalışmaz ve model `GET /api/v1/models` listesinde GÖRÜNMEZ —
# "no OpenRouter listing" iddiası buradan doğmuş.
#
# Vercel Gateway'de kimlik tuzağı var: `typesafe-ai/jev` çalışıyor,
# `typesafe-ai/jev-latest` "Model not found" dönüyor.
OPENROUTER_UC = "https://openrouter.ai/api/alpha/decisions"
OPENROUTER_MODEL = "typesafe/jev-1.13"

GIRDI_USD_MTOK = 0.042          # çıktı 0.00 USD/Mtok olarak fiyatlanıyor

# Uç sınırları (TypeSafe belgeleri). İstek gövdesi bunu aşarsa uç reddeder;
# bizim önceden yakalamamız, 56 kalemlik bir koşunun ortasında patlamaktan iyidir.
AZAMI_ISTEK_TOKEN = 32_000      # state + sorular toplamı

# Bağımsız ölçümlerin bildirdiği çalışma koşulları:
#   * eşzamanlılık 8 ücretli katmanda güvenli; 32 yeniden deneme fırtınası
#     tetikliyor. Ücretsiz katman dakikada birkaç isteğe iniyor.
#   * olasılıklar 0.01'e yuvarlanıyor (rounding.probabilityDecimals = 2) ve
#     sık sık tam 0 ya da tam 1 dönüyor. Tam 0, sıcaklık ölçeklemesiyle
#     onarılamaz — eşik mantığı bunu bilmeli.
ONERILEN_ESZAMANLILIK = 8
OLASILIK_COZUNURLUK = 0.01

# Belgelenmiş hata kodları: 401 geçersiz anahtar, 422 istek doğrulaması,
# 429 hız sınırı, 529 aşırı yük. Yalnız son ikisi ve geçici sunucu hataları
# yeniden denenir; 401/422 denemekle düzelmez.
YENIDEN_DENENIR = frozenset({429, 500, 502, 503, 504, 529})


class JevHatasi(RuntimeError):
    """Ucun döndürdüğü hata ya da sözleşme ihlali."""


# --------------------------------------------------------------------------- #
# Soru kurucuları
# --------------------------------------------------------------------------- #

def noul(instructions: str, kriter: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Olasılıklı evet/hayır. Cevap 0.0-1.0 arası bir sayıdır, bool değil.

    ``kriter`` isteğe bağlıdır ama önerilir: ``{"true": "...", "false": "..."}``
    şeklinde evet/hayırın ne demek olduğunu açıkça yazar. TypeSafe belgeleri
    ikisini de denemeyi öneriyor — ve *instructions ile criteria'nın
    çelişmemesi* gerektiğini özellikle vurguluyor (true'nun "hayır" anlamına
    geldiği bir noul cevapları bozuyor).

    Soru ATOMİK olmalıdır: tek bir yargı sorulmalı. "Dakik ve zeki ve
    deneyimli mi" gibi birden çok boyutu tek soruya sıkıştırmak, birinde
    yüksek diğerinde düşük olan girdiyi yerleştirilemez hâle getirir.
    """
    q: Dict[str, Any] = {"type": "noul", "instructions": instructions}
    if kriter:
        q["criteria"] = dict(kriter)
    return q


def choice(instructions: str, kriter: Dict[str, str]) -> Dict[str, Any]:
    """Seçeneklerden biri. ``kriter`` bir HARİTADIR: {seçenek: açıklaması}.

    Liste değil harita olması bilinçli: modelin seçeneğin ne anlama geldiğini
    bilmesi gerekir. Jev'in state dışında dünya bilgisi yoktur; "billing"in ne
    olduğunu tahmin etmesini beklemek yerine yazmak gerekir.
    """
    if not 2 <= len(kriter) <= 255:
        raise ValueError("choice 2-255 seçenek alır, verilen: %d" % len(kriter))
    return {"type": "choice", "instructions": instructions, "criteria": dict(kriter)}


def score(instructions: str, seviyeler: Sequence[str]) -> Dict[str, Any]:
    """Sıralı ölçek. ``criteria`` SIRALI bir listedir; her eleman bir seviye.

    Tek boyut ölçülmeli. Seviyeler arası bir değer dönebilir (ör. 1.035).
    """
    seviyeler = list(seviyeler)
    if len(seviyeler) < 2:
        raise ValueError("score en az 2 seviye ister, verilen: %d" % len(seviyeler))
    return {"type": "score", "instructions": instructions, "criteria": seviyeler}


@dataclass(frozen=True)
class Cevap:
    """Tek bir sorunun cevabı.

    ``deger``: noul için float, choice için str, score için float.
    ``sahte``: SahteJev üretti mi. Raporda gizlenmez.
    """
    ad: str
    tip: str
    deger: Any
    sahte: bool = False

    @property
    def olasilik(self) -> float:
        """noul için ham olasılık; diğer tipler için anlamsız olduğundan 1.0."""
        return float(self.deger) if self.tip == "noul" else 1.0

    def evet_mi(self, esik: float = 0.5) -> bool:
        if self.tip != "noul":
            raise TypeError("evet_mi yalnız noul için anlamlı (tip=%s)" % self.tip)
        return float(self.deger) >= esik


@dataclass
class Olcer:
    """Çağrı, token ve gecikme sayacı. Pilotun tek maliyet kaynağı budur."""
    cagri: int = 0
    girdi_token: int = 0
    saniye: float = 0.0
    gecikmeler: List[float] = field(default_factory=list)

    def ekle(self, girdi_token: int, saniye: float) -> None:
        self.cagri += 1
        self.girdi_token += girdi_token
        self.saniye += saniye
        self.gecikmeler.append(saniye)

    @property
    def usd(self) -> float:
        return self.girdi_token / 1_000_000 * GIRDI_USD_MTOK

    @property
    def medyan_ms(self) -> float:
        if not self.gecikmeler:
            return 0.0
        s = sorted(self.gecikmeler)
        return 1000 * s[len(s) // 2]

    def ozet(self) -> str:
        return ("%d çağrı · %s girdi tokeni · ~$%.6f · medyan %.0f ms"
                % (self.cagri, "{:,}".format(self.girdi_token).replace(",", "."),
                   self.usd, self.medyan_ms))


def _token_tahmini(nesne: Any) -> int:
    """Kaba tahmin: 1 token ~ 4 karakter. Gerçek istemci ucun sayısını kullanır."""
    return max(1, len(json.dumps(nesne, ensure_ascii=False)) // 4)


# --------------------------------------------------------------------------- #
# Sahte istemci
# --------------------------------------------------------------------------- #

_KATLA = str.maketrans("çğıöşüâîû", "cgiosuaiu")


def katla(metin: str) -> str:
    """Türkçe büyük/küçük ve aksan duyarsız karşılaştırma anahtarı."""
    metin = metin.replace("İ", "i").replace("I", "ı")
    metin = unicodedata.normalize("NFC", metin.lower())
    return metin.translate(_KATLA)


class SahteJev:
    """Anahtarsız, çevrimdışı, deterministik taklit.

    Jev'i *taklit etmez* — boru hattını çalıştırır. Anahtar kelime ağırlıklı
    lojistik bir skor üretir; amacı "Jev ne derdi" değil, "kodum uçtan uca
    çalışıyor mu, eşik mantığım doğru mu, raporum okunur mu" sorularını
    anahtar beklemeden cevaplamaktır. Çıktısı ``sahte=True`` taşır.
    """

    sahte = True
    ad = "SahteJev (çevrimdışı)"

    def __init__(self, ipuclari: Optional[Dict[str, Dict[str, float]]] = None,
                 olcer: Optional[Olcer] = None) -> None:
        # ipuclari: soru adı -> {anahtar kelime: ağırlık}
        self._ipuclari = {a: {katla(k): v for k, v in d.items()}
                          for a, d in (ipuclari or {}).items()}
        self.olcer = olcer if olcer is not None else Olcer()

    def sor(self, state: Any, sorular: Dict[str, Dict[str, Any]]) -> Dict[str, Cevap]:
        basla = time.perf_counter()
        metin = katla(json.dumps(state, ensure_ascii=False))
        cevaplar: Dict[str, Cevap] = {}
        for ad, soru in sorular.items():
            tip = soru["type"]
            if tip == "noul":
                cevaplar[ad] = Cevap(ad, tip, self._noul(ad, soru, metin), sahte=True)
            elif tip == "choice":
                cevaplar[ad] = Cevap(ad, tip, self._choice(soru, metin), sahte=True)
            elif tip == "score":
                seviyeler = soru["levels"]
                p = self._noul(ad, soru, metin)
                cevaplar[ad] = Cevap(ad, tip, round(p * (len(seviyeler) - 1), 2), sahte=True)
            else:
                raise JevHatasi("bilinmeyen soru tipi: %s" % tip)
        self.olcer.ekle(_token_tahmini(state) + _token_tahmini(sorular),
                        time.perf_counter() - basla)
        return cevaplar

    def _noul(self, ad: str, soru: Dict[str, Any], metin: str) -> float:
        agirliklar = self._ipuclari.get(ad)
        if agirliklar is None:
            # İpucu verilmemiş: sorunun kendi kelimeleri kaba bir sinyaldir.
            metinler = [soru.get("instructions", "")]
            kriter = soru.get("criteria")
            if isinstance(kriter, dict):
                metinler += list(kriter.values())
            elif isinstance(kriter, list):
                metinler += kriter
            agirliklar = {k: 1.0 for k in
                          re.findall(r"\w{5,}", katla(" ".join(map(str, metinler))))}
        toplam = sum(a for k, a in agirliklar.items() if k in metin)
        if toplam == 0:
            return 0.04
        # Lojistik sıkıştırma: 0.5 -> ~0.62, 2.0 -> ~0.88, 4.0 -> ~0.97
        return round(min(0.985, 1 / (1 + 2.718281828 ** (-1.15 * toplam + 0.9))), 3)

    @staticmethod
    def _choice(soru: Dict[str, Any], metin: str) -> str:
        secenekler = soru["options"]
        puanlar = {s: sum(1 for p in katla(s).split() if p and p in metin) for s in secenekler}
        en_iyi = max(puanlar, key=lambda s: puanlar[s])
        return en_iyi if puanlar[en_iyi] else secenekler[-1]


# --------------------------------------------------------------------------- #
# Gerçek istemci
# --------------------------------------------------------------------------- #

class GercekJev:
    """api.typesafe.ai veya OpenRouter üzerinden tek uç nokta.

    POST /v1/systemone  ->  {"model", "state", "questions"}
    """

    sahte = False

    def __init__(self, anahtar: str, *, uc: str = TYPESAFE_UC,
                 model: str = VARSAYILAN_MODEL, zaman_asimi: float = 20.0,
                 olcer: Optional[Olcer] = None) -> None:
        if not anahtar:
            raise JevHatasi("anahtar boş")
        self._anahtar = anahtar
        self._uc = uc
        self._model = model
        self._zaman_asimi = zaman_asimi
        self.olcer = olcer if olcer is not None else Olcer()
        self.ad = "Jev (%s · %s)" % (model, urllib.parse.urlparse(uc).netloc)

    def sor(self, state: Any, sorular: Dict[str, Dict[str, Any]]) -> Dict[str, Cevap]:
        istek = {"model": self._model, "state": state, "questions": sorular}
        tahmin = _token_tahmini(istek)
        if tahmin > AZAMI_ISTEK_TOKEN:
            raise JevHatasi(
                "istek ~%d token, uç sınırı %d (state + sorular). State'i kısaltın "
                "ya da soruları bölün." % (tahmin, AZAMI_ISTEK_TOKEN))
        govde = json.dumps(istek, ensure_ascii=False).encode("utf-8")
        istek = urllib.request.Request(self._uc, data=govde, method="POST", headers={
            "Authorization": "Bearer " + self._anahtar,
            "Content-Type": "application/json; charset=utf-8",
        })
        basla = time.perf_counter()
        # 429 ve 5xx'te üstel geri çekilme. Ücretsiz katman dakikada birkaç
        # isteğe iniyor ve yüksek eşzamanlılık yeniden deneme fırtınası
        # tetikliyor; tek bir 429'da pilotun ortasında düşmek anlamsız.
        son_hata: Optional[Exception] = None
        for deneme in range(4):
            try:
                with urllib.request.urlopen(istek, timeout=self._zaman_asimi) as yanit:
                    ham = json.loads(yanit.read().decode("utf-8"))
                break
            except urllib.error.HTTPError as exc:
                detay = exc.read().decode("utf-8", "replace")[:400]
                # Belgelenmiş hata kodları: 401 (anahtar), 422 (doğrulama),
                # 429 (hız sınırı), 529 (aşırı yük). 401 ve 422 yeniden
                # denemeyle düzelmez — anlamsız gecikme olur. 529 TypeSafe'e
                # özgüdür ve standart listelerde yoktur; unutulursa aşırı yük
                # anında pilot düşer.
                if exc.code in YENIDEN_DENENIR and deneme < 3:
                    bekle = float(exc.headers.get("Retry-After") or 0) or 2.0 ** deneme
                    time.sleep(min(bekle, 30.0))
                    son_hata = exc
                    continue
                raise JevHatasi("HTTP %s — %s" % (exc.code, detay)) from exc
            except urllib.error.URLError as exc:
                if deneme < 3:
                    time.sleep(2.0 ** deneme)
                    son_hata = exc
                    continue
                raise JevHatasi("bağlantı: %s" % exc.reason) from exc
        else:
            raise JevHatasi("4 denemede yanıt alınamadı: %s" % son_hata)
        gecen = time.perf_counter() - basla

        kullanim = ham.get("usage") or {}
        self.olcer.ekle(int(kullanim.get("input_tokens") or _token_tahmini(state)), gecen)
        return self._coz(ham, sorular)

    @staticmethod
    def _coz(ham: Dict[str, Any], sorular: Dict[str, Dict[str, Any]]) -> Dict[str, Cevap]:
        cevap_bolumu = ham.get("answers", ham)
        cikti: Dict[str, Cevap] = {}
        for ad, soru in sorular.items():
            if ad not in cevap_bolumu:
                raise JevHatasi("uç '%s' sorusunu cevaplamadı" % ad)
            kutu = cevap_bolumu[ad]
            tip = soru["type"]
            deger = kutu.get(tip) if isinstance(kutu, dict) else kutu
            if deger is None:
                raise JevHatasi("'%s' için %s alanı yok: %r" % (ad, tip, kutu))
            # Şema garantisi uçta; burada yine de doğrula — güven değil, teyit.
            if tip == "choice" and deger not in soru["criteria"]:
                raise JevHatasi("'%s' seçenek dışı değer döndü: %r" % (ad, deger))
            if tip == "noul" and not 0.0 <= float(deger) <= 1.0:
                raise JevHatasi("'%s' için noul aralık dışı: %r" % (ad, deger))
            cikti[ad] = Cevap(ad, tip, deger, sahte=False)
        return cikti


def env_yukle(yol: Optional[Path] = None) -> None:
    """Varsa ``.env``'i sürece yükler. Zaten tanımlı değişkeni EZMEZ.

    Anahtarı her giriş noktasında elle taşımamak için. Değer hiçbir yere
    yazdırılmaz; dosya .gitignore'dadır.
    """
    yol = Path(yol) if yol else Path(__file__).resolve().parent / ".env"
    if not yol.exists():
        return
    try:
        satirlar = yol.read_text(encoding="utf-8").splitlines()
    except OSError:
        return
    for satir in satirlar:
        satir = satir.strip()
        if not satir or satir.startswith("#") or "=" not in satir:
            continue
        ad, _, deger = satir.partition("=")
        os.environ.setdefault(ad.strip(), deger.strip())


def istemci_kur(ipuclari: Optional[Dict[str, Dict[str, float]]] = None,
                *, zorla_sahte: bool = False) -> Any:
    """Ortama göre istemci seçer. Anahtar yoksa sessizce sahteye düşer.

    JEV_API_KEY        -> JEV_UC (varsayılan api.typesafe.ai/v1/systemone)
    OPENROUTER_API_KEY -> OpenRouter Decisions API (/api/alpha/decisions)
    ikisi de yok       -> SahteJev

    Başka bir geçiş (LiteLLM proxy, Cloudflare, Vercel Gateway) için JEV_UC ve
    JEV_MODEL'i o uca çevirin; gövde formatı hepsinde aynıdır.
    """
    if zorla_sahte:
        return SahteJev(ipuclari)
    env_yukle()
    dogrudan = os.environ.get("JEV_API_KEY", "").strip()
    if dogrudan:
        return GercekJev(dogrudan,
                         uc=os.environ.get("JEV_UC", "").strip() or TYPESAFE_UC,
                         model=os.environ.get("JEV_MODEL", VARSAYILAN_MODEL))
    router = os.environ.get("OPENROUTER_API_KEY", "").strip()
    if router:
        return GercekJev(router,
                         uc=os.environ.get("JEV_UC", "").strip() or OPENROUTER_UC,
                         model=os.environ.get("JEV_MODEL", OPENROUTER_MODEL))
    return SahteJev(ipuclari)
