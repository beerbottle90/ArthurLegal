#!/usr/bin/env python3
"""Canlı uç gerçekten bu depoda ölçülen şeyi mi koşturuyor? — dağıtım sonrası doğrulama.

    python canli_dogrula.py                                  # arthurlegal-mcp.fly.dev
    python canli_dogrula.py https://baska-uc.example/mcp

Neden var: ana paketlerin (ArthurLegal v1.9.0) bilgi dosyaları `konu` süzgecini,
torba kanun geçişini ve tarih aralığı düzeltmesini ANLATIYOR. Uç eski sürümde
kalırsa asistan, var olmayan bir parametreyi kullanmayı dener ve kullanıcı bunun
nedenini göremez. Bu betik dağıtımdan sonra koşturulur; GEÇTİ demeden ana depo
sürümü birleştirilmez.

Standart kütüphane; JSON-RPC, POST /mcp, oturum gerektirmez. Çıkış kodu 0 = geçti.
"""
from __future__ import annotations

import json
import sys
import urllib.request
from datetime import date, timedelta

URL = sys.argv[1] if len(sys.argv) > 1 else "https://arthurlegal-mcp.fly.dev/mcp"
ASGARI = (0, 4, 0)


def rpc(method, params=None, _id=1):
    body = json.dumps({"jsonrpc": "2.0", "id": _id, "method": method, "params": params or {}}).encode("utf-8")
    req = urllib.request.Request(URL, data=body, headers={
        "Content-Type": "application/json", "Accept": "application/json, text/event-stream",
        "User-Agent": "arthurlegal-canli-dogrula/2"})
    with urllib.request.urlopen(req, timeout=120) as r:
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
            try:
                return json.loads(c["text"])
            except ValueError:
                return {"_metin": c["text"]}
    return res


sonuclar = []


def kontrol(ad, gecti, ayrinti=""):
    sonuclar.append(gecti)
    print("%-6s %s%s" % ("GEÇTİ" if gecti else "KALDI", ad, ("  — " + ayrinti) if ayrinti else ""))


def surum(s):
    try:
        return tuple(int(x) for x in str(s).split(".")[:3])
    except ValueError:
        return (0, 0, 0)


print("uç:", URL)
araclar = {t["name"]: t for t in rpc("tools/list")["result"]["tools"]}
kontrol("araç listesi geldi", len(araclar) > 0, "%d araç" % len(araclar))

# 1. Şemalar
for ad in ("tr_resmi_gazete_tara", "tr_resmi_gazete_fihrist", "tr_mevzuat_ara"):
    p = (araclar.get(ad) or {}).get("inputSchema", {}).get("properties", {})
    kontrol("%s şemasında konu" % ad, "konu" in p)
tara = (araclar.get("tr_resmi_gazete_tara") or {}).get("inputSchema", {})
kontrol("tr_resmi_gazete_tara artık query zorunlu kılmıyor", "query" not in (tara.get("required") or []))
mv = (araclar.get("tr_mevzuat_ara") or {}).get("inputSchema", {}).get("properties", {})
kontrol("tr_mevzuat_ara page_size üst sınırı 20", (mv.get("page_size") or {}).get("maximum") == 20)
kontrol("mevzuat konu şeması ölçülmüş zayıflığı söylüyor", "enerji 0/3" in ((mv.get("konu") or {}).get("description") or ""))

# 2. status
st = arac("status")
tr = (st.get("backend_status") or {}).get("tr") or {}
kontrol("TR backend sürümü >= 0.4.0", surum(tr.get("version")) >= ASGARI, "sürüm %s" % tr.get("version"))
tri = tr.get("triyaj") or {}
kontrol("konu modeli yüklü", bool(tri.get("var")), "eşik %s" % tri.get("esik"))
kontrol("status mevzuat ölçümünü taşıyor", ((tri.get("mevzuat") or {}).get("gorulmemis") or {}).get("enerji") == {"pozitif": 3, "yakalanan": 0})
idx = tr.get("local_index") or {}
kontrol("arşiv tazelendi (>= 19.498 belge)", int(idx.get("documents") or 0) >= 19498,
        "%s belge, %s vektörlü" % (idx.get("documents"), idx.get("vectorised")))
if int(idx.get("vectorised") or 0) < int(idx.get("documents") or 0):
    print("       not: vektörleme arka planda sürüyor olabilir (start.sh --embed-only); birkaç dakika sonra yeniden bakın")

# 3. Resmî Gazete: konu tek başına
d_to = date.today() - timedelta(days=1)
d_from = d_to - timedelta(days=11)
r = arac("tr_resmi_gazete_tara", konu="icra", date_from=d_from.isoformat(), date_to=d_to.isoformat())
kontrol("RG konu=icra query'siz çalışıyor ve elenen sayısını bildiriyor",
        not r.get("error") and "konu_elenen" in r, "tutulan %s, elenen %s" % (r.get("total"), r.get("konu_elenen")))

# 4. Mevzuat: torba kanun, değiştirilen kanun adından
r = arac("tr_mevzuat_ara", types=["KANUN"], rg_date_from="2024-09-01", rg_date_to="2026-09-19", konu="icra", page_size=20)
kalemler = r.get("results") or []
torba = [k for k in kalemler if k.get("konu_kaynak") == "degistirilen_kanunlar" and "İcra" in (k.get("konu_degistirilen") or "")]
kontrol("7531 sayılı torba kanun İİK üzerinden bulunuyor", bool(torba),
        "toplam %s, elenen %s, belirsiz %s" % (r.get("total"), r.get("konu_elenen"), r.get("konu_belirsiz")))

# 5. Tek taraflı tarih aralığı artık süzüyor
r = arac("tr_mevzuat_ara", types=["KANUN"], rg_date_from="2024-09-01", page_size=5)
kontrol("mevzuat: yalnız rg_date_from süzüyor", 0 < int(r.get("total") or 0) < 100, "total %s (süzgeçsiz ~917)" % r.get("total"))
r = arac("tr_ictihat_ara", query='+"işe iade"', courts=["YARGITAYKARARI"], date_from="2025-01-01", page_size=3)
kontrol("içtihat: yalnız date_from süzüyor", 0 < int(r.get("total") or 0) < 20000, "total %s (süzgeçsiz ~52.993)" % r.get("total"))

# 6. Arşiv artık karar METNİNİ taşıyor. Dağıtımdan önce BDDK belgelerinin gövdesi başlığın kendisiydi;
#    arama alıntısı (snippet) gövdenin başından gelir, yani o zaman alıntı = başlık. Sonuç SAYISINA bakmak
#    yetmez: VEYA'ya düşen arama başlıktaki tek kelimeyle de sonuç döndürür. Ayırt edici işaret, alıntının
#    başlıktan belirgin biçimde uzun olmasıdır ("dolaylı pay sahipliği" 60 BDDK kararının metninde geçer,
#    hiçbirinin başlığında geçmez; Türkçe katlamayla sayıldı). İki indekste de sınandı: eski 0/5, yeni 5/5.
r = arac("tr_semantik_ara", query="dolaylı pay sahipliği", kurum="bddk", mode="lexical", limit=5)
metinli = [x for x in (r.get("results") or []) if len(x.get("snippet") or "") > len(x.get("title") or "") + 40]
kontrol("BDDK arşivi karar metnini taşıyor (alıntı başlıktan uzun)", len(metinli) > 0,
        "%d/%d sonuçta gövde metni var" % (len(metinli), len(r.get("results") or [])))

print("\nSONUÇ: %d/%d — %s" % (sum(sonuclar), len(sonuclar), "GEÇTİ" if all(sonuclar) else "KALDI"))
sys.exit(0 if all(sonuclar) else 1)
