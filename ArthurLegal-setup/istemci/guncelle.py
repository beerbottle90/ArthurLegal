"""ArthurLegal sessiz güncelleyici.

Oturum açılışında (HKCU Run) ve yerel sunucu açıkken 6 saatte bir çalışır:
1. En son GitHub Release'teki arthurlegal-manifest.json ve .sig indirilir; imza, kurulumdaki
   yayın anahtarıyla (Ed25519) doğrulanmadan hiçbir şey kurulmaz.
2. Manifest'teki paket sürümü etkin sürümden yeniyse zip indirilir, sha256 doğrulanır, yeni
   bir surumler\\<sürüm> klasörüne açılır ve aktif.txt tek adımda değiştirilir. Çalışan
   sunucular eski klasörle devam eder; yeni sürüm Claude Desktop'ın bir sonraki açılışında
   devreye girer. Bir önceki sürüm geri dönüş için saklanır.
3. Arthur Mask kurulu sürümden yeniyse (≈1 GB) arka planda indirilir, Claude Desktop kapalıyken
   sessiz kurulur.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
import urllib.error
import zipfile
from pathlib import Path
from urllib.parse import urljoin

import ed25519
import ortak


class GuncellemeHatasi(Exception):
    pass


def _dogrula(ham: bytes, imza_metni: bytes, ayar: dict) -> dict:
    anahtar = bytes.fromhex(ayar.get("yayin_anahtari") or "")
    if len(anahtar) != 32:
        raise GuncellemeHatasi("kurulumda yayın anahtarı yok")
    if not ed25519.verify(anahtar, ham, bytes.fromhex(imza_metni.decode("ascii").strip())):
        raise GuncellemeHatasi("manifest imzası geçersiz; güncelleme reddedildi")
    return json.loads(ham.decode("utf-8"))


def _api_basliklari(ayar: dict, tur="application/vnd.github+json") -> dict:
    basliklar = {"Accept": tur, "X-GitHub-Api-Version": "2022-11-28"}
    if ayar.get("jeton"):
        basliklar["Authorization"] = "Bearer " + ayar["jeton"]
    return basliklar


def manifest_getir(ayar: dict):
    """(manifest, indirici) döndürür; yayın yoksa (None, None). indirici(dosya_adı, hedef) -> sha256.

    Dağıtım private depodan yapılır: varlıklar GitHub API'sinden, kurulumdaki salt okunur jetonla
    indirilir. manifest_url verilmişse (yerel sunucu, testler) düz HTTP yolu kullanılır.
    """
    depo = ayar.get("dagitim_deposu")
    if depo:
        if not ayar.get("jeton"):
            return None, None  # güncelleme kanalı yapılandırılmamış
        taban_api = ayar.get("api_tabani") or "https://api.github.com"
        yayinlar = json.loads(ortak.indir(f"{taban_api}/repos/{depo}/releases?per_page=10",
                                          zaman=30, basliklar=_api_basliklari(ayar)).decode("utf-8"))
        beta = ayar.get("kanal") == "beta"
        for yayin in yayinlar:
            if yayin.get("draft") or (yayin.get("prerelease") and not beta):
                continue
            varliklar = {a["name"]: a for a in yayin.get("assets", [])}
            if "arthurlegal-manifest.json" not in varliklar or "arthurlegal-manifest.sig" not in varliklar:
                continue

            def indirici(dosya, hedef=None, varliklar=varliklar):
                if dosya not in varliklar:
                    raise GuncellemeHatasi(f"yayında yok: {dosya}")
                return ortak.indir(varliklar[dosya]["url"], hedef, zaman=180,
                                   basliklar=_api_basliklari(ayar, "application/octet-stream"))

            manifest = _dogrula(indirici("arthurlegal-manifest.json"), indirici("arthurlegal-manifest.sig"), ayar)
            return manifest, indirici
        return None, None

    url = ayar.get("manifest_url")
    if not url:
        return None, None
    try:
        ham = ortak.indir(url, zaman=30)
    except urllib.error.HTTPError as e:
        if e.code != 404 or not ayar.get("yedek_depo"):
            raise
        # En son yayın manifest taşımıyorsa (ör. yalnız sürüm notu) taşıyan en yeni yayın aranır.
        taban_api = ayar.get("api_tabani") or "https://api.github.com"
        yayinlar = json.loads(ortak.indir(f"{taban_api}/repos/{ayar['yedek_depo']}/releases?per_page=10", zaman=30,
                                          basliklar=_api_basliklari(ayar)).decode("utf-8"))
        beta = ayar.get("kanal") == "beta"
        url = next((a["browser_download_url"] for y in yayinlar
                    if not y.get("draft") and (beta or not y.get("prerelease"))
                    for a in y.get("assets", []) if a.get("name") == "arthurlegal-manifest.json"), None)
        if not url:
            return None, None
        ham = ortak.indir(url, zaman=30)
    manifest = _dogrula(ham, ortak.indir(url[: -len(".json")] + ".sig", zaman=30), ayar)
    taban = manifest.get("taban") or url.rsplit("/", 1)[0] + "/"

    def indirici(dosya, hedef=None):
        return ortak.indir(urljoin(taban, dosya), hedef, zaman=180)

    return manifest, indirici


def _guvenli_ac(zip_yolu: Path, hedef: Path) -> None:
    with zipfile.ZipFile(zip_yolu) as z:
        for ad in z.namelist():
            yol = (hedef / ad).resolve()
            if not str(yol).startswith(str(hedef.resolve())) or ad.startswith(("/", "\\")):
                raise GuncellemeHatasi(f"zip içinde geçersiz yol: {ad}")
        z.extractall(hedef)


def paket_guncelle(manifest: dict, indirici) -> bool:
    yeni, etkin = manifest["surum"], ortak.aktif() or (ortak.surumler() or ["0"])[-1]
    if ortak.surum_demeti(yeni) <= ortak.surum_demeti(etkin):
        return False
    p = manifest["paket"]
    indirilen = ortak.VERI / "indirilen" / p["dosya"]
    sha = indirici(p["dosya"], indirilen)
    if sha != p["sha256"]:
        indirilen.unlink(missing_ok=True)
        raise GuncellemeHatasi(f"paket sha256 uyuşmadı ({p['dosya']})")
    surumler = ortak.KOK / "surumler"
    gecici = surumler / f"{yeni}.yeni"
    shutil.rmtree(gecici, ignore_errors=True)
    _guvenli_ac(indirilen, gecici)
    if (gecici / "surum.txt").read_text(encoding="utf-8").strip() != yeni or not (gecici / "istemci" / "arthurlegal_sunucu.py").exists():
        shutil.rmtree(gecici, ignore_errors=True)
        raise GuncellemeHatasi("paket içeriği beklenen sürümle uyuşmuyor")
    shutil.rmtree(surumler / yeni, ignore_errors=True)
    os.replace(gecici, surumler / yeni)
    ortak.aktif_yaz(yeni)
    indirilen.unlink(missing_ok=True)
    for eski in ortak.surumler()[:-2]:  # etkin + bir önceki kalır
        shutil.rmtree(surumler / eski, ignore_errors=True)
    ortak.gunluk("guncelle", f"paket {etkin} -> {yeni}")
    return True


def mask_guncelle(manifest: dict) -> str:
    m = manifest.get("mask")
    if not m:
        return "mask: manifest'te yok"
    kurulu = ortak.mask_surumu()
    if kurulu and ortak.surum_demeti(kurulu) >= ortak.surum_demeti(m["surum"]):
        return f"mask: güncel ({kurulu})"
    exe = ortak.VERI / "indirilen" / f"ArthurMask-Kurulum-{m['surum']}.exe"
    if not (exe.exists() and ortak.sha256_dosya(exe) == m["sha256"]):
        if ortak.indir(m["url"], exe, zaman=120) != m["sha256"]:
            exe.unlink(missing_ok=True)
            raise GuncellemeHatasi("Arthur Mask sha256 uyuşmadı")
    if ortak.claude_calisiyor():
        return "mask: indirildi, Claude Desktop kapanınca kurulacak"
    sonuc = subprocess.run([str(exe), "/VERYSILENT", "/SUPPRESSMSGBOXES", "/NORESTART", "/SP-"],
                           creationflags=ortak.PENCERESIZ, timeout=3600)
    if sonuc.returncode != 0:
        raise GuncellemeHatasi(f"Arthur Mask kurulumu {sonuc.returncode} ile bitti")
    exe.unlink(missing_ok=True)
    ortak.gunluk("guncelle", f"Arthur Mask {kurulu or 'yok'} -> {m['surum']}")
    return f"mask: {m['surum']} kuruldu"


def _claude_kaydet() -> None:
    """Etkin (belki yeni) sürümün kodu ile Claude Desktop kaydını tazeler."""
    py = ortak.RUNTIME / "python.exe"
    if py.exists():
        subprocess.run([str(py), "-B", str(ortak.AL), "kur", "--kaydet"], creationflags=ortak.PENCERESIZ, timeout=120)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="ArthurLegal güncelleyici")
    ap.add_argument("--sessiz", action="store_true", help="arka plan çalıştırması")
    ap.add_argument("--mask-yok", action="store_true", help="Arthur Mask'e dokunma")
    args = ap.parse_args(argv)

    kilit = ortak.VERI / "guncelle.kilit"
    kilit.parent.mkdir(parents=True, exist_ok=True)
    try:
        if kilit.exists() and time.time() - kilit.stat().st_mtime > 7200:
            kilit.unlink()
        fd = os.open(kilit, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except OSError:
        return 0  # başka bir güncelleyici çalışıyor
    try:
        os.write(fd, str(os.getpid()).encode())
        os.close(fd)
        ortak.durum_guncelle(son_denetim=time.time())
        sonuclar = []
        try:
            manifest, indirici = manifest_getir(ortak.ayar())
            if manifest is None:
                sonuclar.append("yayında manifest yok")
            else:
                sonuclar.append(f"paket {manifest['surum']} kuruldu" if paket_guncelle(manifest, indirici)
                                else f"paket güncel ({ortak.aktif()})")
                if not args.mask_yok:
                    sonuclar.append(mask_guncelle(manifest))
        except (GuncellemeHatasi, OSError, ValueError, KeyError) as e:
            sonuclar.append(f"hata: {e}")
            ortak.gunluk("guncelle", f"hata: {e!r}")
        _claude_kaydet()
        ortak.durum_guncelle(son_sonuc="; ".join(sonuclar))
        if not args.sessiz:
            print("\n".join(sonuclar))
        return 1 if any(s.startswith("hata") for s in sonuclar) else 0
    finally:
        kilit.unlink(missing_ok=True)


if __name__ == "__main__":
    sys.exit(main())
