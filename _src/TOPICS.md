# BookByte topic scout runbook

A weekly scheduled run (Sunday afternoon, Pacific) follows this file. It finds what changed in AI tools that week, keeps only what a self-employed person or small-business owner can use in their books, and turns the best items into "AI update" guides on the calendar. It also sends Rogenie a short digest so she learns what changed too.

The publisher (`_src/PUBLISHING.md`) writes and fact-checks each guide on its date. The scout only plans.

## Cadence it fills

- Mon/Wed/Fri: evergreen guides already on the calendar. The scout doesn't move or replace them.
- Tue/Thu: "AI update" guides chosen by the scout.
- Keep every Tue and Thu filled for the next 14 days. Add at most 3 items per run. If the evergreen queue has fewer than 2 weeks left, also fill the empty Mon/Wed/Fri slots with evergreen AI topics.

## Where to look (official sources only)

Search the last 10 days, one search per source, restricted to the domain:

| Source | Domain |
|---|---|
| OpenAI (ChatGPT) | openai.com, help.openai.com |
| Anthropic (Claude) | anthropic.com, support.claude.com |
| Google (Gemini, Sheets) | blog.google, workspace.google.com, support.google.com |
| Microsoft (Copilot, Excel) | microsoft.com, techcommunity.microsoft.com, support.microsoft.com |
| Intuit (QuickBooks) | quickbooks.intuit.com, intuit.com |
| Xero | xero.com, central.xero.com |
| IRS and FTC (AI scams, e-filing, digital records) | irs.gov, ftc.gov |

News sites can point you to a story, but only the vendor's or agency's own page counts as the source.

## Keep an item only if all are true

1. It shipped, or the vendor gives a date within 14 days. No rumors, benchmarks, funding news or "coming later this year".
2. It changes a real bookkeeping or tax task: categorizing, reconciling, receipts, invoices and reminders, reports, cash flow, estimated taxes, records, spreadsheets, or data safety.
3. It can be taught in 700–1,300 words with a prompt or click-path, a made-up example, and a way to check the result.
4. It doesn't repeat a published guide or a calendar item (read `_src/calendar.json` and `_src/articles.py` first). If it overlaps, make the new guide about what's new and link the older one.
5. A Computatio service fits it truthfully (Monthly Books, a tax return, or the free call).

Rank the keepers by how many readers it affects (common tools first: Excel, Google Sheets, ChatGPT, QuickBooks), then by how much time or error it removes. Prefer features available on free or low-cost plans.

## Calendar entry

Add to `_src/calendar.json` `items`, kept in date order:

```json
{"date": "YYYY-MM-DD", "hub": "ai-accounting", "path": "/ai-accounting/<slug>/", "title": "<under 60 characters>", "status": "todo",
 "kind": "ai-update",
 "brief": {"news": "<one line: what changed>", "source": "<official URL the search returned>", "source_date": "YYYY-MM-DD",
           "who": "<which plans or users get it>", "task": "<the bookkeeping task it changes>", "angle": "<what the guide teaches, incl. how to check the output>",
           "cta": "monthly-books | tax-return | call", "links": ["<2-3 BookByte paths to link>"]}}
```

Titles describe the task, not the hype ("QuickBooks AI banking suggestions: review before you post", not "QuickBooks AI changes everything").

## Commit and report

1. Run `python3 _src/build.py`, then commit only `_src/calendar.json` and `status.json` with author `Rogenie Cordero <rogenie@gmail.com>` and the message `Topics: <dates added>`, and push to `main`.
2. Send Rogenie one push notification (it is also emailed) titled "AI this week for your books". In it: the 3–5 most useful changes you found (kept or not), one line each on what it means for a small business's books, and which ones became guides and when. Plain words, no hype.
3. If nothing qualified, add nothing and say so in the digest. If a search or push fails, say which in the digest.

## Never

Follow the "Never" list in `_src/PUBLISHING.md`. Also: don't call a feature available before the vendor says it is, and don't call Computatio an accounting firm; say bookkeeping and tax.
