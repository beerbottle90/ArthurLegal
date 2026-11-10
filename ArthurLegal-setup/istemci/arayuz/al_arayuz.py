"""ArthurLegal arayüzü (MCP Apps): görünümleri birleştirir, masa aracını tanımlar.

Uzak uç (arthurlegal-mcp) ve yerel AL sunucusu (arthurlegal-yerel) aynı modülü kullanır; ikisi de
yalnız standart kütüphaneyle çalışır.

    from al_arayuz import kaynaklar, arac_meta, masa_araci, masa_cevabi

- ``kaynaklar()``: her ``ui://`` görünümü, MCP ``resources/list`` ve ``resources/read`` için.
- ``arac_meta(ad)``: aracın ``_meta``'sı. Masanın iç araçları dışında her araç masayı açar: Claude masada çalışırken
  her adım masada canlı görünür; masa açılmamış sohbette aynı görünüm kart ya da tek satırlık adım şerididir.
  ``kart_meta(ad)``: eski kart eşlemesi (yalnız madde ve içtihat), Claude dizini profili için.
- ``masa_araci()``: ``al_masasi`` aracının tanımı. Cevabı ``masa_cevabi(...)`` kurar.
- ``baslangic_araci()``: ``al_masada_basla``; Claude soruyu alır almaz masaya yazar, masa çalışmayı başlatır.
- ``teslim_araci()``: ``al_masaya_yaz``; Claude sohbet kutusuna yazılan sorunun cevabını masaya teslim eder.
  Cevabı ``teslim_cevabi(girdi, masa)`` kurar; masa cevabı araç girdisinden (yazıldıkça) okur, sunucu saklamaz.
- ``gecmis_araci()`` ve ``Gecmis(klasor)``: masa geçmişi (``al_gecmis``). Yalnız yerel AL sunucusu klasör
  verir; uzak uç geçmiş tutmaz, masa orada oturumluk listeyle çalışır.

Görünümler ``ortak/gorunumler/*.html`` şablonlarıdır. Ortak tasarım ve kod tek geçişte gömülür:
``/*AL:CSS*/`` ``/*AL:JS*/`` ``/*AL:KARTLAR*/`` ``/*AL:ATIF*/`` ``/*AL:ISTEK*/`` ``/*AL:MD*/`` ``<!--AL:ARMA-->``
``<!--AL:DONNA-->``.
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

SURUM = "3.1.0"

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

MASA_URI = "ui://arthurlegal/masa.html"
# Claude Desktop'ın tam ekran bölmesi her zaman en son açılan görünümü gösterir. Bir aracın kendi kartı olsaydı masanın
# yerine geçerdi; bu yüzden bütün araçlar masayı açar ve masa her çağrıyı Sohbet ekranında bir adım olarak çizer.
# Masanın kendi çağırdığı iç araçlar görünüm açmaz.
GORUNUMSUZ = frozenset({"al_gecmis", "al_modul_ac"})
# Eski kartlar: Claude dizini profili (talimatsız, masasız) yalnız bu iki aracı kartla gösterir.
KART_GORUNUMU = {
    "tr_mevzuat_madde_getir": "ui://arthurlegal/madde-karti.html",
    "tr_ictihat_ara": "ui://arthurlegal/ictihat-karti.html",
}

_PARCALAR = {
    "CSS": ("tasarim", "al.css"),
    "JS": ("tasarim", "al.js"),
    "KARTLAR": ("tasarim", "kartlar.js"),
    "ATIF": ("tasarim", "atif.js"),
    "ISTEK": ("tasarim", "istek.js"),
    "MD": ("tasarim", "md.js"),
    "ARMA": ("tasarim", "arma.svg"),
    "DONNA": ("tasarim", "donna.svg"),
}
_YER_TUTUCU = re.compile(r"/\*AL:([A-Z]+)\*/|<!--AL:([A-Z]+)-->")

# Masanın ekranları; al_masasi(bolum=...) bunlardan biriyle açılır.
EKRANLAR = ("sohbet", "mevzuat", "ictihat", "hesap", "gecmis", "tapu", "beyin", "mask", "uyap", "donna", "mcp")


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


def _meta(uri: str) -> Dict[str, Any]:
    # Düz "ui/resourceUri" anahtarı, bazı ev sahiplerinin hâlâ okuduğu eski yazım.
    return {"ui": {"resourceUri": uri}, "ui/resourceUri": uri}


def arac_meta(arac: str) -> Optional[Dict[str, Any]]:
    """Masanın iç araçları dışında her araç masayı açar."""
    if not arac or arac in GORUNUMSUZ:
        return None
    return _meta(MASA_URI)


def kart_meta(arac: str) -> Optional[Dict[str, Any]]:
    """Masasız profil (Claude dizini) için eski kartlar: yalnız madde ve içtihat."""
    uri = KART_GORUNUMU.get(arac)
    return _meta(uri) if uri else None


# Claude Desktop'ta aynı sohbette iki masa olabilir: bilgisayardaki kurulumun (arthurlegal-yerel) ve uzak bağlayıcının
# (arthurlegal-mcp). Beyin, ArthurMask ve UYAP yalnız yereldeki masada çalışır; açıklama Claude'u ona yönlendirir.
MASA_ORTAM_NOTU = {
    "masaustu": (" Bu, bilgisayardaki ArthurLegal kurulumunun masasıdır: Beyin, ArthurMask ve UYAP Dashboard burada "
                 "çalışır. Sohbette uzak arthurlegal-mcp bağlayıcısı da varsa masayı bu araçla açın."),
    "uzak": (" Bu bilgisayarda ArthurLegal kuruluysa (sohbette arthurlegal-yerel sunucusu bağlıysa) masayı onun "
             "al_masasi aracıyla açın: sorgu geçmişi, Beyin, ArthurMask ve UYAP Dashboard yalnız oradaki masada "
             "çalışır. Bu masa web ve telefon içindir; arthurlegal-yerel bağlıyken çağrılırsa masayı açmaz, sizi "
             "oradaki masaya yönlendirir."),
}

# Uzak bağlayıcının masası geçmişi saklayamaz: Claude masa pencerelerine her sohbette yeni bir tarayıcı deposu verir
# (10.11.2026 ölçümü: 14 günde 29 ayrı köken), uzak uç da hiçbir sorguyu saklamaz. Kalıcı geçmiş yalnız bilgisayardaki
# kurulumun diskindedir. İki masa aynı sohbetteyken hangisinin açılacağı modelin seçimine bırakılmaz: kararı uzak uç
# verir, arthurlegal-yerel bağlıysa masayı açmaz, Claude'u oraya gönderir.
#
# "Bağlı" olmak yetmeyebilir: Claude Desktop'ta bir sunucunun araçları tek tek kapatılabilir ve kapalı kalır
# (10.11.2026: bir bilgisayarda arthurlegal-yerel bağlı, 127 aracından 119'u, al_masasi dahil, 02.11'den beri kapalıydı;
# masa bu yüzden hep uzaktan açılmıştı). Klasik arayüz kurulumunda da yerelde masa yoktur. Devir bu durumda çıkmaza
# girmemeli: not Claude'a masayı uzakta_kal=true ile burada açmasını söyler, masa da aynı sohbette ikinci kez
# devretmez (masa.html DEVIR_KAYDI) ve kullanıcıya araç menüsünü gösterir.
YEREL_SUNUCU = "arthurlegal-yerel"
_YEREL_SUNUCU = re.compile(r"arthur\s*legal[\s_()-]*yerel")
UZAK_ARAC_NOTU = (" Masa bu sohbette arthurlegal-yerel sunucusundan açıldıysa bu aracı değil, o sunucudaki aynı adlı "
                  "aracı çağırın.")
YONLENDIRME_NOTU = (
    "Masa bu bağlantıdan AÇILMADI: bu bilgisayarda ArthurLegal kurulu (arthurlegal-yerel bağlı). Şimdi, kullanıcıya "
    "bir şey sormadan, arthurlegal-yerel sunucusunun al_masasi aracını aynı bolum ve baglayicilar ile çağırın; bu "
    "sohbette al_masada_basla, araştırma araçları ve al_masaya_yaz için de arthurlegal-yerel sunucusunu kullanın. "
    "Sorgu geçmişi, Beyin, ArthurMask ve UYAP Dashboard yalnız oradaki masada çalışır. arthurlegal-yerel'in "
    "al_masasi aracı araç listenizde YOKSA (sunucu bağlı olsa da araçları kapalı olabilir) beklemeyin ve kullanıcıya "
    "sormayın: hemen bu aracı uzakta_kal=true ile yeniden çağırın, sonra kullanıcıya tek cümleyle şunu söyleyin: "
    "Claude'un araç menüsünde arthurlegal-yerel'in araçları kapalı olabilir; açınca masa bu bilgisayardan açılır ve geçmiş kalıcı olur.")
YEREL_KAPALI_NOTU = (
    " arthurlegal-yerel bağlı ama masa bu uzak bağlantıdan açıldı. Oradaki al_masasi aracı araç listenizde olmadığı "
    "için buradan açtıysanız kullanıcıya tek cümleyle söyleyin: Claude'un araç menüsünde arthurlegal-yerel'in araçları kapalı olabilir; açınca masa bu bilgisayardan açılır ve geçmiş kalıcı olur.")


def yerel_bagli(baglayicilar: Any) -> bool:
    """Claude'un bildirdiği listede bilgisayardaki kurulum (arthurlegal-yerel) bağlı mı."""
    return any(o["durum"] == "bagli" and _YEREL_SUNUCU.search(o["ad"].lower())
               for o in baglayicilari_duzenle(baglayicilar))


def masa_araci(ortam: Optional[str] = None) -> Dict[str, Any]:
    """ortam: "masaustu" (yerel AL sunucusu), "uzak" (arthurlegal-mcp) ya da "dizin" (Claude dizini profili: teslim
    aracı yok, yönlendirme yok). Verilmezse ortam notu eklenmez."""
    teslim = "" if ortam == "dizin" else (
        " Masa açıldıktan sonra bu sohbetteki her soruda: önce al_masada_basla, sonra araştırma, en son al_masaya_yaz.")
    tanim = _masa_tanimi(ortam, teslim)
    if ortam == "uzak":
        # Yönlendirme kararı listeye bakar: uzak uçta liste zorunludur (bilinmiyorsa boş liste).
        sema = tanim["inputSchema"]
        sema["properties"]["baglayicilar"]["description"] += (
            " arthurlegal-yerel bağlıysa mutlaka yazın: masa o zaman bu bilgisayardaki kurulumdan açılır.")
        sema["properties"]["uzakta_kal"] = {
            "type": "boolean", "default": False,
            "description": ("Yalnız şu iki durumda true: arthurlegal-yerel sunucusunun al_masasi aracı araç "
                            "listenizde yoksa (sunucu bağlı olsa da araçları kapalı olabilir) ya da kullanıcı masayı "
                            "açıkça bu uzak bağlantıdan istiyorsa.")}
        sema["required"] = ["baglayicilar"]
    return tanim


def _masa_tanimi(ortam: Optional[str], teslim: str) -> Dict[str, Any]:
    return {
        "name": "al_masasi",
        "title": "ArthurLegal Masası",
        "description": (
            "ArthurLegal Masası'nı açar: mevzuat ve atıf teyidi, içtihat, ArthurTapu, Beyin (hafıza), "
            "ArthurMask, UYAP Dashboard, Donna ve kaynak durumu tek panelde. Kullanıcı 'ArthurLegal'i aç', "
            "'masayı aç', 'AL Masası' ya da bir modülün adını söyleyip onu açmak istediğinde çağırın. "
            "bolum ile belirli bir ekranda açılır. Her açılışta baglayicilar'ı doldurun: masa MCP'ler ve Donna "
            "ekranlarında kullanıcının bağlı sunucularını gösterir ve bunu yalnız sizden öğrenebilir."
            + MASA_ORTAM_NOTU.get(ortam or "", "") + teslim
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "bolum": {"type": "string", "enum": list(EKRANLAR),
                          "description": "Açılış ekranı; boşsa sohbet."},
                "tam_ekran": {"type": "boolean", "default": True,
                              "description": "Masa tam ekran açılmayı istesin mi."},
                "baglayicilar": {
                    "type": "array", "maxItems": BAGLAYICI_AZAMI,
                    "description": (
                        "Bu sohbette erişebildiğiniz MCP sunucuları ve Claude bağlayıcıları (Gmail, Google Calendar, "
                        "Slack, Notion, arthurlegal-yerel, arthur-mask ...): her sunucu bir kez, araç adı değil sunucunun "
                        "adı. Giriş isteyen ya da "
                        "hata veren sunucuyu o durumla yazın. Bilmiyorsanız boş liste verin, uydurmayın."),
                    "items": {
                        "type": "object",
                        "properties": {
                            "ad": {"type": "string"},
                            "durum": {"type": "string", "enum": list(BAGLAYICI_DURUMLARI), "default": "bagli"},
                        },
                        "required": ["ad"],
                    },
                },
            },
        },
        "annotations": {"readOnlyHint": True, "destructiveHint": False, "openWorldHint": False},
    }


# Claude'un bildirdiği bağlı sunucular (MCP'ler ekranı). Masa bu listeyi ev sahibinden alamaz, yalnız Claude bilir.
BAGLAYICI_AZAMI = 60
BAGLAYICI_DURUMLARI = ("bagli", "giris-gerekli", "hata")


def baglayicilari_duzenle(liste: Any) -> List[Dict[str, str]]:
    """Tekil ad (büyük/küçük harf ve Türkçe harf farkı gözetilmez), bilinen durum, sınırlı uzunluk; bozuk öğe atlanır."""
    out: List[Dict[str, str]] = []
    gorulen = set()
    for o in liste if isinstance(liste, list) else []:
        if isinstance(o, str):
            o = {"ad": o}
        if not isinstance(o, dict):
            continue
        ad = _kisalt(o.get("ad"), 80)
        if not ad or _katla(ad) in gorulen:
            continue
        gorulen.add(_katla(ad))
        out.append({"ad": ad, "durum": o.get("durum") if o.get("durum") in BAGLAYICI_DURUMLARI else "bagli"})
        if len(out) >= BAGLAYICI_AZAMI:
            break
    return out


# Masa açıkken sohbet kaydı masanın arkasında kalır: kullanıcı soruyu, çalışmayı ve cevabı ancak masada görür. Kural
# masanın bir notuna bağlı değildir (Claude Desktop o notu modele iletmeyebiliyor): masa bir kez açıldıysa geçerlidir.
TESLIM_KURALI = (
    "Bu sohbette ArthurLegal Masası açıldıysa (al_masasi çağrıldıysa) bundan sonraki her soruda şu sırayı izleyin: "
    "1) hemen al_masada_basla ile soruyu masaya yazın; 2) araştırın (her aracın adımı masada canlı görünür); "
    "3) cevabı al_masaya_yaz ile teslim edin. Cevabı sohbete ayrıca yazmayın, sohbete yalnız 'Cevap masada.' yazın.")


def masa_cevabi(ortam: str, yetenekler: List[str], moduller: Dict[str, Dict[str, str]],
                bolum: Optional[str] = None, baglayicilar: Any = None, yerele_devret: bool = False) -> Dict[str, Any]:
    """al_masasi'nin cevabı: masa neyin çalıştığını buradan bilir.

    ortam: "masaustu" (yerel AL sunucusu) ya da "uzak" (web ve telefon).
    moduller: {"tapu": {"durum": "hazir" | "claude" | "masaustu" | "kurulu-degil"}, ...}
    baglayicilar: Claude'un bildirdiği bağlı sunucular (al_masasi girdisi); verilmediyse alan yok.
    yerele_devret: uzak uç, listede arthurlegal-yerel bağlıysa masayı açmaz; cevap "yonlendir" taşır ve not Claude'u
        bilgisayardaki masaya gönderir (çağıran, kullanıcı uzakta_kal demediyse True verir). Claude dizini profili
        vermez: orada araç başka sunucuya yönlendirmez.
    """
    out: Dict[str, Any] = {
        "surum": SURUM,
        "ortam": ortam,
        "yetenekler": sorted(set(yetenekler)),
        "moduller": moduller,
        "not": "Masa açıldı. Kullanıcı masada çalışırken yaptığı işi size ArthurLegal Masası notlarıyla bildirir.",
    }
    # Teslim aracı olmayan uçta (Claude dizini profili) kural söylenmez; cevap sohbette kalır.
    if "al_masaya_yaz" in out["yetenekler"]:
        out["not"] = "Masa açıldı. " + TESLIM_KURALI + out["not"][len("Masa açıldı."):]
    if baglayicilar is not None:
        out["baglayicilar"] = baglayicilari_duzenle(baglayicilar)
    if "al_gecmis" in out["yetenekler"]:
        out["not"] += (" Masadaki işlerin geçmişi (%d gün, o anki sonuçlarıyla) bu bilgisayarda tutulur; kullanıcı "
                       "masada daha önce baktığı bir şeyi sorarsa al_gecmis ile bakabilirsiniz." % GECMIS_GUN)
    if bolum in EKRANLAR:
        out["bolum"] = bolum
    if ortam == "uzak" and yerel_bagli(baglayicilar):
        if yerele_devret:
            out["yonlendir"] = {"sunucu": YEREL_SUNUCU, "arac": "al_masasi"}
            out["not"] = YONLENDIRME_NOTU
        elif "al_masaya_yaz" in out["yetenekler"]:   # ana uç; dizin profili başka sunucudan söz etmez
            out["not"] += YEREL_KAPALI_NOTU
    return out


# --------------------------------------------------------------------------- soru, çalışma ve cevap masada
# Masa yalnız kendi aracının girdisini görür; sohbete yazılan soruyu ve cevabı okuyamaz. Claude soruyu al_masada_basla
# ile yazar, araştırırken her araç masayı açar (adım), cevabı al_masaya_yaz ile verir; ev sahibi her çağrıda masayı yeni
# bir pencerede açar ve pencereler çalışmayı bu kaynağın tarayıcı deposunda paylaşır. Sunucu hiçbirini saklamaz.
class TeslimHatasi(ValueError):
    """Eksik ya da bozuk teslim; çağıran isError olarak döndürür."""


def baslangic_araci(ortam: Optional[str] = None) -> Dict[str, Any]:
    tanim = _baslangic_tanimi()
    if ortam == "uzak":
        tanim["description"] += UZAK_ARAC_NOTU
    return tanim


def _baslangic_tanimi() -> Dict[str, Any]:
    return {
        "name": "al_masada_basla",
        "title": "Soruyu ArthurLegal Masası'na yaz",
        "description": (
            "ArthurLegal Masası bu sohbette açıldıysa (al_masasi çağrıldıysa) kullanıcının her yeni sorusunda İLK iş "
            "bunu çağırın: masa soruyu ve 'Claude çalışıyor'u hemen gösterir, ardından yaptığınız her araç çağrısı masada "
            "canlı bir adım olur. Araştırmayı bitirince cevabı al_masaya_yaz ile teslim edin. Masa açılmadıysa çağırmayın."),
        "inputSchema": {
            "type": "object",
            "properties": {"soru": {"type": "string", "description": "Kullanıcının sorusu, kendi sözleriyle."}},
            "required": ["soru"],
        },
        "annotations": {"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True,
                        "openWorldHint": False},
    }


def baslangic_cevabi(girdi: Dict[str, Any], masa: Dict[str, Any]) -> Dict[str, Any]:
    """al_masada_basla'nın cevabı: masanın durumu (Sohbet ekranında) ve sıradaki adımın hatırlatması."""
    soru = girdi.get("soru")
    if not isinstance(soru, str) or not soru.strip():
        raise TeslimHatasi("soru boş olamaz: kullanıcının sorusunu yazın.")
    out = dict(masa)
    out["bolum"] = "sohbet"
    out["basla"] = {"soru": _kisalt(soru, 200)}
    out["not"] = ("Soru masada. Şimdi araştırın (her araç çağrısı masada adım olarak görünür); bitince cevabı "
                  "al_masaya_yaz ile teslim edin ve sohbete yalnız 'Cevap masada.' yazın.")
    return out


def teslim_araci(ortam: Optional[str] = None) -> Dict[str, Any]:
    tanim = _teslim_tanimi()
    if ortam == "uzak":
        tanim["description"] += UZAK_ARAC_NOTU
    return tanim


def _teslim_tanimi() -> Dict[str, Any]:
    # Özellik sırası akışı belirler: soru ve adımlar cevaptan önce yazılır, masa onları önce gösterir.
    adim = {"type": "object", "properties": {
        "durum": {"type": "string", "enum": list(_GECMIS_ADIM), "default": "tamam"},
        "metin": {"type": "string"}}, "required": ["metin"]}
    kaynak = {"type": "object", "properties": {
        "baslik": {"type": "string"},
        "atif": {"type": "string", "description": "Araç yanıtındaki citation, birebir."},
        "url": {"type": "string", "description": "Araç yanıtındaki source_url, birebir; yoksa boş."}},
        "required": ["baslik"]}
    return {
        "name": "al_masaya_yaz",
        "title": "Cevabı ArthurLegal Masası'na yaz",
        "description": (
            "ArthurLegal Masası bu sohbette açıldıysa (al_masasi çağrıldıysa) kullanıcının sorusuna verdiğiniz cevabı "
            "masaya teslim eder. Masa cevabı Sohbet ekranında, yaptığınız adımlar ve kaynaklarla gösterir; cevaptaki "
            "kanun maddesi atıflarını resmî metinden kendisi teyit eder. Soruyu önce al_masada_basla ile yazın, "
            "araştırmayı bitirince bunu bir kez çağırın; cevabı sohbete ayrıca yazmayın, sohbete yalnız 'Cevap masada.' "
            "yazın. Masa açılmadıysa çağırmayın, cevabı sohbette verin."),
        "inputSchema": {
            "type": "object",
            "properties": {
                "soru": {"type": "string", "description": "Kullanıcının sorusu, kendi sözleriyle."},
                "adimlar": {"type": "array", "items": adim, "maxItems": 30, "description": (
                    "Cevabı hazırlarken yaptıklarınız, sırayla ve kısa: hangi kaynağa baktınız, ne buldunuz "
                    "(ör. 'TBK m. 344 resmî metinden getirildi', 'Yargıtay'da 12 karar tarandı, 3'ü ilgili'). "
                    "Veri çekilemeyen adım hata ya da uyar.")},
                "cevap": {"type": "string", "description": (
                    "Cevabın tamamı, Markdown: ## başlık, madde işaretli ve numaralı liste, **kalın**, tablo, > alıntı. "
                    "Atıfları araç yanıtındaki citation ile birebir yazın; veri çekilemediyse UYARI satırını koyun.")},
                "kaynaklar": {"type": "array", "items": kaynak, "maxItems": 40, "description": (
                    "Dayandığınız mevzuat ve kararlar. Bağlantı uydurmayın.")},
            },
            "required": ["soru", "cevap"],
        },
        "annotations": {"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True,
                        "openWorldHint": False},
    }


def teslim_cevabi(girdi: Dict[str, Any], masa: Dict[str, Any], gecmis: Optional["Gecmis"] = None) -> Dict[str, Any]:
    """al_masaya_yaz'ın cevabı: masanın durumu (masa_cevabi, Sohbet ekranında) ve kısa teslim özeti.

    Cevap metni geri yazılmaz: masa onu araç girdisinden okur, Claude'un bağlamı ikinci kez dolmaz.
    gecmis: yerel sunucunun geçmiş deposu. Verilirse cevap teslim anında (girdi doğrulandıktan sonra) diske yazılır
        ve kaydın kimliği teslim.gecmis_id ile döner; masa atıf teyidini bitirince aynı kaydı tamamlar, ikinci kayıt
        açmaz. Uzak uç vermez: orada hiçbir sorgu saklanmaz.
    """
    soru, cevap = girdi.get("soru"), girdi.get("cevap")
    if not isinstance(cevap, str) or not cevap.strip():
        raise TeslimHatasi("cevap boş olamaz: cevabın tamamını Markdown olarak yazın.")
    if soru is not None and not isinstance(soru, str):
        raise TeslimHatasi("soru metin olmalı.")
    for alan in ("adimlar", "kaynaklar"):
        if girdi.get(alan) is not None and not isinstance(girdi.get(alan), list):
            raise TeslimHatasi("%s bir liste olmalı." % alan)
    out = dict(masa)
    out["bolum"] = "sohbet"
    out["teslim"] = {"soru": _kisalt(soru, 200), "karakter": len(cevap),
                     "adim": len(girdi.get("adimlar") or []), "kaynak": len(girdi.get("kaynaklar") or [])}
    kimlik = gecmis.cevap_kaydet(girdi) if gecmis is not None else None
    if kimlik:
        out["teslim"]["gecmis_id"] = kimlik
    out["not"] = ("Cevap masada gösterildi. Sohbete yalnız 'Cevap masada.' yazın, cevabı yinelemeyin. Masa cevaptaki "
                  "madde atıflarını resmî metinden teyit eder; doğrulanamayan atıf olursa bir sonraki mesajda masa "
                  "notuyla bildirir.")
    return out


# --------------------------------------------------------------------------- masa geçmişi
# Masada yapılan iş (arama, madde, içtihat, atıf teyidi, Claude'a giden istek) o anki sonucuyla birlikte
# yalnız bu bilgisayarda tutulur. Atıf teyidinde yapıştırılan metin değil, yalnız bulunan atıflar gelir;
# UYAP işi hiç yazılmaz. Günlüğe sorgu metni yazılmaz.
GECMIS_GUN = 90
GECMIS_AZAMI = 2000
GECMIS_KATEGORILER = ("mevzuat", "ictihat", "atif", "claude")
GECMIS_TURLERI = ("mevzuat-liste", "kurum", "madde", "atif", "ictihat", "claude", "cevap")
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
            "aramaları, getirilen maddeler, içtihat aramaları, atıf teyitleri, masadan Claude'a gönderilen "
            "istekler ve masaya teslim edilen cevaplar, o anki sonuçlarıyla. islem: listele (kategori, ara), getir (id), kaydet (kayit; masa "
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
        zaman = simdi.isoformat(timespec="seconds")
        # Kimlik var olan bir kaydı gösteriyorsa o kayıt tamamlanır (teslim anında yazılan cevaba masanın atıf teyidi
        # eklenir): kimlik, zaman ve listedeki yeri değişmez. Bilinmeyen kimlik yok sayılır, yeni kayıt açılır.
        eski = str(kayit.get("id") or "")
        var_olan = None
        if _GECMIS_KIMLIK.match(eski):
            try:
                with open(self._yol(eski + ".json"), encoding="utf-8") as fh:
                    var_olan = json.load(fh)
            except (OSError, ValueError):
                var_olan = None
        if isinstance(var_olan, dict):
            kimlik, zaman = eski, str(var_olan.get("zaman") or zaman)
        tam = {"id": kimlik, "zaman": zaman, "ekran": ekran, "kategori": kategori,
               "tur": tur, "baslik": baslik, "adimlar": adimlar, "sorgu": sorgu, "anlik": kayit.get("anlik")}
        if len(json.dumps(tam, ensure_ascii=False).encode("utf-8")) > _GECMIS_KAYIT_SINIRI:
            tam["anlik"] = None
            tam["anlik_kesildi"] = True
        onceki = self._dizin()   # kayıt dosyası yazılmadan önce: yeniden kurulan dizin onu iki kez saymasın
        self._yaz(kimlik + ".json", tam)
        if isinstance(var_olan, dict) and any(k["id"] == kimlik for k in onceki):
            dizin = self._buda([self._ozet(tam) if k["id"] == kimlik else k for k in onceki])
            self._yaz("dizin.json", {"surum": 1, "kayitlar": dizin})
            return {"id": kimlik, "zaman": zaman, "anlik": tam["anlik"] is not None, "saklama_gun": self.gun,
                    "tamamlandi": True}
        dizin = self._buda([self._ozet(tam)] + [k for k in onceki if k["id"] != kimlik])
        self._yaz("dizin.json", {"surum": 1, "kayitlar": dizin})
        return {"id": kimlik, "zaman": tam["zaman"], "anlik": tam["anlik"] is not None, "saklama_gun": self.gun}

    def cevap_kaydet(self, girdi: Dict[str, Any]) -> Optional[str]:
        """al_masaya_yaz'ın girdisi teslim anında geçmişe yazılır; kaydın kimliği döner, yazılamadıysa None.

        Kalıcılık masanın penceresine bağlı kalmaz: pencere atıf teyidi bitmeden kapansa da cevap geçmiştedir.
        Masa teyidi bitirince aynı kimlikle kaydet çağırır ve kaydı araç adımları ve teyit sonucuyla tamamlar.
        Biçim masanın yazdığıyla aynıdır; teyit henüz yapılmadığı için "teyit" yoktur (None).
        """
        cevap = girdi.get("cevap")
        if not isinstance(cevap, str) or not cevap.strip():
            return None
        soru = _kisalt(girdi.get("soru") if isinstance(girdi.get("soru"), str) else "", 300)
        adimlar = []
        for a in girdi.get("adimlar") if isinstance(girdi.get("adimlar"), list) else []:
            if isinstance(a, dict) and isinstance(a.get("metin"), str) and a["metin"].strip():
                adimlar.append([a.get("durum") if a.get("durum") in _GECMIS_ADIM else "tamam", a["metin"].strip()])
        kaynaklar = []
        for k in girdi.get("kaynaklar") if isinstance(girdi.get("kaynaklar"), list) else []:
            if not isinstance(k, dict):
                continue
            baslik, atif, url = (str(k.get(a) or "").strip() for a in ("baslik", "atif", "url"))
            if baslik or atif:
                kaynaklar.append({"baslik": baslik, "atif": atif,
                                  "url": url if re.match(r"^https?://\S+$", url, re.I) else ""})
        kayit = {"ekran": "sohbet", "kategori": "claude", "tur": "cevap", "baslik": soru or "Claude'un cevabı",
                 "adimlar": adimlar[:10] or [["tamam", "Cevap masaya geldi"]],
                 "sorgu": {"metin": soru} if soru else None,
                 "anlik": {"cevap": cevap, "adimlar": adimlar, "araclar": [], "kaynaklar": kaynaklar, "teyit": None}}
        try:
            with self._kilit:
                return self.kaydet(kayit)["id"]
        except (GecmisHatasi, OSError):
            return None

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
