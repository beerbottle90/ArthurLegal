// ArthurLegal sonuç kartları: madde ve içtihat. Sohbetteki tek başına kartlar ile AL Masası aynı
// çizimi kullanır. al.js'ten sonra gömülür (AL:KARTLAR yer tutucusu). ortam = { app, duyuru }.

const KART = (() => {
  const { ogesi, ikon, dugme, baslikDuzeni, baslikGoster, baslikYolu, tarih, zaman, kopyala, cagir, sor, baglantiAc,
    uyari, RESMI_GIRIS } = AL;

  // ------------------------------------------------------------------ ortak parçalar
  function durumRozeti(basarili, toplam) {
    const tam = toplam > 0 && basarili === toplam;
    const sinif = tam ? "nane" : basarili ? "amber" : "kirmizi";
    const yazi = tam ? cev("Doğrulandı") : basarili ? cev("Kısmen doğrulandı") : cev("Doğrulanamadı");
    return ogesi("span", "rozet nokta " + sinif, yazi);
  }

  function altSatir(kaynakYazi, dugmeler) {
    const alt = ogesi("div", "alt-satir");
    alt.append(ogesi("span", "zaman", kaynakYazi));
    const eylem = ogesi("div", "eylemler");
    eylem.append(...dugmeler);
    alt.append(eylem);
    return alt;
  }

  function uzunMetin(paragraflar, sinir) {
    const kap = ogesi("div");
    const metin = ogesi("div", "metin");
    for (const p of paragraflar) metin.append(ogesi("p", null, p));
    kap.append(metin);
    const uzunluk = paragraflar.join("").length;
    if (uzunluk > sinir) {
      metin.classList.add("kisa");
      const ac = ogesi("button", "duz", cev("Tamamını göster"));
      ac.type = "button";
      ac.setAttribute("aria-expanded", "false");
      ac.onclick = () => {
        const acik = metin.classList.toggle("kisa") === false;
        ac.textContent = acik ? cev("Daha az göster") : cev("Tamamını göster");
        ac.setAttribute("aria-expanded", String(acik));
      };
      kap.append(ac);
    }
    return kap;
  }

  function atifKutusu(atif, ortam, etiket = cev("Atıf")) {
    const kutu = ogesi("div", "atif");
    const icerik = ogesi("div", "atif-icerik");
    const deger = ogesi("span", "atif-metin", atif);
    icerik.append(ogesi("span", "etiket", etiket), deger);
    const b = dugme(cev("Kopyala"), { sinif: "kucuk", simge: "kopya", baslik: cev("{0} kopyala", etiket) });
    b.onclick = () => kopyala(atif, b, deger, ortam.duyuru);
    kutu.append(icerik, b);
    return kutu;
  }

  // ------------------------------------------------------------------ madde (tr_mevzuat_madde_getir)
  const MADDE_DURUMU = {
    repealed: [cevN("Mülga"), "kirmizi"],
    annulled: [cevN("İptal"), "kirmizi"],
    incorporated_elsewhere: [cevN("Başka kanuna işlenmiş"), "mavi"],
  };

  function maddeEtiketi(no) {
    const m = /^(geçici|ek)\s+(.+)$/i.exec(String(no || "").trim());
    if (m) return `${m[1].charAt(0).toLocaleUpperCase("tr")}${m[1].slice(1).toLocaleLowerCase("tr")} m. ${m[2]}`;
    return `m. ${no}`;
  }

  function kanunKunyesi(law) {
    const p = [];
    if (law.number) p.push(cev("{0} No. {1}", law.type === "KANUN" || !law.type ? cev("Kanun") : baslikDuzeni(law.type), law.number));
    const t = tarih(law.rg_date);
    if (t || law.rg_number) {
      p.push(t && law.rg_number ? `RG ${t} / ${law.rg_number}` : t ? `RG ${t}` : cev("RG sayı {0} (tarih kaynakta yok)", law.rg_number));
    }
    if (law.mukerrer === "EVET") p.push(cev("mükerrer"));
    return p.join(" · ");
  }

  function maddeParagraflari(item) {
    let metin = String(item.text || "");
    const bas = String(item.header || "");
    if (bas && metin.startsWith(bas)) metin = metin.slice(bas.length).trim();
    return metin.split(/\n{2,}/).map((p) => p.trim()).filter(Boolean);
  }

  function maddeKopyaMetni(veri) {
    return (veri.items || []).filter((it) => it && it.ok)
      .map((it) => [it.citation, baslikYolu(it) ? `(${baslikYolu(it)})` : "", maddeParagraflari(it).join("\n")]
        .filter(Boolean).join("\n"))
      .join("\n\n");
  }

  function madde(veri, ortam) {
    const law = veri.law || {};
    const items = Array.isArray(veri.items) ? veri.items : [];
    const kaynak = law.source_url || RESMI_GIRIS;
    const basarili = items.filter((it) => it && it.ok);
    const tek = items.length === 1;

    const kok = ogesi("div", "sonuc");
    const ust = ogesi("div", "sonuc-ust");
    const baslikKutu = ogesi("div", "sonuc-baslik");
    baslikKutu.append(ogesi("h2", null, law.title ? baslikDuzeni(law.title) : cev("Mevzuat")),
      ogesi("div", "kunye", kanunKunyesi(law)));
    ust.append(baslikKutu, durumRozeti(basarili.length, items.length));
    kok.append(ust);

    for (const it of items) {
      const g = ogesi("section", "grup");
      const bas = ogesi("div", "grup-bas");
      if (it && it.ok) {
        // Kademeli başlıkta (TBK, TMK) üst kademeler başlığın üstünde: "E. Kira bedeli ›".
        const yol = Array.isArray(it.heading_path) ? it.heading_path : [];
        if (yol.length > 1) g.append(ogesi("div", "baslik-yolu", yol.slice(0, -1).map(baslikGoster).join(" › ") + " ›"));
        bas.append(ogesi("span", "hap-altin", maddeEtiketi(it.madde_no || it.requested)));
        bas.append(it.heading ? ogesi("span", "baslik", baslikGoster(it.heading)) : ogesi("span", "baslik yok", cev("Başlık kaynakta yok")));
        const r = MADDE_DURUMU[it.status];
        if (r) bas.append(ogesi("span", "rozet " + r[1], r[0]));
        g.append(bas, uzunMetin(maddeParagraflari(it), tek ? 900 : 450));
        if (it.truncated) g.append(ogesi("p", "aciklama", cev("Metin kısaltıldı ({0} karakter); tamamı resmî kaynakta.", it.chars)));
        const notlar = (it.annotations || []).filter(Boolean);
        if (notlar.length) {
          const sira = ogesi("div", "notlar");
          notlar.slice(0, 4).forEach((n) => sira.append(ogesi("span", "not", n)));
          if (notlar.length > 4) sira.append(ogesi("span", "not", cev("+{0} not", notlar.length - 4)));
          g.append(sira);
        }
        if (it.citation) g.append(atifKutusu(it.citation, ortam));
      } else {
        const it2 = it || {};
        bas.append(ogesi("span", "hap-altin", maddeEtiketi(it2.requested)));
        bas.append(ogesi("span", "rozet amber", it2.error_code === "NOT_FOUND" ? cev("Bulunamadı") : cev("Doğrulanamadı")));
        g.append(bas);
        // Aracın açıklamasının ilk cümlesi yeter; kuralın kendisi UYARI satırında.
        const ilk = String(it2.message || "").split(/(?<=\.)\s/)[0];
        if (ilk) g.append(ogesi("p", "aciklama", ilk));
        g.append(ogesi("p", "uyari", uyari(kaynak)));
      }
      kok.append(g);
    }
    if (!items.length) {
      const g = ogesi("section", "grup");
      g.append(ogesi("p", "aciklama", cev("Araç madde döndürmedi.")), ogesi("p", "uyari", uyari(kaynak)));
      kok.append(g);
    }

    const ac = dugme(cev("Resmî metin"), { simge: "dis" });
    ac.onclick = () => baglantiAc(ortam.app, kaynak, ortam.duyuru);
    const dugmeler = [ac];
    if (basarili.length) {
      const kp = dugme(basarili.length > 1 ? cev("Maddeleri kopyala") : cev("Metni kopyala"), { sinif: "birincil", simge: "kopya" });
      kp.onclick = () => kopyala(maddeKopyaMetni(veri), kp, kok, ortam.duyuru);
      dugmeler.push(kp);
    }
    const z = zaman(veri.fetched_at);
    kok.append(altSatir(z ? `mevzuat.gov.tr · ${z}` : "mevzuat.gov.tr", dugmeler));
    return kok;
  }

  // ------------------------------------------------------------------ içtihat (tr_ictihat_ara)
  function kararSatiri(k, ortam) {
    const g = ogesi("section", "grup karar");
    const bas = ogesi("div", "grup-bas");
    bas.append(ogesi("span", "hap-altin", k.karar_tarihi || cev("tarih yok")));
    bas.append(ogesi("span", "baslik", [k.court && k.court.replace(/ Kararı$/, ""), k.chamber].filter(Boolean).join(" ")));
    if (k.kesinlesme) bas.append(ogesi("span", "rozet nane", k.kesinlesme));
    g.append(bas);
    g.append(ogesi("div", "kunye", [k.esas_no && `E. ${k.esas_no}`, k.karar_no && `K. ${k.karar_no}`, k.karar_turu]
      .filter(Boolean).join(" · ")));

    const yer = ogesi("div", "karar-metni");
    const eylem = ogesi("div", "eylemler sol");
    const getir = dugme(cev("Metni aç"), { simge: "kitap" });
    const kopya = dugme(cev("Künyeyi kopyala"), { simge: "kopya" });
    const kaynak = dugme(cev("Kaynak"), { simge: "dis" });
    let acik = false;
    getir.onclick = async () => {
      if (acik) { yer.replaceChildren(); acik = false; getir.querySelector("span").textContent = cev("Metni aç"); return; }
      acik = true;
      getir.querySelector("span").textContent = cev("Metni kapat");
      const adim = AL.adimlar(yer).ekle(cev("Karar metni resmî kaynaktan getiriliyor…"));
      try {
        const { veri, hata } = await cagir(ortam.app, "tr_ictihat_getir", { document_id: String(k.document_id) });
        if (hata || !veri || !veri.text) throw new Error(hata || cev("Metin boş geldi."));
        adim.tamam(cev("Metin geldi ({0} karakter{1}).", veri.chars || veri.text.length, veri.has_more ? cev(", ilk sayfa") : ""));
        const paragraflar = String(veri.text).split(/\n+/).map((p) => p.trim()).filter(Boolean);
        yer.append(uzunMetin(paragraflar, 700));
        const ozet = dugme(cev("Claude'a özetlet"), { sinif: "kucuk", simge: "sohbet" });
        ozet.onclick = () => sor(ortam.app, cev("Şu kararı ArthurLegal kurallarıyla özetle ve künyesini birebir kullan: {0} (document_id {1}).", k.citation, k.document_id))
          .catch(() => { if (ortam.duyuru) ortam.duyuru.textContent = cev("Mesaj gönderilemedi."); });
        yer.append(ozet);
      } catch (e) {
        adim.hata(cev("Metin getirilemedi."));
        yer.append(ogesi("p", "uyari", uyari((k.source_url || "https://karararama.yargitay.gov.tr/"))));
      }
    };
    kopya.onclick = () => kopyala(k.citation || "", kopya, null, ortam.duyuru);
    kaynak.onclick = () => baglantiAc(ortam.app, k.source_url || "https://karararama.yargitay.gov.tr/", ortam.duyuru);
    eylem.append(getir, kopya, kaynak);
    g.append(eylem, yer);
    return g;
  }

  function ictihat(veri, ortam) {
    const sonuclar = Array.isArray(veri.results) ? veri.results : [];
    const kok = ogesi("div", "sonuc");
    const ust = ogesi("div", "sonuc-ust");
    const bk = ogesi("div", "sonuc-baslik");
    const sorgu = veri.uygulanan_sorgu || veri.query || "";
    bk.append(ogesi("h2", null, sorgu ? `“${String(sorgu).replace(/^"|"$/g, "")}”` : cev("İçtihat araması")));
    const mahkemeler = (veri.courts || []).map((c) => /YARGITAY/.test(c) ? cev("Yargıtay") : /DANISTAY/.test(c) ? cev("Danıştay") : c);
    bk.append(ogesi("div", "kunye", [cev("{0} karar", veri.total ?? sonuclar.length), mahkemeler.join(", "), veri.arama_modu]
      .filter(Boolean).join(" · ")));
    ust.append(bk, ogesi("span", "rozet nokta " + (sonuclar.length ? "nane" : "amber"), sonuclar.length ? cev("Kaynaktan") : cev("Sonuç yok")));
    kok.append(ust);

    if (!sonuclar.length) {
      const g = ogesi("section", "grup");
      g.append(ogesi("p", "aciklama", cev("Bu sorguyla karar bulunamadı. Daha geniş bir ifade ya da farklı mahkeme deneyin.")));
      kok.append(g);
    }
    for (const k of sonuclar) kok.append(kararSatiri(k, ortam));

    const kunyeler = sonuclar.map((k) => k.citation).filter(Boolean).join("\n");
    const dugmeler = [];
    if (kunyeler) {
      const kp = dugme(cev("Künyeleri kopyala"), { sinif: "birincil", simge: "kopya" });
      kp.onclick = () => kopyala(kunyeler, kp, null, ortam.duyuru);
      dugmeler.push(kp);
    }
    kok.append(altSatir(cev("Bedesten · mevzuat.adalet.gov.tr"), dugmeler));
    return kok;
  }

  return { madde, ictihat, maddeEtiketi, durumRozeti, uzunMetin };
})();
