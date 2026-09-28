#!/usr/bin/env python3
"""Jev'i geniş bir dilimde koşturur ve olasılıklarının ne anlama geldiğini ölçer.

Altın küme 56 kalem — eşik seçmek için fazla küçük. Bu betik etiketli 938 küme
temsilcisinde Jev'i koşturur ve güvenilirlik diyagramı, ECE (gürültü tabanıyla),
yeniden uydurulan sıcaklık ve eşik süpürmesi çıkarır.

═══════════════════════════════════════════════════════════════════════════
ÖLÇÜMÜN SINIRI — önce bunu okuyun:

Buradaki etiketler ALTIN DEĞİL. Opus damıtmasıyla üretildiler. Dolayısıyla
ölçülen şey "Jev doğru mu" değil, **"Jev Opus ile ne kadar örtüşüyor"dur.**
İkisi aynı yerde yanılıyorsa bu ölçüm onu göremez.

Buna rağmen değerli: eşik seçimi için gereken şey mutlak doğruluk değil,
olasılık dağılımının ŞEKLİDİR — hangi olasılıkta kaç pozitif var. 56 kalemle
bu şekil çıkmaz, 938 kalemle çıkar.

Gerçek altın küme (56 kalem) bu koşuya GİRMEZ; temiz kalır.
═══════════════════════════════════════════════════════════════════════════

Gönderilen veri: yalnız kamuya açık Resmî Gazete başlıkları.

    python kalibrasyon.py --kos          # Jev'i koştur (yeniden başlatılabilir)
    python kalibrasyon.py                # kaydedilmiş sonucu çözümle
"""

from __future__ import annotations

import argparse
import json
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

KOK = Path(__file__).resolve().parent
if str(KOK) not in sys.path:
    sys.path.insert(0, str(KOK))

import etiket_hazirla as eh       # noqa: E402
import etiket_kumele as ek        # noqa: E402
import jev                        # noqa: E402
from pilot_b_fihrist import SORULAR  # noqa: E402

DEPO = KOK / "fixtures" / "etiketler_kalem.json"
HAM = KOK / "olcum" / "jev_kalibrasyon_ham.jsonl"
KONULAR = ("enerji", "rekabet", "vergi", "icra")


# --------------------------------------------------------------------------- #
# Koşu
# --------------------------------------------------------------------------- #

def adaylar() -> List[Dict[str, Any]]:
    """Etiketli küme temsilcileri. Altın küme dışarıda (eh.ayir zaten ayırıyor)."""
    etiketli = json.loads(DEPO.read_text(encoding="utf-8"))["etiket"]
    kalemler, kumeler = ek.hazirla()
    cikti = []
    for ki, uyeler in enumerate(kumeler):
        t = kalemler[uyeler[0]]
        a = eh.anahtar(t["baslik"])
        if a in etiketli:
            cikti.append({"kume": ki, "bolum": t["bolum"], "baslik": t["baslik"],
                          "uye": len(uyeler), "altin": etiketli[a]})
    return cikti


def bitmisler() -> set:
    if not HAM.exists():
        return set()
    bitti = set()
    for satir in HAM.read_text(encoding="utf-8").splitlines():
        if satir.strip():
            try:
                bitti.add(json.loads(satir)["kume"])
            except (ValueError, KeyError):
                pass
    return bitti


def kos(eszamanlilik: int, sinir: Optional[int]) -> int:
    jev.env_yukle()
    istemci = jev.istemci_kur()
    if getattr(istemci, "sahte", False):
        raise SystemExit("Jev anahtarı yok. Kalibrasyon gerçek uç ister.")

    is_listesi = [k for k in adaylar() if k["kume"] not in bitmisler()]
    if sinir:
        is_listesi = is_listesi[:sinir]
    if not is_listesi:
        print("Çekilecek yeni kalem yok.")
        return 0
    print("Kalem: %d · eşzamanlılık %d · tahmini ~$%.3f"
          % (len(is_listesi), eszamanlilik, len(is_listesi) * 1033 / 1e6 * 0.042))

    HAM.parent.mkdir(exist_ok=True)
    kilit = threading.Lock()
    dosya = HAM.open("a", encoding="utf-8")
    sayac = {"ok": 0, "hata": 0}
    t0 = time.perf_counter()

    def tek(k: Dict[str, Any]) -> None:
        state = {"kaynak": "Resmî Gazete fihristi", "bolum": k["bolum"],
                 "baslik": k["baslik"]}
        try:
            b = time.perf_counter()
            cevap = istemci.sor(state, SORULAR)
            ms = 1000 * (time.perf_counter() - b)
        except jev.JevHatasi as exc:
            with kilit:
                sayac["hata"] += 1
                print("  HATA kume=%d: %s" % (k["kume"], str(exc)[:80]))
            return
        kayit = {"kume": k["kume"], "baslik": k["baslik"], "altin": k["altin"],
                 "uye": k["uye"], "ms": round(ms),
                 "p": {a: float(c.deger) for a, c in cevap.items()}}
        with kilit:
            dosya.write(json.dumps(kayit, ensure_ascii=False) + "\n")
            dosya.flush()
            sayac["ok"] += 1
            n = sayac["ok"] + sayac["hata"]
            if n % 50 == 0:
                gecen = time.perf_counter() - t0
                print("  %d/%d  (%.0f sn, kalan ~%.0f sn)"
                      % (n, len(is_listesi), gecen,
                         gecen / n * (len(is_listesi) - n)))

    with ThreadPoolExecutor(max_workers=eszamanlilik) as havuz:
        for f in as_completed([havuz.submit(tek, k) for k in is_listesi]):
            f.result()
    dosya.close()
    print()
    print("Bitti: %d başarılı, %d hata, %.0f sn" %
          (sayac["ok"], sayac["hata"], time.perf_counter() - t0))
    return 0


# --------------------------------------------------------------------------- #
# Çözümleme
# --------------------------------------------------------------------------- #

def yukle() -> List[Dict[str, Any]]:
    if not HAM.exists():
        raise SystemExit("Ham kayıt yok. Önce: python kalibrasyon.py --kos")
    return [json.loads(s) for s in HAM.read_text(encoding="utf-8").splitlines()
            if s.strip()]


def _kirp(p: np.ndarray, eps: float = 1e-4) -> np.ndarray:
    """Tam 0 ve tam 1'i logit için kırp. Jev bunları sıkça döndürüyor."""
    return np.clip(p, eps, 1 - eps)


def ece(p: np.ndarray, y: np.ndarray, kova: int = 10) -> float:
    kenar = np.linspace(0.0, 1.0, kova + 1)
    toplam = 0.0
    for i in range(kova):
        m = (p >= kenar[i]) & (p < kenar[i + 1] if i < kova - 1 else p <= 1.0)
        if m.sum() == 0:
            continue
        toplam += m.sum() / len(p) * abs(y[m].mean() - p[m].mean())
    return float(toplam)


def gurultu_tabani(p: np.ndarray, tekrar: int = 200, tohum: int = 20260920) -> float:
    """Mükemmel kalibre bir modelin bu n'de üreteceği ortalama ECE.

    Ölçülen ECE bunun altındaysa sapma yoktur; ECE tek başına yanıltıcıdır.
    """
    rng = np.random.default_rng(tohum)
    return float(np.mean([ece(p, (rng.random(len(p)) < p).astype(float))
                          for _ in range(tekrar)]))


def sicaklik_uydur(p: np.ndarray, y: np.ndarray) -> float:
    """NLL'i en aza indiren T. T>1 aşırı güvenli, T<1 güvensiz demektir."""
    z = np.log(_kirp(p) / (1 - _kirp(p)))
    en_iyi, en_iyi_nll = 1.0, np.inf
    for t in np.exp(np.linspace(np.log(0.2), np.log(6.0), 120)):
        q = _kirp(1 / (1 + np.exp(-z / t)))
        nll = -np.mean(y * np.log(q) + (1 - y) * np.log(1 - q))
        if nll < en_iyi_nll:
            en_iyi, en_iyi_nll = float(t), float(nll)
    return en_iyi


def guvenilirlik(p: np.ndarray, y: np.ndarray, kova: int = 10) -> List[Tuple]:
    kenar = np.linspace(0.0, 1.0, kova + 1)
    satir = []
    for i in range(kova):
        m = (p >= kenar[i]) & (p < kenar[i + 1] if i < kova - 1 else p <= 1.0)
        if m.sum():
            satir.append((kenar[i], kenar[i + 1], int(m.sum()),
                          float(p[m].mean()), float(y[m].mean())))
    return satir


def cozumle() -> int:
    kayit = yukle()
    print("=" * 78)
    print("JEV KALİBRASYONU — %d küme temsilcisi" % len(kayit))
    print("=" * 78)
    print("UYARI: etiketler Opus damıtmasıdır, altın değildir. Ölçülen şey")
    print("       'Jev doğru mu' değil, 'Jev Opus ile ne kadar örtüşüyor'dur.")
    ms = np.array([k["ms"] for k in kayit], dtype=float)
    print()
    print("Gecikme: medyan %.0f ms · p90 %.0f ms · azami %.0f ms"
          % (np.median(ms), np.percentile(ms, 90), ms.max()))
    print()

    for konu in KONULAR:
        p = np.array([k["p"][konu] for k in kayit], dtype=float)
        y = np.array([float(k["altin"].get(konu, 0)) for k in kayit])
        poz = int(y.sum())
        e = ece(p, y)
        taban = gurultu_tabani(p)
        T = sicaklik_uydur(p, y)
        yon = ("aşırı güvenli" if T > 1.15 else
               "güvensiz" if T < 0.87 else "kalibre sayılır")
        print("-" * 78)
        print("%s  ·  pozitif %d/%d (%%%.1f)"
              % (konu.upper(), poz, len(y), 100 * poz / len(y)))
        print("  ECE %.3f   gürültü tabanı %.3f   oran %.1fx   T %.2f  (%s)"
              % (e, taban, e / taban if taban else 0, T, yon))
        print("  %-13s %6s %9s %9s" % ("bant", "n", "ort. p", "gerçek"))
        for a, b, n, pm, ym in guvenilirlik(p, y):
            isaret = ""
            if n >= 10:
                isaret = "  <" if ym > pm + 0.10 else ("  >" if ym < pm - 0.10 else "")
            print("  %.1f-%.1f %9d %9.3f %9.3f%s" % (a, b, n, pm, ym, isaret))
    print("-" * 78)

    # Eşik süpürmesi: bu iş için asıl sayı duyarlılık.
    print()
    print("EŞİK SÜPÜRMESİ (duyarlılık / elenen oranı)")
    print("%6s %s %9s" % ("eşik", "".join("%14s" % k for k in KONULAR), "elenen"))
    for esik in (0.02, 0.05, 0.10, 0.15, 0.20, 0.30, 0.50):
        satir = ""
        for konu in KONULAR:
            p = np.array([k["p"][konu] for k in kayit])
            y = np.array([float(k["altin"].get(konu, 0)) for k in kayit])
            d = float(((p >= esik) & (y > 0)).sum() / y.sum()) if y.sum() else 0
            satir += "%13.0f%%" % (100 * d)
        elenen = np.mean([all(k["p"][c] < esik for c in KONULAR) for k in kayit])
        print("%6.2f %s %8.0f%%" % (esik, satir, 100 * elenen))
    print()
    print("Okuma: bir ön elemede kaçırmak pahalı, fazladan okumak ucuz.")
    print("       Duyarlılığı %100'e yakın tutan EN YÜKSEK eşik seçilmeli.")
    return 0


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--kos", action="store_true", help="Jev'i koştur")
    ap.add_argument("--eszamanlilik", type=int, default=jev.ONERILEN_ESZAMANLILIK)
    ap.add_argument("--sinir", type=int, default=None, help="yalnız ilk N kalem")
    a = ap.parse_args(argv)
    return kos(a.eszamanlilik, a.sinir) if a.kos else cozumle()


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, OSError):
        pass
    raise SystemExit(main())
