// Claude'un Markdown cevabını masada gösterir (al_masaya_yaz). İki katman:
// - bloklar(metin): saf ayrıştırıcı; başlık, paragraf, UYARI satırı, liste (iç içe), alıntı, tablo, kod, çizgi.
//   DOM'suz çalışır, Node testleri bunu sınar (tests/test_md.mjs).
// - ciz(metin, { baglanti }): bloklardan öğe kurar. Metin yalnız textContent ile yazılır; bağlantı yalnız http(s).
// - duzMetin(metin): panoya giden okunaklı düz metin (madde işaretleri, numaralar, sekmeli tablo).
//
// Cevap yazıldıkça parça parça gelir: yarım kalmış işaret (** ya da tablo ayıracı) olduğu gibi yazı olarak görünür,
// tamamlanınca biçimlenir.

const MD = (() => {
  const BASLIK = /^\s{0,3}(#{1,6})\s+(.*?)\s*#*\s*$/;
  const CIZGI = /^\s{0,3}([-*_])(?:\s*\1){2,}\s*$/;
  const ALINTI = /^\s{0,3}>\s?(.*)$/;
  const KOD = /^\s{0,3}(```|~~~)/;
  const LISTE = /^(\s*)([-*+•]|\d{1,9}[.)])\s+(.*)$/;
  const AYIRAC = /^\s*\|?\s*:?-{3,}:?\s*(?:\|\s*:?-{3,}:?\s*)*\|?\s*$/;

  // Satır içi: kod, kalın, bağlantı, eğik, çıplak adres. Sıra önemlidir: kod içindeki yıldız biçim değildir.
  const SATIR_ICI = new RegExp([
    "(`+)([^`]|[^`][\\s\\S]*?[^`])\\1(?!`)",
    "\\*\\*(?=\\S)([\\s\\S]*?\\S)\\*\\*",
    "__(?=\\S)([\\s\\S]*?\\S)__(?![\\p{L}\\p{N}])",
    "\\[([^\\]\\n]+)\\]\\((https?:\\/\\/[^\\s)]+)\\)",
    "(?<![\\p{L}\\p{N}*])\\*(?=[^\\s*])([^*\\n]*?[^\\s*])\\*(?![\\p{L}\\p{N}*])",
    "(?<![\\p{L}\\p{N}_])_(?=[^\\s_])([^_\\n]*?[^\\s_])_(?![\\p{L}\\p{N}_])",
    "(https?:\\/\\/[^\\s<>()\\[\\]]*[^\\s<>()\\[\\].,;:!?'\"”’])",
  ].join("|"), "gu");

  function satirIci(metin) {
    const s = String(metin ?? "");
    const out = [];
    let son = 0;
    for (const m of s.matchAll(SATIR_ICI)) {   // matchAll kendi kopyasıyla tarar: iç içe çağrı güvenli
      if (m.index > son) out.push({ t: "yazi", m: s.slice(son, m.index) });
      if (m[2] != null) out.push({ t: "kod", m: m[2] });
      else if (m[3] != null || m[4] != null) out.push({ t: "kalin", ic: satirIci(m[3] ?? m[4]) });
      else if (m[5] != null) out.push({ t: "bag", ic: satirIci(m[5]), url: m[6] });
      else if (m[7] != null || m[8] != null) out.push({ t: "egik", ic: satirIci(m[7] ?? m[8]) });
      else out.push({ t: "bag", ic: [{ t: "yazi", m: m[9] }], url: m[9] });
      son = m.index + m[0].length;
    }
    if (son < s.length) out.push({ t: "yazi", m: s.slice(son) });
    return out;
  }

  function hucreler(satir) {
    let s = satir.trim();
    if (s.startsWith("|")) s = s.slice(1);
    if (s.endsWith("|") && !s.endsWith("\\|")) s = s.slice(0, -1);
    return s.split(/(?<!\\)\|/).map((h) => h.trim().replace(/\\\|/g, "|"));
  }

  // Liste: aynı girintideki aynı türden maddeler; daha girintili madde alt liste, işaretsiz girintili satır maddenin
  // devamıdır. Maddeler arasındaki boş satır listeyi bölmez.
  function listeOku(satirlar, i) {
    const ilk = LISTE.exec(satirlar[i]);
    const girinti = ilk[1].length;
    const sirali = /\d/.test(ilk[2]);
    const liste = { t: "liste", sirali, baslangic: sirali ? parseInt(ilk[2], 10) : 1, ogeler: [] };
    const ogeler = [];
    while (i < satirlar.length) {
      const s = satirlar[i];
      if (!s.trim()) {
        let j = i + 1;
        while (j < satirlar.length && !satirlar[j].trim()) j++;
        const sonraki = j < satirlar.length && LISTE.exec(satirlar[j]);
        if (sonraki && sonraki[1].length >= girinti && ogeler.length) { i = j; continue; }
        break;
      }
      const m = LISTE.exec(s);
      if (m && m[1].length === girinti && /\d/.test(m[2]) === sirali) { ogeler.push({ metin: [m[3]], alt: [] }); i++; continue; }
      if (m && m[1].length > girinti && ogeler.length) {
        const [alt, son] = listeOku(satirlar, i);
        ogeler[ogeler.length - 1].alt.push(alt);
        i = son;
        continue;
      }
      if (!m && /^\s/.test(s) && ogeler.length) { ogeler[ogeler.length - 1].metin.push(s.trim()); i++; continue; }
      break;
    }
    liste.ogeler = ogeler.map((o) => ({ ic: satirIci(o.metin.join(" ")), alt: o.alt }));
    return [liste, i];
  }

  function bloklar(metin) {
    const satirlar = String(metin ?? "").replace(/\r\n?/g, "\n").split("\n");
    const out = [];
    let paragraf = [];
    const paragrafBitir = () => {
      if (!paragraf.length) return;
      const m = paragraf.join(" ");
      out.push({ t: /^UYARI:/.test(m) ? "uyari" : "p", ic: satirIci(m) });
      paragraf = [];
    };
    let i = 0;
    while (i < satirlar.length) {
      const s = satirlar[i];
      let m;
      if (!s.trim()) { paragrafBitir(); i++; continue; }
      if ((m = KOD.exec(s))) {
        paragrafBitir();
        const govde = [];
        i++;
        while (i < satirlar.length && !satirlar[i].trim().startsWith(m[1])) govde.push(satirlar[i++]);
        i++;
        out.push({ t: "kod", m: govde.join("\n") });
        continue;
      }
      if ((m = BASLIK.exec(s))) {
        paragrafBitir();
        const n = m[1].length;
        out.push({ t: "h", d: n <= 2 ? 3 : n === 3 ? 4 : 5, ic: satirIci(m[2]) });
        i++;
        continue;
      }
      if (CIZGI.test(s)) { paragrafBitir(); out.push({ t: "cizgi" }); i++; continue; }
      if (ALINTI.test(s)) {
        paragrafBitir();
        const ic = [];
        while (i < satirlar.length && ALINTI.test(satirlar[i])) ic.push(ALINTI.exec(satirlar[i++])[1]);
        out.push({ t: "alinti", bloklar: bloklar(ic.join("\n")) });
        continue;
      }
      if (s.includes("|") && i + 1 < satirlar.length && AYIRAC.test(satirlar[i + 1])) {
        paragrafBitir();
        const baslik = hucreler(s);
        const hiza = hucreler(satirlar[i + 1]).map((h) => (/^:.*:$/.test(h) ? "center" : /:$/.test(h) ? "right" : ""));
        i += 2;
        const satir = [];
        while (i < satirlar.length && satirlar[i].includes("|") && satirlar[i].trim()) satir.push(hucreler(satirlar[i++]));
        out.push({ t: "tablo", hiza, baslik: baslik.map(satirIci), satirlar: satir.map((r) => baslik.map((_, j) => satirIci(r[j] ?? ""))) });
        continue;
      }
      if (LISTE.test(s)) {
        paragrafBitir();
        const [liste, son] = listeOku(satirlar, i);
        out.push(liste);
        i = son;
        continue;
      }
      paragraf.push(s.trim());
      i++;
    }
    paragrafBitir();
    return out;
  }

  // ---- düz metin (pano) ----
  function duzIc(ic) {
    return ic.map((n) => {
      if (n.t === "yazi" || n.t === "kod") return n.m;
      if (n.t === "bag") { const y = duzIc(n.ic); return y === n.url ? y : `${y} (${n.url})`; }
      return duzIc(n.ic);
    }).join("");
  }

  function duzBloklar(bl, on = "") {
    const parca = [];
    for (const b of bl) {
      if (b.t === "h" || b.t === "p" || b.t === "uyari") parca.push(on + duzIc(b.ic));
      else if (b.t === "kod") parca.push(b.m.split("\n").map((x) => on + x).join("\n"));
      else if (b.t === "cizgi") parca.push(on + "—");
      else if (b.t === "alinti") parca.push(duzBloklar(b.bloklar, on + "> "));
      else if (b.t === "tablo") {
        parca.push([b.baslik, ...b.satirlar].map((r) => on + r.map(duzIc).join("\t")).join("\n"));
      } else if (b.t === "liste") parca.push(duzListe(b, on));
    }
    return parca.join("\n\n");
  }

  function duzListe(b, on) {
    return b.ogeler.map((o, k) => {
      const isaret = b.sirali ? `${b.baslangic + k}. ` : "• ";
      const alt = o.alt.map((x) => duzListe(x, on + "   ")).join("\n");
      return on + isaret + duzIc(o.ic) + (alt ? "\n" + alt : "");
    }).join("\n");
  }

  const duzMetin = (metin) => duzBloklar(bloklar(metin));

  // ---- çizim (tarayıcı) ----
  function ogesi(etiket, sinif) {
    const e = document.createElement(etiket);
    if (sinif) e.className = sinif;
    return e;
  }

  function icCiz(kap, ic, baglanti) {
    for (const n of ic) {
      if (n.t === "yazi") kap.append(document.createTextNode(n.m));
      else if (n.t === "kod") { const c = ogesi("code"); c.textContent = n.m; kap.append(c); }
      else if (n.t === "bag") {
        const a = ogesi("a");
        a.href = n.url;
        a.rel = "noopener noreferrer";
        a.target = "_blank";
        icCiz(a, n.ic, baglanti);
        if (baglanti) a.addEventListener("click", (e) => { e.preventDefault(); baglanti(n.url); });
        kap.append(a);
      } else {
        const e = ogesi(n.t === "kalin" ? "strong" : "em");
        icCiz(e, n.ic, baglanti);
        kap.append(e);
      }
    }
  }

  function blokCiz(kap, b, baglanti) {
    let e;
    if (b.t === "h" || b.t === "p" || b.t === "uyari") {
      e = ogesi(b.t === "h" ? "h" + b.d : "p", b.t === "uyari" ? "uyari" : null);
      icCiz(e, b.ic, baglanti);
    } else if (b.t === "liste") {
      e = ogesi(b.sirali ? "ol" : "ul");
      if (b.sirali && b.baslangic !== 1) e.start = b.baslangic;
      for (const o of b.ogeler) {
        const li = ogesi("li");
        icCiz(li, o.ic, baglanti);
        for (const alt of o.alt) blokCiz(li, alt, baglanti);
        e.append(li);
      }
    } else if (b.t === "alinti") {
      e = ogesi("blockquote");
      for (const x of b.bloklar) blokCiz(e, x, baglanti);
    } else if (b.t === "tablo") {
      e = ogesi("div", "md-tablo");
      const t = ogesi("table");
      const satir = (hucre, r) => {
        const tr = ogesi("tr");
        r.forEach((ic, j) => {
          const h = ogesi(hucre);
          if (b.hiza[j]) h.style.textAlign = b.hiza[j];
          icCiz(h, ic, baglanti);
          tr.append(h);
        });
        return tr;
      };
      const thead = ogesi("thead");
      thead.append(satir("th", b.baslik));
      const tbody = ogesi("tbody");
      for (const r of b.satirlar) tbody.append(satir("td", r));
      t.append(thead, tbody);
      e.append(t);
    } else if (b.t === "kod") {
      e = ogesi("pre");
      const c = ogesi("code");
      c.textContent = b.m;
      e.append(c);
    } else {
      e = ogesi("hr");
    }
    kap.append(e);
  }

  function ciz(metin, { baglanti } = {}) {
    const kok = ogesi("div", "md");
    for (const b of bloklar(metin)) blokCiz(kok, b, baglanti);
    return kok;
  }

  return { bloklar, satirIci, duzMetin, ciz };
})();

if (typeof module !== "undefined") module.exports = MD;
