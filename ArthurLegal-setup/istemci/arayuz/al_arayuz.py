"""ArthurLegal arayüzü (MCP Apps): görünümleri birleştirir, masa aracını tanımlar.

Uzak uç (arthurlegal-mcp) ve yerel AL sunucusu (arthurlegal-yerel) aynı modülü kullanır; ikisi de
yalnız standart kütüphaneyle çalışır.

    from al_arayuz import kaynaklar, arac_meta, masa_araci, masa_cevabi

- ``kaynaklar()``: her ``ui://`` görünümü, MCP ``resources/list`` ve ``resources/read`` için.
- ``arac_meta(ad)``: aracın görünümü varsa ``_meta``; host o aracın sonucunu görünümle çizer.
- ``masa_araci()``: ``al_masasi`` aracının tanımı. Cevabı ``masa_cevabi(...)`` kurar.
- ``gecmis_araci()`` ve ``Gecmis(klasor)``: masa geçmişi (``al_gecmis``). Yalnız yerel AL sunucusu klasör
  verir; uzak uç geçmiş tutmaz, masa orada oturumluk listeyle çalışır.

Görünümler ``ortak/gorunumler/*.html`` şablonlarıdır. Ortak tasarım ve kod tek geçişte gömülür:
``/*AL:CSS*/`` ``/*AL:JS*/`` ``/*AL:KARTLAR*/`` ``/*AL:ATIF*/`` ``<!--AL:ARMA-->`` ``<!--AL:DONNA-->``.
Gömülen içerik yeniden taranmaz; bir dosyanın kendi yorumunda yer tutucu adı geçse de bozulmaz.
"""
from __future__ import annotations

import json
import os
import re
import secrets
import threading
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional

SURUM = "3.0.5"

# ortak/ bu dosyanın bir üstünde (depo) ya da yanında (dağıtım paketi).
_BURASI = os.path.dirname(os.path.abspath(__file__))
ORTAK = os.environ.get("AL_ARAYUZ_ORTAK") or next(
    (p for p in (os.path.join(_BURASI, "ortak"), os.path.join(os.path.dirname(_BURASI), "ortak"))
     if os.path.isdir(p)),
    os.path.join(os.path.dirname(_BURASI), "ortak"),
)

MIME = "text/html;profile=mcp-app"
# Görünümün kum havuzu yalnız sabit sürümlü MCP Apps istemcisini yükleyebilir; yazı tipi cihazın.
META = {"ui": {"csp": {"resourceDomains": ["https://unpkg.com"]}, "prefersBorder": False}}

# ui:// adresi -> (şablon, başlık, açıklama)
GORUNUMLER = {
    "ui://arthurlegal/madde-karti.html": ("madde-karti.html", "Mevzuat madde kartı",
                                          "tr_mevzuat_madde_getir sonucunu ArthurLegal kartıyla gösterir."),
    "ui://arthurlegal/ictihat-karti.html": ("ictihat-karti.html", "İçtihat kartı",
                                            "tr_ictihat_ara sonucunu künyeleriyle listeler; metin kartta açılır."),
    "ui://arthurlegal/masa.html": ("masa.html", "ArthurLegal Masası",
                                   "ArthurLegal'in tek panelli yüzü: modüller solda, iş adımları ortada."),
}

# araç -> görünüm
ARAC_GORUNUMU = {
    "tr_mevzuat_madde_getir": "ui://arthurlegal/madde-karti.html",
    "tr_ictihat_ara": "ui://arthurlegal/ictihat-karti.html",
    "al_masasi": "ui://arthurlegal/masa.html",
}

_PARCALAR = {
    "CSS": ("tasarim", "al.css"),
    "JS": ("tasarim", "al.js"),
    "KARTLAR": ("tasarim", "kartlar.js"),
    "ATIF": ("tasarim", "atif.js"),
    "ISTEK": ("tasarim", "istek.js"),
    "ARMA": ("tasarim", "arma.svg"),
    "DONNA": ("tasarim", "donna.svg"),
}
_YER_TUTUCU = re.compile(r"/\*AL:([A-Z]+)\*/|<!--AL:([A-Z]+)-->")

# Masanın ekranları; al_masasi(bolum=...) bunlardan biriyle açılır.
EKRANLAR = ("sohbet", "mevzuat", "ictihat", "gecmis", "tapu", "beyin", "mask", "uyap", "donna", "mcp")


def _oku(*yol: str) -> str:
    with open(os.path.join(ORTAK, *yol), encoding="utf-8") as fh:
        return fh.read()


def gorunum(sablon: str) -> str:
    """Şablonu ortak parçalarla birleştirir. Bilinmeyen yer tutucu hatadır, sessizce kalmaz."""
    metin = _oku("gorunumler", sablon)
    onbellek: Dict[str, str] = {}

    def koy(m: "re.Match[str]") -> str:
        ad = m.group(1) or m.group(2)
        if ad not in _PARCALAR:
            raise KeyError("bilinmeyen yer tutucu: %s (%s)" % (ad, sablon))
        if ad not in onbellek:
            onbellek[ad] = _oku(*_PARCALAR[ad]).strip()
        return onbellek[ad]

    return _YER_TUTUCU.sub(koy, metin)


def kaynaklar() -> List[Dict[str, Any]]:
    """Her görünüm: uri, ad, mimeType, açıklama, _meta ve birleşmiş HTML (text)."""
    out = []
    for uri, (sablon, ad, aciklama) in GORUNUMLER.items():
        out.append({"uri": uri, "name": ad, "mimeType": MIME, "description": aciklama,
                    "_meta": META, "text": gorunum(sablon)})
    return out


def arac_meta(arac: str) -> Optional[Dict[str, Any]]:
    uri = ARAC_GORUNUMU.get(arac)
    if not uri:
        return None
    # Düz "ui/resourceUri" anahtarı, bazı ev sahiplerinin hâlâ okuduğu eski yazım.
    return {"ui": {"resourceUri": uri}, "ui/resourceUri": uri}


def masa_araci() -> Dict[str, Any]:
    return {
        "name": "al_masasi",
        "title": "ArthurLegal Masası",
        "description": (
            "ArthurLegal Masası'nı açar: mevzuat ve atıf teyidi, içtihat, ArthurTapu, Beyin (hafıza), "
            "Arthur Mask, UYAP Dashboard, Donna ve kaynak durumu tek panelde. Kullanıcı 'ArthurLegal'i aç', "
            "'masayı aç', 'AL Masası' ya da bir modülün adını söyleyip onu açmak istediğinde çağırın. "
            "bolum ile belirli bir ekranda açılır."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "bolum": {"type": "string", "enum": list(EKRANLAR),
                          "description": "Açılış ekranı; boşsa sohbet."},
                "tam_ekran": {"type": "boolean", "default": True,
                              "description": "Masa tam ekran açılmayı istesin mi."},
            },
        },
        "annotations": {"readOnlyHint": True, "destructiveHint": False, "openWorldHint": False},
    }


def masa_cevabi(ortam: str, yetenekler: List[str], moduller: Dict[str, Dict[str, str]],
                bolum: Optional[str] = None) -> Dict[str, Any]:
    """al_masasi'nin cevabı: masa neyin çalıştığını buradan bilir.

    ortam: "masaustu" (yerel AL sunucusu) ya da "uzak" (web ve telefon).
    moduller: {"tapu": {"durum": "hazir" | "claude" | "masaustu" | "kurulu-degil"}, ...}
    """
    out: Dict[str, Any] = {
        "surum": SURUM,
        "ortam": ortam,
        "yetenekler": sorted(set(yetenekler)),
        "moduller": moduller,
        "not": ("Masa açıldı. Kullanıcı masada çalışırken yaptığı işi size ArthurLegal Masası notlarıyla "
                "bildirir; masa kendi başına size bir şey göndermez."),
    }
    if "al_gecmis" in out["yetenekler"]:
        out["not"] += (" Masadaki işlerin geçmişi (%d gün, o anki sonuçlarıyla) bu bilgisayarda tutulur; kullanıcı "
                       "masada daha önce baktığı bir şeyi sorarsa al_gecmis ile bakabilirsiniz." % GECMIS_GUN)
    if bolum in EKRANLAR:
        out["bolum"] = bolum
    return out


# --------------------------------------------------------------------------- masa geçmişi
# Masada yapılan iş (arama, madde, içtihat, atıf teyidi, Claude'a giden istek) o anki sonucuyla birlikte
# yalnız bu bilgisayarda tutulur. Atıf teyidinde yapıştırılan metin değil, yalnız bulunan atıflar gelir;
# UYAP işi hiç yazılmaz. Günlüğe sorgu metni yazılmaz.
GECMIS_GUN = 90
GECMIS_AZAMI = 2000
GECMIS_KATEGORILER = ("mevzuat", "ictihat", "atif", "claude")
GECMIS_TURLERI = ("mevzuat-liste", "kurum", "madde", "atif", "ictihat", "claude")
_GECMIS_ADIM = ("tamam", "uyar", "hata")
_GECMIS_KAYIT_SINIRI = 600_000   # bayt; anlık sonuç bundan büyükse kayıt sonuçsuz saklanır
_GECMIS_SORGU_SINIRI = 20_000
_GECMIS_KIMLIK = re.compile(r"^\d{8}-\d{6}-[0-9a-f]{6}$")
_KATLA = str.maketrans("İIıŞşĞğÜüÖöÇçÂâÎîÛû", "iiissgguuooccaaiiuu")


class GecmisHatasi(ValueError):
    """Geçersiz istek ya da okunamayan kayıt; çağıran isError olarak döndürür."""


def gecmis_araci() -> Dict[str, Any]:
    return {
        "name": "al_gecmis",
        "title": "ArthurLegal Masası geçmişi",
        "description": (
            "ArthurLegal Masası'nda yapılan işlerin bu bilgisayardaki geçmişi (%d gün): mevzuat ve kurum kararı "
            "aramaları, getirilen maddeler, içtihat aramaları, atıf teyitleri ve masadan Claude'a gönderilen "
            "istekler, o anki sonuçlarıyla. islem: listele (kategori, ara), getir (id), kaydet (kayit; masa "
            "kullanır), sil (id), temizle. Kullanıcı masada daha önce baktığı bir şeyi sorarsa listele ve getir "
            "ile bakın; kayıttaki sonuç o günkü haldir, güncel hali için kaynağı yeniden sorgulayın. kaydet, sil ve "
            "temizle'yi yalnız kullanıcı isterse çağırın." % GECMIS_GUN),
        "inputSchema": {
            "type": "object",
            "properties": {
                "islem": {"type": "string", "enum": ["listele", "getir", "kaydet", "sil", "temizle"],
                          "default": "listele"},
                "kategori": {"type": "string", "enum": list(GECMIS_KATEGORILER),
                             "description": "listele: yalnız bu tür işler."},
                "ara": {"type": "string", "description": "listele: başlıkta ve adımlarda geçen ifade."},
                "en_fazla": {"type": "integer", "minimum": 1, "maximum": 500, "default": 200},
                "id": {"type": "string", "description": "getir / sil: kaydın kimliği."},
                "kayit": {"type": "object", "description": (
                    "kaydet: {ekran, kategori, tur, baslik, adimlar: [[tamam|uyar|hata, metin]], sorgu, anlik}.")},
            },
        },
        "annotations": {"readOnlyHint": False, "destructiveHint": False, "idempotentHint": False,
                        "openWorldHint": False},
    }


def _katla(s: Any) -> str:
    return str(s or "").translate(_KATLA).lower()


def _kisalt(s: Any, n: int) -> str:
    s = re.sub(r"\s+", " ", str(s or "")).strip()
    return s if len(s) <= n else s[: n - 1] + "…"


class Gecmis:
    """Kayıt başına bir JSON dosyası (<kimlik>.json) ve özetlerin dizini (dizin.json), en yeni önce.

    Kimlik zaman damgasıyla başlar; eskiyen kayıt (``gun``) ve sınırı (``azami``) aşan en eski kayıt her
    yazışta ve listelemede silinir. Yazma geçici dosya + değiştirme ile yapılır: yarım dosya kalmaz.
    """

    def __init__(self, klasor: str, gun: int = GECMIS_GUN, azami: int = GECMIS_AZAMI) -> None:
        self.klasor = klasor
        self.gun = gun
        self.azami = azami
        self._kilit = threading.Lock()

    # ---- dosya ----
    def _yol(self, ad: str) -> str:
        return os.path.join(self.klasor, ad)

    def _yaz(self, ad: str, veri: Any) -> None:
        os.makedirs(self.klasor, exist_ok=True)
        gecici = self._yol(ad + ".yaziliyor")
        with open(gecici, "w", encoding="utf-8") as fh:
            json.dump(veri, fh, ensure_ascii=False, separators=(",", ":"))
        os.replace(gecici, self._yol(ad))

    def _dizin(self) -> List[Dict[str, Any]]:
        try:
            with open(self._yol("dizin.json"), encoding="utf-8") as fh:
                kayitlar = json.load(fh).get("kayitlar")
            if isinstance(kayitlar, list):
                return [k for k in kayitlar if isinstance(k, dict) and _GECMIS_KIMLIK.match(str(k.get("id", "")))]
        except (OSError, ValueError, AttributeError):
            pass
        return self._dizini_kur()

    def _dizini_kur(self) -> List[Dict[str, Any]]:
        """Dizin yoksa ya da bozuksa kayıt dosyalarından yeniden kurulur."""
        out = []
        try:
            adlar = sorted((a for a in os.listdir(self.klasor) if a.endswith(".json") and _GECMIS_KIMLIK.match(a[:-5])),
                           reverse=True)
        except OSError:
            return []
        for ad in adlar:
            try:
                with open(self._yol(ad), encoding="utf-8") as fh:
                    out.append(self._ozet(json.load(fh)))
            except (OSError, ValueError):
                continue
        return out

    @staticmethod
    def _ozet(k: Dict[str, Any]) -> Dict[str, Any]:
        ozet = {a: k.get(a) for a in ("id", "zaman", "ekran", "kategori", "tur", "baslik", "adimlar")}
        ozet["anlik"] = k.get("anlik") is not None
        return ozet

    def _buda(self, dizin: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        sinir = (datetime.now() - timedelta(days=self.gun)).strftime("%Y%m%d-%H%M%S")
        kalan, silinecek = [], []
        for k in dizin:
            (kalan if k["id"][:15] >= sinir and len(kalan) < self.azami else silinecek).append(k)
        for k in silinecek:
            try:
                os.remove(self._yol(k["id"] + ".json"))
            except OSError:
                pass
        return kalan

    # ---- işlemler ----
    def cagir(self, g: Dict[str, Any]) -> Dict[str, Any]:
        islem = g.get("islem") or "listele"
        with self._kilit:
            if islem == "listele":
                return self.listele(g.get("kategori"), g.get("ara"), g.get("en_fazla"))
            if islem == "getir":
                return self.getir(g.get("id"))
            if islem == "kaydet":
                return self.kaydet(g.get("kayit"))
            if islem == "sil":
                return self.sil(g.get("id"))
            if islem == "temizle":
                return self.temizle()
        raise GecmisHatasi("Bilinmeyen işlem: %s (listele, getir, kaydet, sil, temizle)" % islem)

    def listele(self, kategori: Optional[str] = None, ara: Optional[str] = None,
                en_fazla: Optional[int] = None) -> Dict[str, Any]:
        dizin = self._dizin()
        kalan = self._buda(dizin)
        if len(kalan) != len(dizin):
            self._yaz("dizin.json", {"surum": 1, "kayitlar": kalan})
        secili = [k for k in kalan if not kategori or k.get("kategori") == kategori]
        if ara and str(ara).strip():
            q = _katla(ara)
            secili = [k for k in secili if q in _katla(k.get("baslik")) or
                      any(q in _katla(a[1]) for a in (k.get("adimlar") or []) if isinstance(a, list) and len(a) > 1)]
        try:
            n = max(1, min(500, int(en_fazla or 200)))
        except (TypeError, ValueError):
            n = 200
        return {"kayitlar": secili[:n], "toplam": len(secili), "saklama_gun": self.gun}

    def getir(self, kimlik: Any) -> Dict[str, Any]:
        kimlik = str(kimlik or "")
        if not _GECMIS_KIMLIK.match(kimlik):
            raise GecmisHatasi("Geçersiz kayıt kimliği.")
        try:
            with open(self._yol(kimlik + ".json"), encoding="utf-8") as fh:
                return {"kayit": json.load(fh), "saklama_gun": self.gun}
        except FileNotFoundError:
            raise GecmisHatasi("Bu kayıt yok; silinmiş ya da süresi dolmuş olabilir.") from None
        except (OSError, ValueError):
            raise GecmisHatasi("Kayıt okunamadı.") from None

    def kaydet(self, kayit: Any) -> Dict[str, Any]:
        if not isinstance(kayit, dict):
            raise GecmisHatasi("kayit bir nesne olmalı.")
        ekran = str(kayit.get("ekran") or "")
        if ekran not in EKRANLAR or ekran == "uyap":
            raise GecmisHatasi("Bu ekranın işi geçmişe yazılmaz.")
        kategori, tur = kayit.get("kategori"), kayit.get("tur")
        if kategori not in GECMIS_KATEGORILER or tur not in GECMIS_TURLERI:
            raise GecmisHatasi("Bilinmeyen kategori ya da tür.")
        baslik = _kisalt(kayit.get("baslik"), 300)
        if not baslik:
            raise GecmisHatasi("baslik boş olamaz.")
        adimlar = []
        for a in (kayit.get("adimlar") or [])[:10]:
            if isinstance(a, (list, tuple)) and len(a) >= 2 and a[0] in _GECMIS_ADIM:
                adimlar.append([a[0], _kisalt(a[1], 300)])
        sorgu = kayit.get("sorgu")
        if sorgu is not None and (not isinstance(sorgu, dict) or
                                  len(json.dumps(sorgu, ensure_ascii=False)) > _GECMIS_SORGU_SINIRI):
            raise GecmisHatasi("sorgu bir nesne olmalı ve %d karakteri aşmamalı." % _GECMIS_SORGU_SINIRI)
        simdi = datetime.now().astimezone()
        kimlik = simdi.strftime("%Y%m%d-%H%M%S") + "-" + secrets.token_hex(3)
        tam = {"id": kimlik, "zaman": simdi.isoformat(timespec="seconds"), "ekran": ekran, "kategori": kategori,
               "tur": tur, "baslik": baslik, "adimlar": adimlar, "sorgu": sorgu, "anlik": kayit.get("anlik")}
        if len(json.dumps(tam, ensure_ascii=False).encode("utf-8")) > _GECMIS_KAYIT_SINIRI:
            tam["anlik"] = None
            tam["anlik_kesildi"] = True
        onceki = self._dizin()   # kayıt dosyası yazılmadan önce: yeniden kurulan dizin onu iki kez saymasın
        self._yaz(kimlik + ".json", tam)
        dizin = self._buda([self._ozet(tam)] + onceki)
        self._yaz("dizin.json", {"surum": 1, "kayitlar": dizin})
        return {"id": kimlik, "zaman": tam["zaman"], "anlik": tam["anlik"] is not None, "saklama_gun": self.gun}

    def sil(self, kimlik: Any) -> Dict[str, Any]:
        kimlik = str(kimlik or "")
        if not _GECMIS_KIMLIK.match(kimlik):
            raise GecmisHatasi("Geçersiz kayıt kimliği.")
        dizin = self._dizin()
        kalan = [k for k in dizin if k["id"] != kimlik]
        try:
            os.remove(self._yol(kimlik + ".json"))
            silindi = True
        except FileNotFoundError:
            silindi = len(kalan) != len(dizin)
        self._yaz("dizin.json", {"surum": 1, "kayitlar": kalan})
        return {"silindi": silindi}

    def temizle(self) -> Dict[str, Any]:
        n = 0
        try:
            adlar = os.listdir(self.klasor)
        except OSError:
            adlar = []
        for ad in adlar:
            if ad.endswith(".json") and (ad == "dizin.json" or _GECMIS_KIMLIK.match(ad[:-5])):
                try:
                    os.remove(self._yol(ad))
                    n += ad != "dizin.json"
                except OSError:
                    pass
        return {"silinen": n}
