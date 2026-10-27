// Taslak metindeki kanun maddesi atıflarını bulur ve kanunları numaraya çevirir. Saf işlevler: DOM ve
// ağ yok. Masaya AL:ATIF yer tutucusuyla gömülür; tests/test_atif.mjs aynı dosyayı Node'da sınar.
// Sunucuya metin gitmez: yalnız bulunan kanun ve madde numaraları doğrulanır.

const ATIF = (() => {
  // [numara, ad, kısaltma]
  const KANUNLAR = [
    ["6098", "Türk Borçlar Kanunu", "TBK"], ["4721", "Türk Medeni Kanunu", "TMK"],
    ["6100", "Hukuk Muhakemeleri Kanunu", "HMK"], ["2004", "İcra ve İflas Kanunu", "İİK"],
    ["6102", "Türk Ticaret Kanunu", "TTK"], ["5237", "Türk Ceza Kanunu", "TCK"],
    ["5271", "Ceza Muhakemesi Kanunu", "CMK"], ["4857", "İş Kanunu", "İşK"],
    ["7036", "İş Mahkemeleri Kanunu", ""], ["6698", "Kişisel Verilerin Korunması Kanunu", "KVKK"],
    ["6769", "Sınai Mülkiyet Kanunu", "SMK"], ["5846", "Fikir ve Sanat Eserleri Kanunu", "FSEK"],
    ["6502", "Tüketicinin Korunması Hakkında Kanun", "TKHK"], ["2577", "İdari Yargılama Usulü Kanunu", "İYUK"],
    ["5718", "Milletlerarası Özel Hukuk ve Usul Hukuku Hakkında Kanun", "MÖHUK"],
    ["6325", "Hukuk Uyuşmazlıklarında Arabuluculuk Kanunu", "HUAK"], ["634", "Kat Mülkiyeti Kanunu", "KMK"],
    ["4054", "Rekabetin Korunması Hakkında Kanun", "RKHK"], ["213", "Vergi Usul Kanunu", "VUK"],
    ["2709", "Türkiye Cumhuriyeti Anayasası", "AY"],
  ];

  const buyuk = (s) => String(s).toLocaleUpperCase("tr");
  const kucuk = (s) => String(s).toLocaleLowerCase("tr");

  const KISALTMA = Object.fromEntries(KANUNLAR.filter((k) => k[2]).map((k) => [buyuk(k[2]), k[0]]));
  // Yaygın diğer yazımlar.
  Object.assign(KISALTMA, { "MK": "4721", "IIK": "2004", "İK": "4857", "ANAYASA": "2709" });
  const AD = Object.fromEntries(KANUNLAR.map((k) => [k[0], k]));

  // "TBK", "6098", "TBK · 6098" ya da kanun adının başı -> "6098"; tanınmazsa null.
  function kanunCoz(s) {
    const t = String(s || "").split("·").map((x) => x.trim()).filter(Boolean);
    for (const parca of t.length ? t : [""]) {
      const sayi = /^(\d{3,5})\b/.exec(parca);
      if (sayi) return sayi[1];
      const kisa = KISALTMA[buyuk(parca)];
      if (kisa) return kisa;
      const k = kucuk(parca);
      const tam = KANUNLAR.find((x) => kucuk(x[1]) === k || (k.length > 5 && kucuk(x[1]).startsWith(k)));
      if (tam) return tam[0];
    }
    return null;
  }

  function kanunAdi(no) {
    const k = AD[no];
    return k ? (k[2] ? `${k[2]} (${no} sayılı ${k[1]})` : `${no} sayılı ${k[1]}`) : `${no} sayılı Kanun`;
  }

  function kisaAd(no) {
    const k = AD[no];
    return k && k[2] ? k[2] : no;
  }

  const kac = (s) => s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");

  function desenler() {
    const kisalar = Object.keys(KISALTMA).sort((a, b) => b.length - a.length).map(kac).join("|");
    const ek = "(?:['’][\\p{L}]+)?";
    return [
      // TBK m. 344 · TBK md. 344/1 · TBK madde 344
      [new RegExp(`(?<!\\p{L})(${kisalar})${ek}\\s*(?:m\\.|md\\.|madde(?:si)?)\\s*(\\d{1,4})`, "giu"),
        (m) => [KISALTMA[buyuk(m[1])], m[2]]],
      // TBK'nın 344. maddesi
      [new RegExp(`(?<!\\p{L})(${kisalar})${ek}\\s+(\\d{1,4})\\s*\\.\\s*madde`, "giu"),
        (m) => [KISALTMA[buyuk(m[1])], m[2]]],
      // 6098 sayılı … Kanun'un 344. maddesi · 6098 sayılı … m. 344
      // JavaScript'te \b Türkçe harfleri tanımaz ("sayılı" ı ile biter): sınırlar \p{L} ile yazılır.
      [/(\d{3,5})\s+sayılı(?!\p{L})[^\n.;]{0,110}?(?:(?<!\p{L})(?:m|md)\.\s*(\d{1,4})|(?<![\p{L}\d])(\d{1,4})\s*\.\s*madde)/giu,
        (m) => [m[1], m[2] || m[3]]],
    ];
  }

  // Metindeki atıflar, ilk geçiş sırasıyla ve tekil: [{kanun, madde, yazim, cumle}]
  function atiflariBul(metin) {
    const metinS = String(metin || "");
    const bulunan = new Map();
    const sira = [];
    for (const [desen, coz] of desenler()) {
      for (const m of metinS.matchAll(desen)) {
        const [kanun, madde] = coz(m);
        if (!kanun || !madde) continue;
        const anahtar = kanun + ":" + madde;
        if (bulunan.has(anahtar)) continue;
        const bas = Math.max(0, m.index - 160);
        bulunan.set(anahtar, {
          kanun, madde, yazim: m[0].trim(), konum: m.index,
          cumle: metinS.slice(bas, m.index + m[0].length + 160).replace(/\s+/g, " ").trim(),
        });
      }
    }
    for (const v of bulunan.values()) sira.push(v);
    return sira.sort((a, b) => a.konum - b.konum);
  }

  return { KANUNLAR, KISALTMA, kanunCoz, kanunAdi, kisaAd, atiflariBul };
})();

if (typeof module !== "undefined") module.exports = ATIF;
