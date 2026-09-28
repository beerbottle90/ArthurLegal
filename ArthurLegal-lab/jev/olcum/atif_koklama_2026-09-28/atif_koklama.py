"""Madde atfı doğrulama — Jev koklama testi (n=16, benchmark DEĞİL).

Soru: Jev, "maddeye yüklenen içerik metinle örtüşüyor mu?" sorusunu
(mevzuat-mcp-rehberi.md bölüm 9, adım 4) Türkçe kanun metninde yanıtlayabiliyor mu?

Veri: madde metinleri tr_mevzuat_madde_getir ile 2026-09-28'de canlı çekildi
(kamuya açık). İddialar uydurmadır; müvekkil verisi yoktur.
Altın etiketleri iddiaları yazan kişi koydu: yazar yanlılığı olabilir.
"""
import json
import sys
import time
from pathlib import Path

JEV_DIR = Path(__file__).resolve().parents[2]   # depo kökü: olcum/<klasör>/bu_dosya
sys.path.insert(0, str(JEV_DIR))
import jev  # noqa: E402

jev.env_yukle(JEV_DIR / ".env")

MADDE = {
    "SMK120": {
        "atif": "SINAİ MÜLKİYET KANUNU (Kanun No. 6769, RG 10.01.2017/29944) m. 120",
        "baslik": "Çalışanın önalım hakkı",
        "metin": "MADDE 120- (1) İşverenin iflas etmesi ve iflas idaresinin de buluşu işletmeden ayrı olarak devretmek istemesi hâlinde çalışanın, yapmış olduğu ve işverenin de tam hak talebinde bulunduğu buluşa ilişkin olarak önalım hakkı vardır.\n\n(2) Çalışan buluşundan doğan bedel alacağı, imtiyazlı alacaklardandır. İflas idaresi bu nitelikteki birden çok bedel alacağını, alacaklılar arasında alacakları oranında dağıtır. Çalışan, bedel alacağı yerine buluşunun serbest buluşa dönüşmesini talep edebilir.",
    },
    "TBK146": {
        "atif": "TÜRK BORÇLAR KANUNU (Kanun No. 6098, RG sayı 27836) m. 146",
        "baslik": "",
        "metin": "MADDE 146- Kanunda aksine bir hüküm bulunmadıkça, her alacak on yıllık zamanaşımına tabidir.",
    },
    "TBK147": {
        "atif": "TÜRK BORÇLAR KANUNU (Kanun No. 6098, RG sayı 27836) m. 147",
        "baslik": "",
        "metin": "MADDE 147- Aşağıdaki alacaklar için beş yıllık zamanaşımı uygulanır:\n\n1. Kira bedelleri, anapara faizleri ve ücret gibi diğer dönemsel edimler.\n\n2. Otel, motel, pansiyon ve tatil köyü gibi yerlerdeki konaklama bedelleri ile lokanta ve benzeri yerlerdeki yeme içme bedelleri.\n\n3. Küçük sanat işlerinden ve küçük çapta perakende satışlardan doğan alacaklar.\n\n4. Bir ortaklıkta, ortaklık sözleşmesinden doğan ve ortakların birbirleri veya kendileri ile ortaklık arasındaki; bir ortaklığın müdürleri, temsilcileri, denetçileri ile ortaklık veya ortaklar arasındaki alacaklar.\n\n5. Vekâlet, komisyon ve acentalık sözleşmelerinden, ticari simsarlık ücreti alacağı dışında, simsarlık sözleşmesinden doğan alacaklar.\n\n6. Yüklenicinin yükümlülüklerini ağır kusuruyla hiç ya da gereği gibi ifa etmemesi dışında, eser sözleşmesinden doğan alacaklar.",
    },
    "ISK17": {
        "atif": "İŞ KANUNU (Kanun No. 4857, RG sayı 25134) m. 17",
        "baslik": "Süreli fesih",
        "metin": "Madde 17 - Belirsiz süreli iş sözleşmelerinin feshinden önce durumun diğer tarafa bildirilmesi gerekir.\n\nİş sözleşmeleri;\n\na) İşi altı aydan az sürmüş olan işçi için, bildirimin diğer tarafa yapılmasından başlayarak iki hafta sonra,\n\nb) İşi altı aydan birbuçuk yıla kadar sürmüş olan işçi için, bildirimin diğer tarafa yapılmasından başlayarak dört hafta sonra,\n\nc) İşi birbuçuk yıldan üç yıla kadar sürmüş olan işçi için, bildirimin diğer tarafa yapılmasından başlayarak altı hafta sonra,\n\nd) İşi üç yıldan fazla sürmüş işçi için, bildirim yapılmasından başlayarak sekiz hafta sonra,\n\nfeshedilmiş sayılır.\n\nBu süreler asgari olup sözleşmeler ile artırılabilir.\n\nBildirim şartına uymayan taraf, bildirim süresine ilişkin ücret tutarında tazminat ödemek zorundadır.\n\nİşveren bildirim süresine ait ücreti peşin vermek suretiyle iş sözleşmesini feshedebilir.",
    },
    "KVKK11": {
        "atif": "KİŞİSEL VERİLERİN KORUNMASI KANUNU (Kanun No. 6698, RG 07.04.2016/29677) m. 11",
        "baslik": "İlgili kişinin hakları",
        "metin": "MADDE 11- (1) Herkes, veri sorumlusuna başvurarak kendisiyle ilgili;\n\na) Kişisel veri işlenip işlenmediğini öğrenme,\n\nb) Kişisel verileri işlenmişse buna ilişkin bilgi talep etme,\n\nc) Kişisel verilerin işlenme amacını ve bunların amacına uygun kullanılıp kullanılmadığını öğrenme,\n\nç) Yurt içinde veya yurt dışında kişisel verilerin aktarıldığı üçüncü kişileri bilme,\n\nd) Kişisel verilerin eksik veya yanlış işlenmiş olması hâlinde bunların düzeltilmesini isteme,\n\ne) 7 nci maddede öngörülen şartlar çerçevesinde kişisel verilerin silinmesini veya yok edilmesini isteme,\n\nf) (d) ve (e) bentleri uyarınca yapılan işlemlerin, kişisel verilerin aktarıldığı üçüncü kişilere bildirilmesini isteme,\n\ng) İşlenen verilerin münhasıran otomatik sistemler vasıtasıyla analiz edilmesi suretiyle kişinin kendisi aleyhine bir sonucun ortaya çıkmasına itiraz etme,\n\nğ) Kişisel verilerin kanuna aykırı olarak işlenmesi sebebiyle zarara uğraması hâlinde zararın giderilmesini talep etme,\n\nhaklarına sahiptir.",
    },
    "HMK345": {
        "atif": "HUKUK MUHAKEMELERİ KANUNU (Kanun No. 6100, RG sayı 27836) m. 345",
        "baslik": "Başvuru süresi",
        "metin": "MADDE 345- (1) İstinaf yoluna başvuru süresi iki haftadır. Bu süre, ilamın usulen taraflardan her birine tebliğiyle işlemeye başlar. İstinaf yoluna başvuru süresine ilişkin özel kanun hükümleri saklıdır.",
    },
}

# (no, madde, iddia, altın durum, hata türü)
VAKALAR = [
    (1, "SMK120", "SMK m. 120, şirketin (işverenin) çalışanın buluşu üzerinde önalım hakkını düzenler.", "celisiyor", "hak sahibi ters (rehberdeki örnek hata)"),
    (2, "SMK120", "SMK m. 120'ye göre işveren iflas eder ve iflas idaresi buluşu işletmeden ayrı devretmek isterse, buluşu yapan çalışanın önalım hakkı vardır.", "destekliyor", "-"),
    (3, "SMK120", "SMK m. 120'ye göre işveren buluşu devretmek istediğinde, iflas şartı aranmaksızın her durumda çalışanın önalım hakkı doğar.", "celisiyor", "şart düşürülmüş (ince)"),
    (4, "SMK120", "SMK m. 120'ye göre çalışan buluşundan doğan bedel alacağı imtiyazlı alacaklardandır.", "destekliyor", "-"),
    (5, "TBK146", "TBK m. 146'ya göre, kanunda aksine hüküm yoksa her alacak on yıllık zamanaşımına tabidir.", "destekliyor", "-"),
    (6, "TBK146", "TBK m. 146'ya göre genel zamanaşımı süresi beş yıldır.", "celisiyor", "süre yanlış"),
    (7, "TBK146", "TBK m. 146, kira bedellerinin beş yıllık zamanaşımına tabi olduğunu düzenler.", "metinde_yok", "yanlış madde (doğrusu m. 147)"),
    (8, "TBK147", "TBK m. 147'ye göre kira bedelleri beş yıllık zamanaşımına tabidir.", "destekliyor", "-"),
    (9, "ISK17", "İş K. m. 17'ye göre işi altı aydan az sürmüş işçi için iş sözleşmesi, bildirimden başlayarak iki hafta sonra feshedilmiş sayılır.", "destekliyor", "-"),
    (10, "ISK17", "İş K. m. 17'ye göre bildirim süresi, işçinin kıdemine bakılmaksızın herkes için dört haftadır.", "celisiyor", "kademe yok sayılmış"),
    (11, "ISK17", "İş K. m. 17'ye göre bildirim süreleri azami sürelerdir; sözleşmeyle artırılamaz.", "celisiyor", "asgari/azami ters (ince)"),
    (12, "KVKK11", "KVKK m. 11'e göre herkes, kişisel verisinin işlenip işlenmediğini öğrenme hakkına sahiptir.", "destekliyor", "-"),
    (13, "KVKK11", "KVKK m. 11, veri sorumlularının Veri Sorumluları Siciline kayıt yükümlülüğünü düzenler.", "metinde_yok", "yanlış madde (sicil başka maddede)"),
    (14, "HMK345", "HMK m. 345'e göre istinaf süresi iki haftadır ve ilamın taraflara tebliğiyle işlemeye başlar.", "destekliyor", "-"),
    (15, "HMK345", "HMK m. 345'e göre istinaf süresi iki haftadır ve kararın tefhimiyle işlemeye başlar.", "celisiyor", "başlangıç anı yanlış (ince)"),
    (16, "HMK345", "HMK m. 345'e göre istinaf süresi otuz gündür.", "celisiyor", "süre yanlış"),
]

SORULAR = {
    "destek": jev.noul(
        "`iddia` cümlesi `madde.metin` içindeki hükümle tam olarak doğrulanıyor mu? "
        "Genel hukuk bilgisini değil yalnız madde metnini esas al. Hakkın veya "
        "yükümlülüğün sahibi, şart, süre, sürenin başlangıcı ve sonuç unsurlarının "
        "her biri metinle aynı olmalı.",
        {
            "true": "Madde metni iddianın bütün unsurlarını (kim, hangi şartla, hangi süre, "
                    "süre ne zaman başlar, hangi sonuç) aynı şekilde söylüyor.",
            "false": "İddianın en az bir unsuru metinde yok ya da metinle farklı: başka bir "
                     "kişi, eksik veya farklı şart, farklı süre ya da başlangıç anı, farklı sonuç.",
        },
    ),
    "durum": jev.choice(
        "`iddia` cümlesinin `madde.metin` ile ilişkisini sınıflandır. Yalnız madde metnini esas al.",
        {
            "destekliyor": "Metin iddiayı bütün unsurlarıyla doğruluyor.",
            "celisiyor": "Metin aynı konuyu düzenliyor ama iddianın bir unsurunu (kişi, şart, "
                         "süre, sürenin başlangıcı, sonuç) farklı söylüyor.",
            "metinde_yok": "Metin iddianın konusunu hiç düzenlemiyor; iddia başka bir maddeye "
                           "ait olabilir.",
        },
    ),
}


def main() -> None:
    istemci = jev.istemci_kur()
    if getattr(istemci, "sahte", True):
        print("UYARI: anahtar bulunamadı, SahteJev devrede — sonuç anlamsız, durduruldu.")
        sys.exit(2)
    print("istemci:", istemci.ad)
    satirlar = []
    for no, mk, iddia, altin, tur in VAKALAR:
        state = {"madde": MADDE[mk], "iddia": iddia}
        t0 = time.perf_counter()
        cev = istemci.sor(state, SORULAR)
        ms = (time.perf_counter() - t0) * 1000
        p = float(cev["destek"].deger)
        d = cev["durum"].deger
        satirlar.append({"no": no, "madde": mk, "altin": altin, "tur": tur,
                         "p_destek": p, "durum": d, "ms": round(ms)})
        print("#%-2d %-7s altin=%-11s p_destek=%.2f durum=%-11s %5.0f ms  %s"
              % (no, mk, altin, p, d, ms, tur))

    # Özet: iddia yanlış mı? (altin != destekliyor) — "yakalama" = bayrak kaldırmak
    def ozet(esik: float) -> str:
        yakalanan = kacan = yanlis_alarm = dogru_gecen = 0
        for s in satirlar:
            yanlis_iddia = s["altin"] != "destekliyor"
            bayrak = s["p_destek"] < esik
            if yanlis_iddia and bayrak:
                yakalanan += 1
            elif yanlis_iddia:
                kacan += 1
            elif bayrak:
                yanlis_alarm += 1
            else:
                dogru_gecen += 1
        return ("esik %.2f: hatali iddia yakalanan %d/%d, kacan %d | dogru iddiaya "
                "yanlis alarm %d/%d" % (esik, yakalanan, yakalanan + kacan, kacan,
                                        yanlis_alarm, yanlis_alarm + dogru_gecen))

    print()
    for e in (0.3, 0.5, 0.7, 0.9):
        print(ozet(e))
    uc_sinif = sum(1 for s in satirlar if s["durum"] == s["altin"])
    print("choice 3 sinif tam isabet: %d/%d" % (uc_sinif, len(satirlar)))
    print("olcer:", istemci.olcer.ozet())
    cikti = Path(__file__).with_name("atif_koklama_sonuc.json")
    cikti.write_text(json.dumps({"tarih": "2026-09-28", "istemci": istemci.ad,
                                 "satirlar": satirlar}, ensure_ascii=False, indent=1),
                     encoding="utf-8")
    print("ham kayit:", cikti.name)


if __name__ == "__main__":
    main()
