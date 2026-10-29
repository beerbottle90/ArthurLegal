"""Claude dizini denetimi: dizindeki ilanların söylediği hâlâ canlı uçla ve eklentiyle aynı mı. Yalnız standart
kütüphane; haftalık GitHub işi (.github/workflows/dizin-denetimi.yml) koşturur, elle de çalıştırılabilir:

    python tests/dizin_denetimi.py               canlı /directory/mcp ucunu dizin_kaydi.json ile karşılaştırır
    python tests/dizin_denetimi.py --json s.json sonucu JSON olarak da yazar
    python tests/dizin_denetimi.py --kaydet      portaldaki ilan metni güncellendikten sonra kaydı canlı uçtan yeniler

Bağlayıcı ilanının metni (araç sayısı, yargı çevresi, araç adları) depoda değil, claude.ai/directory/manage
portalında durur; kodla birlikte değişmez. Araç eklenir ya da çıkarsa yeniden başvuru gerekmez, ama ilan metni elle
düzenlenir ve inceleyici onaylar. Portalda sürüm alanı yoktur: sunucu sürümü yalnız bilgi olarak yazılır.

Denetlenenler: araç adları kayıttakiyle aynı mı, her araçta dizin kuralları (başlık, readOnlyHint ya da
destructiveHint, en çok 64 karakterlik ad), yargı çevresi sayısı ilanla ve eklentiyle aynı mı, eklentinin bağlantısı
kayıttaki uç mu, eklenti klasörü paketten üretilmiş mi.

Sonuç: her denetim "geçti", "uyarı" ya da "kaldı". En az bir "kaldı" varsa çıkış kodu 1, uç hiç okunamadıysa 2.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Dict, List, Tuple

BURASI = Path(__file__).resolve().parents[1]
KAYIT = BURASI / "tests" / "dizin_kaydi.json"
sys.path.insert(0, str(BURASI / "yayin"))
import eklenti_uret  # noqa: E402

# Yargı çevresi olmayan önekler: tüzel kişi kimliği, doktrin, sözleşme arşivi, durum ve masa
YARGI_DISI = {"gleif", "scholar", "contracts", "status", "al"}
AD_SINIRI = 64

Sonuc = Tuple[str, str, str]   # (durum, denetim, ayrıntı)


def yargi_cevreleri(adlar: List[str]) -> List[str]:
    return sorted({ad.split("_")[0] for ad in adlar} - YARGI_DISI)


def _istek(url: str, govde: dict, oturum: str = "", zaman: int = 60) -> Tuple[dict, str]:
    basliklar = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream",
                 "User-Agent": "arthurlegal-dizin-denetimi"}
    if oturum:
        basliklar["Mcp-Session-Id"] = oturum
    istek = urllib.request.Request(url, data=json.dumps(govde).encode("utf-8"), headers=basliklar, method="POST")
    with urllib.request.urlopen(istek, timeout=zaman) as y:
        ham = y.read().decode("utf-8")
        oturum = y.headers.get("Mcp-Session-Id", oturum)
        if "text/event-stream" in y.headers.get("Content-Type", ""):
            veri = [s[5:].strip() for s in ham.splitlines() if s.startswith("data:")]
            ham = veri[-1] if veri else ""
    return (json.loads(ham) if ham.strip() else {}), oturum


def canli_araclar(url: str, deneme: int = 3) -> Tuple[str, List[dict]]:
    """(sunucu sürümü, araçlar). Fly makinesi uykudan uyanırken ilk istek düşebilir; birkaç kez dener."""
    son = None
    for i in range(deneme):
        try:
            bas, oturum = _istek(url, {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {
                "protocolVersion": "2025-06-18", "capabilities": {},
                "clientInfo": {"name": "arthurlegal-dizin-denetimi", "version": "1"}}})
            try:
                _istek(url, {"jsonrpc": "2.0", "method": "notifications/initialized"}, oturum)
            except (urllib.error.URLError, ValueError):
                pass   # durumsuz sunucu bildirimi yanıtlamayabilir
            araclar, imlec = [], None
            while True:
                yanit, oturum = _istek(url, {"jsonrpc": "2.0", "id": 2, "method": "tools/list",
                                             "params": {"cursor": imlec} if imlec else {}}, oturum)
                araclar += yanit["result"]["tools"]
                imlec = yanit["result"].get("nextCursor")
                if not imlec:
                    break
            return bas["result"]["serverInfo"].get("version", "?"), araclar
        except (urllib.error.URLError, OSError, ValueError, KeyError) as e:
            son = e
            if i + 1 < deneme:
                time.sleep(10)
    raise ConnectionError(str(son))


def karsilastir(kayit: dict, araclar: List[dict]) -> List[Sonuc]:
    """Canlı araç listesini ilan kaydıyla ve dizin kurallarıyla karşılaştırır (ağsız; testler de kullanır)."""
    b = kayit["baglayici"]
    sonuclar: List[Sonuc] = []
    adlar = [a["name"] for a in araclar]
    eklenen, cikan = sorted(set(adlar) - set(b["araclar"])), sorted(set(b["araclar"]) - set(adlar))
    if eklenen or cikan:
        sonuclar.append(("kaldı", "araç listesi", "ilanda %d, canlıda %d araç; eklenen: %s; çıkan: %s. Portaldaki ilan "
                         "metnini (araç sayısı, araç adları) güncelleyin, sonra: python ArthurLegal-setup/tests/"
                         "dizin_denetimi.py --kaydet" % (len(b["araclar"]), len(adlar), ", ".join(eklenen) or "yok",
                                                         ", ".join(cikan) or "yok")))
    else:
        sonuclar.append(("geçti", "araç listesi", "%d araç, ilanla aynı" % len(adlar)))

    kural = []
    for a in araclar:
        notlar = a.get("annotations") or {}
        if not (a.get("title") or notlar.get("title")):
            kural.append("%s: başlık yok" % a["name"])
        if not isinstance(notlar.get("readOnlyHint"), bool) and not isinstance(notlar.get("destructiveHint"), bool):
            kural.append("%s: readOnlyHint/destructiveHint yok" % a["name"])
        if len(a["name"]) > AD_SINIRI:
            kural.append("%s: ad %d karakterden uzun" % (a["name"], AD_SINIRI))
    sonuclar.append(("kaldı", "dizin kuralları", "; ".join(kural)) if kural
                    else ("geçti", "dizin kuralları", "her araçta başlık ve salt okunur/yıkıcı işareti var"))

    cevreler = yargi_cevreleri(adlar)
    if len(cevreler) != b["yargi_cevresi"]:
        sonuclar.append(("kaldı", "yargı çevresi", "ilan %d diyor, canlıda %d önek var (%s). İlan metnini ve "
                         "eklenti_uret.YARGI_CEVRESI'ni güncelleyin" % (b["yargi_cevresi"], len(cevreler),
                                                                       ", ".join(cevreler))))
    else:
        sonuclar.append(("geçti", "yargı çevresi", "%d (%s)" % (len(cevreler), ", ".join(cevreler))))
    return sonuclar


def eklenti_denetimi(kayit: dict) -> List[Sonuc]:
    """Eklentinin söyledikleri bağlayıcı ilanıyla aynı mı ve klasör paketten üretilmiş mi (ağsız)."""
    b = kayit["baglayici"]
    sonuclar: List[Sonuc] = []
    if eklenti_uret.MCP_URL != b["url"]:
        sonuclar.append(("kaldı", "eklenti bağlantısı", "%s, ilan %s" % (eklenti_uret.MCP_URL, b["url"])))
    if eklenti_uret.YARGI_CEVRESI != b["yargi_cevresi"]:
        sonuclar.append(("kaldı", "eklenti yargı çevresi", "eklenti %d, ilan %d"
                         % (eklenti_uret.YARGI_CEVRESI, b["yargi_cevresi"])))
    sorunlar = eklenti_uret.denetle()
    if sorunlar:
        sonuclar.append(("kaldı", "eklenti klasörü", "; ".join(sorunlar[:5]) + ". Çalıştırın: python "
                         "ArthurLegal-setup/yayin/eklenti_uret.py"))
    if not sonuclar:
        sonuclar.append(("geçti", "eklenti", "sürüm %s, ilanla aynı uç ve yargı çevresi, paketle aynı"
                         % eklenti_uret.mevcut_surum()))
    return sonuclar


def kaydet(url: str) -> Dict:
    surum, araclar = canli_araclar(url)
    adlar = sorted(a["name"] for a in araclar)
    eski = json.loads(KAYIT.read_text(encoding="utf-8")) if KAYIT.exists() else {}
    kayit = {k: v for k, v in eski.items() if k not in ("kayit_tarihi", "baglayici")}
    kayit["kayit_tarihi"] = time.strftime("%Y-%m-%d")
    kayit["baglayici"] = {**eski.get("baglayici", {}), "url": url, "sunucu_surumu": surum,
                          "yargi_cevresi": len(yargi_cevreleri(adlar)), "arac_sayisi": len(adlar), "araclar": adlar}
    KAYIT.write_text(json.dumps(kayit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return kayit


def _yaz(durum: str, ad: str, ayrinti: str) -> None:
    print(f"  {durum:<6} {ad}" + (f": {ayrinti}" if ayrinti else ""), flush=True)


def main(argv=None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--json", metavar="DOSYA", help="sonucu JSON olarak da yaz")
    ap.add_argument("--kaydet", action="store_true", help="kaydı canlı uçtan yenile (ilan metni güncellendikten sonra)")
    a = ap.parse_args(argv)
    kayit = json.loads(KAYIT.read_text(encoding="utf-8"))
    url = kayit["baglayici"]["url"]
    if a.kaydet:
        b = kaydet(url)["baglayici"]
        print("Kayıt yenilendi: %d araç, %d yargı çevresi, sunucu %s" % (b["arac_sayisi"], b["yargi_cevresi"],
                                                                        b["sunucu_surumu"]))
        return 0

    print(f"Dizin denetimi: {url}", flush=True)
    sonuclar: List[Sonuc] = []
    try:
        surum, araclar = canli_araclar(url)
    except ConnectionError as e:
        print("UYARI: veri çekilemedi, teyidiniz gerekli: %s (%s)" % (url, e))
        sonuclar.append(("kaldı", "canlı uç", "okunamadı: %s" % e))
        araclar, surum = None, None
    if araclar is not None:
        sonuclar += karsilastir(kayit, araclar)
        eski = kayit["baglayici"].get("sunucu_surumu")
        sonuclar.append(("geçti" if surum == eski else "uyarı", "sunucu sürümü", "%s%s (bilgi; portalda sürüm alanı "
                         "yok)" % (surum, "" if surum == eski else ", kayıtta " + str(eski))))
    sonuclar += eklenti_denetimi(kayit)
    for s in sonuclar:
        _yaz(*s)
    kalan = sum(1 for s in sonuclar if s[0] == "kaldı")
    uyari = sum(1 for s in sonuclar if s[0] == "uyarı")
    print(f"\n{len(sonuclar)} denetim: {len(sonuclar) - kalan - uyari} geçti, {uyari} uyarı, {kalan} kaldı")
    if a.json:
        Path(a.json).write_text(json.dumps([dict(zip(("durum", "denetim", "ayrinti"), s)) for s in sonuclar],
                                           ensure_ascii=False, indent=2), encoding="utf-8")
    if araclar is None:
        return 2
    return 1 if kalan else 0


if __name__ == "__main__":
    sys.exit(main())
