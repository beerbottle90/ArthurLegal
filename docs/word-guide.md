# ArthurLegal in Word

[Türkçe](word-rehberi.md) · [Azərbaycan dili](word-beledcisi.md)

Anthropic's Word add-in opens Claude in a panel next to your document. When ArthurLegal's research connector is
connected to your claude.ai account, Claude in Word also pulls Turkish legislation and case law live from official
sources: it reads the article next to your document, proposes the fix as a tracked change and leaves the reasoning as a
comment. There is nothing extra to install or pay for; it runs on your Claude subscription.

## What you need

- **Claude plan:** Pro, Max, Team or Enterprise.
- **Word version:**
  - Word on the web (in the browser; a free Microsoft account is enough), or
  - Word on Windows with a Microsoft 365 subscription, Version 2205 (build 15202.10000) or later, or
  - Word on Mac, version 16.61 or later.
- **Not supported:** Word 2016 and 2019 (perpetual or volume licence), Word on iPad and Android, `.doc` files (save as
  `.docx` first). Perpetual Word 2021 and 2024 are not mentioned on the official page; if in doubt, use Word on the web.

If the Word on your computer is too old, the add-in simply does not appear in the store. That is not a search problem;
Word on the web works.

## Setup

1. **ArthurLegal connector:** on claude.ai, ArthurLegal must be connected under Settings › Connectors. If it is not,
   use **Add custom connector** with this address: `https://arthurlegal-mcp.fly.dev/mcp`
2. **Open Word:** open Word on the web (word.cloud.microsoft) or Microsoft 365 Word, and open a document.
3. **Add the add-in:** press **Home › Add-ins** (in some layouts **Insert › Add-ins**) and search for `Claude`. Its
   store name is **Claude for Microsoft 365** (publisher Anthropic); a search for "Claude for Word" may find nothing.
   Press **Add**. Store page: [Claude for Microsoft 365](https://marketplace.microsoft.com/en-us/product/office/WA200010725)
4. **Sign in:** in the Claude panel on the right, sign in with **your Claude account**. This is separate from your
   Microsoft account; use the account that holds your Claude subscription.

### If the add-in does not appear on a firm or company account

In some organisations an administrator has to allow add-ins. In the Microsoft 365 admin center:

- **Settings › Org settings › User owned apps and services**: "Let users access the Office Store" must be on, or
- **Settings › Integrated apps › Add-ins**: search for Claude for Microsoft 365 and assign it to the organisation,
  users or groups. An organisation-wide rollout can take up to 24 hours.

If the store is kept closed, Anthropic's Word page also provides an add-in file the administrator can upload (see the
sources below).

## Example uses

Select the relevant text first, then type in the panel.

- **Clause review:** "Review this clause under the Turkish Code of Obligations; pull the article you rely on from the
  official text with ArthurLegal." A **Used … tools** line appears above the answer, showing that Claude fetched the
  article with a tool rather than from memory. The article text should come with a mevzuat.gov.tr link.
- **Fix as a tracked change:** "Rewrite this clause so it complies with the law, apply the change as a tracked change
  and add the reasoning as a comment." You accept or reject changes in Word's own **Review** pane; undo with Ctrl+Z
  (Cmd+Z on Mac).
- **Work through comments:** "Work through the comments in order and apply each as a tracked change." Claude replies to
  each comment thread with what it did.
- **Counterparty changes:** "Summarise the counterparty's tracked changes; flag those that conflict with the law or
  work against the client."
- **Skills:** skills enabled in your Claude settings also work in Word. Type `/` in the panel to list them.

## Limits

- **Only the research connector comes along.** Claude in Word uses the connectors on your claude.ai account.
  ArthurMask, UYAP Dashboard, Beyin and the ArthurLegal Desk run on your computer and do not appear in Word.
- **Document content goes to Anthropic.** When you sign in with a Claude account, the conversation, the content Claude
  reads from the document (text, comments, tracked changes, footnotes, tables) and any files you attach are sent to
  Anthropic. ArthurMask does not sit in between here: for a document with client confidential or personal data, mask it
  first with ArthurMask and work on the masked document in Word. Details: [Where your data goes](your-data.md).
- **Retention.** According to Anthropic's Word page, inputs and outputs are deleted within 30 days, except in the cases
  listed on its privacy page. Your organisation's custom retention settings do not apply to this add-in. Chat history
  stays only in that browser (the 50 most recent conversations per app). The add-in writes its own identifier into the
  document; it travels with the document when shared.
- **The final check is the lawyer's.** Anthropic also recommends using the add-in only with trusted documents and having
  a human review the final text before it goes to a client or counterparty. ArthurLegal does not give legal advice; it
  speeds up your work with the sources it finds.

## Sources

- Anthropic, Claude for Word: https://claude.com/docs/office-agents/word
- Anthropic, Connectors and skills: https://claude.com/docs/office-agents/connectors-and-skills
- Anthropic, Data storage: https://claude.com/docs/office-agents/data-storage
- Microsoft Marketplace, Claude for Microsoft 365: https://marketplace.microsoft.com/en-us/product/office/WA200010725

Official pages can change; if a version requirement is unclear, check Anthropic's Word page first.

---

Microsoft, Word and Microsoft 365 are trademarks of the Microsoft group of companies. Claude is a trademark of
Anthropic. ArthurLegal is not affiliated with these companies; the names are used only to state compatibility.
