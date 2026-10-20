# BookByte publishing runbook

Scheduled runs follow this file to publish one guide per scheduled day. Rogenie Cordero chose fully automatic publishing: nothing waits for review, so every run must pass the checks below before anything goes live.

## Each run

1. Get today's date in America/Los_Angeles.
2. Open `_src/calendar.json` and find the item whose `date` is today.
   - No item for today: stop. Make no commits and send no message.
   - Status `published`: stop. It is already done.
   - Status `held`: stop. It is waiting for Rogenie.
3. If the status is `written`, the article is already in `_src/articles.py` with today's date. Go to "Publish".
4. If the status is `todo`, write the article (below), pass the fact check, and add it to the end of the `ARTICLES` list in `_src/articles.py` using the `article(...)` helper, with `published` set to today. Then go to "Publish".

Never publish an item dated in the future, and never skip ahead to the next item.

## Writing standards

- **Audience:** self-employed people and small-business owners anywhere in the US. Add a state note (`<div class="callout"><b>State note.</b> …</div>`) where a state's rules differ. California is the usual example.
- **AI articles** (most of the calendar): show the exact prompt in a callout, a sample run on made-up data labeled "Example (made-up data)", and how to check the output. Teach methods that work in any AI tool. Name a product only in comparison articles, check its features on the vendor's own pages that day, and date the article.
- **Accounting substance:** every AI tip must rest on a correct bookkeeping or tax rule. AI never replaces reconciling, keeping receipts, or the taxpayer's responsibility for their return.
- **Length:** 700–1,300 words. Short sentences and plain words. Use numbered steps where the reader follows along.
- **Title:** under 60 characters. **Description:** under 155 characters.
- **Links:** at least 3 links to BookByte guides or hubs. The build turns links to unpublished guides into plain text, so link freely to planned paths in the calendar.
- **Call to action:** pass exactly one `cta_html` with `CTAURL` where the link goes. Match it to the topic:
  - bookkeeping and AI workflow: Computatio Monthly Books, $500 a month; AI does the work and a person reviews every account
  - tax returns: Simple Return $350, Self-Employed Return $600
  - business structure or complex situations: a free 20-minute call with Computatio
- **Sources:** 2–5 official sources (irs.gov, state tax agencies, ssa.gov) as `(title, url)` pairs. Use a non-government source only when no official page exists.

## Never

- Use "CPA" in any form, or call Rogenie or Computatio an accountant or accounting firm.
- Use "PTIN preparer" or "licensed preparer".
- Describe Computatio's services as "accounting". Say bookkeeping and tax.
- Promise refunds, savings, rankings or results.
- Invent clients, results, testimonials, quotes or statistics.
- Copy text from sources. Paraphrase everything, and quote nothing longer than a few words.

## Fact check (required before publishing)

1. List every rate, dollar threshold, percentage, deadline, form number and rule the article states.
2. Confirm each one on an official source fetched during this run. Confirm the tax year, not just the number.
3. If an item can't be confirmed, remove it or rewrite the sentence without it.
4. If the article can't stand without an unconfirmed item, don't publish. Set the item's status to `held`, add a `note` explaining why, commit and push only that calendar change, and report "HELD" with the reason.
5. Re-read the finished HTML once against the "Never" list above.

## Publish

1. From the repo root, run `python3 _src/build.py`. Today's guide must appear in the output count.
2. Set the calendar item's status to `published` and add `"url": "https://bookbytellc.com<path>"`.
3. Commit with author `Rogenie Cordero <rogenie@gmail.com>` and the message `Publish: <title>`, then push to `main`.
4. Verify: wait for the latest GitHub Pages run to show `completed` / `success` using `https://api.github.com/repos/rogenie/bookbyte-site/actions/runs?per_page=1`, then fetch the live page once to confirm the title appears.
5. Write a LinkedIn post for the Computatio company page and save it as `_src/social/linkedin/<date>-<slug>.md` in the same commit (or a follow-up commit). Rules: 120–200 words, a first line that names a specific problem, 3 short takeaways from the guide, then the link `https://bookbytellc.com<path>?utm_source=linkedin&utm_medium=social&utm_campaign=<slug>`. Keep the same "Never" rules. No hashtag walls (3 at most). Write in first person plural ("we") as Computatio.
6. Finish with a short summary: the title, the live URL, the facts that were checked, anything removed for lack of a source, and the full LinkedIn post text.

## Newsletter

Every guide already carries the free "47 write-offs" download box through the `article()` helper. Don't add another newsletter link to the body.
