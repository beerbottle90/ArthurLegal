# ArthurLegal for Claude

ArthurLegal is a Turkish-law-first legal assistant for law firms. This plugin brings its working rules and
142 practice skills to Claude: contracts and NDAs, corporate and M&A, employment, KVKK and privacy,
regulatory, intellectual property, litigation and petitions, tax, administrative law, criminal defense, energy and
finance, expert opinions, contract drafting and law firm operations. Statutes and decisions are quoted from the official
text through ArthurLegal MCP, which covers fifteen jurisdictions from Türkiye and the EU to the UK, Germany and Japan.

Plugin version 1.12.5 is the ArthurLegal Law Firm package 1.12.5. Source: [https://github.com/beerbottle90/ArthurLegal](https://github.com/beerbottle90/ArthurLegal).

## What it contains

- **`/arthurlegal:arthurlegal`**: the working rules: output format, citation and statute-verification gates, and the `UYARI` line
  that replaces any fact a live source could not return. Claude loads it before any legal task.
- **142 practice skills**, called as `/arthurlegal:<area>-<skill>`, for example
  `/arthurlegal:commercial-legal-nda-review` or `/arthurlegal:tax-legal-gib-ozelge-request`. Areas: `administrative-legal`, `advocacy-legal`, `commercial-legal`, `contract-drafting`, `corporate-legal`, `criminal-defense`, `employment-legal`, `energy-finance`, `expert-opinion`, `firm-operations`, `ip-legal`, `legal-research`, `litigation-legal`, `privacy-legal`, `regulatory-legal`, `tax-legal`.
- **`references/`**: 104 guides, practice profiles and a firm profile template that the skills read.
- **One connector: ArthurLegal MCP** (`https://arthurlegal-mcp.fly.dev/directory/mcp`), read-only legal research with no account.

## What it runs and sends

The plugin contains no scripts, hooks or programs; it is Markdown, one image and one connector declaration. Its only
network connection is ArthurLegal MCP: when Claude calls one of its tools, the tool name and its arguments (search words,
statute and article numbers, decision identifiers) go to that server, which queries the official sources and returns
the result. Interactive views (article card, decision list, the ArthurLegal desk) load the MCP Apps client library from
unpkg.com. What the server stores and for how long is in its [privacy policy](https://github.com/beerbottle90/arthurlegal-mcp/blob/master/PRIVACY.md). Do not put client names or
other confidential facts into requests; mask documents on your own computer first with Arthur Mask.

Some skills also ask Claude to use tools the user already has, through Claude and with the user's own permissions; the
plugin installs none of them and sends nothing to them by itself:

- **Claude's web search and web fetch**, for official public sources such as EUR-Lex, legislation.gov.uk, HUDOC, KAP
  and GovInfo (search words and document identifiers).
- **Connectors the user has added**, when they are connected: CourtListener and TR Legal MCP for case law; document
  stores such as Google Drive, Box or iManage; Slack for posting a report the user asked for; DocuSign for sending a
  document for signature after the user approves it.
- **The local ArthurLegal modules** described below (`arthur-tapu`, `arthur-uyap`, Arthur Mask), which run on the
  user's computer.

## Desktop modules (not part of this plugin)

ArthurTapu (land registry), UYAP Dashboard (a read-only bridge to the lawyer's own UYAP account), Arthur Mask and
ArthurLegal Hafıza run on the lawyer's computer and come with the ArthurLegal installer ([download](https://github.com/beerbottle90/ArthurLegal#download)).
When they are installed, the `arthurlegal` skill sends land-registry work to `arthur-tapu` and UYAP work to `arthur-uyap`;
when they are not, it says the data could not be retrieved instead of guessing.

## A lawyer stays in charge

Every output is a draft for review by a qualified lawyer and is marked as such. ArthurLegal does not give legal advice,
does not file anything and does not write to UYAP.

## License and support

[LICENSE](LICENSE) (ArthurLegal Proprietary Non-Commercial License). Parts derived from Anthropic's claude-for-legal
are under Apache 2.0: [LICENSE-APACHE-2.0-THIRD-PARTY.txt](LICENSE-APACHE-2.0-THIRD-PARTY.txt),
[ATTRIBUTION.md](ATTRIBUTION.md). Support: [GitHub issues](https://github.com/beerbottle90/ArthurLegal/issues) or ertug@datsproject.io.

## Türkçe

ArthurLegal, Türk hukuku odaklı hukuk bürosu asistanıdır. Bu eklenti çalışma kurallarını ve 142 beceriyi
Claude'a ekler; mevzuat ve kararlar ArthurLegal MCP üzerinden resmî metinden alıntılanır. Tapu, UYAP Dashboard, Arthur
Mask ve ArthurLegal Hafıza bilgisayarınızdaki ArthurLegal kurulumuyla gelir ([indir](https://github.com/beerbottle90/ArthurLegal#indir)); kuruluysa eklenti
onlara yönlendirir. Çıktılar avukat incelemesi öncesi taslaktır.
