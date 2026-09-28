"""Birleşik motor — yerel kural/model + Jev, ikisinin azamisi.

Bu modül bir tahminin değil, bir ÖLÇÜMÜN ürünüdür. Tutulan 56 kalemlik altın
kümede Jev ile yerel motor farklı yerlerde hata yaptı:

    JEV yakaladı, YEREL kaçırdı
      [enerji] jev=0.49 yerel=0.00  Katı Yakıtların Kontrolü Yönetmeliği
      [enerji] jev=0.28 yerel=0.08  Isınmadan Kaynaklanan Hava Kirliliği Yön.

    YEREL yakaladı, JEV kaçırdı
      [icra]   jev=0.18 yerel=1.00  BM Güvenlik Konseyi ... Malvarlığının
                                     Dondurulması

Sebepleri simetrik ve öğretici:

  * Jev'in DÜNYA BİLGİSİ var. "Katı yakıt"ın kömür demek olduğunu, ısınma
    yönetmeliğinin yakıt düzenlediğini biliyor. Yerel modelin 776 günlük
    gövdesinde bu kalıptan bir tane var — öğrenemez.
  * Yerelin ALAN KURALLARI var. "Malvarlığının dondurulması"nın cebrî icra
    olduğunu bir kural söylüyor ve o kural veto edilemiyor. Jev bunu Türk
    hukuku bağlamında görmediği için 0.18 diyor.

Birleştirme yine ``max`` ile yapılır — aynı "yalnız ekler" ilkesi. Ölçülen
sonuç: kaçan 3 → **1**, duyarlılık icra'da %50→%100 ve enerji'de %62→%88.
Bedeli triyajın %73'ten %62'ye düşmesi, yani Opus'a 15 yerine 21 kalem gitmesi.
Bir kaçağı altı fazladan okumayla değiştirmek, bu işte doğru takastır.

Jev'e YALNIZ kamuya açık metin gider (Resmî Gazete başlığı). Müvekkil verisi
bu motordan geçemez; ``sor`` çağrısı state'i olduğu gibi iletir, dolayısıyla
ne gönderildiği çağıranın sorumluluğundadır — pilot_b yalnız fihrist yollar.
"""

from __future__ import annotations

import time
from typing import Any, Dict, Optional

from jev import Cevap, JevHatasi, Olcer


class BirlesikMotor:
    """``sor(state, sorular)`` sözleşmesini taşır; iki motoru birleştirir.

    Jev erişilemezse (ağ, 429, anahtar yok) sessizce yerele düşer ve bunu
    ``jev_hatasi`` sayacında tutar. Bir ön elemede dış uç çökünce bütün
    boru hattının durması kabul edilemez; yerel motor her zaman ayaktadır.
    """

    sahte = False
    yerel = True

    def __init__(self, yerel_motor: Any, jev_istemci: Optional[Any] = None,
                 *, ad: str = "Birleşik (yerel + Jev)") -> None:
        self._yerel = yerel_motor
        self._jev = jev_istemci
        self.ad = ad if jev_istemci is not None else "Birleşik (yalnız yerel)"
        self.olcer = Olcer()
        self.jev_hatasi = 0
        self.kaynak_sayaci = {"yerel": 0, "jev": 0, "esit": 0}

    def sor(self, state: Any, sorular: Dict[str, Dict[str, Any]]) -> Dict[str, Cevap]:
        basla = time.perf_counter()
        yerel_cevap = self._yerel.sor(state, sorular)

        jev_cevap: Dict[str, Cevap] = {}
        if self._jev is not None:
            try:
                jev_cevap = self._jev.sor(state, sorular)
            except JevHatasi:
                self.jev_hatasi += 1

        cikti: Dict[str, Cevap] = {}
        for ad in sorular:
            y = float(yerel_cevap[ad].deger)
            if ad in jev_cevap:
                j = float(jev_cevap[ad].deger)
                if j > y:
                    self.kaynak_sayaci["jev"] += 1
                elif y > j:
                    self.kaynak_sayaci["yerel"] += 1
                else:
                    self.kaynak_sayaci["esit"] += 1
                deger = max(y, j)
            else:
                self.kaynak_sayaci["yerel"] += 1
                deger = y
            cikti[ad] = Cevap(ad, "noul", round(deger, 4), sahte=False)

        # Maliyet Jev tarafındadır; yerelin token'ı yok.
        if self._jev is not None:
            self.olcer.girdi_token = self._jev.olcer.girdi_token
        self.olcer.ekle(0, time.perf_counter() - basla)
        self.olcer.girdi_token = (self._jev.olcer.girdi_token
                                  if self._jev is not None else 0)
        return cikti

    def neden(self, state: Any, konu: str, kac: int = 8) -> Dict[str, Any]:
        """Yerel motorun gerekçesi; Jev gerekçe üretmez (metin yazmaz)."""
        g = self._yerel.neden(state, konu, kac)
        g["not"] = ("Jev bir gerekçe döndürmez — yalnız olasılık verir. "
                    "Aşağıdaki dayanak yerel motorundur.")
        return g
