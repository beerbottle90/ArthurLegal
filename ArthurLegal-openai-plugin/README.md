# ArthurLegal plugin (ChatGPT)

ArthurLegal is a Turkish-law-first legal assistant for lawyers in Türkiye. This plugin brings its working rules,
112 law-firm workflows and 33 setup helpers to ChatGPT as 12 skills (one rule skill and 11 practice
areas), connected to ArthurLegal MCP at `https://arthurlegal-mcp.fly.dev/openai/mcp`.

**Status: in preparation.** This plugin is not yet published in the ChatGPT plugin directory and the ArthurLegal
installer has no ChatGPT option yet. It has been tested in the ChatGPT desktop app and is generated from the same
package as ArthurLegal's other plugin, so the two stay in step.

Version 1.12.8, generated from the ArthurLegal Law Firm package 1.12.6 by
`ArthurLegal-setup/yayin/openai_eklenti_uret.py`. Do not edit this folder by hand.

ChatGPT and OpenAI are trademarks of OpenAI.

## Skills

- `arthurlegal`: working rules, citation checks, the warning line for unreachable sources, the ArthurLegal desk.
- `arthurlegal-dava-ve-dilekce`: Litigation and pleadings
- `arthurlegal-idare-ve-duzenleyici-kurumlar`: Administrative and regulatory
- `arthurlegal-sozlesme`: Contracts
- `arthurlegal-sirketler-ve-birlesme`: Corporate and M&A
- `arthurlegal-is-hukuku`: Employment
- `arthurlegal-fikri-mulkiyet`: Intellectual property
- `arthurlegal-kisisel-veriler`: Personal data
- `arthurlegal-vergi`: Tax
- `arthurlegal-enerji-ve-proje-finansmani`: Energy and project finance
- `arthurlegal-buro-isleri`: Firm operations
- `arthurlegal-arastirma-ve-atif`: Research and citations

Each practice-area skill lists its workflows; the full steps are in that skill's `references/` folder.

## Notes

- Free and open source for lawyers in Türkiye; non-commercial use. See `LICENSE`.
- Land-registry tools that take coordinates, an address or a geometry file are not on this connection; parcels are
  found by province, district, neighbourhood, block and parcel.
- UYAP, ArthurMask and ArthurLegal Memory run only with the ArthurLegal desktop install.
- Outputs are drafts for review by a lawyer.
