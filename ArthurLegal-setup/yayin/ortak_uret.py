#!/usr/bin/env python3
"""Ortak rehberler: birden çok pakete giren rehberlerin tek kaynağı.

Kaynak `ArthurLegal-setup/ortak-rehberler/references/<ad>.md`'dir. Pakete göre değişen yer tutucular (ör. hukuk bürosunda
`[Müvekkil]`, kurumsal pakette `[ŞİRKET ADI]`) kaynakta `{{AL_DEGISKEN}}` biçimindedir; değerleri ve hangi rehberin
hangi pakete girdiği `ortak-rehberler/paketler.json`'dadır. Paketlerdeki kopyalar bu kaynaktan üretilir ve commitlenir;
kurulum paket klasörlerini olduğu gibi okur. Ortak bir rehber düzeltilecekse kaynak düzeltilir ve bu betik
çalıştırılır; paketteki kopyayı elle düzeltmek testte yakalanır.

    python yayin/ortak_uret.py                 kaynaklardan paket kopyalarını yeniden üret
    python yayin/ortak_uret.py --denetle       yalnız denetle: bir kopya kaynaktan farklıysa 1 ile çık
    python yayin/ortak_uret.py --benimse AD..  paketlerdeki kopyalardan kaynak türet; fark yalnız tablodaki
                                               değişkenlerle açıklanabiliyorsa kabul edilir, içerik farkında durur
"""
import argparse
import difflib
import glob
import json
import re
import sys
from pathlib import Path

KOK = Path(__file__).resolve().parents[2]
DEGISKEN = re.compile(r"\{\{AL_([A-Z0-9_]+)\}\}")
TOKEN = re.compile(r"\[[^\]\n]{1,80}\]|`[^`\n]{1,80}`|\w+|\s+|[^\w\s]", re.U)
BOM = "﻿"


class OrtakHata(Exception):
    pass


def ortak_dizini(kok: Path) -> Path:
    return kok / "ArthurLegal-setup" / "ortak-rehberler"


def tablo_oku(kok: Path) -> dict:
    return json.loads((ortak_dizini(kok) / "paketler.json").read_text(encoding="utf-8"))


def paket_rehber_dizini(kok: Path, kalip: str) -> Path:
    bulunan = sorted(glob.glob(str(kok / kalip)))
    if len(bulunan) != 1:
        raise OrtakHata(f"{kalip}: {len(bulunan)} klasör bulundu, 1 bekleniyordu")
    return Path(bulunan[0]) / "knowledge" / "references"


def oku(yol: Path) -> tuple:
    """(BOM'suz ve LF'li metin, BOM var mı, CRLF mi)."""
    ham = yol.read_bytes().decode("utf-8")
    return ham.replace("\r\n", "\n").lstrip(BOM), ham.startswith(BOM), "\r\n" in ham


def uret(sablon: str, degiskenler: dict, paket: str, ad: str = "") -> str:
    def degistir(m):
        deger = degiskenler.get(m.group(1), {}).get(paket)
        if deger is None:
            raise OrtakHata(f"{ad}: {{{{AL_{m.group(1)}}}}} değişkeninin '{paket}' için değeri yok")
        return deger
    return DEGISKEN.sub(degistir, sablon)


def denetle(kok: Path = KOK) -> list:
    """Kaynaktan üretilen metinle paketteki kopya arasındaki farkları listeler (boşsa sorun yok)."""
    t = tablo_oku(kok)
    sorunlar = []
    for ad, paketler in sorted(t["rehberler"].items()):
        kaynak = ortak_dizini(kok) / "references" / ad
        if not kaynak.exists():
            sorunlar.append(f"{ad}: kaynak yok")
            continue
        sablon = oku(kaynak)[0]
        for p in paketler:
            hedef = paket_rehber_dizini(kok, t["paketler"][p]) / ad
            if not hedef.exists():
                sorunlar.append(f"{ad}: {p} paketinde kopya yok")
                continue
            try:
                beklenen = uret(sablon, t["degiskenler"], p, ad)
            except OrtakHata as e:
                sorunlar.append(str(e))
                continue
            if oku(hedef)[0] != beklenen:
                sorunlar.append(f"{ad}: {p} paketindeki kopya kaynaktan farklı")
    kaynaklar = {y.name for y in (ortak_dizini(kok) / "references").glob("*.md")}
    for fazla in sorted(kaynaklar - set(t["rehberler"])):
        sorunlar.append(f"{fazla}: kaynak var ama paketler.json'da yok")
    return sorunlar


def yaz_paketlere(kok: Path = KOK) -> int:
    """Kaynaklardan paket kopyalarını yazar; var olan dosyanın BOM ve satır sonu biçimini korur."""
    t = tablo_oku(kok)
    degisen = 0
    for ad, paketler in sorted(t["rehberler"].items()):
        sablon = oku(ortak_dizini(kok) / "references" / ad)[0]
        for p in paketler:
            hedef = paket_rehber_dizini(kok, t["paketler"][p]) / ad
            metin = uret(sablon, t["degiskenler"], p, ad)
            bom, crlf = (oku(hedef)[1:] if hedef.exists() else (False, False))
            if hedef.exists() and oku(hedef)[0] == metin:
                continue
            cikti = (BOM if bom else "") + (metin.replace("\n", "\r\n") if crlf else metin)
            hedef.write_bytes(cikti.encode("utf-8"))
            degisen += 1
    return degisen


def _isaretle(taban: list, diger: list, taban_p: str, diger_p: str, degiskenler: dict, isaret: dict) -> None:
    """taban ile diger arasındaki her farkı bir değişkenle açıklar; açıklanamayan fark OrtakHata."""
    def degisken_bul(a: str, b: str):
        for ad, degerler in degiskenler.items():
            if degerler.get(taban_p) == a and degerler.get(diger_p) == b:
                return ad
        return None

    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, taban, diger, autojunk=False).get_opcodes():
        if op == "equal":
            continue
        a, b = "".join(taban[i1:i2]), "".join(diger[j1:j2])
        ad = degisken_bul(a, b) if op == "replace" else None
        parcalar = [((i1, i2), ad)] if ad else []
        if not ad and op == "replace" and i2 - i1 == j2 - j1:
            # bitişik birkaç değişken tek öbekte birleşmiş olabilir: belirteç belirteç dene
            for k in range(i2 - i1):
                x, y = taban[i1 + k], diger[j1 + k]
                if x == y:
                    continue
                v = degisken_bul(x, y)
                if not v:
                    parcalar = []
                    break
                parcalar.append(((i1 + k, i1 + k + 1), v))
        if not parcalar:
            raise OrtakHata(f"içerik farkı ({taban_p} / {diger_p}): {a[:60]!r} ile {b[:60]!r}")
        for aralik, v in parcalar:
            if isaret.get(aralik, v) != v:
                raise OrtakHata(f"aynı yer iki ayrı değişkene düşüyor: {a[:60]!r}")
            isaret[aralik] = v


def sablon_turet(metinler: dict, degiskenler: dict, sira: list) -> str:
    """Paket kopyalarından kaynak şablonu türetir ve her paket için birebir geri üretildiğini doğrular."""
    paketler = [p for p in sira if p in metinler]
    taban_p = paketler[0]
    taban = TOKEN.findall(metinler[taban_p])
    if "".join(taban) != metinler[taban_p]:
        raise OrtakHata("metin belirteçlere bölünemedi")
    if "{{AL_" in metinler[taban_p]:
        raise OrtakHata("metin değişken işaretini ({{AL_) zaten içeriyor")
    isaret = {}
    for p in paketler[1:]:
        if metinler[p] != metinler[taban_p]:
            _isaretle(taban, TOKEN.findall(metinler[p]), taban_p, p, degiskenler, isaret)
    araliklar = sorted(isaret)
    for (a1, a2), (b1, _) in zip(araliklar, araliklar[1:]):
        if b1 < a2:
            raise OrtakHata("değişken aralıkları çakışıyor")
    parcalar, konum = [], 0
    for (i1, i2) in araliklar:
        parcalar.append("".join(taban[konum:i1]) + "{{AL_" + isaret[(i1, i2)] + "}}")
        konum = i2
    sablon = "".join(parcalar) + "".join(taban[konum:])
    for p in paketler:
        if uret(sablon, degiskenler, p) != metinler[p]:
            raise OrtakHata(f"{p} için geri üretim tutmadı")
    return sablon


def _alt_kumeler(paketler: list, sira: list) -> list:
    """Denenecek paket kümeleri, büyükten küçüğe: hepsi, sonra sondan birer birer çıkarılarak (en az iki paket)."""
    paketler = [p for p in sira if p in paketler]
    kumeler = []
    for n in range(len(paketler), 1, -1):
        for atilan in _bilesimler([p for p in paketler if p != paketler[0]], len(paketler) - n):
            kume = [p for p in paketler if p not in atilan]
            if kume not in kumeler:
                kumeler.append(kume)
    return kumeler


def _bilesimler(ogeler: list, k: int) -> list:
    if k == 0:
        return [[]]
    return [[ogeler[i]] + geri for i in range(len(ogeler) - 1, -1, -1) for geri in _bilesimler(ogeler[:i], k - 1)]


def benimse(adlar: list, kok: Path = KOK) -> tuple:
    """Verilen rehberler için kaynak türetir ve paketler.json'a yazar. (kabul edilenler, {ad: neden})."""
    t = tablo_oku(kok)
    sira = list(t["paketler"])
    kabul, red = [], {}
    for ad in adlar:
        metinler = {}
        for p, kalip in t["paketler"].items():
            yol = paket_rehber_dizini(kok, kalip) / ad
            if yol.exists():
                metinler[p] = oku(yol)[0]
        if len(metinler) < 2:
            red[ad] = "yalnız bir pakette var"
            continue
        # Önce rehberin bulunduğu bütün paketler denenir. Tutmazsa, metni kendi kitlesine göre yeniden yazılmış
        # paketler (ör. hâkimler için Courthouse) dışarıda bırakılarak daha küçük kümeler denenir; dışarıda kalan
        # paketin kopyası bağımsız kalır.
        sablon, secilen, ilk_hata = None, None, None
        for kume in _alt_kumeler(list(metinler), sira):
            try:
                sablon = sablon_turet({p: metinler[p] for p in kume}, t["degiskenler"], sira)
                secilen = kume
                break
            except OrtakHata as e:
                ilk_hata = ilk_hata or str(e)
        if sablon is None:
            red[ad] = ilk_hata
            continue
        (ortak_dizini(kok) / "references").mkdir(parents=True, exist_ok=True)
        (ortak_dizini(kok) / "references" / ad).write_text(sablon, encoding="utf-8", newline="\n")
        t["rehberler"][ad] = [p for p in sira if p in secilen]
        kabul.append(ad)
    t["rehberler"] = dict(sorted(t["rehberler"].items()))
    (ortak_dizini(kok) / "paketler.json").write_text(json.dumps(t, ensure_ascii=False, indent=2) + "\n",
                                                     encoding="utf-8", newline="\n")
    return kabul, red


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--denetle", action="store_true", help="yalnız denetle, yazma")
    ap.add_argument("--benimse", nargs="+", metavar="AD", help="paket kopyalarından kaynak türet")
    a = ap.parse_args(argv)
    try:
        if a.benimse:
            kabul, red = benimse(a.benimse)
            print(f"kaynağa alındı: {len(kabul)}")
            for ad, neden in sorted(red.items()):
                print(f"  alınmadı: {ad}: {neden}")
            return 0
        if a.denetle:
            sorunlar = denetle()
            for s in sorunlar:
                print(s)
            print("ortak rehberler: " + ("tutarlı" if not sorunlar else f"{len(sorunlar)} sorun"))
            return 1 if sorunlar else 0
        print(f"yeniden üretilen kopya: {yaz_paketlere()}")
        return 0
    except OrtakHata as e:
        print(f"hata: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
