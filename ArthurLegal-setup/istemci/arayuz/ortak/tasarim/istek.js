// Masanın arama kutusuna yazılan Türkçe isteği çözer: kurul kararı mı, mevzuat mı; hangi kurum, kaç tane, hangi
// piyasa ya da karar türü, hangi yıl ve geriye kalan konu. "son 5 EPDK elektrik piyasası kurul kararı" →
// { hedef: "kurum", kurum: "epdk", piyasa: "elektrik", sayi: 5, konu: "" }. Saf işlevler: DOM ve ağ yok. Masaya
// AL:ISTEK yer tutucusuyla gömülür; tests/test_istek.mjs aynı dosyayı Node'da sınar.
//
// Çözücü bilmediğini uydurmaz: kurum adı geçmeyen istek mevzuat aramasına gider, masada Claude'a sorma düğmesi
// her zaman durur. Kurum adı geçse de istek mevzuat soruyorsa ("Rekabetin Korunması Hakkında Kanun", "KVKK m. 5")
// mevzuata gider.

const ISTEK = (() => {
  const HARF = { "ı": "i", "İ": "i", "ş": "s", "ğ": "g", "ü": "u", "ö": "o", "ç": "c", "â": "a", "î": "i", "û": "u" };
  const kucuk = (s) => String(s || "").toLocaleLowerCase("tr");
  const katla = (s) => [...kucuk(s)].map((h) => HARF[h] || h).join("");

  // Kurum: anahtar (tr_kurum_karari_ara), ekranda görünen ad, adın ifadeleri (katlanmış kelime dizileri).
  // "yalniz_kararla": kelime tek başına kurumu söylemez ("haksız rekabet"), yanında karar ya da kurul geçmeli.
  const KURUMLAR = [
    { anahtar: "epdk", ad: "EPDK", ifadeler: [["epdk"], ["enerji", "piyasasi", "duzenleme"]] },
    { anahtar: "spk", ad: "SPK", ifadeler: [["spk"], ["sermaye", "piyasasi", "kurul"]] },
    { anahtar: "rekabet", ad: "Rekabet Kurulu", ifadeler: [["rekabet", "kurul"], ["rekabet", "kurum"], ["rk"]] },
    { anahtar: "rekabet", ad: "Rekabet Kurulu", ifadeler: [["rekabet"]], yalniz_kararla: true },
    { anahtar: "bddk", ad: "BDDK", ifadeler: [["bddk"], ["bankacilik", "duzenleme"]] },
    { anahtar: "kvkk", ad: "KVKK", ifadeler: [["kvkk"], ["kvk"], ["kisisel", "verileri", "koruma", "kurul"]] },
    { anahtar: "btk", ad: "BTK", ifadeler: [["btk"], ["bilgi", "teknolojileri", "ve", "iletisim"]] },
    { anahtar: "gib", ad: "GİB özelgeleri", ifadeler: [["gib"], ["ozelge"], ["gelir", "idaresi"]] },
    { anahtar: "sigorta_tahkim", ad: "Sigorta Tahkim Komisyonu",
      ifadeler: [["sigorta", "tahkim"], ["tahkim", "komisyon"], ["hakem", "karar"]] },
  ];
  const AD = Object.fromEntries(KURUMLAR.map((k) => [k.anahtar, k.ad]));

  // EPDK piyasaları (market) ve Rekabet karar türleri (decision_type): kelimenin başı yeter.
  const PIYASALAR = [["elektrik", "elektrik"], ["dogalgaz", "dogalgaz"], ["dogal|gaz", "dogalgaz"],
    ["petrol", "petrol"], ["akaryakit", "petrol"], ["lpg", "lpg"], ["otogaz", "lpg"]];
  const PIYASA_ADI = { elektrik: "elektrik", dogalgaz: "doğal gaz", petrol: "petrol", lpg: "LPG" };
  const REKABET_TURLERI = [["birlesme", "birlesme_devralma"], ["devralma", "birlesme_devralma"], ["devir", "birlesme_devralma"],
    ["ihlal", "rekabet_ihlali"], ["sorusturma", "rekabet_ihlali"], ["kartel", "rekabet_ihlali"],
    ["muafiyet", "muafiyet_menfi_tespit"], ["menfi", "muafiyet_menfi_tespit"], ["ozellestirme", "ozellestirme"]];
  const TUR_ADI = { birlesme_devralma: "birleşme ve devralma", rekabet_ihlali: "rekabet ihlali",
    muafiyet_menfi_tespit: "muafiyet ve menfi tespit", ozellestirme: "özelleştirme" };

  const SAYILAR = { bir: 1, iki: 2, uc: 3, dort: 4, bes: 5, alti: 6, yedi: 7, sekiz: 8, dokuz: 9, on: 10,
    onbes: 15, yirmi: 20, otuz: 30, elli: 50 };
  const KARAR = /^(karar|kurul|bulten|ozelge|hakem)/;
  // Kökler ünsüz yumuşamasına dayanıklı: yönetmelik → yönetmeliği, tüzük → tüzüğü.
  const MEVZUAT = /^(kanun|yonetmeli|teblig|khk|kararname|tuzu|genelge|mevzuat|madde|sayili)/;
  // Konudan atılan kelimeler (katlanmış): istek kipi, ek parçaları, liste sözcükleri.
  const DOLGU = new Set(("son en yeni guncel yakin tum butun hepsi bana lutfen getir getirir getirin goster gosterir " +
    "listele bul ara arat ilgili hakkinda iliskin dair olan ve ile icin tane adet nedir neler hangi verilen alinan " +
    "yayimlanan yayinlanan kurul kurulu kurulun kurulunun kurulca kurum kurumu kurumunun karar karari kararlari " +
    "kararlarini kararini kararlar kararlardan kararlarindan kararinin bulten bulteni bultenleri bultenler ozelge " +
    "ozelgeleri ozelgesi piyasa piyasasi piyasalari piyasasina nin nun in un ni nu yi yu ye ya de da te ta den dan " +
    "ten tan e a i u yil yili yilinda yilindaki deki daki teki taki").split(" "));

  function kelimeler(metin) {
    // Kesme ve noktalama ayraçtır: "EPDK'nın" → "EPDK", "nın". Esas/karar no biçimleri (2024/2196) bütün kalır.
    return (String(metin || "").match(/[0-9]+\/[0-9]+|[\p{L}\p{N}]+/gu) || []).map((k) => ({ asil: k, k: katla(k) }));
  }

  // İfade (katlanmış kelime dizisi) kelime listesinde nerede başlıyor; her kelime önek olarak eşleşir.
  function ifadeBul(liste, ifade, alinan) {
    for (let i = 0; i + ifade.length <= liste.length; i++) {
      if (ifade.every((p, j) => !alinan.has(i + j) && (p.length <= 3 ? liste[i + j].k === p : liste[i + j].k.startsWith(p)))) {
        return i;
      }
    }
    return -1;
  }

  function coz(metin) {
    const liste = kelimeler(metin);
    const alinan = new Set();      // çözülüp konudan çıkan kelimelerin sırası
    const al = (i, n = 1) => { for (let j = 0; j < n; j++) alinan.add(i + j); };
    const kararVar = liste.some((w) => KARAR.test(w.k));
    const mevzuatVar = liste.some((w) => MEVZUAT.test(w.k)) || /\bm\.\s*\d/i.test(String(metin || ""));

    let kurum = null;
    for (const t of KURUMLAR) {
      if (t.yalniz_kararla && !kararVar) continue;
      for (const ifade of t.ifadeler) {
        const i = ifadeBul(liste, ifade, alinan);
        if (i >= 0) {
          if (!kurum) kurum = t.anahtar;
          if (t.anahtar === kurum) al(i, ifade.length);
        }
      }
      if (kurum) break;
    }
    // Kurum adı geçse de soru mevzuatsa ("KVKK m. 5", "Rekabetin Korunması Hakkında Kanun") mevzuata gider.
    const hedef = kurum && (kararVar || !mevzuatVar) ? "kurum" : "mevzuat";

    // Sayı: "son 5", "5 tane", "son beş", "10 karar". Yoksa 10; en çok 50.
    let sayi = null;
    liste.forEach((w, i) => {
      if (sayi !== null || alinan.has(i)) return;
      const sonra = liste[i + 1] ? liste[i + 1].k : "";
      const once = liste[i - 1] ? liste[i - 1].k : "";
      const n = /^\d{1,3}$/.test(w.k) ? Number(w.k) : SAYILAR[w.k];
      if (n && (once === "son" || /^(tane|adet)$/.test(sonra) || KARAR.test(sonra) || /^(en|yeni)$/.test(once))) {
        sayi = n;
        al(i);
        if (/^(tane|adet)$/.test(sonra)) al(i + 1);
      }
    });
    const enYeni = liste.some((w) => /^(son|yeni|guncel|yakin)/.test(w.k));

    // Yıl: 1990–2099 arası dört hane, ardından "sayılı" gelmiyorsa (2004 sayılı İİK bir kanun numarasıdır).
    let yil = null;
    liste.forEach((w, i) => {
      if (yil !== null || alinan.has(i) || !/^(19[9]\d|20\d\d)$/.test(w.k)) return;
      if (liste[i + 1] && /^sayili/.test(liste[i + 1].k)) return;
      if (hedef === "mevzuat" && !(liste[i + 1] && /^yil/.test(liste[i + 1].k))) return;
      yil = Number(w.k);
      al(i);
    });

    let piyasa = null;
    let karar_turu = null;
    if (hedef === "kurum" && kurum === "epdk") {
      for (const [desen, deger] of PIYASALAR) {
        const ifade = desen.split("|");
        const i = ifadeBul(liste, ifade, alinan);
        if (i >= 0) { piyasa = deger; al(i, ifade.length); break; }
      }
    }
    if (hedef === "kurum" && kurum === "rekabet") {
      liste.forEach((w, i) => {
        if (alinan.has(i)) return;
        const tur = REKABET_TURLERI.find(([on]) => w.k.startsWith(on));
        if (tur) { karar_turu = karar_turu || tur[1]; al(i); }
      });
    }

    // Mevzuat sorusunda metin olduğu gibi aranır; kurum isteğinde çözülen parçalar ve dolgu kelimeler çıkar.
    const konu = hedef === "kurum"
      ? liste.filter((w, i) => !alinan.has(i) && !DOLGU.has(w.k) && !/^\d{1,3}$/.test(w.k)).map((w) => w.asil).join(" ")
      : String(metin || "").replace(/\s+/g, " ").trim();
    return {
      hedef, kurum: hedef === "kurum" ? kurum : null, kurum_adi: hedef === "kurum" ? AD[kurum] : null,
      sayi: sayi || (hedef === "kurum" ? 10 : null), sayi_yazildi: sayi !== null, en_yeni: enYeni,
      yil, piyasa, karar_turu, konu,
    };
  }

  // Çözülen isteğin insan dilinde özeti: masada adım satırı olur ("EPDK · elektrik piyasası · en yeni 5 karar").
  function ozet(c) {
    if (c.hedef !== "kurum") return c.konu ? `Mevzuatta “${c.konu}”` : "Mevzuat";
    const parca = [c.kurum_adi];
    if (c.piyasa) parca.push(`${PIYASA_ADI[c.piyasa]} piyasası`);
    if (c.karar_turu) parca.push(TUR_ADI[c.karar_turu]);
    if (c.yil) parca.push(String(c.yil));
    if (c.konu) parca.push(`konu “${c.konu}”`);
    // Konu verilip "son" denmediyse sıra ilgiye göredir: "en yeni" yazılmaz.
    const sira = c.en_yeni || !c.konu ? "en yeni" : "en çok";
    parca.push(c.kurum === "spk" && !c.konu ? `${sira} ${c.sayi} bülten` : `${sira} ${c.sayi} karar`);
    return parca.join(" · ");
  }

  return { coz, ozet, katla, KURUMLAR, AD, PIYASA_ADI, TUR_ADI };
})();

if (typeof module !== "undefined") module.exports = ISTEK;
