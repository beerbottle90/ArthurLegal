# Where your data goes

[Türkçe](verileriniz.md) · [Azərbaycan dili](melumatlariniz.md)

ArthurLegal is free and open source; it does not enter into a service contract with you. What follows is therefore
not a contractual promise but **the design itself**: every row is backed by open code that anyone can check.

## In one table

| What | Where it stays | Who receives it |
|---|---|---|
| Your question and Claude's answer | In Claude (Anthropic). The desk's history also stays on your own device: in the installation folder if ArthurLegal is installed on your computer, otherwise in the desk's browser storage; deleted after 90 days. | Anthropic, under the terms of your own Claude use (see "Your Claude setting" below). |
| Research requests (search words, statute and article numbers, case references) | The ArthurLegal server does not store search text and keeps no request logs. The exceptions (short caches of the German and Azerbaijani tools) are in the [server's privacy policy](https://github.com/beerbottle90/arthurlegal-mcp/blob/master/PRIVACY.md). | The ArthurLegal MCP server (Fly.io, Amsterdam), and from there, with only the necessary parameters, the official source: mevzuat.gov.tr, the Official Gazette, the Court of Cassation, the Council of State, the Constitutional Court and regulators. For semantic search, the search text goes to Voyage AI to compute its meaning. |
| Client documents (with ArthurMask) | The original document and the real names and numbers stay only on your computer. | Claude receives only labelled text (e.g. `{{KİŞİ-01}}`). The real value behind a label is not sent to Claude. |
| UYAP | ArthurLegal writes nothing to UYAP; it reads, on your computer, the lists you open in UYAP. | Case numbers reach Claude labelled; the real values appear only on your screen. |
| ArthurLegal Memory (Beyin) | On your computer. | Claude, when a chat starts: only your preferences, corrections and last-session summary. |
| Land registry (TKGM) parcel lookups | Parcel identifier and data in the server's memory for up to 24 hours; never written to disk or logs. | TKGM Parcel Query, from the server. |
| The desk's language and theme | On your device. | Nobody. |

## Your Claude setting

ArthurLegal works with your own Claude account and can neither see nor change its settings. If you use Claude on a
**Free, Pro or Max** plan, your new chats may be used to improve Anthropic's models while the model improvement
setting under **Settings › Privacy** is on. Check this setting before entering client information, and run client
documents through ArthurMask. Team, Enterprise and API use fall under Anthropic's commercial terms. Source:
[Anthropic, model improvement privacy setting](https://privacy.claude.com/en/articles/12109829-how-do-i-change-my-model-improvement-privacy-settings).

## About the output

- ArthurLegal's and Claude's output is **not legal advice**.
- The output **may be wrong or incomplete**.
- **The lawyer checks it against the official source before using it**; professional responsibility stays with the lawyer.

The desk's citation check shows that the article number and heading exist in the official text. Whether the article
really says what the sentence attributes to it (who holds the right, conditions, time limits, consequences) is for the
lawyer to read; the desk's "Show text" button opens the sentence and the official text side by side. When a source
returns no data, ArthurLegal does not fill the gap; it writes this line: `UYARI: veri çekilemedi, teyidiniz gerekli: <link>`
("warning: the data could not be retrieved, please verify").

## If you want to check

- The remote server's detailed privacy policy: [arthurlegal-mcp/PRIVACY.md](https://github.com/beerbottle90/arthurlegal-mcp/blob/master/PRIVACY.md)
- How ArthurMask works: [arthur-mask](https://github.com/beerbottle90/arthur-mask)
- This repository: all the code of the installer and the desk.

This page is reviewed with every release; its history is in the repository.
