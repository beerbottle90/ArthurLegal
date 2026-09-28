"""Yerel karar motoru — Jev'in yerine geçen, cihazdan çıkmayan sürüm.

``jev.py`` ile AYNI arayüzü taşır: ``sor(state, sorular) -> {ad: Cevap}``.
Bu yüzden pilotlarda tek satır değiştirilerek yer değiştirebilirler ve aynı
altın küme üzerinde yan yana ölçülürler.

Neden bu tasarım (üç ayağınıza göre):

  1. DOĞRU RESMÎ KAYNAK — eğitim gövdesi resmigazete.gov.tr'nin kendi fihristi,
     ArthurLegalTR'nin kendi ayrıştırıcısıyla okunuyor. Arada kimse yok.

  2. AZ HATALI SÖZEL YORUM — bu motor yorum YAPMAZ. Yorumu Opus yapar. Buranın
     tek işi Opus'a neyin gideceğine karar vermek. O yüzden ölçtüğümüz şey
     doğruluk değil, KAÇIRMAMAKTIR.

  3. İNSAN DENETİMİ — her karar açıklanabilir: ``neden()`` kararı sürükleyen
     n-gramları döndürür, kural katmanı ise satır satır okunabilir.

═══════════════════════════════════════════════════════════════════════════
TASARIMIN OMURGASI: kural katmanı yalnızca EKLER, asla ELEMEZ.

    p_son = max(p_kural, p_model)

Bir kural eşleşirse olasılık 1.0'a sabitlenir ve model bunu veto EDEMEZ.
Sonuç: sistemin duyarlılığı, modelin ne yaptığından bağımsız olarak
kuralların duyarlılığından ASLA düşük olamaz. Kanıtlanabilir bir taban.
Model yalnızca kuralların sessiz kaldığı yerde konuşur.
═══════════════════════════════════════════════════════════════════════════

Bağımlılık: yalnız numpy. Ayrı süreç, sunucu, pencere yoktur — bu bir modüldür,
``import yerel`` ile ArthurLegalTR veya uyap-mcp içine gömülür.
"""

from __future__ import annotations

import json
import re
import time
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

import numpy as np

from jev import Cevap, Olcer, katla

__all__ = ["Kural", "KURALLAR", "YerelMotor", "egit", "ngramlar"]

N_MIN, N_MAX = 3, 5


# --------------------------------------------------------------------------- #
# Kural katmanı — deterministik, açıklanabilir, yalnız ekleyici
# --------------------------------------------------------------------------- #

@dataclass(frozen=True)
class Kural:
    """Eşleşirse konuyu ZORLA geçiren yüksek isabetli desen.

    Bu desenler bilinçli olarak dardır. Bir kuralın yanlış pozitif vermesi
    ucuzdur (bir kalem fazladan Opus'a gider); ama kural listesi genişledikçe
    okunabilirliği düşer ve okunabilirlik burada bir özellik, süs değil.
    """
    konu: str
    desen: str
    gerekce: str
    kurum_adi: bool = False   # desen bir KURUM ADINI yakalıyorsa True

    def eslesir(self, katli_metin: str) -> bool:
        if re.search(self.desen, katli_metin) is None:
            return False
        # Kurum adına bakan kurallar, o kurumun KENDİ İÇ İDARİ düzenlemelerinde
        # susar. "Gelir İdaresi Başkanlığı Personeli Görevde Yükselme
        # Yönetmeliği" bir vergi düzenlemesi değildir; kurumun personel işidir.
        # Kural katmanı model tarafından veto edilemediği için, bu istisna
        # olmadan düzeltilemeyen bir yanlış pozitif doğardı.
        #
        # Bu, "kural yalnız ekler" ilkesini bozmaz: istisna kuralın ATEŞLENİP
        # ateşlenmeyeceğine karar verir, modelin cevabını bastırmaz. Kural
        # sustuğunda model konuşur.
        if self.kurum_adi and IC_IDARE.search(katli_metin):
            return False
        return True


# Kurumun kendi iç işleyişini düzenleyen başlıklar. Yalnız ``kurum_adi=True``
# kuralları susturur; konuya bakan kuralları ("elektrik piyasası", "vergi usul
# kanunu" gibi) hiç etkilemez.
IC_IDARE = re.compile(
    r"personeli|gorevde yukselme|unvan degisikligi|yer degistirme|"
    r"disiplin amirleri|hukuk musavirligi|doner sermaye|"
    r"hurda|malzeme-tasit|meslek personeli|uzmanligi yonetmeligi|"
    r"atama ve yer degistirme|burs program|odul program")


# Desenler KATLANMIŞ metne uygulanır (küçük harf, aksansız — bkz. jev.katla).
KURALLAR: Tuple[Kural, ...] = (
    # --- enerji ---
    Kural("enerji", r"enerji piyasasi duzenleme", "EPDK'nın tam adı", kurum_adi=True),
    Kural("enerji", r"\bepdk\b", "EPDK kısaltması", kurum_adi=True),
    Kural("enerji", r"(elektrik|dogal gaz|petrol|lpg|sivilastirilmis) piyasasi",
          "piyasa kanunlarının adı"),
    Kural("enerji", r"enerji (nakil|iletim|dagitim) hat", "iletim/dağıtım altyapısı"),
    Kural("enerji", r"\b(teias|tedas|euas|botas|tetas)\b", "kamu enerji şirketleri", kurum_adi=True),
    Kural("enerji", r"yenilenebilir enerji", "YEK mevzuatı"),
    Kural("enerji", r"nukleer (santral|enerji|guc)", "nükleer enerji"),
    Kural("enerji", r"elektrik (uretim|dagitim|tuketim|abonel)", "elektrik faaliyetleri", kurum_adi=True),
    # NOT: "Maden Kanunu" bilinçli olarak KURAL DEĞİL. Maden mevzuatı her tür
    # madeni kapsar; linyit/taşkömürü dışındakiler enerji değildir ve gövdeyi
    # etiketlerken maden kalemleri enerji sayılmadı. Kural katmanı model
    # tarafından veto edilemediği için buraya konan geniş bir desen, sonradan
    # düzeltilemeyen bir yanlış pozitif olurdu. Linyit/kömür sinyalini modelin
    # öğrenmesi gerekir, kuralın değil.
    Kural("enerji", r"\bsarj hizmeti", "elektrikli araç şarjı — 6446 s.K. kapsamında"),
    Kural("enerji", r"jeotermal", "jeotermal kaynak — 5686 s.K."),
    Kural("enerji", r"emisyon ticaret", "ETS — fosil yakıt yakımını fiyatlar"),
    Kural("enerji", r"enerji performansi", "binalarda enerji performansı"),
    Kural("enerji", r"enerji piyasalari isletme", "EPİAŞ", kurum_adi=True),

    # --- rekabet ---
    Kural("rekabet", r"rekabet kur(umu|ulu)", "Rekabet Kurumu/Kurulu", kurum_adi=True),
    Kural("rekabet", r"rekabetin korunmasi", "4054 sayılı Kanun'un adı"),
    Kural("rekabet", r"\b4054\b", "4054 sayılı Kanun"),
    Kural("rekabet", r"birlesme ve devralma", "yoğunlaşma denetimi"),

    # --- vergi ---
    Kural("vergi", r"vergi usul kanunu", "VUK"),
    Kural("vergi", r"(gelir|kurumlar|emlak|damga|veraset) vergisi", "vergi türleri"),
    Kural("vergi", r"(katma deger|ozel tuketim|ozel iletisim) vergisi", "KDV/ÖTV/ÖİV"),
    Kural("vergi", r"\b(kdv|otv)\b", "kısaltmalar"),
    Kural("vergi", r"gelir idaresi baskanligi", "GİB", kurum_adi=True),
    Kural("vergi", r"vergi, resim ve harc", "istisna mevzuatının kalıbı"),
    Kural("vergi", r"vergi (kanunu|tebligi|mukellef|beyanname|matrah)", "vergi mevzuatı"),
    Kural("vergi", r"\b(193|213|3065|4760|5520) sayili", "kanun numaraları"),

    Kural("vergi", r"amme alacaklarinin tahsil", "6183 AATUHK"),
    Kural("vergi", r"tahsilat genel tebligi", "6183 uygulama tebliği"),

    # --- icra / usul ---
    Kural("icra", r"icra ve iflas", "İİK'nın adı"),
    Kural("icra", r"\bicra (dairesi|mudurlugu|takibi|hukuk)", "icra teşkilatı"),
    Kural("icra", r"hukuk muhakemeleri kanunu", "HMK"),
    Kural("icra", r"\b(2004|6100|1086) sayili", "İİK / HMK kanun numaraları"),
    Kural("icra", r"yargi cevresinin belirlenmesi", "yargı çevresi kararları"),
    Kural("icra", r"mahkemesi(nin)? kurulmasina", "mahkeme kuruluş kararları"),
    Kural("icra", r"malvarliginin dondurulmasi", "cebrî tedbir"),
    Kural("icra", r"\b(haciz|ihtiyati tedbir|ilamsiz takip)\b", "cebrî icra kavramları"),
    Kural("icra", r"konkordato", "İİK konkordato hükümleri"),
    Kural("icra", r"amme alacaklarinin tahsil", "cebrî tahsil usulü"),
    Kural("icra", r"avukatlik asgari ucret", "yargılama gideri/vekâlet ücreti"),
)


def kural_eslesmeleri(metin: str, konu: str) -> List[Kural]:
    katli = katla(metin)
    return [k for k in KURALLAR if k.konu == konu and k.eslesir(katli)]


# --------------------------------------------------------------------------- #
# Özellik çıkarımı — karakter n-gramları
# --------------------------------------------------------------------------- #

def ngramlar(metin: str, n_min: int = N_MIN, n_max: int = N_MAX) -> Counter:
    """Katlanmış metnin karakter n-gramları.

    Türkçe eklemeli bir dildir: 'vergisinin', 'vergiye', 'vergilendirme' aynı
    kökten gelir ama kelime tabanlı bir model bunları üç ayrı şey sanır.
    Karakter n-gramları bu sorunu kökbulma (stemming) yapmadan çözer — ki
    Türkçe kökbulma kendi başına hataya açık bir iştir.

    Metin boşlukla sarılır ki kelime başı/sonu da bir sinyal olsun.
    """
    s = " " + " ".join(katla(metin).split()) + " "
    sayac: Counter = Counter()
    for n in range(n_min, n_max + 1):
        for i in range(len(s) - n + 1):
            sayac[s[i:i + n]] += 1
    return sayac


class Sozluk:
    """n-gram -> sütun indeksi, artı IDF ağırlıkları."""

    def __init__(self, esleme: Dict[str, int], idf: np.ndarray) -> None:
        self.esleme = esleme
        self.idf = idf
        self.ters = {i: g for g, i in esleme.items()}

    @classmethod
    def kur(cls, metinler: Sequence[str], *, asgari_df: int = 3,
            azami_oran: float = 0.55, azami_ozellik: int = 60_000) -> "Sozluk":
        df: Counter = Counter()
        for m in metinler:
            df.update(set(ngramlar(m)))
        n = len(metinler)
        adaylar = [(g, c) for g, c in df.items()
                   if c >= asgari_df and c <= azami_oran * n]
        adaylar.sort(key=lambda gc: (-gc[1], gc[0]))
        adaylar = adaylar[:azami_ozellik]
        esleme = {g: i for i, (g, _) in enumerate(adaylar)}
        idf = np.array([np.log((1 + n) / (1 + c)) + 1.0 for _, c in adaylar],
                       dtype=np.float64)
        return cls(esleme, idf)

    def vektor(self, metin: str) -> Tuple[np.ndarray, np.ndarray]:
        """(indeksler, l2-normlu tf-idf değerleri) — seyrek gösterim."""
        sayac = ngramlar(metin)
        idx, val = [], []
        for g, c in sayac.items():
            j = self.esleme.get(g)
            if j is not None:
                idx.append(j)
                val.append((1.0 + np.log(c)) * self.idf[j])
        if not idx:
            return np.zeros(0, dtype=np.int64), np.zeros(0, dtype=np.float64)
        i_arr = np.array(idx, dtype=np.int64)
        v_arr = np.array(val, dtype=np.float64)
        norm = np.linalg.norm(v_arr)
        if norm > 0:
            v_arr /= norm
        return i_arr, v_arr

    def yigin(self, metinler: Sequence[str]) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """Tüm gövdeyi tek düz CSR'a serer: (satir_id, sutun_id, deger).

        Düz diziler sayesinde eğitim tamamen vektörleştirilir; Python döngüsü
        yalnız bir kez, veriyi kurarken çalışır.
        """
        satir, sutun, deger = [], [], []
        for r, m in enumerate(metinler):
            i_arr, v_arr = self.vektor(m)
            satir.append(np.full(i_arr.shape, r, dtype=np.int64))
            sutun.append(i_arr)
            deger.append(v_arr)
        if not satir:
            bos = np.zeros(0)
            return bos.astype(np.int64), bos.astype(np.int64), bos
        return (np.concatenate(satir), np.concatenate(sutun), np.concatenate(deger))

    @property
    def boyut(self) -> int:
        return len(self.esleme)


# --------------------------------------------------------------------------- #
# Lojistik regresyon — saf numpy, Adam, sınıf ağırlıklı
# --------------------------------------------------------------------------- #

def _skor(satir: np.ndarray, sutun: np.ndarray, deger: np.ndarray,
          w: np.ndarray, b: float, n_satir: int) -> np.ndarray:
    return np.bincount(satir, weights=deger * w[sutun], minlength=n_satir) + b


def _sigmoid(z: np.ndarray) -> np.ndarray:
    return np.where(z >= 0, 1.0 / (1.0 + np.exp(-np.clip(z, -60, 60))),
                    np.exp(np.clip(z, -60, 60)) / (1.0 + np.exp(np.clip(z, -60, 60))))


def _egit_lojistik(satir: np.ndarray, sutun: np.ndarray, deger: np.ndarray,
                   y: np.ndarray, n_ozellik: int, *, l2: float = 1e-4,
                   adim: float = 0.5, devir: int = 400) -> Tuple[np.ndarray, float]:
    """Sınıf ağırlıklı lojistik regresyon.

    Sınıf ağırlığı şart: 1500 kalemde 30 pozitif varsa ağırlıksız model
    "hep hayır" diyerek %98 isabet alır ve tamamen işe yaramaz olur. Bizim
    umursadığımız sayı duyarlılık olduğu için pozitifler yukarı ağırlıklanır.
    """
    n = len(y)
    w = np.zeros(n_ozellik, dtype=np.float64)
    b = 0.0
    poz, neg = float(y.sum()), float(n - y.sum())
    if poz == 0 or neg == 0:
        return w, -6.0 if poz == 0 else 6.0
    agirlik = np.where(y > 0, n / (2 * poz), n / (2 * neg))

    mw = np.zeros_like(w); vw = np.zeros_like(w)
    mb = vb = 0.0
    b1, b2, eps = 0.9, 0.999, 1e-8
    for t in range(1, devir + 1):
        z = _skor(satir, sutun, deger, w, b, n)
        p = _sigmoid(z)
        art = agirlik * (p - y)                       # ağırlıklı artık
        gw = np.bincount(sutun, weights=deger * art[satir], minlength=n_ozellik)
        gw = gw / n + l2 * w
        gb = float(art.sum()) / n

        mw = b1 * mw + (1 - b1) * gw
        vw = b2 * vw + (1 - b2) * gw * gw
        mb = b1 * mb + (1 - b1) * gb
        vb = b2 * vb + (1 - b2) * gb * gb
        w -= adim * (mw / (1 - b1 ** t)) / (np.sqrt(vw / (1 - b2 ** t)) + eps)
        b -= adim * (mb / (1 - b1 ** t)) / (np.sqrt(vb / (1 - b2 ** t)) + eps)
    return w, b


def _platt(skorlar: np.ndarray, y: np.ndarray, devir: int = 600) -> Tuple[float, float]:
    """Ham skoru kalibre olasılığa çeviren 1 boyutlu lojistik: p = sig(a*s + c).

    Sınıf ağırlıklı eğitim olasılıkları bilerek bozar (pozitifleri yukarı
    iter). Kalibrasyon bunu geri alır — yoksa 0.70 eşiği hiçbir şey ifade
    etmez. Katsayılar KATLANMAMIŞ (out-of-fold) skorlardan öğrenilir; aynı
    veriye bakarak kalibre etmek kendini kandırmaktır.
    """
    a, c = 1.0, 0.0
    n = len(y)
    if n == 0 or y.sum() in (0, n):
        return 1.0, 0.0
    for _ in range(devir):
        p = _sigmoid(a * skorlar + c)
        art = p - y
        ga = float((art * skorlar).sum()) / n
        gc = float(art.sum()) / n
        a -= 1.0 * ga
        c -= 1.0 * gc
    # Negatif eğim, "skor yükseldikçe olasılık düşsün" demektir — monoton bir
    # sınıflandırıcıda bu asla istenmez ve SIRALAMAYI TERSİNE ÇEVİRİR. Az veride
    # (küçük sınıf, az kat) gerçekten olabilir ve hata vermeden olur: model
    # sessizce her şeyi ters cevaplar. Böyle bir durumda kalibrasyondan
    # vazgeçip ham skoru kullanmak, ters çevrilmiş bir modelden iyidir.
    if not np.isfinite(a) or not np.isfinite(c) or a <= 0.0:
        return 1.0, 0.0
    return a, c


# --------------------------------------------------------------------------- #
# Motor
# --------------------------------------------------------------------------- #

class YerelMotor:
    """jev.GercekJev / jev.SahteJev ile aynı sözleşme, sıfır ağ trafiği."""

    sahte = False
    yerel = True

    def __init__(self, sozluk: Sozluk, katsayilar: Dict[str, Dict[str, Any]],
                 *, olcer: Optional[Olcer] = None, ad: str = "YerelMotor") -> None:
        self._sozluk = sozluk
        self._k = katsayilar          # konu -> {w, b, platt_a, platt_c}
        self.olcer = olcer if olcer is not None else Olcer()
        self.ad = ad

    # -- çıkarım ----------------------------------------------------------- #

    @staticmethod
    def _metin(state: Any) -> str:
        if isinstance(state, dict):
            parcalar = [str(v) for k, v in state.items()
                        if k in ("bolum", "baslik", "metin", "title", "section")]
            if parcalar:
                return " ".join(parcalar)
            return " ".join(str(v) for v in state.values())
        return str(state)

    def _model_p(self, konu: str, metin: str) -> float:
        kat = self._k.get(konu)
        if kat is None:
            return 0.0
        idx, val = self._sozluk.vektor(metin)
        ham = float(np.dot(kat["w"][idx], val)) + kat["b"] if len(idx) else kat["b"]
        return float(_sigmoid(np.array([kat["platt_a"] * ham + kat["platt_c"]]))[0])

    def p(self, konu: str, metin: str) -> float:
        """max(kural, model) — kural yalnız yukarı çeker."""
        if kural_eslesmeleri(metin, konu):
            return 1.0
        return self._model_p(konu, metin)

    def sor(self, state: Any, sorular: Dict[str, Dict[str, Any]]) -> Dict[str, Cevap]:
        basla = time.perf_counter()
        metin = self._metin(state)
        cevaplar: Dict[str, Cevap] = {}
        for ad, soru in sorular.items():
            if soru["type"] != "noul":
                raise NotImplementedError(
                    "YerelMotor şimdilik yalnız noul destekler (istenen: %s)" % soru["type"])
            cevaplar[ad] = Cevap(ad, "noul", round(self.p(ad, metin), 4), sahte=False)
        self.olcer.ekle(0, time.perf_counter() - basla)   # token yok: maliyet sıfır
        return cevaplar

    # -- açıklama ---------------------------------------------------------- #

    def neden(self, state: Any, konu: str, kac: int = 8) -> Dict[str, Any]:
        """Kararı sürükleyen gerekçe. İnsan denetiminin dayanağı budur."""
        metin = self._metin(state)
        kurallar = kural_eslesmeleri(metin, konu)
        if kurallar:
            return {"karar": 1.0, "dayanak": "kural",
                    "kurallar": [{"desen": k.desen, "gerekce": k.gerekce}
                                 for k in kurallar]}
        kat = self._k.get(konu)
        if kat is None:
            return {"karar": 0.0, "dayanak": "model yok"}
        idx, val = self._sozluk.vektor(metin)
        katki = kat["w"][idx] * val
        sira = np.argsort(-np.abs(katki))[:kac]
        return {
            "karar": round(self.p(konu, metin), 4),
            "dayanak": "model",
            "ngramlar": [{"ngram": self._sozluk.ters[int(idx[i])],
                          "katki": round(float(katki[i]), 4)} for i in sira],
        }

    # -- kalıcılık --------------------------------------------------------- #

    def kaydet(self, yol: Path) -> None:
        yol = Path(yol)
        np.savez_compressed(
            yol.with_suffix(".npz"),
            idf=self._sozluk.idf,
            **{("w_" + k): v["w"] for k, v in self._k.items()},
        )
        yol.with_suffix(".json").write_text(json.dumps({
            "ad": self.ad,
            "ngram": [N_MIN, N_MAX],
            "sozluk": list(self._sozluk.esleme.keys()),
            "konular": {k: {"b": v["b"], "platt_a": v["platt_a"],
                            "platt_c": v["platt_c"]} for k, v in self._k.items()},
        }, ensure_ascii=False), encoding="utf-8")

    @classmethod
    def yukle(cls, yol: Path, *, olcer: Optional[Olcer] = None) -> "YerelMotor":
        yol = Path(yol)
        ust = json.loads(yol.with_suffix(".json").read_text(encoding="utf-8"))
        ag = np.load(yol.with_suffix(".npz"))
        esleme = {g: i for i, g in enumerate(ust["sozluk"])}
        sozluk = Sozluk(esleme, ag["idf"])
        katsayilar = {k: {"w": ag["w_" + k], "b": v["b"],
                          "platt_a": v["platt_a"], "platt_c": v["platt_c"]}
                      for k, v in ust["konular"].items()}
        return cls(sozluk, katsayilar, olcer=olcer, ad=ust.get("ad", "YerelMotor"))


# --------------------------------------------------------------------------- #
# Eğitim
# --------------------------------------------------------------------------- #

def egit(metinler: Sequence[str], etiketler: Dict[str, np.ndarray], *,
         katlar: int = 5, l2: float = 1e-4, devir: int = 400,
         ad: str = "YerelMotor", sessiz: bool = False) -> YerelMotor:
    """Konu başına bir sınıflandırıcı + çapraz katlamalı Platt kalibrasyonu."""
    sozluk = Sozluk.kur(metinler)
    satir, sutun, deger = sozluk.yigin(metinler)
    n = len(metinler)
    if not sessiz:
        print("Sözlük: %d n-gram · gövde: %d kalem · seyrek hücre: %d"
              % (sozluk.boyut, n, len(deger)))

    rng = np.random.default_rng(20260920)
    kat_no = rng.permutation(n) % katlar

    katsayilar: Dict[str, Dict[str, Any]] = {}
    for konu, y in etiketler.items():
        y = y.astype(np.float64)
        # Katlar arası (out-of-fold) skorlar — kalibrasyon bunlardan öğrenilir.
        oof = np.zeros(n, dtype=np.float64)
        for k in range(katlar):
            egitim = kat_no != k
            maske = egitim[satir]
            yerel_satir = satir[maske]
            # satır indekslerini sıkıştır
            harita = -np.ones(n, dtype=np.int64)
            egitim_idx = np.flatnonzero(egitim)
            harita[egitim_idx] = np.arange(len(egitim_idx))
            w, b = _egit_lojistik(harita[yerel_satir], sutun[maske], deger[maske],
                                  y[egitim_idx], sozluk.boyut, l2=l2, devir=devir)
            oof += np.where(egitim, 0.0, _skor(satir, sutun, deger, w, b, n))
        a, c = _platt(oof, y)
        w, b = _egit_lojistik(satir, sutun, deger, y, sozluk.boyut, l2=l2, devir=devir)
        katsayilar[konu] = {"w": w, "b": b, "platt_a": a, "platt_c": c}
        if not sessiz:
            print("  %-8s pozitif=%-4d  platt a=%.3f c=%.3f"
                  % (konu, int(y.sum()), a, c))
    return YerelMotor(sozluk, katsayilar, ad=ad)
