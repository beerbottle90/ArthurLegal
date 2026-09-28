#!/usr/bin/env python3
"""Şablon kümeleme — aynı kalıbın onlarca örneğini bir kez etiketlemek için.

Resmî Gazete başlıkları şablonludur. "154 kV X-Y Enerji İletim Hattı Projesi
Kapsamında Bazı Taşınmazların TEİAŞ Tarafından Acele Kamulaştırılması Hakkında
Karar" kalıbı otuz kez, yalnız güzergâh adı değişerek geçer. Bunları tek tek
etiketlemek hem israf hem de tutarsızlık kaynağıdır: aynı kalıba iki farklı
etiket vermek modele gürültü olarak girer.

Kümeleme, yer adlarını ve sayıları attıktan sonra kalan kelime kümesi üzerinden
Jaccard benzerliğiyle yapılır. Eşik yüksek tutulmuştur (0.82): birleşmeyen
kalır, yanlış birleşen olmaz. Aşırı birleştirme bir etiket hatasını otuz kaleme
yayar; az birleştirmenin bedeli yalnız biraz fazla okumaktır. Asimetri
bilinçlidir.

    python etiket_kumele.py --ozet
    python etiket_kumele.py --parti 0
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

KOK = Path(__file__).resolve().parent
if str(KOK) not in sys.path:
    sys.path.insert(0, str(KOK))

import etiket_hazirla as eh
from jev import katla

KUME_DOSYA = KOK / "fixtures" / "kumeler.json"
ESIK = 0.82
PARTI_BOY = 120

# Kalıbı bozan, kümelemede dikkate alınmayacak parçalar.
_SAYI = re.compile(r"\b\w*\d\w*\b")
_PARANTEZ = re.compile(r"\([^)]*\)")
_NOKTALAMA = re.compile(r"[^\w\s]")


def iskelet(baslik: str) -> Set[str]:
    """Kalıbı taşıyan kelimeler: sayılar, parantezler ve kısa kelimeler atılır.

    Yer adları burada elenmez — eleyecek güvenilir bir liste yok. Onun yerine
    Jaccard eşiği, iki başlığın ORTAK yapısal kelimelerinin baskın olmasını
    şart koşar; birkaç farklı yer adı benzerliği eşiğin altına düşürmez.
    """
    s = _PARANTEZ.sub(" ", baslik)
    s = _SAYI.sub(" ", s)
    s = _NOKTALAMA.sub(" ", katla(s))
    return {k for k in s.split() if len(k) >= 4}


def kirp(baslik: str, bas: int = 115, son: int = 65) -> str:
    """Uzun başlığı iki uçtan gösterir.

    Türkçe Resmî Gazete başlıklarında konu genellikle BAŞTA (neyin düzenlendiği)
    ve SONDA (hangi işlem / hangi kurum) durur; ortası yer adı, ada-parsel ve
    tarih dolgusudur. Tek uçtan kırpmak 'Enerji Piyasası Düzenleme Kurumu
    Tarafından Acele Kamulaştırılması' gibi sondaki kurum bilgisini yutar.
    """
    if len(baslik) <= bas + son + 5:
        return baslik
    return baslik[:bas].rstrip() + " … " + baslik[-son:].lstrip()


def jaccard(a: Set[str], b: Set[str]) -> float:
    if not a or not b:
        return 0.0
    kesisim = len(a & b)
    return kesisim / (len(a) + len(b) - kesisim)


def kumele(kalemler: List[Dict], esik: float = ESIK) -> List[List[int]]:
    """Açgözlü kümeleme. Büyük iskeletten küçüğe; ilk bulunan küme kazanır."""
    iskeletler = [iskelet(k["baslik"]) for k in kalemler]
    sira = sorted(range(len(kalemler)), key=lambda i: -len(iskeletler[i]))
    atanmis = [False] * len(kalemler)
    kumeler: List[List[int]] = []
    for i in sira:
        if atanmis[i]:
            continue
        kume = [i]
        atanmis[i] = True
        for j in sira:
            if atanmis[j]:
                continue
            if jaccard(iskeletler[i], iskeletler[j]) >= esik:
                kume.append(j)
                atanmis[j] = True
        kumeler.append(sorted(kume))
    # Küme numarası, temsilcinin gövde sırasına göre sabitlenir ki parti
    # numaraları çalıştırmalar arasında kaymasın.
    kumeler.sort(key=lambda c: c[0])
    return kumeler


def hazirla() -> Tuple[List[Dict], List[List[int]]]:
    _, _, etiketlenecek = eh.ayir()
    if KUME_DOSYA.exists():
        kayit = json.loads(KUME_DOSYA.read_text(encoding="utf-8"))
        if kayit.get("n") == len(etiketlenecek) and kayit.get("esik") == ESIK:
            return etiketlenecek, kayit["kumeler"]
    kumeler = kumele(etiketlenecek)
    KUME_DOSYA.write_text(json.dumps(
        {"n": len(etiketlenecek), "esik": ESIK, "kumeler": kumeler},
        ensure_ascii=False), encoding="utf-8")
    return etiketlenecek, kumeler


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ozet", action="store_true")
    ap.add_argument("--parti", type=int, default=None)
    ap.add_argument("--boy", type=int, default=PARTI_BOY)
    ap.add_argument("--kume", type=int, default=None, help="tek kümenin üyelerini göster")
    a = ap.parse_args(argv)

    kalemler, kumeler = hazirla()

    if a.kume is not None:
        for i in kumeler[a.kume]:
            print("  %s" % kalemler[i]["baslik"])
        return 0

    if a.ozet or a.parti is None:
        buyuk = sorted(kumeler, key=len, reverse=True)[:12]
        print("Kalem: %d  ->  Küme: %d   (etiketleme yükü %%%.0f azaldı)"
              % (len(kalemler), len(kumeler),
                 100 * (1 - len(kumeler) / len(kalemler))))
        print("Parti: %d × %d" % ((len(kumeler) + a.boy - 1) // a.boy, a.boy))
        print()
        print("En büyük kümeler:")
        for c in buyuk:
            print("  %3d × %.88s" % (len(c), kalemler[c[0]]["baslik"]))
        tek = sum(1 for c in kumeler if len(c) == 1)
        print()
        print("Tek üyeli küme: %d (%%%.0f)" % (tek, 100 * tek / len(kumeler)))
        return 0

    bas = a.parti * a.boy
    dilim = list(enumerate(kumeler))[bas:bas + a.boy]
    if not dilim:
        print("Parti boş.")
        return 1
    print("### KUME PARTI %d  (küme %d-%d / %d)"
          % (a.parti, bas, bas + len(dilim) - 1, len(kumeler)))
    for ki, c in dilim:
        temsilci = kalemler[c[0]]
        etiket = "%d×" % len(c) if len(c) > 1 else "  "
        print("%d|%s|%s|%s" % (ki, etiket, temsilci["bolum"], kirp(temsilci["baslik"])))
    return 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, OSError):
        pass
    raise SystemExit(main())
