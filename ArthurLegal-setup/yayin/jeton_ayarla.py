"""Kurulumların güncelleme için kullanacağı salt okunur GitHub jetonunu kaynaklar.json'a yazar.

    python yayin/jeton_ayarla.py github_pat_...

Jeton, private dağıtım deposuna yalnız okuma yetkisiyle üretilir:
GitHub → Settings → Developer settings → Personal access tokens → Fine-grained tokens → Generate new token
  · Resource owner: hesabınız · Only select repositories: dağıtım deposu (kaynaklar.json > dagitim_deposu)
  · Repository permissions → Contents: Read-only  · Expiration: 1 yıl
Jeton kurulum dosyasının içine gömülür: kurulumu elinde tutan kişi dağıtım deposunu okuyabilir,
başka hiçbir depoya erişemez. Süresi dolunca yeni jetonla yeniden derleyip dağıtın.
"""
import json
import sys
from pathlib import Path

BURASI = Path(__file__).resolve().parents[1]


def main(argv=None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 1 or not argv[0].strip():
        sys.exit("kullanım: python yayin/jeton_ayarla.py <github_pat_...>")
    yol = BURASI / "kaynaklar.json"
    k = json.loads(yol.read_text(encoding="utf-8"))
    k["istemci_jetonu"] = argv[0].strip()
    yol.write_text(json.dumps(k, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Jeton yazıldı ({len(k['istemci_jetonu'])} karakter). Şimdi yeniden derleyip dağıtın:\n"
          "  python yayin/derle.py\n"
          "  python yayin/yayinla.py <etiket> --on-surum")
    return 0


if __name__ == "__main__":
    sys.exit(main())
