"""ArthurLegal yerel MCP sunucusu (stdio) — Claude Desktop'ta `arthurlegal-yerel`.

İki iş yapar (ArthurLegal Hafıza seçildiyse üç):
1. Paket: kurulumda seçilen paketlerin (Law Firm, Corporate, Courthouse, Academician; ortak.moduller)
   SYSTEM_PROMPT'u ve bütün knowledge dosyaları (büro katmanıyla) araçla okunur. Paket güncellenince
   Project'e hiçbir şey yüklenmez; Project'teki kısa ön yükleme talimatı (ortak.ONYUKLEME) hiç değişmez.
2. Araştırma köprüsü: https://arthurlegal-mcp.fly.dev/mcp araçları aynen aktarılır, connector
   eklemek gerekmez. `tkgm_` araçları aktarılmaz: tapu işleri yerel arthur-tapu'dadır ve tapu
   kaydı metni buluta gitmez.
3. Hafıza: `hafiza_` araçları bu bilgisayardaki Markdown kasasına yazar ve okur (hafiza.py).

Yalnız standart kütüphane. Günlüğe sorgu metni veya belge içeriği yazılmaz.
"""
from __future__ import annotations

import concurrent.futures
import json
import math
import os
import re
import subprocess
import sys
import threading
import time
import traceback
import urllib.error

import dogrulama_kaydi
import hafiza
import ortak
from pathlib import Path

# ArthurLegal Masası ve sohbet içi kartlar (MCP Apps). Görünümler istemci/arayuz'dadır: kopya, asıl yeri
# beerbottle90/arthurlegal-app4all (sunucu/esitle.py). Klasör yoksa ya da kurulumda "Claude Desktop klasik"
# seçildiyse (ortak.arayuz) sunucu masasız ve kartsız, metin araçlarıyla çalışır.
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "arayuz"))
try:
    import al_arayuz
except ImportError:
    al_arayuz = None
# Model ve effort önerisi arayüz seçiminden bağımsızdır: klasik arayüzde de sunucu talimatına girer. Sunucu modeli
# değiştiremez; kural, ölçümde yetersiz kalan modelle çalışan Claude'un kullanıcıya bir kez söylemesini ister.
try:
    MODEL_KURALI = al_arayuz.model_kurali() if hasattr(al_arayuz, "model_kurali") else ""
except (OSError, ValueError, KeyError):
    MODEL_KURALI = ""
if ortak.arayuz() != "yeni":
    al_arayuz = None

PROTOKOLLER = ("2025-11-25", "2025-06-18", "2025-03-26", "2024-11-05")
AZAMI = 60000
# Araç önbelleği yokken (ilk açılış) tools/list uzak araç listesini en çok bu kadar bekler (sn). Ev sahibi, sunucunun
# açılışına (initialize + tools/list) sınırlı süre tanır: ChatGPT'de startup_timeout_sec (kurulum 30 yazar, elle eklenen
# sunucuda varsayılan 10). Uzak uca ulaşılamayan bilgisayarda liste 40 sn bekletiyordu; ChatGPT sunucuyu kapatıyor,
# önbellek hiç yazılmıyor, masa hiçbir denemede açılmıyordu (18.11.2026).
ILK_LISTE_BEKLEME = 6.0
# Uzak liste hiç alınamadıysa arka plandaki yeniden deneme aralıkları (sn); sonuncusu yinelenir.
YENIDEN_DENEME = (15, 30, 60, 120, 300)
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

# Paketin hangi iş için olduğu: araç açıklamasında ve birden çok paket kuruluyken oturum talimatında.
PROFIL_ACIKLAMASI = {
    "hukuk-burosu": "avukat ve hukuk bürosu işi (dilekçe, sözleşme, dava, müvekkil)",
    "kurumsal": "şirket içi hukuk birimi işi",
    "adliye": "hâkim ve kalem (mahkeme) işi: gerekçeli karar, tensip, müzekkere, tebligat, duruşma",
    "akademisyen": "hukuk akademisyeninin işi: makale, tez, atıf, dergi seçimi, proje başvurusu",
}

_AVUKAT_MASK = ("ArthurMask için SYSTEM_PROMPT'taki kurallar geçerlidir; müvekkil belgesi sohbete doğrudan "
                "yapıştırılmışsa kullanıcıyı ArthurMask'e yönlendir. UYAP (`arthur-uyap`, salt okunur, maskeli) kuruluysa "
                "onun kendi talimatı geçerlidir: son gün hesaplanmaz ve sana gün gelmez, takvim kaydı avukatın "
                "bilgisayarında oluşur.")
MASK_MADDESI = {
    "hukuk-burosu": _AVUKAT_MASK,
    "kurumsal": _AVUKAT_MASK,
    "adliye": "ArthurMask için SYSTEM_PROMPT'taki kurallar geçerlidir; dosya belgesi (UYAP UDF dâhil) sohbete doğrudan "
              "yapıştırılmışsa kullanıcıyı ArthurMask'e yönlendir. Gizlilik ya da kısıtlama kararı olan dosyanın "
              "içeriği maskeli olsa bile kurum kuralları izin vermedikçe sohbete alınmaz. Asistan UYAP'a bağlanmaz.",
    "akademisyen": "ArthurMask kuruluysa kişisel veri içeren belgeler için kullanılabilir; ancak değerlendirme altındaki "
                   "gizli müsvedde, proje önerisi, tez ya da hakem materyali maskeli olsa bile sohbete alınmaz "
                   "(SYSTEM_PROMPT, ÜYZ Kapısı).",
}


class Bilgi:
    def __init__(self, surum_dizini, firma_dizini):
        self.paketler = surum_dizini / "paketler"
        self.firma = firma_dizini
        self.firma_bilgi = ortak.json_oku(firma_dizini / "firma.json")
        self._harita, self._metin, self._kilit = {}, {}, threading.Lock()

    def profiller(self):
        """Kurulumda seçilen ve bu sürümde bulunan paketler; sıra varsayılan profilin önceliğidir."""
        secili = ortak.moduller()
        return [p for p in ortak.PROFILLER if p in secili and (self.paketler / p / "SYSTEM_PROMPT.md").exists()]

    def varsayilan(self, mevcut=None):
        """Profil verilmeden çağrılınca: ayardaki varsayılan kuruluysa o, değilse ilk kurulu paket. Yalnız Courthouse
        seçilmiş bir bilgisayarda Courthouse'tur."""
        mevcut = self.profiller() if mevcut is None else mevcut
        istenen = ortak.ayar().get("varsayilan_profil")
        return istenen if istenen in mevcut else (mevcut[0] if mevcut else "")

    def paket_sorunu(self):
        """Hiçbir paket yüklenemiyorsa nedeni; en az biri yüklenebiliyorsa None.

        profiller() iki şeyi birlikte ister: paket seçilmiş olmalı (moduller.json) ve çalışan sunucunun sürüm
        klasöründe durmalı. Üç yol boş listeye götürür:
        - "surum": sürüm klasöründe hiç paket yok. Sunucu açıkken klasörü silinmiştir (iki güncelleme arasında
          uygulama hiç kapanmadıysa güncelleyici "iki önceki" diye çalışan sunucunun klasörünü siliyordu; bkz.
          guncelle.eski_surumleri_sil) ya da klasör eksik açılmıştır.
        - "secim": seçim dosyasında paket yok (elle düzenlenmiş ya da başka bir araçla yazılmış moduller.json;
          ortak.moduller_yaz bunu reddeder ama ortak.moduller okurken denetlemez).
        - "uyusmazlik": seçilen paket bu sürümde yok (paketlerin bir kısmıyla derlenmiş kurulum; seçim dosyası
          yokken varsayılan sayılan Hukuk Bürosu ve Kurumsal'ın derlemede bulunmaması).
        yeniden_acmak_yeter: uygulama yeniden açılınca başlayacak sürümde (bin/al.py'nin seçeceği) seçili paket var."""
        if self.profiller():
            return None
        secili = [p for p in ortak.PAKETLER if p in ortak.moduller()]
        surumde = [p for p in ortak.PAKETLER if (self.paketler / p / "SYSTEM_PROMPT.md").exists()]
        sonraki = sonraki_surum_dizini()
        return {"sorun": "surum" if not surumde else ("secim" if not secili else "uyusmazlik"),
                "secilen": secili, "surumde": surumde,
                "yeniden_acmak_yeter": bool(sonraki and sonraki.resolve() != self.paketler.parent.resolve() and any(
                    (sonraki / "paketler" / p / "SYSTEM_PROMPT.md").exists() for p in secili))}

    def profil(self, istenen):
        mevcut = self.profiller()
        if not mevcut:
            raise Hata(-32603, "Bu kurulumda paket yok.")
        if not istenen:
            return self.varsayilan(mevcut)
        if istenen not in mevcut:
            raise Hata(-32602, f"Bu kurulumda olmayan profil: {istenen}. Kurulu olanlar: {', '.join(mevcut)}")
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

    @staticmethod
    def _profil_dosyasi(profil, h):
        """Paketin kendi profil dosyası (büro, şirket, mahkeme, akademisyen)."""
        if profil == "adliye":
            turler = any(k.startswith("knowledge/profiles/") for k in h)
            return ("mahkeme bilgisi `knowledge/mahkeme-profili.md` dosyasındadır"
                    + ("; mahkeme türüne göre ayrıntı `knowledge/profiles/` altındadır." if turler else "."))
        if profil == "akademisyen":
            return "akademisyen bilgisi `knowledge/akademisyen-profili.md` dosyasındadır."
        return "büro bilgisi `knowledge/firm-profile.md` (Corporate'ta `knowledge/company-profile.md`) dosyasındadır."

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
            "Metinde geçen `~/.claude/plugins/config/...` yolları bu kurulumda yoktur; " + self._profil_dosyasi(profil, h),
            "Araştırma araçları (`tr_`, `az_`, `eu_`, `uk_` ... önekli) ve `status` bu `arthurlegal-yerel` sunucusundan "
            "gelir. Aynı araçlar ayrıca claude.ai connector'ı olarak görünüyorsa bu sunucudakini kullan.",
            ("Tapu, parsel ve harç işlerinde `arthur-tapu` yerel araçlarını kullan; `tkgm_` önekli uzak araçları kullanma. "
             "Parseli `parsel_sorgula` (il/ilçe/mahalle + ada/parsel ya da `metin`), `konumdan_parsel` ve `yer_bul` TKGM "
             "Parsel Sorgu'dan canlı getirir: kullanıcıdan GeoJSON/KML dosyası isteme. Sohbetteki ilk canlı çağrı onay "
             "kartı döndürür; kartı olduğu gibi göster, kabulde `onay=true` ile yinele ve o sohbette `onay=true` gönder. "
             "Tapu kaydı metni (`tapu_kaydi_oku`) bilgisayardan çıkmaz. Ayrıntı: `tapu-kadastro-rehberi.md`."
             if ortak.bilesen_var("tapu") else
             "Bu kurulumda ArthurLegal Tapu seçilmedi; `tkgm_` önekli uzak araçları da kullanma. Taşınmaz ya da parsel "
             "bilgisi gerekiyorsa uydurma, `UYARI: veri çekilemedi, teyidiniz gerekli: https://parselsorgu.tkgm.gov.tr/` "
             "yaz."),
            MASK_MADDESI.get(profil, MASK_MADDESI["hukuk-burosu"]),
        ]
        if ortak.hafiza_acik():
            maddeler.append(hafiza.talimat_maddesi())
        oteki =[p for p in self.profiller() if p != profil]
        if oteki:
            maddeler.append(
                "Bu bilgisayarda başka paketler de kurulu: " + "; ".join(f"`{p}` = {PROFIL_ACIKLAMASI[p]}" for p in oteki)
                + ". İstenen iş o paketlerden birine aitse `arthurlegal_talimat`'ı o profille yeniden çağır.")
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


# ---------------------------------------------------------------------------- paket yüklenemediğinde

# Paket (sistem talimatı ve bilgi dosyaları) okunamıyorsa arthurlegal_talimat hata döndürmez. Hata, asistanın cevabın
# sonuna düştüğü tek satırlık bir nota dönüşüyor ve sohbet ArthurLegal'in hiçbir kuralı olmadan sürüyordu. Bunun yerine
# (a) en ağır hataları önleyen kısa bir çekirdek kural metni ve (b) asistanın ilk cevabının başında kullanıcıya aynen
# ileteceği onarım cümlesi döner. Metin paketin yerine geçmez; paketteki karşılıkları SYSTEM_PROMPT'un "Üretim
# ilkeleri"ndedir (madde doğrulama kapısı, karar künyesi kapısı, canlı veri uyarısı, içtihat araştırma disiplini).
CEKIRDEK_KURALLAR = (
    "1. Taslak. Her çıktı taslaktır: hukukçunun değerlendirmesi için malzemedir, kendi başına hukuki tavsiye değildir.\n"
    "2. Madde atfı kapısı. Bir kanun maddesini (not, sözleşme, dilekçe ya da karar gövdesi dâhil) yazmadan önce "
    "`tr_mevzuat_madde_getir` ile metnini ve başlığını çek; yanıttaki `citation` birebir yazılır. Maddeye yüklediğin "
    "içerik (hakkın ya da yükümlülüğün sahibi, şart, süre, sonuç) okunan başlık ve metinle örtüşmeli, madde mülga "
    "olmamalıdır. Çekilemeyen madde ezberden yazılmaz.\n"
    "3. Karar künyesi kapısı. Çıktıda geçen her Türk yargı kararı künyesi (mahkeme ya da daire, esas, karar, tarih) bu "
    "sohbette `tr_` araçlarıyla bulunmuş olmalıdır: esas, karar ve tarih aynı kayıtta eşleşir, yanıttaki `citation` "
    "birebir yazılır. Yalnız esas numarasının bulunması doğrulama değildir. Bulunamayan künye tamamlanmaz, düzeltilmez, "
    "tahmin edilmez.\n"
    "4. UYARI satırı. Bir hukuki bilgi bu sohbette araçla çekilemediyse (araç yok, hata, iptal, onay yok ya da bilgi "
    "hafızadan geliyor) boşluk tahminle doldurulmaz; bilginin hemen ardından açıkça ve tam olarak şu yazılır: "
    "`UYARI: veri çekilemedi, teyidiniz gerekli: <bağlantı>`. Bağlantı aracın `source_url`'si ya da kaynağın resmî giriş "
    "sayfasıdır (mevzuat: https://www.mevzuat.gov.tr/ ; Yargıtay kararları: https://karararama.yargitay.gov.tr/). "
    "Bağlantı uydurulmaz, köşeli ayraçlı etiket (\"[doğrulayın]\" gibi) kullanılmaz.\n"
    "5. İçtihat araması. (a) `tr_ictihat_ara` ilgiye göre sıralar (`sort=\"ilgi\"`, varsayılan); güncel uygulama için "
    "aynı sorguyu `sort=\"yeni\"` ile yinele. `tr_ictihat_semantik_ara` keşif aracı değildir: yalnız ilk 5 ile 10 adayı "
    "okur, orada sonuç çıkmaması karar olmadığını göstermez. (b) Soruyu mahkemenin kendi diliyle kur ve en az üç farklı "
    "ifadeyle ara; bulduğun ilgili kararın kalıp cümlesini tırnak içinde yeniden arat. (c) Kullanıcının istediği sonucu "
    "destekleyen kararla yetinme: aksi yöndeki kararı ayrıca ara ve bulduğunu yaz; \"şunu çürüt\" isteğinde bile önce "
    "karşı görüşün doğru olup olmadığını ara. (d) \"Karar bulunamadı\" derken kaç sorgu yaptığını, hangi ifadeleri "
    "kullandığını ve kaç adaydan kaçını okuduğunu yaz; bulunamaması kararın yokluğu sayılmaz. (e) Kıyasla ya da genel "
    "hükümden vardığın sonucu yerleşik içtihat gibi sunma. (f) Süreli işte (itiraz, dava, istinaf, temyiz) dilekçeyi "
    "teyit edilmemiş bir önermeye dayandırmadan önce bunu kullanıcıya açıkça söyle.")

SORUN_ACIKLAMASI = {
    "surum": "çalışan sunucunun sürüm klasöründe paket dosyaları yok (klasör güncelleme sırasında silinmiş ya da eksik "
             "açılmış)",
    "secim": "seçim dosyasında (moduller.json) asistan paketi yok",
    "uyusmazlik": "seçilen paket bu sürümde yok",
}

# Onarım cümlesinin parçaları, arayüzün dilinde (ortak.arayuz_dili). Uygulama, bu sunucuyu çalıştıran uygulamadır
# (Claude Desktop ya da ChatGPT). Windows'ta ikisi de sistem tepsisinde açık kalır; macOS'ta Cmd+Q ile çıkılır
# (kurulum/rehber*.html'deki anlatımla aynı).
_KAPAT_AC = {
    "tr": {(False, False): "Claude Desktop'u sistem tepsisindeki simge dâhil tamamen kapatıp yeniden açın",
           (False, True): "Claude Desktop'tan Cmd+Q ile çıkıp yeniden açın",
           (True, False): "ChatGPT'yi sistem tepsisindeki simge dâhil tamamen kapatıp yeniden açın",
           (True, True): "ChatGPT'den Cmd+Q ile çıkıp yeniden açın"},
    "en": {(False, False): "quit Claude Desktop completely, including the system tray icon, and open it again",
           (False, True): "quit Claude Desktop with Cmd+Q and open it again",
           (True, False): "quit ChatGPT completely, including the system tray icon, and open it again",
           (True, True): "quit ChatGPT with Cmd+Q and open it again"},
    "az": {(False, False): "Claude Desktop-u sistem treyindəki nişan da daxil olmaqla tamamilə bağlayıb yenidən açın",
           (False, True): "Claude Desktop-dan Cmd+Q ilə çıxıb yenidən açın",
           (True, False): "ChatGPT-ni sistem treyindəki nişan da daxil olmaqla tamamilə bağlayıb yenidən açın",
           (True, True): "ChatGPT-dən Cmd+Q ilə çıxıb yenidən açın"},
}
# Kurulum yeniden çalışınca sürüm klasörünü paketleriyle yeniden yazar ve modül ekranında en az bir paket ister
# (kurulum/ArthurLegal.iss ModulPaketGerekli; kur.py --moduller, ortak.secim_coz). Güncelleme denetimi bu durumu
# onarmaz: güncelleyici yalnız daha yeni bir sürüm varsa paket indirir (guncelle.paket_guncelle). Eski bir kurulum
# dosyası da onarmaz, çünkü kurulum en yeni sürüm klasörünü etkin bırakır (kur.py --kurulum): cümle güncel kurulumu ister.
# Çiftin ilki genel kurulum (cümlede ardından ": <indirme sayfası>"), ikincisi büroya özel kurulum (ardından nokta);
# masanın paket uyarısı aynı metni adım olarak, adresi düğme olarak gösterir (paket_bilgisi).
_KURULUM = {
    "tr": ("güncel {urun} kurulumunu yeniden çalıştırıp en az bir asistan paketi seçin",
           "{urun} kurulum dosyasını yeniden çalıştırıp en az bir asistan paketi seçin"),
    "en": ("run the current {urun} installer again and select at least one assistant package",
           "run the {urun} installer again and select at least one assistant package"),
    "az": ("cari {urun} quraşdırmasını yenidən işə salıb ən azı bir köməkçi paketi seçin",
           "{urun} quraşdırma faylını yenidən işə salıb ən azı bir köməkçi paketi seçin"),
}
_ONARIM = {
    "tr": ("{urun} paketi bu oturumda yüklenemedi, bu cevap paketin tam kuralları olmadan hazırlandı; onarmak için "
           "{kapat_ac}, sorun sürerse {kurulum}",
           "{urun} paketi bu kurulumda yüklenemiyor, bu cevap paketin tam kuralları olmadan hazırlandı; onarmak için "
           "{kurulum}"),
    "en": ("The {urun} package could not be loaded in this session, so this answer was prepared without the package's "
           "full rules; to repair it, {kapat_ac}, and if the problem continues {kurulum}",
           "The {urun} package cannot be loaded in this installation, so this answer was prepared without the package's "
           "full rules; to repair it, {kurulum}"),
    "az": ("{urun} paketi bu sessiyada yüklənə bilmədi, bu cavab paketin tam qaydaları olmadan hazırlanıb; düzəltmək "
           "üçün {kapat_ac}, problem davam edərsə {kurulum}",
           "{urun} paketi bu quraşdırmada yüklənə bilmir, bu cavab paketin tam qaydaları olmadan hazırlanıb; düzəltmək "
           "üçün {kurulum}"),
}


def sonraki_surum_dizini():
    """Uygulama yeniden açılınca başlayacak sürüm klasörü (bin/al.py etkin_dizin ile aynı kural): aktif.txt'deki
    sürüm geçerliyse o, değilse en yeni geçerli sürüm; hiç yoksa None."""
    gecerli = ortak.surumler()
    etkin = ortak.aktif()
    ad = etkin if etkin in gecerli else (gecerli[-1] if gecerli else "")
    return ortak.KOK / "surumler" / ad if ad else None


def onarim_cumlesi(sorun: dict, ev=None, dil=None) -> str:
    """Kullanıcıya aynen iletilecek onarım cümlesi. Sunucunun klasörü silinmişse ve diskte paketi olan daha yeni bir
    sürüm bekliyorsa önce uygulamayı kapatıp açmak yeter (yeni sunucu o sürümden başlar); öteki hâllerde kurulum
    yeniden çalıştırılır. Genel kurulumda indirme sayfasının adresi verilir; büroya özel kurulumda (kendi dağıtımı
    olan) adres verilmez, büronun kurulum dosyası istenir.

    Bu yol sürüm klasörü silinmişken de çalışmalıdır: yalnız süreç başlarken yüklenmiş modüllere dayanır, burada yeni
    bir modül içe aktarılmaz (silinmiş klasörden içe aktarma başarısız olur)."""
    dil = dil if dil in ortak.DILLER else ortak.arayuz_dili()
    urun, adres = ortak.urun_adi(), _kurulum_adresi()
    kurulum = _KURULUM[dil][0 if adres else 1].format(urun=urun) + (": " + adres if adres else ".")
    if sorun.get("yeniden_acmak_yeter"):
        return _ONARIM[dil][0].format(urun=urun, kapat_ac=_KAPAT_AC[dil][(ev == "chatgpt", ortak.MAC)], kurulum=kurulum)
    return _ONARIM[dil][1].format(urun=urun, kurulum=kurulum)


def _kurulum_adresi():
    """Genel kurulumda indirme sayfası; büroya özel kurulumda (kendi dağıtımı ya da adı olan) None."""
    if ortak.ayar().get("dagitim_deposu") or ortak.urun_adi() != ortak.URUN_VARSAYILAN:
        return None
    return ortak.KURULUM_SAYFASI_MAC if ortak.MAC else ortak.KURULUM_SAYFASI


def paket_bilgisi(sorun: dict, ev=None) -> dict:
    """Masanın paket uyarısı için (al_arayuz.paket_uyarisi): sorun ve onarım adımları, üç dilde. Adımlar onarım
    cümlesiyle aynı parçalardır; kapat_ac yalnız uygulamayı yeniden açmak yetiyorsa vardır. Masa, kullanıcının
    seçtiği dile göre birini gösterir. onarim_cumlesi gibi yalnız bellekteki modüllere dayanır."""
    urun, adres = ortak.urun_adi(), _kurulum_adresi()
    yeter = bool(sorun.get("yeniden_acmak_yeter"))
    adimlar = {}
    for dil in ortak.DILLER:
        adim = {"kurulum": _KURULUM[dil][0 if adres else 1].format(urun=urun)}
        if yeter:
            adim["kapat_ac"] = _KAPAT_AC[dil][(ev == "chatgpt", ortak.MAC)]
        adimlar[dil] = adim
    out = {"sorun": sorun["sorun"], "yeniden_acmak_yeter": yeter, "adimlar": adimlar}
    if adres:
        out["adres"] = adres
    return out


def cekirdek_talimat(sorun: dict, ev=None) -> str:
    """arthurlegal_talimat'ın paket yüklenemediğindeki cevabı: onarım cümlesi ve çekirdek kurallar."""
    return (
        "# ArthurLegal — çekirdek kurallar (paket yüklenemedi)\n"
        f"Yerel kurulum {ortak.SURUM_DIZINI.name}. Bu bilgisayardaki ArthurLegal paketi (sistem talimatı ve bilgi "
        f"dosyaları) okunamadı: {SORUN_ACIKLAMASI[sorun['sorun']]}. Paketin tam kuralları, becerileri ve rehberleri bu "
        "sohbette YOK; `arthurlegal_bilgi_ara` ve `arthurlegal_bilgi_getir` de çalışmaz. Aşağıdaki çekirdek kurallar "
        "onların yerine geçmez, yalnız en ağır hataları önler; bu sohbetin sistem talimatı olarak uygula. Araştırma "
        "araçları (`tr_`, `eu_` ... önekli) bu durumdan etkilenmez.\n\n"
        "KULLANICIYA BİLDİRİM (zorunlu). İlk cevabının EN BAŞINA, başka hiçbir şeyden önce, aşağıdaki cümleyi aynen yaz: "
        "kısaltma, başka dile çevirme, cevabın sonuna ya da dipnota taşıma. Kullanıcı sonraki mesajlarda süreli bir iş "
        "(itiraz, dava, istinaf, temyiz) için belge isterse aynı cümleyi o cevabın başında yinele. Kullanıcı onardığını "
        "söylerse `arthurlegal_talimat`'ı yeniden çağır.\n\n"
        f"> {onarim_cumlesi(sorun, ev)}\n\n"
        "## Çekirdek kurallar\n" + CEKIRDEK_KURALLAR + "\n")


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

TALIMAT_KONULARI = "Türk veya yabancı hukuk, sözleşme, dilekçe, mevzuat, içtihat, süre, KVKK, iş, vergi, ceza, idare, şirketler, tapu, UYAP"
EK_KONULAR = {"adliye": "gerekçeli karar, tensip, müzekkere, tebligat, duruşma, dosya belgesi",
              "akademisyen": "makale, tez, atıf, dergi, proje başvurusu"}


def yerel_araclar(profiller, varsayilan):
    """Yerel araçlar, bu bilgisayarda kurulu paketlere göre: profil seçenekleri yalnız kurulu paketlerdir ve
    talimat aracının açıklaması hangi işte hangi profilin verileceğini söyler."""
    profiller = list(profiller) or list(ortak.ESKI_SECIM[:2])
    ozellik = {"type": "string", "enum": profiller,
               "description": ", ".join(f"{p} = {PROFIL_ACIKLAMASI[p]}" for p in profiller)}
    konular = ", ".join([TALIMAT_KONULARI] + [EK_KONULAR[p] for p in profiller if p in EK_KONULAR]
                        + (["müvekkil belgesi"] if {"hukuk-burosu", "kurumsal"} & set(profiller) else []))
    oteki = [p for p in profiller if p != varsayilan]
    secim = ("profil verme: kurulumda seçilen varsayılan (" + (varsayilan or profiller[0]) + ") kullanılır"
             + ("; istenen iş başka bir kurulu pakete aitse o profili ver: "
                + "; ".join(f"profil=\"{p}\" = {PROFIL_ACIKLAMASI[p]}" for p in oteki) if oteki else "") + ".")
    araclar = [
        {"name": "arthurlegal_talimat",
         "description": "ÖNCE BU ARACI ÇAĞIR. Bu bilgisayarda ArthurLegal hukuk asistanı kurulu. Kullanıcı hukukla ilgili "
                        f"herhangi bir şey sorduğunda ya da istediğinde ({konular}) cevap vermeden önce ilk iş bu aracı "
                        "çağır ve dönen metni bu sohbetin sistem talimatı olarak eksiksiz uygula. Sohbet başına bir kez "
                        "yeterli. Proje gerekmez. " + secim,
         "inputSchema": {"type": "object", "properties": {"profil": ozellik}}},
        {"name": "arthurlegal_bilgi_ara",
         "description": "Paketin bilgi dosyalarında (skills, references, profiles, agents, büro kuralları) Türkçe karakter "
                        "duyarsız anahtar kelime araması yapar; dosya yolu ve eşleşen satırları döndürür.",
         "inputSchema": {"type": "object", "properties": {
             "sorgu": {"type": "string"}, "profil": ozellik,
             "en_fazla": {"type": "integer", "minimum": 1, "maximum": 20, "default": 8}}, "required": ["sorgu"]}},
        {"name": "arthurlegal_bilgi_getir",
         "description": "Bir bilgi dosyasını getirir (ör. knowledge/references/hmk-rehberi.md). `bolum` verilirse yalnız o "
                        "başlığın bölümü döner; skill komutları için bolum=\"/eklenti:komut\". Uzun dosyalar `baslangic` ile "
                        "parça parça okunur.",
         "inputSchema": {"type": "object", "properties": {
             "yol": {"type": "string"}, "profil": ozellik, "bolum": {"type": "string"},
             "baslangic": {"type": "integer", "minimum": 0}}, "required": ["yol"]}},
        {"name": "arthurlegal_durum",
         "description": "Yerel kurulumun durumu: seçilen modüller, paket ve bileşen sürümleri, paketin yüklenip "
                        "yüklenemediği (yüklenemiyorsa nedeni ve onarım adımı), son güncelleme denetimi, araştırma "
                        "sunucusu bağlantısı.",
         "inputSchema": {"type": "object", "properties": {}}},
    ]
    for a in araclar:
        a["annotations"] = {"readOnlyHint": True, "destructiveHint": False, "openWorldHint": False}
    # Hafıza araçları kendi işaretleriyle gelir: yazanlar salt okunur değildir, Claude Desktop izin sorar.
    return araclar + (hafiza.araclar() if ortak.hafiza_acik() else [])

def salt_okunur_isaretle(araclar):
    """Köprülenen araştırma araçları yalnız okur (arama, getirme, sayma): uzak sunucu işaret koymadıysa
    readOnlyHint (ve dış kaynağa gittiği için openWorldHint) eklenir. Claude Desktop kalıcı "Always allow" iznini
    salt okunur araçlara sunar; işaretsiz araç her sohbette yeniden izin isteyebilir. Uzak sunucu bir aracı açıkça
    yazan (readOnlyHint false) ya da yıkıcı (destructiveHint true) diye işaretlediyse işarete dokunulmaz."""
    sonuc = []
    for arac in araclar or []:
        arac = dict(arac)
        isaret = dict(arac.get("annotations") or {})
        if "readOnlyHint" not in isaret and not isaret.get("destructiveHint"):
            isaret["readOnlyHint"] = True
        # Üç işaret her araçta açıkça yazılır (OpenAI dizin kuralı): araştırma araçları resmî kaynaklara, yani açık
        # dünyaya gider; uzak sunucunun açıkça koyduğu değere dokunulmaz.
        isaret.setdefault("readOnlyHint", False)   # yıkıcı işaretli araç salt okunur değildir
        isaret.setdefault("destructiveHint", False)
        isaret.setdefault("openWorldHint", True)
        arac["annotations"] = isaret
        sonuc.append(arac)
    return sonuc


def isaretleri_tamamla(araclar):
    """Bu bilgisayardaki araçlar: eksik işaret temkinli değerle yazılır (salt okunur sayılmaz, yıkıcı değil, dışarı
    çıkmaz). Açıkça konmuş işarete dokunulmaz; sözlükler kopyalanır."""
    sonuc = []
    for arac in araclar or []:
        isaret = {"readOnlyHint": False, "destructiveHint": False, "openWorldHint": False, **(arac.get("annotations") or {})}
        sonuc.append({**arac, "annotations": isaret})
    return sonuc


# ChatGPT (16.11.2026, K25). Kurulumun ChatGPT ayarı AL_EV=chatgpt yazar; yazmasa da ChatGPT/Codex kendini initialize'da
# tanıtır. ChatGPT'de görünümü yalnız al_masasi taşır, soru/adımlar/cevap bu süreçte bellekte tutulur (al_arayuz.CanliMasa).
def ev_ayari():
    return "chatgpt" if str(os.environ.get("AL_EV") or "").strip().lower() == "chatgpt" else None


def sonuc_verisi(sonuc):
    """Araç sonucunun JSON verisi (yapılandırılmış ya da metin bloğundaki), adım özeti için; yoksa None."""
    if not isinstance(sonuc, dict) or sonuc.get("isError"):
        return None
    if isinstance(sonuc.get("structuredContent"), dict):
        return sonuc["structuredContent"]
    metin = "".join(b.get("text", "") for b in sonuc.get("content") or [] if isinstance(b, dict) and b.get("type") == "text")
    try:
        veri = json.loads(metin)
    except ValueError:
        return None
    return veri if isinstance(veri, dict) else None


def sonuc_hatasi(sonuc):
    if isinstance(sonuc, dict) and sonuc.get("isError"):
        return "".join(b.get("text", "") for b in sonuc.get("content") or [] if isinstance(b, dict))[:200] or "hata"
    return None


# ---------------------------------------------------------------------------- AL Masası

# Sonucu kart verisi (structuredContent) taşıyan uzak araçlar ve masanın doğrudan çağırdıkları.
KARTLI_UZAK = ("tr_mevzuat_madde_getir", "tr_ictihat_ara")
MASA_UZAK = ("tr_mevzuat_madde_getir", "tr_mevzuat_ara", "tr_mevzuat_icindekiler", "tr_ictihat_ara", "tr_ictihat_getir",
             "tr_kurum_karari_ara", "tr_kurum_karari_getir", "tr_semantik_ara", "tr_belge_getir",
             "tr_spk_bulten_icinde_ara", "status",
             "hesap_kalemleri", "hesap_vekalet_ucreti", "hesap_yargi_harci", "hesap_faiz", "hesap_iscilik_alacagi",
             "tr_resmi_gazete_fihrist")
MODUL_KOMUTU = {"tapu": "tapu", "uyap": "uyap-ekran", "mask": "mask"}


def gorunum_ev(ev):
    """al_arayuz.arac_meta'ya verilecek ev değeri: ChatGPT'de masaüstü düzeni; eski arayüz kopyasında hiç verilmez."""
    return getattr(al_arayuz, "CHATGPT_MASAUSTU", None) if ev == "chatgpt" else None


def _arac_meta(ad, ev=None):
    gev = gorunum_ev(ev)
    return al_arayuz.arac_meta(ad, gev) if gev else al_arayuz.arac_meta(ad)


def masa_araclari(ev=None):
    """al_masasi (masayı açar) ve al_modul_ac (yerel modül penceresi). Arayüz klasörü yoksa yok."""
    if al_arayuz is None:
        return []
    # Açıklama bunun bilgisayardaki masa olduğunu söyler: aynı sohbette uzak arthurlegal-mcp de varsa Claude bunu seçer.
    masa = dict(al_arayuz.masa_araci("masaustu") if hasattr(al_arayuz, "MASA_ORTAM_NOTU") else al_arayuz.masa_araci())
    # ChatGPT'de model alanı yok (K14): modeller ölçülmedi, modelin kendi beyanı güvenilir değildir.
    modelsiz = getattr(al_arayuz, "modelsiz", None) if ev == "chatgpt" else None
    if modelsiz:
        masa = modelsiz(masa)
    masa["_meta"] = _arac_meta("al_masasi", ev)
    ac = {"name": "al_modul_ac", "title": "ArthurLegal modülünü aç",
          "description": "Bu bilgisayarda kurulu bir ArthurLegal modülünün penceresini açar: tapu (Tapu arayüzü), "
                         "uyap (UYAP Dashboard), mask (ArthurMask). Masadaki düğmeler kullanır.",
          "inputSchema": {"type": "object", "properties": {"modul": {"type": "string", "enum": list(MODUL_KOMUTU)}},
                          "required": ["modul"]},
          "annotations": {"readOnlyHint": False, "destructiveHint": False, "openWorldHint": False}}
    araclar = [masa, ac]
    # Cevabı masaya teslim (al_masaya_yaz): sohbet kaydı tam ekran masanın arkasında kalır, masa onu okuyamaz.
    # Eski arayüz kopyasında yoksa eklenmez.
    if hasattr(al_arayuz, "teslim_araci"):
        teslim = dict(al_arayuz.teslim_araci())
        meta = _arac_meta("al_masaya_yaz", ev)
        if meta:
            teslim["_meta"] = meta
        araclar.insert(1, teslim)
        # Soru araştırmadan önce masada (al_masada_basla); araçların adımları ve cevap ona eklenir.
        if hasattr(al_arayuz, "baslangic_araci"):
            basla = dict(al_arayuz.baslangic_araci())
            if modelsiz:
                basla = modelsiz(basla)
            meta = _arac_meta("al_masada_basla", ev)
            if meta:
                basla["_meta"] = meta
            araclar.insert(1, basla)
    # ChatGPT'de açık masa soruyu, adımları ve cevabı bu araçla yoklar (yalnız masa çağırır).
    if ev == "chatgpt" and hasattr(al_arayuz, "canli_araci"):
        araclar.append(al_arayuz.canli_araci())
    # Masa geçmişi (al_gecmis): yalnız bu bilgisayarda, veri/masa-gecmisi; eski arayüz kopyasında yoksa eklenmez.
    if hasattr(al_arayuz, "gecmis_araci"):
        araclar.append(al_arayuz.gecmis_araci())
        # Doğrulama kaydı (al_dogrulama_kaydi): geçmişteki atıf teyitlerini dosyaya döker; görünüm açmaz.
        araclar.append(dogrulama_kaydi.arac_tanimi())
    # Masanın dili (al_dil): kullanıcının bayraklardan seçtiği dil bu bilgisayarda kalır (veri/durum.json, masa_dili).
    if hasattr(al_arayuz, "dil_araci"):
        araclar.append(al_arayuz.dil_araci())
    # Masanın sağ üstündeki "Güncellemeleri denetle", Görünüm (Aa) ve Yardım (ⓘ) menüleri (3.3.1): masa çerçevesi
    # GitHub'a bağlanamaz; denetimi, güncellemeyi başlatmayı ve sistem bilgisini bu yerel araç yapar.
    araclar.append(GUNCELLEME_ARACI)
    return araclar


GUNCELLEME_ARACI = {
    "name": "al_guncelleme",
    "title": "ArthurLegal güncelleme ve görünüm",
    "description": (
        "ArthurLegal Masası'nın sağ üstündeki düğmelerin yerel aracı; masa kendisi çağırır. islem: denetle (yeni sürüm "
        "var mı; indirmez, kurmaz), guncelle (imzalı güncelleyiciyi arka planda başlatır; yeni sürüm Claude Desktop "
        "yeniden açılınca devreye girer), tani (destek için sistem bilgisi; belge ya da müvekkil bilgisi içermez), "
        "yenilikler (kurulu sürümün yenilikleri), tercih (yazı boyutu, yüksek karşıtlık, görülen yenilikler). "
        "Kullanıcı güncelleme isterse guncelle'yi ancak onun açık isteğiyle çağırın."),
    "inputSchema": {"type": "object", "properties": {
        "islem": {"type": "string", "enum": ["denetle", "guncelle", "tani", "yenilikler", "tercih"]},
        "zorla": {"type": "boolean", "description": "denetle: bir saatlik saklanan sonucu kullanma"},
        "yazi": {"type": "string", "enum": ["normal", "buyuk", "cok-buyuk"]},
        "karsitlik": {"type": "boolean"},
        "gorulen": {"type": "string", "description": "tercih: Yenilikler'i görülen masa sürümü"}},
        "required": ["islem"]},
    "annotations": {"readOnlyHint": False, "destructiveHint": False, "openWorldHint": True},
}


def guncelleme_islemi(a: dict) -> dict:
    """al_guncelleme'nin işi. guncelleyici aynı süreçte değil, ayrı süreçte çalışır: sunucu cevap vermeyi sürdürür ve
    güncelleyicinin kilidi ikinci bir başlatmayı zaten engeller."""
    import guncelle
    islem = a.get("islem")
    if islem == "denetle":
        return guncelle.denetle(bool(a.get("zorla")))
    if islem == "tani":
        return guncelle.tani()
    if islem == "yenilikler":
        return {**guncelle.kurulu_yenilikler(), "tercih": ortak.tercihler()}
    if islem == "tercih":
        alanlar = {k: a[k] for k in ("yazi", "karsitlik") if k in a}
        if a.get("gorulen"):
            alanlar["gorulen_yenilikler"] = {"masa": str(a["gorulen"])}
        return {"tercih": ortak.tercih_yaz(**alanlar) if alanlar else ortak.tercihler()}
    if islem == "guncelle":
        durum = guncelle.denetle()["guncelleme"]
        if durum["calisiyor"]:
            return {"basladi": False, "calisiyor": True}
        py = ortak.python_yolu()
        komut = [str(py if py.exists() else sys.executable), "-B", str(ortak.AL), "guncelle", "--sessiz"]
        ortak_ek = {"stdin": subprocess.DEVNULL, "stdout": subprocess.DEVNULL, "stderr": subprocess.DEVNULL, "close_fds": True}
        if sys.platform == "win32":
            # Claude Desktop sunucuyu bir iş nesnesinde (job) başlatabilir; kapanınca alt süreçleri de sonlandırır.
            # Güncelleyici işten koparılarak başlatılır (CREATE_BREAKAWAY_FROM_JOB); iş buna izin vermezse yarıda kalan
            # güncelleme zararsızdır (kilit iki saatte düşer, paket yeni klasöre açılır), bir sonraki denetim tamamlar.
            temel = ortak.PENCERESIZ | 0x00000200  # CREATE_NEW_PROCESS_GROUP
            try:
                subprocess.Popen(komut, creationflags=temel | 0x01000000, **ortak_ek)
            except OSError:
                subprocess.Popen(komut, creationflags=temel, **ortak_ek)
        else:
            subprocess.Popen(komut, start_new_session=True, **ortak_ek)
        ortak.gunluk("guncelle", "masadan elle başlatıldı")
        return {"basladi": True, "calisiyor": True}
    raise ValueError("islem: denetle, guncelle, tani, yenilikler ya da tercih olmalı")


_GECMIS = None


def masa_gecmisi():
    """Masa geçmişinin deposu; ilk çağrıda kurulur (klasör ilk kayıtta açılır)."""
    global _GECMIS
    if _GECMIS is None:
        _GECMIS = al_arayuz.Gecmis(str(ortak.VERI / "masa-gecmisi"))
    return _GECMIS


def dogrulama_dizini():
    """Doğrulama kaydı dosyalarının klasörü: ayardaki `dogrulama_dizini`, yoksa kullanıcı klasöründe sabit ad.
    Claude klasör seçemez; araç yalnız buraya yazar."""
    ozel = str(ortak.ayar().get("dogrulama_dizini") or "").strip()
    return Path(os.path.expanduser(ozel)) if ozel else Path.home() / dogrulama_kaydi.VARSAYILAN_AD


def dogrulama_kaydi_yaz(a):
    """al_dogrulama_kaydi: masa geçmişindeki atıf teyitlerini dosyaya yazar; içerik günlüğe yazılmaz."""
    try:
        veri = dogrulama_kaydi.disa_aktar(masa_gecmisi().klasor, str(dogrulama_dizini()), a,
                                          getattr(al_arayuz, "GECMIS_GUN", 90))
    except (ValueError, OSError) as e:  # KayitHatasi da ValueError'dır
        return {"content": [{"type": "text", "text": str(e)}], "isError": True}
    return {"content": [{"type": "text", "text": json.dumps(veri, ensure_ascii=False)}], "structuredContent": veri}


def gorunum_meta(araclar, ev=None):
    """Araçlara _meta.ui.resourceUri (al_arayuz.arac_meta): Claude'da bütün araçlar masayı açar, çünkü tam ekran
    bölmesi en son açılan görünümü gösterir ve kendi kartı olan araç masanın yerine geçerdi. Masa açıksa çağrı
    masada canlı adım olur; açık değilse aynı görünüm madde ve içtihatta kartı, ötekilerde tek satırı çizer.
    ChatGPT'de (ev="chatgpt") araştırma araçları görünüm açmaz: adım masaya bu süreçten gelir."""
    if al_arayuz is None:
        return araclar
    sonuc = []
    for arac in araclar:
        meta = _arac_meta(arac.get("name", ""), ev)
        if ev == "chatgpt" and not meta:   # köprülenen araçta uzak ucun görünüm işareti de kalkar
            kalan = {k: v for k, v in (arac.get("_meta") or {}).items() if k not in ("ui", "ui/resourceUri")}
            arac = {k: v for k, v in arac.items() if k != "_meta"}
            if kalan:
                arac["_meta"] = kalan
        sonuc.append({**arac, "_meta": {**(arac.get("_meta") or {}), **meta}} if meta else arac)
    return sonuc


def kopru_araclari(araclar, gorunumler=None):
    """Uzak uçtan köprülenen araçlar, bu sunucunun karşılayabildiği kadarıyla. Uzak ucun masa araçları (al_)
    listelenmez: masa yereldedir ve bu bilgisayarın modüllerini bilir. Görünüm işareti (_meta.ui) yalnız bu sunucu o
    ui:// görünümü veriyorsa kalır; klasik arayüzde hiçbiri kalmaz ve sonuç metin olarak gelir."""
    if gorunumler is None:
        gorunumler = set(al_arayuz.GORUNUMLER) if al_arayuz is not None else set()
    sonuc = []
    for arac in araclar or []:
        if arac.get("name", "").startswith("al_"):
            continue
        meta = arac.get("_meta") or {}
        ui = meta.get("ui") if isinstance(meta.get("ui"), dict) else {}
        uri = ui.get("resourceUri") or meta.get("ui/resourceUri")
        if uri and uri not in gorunumler:
            kalan = {k: v for k, v in meta.items() if k not in ("ui", "ui/resourceUri")}
            arac = {k: v for k, v in arac.items() if k != "_meta"}
            if kalan:
                arac["_meta"] = kalan
        sonuc.append(arac)
    return sonuc


def kart_verisi(ad, sonuc):
    """Kartlı aracın sonucu kart için structuredContent da taşır: uzak uç vermediyse metin bloğundaki JSON.
    Modelin okuduğu metin değişmez."""
    if (al_arayuz is None or ad not in KARTLI_UZAK or not isinstance(sonuc, dict) or sonuc.get("isError")
            or "structuredContent" in sonuc):
        return sonuc
    metin = "".join(b.get("text", "") for b in sonuc.get("content") or [] if b.get("type") == "text")
    try:
        veri = json.loads(metin)
    except ValueError:
        return sonuc
    return {**sonuc, "structuredContent": veri} if isinstance(veri, dict) else sonuc


def masa_modulleri():
    """Masa panelinin modül durumları, bu kurulumun seçimine göre."""
    hazir = lambda var: "hazir" if var else "kurulu-degil"  # noqa: E731
    return {
        "tapu": {"durum": "hazir" if ortak.bilesen_var("tapu") else "claude"},
        "beyin": {"durum": hazir(ortak.hafiza_acik())},
        "mask": {"durum": hazir(ortak.mask_surumu())},
        "uyap": ({"durum": "hazir", "ozet": ortak.uyap_ozeti()} if ortak.uyap_acik() else {"durum": "kurulu-degil"}),
        "donna": {"durum": "hazir"},
    }


TALIMAT = ("Bu bilgisayarda ArthurLegal hukuk asistanı kurulu. Kullanıcı hukukla ilgili bir şey sorduğunda, cevap vermeden "
           "önce `arthurlegal_talimat` aracını çağır ve dönen metni bu sohbetin sistem talimatı olarak uygula; proje gerekmez. "
           "Bilgi dosyaları `arthurlegal_bilgi_ara` / `arthurlegal_bilgi_getir` ile okunur. Araştırma araçları önekli "
           "adlarıyla (tr_, az_, eu_ ...) bu sunucudadır.")
HAFIZA_TALIMATI = (" ArthurLegal Hafıza açık: talimattan sonra `hafiza_baslangic` ile kullanıcının tercihlerini, "
                   "düzeltmelerini ve son oturum kartını yükle.")
MASA_TALIMATI = (" Kullanıcı 'ArthurLegal Masası'nı aç' derse ya da masayı, bir modülü (Mevzuat, İçtihat, ArthurTapu, "
                 "Beyin, ArthurMask, UYAP Dashboard, Donna) açmak isterse bu sunucunun `al_masasi` aracını çağır; uzak "
                 "arthurlegal-mcp bağlayıcısınınkini değil: Beyin, ArthurMask ve UYAP Dashboard yalnız bu bilgisayardaki "
                 "masada çalışır.")


class Sunucu:
    def __init__(self):
        self.bilgi = Bilgi(ortak.SURUM_DIZINI, ortak.FIRMA)
        self.uzak = Uzak(ortak.ayar()["uzak_mcp"])
        self.onbellek = ortak.VERI / "uzak_araclar.json"
        onbellek = ortak.json_oku(self.onbellek, {}).get("araclar")
        self.uzak_araclar = None if onbellek is None else salt_okunur_isaretle(onbellek)
        self.uzak_hata, self.baslatildi = None, False
        self._paket_sorunu_yazildi = False
        self._gorunum_onbellek, self._gorunum_kilit = None, threading.Lock()
        self.ev = ev_ayari()   # "chatgpt" ya da None (Claude); initialize'daki clientInfo da belirler
        self.canli = al_arayuz.CanliMasa() if al_arayuz is not None and hasattr(al_arayuz, "CanliMasa") else None
        self._yaz_kilit, self._yenile_kilit, self._liste_kilit = threading.Lock(), threading.Lock(), threading.Lock()
        self._yenileme_isi = None   # süren uzak liste yenilemesi (aynı anda tek tane: _yenileme)
        self._eksik_liste = False   # istemciye uzak araçlar olmadan liste verildi: liste gelince haber verilir
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
        try:
            # Başlangıç paneli Claude Desktop'ın gerçekte hangi sürümle çalıştığını gösterir: güncelleme
            # kurulduysa ama Claude Desktop yeniden açılmadıysa panel bunu söyler.
            ortak.durum_guncelle(calisan_surum=ortak.surum(), calisan_zaman=time.time())
        except OSError:
            pass
        if al_arayuz is not None:
            threading.Thread(target=self._gorunumleri_hazirla, daemon=True).start()
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
                    threading.Thread(target=self._uzak_baglan, daemon=True).start()
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
            yetenek = {"tools": {"listChanged": True}, "prompts": {"listChanged": False}}
            if al_arayuz is not None:
                yetenek["resources"] = {"listChanged": False}
            if self.ev is None and al_arayuz is not None and hasattr(al_arayuz, "ev_tani"):
                self.ev = "chatgpt" if al_arayuz.ev_tani(p.get("clientInfo")) == "chatgpt" else None
            # Model kuralı Claude'un ölçümüne dayanır; ChatGPT modelleri ölçülmedi (K7): orada yazılmaz.
            model = "" if self.ev == "chatgpt" else (" " + MODEL_KURALI if MODEL_KURALI else "")
            return {"protocolVersion": istenen if istenen in PROTOKOLLER else PROTOKOLLER[0],
                    "capabilities": yetenek,
                    "serverInfo": {"name": "arthurlegal-yerel", "version": ortak.surum()},
                    "instructions": TALIMAT + (MASA_TALIMATI + (" " + al_arayuz.TESLIM_KURALI if hasattr(al_arayuz, "TESLIM_KURALI") else "")
                                               if al_arayuz is not None else "")
                                    + (HAFIZA_TALIMATI if ortak.hafiza_acik() else "")
                                    + model}
        if metod == "ping":
            return {}
        if metod == "tools/list":
            if self.uzak_araclar is None:
                # İlk açılış: liste sınırlı süre beklenir. Yetişmezse yerel araçlar ve masa hemen verilir; uzak araçlar
                # gelince istemciye tools/list_changed gider (_uzak_yenile).
                self._yenileme().join(ILK_LISTE_BEKLEME)
            with self._liste_kilit:
                uzak = self.uzak_araclar or []
                self._eksik_liste = not uzak
            profiller = self.bilgi.profiller()
            return {"tools": isaretleri_tamamla(
                gorunum_meta(yerel_araclar(profiller, self.bilgi.varsayilan(profiller)), self.ev) + masa_araclari(self.ev))
                    + gorunum_meta(kopru_araclari(uzak), self.ev)}
        if metod == "tools/call":
            return self._arac(p.get("name", ""), p.get("arguments") or {})
        if metod == "prompts/list":
            return {"prompts": [{"name": pr, "description": f"ArthurLegal {ortak.PROFILLER[pr]} olarak başla (Project kullanmadan)"}
                                for pr in self.bilgi.profiller()]}
        if metod == "prompts/get":
            ad = p.get("name")
            if ad not in ortak.ONYUKLEME or ad not in self.bilgi.profiller():
                raise Hata(-32602, f"Bilinmeyen istem: {ad}")
            return {"messages": [{"role": "user", "content": {"type": "text", "text": ortak.ONYUKLEME[ad]}}]}
        if metod == "resources/templates/list":
            return {"resourceTemplates": []}
        if metod == "resources/list":
            return {"resources": [{k: v for k, v in g.items() if k != "text"} for g in self._gorunumler()]}
        if metod == "resources/read":
            g = next((g for g in self._gorunumler() if g["uri"] == p.get("uri")), None)
            if g is None:
                raise Hata(-32002, f"Bilinmeyen kaynak: {p.get('uri')}")
            return {"contents": [{"uri": g["uri"], "mimeType": g["mimeType"], "text": g["text"], "_meta": g["_meta"]}]}
        raise Hata(-32601, f"Desteklenmeyen yöntem: {metod}")

    def _gorunumler(self):
        """Masa ve kartların birleşmiş HTML'i; bir kez kurulur (açılışta _gorunumleri_hazirla)."""
        if al_arayuz is None:
            return []
        with self._gorunum_kilit:
            if self._gorunum_onbellek is None:
                self._gorunum_onbellek = al_arayuz.kaynaklar()
        return self._gorunum_onbellek

    def _gorunumleri_hazirla(self):
        """Görünümler açılışta belleğe alınır. Sunucu açıkken sürüm klasörü silinirse (paketin yüklenemediği en olası
        yol) masa dosyaları da gider; bellekteki masa yine açılır ve paket uyarısını gösterir."""
        try:
            self._gorunumler()
        except (OSError, ValueError, KeyError) as e:
            ortak.gunluk("sunucu", f"görünümler hazırlanamadı: {e!r}")

    def _masa_verisi(self, a):
        yetenekler = [t["name"] for t in (self.uzak_araclar or []) if t.get("name") in MASA_UZAK] + ["al_modul_ac"]
        if hasattr(al_arayuz, "Gecmis"):
            yetenekler.append("al_gecmis")
        if ortak.hafiza_acik():
            yetenekler += [t["name"] for t in hafiza.araclar()]
        if not hasattr(al_arayuz, "teslim_araci"):  # eski arayüz kopyası: teslim ve bağlayıcı listesi yok
            return al_arayuz.masa_cevabi("masaustu", yetenekler, masa_modulleri(), a.get("bolum"))
        yetenekler.append("al_masaya_yaz")
        if hasattr(al_arayuz, "baslangic_araci"):
            yetenekler.append("al_masada_basla")
        # Claude kendi model adını bildirir (al_masasi girdisi): masa önerilen modelle çalışılıp çalışılmadığını gösterir.
        ek = {"model": a.get("model")} if hasattr(al_arayuz, "model_degerlendir") else {}
        # Masa üç dillidir. Sıra: kullanıcının masada seçip bu bilgisayara kaydettiği dil (al_dil), Claude'un
        # bildirdiği dil, kurulumun dili. Kullanıcı masanın sağ üstündeki bayraklardan değiştirir.
        if hasattr(al_arayuz, "dil_gecerli"):
            ek["dil"] = (al_arayuz.dil_gecerli(ortak.durum().get("masa_dili")) or al_arayuz.dil_gecerli(a.get("dil"))
                         or ortak.dil())
        if hasattr(al_arayuz, "dil_araci"):
            yetenekler.append("al_dil")
        yetenekler.append("al_guncelleme")
        if self.ev == "chatgpt" and self.canli is not None:
            yetenekler.append("al_masa_durumu")
            ek["ev"] = al_arayuz.CHATGPT_MASAUSTU
        # Kurulum sağlığı (kalite süreci 4): paket yüklenemiyorsa masa her ekranda uyarır ve onarım adımlarını
        # gösterir. 18.11.2026 olayında paket hiç yüklenmemişti ve kimse fark etmemişti.
        if hasattr(al_arayuz, "paket_uyarisi"):
            try:
                sorun = self.bilgi.paket_sorunu()
            except (OSError, ValueError) as e:   # masa açılışı bu denetim yüzünden düşmez
                ortak.gunluk("sunucu", f"paket durumu okunamadı: {e!r}")
                sorun = None
            if sorun:
                ek["paket"] = paket_bilgisi(sorun, self.ev)
        return al_arayuz.masa_cevabi("masaustu", yetenekler, masa_modulleri(), a.get("bolum"), a.get("baglayicilar"), **ek)

    def _masa(self, a):
        veri = self._masa_verisi(a)
        return {"content": [{"type": "text", "text": json.dumps(veri, ensure_ascii=False)}], "structuredContent": veri}

    def _teslim(self, a):
        """al_masaya_yaz: cevap masada açılır ve o anda bu bilgisayardaki geçmişe yazılır (veri/masa-gecmisi).

        Kayıt masanın penceresine bağlı değildir: pencere atıf teyidi bitmeden kapansa da cevap geçmiştedir; masa
        teyidi bitirince aynı kaydı tamamlar. Cevap geri yazılmaz, masanın durumu döner. Geçmiş yazılamazsa teslim
        yine tamamlanır (kayıt kimliği dönmez, masa kaydı kendisi açar).
        """
        try:
            if hasattr(al_arayuz.Gecmis, "cevap_kaydet"):
                veri = al_arayuz.teslim_cevabi(a, self._masa_verisi({}), masa_gecmisi())
            else:  # eski arayüz kopyası: geçmişi yalnız masa yazar
                veri = al_arayuz.teslim_cevabi(a, self._masa_verisi({}))
        except ValueError as e:  # TeslimHatasi
            return {"content": [{"type": "text", "text": str(e)}], "isError": True}
        return {"content": [{"type": "text", "text": json.dumps(veri, ensure_ascii=False)}], "structuredContent": veri}

    def _basla(self, a):
        """al_masada_basla: soru araştırma başlamadan masada; sunucu soruyu saklamaz, masanın durumunu döndürür."""
        try:
            veri = al_arayuz.baslangic_cevabi(a, self._masa_verisi({}))
        except ValueError as e:  # TeslimHatasi
            return {"content": [{"type": "text", "text": str(e)}], "isError": True}
        return {"content": [{"type": "text", "text": json.dumps(veri, ensure_ascii=False)}], "structuredContent": veri}

    def _modul_ac(self, a):
        modul = str(a.get("modul") or "")
        komut = MODUL_KOMUTU.get(modul)
        if not komut:
            return {"content": [{"type": "text", "text": f"Bilinmeyen modül: {modul} (tapu, uyap, mask)"}], "isError": True}
        if masa_modulleri()[modul]["durum"] != "hazir":
            return {"content": [{"type": "text", "text": "Bu modül bu kurulumda yok."}], "isError": True}
        ortak.arka_planda([ortak.python_yolu(pencereli=True), "-B", ortak.AL, "kisayol", komut])
        mesaj = {"tapu": "Tapu arayüzü açılıyor.", "uyap": "UYAP Dashboard açılıyor.", "mask": "ArthurMask açılıyor."}
        return {"content": [{"type": "text", "text": json.dumps({"mesaj": mesaj[modul]}, ensure_ascii=False)}],
                "structuredContent": {"mesaj": mesaj[modul]}}

    def _arac(self, ad, a):
        """ChatGPT'de (K25) açık masa soruyu, adımları ve cevabı bu süreçten okur: her çağrı canlı masaya işlenir.
        Claude'da hiçbir şey tutulmaz (her araç kendi penceresinde masayı açar)."""
        canli = self.canli if self.ev == "chatgpt" else None
        if canli is None:
            return self._arac_calistir(ad, a)
        if ad == "al_masa_durumu":
            veri = canli.durum(a)
            return {"content": [{"type": "text", "text": json.dumps(veri, ensure_ascii=False)}], "structuredContent": veri}
        kimlik = None if ad.startswith("al_") else canli.adim_basladi(ad, a)
        try:
            sonuc = self._arac_calistir(ad, a)
        except Exception as e:
            if kimlik:
                canli.adim_bitti(kimlik, hata=str(e) or "hata")
            raise
        if kimlik:
            canli.adim_bitti(kimlik, sonuc_verisi(sonuc), sonuc_hatasi(sonuc))
        elif not (isinstance(sonuc, dict) and sonuc.get("isError")):
            if ad == "al_masada_basla":
                canli.basla(a)
            elif ad == "al_masaya_yaz":
                teslim = (sonuc.get("structuredContent") or {}).get("teslim") or {}
                canli.teslim(a, teslim.get("gecmis_id"))
        return sonuc

    def _arac_calistir(self, ad, a):
        if al_arayuz is not None and ad == "al_masasi":
            return self._masa(a)
        if al_arayuz is not None and ad == "al_modul_ac":
            return self._modul_ac(a)
        if al_arayuz is not None and ad == "al_masaya_yaz" and hasattr(al_arayuz, "teslim_araci"):
            return self._teslim(a)
        if al_arayuz is not None and ad == "al_masada_basla" and hasattr(al_arayuz, "baslangic_araci"):
            return self._basla(a)
        if al_arayuz is not None and ad == "al_gecmis" and hasattr(al_arayuz, "Gecmis"):
            try:
                veri = masa_gecmisi().cagir(a)
            except (ValueError, OSError) as e:  # GecmisHatasi da ValueError'dır; içerik günlüğe yazılmaz
                return {"content": [{"type": "text", "text": str(e)}], "isError": True}
            return {"content": [{"type": "text", "text": json.dumps(veri, ensure_ascii=False)}], "structuredContent": veri}
        if al_arayuz is not None and ad == "al_dil" and hasattr(al_arayuz, "dil_araci"):
            try:
                # Dil dört arayüzün ortak tercihidir (3.3.1): ArthurMask, UYAP Dashboard ve ArthurTapu da aynı dili açar.
                veri = al_arayuz.dil_cevabi(a, ortak.durum().get("masa_dili"),
                                            lambda d: (ortak.durum_guncelle(masa_dili=d), ortak.tercih_yaz(dil=d)))
            except (ValueError, OSError) as e:
                return {"content": [{"type": "text", "text": str(e)}], "isError": True}
            return {"content": [{"type": "text", "text": json.dumps(veri, ensure_ascii=False)}], "structuredContent": veri}
        if ad == "al_guncelleme":
            try:
                veri = guncelleme_islemi(a)
            except (ValueError, OSError, subprocess.SubprocessError) as e:
                return {"content": [{"type": "text", "text": str(e)}], "isError": True}
            return {"content": [{"type": "text", "text": json.dumps(veri, ensure_ascii=False)}], "structuredContent": veri}
        if al_arayuz is not None and ad == "al_dogrulama_kaydi" and hasattr(al_arayuz, "Gecmis"):
            return dogrulama_kaydi_yaz(a)
        if ad.startswith("al_"):  # uzak ucun masa araçları köprülenmez (kopru_araclari)
            metin = ("ArthurLegal Masası bu kurulumda kapalı (klasik arayüz). Kurulumu yeniden çalıştırıp "
                     "'ArthurLegal yeni arayüz'ü seçebilirsiniz." if al_arayuz is None else f"Bilinmeyen masa aracı: {ad}")
            return {"content": [{"type": "text", "text": metin}], "isError": True}
        yerel = {
            "arthurlegal_talimat": lambda: self.bilgi.talimat(self.bilgi.profil(a.get("profil"))),
            "arthurlegal_bilgi_ara": lambda: self.bilgi.ara(self.bilgi.profil(a.get("profil")), a.get("sorgu", ""),
                                                            max(1, min(20, int(a.get("en_fazla") or 8)))),
            "arthurlegal_bilgi_getir": lambda: self.bilgi.getir(self.bilgi.profil(a.get("profil")), a.get("yol", ""),
                                                                a.get("bolum"), a.get("baslangic", 0)),
            "arthurlegal_durum": self._durum,
        }
        if ad in yerel:
            sorun = self.bilgi.paket_sorunu() if ad != "arthurlegal_durum" else None
            if sorun:
                return self._paketsiz(ad, sorun)
            try:
                return {"content": [{"type": "text", "text": yerel[ad]()}]}
            except Hata as e:
                return {"content": [{"type": "text", "text": str(e)}], "isError": True}
        if ad.startswith("hafiza_"):
            if not ortak.hafiza_acik():
                return {"content": [{"type": "text", "text": "Bu kurulumda ArthurLegal Hafıza seçilmedi."}], "isError": True}
            try:
                return {"content": [{"type": "text", "text": hafiza.cagir(ad, a)}]}
            except KeyError:
                raise Hata(-32602, f"Bilinmeyen araç: {ad}") from None
            except (ValueError, OSError) as e:  # HafizaHatasi da ValueError'dır
                return {"content": [{"type": "text", "text": str(e)}], "isError": True}
        if ad.startswith("tkgm_"):
            metin = ("tkgm_ araçları bu kurulumda yerel arthur-tapu sunucusundadır." if ortak.bilesen_var("tapu") else
                     "Bu kurulumda ArthurLegal Tapu seçilmedi; parsel bilgisi bu kurulumdan alınamaz.")
            return {"content": [{"type": "text", "text": metin}], "isError": True}
        try:
            return kart_verisi(ad, self.uzak.cagir("tools/call", {"name": ad, "arguments": a}))
        except Hata as e:
            if e.kod == -32602 or "not found" in str(e).lower() or "unknown" in str(e).lower():
                raise
            return {"content": [{"type": "text", "text": f"Araştırma sunucusu hata verdi: {e}"}], "isError": True}
        except (OSError, urllib.error.URLError, ValueError) as e:
            ortak.gunluk("sunucu", f"uzak çağrı başarısız ({ad}): {e!r}")
            return {"content": [{"type": "text", "text": f"ArthurLegal araştırma sunucusuna ulaşılamadı ({e}). "
                                 "İnternet bağlantısını denetleyin; sonuç doğrulanmadan cevap vermeyin."}], "isError": True}

    def _yenileme(self) -> threading.Thread:
        """Süren uzak liste yenilemesini döndürür, yoksa başlatır: aynı anda tek yenileme çalışır. Çağıran dilediği
        kadar bekler (join); iş arka plan ipliğidir, sunucu kapanırken bekletmez."""
        with self._yenile_kilit:
            if self._yenileme_isi is None or not self._yenileme_isi.is_alive():
                self._yenileme_isi = threading.Thread(target=self._uzak_yenile, daemon=True)
                self._yenileme_isi.start()
            return self._yenileme_isi

    def _uzak_baglan(self):
        """Açılışta uzak araç listesini tazeler. Liste hiç alınamadıysa (ilk kurulum; ağ yok, yavaş ya da engelli)
        arka planda aralıklarla yeniden dener: ağ gelince araçlar önbelleğe yazılır ve istemciye haber verilir."""
        aralik, bekle = iter(YENIDEN_DENEME), 0
        while True:
            self._yenileme().join()
            if self.uzak_araclar is not None:
                return
            bekle = next(aralik, bekle)
            time.sleep(bekle)

    def _uzak_yenile(self):
        """Uzak araç listesini çeker (yalnız _yenileme üzerinden çağrılır). Alınamazsa eldeki liste (önbellek) kalır;
        hiç liste yoksa uzak_araclar None kalır ve tools/list yerel araçlarla cevap verir."""
        try:
            araclar = salt_okunur_isaretle([t for t in self.uzak.araclar() if not t.get("name", "").startswith("tkgm_")])
        except Exception as e:  # noqa: BLE001
            self.uzak_hata = str(e)
            ortak.gunluk("sunucu", f"uzak araç listesi alınamadı: {e!r}")
            return
        self.uzak_hata = None
        if araclar == self.uzak_araclar:
            return
        with self._liste_kilit:
            onceki, self.uzak_araclar = self.uzak_araclar, araclar
            # Liste değiştiyse ya da istemci açılışta uzak araçlar olmadan liste aldıysa yeniden istemesi söylenir.
            bildir = self.baslatildi and bool(onceki or self._eksik_liste)
            self._eksik_liste = False
        ortak.json_yaz(self.onbellek, {"zaman": time.time(), "araclar": araclar})
        if bildir:
            self.yaz({"jsonrpc": "2.0", "method": "notifications/tools/list_changed"})

    def _guncelleme_dongusu(self):
        if os.environ.get("ARTHURLEGAL_GUNCELLEME") == "0":
            return
        pythonw = ortak.python_yolu(pencereli=True)
        while pythonw.exists():
            aralik = float(ortak.ayar().get("denetim_araligi_saat", 6)) * 3600
            if time.time() - float(ortak.durum().get("son_denetim", 0)) > aralik:
                try:
                    ortak.arka_planda([pythonw, "-B", ortak.AL, "guncelle", "--sessiz"])
                except OSError as e:
                    ortak.gunluk("sunucu", f"güncelleyici başlatılamadı: {e!r}")
            time.sleep(1800)

    def _paketsiz(self, ad, sorun):
        """Paket yüklenemiyorken talimat ve bilgi araçları. Talimat hata değildir: çekirdek kurallar ve kullanıcıya
        iletilecek onarım cümlesi döner (cekirdek_talimat). Bilgi araçlarının okuyacağı dosya yoktur; hata metni aynı
        onarım cümlesini taşır. Neden günlüğe bir kez yazılır (yalnız modül adları ve sürüm numaraları): bu durum
        önceden hiçbir iz bırakmıyordu."""
        if not self._paket_sorunu_yazildi:
            self._paket_sorunu_yazildi = True
            ortak.gunluk("sunucu", f"hata: paket yüklenemedi ({sorun['sorun']}); seçilen {sorun['secilen']}, sürüm "
                                   f"klasöründe {sorun['surumde']}; çalışan {ortak.SURUM_DIZINI.name}, etkin "
                                   f"{ortak.aktif() or '-'}, sürümler {ortak.surumler()}")
        if ad == "arthurlegal_talimat":
            return {"content": [{"type": "text", "text": cekirdek_talimat(sorun, self.ev)}]}
        metin = ("ArthurLegal paketi yüklenemediği için bilgi dosyaları okunamıyor (" + SORUN_ACIKLAMASI[sorun["sorun"]]
                 + "). Okunamayan dosyanın içeriğini varsaymayın; `arthurlegal_talimat` çekirdek kuralları verir. "
                 "Kullanıcıya aynen iletilecek onarım adımı: " + onarim_cumlesi(sorun, self.ev))
        return {"content": [{"type": "text", "text": metin}], "isError": True}

    def _paket_durumu(self):
        """arthurlegal_durum için: paket yüklenebiliyorsa "tamam", yüklenemiyorsa nedeni ve onarım adımı."""
        sorun = self.bilgi.paket_sorunu()
        if not sorun:
            return "tamam"
        return {"durum": "PAKET YÜKLENEMİYOR: arthurlegal_talimat yalnız çekirdek kuralları verir",
                "neden": SORUN_ACIKLAMASI[sorun["sorun"]],
                "secilen_paketler": sorun["secilen"], "surum_klasorundeki_paketler": sorun["surumde"],
                "calisan_surum_klasoru": ortak.SURUM_DIZINI.name, "etkin_surum": ortak.aktif() or "-",
                "onarim": onarim_cumlesi(sorun, self.ev)}

    def _durum(self):
        d = ortak.durum()
        icerik = ortak.json_oku(ortak.SURUM_DIZINI / "icerik.json")
        return json.dumps({
            "yerel_kurulum": ortak.surum(),
            "secilen_moduller": ortak.moduller(),
            "paket_durumu": self._paket_durumu(),
            "paketler":{p: self.bilgi.paket_surumu(p) for p in self.bilgi.profiller()},
            "bilesenler": icerik.get("bilesenler", {}),
            "arthur_mask": ortak.mask_surumu() or "kurulu değil",
            "buro": self.bilgi.firma_bilgi.get("ad") or "yok (standart paket)",
            "hafiza": str(hafiza.kasa()) if ortak.hafiza_acik() else "seçilmedi",
            "son_guncelleme_denetimi": time.strftime("%Y-%m-%d %H:%M", time.localtime(d["son_denetim"])) if d.get("son_denetim") else "henüz yok",
            "son_guncelleme_sonucu": d.get("son_sonuc", "-"),
            # Araç listesi henüz gelmediyse "ulaşılamadı" denmez: bağlantı denenmeden başarısız sayılmaz.
            "arastirma_sunucusu": (f"ulaşılamadı: {self.uzak_hata}" if self.uzak_hata else
                                   "bağlı" if self.uzak_araclar else "henüz bağlanılmadı (araç listesi bekleniyor)"),
            "uzak_arac_sayisi": len(self.uzak_araclar or []),
        }, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    Sunucu().calis()
