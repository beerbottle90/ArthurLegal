"""Atıf altın kümesinin madde metinlerini canlı MCP'den çeker (elle kopyalama yok).

    python atif_madde_hasat.py            # fixtures/atif_maddeler.json yazar

Kaynak: arthurlegal-mcp `tr_mevzuat_madde_getir` (Bedesten). Her madde için ham metin ve
temizlenmiş metin birlikte saklanır. Temizlik, ürünün atıf denetçisinin de yapması gereken
şeydir: maddenin sonuna yapışan bir SONRAKİ bölümün başlıkları ("II. BEŞ YILLIK
ZAMANAŞIMI" gibi) denetçiyi yanıltabilir, dipnot işaretleri gürültüdür.

Geliştirme kümesindeki maddeler (olcum/atif_koklama_2026-09-28: SMK 120, TBK 146-147,
İş K. 17, KVKK 11, HMK 345) bilerek dışarıda: istem onlarla denendi, sınav onlarla yapılmaz.
"""
from __future__ import annotations

import json
import re
import sys
import time
import urllib.request
from pathlib import Path

URL = "https://arthurlegal-mcp.fly.dev/mcp"
CIKTI = Path(__file__).resolve().parent / "fixtures" / "atif_maddeler.json"

KANUNLAR = {
    "6098": ("TBK", "Türk Borçlar Kanunu", ["27", "39", "72", "117", "136", "182", "315", "347", "350", "444"]),
    "6102": ("TTK", "Türk Ticaret Kanunu", ["18", "21", "23", "395", "445", "446"]),
    "6100": ("HMK", "Hukuk Muhakemeleri Kanunu", ["94", "107", "127", "361", "389", "393", "397"]),
    "2004": ("İİK", "İcra ve İflas Kanunu", ["62", "67", "68", "72", "89", "168"]),
    "4857": ("İş K.", "İş Kanunu", ["18", "20", "21", "26", "32", "41", "53", "63"]),
    "6698": ("KVKK", "Kişisel Verilerin Korunması Kanunu", ["5", "7", "9", "10", "12", "13", "14"]),
    "2577": ("İYUK", "İdari Yargılama Usulü Kanunu", ["7", "10", "11"]),
    "4054": ("4054 s. K.", "Rekabetin Korunması Hakkında Kanun", ["4", "16"]),
    "5271": ("CMK", "Ceza Muhakemesi Kanunu", ["268", "273"]),
    "7036": ("7036 s. K.", "İş Mahkemeleri Kanunu", ["3"]),
    "6502": ("TKHK", "Tüketicinin Korunması Hakkında Kanun", ["11"]),
}
ANAHTAR_ONEKI = {"6098": "TBK", "6102": "TTK", "6100": "HMK", "2004": "IIK", "4857": "ISK",
                 "6698": "KVKK", "2577": "IYUK", "4054": "RKHK", "5271": "CMK", "7036": "IMK",
                 "6502": "TKHK"}

BASLIK_AZAMI = 90                       # bundan uzun satır başlık sayılmaz
SON_NOKTALAMA = (".", ":", ";", ",", ")")


def rpc(method, params=None, _id=1):
    body = json.dumps({"jsonrpc": "2.0", "id": _id, "method": method,
                       "params": params or {}}).encode("utf-8")
    req = urllib.request.Request(URL, data=body, headers={
        "Content-Type": "application/json", "Accept": "application/json, text/event-stream",
        "User-Agent": "arthurlegal-atif-hasat/1"})
    with urllib.request.urlopen(req, timeout=180) as r:
        raw = r.read().decode("utf-8")
    try:
        return json.loads(raw)
    except ValueError:
        for line in raw.splitlines():
            if line.startswith("data:"):
                return json.loads(line[5:].strip())
        raise


def arac(ad, **arg):
    res = (rpc("tools/call", {"name": ad, "arguments": arg}, 2).get("result") or {})
    for c in res.get("content") or []:
        if c.get("type") == "text":
            return json.loads(c["text"])
    raise RuntimeError("beklenmeyen yanıt: %r" % (res,)[:300])


def temizle(metin: str) -> str:
    """Dipnot işaretlerini ve maddeye yapışan sonraki bölüm başlıklarını atar."""
    m = metin.replace("&NBSP;", " ").replace("\xa0", " ")
    m = re.sub(r"\[\d{1,3}\]", "", m)                      # [13]
    m = re.sub(r"(?<=[.;:])\d{1,3}(?=\s|$)", "", m)       # "bildirebilirler.116"
    satirlar = [s.rstrip() for s in m.split("\n")]
    while satirlar:
        s = satirlar[-1].strip()
        if not s or (len(s) <= BASLIK_AZAMI and not s.endswith(SON_NOKTALAMA)):
            satirlar.pop()
            continue
        break
    m = "\n".join(satirlar)
    return re.sub(r"\n{3,}", "\n\n", m).strip()


def main() -> int:
    maddeler = {}
    for no, (kisa, ad, liste) in KANUNLAR.items():
        yanit = arac("tr_mevzuat_madde_getir", number=no, madde_no=liste,
                     max_chars_per_article=20000)
        kanun = yanit.get("law") or {}
        for it in yanit.get("items") or []:
            if not it.get("ok"):
                print("ÇEKİLEMEDİ:", no, it.get("requested"), it.get("error"), file=sys.stderr)
                return 1
            if it.get("truncated"):
                print("KESİK METİN:", no, it.get("madde_no"), file=sys.stderr)
                return 1
            anahtar = "%s-%s" % (ANAHTAR_ONEKI[no], it["madde_no"])
            ham = it.get("text") or ""
            maddeler[anahtar] = {
                "anahtar": anahtar,
                "kanun_kisa": kisa,
                "kanun_ad": ad,
                "kanun_no": no,
                "madde_no": it["madde_no"],
                "atif": it.get("citation"),
                "baslik": it.get("heading"),
                "durum": it.get("status"),
                "durum_notu": it.get("status_note"),
                "metin": temizle(ham),
                "metin_ham": ham,
                "notlar": it.get("annotations") or [],
                "dipnotlar": it.get("footnotes") or {},
                "kaynak": kanun.get("source_url"),
                "cekildi": it.get("fetched_at"),
            }
        print("%-5s %-26s %d madde" % (no, ad, len(yanit.get("items") or [])))
        time.sleep(1.0)
    CIKTI.write_text(json.dumps(maddeler, ensure_ascii=False, indent=1), encoding="utf-8")
    print("yazıldı:", CIKTI.name, "·", len(maddeler), "madde")
    return 0


if __name__ == "__main__":
    sys.exit(main())
