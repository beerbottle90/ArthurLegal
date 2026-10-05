# Arthur Mask — User Guide

**Arthur Mask 1.0.0** · ships with ArthurLegal Law Firm Assistant v1.8.0 · 2026-09-13
Türkçe → [ARTHUR-MASK.md](ARTHUR-MASK.md)

Arthur Mask is a Windows app that masks client documents **on your own computer**
before Claude sees them. Names, companies, national ID and tax numbers, IBANs,
addresses, phone numbers, e-mail addresses, birth dates, file numbers, passport
numbers and licence plates are replaced with labels such as `{{KİŞİ-01}}`,
`{{ŞİRKET-02}}` or `{{TCKN-01}}`. The real values stay on your computer, in an
encrypted vault kept separately for each matter. Claude receives only the masked
text; its answer is turned back into real names on your computer and opened in
Word or as a UDF file.

> **Important.** Arthur Mask works only with **Claude Desktop for Windows**. It does
> not work in claude.ai in the web browser or in the mobile apps. Open your ArthurLegal
> Project from Claude Desktop; Projects are shared between web and desktop.

> **[⬇ Download the installer (Windows, about 1 GB)](https://github.com/beerbottle90/ArthurLegal/releases/download/arthur-mask/ArthurMask-Kurulum.exe)** · direct download, no GitHub account needed

---

## When to use it

- **Use it for:** pleadings, contracts, expert reports, correspondence and minutes that name clients, counterparties, witnesses or employees, or contain ID numbers, addresses, phone numbers, IBANs or file numbers.
- **Not needed for:** legal research questions that name no person or company, legislation and case-law searches, blank templates.
- **When in doubt:** if a document contains even one detail that identifies a person or company, run it through Arthur Mask. Do not paste or attach the document to the Claude chat directly; that path bypasses Arthur Mask.

If you have not set up the ArthurLegal Project yet, complete [INSTALLATION.md](INSTALLATION.md) first.

---

## 1. What you need

| | |
|---|---|
| Computer | Windows 10 or 11, 64-bit |
| Claude | Claude Desktop for Windows: [claude.ai/download](https://claude.ai/download) |
| Disk | About 4 GB free |
| Memory | 8 GB RAM recommended |
| Internet | Not needed for masking; the app works fully offline |

Your document data does not leave your computer. The only thing that goes out is the
masked text Claude Desktop receives. That text goes to Claude, that is, to Anthropic, and your Claude
account's data-use and retention settings apply to it. The only other network call is a once-a-day
update check that reads the latest version number from the ArthurLegal releases page
(no document data).

---

## 2. Installation (about 10 minutes)

1. **Download.** **[⬇ Click here to download the Arthur Mask installer](https://github.com/beerbottle90/ArthurLegal/releases/download/arthur-mask/ArthurMask-Kurulum.exe)** (Windows, about 1 GB).
   No GitHub account or GitHub knowledge is needed: the link downloads `ArthurMask-Kurulum.exe` straight into
   your **Downloads** folder. Depending on your connection this can take a few minutes. If the browser asks
   whether to keep the file, choose **Keep**. When the download finishes, double-click the file in Downloads.
2. **Run it.** The installer is not code-signed, so Windows SmartScreen may say
   **"Windows protected your PC"** (Turkish: "Windows bilgisayarınızı korudu"):
   **More info** → **Run anyway**. Some antivirus products scan the file for a while.
3. **Install.** No administrator rights needed. It installs to
   `%LOCALAPPDATA%\Programs\Arthur Mask`, adds an **Arthur Mask** shortcut to the Start
   menu and desktop, and registers the `arthur-mask` local connector in Claude
   Desktop's configuration (a backup of the previous configuration file is kept).
4. **Restart Claude Desktop.** Quit Claude Desktop **completely** (also from the system
   tray icon), then open it again.
5. **Check.** In Claude Desktop → **Settings → Developer**, `arthur-mask` is listed as
   running. In a chat, the tools menu shows the Arthur Mask tools.

---

## 3. First thing: the recovery key

Open Arthur Mask → top menu **Kurtarma anahtarı** (recovery key).

Your vaults are protected by your Windows user account. If the computer changes or
Windows is reinstalled, **only this key** opens them. The key is shown once: print it
or store it safely, then press **Sakladım** ("I have stored it"). **Never type the key
into Claude.**

---

## 4. Everyday use in six steps

The interface is in Turkish; button names are given as they appear.

**1. Open.** The **Arthur Mask** shortcut opens `http://127.0.0.1:47831` in your
browser. The top-right chips read **Claude Desktop'a bağlı** (connected to Claude
Desktop) and **Tam koruma** (full protection).

**2. Drop the document.** Word (.docx), UYAP (.udf), PDF, scanned PDF or photo, .txt or
.md. The first document creates a new matter (**dosya**) named after it. Use
**+ Yeni dosya** for another client or matter. Documents in the same matter share
labels: the same person gets the same label in every document.

**3. Review.** If the status is **Onayınızı bekliyor** (awaiting your approval) or
**Kırmızı hat** (red line), open **İncele**:

- For each uncertain item choose **Maskele** (mask) or **Açık bırak** (leave visible).
- Check the masked copy.
- For red-line content (defence strategy, settlement limits, special categories of
  personal data, inside information), write a short justification; sending stays
  blocked until you do.
- Press **Onayla — Claude'a hazırla** (approve, prepare for Claude).

**4. Hand it to Claude.** Arthur Mask shows a command such as:

```
Arthur Mask'teki belge-1'i incele
```

Copy it into the **ArthurLegal Project chat in Claude Desktop** and add what you need.
**Do not also attach the original document to the chat.**

**5. Get the answer.** Claude's answer appears under **Cevaplar** (answers) with real
names: **Word'de aç** (open in Word), **UYAP editöründe aç** (open in the UYAP editor)
or, for revisions, **Word'de aç (izli değişiklikler)**: the changes are applied to your
original document as Word tracked changes, with the layout preserved. Tabs
**Gerçek adlarla / Claude'daki hâli** show the real-name and the masked version.

**6. Audit.** The **Claude'a giden** panel shows exactly what Claude received.
**Sızıntı denetimi yap** (run leak check) re-scans everything sent and received against
the vault and returns **✓ Temiz** (clean) or a list of findings.

---

## 5. Four safeguards

1. **Review screen.** Uncertain detections wait for your decision.
2. **Red line.** Content that must not go to AI even when masked cannot be sent without
   your written justification.
3. **Exit gate.** Every response sent to Claude is re-scanned against all real values in
   the vault right before sending; any occurrence is replaced with its label. The gate recognises values
   that were **detected at least once** in any document of the matter; it cannot catch information that
   was never detected. That is what the review screen and your own reading are for.
4. **Log and leak check.** Everything sent to Claude is logged in masked form, and you
   can run a leak check at any time.

---

## 6. Where your data is

`Documents\Arthur Mask\<matter name>` (`Belgeler` on a Turkish Windows). Masked copies
are deleted automatically after 30 days; decoded answers and the vault remain. Your
firm's retention and destruction rules apply to this folder too.

---

## 7. Updates and uninstalling

**Updates.** When a newer installer is published on the ArthurLegal releases page, the
Arthur Mask interface shows a notice. Download the new file from [the same link](https://github.com/beerbottle90/ArthurLegal/releases/download/arthur-mask/ArthurMask-Kurulum.exe) and install it
over the old one; your matters, vaults and recovery key are kept.

**Verifying the file (optional).** The installer's SHA-256 is published on the [Arthur Mask release page](https://github.com/beerbottle90/ArthurLegal/releases/tag/arthur-mask).
In PowerShell, `Get-FileHash .\ArthurMask-Kurulum.exe` must print the same value.

**Uninstall.** Windows **Settings → Apps → Arthur Mask → Uninstall**. This removes the
program and the Claude Desktop connector entry. The `Arthur Mask` documents folder and
the recovery key file are kept; delete them manually if you wish.

---

## 8. Troubleshooting

| What you see | What to do |
|---|---|
| **Bağlantı yok — Claude Desktop'u açın** (no connection) | Claude Desktop is not running or was not restarted after installation. Quit completely and reopen. |
| Arthur Mask tools not visible in Claude | Quit Claude Desktop completely (including the tray icon) and reopen; check `arthur-mask` under **Settings → Developer**. |
| **Koruma hazırlanıyor…** (preparing protection) | Normal for about 15 to 30 seconds after start (models loading). |
| **Temel koruma** (basic protection) | The AI detection or OCR component could not load; rules still work. Reinstall. |
| Claude says the document is not ready | Finish the review in Arthur Mask and approve. |
| Unknown label warning under an answer | Claude altered a label; check that sentence. |
| **Leak check** shows findings | "Before the exit gate" rows mean the value sits in the stored masked text and is labelled on the way to Claude. A "text Claude wrote" row means Claude saw that value in plain form somewhere, for example something typed or attached in the chat. Review that conversation and re-mask the document in a new matter. |
| Not working in claude.ai web or on the phone | Not supported; use Claude Desktop. |

---

## 9. FAQ

**Is the masked document anonymous?**
No. Legally this is **pseudonymisation**, not anonymisation. The real values sit in
your vault and the labels can be reversed; the remaining text may still identify a
person in context.

**Does Arthur Mask catch every piece of personal data?**
That cannot be guaranteed; detection is probabilistic. This is why the review screen,
the exit gate and the leak check exist. Look at the masked copy before sending.

**What is deliberately not masked?**
Dates and amounts (needed for deadlines and calculations). Supreme court and high
court citations are preserved. If an amount is itself confidential (a settlement
limit, for example), use the red line or remove that part.

**What cannot be masked?**
Images and embedded objects inside Word files; handwriting, signatures, stamps and QR
codes in scans.

**Does using Arthur Mask shift my responsibility?**
No. Your obligations under data protection law (KVKK, GDPR), professional secrecy,
trade secret rules and NDAs remain in full. Arthur Mask helps you meet them; the
decision to send masked text to Claude is yours.

**English or Azerbaijani documents?**
Supported. Bilingual two-column Word contracts keep their table structure, and Claude
revises both language columns together.

**Why not claude.ai on the web?**
Remote connectors on claude.ai are called from Anthropic's cloud, which cannot reach a
program running on your computer. The gate works only through Claude Desktop's local
connector.

**Where is the source code?**
Arthur Mask is distributed as an installer only. Notices for the third-party
open-source components it bundles ship inside the installation folder; see
[ATTRIBUTION.md](ATTRIBUTION.md).
