"""belge_oku testleri: redline'ı koruyan DOCX okuması, yol güvenliği, markitdown yokken PDF.
Ağa çıkmaz; belgeler geçici klasörde standart kütüphaneyle üretilir.

    python -m unittest discover -s tests
"""
import os
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest import mock

BURASI = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BURASI / "istemci"))
import belge_oku  # noqa: E402

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"


def docx_yaz(yol: Path, govde: str, yorumlar: str = "") -> None:
    parcalar = {
        "[Content_Types].xml": (
            '<?xml version="1.0" encoding="UTF-8"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
            '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
            '<Default Extension="xml" ContentType="application/xml"/>'
            '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
            "</Types>"),
        "_rels/.rels": (
            '<?xml version="1.0" encoding="UTF-8"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>'
            "</Relationships>"),
        "word/styles.xml": (f'<?xml version="1.0" encoding="UTF-8"?><w:styles xmlns:w="{W}">'
                            '<w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/></w:style></w:styles>'),
        "word/document.xml": f'<?xml version="1.0" encoding="UTF-8"?><w:document xmlns:w="{W}"><w:body>{govde}</w:body></w:document>',
    }
    if yorumlar:
        parcalar["word/comments.xml"] = f'<?xml version="1.0" encoding="UTF-8"?><w:comments xmlns:w="{W}">{yorumlar}</w:comments>'
    with zipfile.ZipFile(yol, "w") as z:
        for ad, icerik in parcalar.items():
            z.writestr(ad, icerik.encode("utf-8"))


REDLINE = (
    '<w:p><w:pPr><w:pStyle w:val="Heading2"/></w:pPr><w:r><w:t>MADDE 4 – ÜCRET</w:t></w:r></w:p>'
    '<w:p><w:r><w:t xml:space="preserve">Ödeme </w:t></w:r>'
    '<w:del w:id="1" w:author="Karşı Taraf"><w:r><w:delText>30 (otuz) gün</w:delText></w:r></w:del>'
    '<w:ins w:id="2" w:author="Karşı Taraf"><w:r><w:t>15 (on beş) gün</w:t></w:r></w:ins>'
    '<w:r><w:t xml:space="preserve"> içinde yapılır.</w:t></w:r></w:p>'
    '<w:p><w:commentRangeStart w:id="0"/><w:r><w:t>Gecikme faizi yıllık %24.</w:t></w:r>'
    '<w:commentRangeEnd w:id="0"/><w:r><w:commentReference w:id="0"/></w:r></w:p>'
    '<w:tbl><w:tr><w:tc><w:p><w:r><w:t>Taksit</w:t></w:r></w:p></w:tc><w:tc><w:p><w:r><w:t>Tutar</w:t></w:r></w:p></w:tc></w:tr>'
    '<w:tr><w:tc><w:p><w:r><w:t>1</w:t></w:r></w:p></w:tc><w:tc><w:p><w:r><w:t>125.000,00 TL</w:t></w:r></w:p></w:tc></w:tr></w:tbl>'
)
YORUM = ('<w:comment w:id="0" w:author="Karşı Taraf" w:date="2026-09-10T10:05:00Z">'
         "<w:p><w:r><w:t>Faiz %12'ye indirilsin.</w:t></w:r></w:p></w:comment>")


class BelgeOkuTesti(unittest.TestCase):
    def setUp(self):
        self.gecici = tempfile.TemporaryDirectory()
        self.kok = Path(self.gecici.name)
        self.ortam = mock.patch.dict(os.environ, {"USERPROFILE": str(self.kok)})
        self.ortam.start()

    def tearDown(self):
        self.ortam.stop()
        self.gecici.cleanup()

    def test_redline_silinen_metin_ve_yorum_korunur(self):
        yol = self.kok / "karsi-taraf.docx"
        docx_yaz(yol, REDLINE, YORUM)
        md = belge_oku.oku(str(yol))
        self.assertIn("{--30 (otuz) gün--}", md, "silinen metin kaybolmamalı")
        self.assertIn("{++15 (on beş) gün++}", md)
        self.assertIn("{==Gecikme faizi yıllık %24.==}{>>Karşı Taraf 2026-09-10: Faiz %12'ye indirilsin.<<}", md)
        self.assertIn("1 ekleme, 1 silme, 1 yorum", md)
        self.assertIn("## MADDE 4 – ÜCRET", md)
        self.assertIn("| Taksit | Tutar |", md)

    def test_temiz_docx_ozet_satiri_tasimaz(self):
        yol = self.kok / "temiz.docx"
        docx_yaz(yol, "<w:p><w:r><w:t>Temiz metin.</w:t></w:r></w:p>")
        self.assertEqual(belge_oku.oku(str(yol)).strip(), "Temiz metin.")

    def test_kullanici_klasoru_disi_ve_uzanti_reddedilir(self):
        disari = Path(tempfile.gettempdir()) / "arthurlegal-test-disari.docx"
        with self.assertRaises(belge_oku.BelgeHatasi):
            belge_oku.oku(str(disari))
        (self.kok / "ayar.json").write_text("{}", encoding="utf-8")
        with self.assertRaises(belge_oku.BelgeHatasi):
            belge_oku.oku(str(self.kok / "ayar.json"))

    def test_markitdown_yokken_pdf_metin_uydurmaz(self):
        yol = self.kok / "karar.pdf"
        yol.write_bytes(b"%PDF-1.4\n%%EOF\n")
        with mock.patch.object(belge_oku.shutil, "which", return_value=None):
            metin = belge_oku.oku(yol.as_uri())
        self.assertIn("UYDURULMADI", metin)

    def test_uzun_belge_parca_parca(self):
        yol = self.kok / "uzun.docx"
        docx_yaz(yol, "".join(f"<w:p><w:r><w:t>Satır {i} {'x' * 90}</w:t></w:r></w:p>" for i in range(1000)))
        ilk = belge_oku.oku(str(yol))
        self.assertIn("baslangic=60000", ilk)
        self.assertIn("Satır", belge_oku.oku(str(yol), 60000)[:200], "ikinci parça kaldığı yerden sürmeli")


if __name__ == "__main__":
    unittest.main()
