"""ArthurLegal arayüzü (MCP Apps): görünümleri birleştirir, masa aracını tanımlar.

Uzak uç (arthurlegal-mcp) ve yerel AL sunucusu (arthurlegal-yerel) aynı modülü kullanır; ikisi de
yalnız standart kütüphaneyle çalışır.

    from al_arayuz import kaynaklar, arac_meta, masa_araci, masa_cevabi

- ``kaynaklar()``: her ``ui://`` görünümü, MCP ``resources/list`` ve ``resources/read`` için.
- ``arac_meta(ad)``: aracın görünümü varsa ``_meta``; host o aracın sonucunu görünümle çizer.
- ``masa_araci()``: ``al_masasi`` aracının tanımı. Cevabı ``masa_cevabi(...)`` kurar.

Görünümler ``ortak/gorunumler/*.html`` şablonlarıdır. Ortak tasarım ve kod tek geçişte gömülür:
``/*AL:CSS*/`` ``/*AL:JS*/`` ``/*AL:KARTLAR*/`` ``/*AL:ATIF*/`` ``<!--AL:ARMA-->`` ``<!--AL:DONNA-->``.
Gömülen içerik yeniden taranmaz; bir dosyanın kendi yorumunda yer tutucu adı geçse de bozulmaz.
"""
from __future__ import annotations

import os
import re
from typing import Any, Dict, List, Optional

SURUM = "3.0.1"

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
    "ARMA": ("tasarim", "arma.svg"),
    "DONNA": ("tasarim", "donna.svg"),
}
_YER_TUTUCU = re.compile(r"/\*AL:([A-Z]+)\*/|<!--AL:([A-Z]+)-->")

# Masanın ekranları; al_masasi(bolum=...) bunlardan biriyle açılır.
EKRANLAR = ("sohbet", "mevzuat", "ictihat", "tapu", "beyin", "mask", "uyap", "donna", "mcp")


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
                "bildirir; masa kendi başına ne gönderir ne yazar."),
    }
    if bolum in EKRANLAR:
        out["bolum"] = bolum
    return out
