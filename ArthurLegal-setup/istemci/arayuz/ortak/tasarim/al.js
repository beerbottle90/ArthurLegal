// ArthurLegal ortak görünüm kodu: her görünümün <script type="module"> bloğuna sunucuda gömülür
// (sunucu/al_arayuz.py, AL:JS yer tutucusu). Resmî MCP Apps istemcisine (App) bağlı değildir;
// App gerektiren yardımcılar onu parametre olarak alır.
//
// Araç sonucundaki hiçbir değer HTML olarak yazılmaz: her şey textContent ya da createElementNS.

const AL = (() => {
  const RESMI_GIRIS = "https://www.mevzuat.gov.tr/";
  const UYARI = "UYARI: veri çekilemedi, teyidiniz gerekli: ";
  const SURUM = "3.0.1";
  const NS = "http://www.w3.org/2000/svg";

  // 16x16 çizgi simgeleri; tek kalınlık, tek köşe biçimi.
  const IKONLAR = {
    kopya: [["rect", { x: 5.5, y: 5.5, width: 8, height: 8, rx: 2 }],
            ["path", { d: "M10.5 5.5V4a1.5 1.5 0 0 0-1.5-1.5H4A1.5 1.5 0 0 0 2.5 4v5A1.5 1.5 0 0 0 4 10.5h1.5" }]],
    dis: [["path", { d: "M9.5 2.5h4v4M13.5 2.5 7.5 8.5M12 9.5v3a1 1 0 0 1-1 1H3.5a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3" }]],
    onay: [["path", { d: "M3.5 8.5l3 3 6-7" }]],
    carpi: [["path", { d: "M4 4l8 8M12 4l-8 8" }]],
    uyari: [["path", { d: "M8 2.5 14 13H2z" }], ["path", { d: "M8 6.5v3M8 11.3v.1" }]],
    sohbet: [["path", { d: "M2.5 4A1.5 1.5 0 0 1 4 2.5h8A1.5 1.5 0 0 1 13.5 4v5.5A1.5 1.5 0 0 1 12 11H6.5l-3 2.5V11A1.5 1.5 0 0 1 2.5 9.5z" }]],
    kitap: [["path", { d: "M3 3.5A1.5 1.5 0 0 1 4.5 2H13v10H4.5A1.5 1.5 0 0 0 3 13.5z" }], ["path", { d: "M3 13.5A1.5 1.5 0 0 0 4.5 15H13v-3" }]],
    terazi: [["path", { d: "M8 2v12M5 14h6M3 4.5h10M3 4.5 1.5 9a1.8 1.8 0 0 0 3 0zM13 4.5 11.5 9a1.8 1.8 0 0 0 3 0z" }]],
    harita: [["path", { d: "M2 4l4-1.5 4 1.5 4-1.5v9.5l-4 1.5-4-1.5-4 1.5z" }], ["path", { d: "M6 2.5V12M10 4v9.5" }]],
    beyin: [["path", { d: "M6.5 2.5A2 2 0 0 0 4.5 4.3 2.2 2.2 0 0 0 3 8a2.2 2.2 0 0 0 1.5 3.7 2 2 0 0 0 2 1.8zM9.5 2.5a2 2 0 0 1 2 1.8A2.2 2.2 0 0 1 13 8a2.2 2.2 0 0 1-1.5 3.7 2 2 0 0 1-2 1.8z" }]],
    maske: [["path", { d: "M2 5c2-1 4-1 6 0 2-1 4-1 6 0 0 3.2-1.6 6-3.6 6-1 0-1.6-1-2.4-1s-1.4 1-2.4 1C3.6 11 2 8.2 2 5z" }], ["path", { d: "M5 7h1.5M9.5 7H11" }]],
    bina: [["path", { d: "M2 6l6-3.5L14 6M3.5 6.5v5.5M6.5 6.5v5.5M9.5 6.5v5.5M12.5 6.5v5.5M2 13.5h12" }]],
    fis: [["path", { d: "M6 2v3M10 2v3M4.5 5h7v2.5a3.5 3.5 0 0 1-7 0zM8 11v3" }]],
    zil: [["path", { d: "M4 11V7a4 4 0 0 1 8 0v4l1.5 1.5h-11zM6.5 14a1.5 1.5 0 0 0 3 0" }]],
    arama: [["circle", { cx: 7, cy: 7, r: 4.5 }], ["path", { d: "M10.5 10.5 14 14" }]],
    genislet: [["path", { d: "M2.5 6V2.5H6M10 2.5h3.5V6M13.5 10v3.5H10M6 13.5H2.5V10" }]],
    gunes: [["circle", { cx: 8, cy: 8, r: 3 }], ["path", { d: "M8 1.5V3M8 13v1.5M1.5 8H3M13 8h1.5M3.4 3.4l1 1M11.6 11.6l1 1M3.4 12.6l1-1M11.6 4.4l1-1" }]],
    ay: [["path", { d: "M13 9.5A5.5 5.5 0 0 1 6.5 3a5.5 5.5 0 1 0 6.5 6.5z" }]],
    otomatik: [["circle", { cx: 8, cy: 8, r: 5.5 }], ["path", { d: "M8 2.5a5.5 5.5 0 0 0 0 11z", fill: "currentColor" }]],
    ok: [["path", { d: "M6 3.5 10.5 8 6 12.5" }]],
    liste: [["path", { d: "M6 4h7.5M6 8h7.5M6 12h7.5M2.5 4h.1M2.5 8h.1M2.5 12h.1" }]],
    bag: [["path", { d: "M6.5 9.5l3-3M5.5 7 4 8.5a2.5 2.5 0 0 0 3.5 3.5L9 10.5M10.5 9 12 7.5A2.5 2.5 0 0 0 8.5 4L7 5.5" }]],
  };

  function ikon(ad) {
    const s = document.createElementNS(NS, "svg");
    for (const [k, v] of Object.entries({ viewBox: "0 0 16 16", fill: "none", stroke: "currentColor",
      "stroke-width": "1.6", "stroke-linecap": "round", "stroke-linejoin": "round", "aria-hidden": "true" })) {
      s.setAttribute(k, v);
    }
    for (const [etiket, ozellik] of IKONLAR[ad] || []) {
      const e = document.createElementNS(NS, etiket);
      for (const [k, v] of Object.entries(ozellik)) e.setAttribute(k, String(v));
      s.append(e);
    }
    return s;
  }

  function ogesi(etiket, sinif, metin) {
    const el = document.createElement(etiket);
    if (sinif) el.className = sinif;
    if (metin != null) el.textContent = metin;
    return el;
  }

  function dugme(yazi, { sinif = "", simge = null, baslik = null } = {}) {
    const b = ogesi("button", sinif);
    b.type = "button";
    if (simge) b.append(ikon(simge));
    b.append(ogesi("span", null, yazi));
    if (baslik) b.setAttribute("aria-label", baslik);
    return b;
  }

  // Kanun adları kaynakta BÜYÜK HARFLE gelir; başlıkta okunaklı yazılır, atıf alanı birebir kalır.
  // Parantez ya da tırnakla başlayan kelime de büyük harfle başlar; bilinen kısaltmalar büyük kalır:
  // "(ELEKTRİK PİYASASI …)" -> "(Elektrik Piyasası …)", "(LPG)" -> "(LPG)".
  const KUCUK = new Set(["ve", "ile", "veya", "ya", "da", "de"]);
  const KISALTMALAR = new Set(["LPG", "KHK", "YEK", "AB", "TBMM", "KDV", "ÖTV", "SGK", "BDDK", "SPK", "EPDK", "KVKK", "BTK",
    "TCK", "TBK", "TMK", "TTK", "HMK", "CMK", "İİK", "BM", "NATO", "OECD"]);
  function baslikDuzeni(s) {
    return String(s || "").split(/\s+/).filter(Boolean).map((ham, i) => {
      const [, on, govde, son] = /^([("'“]*)(.*?)([)"'”.,;:]*)$/u.exec(ham);
      if (KISALTMALAR.has(govde.toLocaleUpperCase("tr"))) return on + govde.toLocaleUpperCase("tr") + son;
      const w = govde.toLocaleLowerCase("tr");
      if (i > 0 && !on && KUCUK.has(w)) return w + son;
      return on + w.charAt(0).toLocaleUpperCase("tr") + w.slice(1) + son;
    }).join(" ");
  }

  // Kenar başlığının ekrandaki hali. Kaynak verisine dokunmaz, yalnız gösterir:
  // - sondaki dipnot işaretleri ("…MESİ2", "[3][4]") gösterilmez (eski sunucu yanıtlarına karşı da);
  // - tamamı büyük harfli başlık cümle düzenine iner, etiket olduğu gibi kalır: "II. BELİRLENMESİ" -> "II. Belirlenmesi".
  const ETIKET = /^\s*((?:[IVXLC]{1,6}|[A-ZÇĞİÖŞÜ]|\d{1,2}|[a-zçğıöşü]{1,2})\.\s+)/u;
  function baslikGoster(s) {
    let t = String(s || "").replace(/(?:\s*\[\d{1,4}\])+\s*$/u, "").replace(/(?<=\p{L})\d{1,2}$/u, "").trim();
    if (t && !/[a-zçğıöşüâîû]/u.test(t)) {
      const m = ETIKET.exec(t);
      const etiket = m ? m[1] : "";
      const govde = t.slice(etiket.length).toLocaleLowerCase("tr");
      t = etiket + govde.charAt(0).toLocaleUpperCase("tr") + govde.slice(1);
    }
    return t;
  }

  // Başlık ve üst kademeleri tek satırda: "E. Kira bedeli › II. Belirlenmesi". Yol yoksa yalnız başlık.
  function baslikYolu(item) {
    const yol = Array.isArray(item && item.heading_path) ? item.heading_path : [];
    if (yol.length > 1) return yol.map(baslikGoster).join(" › ");
    return item && item.heading ? baslikGoster(item.heading) : "";
  }

  // Sayıya iyelik eki: 1'i, 2'si, 3'ü, 6'sı, 10'u, 40'ı, 100'ü. Ek, sayının okunuşundaki son kelimeye uyar.
  const BIRLER = { 1: "i", 2: "si", 3: "ü", 4: "ü", 5: "i", 6: "sı", 7: "si", 8: "i", 9: "u" };
  const ONLAR = { 1: "u", 2: "si", 3: "u", 4: "ı", 5: "si", 6: "ı", 7: "i", 8: "i", 9: "ı" };
  function sayiEki(n) {
    const s = Math.abs(Math.trunc(Number(n) || 0));
    const ek = s === 0 ? "ı" : s % 10 ? BIRLER[s % 10] : s % 100 ? ONLAR[(s / 10) % 10] : s % 1000 ? "ü" : "i";
    return `${s}'${ek}`;
  }

  function tarih(iso) {
    const m = /^(\d{4})-(\d{2})-(\d{2})/.exec(iso || "");
    return m ? `${m[3]}.${m[2]}.${m[1]}` : "";
  }

  function zaman(iso) {
    const d = new Date(iso);
    return Number.isNaN(d.getTime()) ? "" : d.toLocaleString("tr-TR", { dateStyle: "short", timeStyle: "short" });
  }

  // Araç sonucunu okur: önce structuredContent, yoksa metin bloğundaki JSON.
  function veriAl(sonuc) {
    if (sonuc && sonuc.structuredContent && typeof sonuc.structuredContent === "object") {
      return { veri: sonuc.structuredContent };
    }
    const metin = sonuc && Array.isArray(sonuc.content)
      ? sonuc.content.filter((b) => b && b.type === "text").map((b) => b.text).join("\n") : "";
    if (sonuc && sonuc.isError) return { hata: metin.replace(/^ERROR:\s*/, "") || "Araç hata döndürdü." };
    try { return { veri: JSON.parse(metin) }; } catch { return { hata: metin || "Araç sonucu okunamadı." }; }
  }

  // Panoya kopyalama: çerçeve izin vermeyebilir. Clipboard API, sonra eski yol; ikisi de olmazsa
  // metni seçili bırakır ve kullanıcıya elle kopyalamasını söyler.
  async function kopyala(metin, dugmeEl, secilecek, duyuru) {
    let oldu = false;
    try {
      await navigator.clipboard.writeText(metin);
      oldu = true;
    } catch {
      const t = document.createElement("textarea");
      t.value = metin;
      t.setAttribute("readonly", "");
      t.style.cssText = "position:fixed;opacity:0;pointer-events:none";
      document.body.append(t);
      t.select();
      try { oldu = document.execCommand("copy"); } catch { oldu = false; }
      t.remove();
    }
    if (!oldu && secilecek) {
      const r = document.createRange();
      r.selectNodeContents(secilecek);
      const s = getSelection();
      s.removeAllRanges();
      s.addRange(r);
    }
    const yazi = dugmeEl && dugmeEl.querySelector("span");
    if (yazi) {
      const eski = yazi.textContent;
      yazi.textContent = oldu ? "Kopyalandı" : "Seçildi, Ctrl+C";
      setTimeout(() => { yazi.textContent = eski; }, 1800);
    }
    if (duyuru) duyuru.textContent = oldu ? "Panoya kopyalandı." : "Kopyalanamadı; metin seçildi, klavyeyle kopyalayın.";
    return oldu;
  }

  // ---- Tema: açık (varsayılan, beyaz) / koyu / otomatik (Claude'a uyar) ----
  // Seçim aynı sunucunun bütün görünümlerinde ortaktır (aynı köken, localStorage).
  const tema = {
    anahtar: "al.tema",
    host: "light",
    secim() {
      try { return localStorage.getItem(this.anahtar) || "acik"; } catch { return "acik"; }
    },
    sec(deger) {
      try { localStorage.setItem(this.anahtar, deger); } catch { /* depolama kapalıysa yalnız bu görünüm */ }
      this._gecici = deger;
      this.uygula();
    },
    uygula() {
      const s = this._gecici || this.secim();
      const koyu = s === "koyu" || (s === "otomatik" && this.host === "dark");
      document.documentElement.dataset.tema = koyu ? "koyu" : "acik";
      document.dispatchEvent(new CustomEvent("al-tema", { detail: s }));
    },
    baglamdan(ctx) {
      if (!ctx) return;
      if (ctx.theme) this.host = ctx.theme;
      const g = ctx.safeAreaInsets;
      if (g) {
        const kok = document.documentElement.style;
        kok.setProperty("--guvenli-ust", `${g.top || 0}px`);
        kok.setProperty("--guvenli-sag", `${g.right || 0}px`);
        kok.setProperty("--guvenli-alt", `${g.bottom || 0}px`);
        kok.setProperty("--guvenli-sol", `${g.left || 0}px`);
      }
      this.uygula();
    },
  };
  addEventListener("storage", (e) => { if (e.key === tema.anahtar) { tema._gecici = null; tema.uygula(); } });
  tema.uygula();

  // ---- İş adımları: kullanıcı neyin yapıldığını sırayla görür ----
  function adimlar(kok) {
    const kutu = ogesi("div", "adimlar");
    kutu.setAttribute("role", "status");
    kok.append(kutu);
    return {
      kutu,
      ekle(metin) {
        const satir = ogesi("div", "adim suruyor");
        const im = ogesi("span", "im");
        const yazi = ogesi("span", null, metin);
        satir.append(im, yazi);
        kutu.append(satir);
        const bitir = (sinif, simge, m) => {
          satir.className = "adim " + sinif;
          im.replaceChildren(ikon(simge));
          if (m != null) yazi.textContent = m;
        };
        return {
          tamam: (m) => bitir("tamam", "onay", m),
          hata: (m) => bitir("hata", "carpi", m),
          uyar: (m) => bitir("uyar", "uyari", m),
        };
      },
    };
  }

  // ---- Claude ile çalışma ----
  async function cagir(app, ad, girdi) {
    const sonuc = await app.callServerTool({ name: ad, arguments: girdi || {} });
    return veriAl(sonuc);
  }

  // Dil gerektiren işi Claude'a bırakır: mesaj sohbete kullanıcı adına düşer, cevap sohbette gelir.
  async function sor(app, metin) {
    const sonuc = await app.sendMessage({ role: "user", content: [{ type: "text", text: metin }] });
    if (sonuc && sonuc.isError) throw new Error("Claude mesajı kabul etmedi.");
  }

  async function baglantiAc(app, url, duyuru) {
    try {
      await app.openLink({ url });
    } catch {
      if (duyuru) duyuru.textContent = `Bağlantı açılamadı: ${url}`;
    }
  }

  return {
    RESMI_GIRIS, UYARI, SURUM, ikon, ogesi, dugme, baslikDuzeni, baslikGoster, baslikYolu, sayiEki, tarih, zaman,
    veriAl, kopyala,
    tema, adimlar, cagir, sor, baglantiAc,
  };
})();
