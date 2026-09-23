"""ArthurLegal yerel MCP sunucusu (stdio) — Claude Desktop'ta `arthurlegal-yerel`.

İki iş yapar:
1. Paket: Law Firm ve Corporate paketlerinin SYSTEM_PROMPT'u ve bütün knowledge dosyaları
   (büro katmanıyla) araçla okunur. Paket güncellenince Project'e hiçbir şey yüklenmez;
   Project'teki kısa ön yükleme talimatı (ortak.ONYUKLEME) hiç değişmez.
2. Araştırma köprüsü: https://arthurlegal-mcp.fly.dev/mcp araçları aynen aktarılır, connector
   eklemek gerekmez. `tkgm_` araçları aktarılmaz: tapu işleri yerel arthur-tapu'dadır ve tapu
   kaydı metni buluta gitmez.

Yalnız standart kütüphane. Günlüğe sorgu metni veya belge içeriği yazılmaz.
"""
from __future__ import annotations

import concurrent.futures
import json
import math
import os
import re
import sys
import threading
import time
import traceback
import urllib.error

import ortak

PROTOKOLLER = ("2025-11-25", "2025-06-18", "2025-03-26", "2024-11-05")
AZAMI = 60000
UZANTILAR = (".md", ".json", ".txt", ".csv")
_KATLAMA = str.maketrans("İIıŞşĞğÜüÖöÇçÂâÎîÛû", "iiissgguuooccaaiiuu")
_BECERI = re.compile(r"^#{1,2}\s+/[\w-]+:[\w-]+")


def katla(metin: str) -> str:
    return metin.translate(_KATLAMA).lower()


class Hata(Exception):
    def __init__(self, kod: int, mesaj: str):
        super().__init__(mesaj)
        self.kod = kod


# ---------------------------------------------------------------------------- paket bilgisi

class Bilgi:
    def __init__(self, surum_dizini, firma_dizini):
        self.paketler = surum_dizini / "paketler"
        self.firma = firma_dizini
        self.firma_bilgi = ortak.json_oku(firma_dizini / "firma.json")
        self._harita, self._metin, self._kilit = {}, {}, threading.Lock()

    def profiller(self):
        return [p for p in ortak.PROFILLER if (self.paketler / p / "SYSTEM_PROMPT.md").exists()]

    def profil(self, istenen):
        mevcut = self.profiller()
        if not mevcut:
            raise Hata(-32603, "Bu kurulumda paket yok.")
        if not istenen:  # kurulumda seçilen varsayılan; yoksa ilk paket
            varsayilan = ortak.ayar().get("varsayilan_profil")
            return varsayilan if varsayilan in mevcut else mevcut[0]
        if istenen not in mevcut:
            raise Hata(-32602, f"Bilinmeyen profil: {istenen}. Seçenekler: {', '.join(mevcut)}")
        return istenen

    def harita(self, profil):
        with self._kilit:
            if profil not in self._harita:
                h = {}
                for kok, atla in ((self.paketler / profil, ()), (self.firma, ("firma.json",))):
                    if kok.is_dir():  # büro katmanı sonra gelir: aynı yoldaki paket dosyasını ezer
                        for y in sorted(kok.rglob("*")):
                            if y.is_file() and y.suffix.lower() in UZANTILAR and y.name not in atla:
                                h[y.relative_to(kok).as_posix()] = y
                self._harita[profil] = h
            return self._harita[profil]

    def metin(self, yol):
        with self._kilit:
            if yol not in self._metin:
                ham = yol.read_text(encoding="utf-8", errors="replace")
                self._metin[yol] = (ham, katla(ham))
            return self._metin[yol]

    def bul(self, profil, yol):
        h = self.harita(profil)
        y = (yol or "").strip().replace("\\", "/").lstrip("./")
        for aday in (y, "knowledge/" + y):
            if aday in h:
                return aday
        ad = y.rsplit("/", 1)[-1].lower()
        eslesen = [k for k in h if k.rsplit("/", 1)[-1].lower() == ad]
        if len(eslesen) == 1:
            return eslesen[0]
        if eslesen:
            raise Hata(-32602, "Birden çok dosya eşleşti: " + ", ".join(eslesen))
        raise Hata(-32602, f"Dosya yok: {yol}. `arthurlegal_bilgi_ara` ile arayın.")

    def ara(self, profil, sorgu, en_fazla=8):
        h = self.harita(profil)
        terimler = list(dict.fromkeys(t for t in re.findall(r"[\w/:.-]+", katla(sorgu)) if len(t) >= 2))
        if not terimler:
            raise Hata(-32602, "Sorgu boş.")
        sayim = {k: [self.metin(y)[1].count(t) for t in terimler] for k, y in h.items()}
        n = len(h) or 1
        idf = [math.log((n + 1) / (1 + sum(1 for s in sayim.values() if s[i]))) + 1 for i in range(len(terimler))]
        puanlar = []
        for k, s in sayim.items():
            yol_katli = katla(k)
            puan = sum(math.log1p(c) * idf[i] for i, c in enumerate(s)) + sum(3 * idf[i] for i, t in enumerate(terimler) if t in yol_katli)
            kapsam = sum(1 for c in s if c)
            if puan:
                puanlar.append((puan * (1 + kapsam) / (1 + len(terimler)), k))
        puanlar.sort(reverse=True)
        satirlar = [f"'{sorgu}' için {len(puanlar)} dosya eşleşti; ilk {min(en_fazla, len(puanlar))}:"]
        for puan, k in puanlar[:en_fazla]:
            ham, katli = self.metin(h[k])
            satirlar.append(f"\n{k}  (puan {puan:.1f})")
            gorulen = set()
            for t in sorted(terimler, key=lambda t: -idf[terimler.index(t)])[:3]:
                i = katli.find(t)
                if i < 0:
                    continue
                no = ham.count("\n", 0, i) + 1
                if no in gorulen:
                    continue
                gorulen.add(no)
                satir = ham.splitlines()[no - 1].strip()
                satirlar.append(f"  s.{no}: {satir[:240]}")
        if not puanlar:
            satirlar.append("Eşleşme yok. Daha genel bir terim deneyin.")
        return "\n".join(satirlar)

    def getir(self, profil, yol, bolum=None, baslangic=0):
        k = self.bul(profil, yol)
        ham, _ = self.metin(self.harita(profil)[k])
        if bolum:
            return f"[{k} — bölüm: {bolum}]\n\n" + self._bolum(ham, bolum)
        baslangic = max(0, int(baslangic or 0))
        parca = ham[baslangic:baslangic + AZAMI]
        son = baslangic + len(parca)
        dip = f"\n\n[devamı var: baslangic={son} ile isteyin; toplam {len(ham)} karakter]" if son < len(ham) else ""
        return f"[{k}]\n\n{parca}{dip}"

    @staticmethod
    def _bolum(ham, bolum):
        satirlar = ham.splitlines(keepends=True)
        basliklar = [(i, len(m.group(1)), m.group(2).strip()) for i, s in enumerate(satirlar)
                     for m in [re.match(r"(#{1,6})\s+(.*)", s)] if m]
        b = katla(bolum).strip().lstrip("/")
        secim = (next((x for x in basliklar if katla(x[2]).lstrip("/") == b), None)
                 or next((x for x in basliklar if _BECERI.match(satirlar[x[0]]) and katla(x[2]).endswith(":" + b)), None)
                 or next((x for x in basliklar if b in katla(x[2])), None))
        if not secim:
            yakin = [x[2] for x in basliklar if any(t in katla(x[2]) for t in b.replace(":", " ").split())][:15]
            return "Bölüm bulunamadı." + (" Yakın başlıklar:\n- " + "\n- ".join(yakin) if yakin else "")
        i, duzey, _ = secim
        beceri = bool(_BECERI.match(satirlar[i]))
        for j, dz, _ in basliklar:
            if j > i and ((beceri and _BECERI.match(satirlar[j])) or (not beceri and dz <= duzey)):
                parca = "".join(satirlar[i:j])
                break
        else:
            parca = "".join(satirlar[i:])
        return parca[:AZAMI] + ("\n\n[bölüm kısaltıldı]" if len(parca) > AZAMI else "")

    def paket_surumu(self, profil):
        surum = ortak.json_oku(self.paketler.parent / "icerik.json").get("paketler", {}).get(profil)
        if surum:  # derleme, sürümü paket klasörünün adından yazar (VERSION.md geride kalabiliyor)
            return surum
        try:
            return (self.paketler / profil / "VERSION.md").read_text(encoding="utf-8").strip().lstrip("v")
        except OSError:
            return "?"

    def talimat(self, profil):
        h = self.harita(profil)
        sp, _ = self.metin(h["SYSTEM_PROMPT.md"])
        firma = self.firma_bilgi.get("ad")
        buro = [k for k in h if k.startswith("buro/")]
        kirmizi = next((k for k in buro if "kirmizi" in k), None)
        maddeler = [
            "Bilgi dosyaları Project'e yüklenmedi. SYSTEM_PROMPT'ta adı geçen her `knowledge/...` dosyasını "
            "`arthurlegal_bilgi_getir` ile oku; hangi dosyada olduğunu bilmediğin konuda önce `arthurlegal_bilgi_ara`. "
            "Okumadığın dosyanın içeriğini varsayma.",
            "`/eklenti:komut` biçimindeki bir komut istendiğinde `knowledge/skills/<eklenti>__skills.md` dosyasını "
            "`bolum=\"/<eklenti>:<komut>\"` ile getir ve oradaki adımları uygula.",
            "Metinde geçen `~/.claude/plugins/config/...` yolları bu kurulumda yoktur; büro bilgisi "
            "`knowledge/firm-profile.md` (Corporate'ta `knowledge/company-profile.md`) dosyasındadır.",
            "Araştırma araçları (`tr_`, `az_`, `eu_`, `uk_` ... önekli) ve `status` bu `arthurlegal-yerel` sunucusundan "
            "gelir. Aynı araçlar ayrıca claude.ai connector'ı olarak görünüyorsa bu sunucudakini kullan.",
            "Tapu, parsel ve harç işlerinde `arthur-tapu` yerel araçlarını kullan; `tkgm_` önekli uzak araçları kullanma. "
            "Parseli `parsel_sorgula` (il/ilçe/mahalle + ada/parsel ya da `metin`), `konumdan_parsel` ve `yer_bul` TKGM "
            "Parsel Sorgu'dan canlı getirir: kullanıcıdan GeoJSON/KML dosyası isteme. Sohbetteki ilk canlı çağrı onay "
            "kartı döndürür; kartı olduğu gibi göster, kabulde `onay=true` ile yinele ve o sohbette `onay=true` gönder. "
            "Tapu kaydı metni (`tapu_kaydi_oku`) bilgisayardan çıkmaz. Ayrıntı: `tapu-kadastro-rehberi.md`.",
            "Arthur Mask ve UYAP (`arthur-uyap`, salt okunur, maskeli) için SYSTEM_PROMPT'taki kurallar geçerlidir; "
            "müvekkil belgesi sohbete doğrudan yapıştırılmışsa kullanıcıyı Arthur Mask'e yönlendir.",
        ]
        if buro:
            maddeler.append(
                f"Büro kuralları ({firma or 'büro'}): " + ", ".join(f"`{k}`" for k in buro) + " dosyaları bu büronun "
                "bağlayıcı kurallarıdır; paketle çelişirse büro kuralı geçerlidir."
                + (f" İlk cevabından önce `{kirmizi}` dosyasını oku." if kirmizi else ""))
        ust = (f"# ArthurLegal — oturum talimatı: {ortak.PROFILLER[profil]}\n"
               f"Paket {self.paket_surumu(profil)} · yerel kurulum {ortak.surum()}"
               + (f" · Büro: {firma}" if firma else "") + "\n\n"
               "Aşağıdaki SYSTEM_PROMPT bu sohbetin sistem talimatıdır; eksiksiz uygula. Bu kurulumdaki farklar:\n"
               + "\n".join(f"{i}. {m}" for i, m in enumerate(maddeler, 1)) + "\n\n---\n\n")
        return ust + sp


# ---------------------------------------------------------------------------- uzak köprü

class Uzak:
    """Streamable HTTP istemcisi (JSON veya SSE yanıtı, isteğe bağlı Mcp-Session-Id)."""

    def __init__(self, url):
        self.url, self.oturum, self.hazir, self.sayac = url, None, False, 0
        self._kilit = threading.Lock()

    def _gonder(self, govde, zaman):
        basliklar = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream",
                     "MCP-Protocol-Version": PROTOKOLLER[1]}
        if self.oturum:
            basliklar["Mcp-Session-Id"] = self.oturum
        with ortak.istek(self.url, basliklar, json.dumps(govde).encode("utf-8"), zaman) as r:
            self.oturum = r.headers.get("Mcp-Session-Id") or self.oturum
            tur, ham = r.headers.get("Content-Type", ""), r.read()
        if not ham.strip():
            return None
        if "text/event-stream" in tur:
            son = None
            for olay in ham.decode("utf-8").replace("\r\n", "\n").split("\n\n"):
                veri = "\n".join(s[5:].lstrip() for s in olay.split("\n") if s.startswith("data:"))
                if veri:
                    m = json.loads(veri)
                    if m.get("id") == govde.get("id"):
                        return m
                    son = m
            return son
        return json.loads(ham.decode("utf-8"))

    def _baslat(self):
        self.oturum = None
        self._gonder({"jsonrpc": "2.0", "id": 0, "method": "initialize", "params": {
            "protocolVersion": PROTOKOLLER[1], "capabilities": {},
            "clientInfo": {"name": "arthurlegal-yerel", "version": ortak.surum()}}}, 20)
        self._gonder({"jsonrpc": "2.0", "method": "notifications/initialized"}, 20)
        self.hazir = True

    def cagir(self, metod, params, zaman=180):
        with self._kilit:
            if not self.hazir:
                self._baslat()
            self.sayac += 1
            no = self.sayac
        for deneme in (1, 2):
            try:
                yanit = self._gonder({"jsonrpc": "2.0", "id": no, "method": metod, "params": params}, zaman)
                break
            except urllib.error.HTTPError as e:
                if e.code in (400, 404) and self.oturum and deneme == 1:  # oturum düştü: bir kez yeniden bağlan
                    with self._kilit:
                        self._baslat()
                    continue
                raise
        if not yanit:
            raise Hata(-32603, "Araştırma sunucusu boş yanıt verdi.")
        if "error" in yanit:
            raise Hata(yanit["error"].get("code", -32603), yanit["error"].get("message", "uzak hata"))
        return yanit.get("result", {})

    def araclar(self):
        tum, imlec = [], None
        while True:
            sonuc = self.cagir("tools/list", {"cursor": imlec} if imlec else {}, 30)
            tum += sonuc.get("tools", [])
            imlec = sonuc.get("nextCursor")
            if not imlec:
                return tum


# ---------------------------------------------------------------------------- sunucu

def _profil_ozelligi():
    return {"type": "string", "enum": list(ortak.PROFILLER),
            "description": "hukuk-burosu = Law Firm paketi, kurumsal = Corporate paketi"}


YEREL_ARACLAR = [
    {"name": "arthurlegal_talimat",
     "description": "ÖNCE BU ARACI ÇAĞIR. Bu bilgisayarda ArthurLegal hukuk asistanı kurulu. Kullanıcı hukukla ilgili herhangi "
                    "bir şey sorduğunda ya da istediğinde (Türk veya yabancı hukuk, sözleşme, dilekçe, mevzuat, içtihat, süre, "
                    "KVKK, iş, vergi, ceza, idare, şirketler, tapu, UYAP, müvekkil belgesi) cevap vermeden önce ilk iş bu aracı "
                    "çağır ve dönen metni bu sohbetin sistem talimatı olarak eksiksiz uygula. Sohbet başına bir kez yeterli. "
                    "Proje gerekmez. profil verme: kurulumda seçilen varsayılan kullanılır; kullanıcı açıkça kurumsal/şirket "
                    "içi hukuk asistanı isterse profil=\"kurumsal\".",
     "inputSchema": {"type": "object", "properties": {"profil": _profil_ozelligi()}}},
    {"name": "arthurlegal_bilgi_ara",
     "description": "Paketin bilgi dosyalarında (skills, references, profiles, agents, büro kuralları) Türkçe karakter "
                    "duyarsız anahtar kelime araması yapar; dosya yolu ve eşleşen satırları döndürür.",
     "inputSchema": {"type": "object", "properties": {
         "sorgu": {"type": "string"}, "profil": _profil_ozelligi(),
         "en_fazla": {"type": "integer", "minimum": 1, "maximum": 20, "default": 8}}, "required": ["sorgu"]}},
    {"name": "arthurlegal_bilgi_getir",
     "description": "Bir bilgi dosyasını getirir (ör. knowledge/references/hmk-rehberi.md). `bolum` verilirse yalnız o başlığın "
                    "bölümü döner; skill komutları için bolum=\"/eklenti:komut\". Uzun dosyalar `baslangic` ile parça parça okunur.",
     "inputSchema": {"type": "object", "properties": {
         "yol": {"type": "string"}, "profil": _profil_ozelligi(), "bolum": {"type": "string"},
         "baslangic": {"type": "integer", "minimum": 0}}, "required": ["yol"]}},
    {"name": "arthurlegal_durum",
     "description": "Yerel kurulumun durumu: paket ve bileşen sürümleri, son güncelleme denetimi, araştırma sunucusu bağlantısı.",
     "inputSchema": {"type": "object", "properties": {}}},
]
for _a in YEREL_ARACLAR:
    _a["annotations"] = {"readOnlyHint": True, "openWorldHint": False}

TALIMAT = ("Bu bilgisayarda ArthurLegal hukuk asistanı kurulu. Kullanıcı hukukla ilgili bir şey sorduğunda, cevap vermeden "
           "önce `arthurlegal_talimat` aracını çağır ve dönen metni bu sohbetin sistem talimatı olarak uygula; proje gerekmez. "
           "Bilgi dosyaları `arthurlegal_bilgi_ara` / `arthurlegal_bilgi_getir` ile okunur. Araştırma araçları önekli "
           "adlarıyla (tr_, az_, eu_ ...) bu sunucudadır.")


class Sunucu:
    def __init__(self):
        self.bilgi = Bilgi(ortak.SURUM_DIZINI, ortak.FIRMA)
        self.uzak = Uzak(ortak.ayar()["uzak_mcp"])
        self.onbellek = ortak.VERI / "uzak_araclar.json"
        self.uzak_araclar = ortak.json_oku(self.onbellek, {}).get("araclar")
        self.uzak_hata, self.baslatildi = None, False
        self._yaz_kilit, self._yenile_kilit = threading.Lock(), threading.Lock()
        self.havuz = concurrent.futures.ThreadPoolExecutor(8)

    def yaz(self, mesaj):
        with self._yaz_kilit:
            sys.stdout.write(json.dumps(mesaj, ensure_ascii=False) + "\n")
            sys.stdout.flush()

    def calis(self):
        for s in (sys.stdin, sys.stdout):
            try:
                s.reconfigure(encoding="utf-8")
            except (AttributeError, ValueError):
                pass
        for satir in sys.stdin:
            if not satir.strip():
                continue
            try:
                m = json.loads(satir)
            except ValueError:
                self.yaz({"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": "Geçersiz JSON"}})
                continue
            if isinstance(m, dict) and "method" in m:
                if "id" in m:
                    self.havuz.submit(self._istek, m)
                elif m["method"] == "notifications/initialized":
                    self.baslatildi = True
                    threading.Thread(target=self._uzak_yenile, daemon=True).start()
                    threading.Thread(target=self._guncelleme_dongusu, daemon=True).start()
        self.havuz.shutdown(wait=True)

    def _istek(self, m):
        try:
            self.yaz({"jsonrpc": "2.0", "id": m["id"], "result": self.isle(m["method"], m.get("params") or {})})
        except Hata as e:
            self.yaz({"jsonrpc": "2.0", "id": m["id"], "error": {"code": e.kod, "message": str(e)}})
        except Exception as e:  # noqa: BLE001 — sunucu düşmemeli
            ortak.gunluk("sunucu", f"{m.get('method')}: {e!r}\n{traceback.format_exc()}")
            self.yaz({"jsonrpc": "2.0", "id": m["id"], "error": {"code": -32603, "message": f"İç hata: {e}"}})

    def isle(self, metod, p):
        if metod == "initialize":
            istenen = p.get("protocolVersion")
            return {"protocolVersion": istenen if istenen in PROTOKOLLER else PROTOKOLLER[0],
                    "capabilities": {"tools": {"listChanged": True}, "prompts": {"listChanged": False}},
                    "serverInfo": {"name": "arthurlegal-yerel", "version": ortak.surum()}, "instructions": TALIMAT}
        if metod == "ping":
            return {}
        if metod == "tools/list":
            if self.uzak_araclar is None:
                self._uzak_yenile(zaman_asimi=True)
            return {"tools": YEREL_ARACLAR + (self.uzak_araclar or [])}
        if metod == "tools/call":
            return self._arac(p.get("name", ""), p.get("arguments") or {})
        if metod == "prompts/list":
            return {"prompts": [{"name": pr, "description": f"ArthurLegal {ad} olarak başla (Project kullanmadan)"}
                                for pr, ad in ortak.PROFILLER.items()]}
        if metod == "prompts/get":
            ad = p.get("name")
            if ad not in ortak.ONYUKLEME:
                raise Hata(-32602, f"Bilinmeyen istem: {ad}")
            return {"messages": [{"role": "user", "content": {"type": "text", "text": ortak.ONYUKLEME[ad]}}]}
        if metod in ("resources/list", "resources/templates/list"):
            return {"resources": []} if metod == "resources/list" else {"resourceTemplates": []}
        raise Hata(-32601, f"Desteklenmeyen yöntem: {metod}")

    def _arac(self, ad, a):
        yerel = {
            "arthurlegal_talimat": lambda: self.bilgi.talimat(self.bilgi.profil(a.get("profil"))),
            "arthurlegal_bilgi_ara": lambda: self.bilgi.ara(self.bilgi.profil(a.get("profil")), a.get("sorgu", ""),
                                                            max(1, min(20, int(a.get("en_fazla") or 8)))),
            "arthurlegal_bilgi_getir": lambda: self.bilgi.getir(self.bilgi.profil(a.get("profil")), a.get("yol", ""),
                                                                a.get("bolum"), a.get("baslangic", 0)),
            "arthurlegal_durum": self._durum,
        }
        if ad in yerel:
            try:
                return {"content": [{"type": "text", "text": yerel[ad]()}]}
            except Hata as e:
                return {"content": [{"type": "text", "text": str(e)}], "isError": True}
        if ad.startswith("tkgm_"):
            return {"content": [{"type": "text", "text": "tkgm_ araçları bu kurulumda yerel arthur-tapu sunucusundadır."}],
                    "isError": True}
        try:
            return self.uzak.cagir("tools/call", {"name": ad, "arguments": a})
        except Hata as e:
            if e.kod == -32602 or "not found" in str(e).lower() or "unknown" in str(e).lower():
                raise
            return {"content": [{"type": "text", "text": f"Araştırma sunucusu hata verdi: {e}"}], "isError": True}
        except (OSError, urllib.error.URLError, ValueError) as e:
            ortak.gunluk("sunucu", f"uzak çağrı başarısız ({ad}): {e!r}")
            return {"content": [{"type": "text", "text": f"ArthurLegal araştırma sunucusuna ulaşılamadı ({e}). "
                                 "İnternet bağlantısını denetleyin; sonuç doğrulanmadan cevap vermeyin."}], "isError": True}

    def _uzak_yenile(self, zaman_asimi=False):
        if not self._yenile_kilit.acquire(blocking=not zaman_asimi or self.uzak_araclar is None):
            return
        try:
            araclar = [t for t in self.uzak.araclar() if not t.get("name", "").startswith("tkgm_")]
            self.uzak_hata = None
        except Exception as e:  # noqa: BLE001
            self.uzak_hata = str(e)
            ortak.gunluk("sunucu", f"uzak araç listesi alınamadı: {e!r}")
            if self.uzak_araclar is None:
                self.uzak_araclar = []
            return
        finally:
            self._yenile_kilit.release()
        if araclar != self.uzak_araclar:
            onceki = self.uzak_araclar
            self.uzak_araclar = araclar
            ortak.json_yaz(self.onbellek, {"zaman": time.time(), "araclar": araclar})
            if self.baslatildi and onceki:
                self.yaz({"jsonrpc": "2.0", "method": "notifications/tools/list_changed"})

    def _guncelleme_dongusu(self):
        if os.environ.get("ARTHURLEGAL_GUNCELLEME") == "0":
            return
        pythonw = ortak.RUNTIME / "pythonw.exe"
        while pythonw.exists():
            aralik = float(ortak.ayar().get("denetim_araligi_saat", 6)) * 3600
            if time.time() - float(ortak.durum().get("son_denetim", 0)) > aralik:
                try:
                    ortak.arka_planda([pythonw, "-B", ortak.AL, "guncelle", "--sessiz"])
                except OSError as e:
                    ortak.gunluk("sunucu", f"güncelleyici başlatılamadı: {e!r}")
            time.sleep(1800)

    def _durum(self):
        d = ortak.durum()
        icerik = ortak.json_oku(ortak.SURUM_DIZINI / "icerik.json")
        return json.dumps({
            "yerel_kurulum": ortak.surum(),
            "paketler": {p: self.bilgi.paket_surumu(p) for p in self.bilgi.profiller()},
            "bilesenler": icerik.get("bilesenler", {}),
            "arthur_mask": ortak.mask_surumu() or "kurulu değil",
            "buro": self.bilgi.firma_bilgi.get("ad") or "yok (standart paket)",
            "son_guncelleme_denetimi": time.strftime("%Y-%m-%d %H:%M", time.localtime(d["son_denetim"])) if d.get("son_denetim") else "henüz yok",
            "son_guncelleme_sonucu": d.get("son_sonuc", "-"),
            "arastirma_sunucusu": "bağlı" if self.uzak_araclar and not self.uzak_hata else f"ulaşılamadı: {self.uzak_hata}",
            "uzak_arac_sayisi": len(self.uzak_araclar or []),
        }, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    Sunucu().calis()
