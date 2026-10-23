# BookByte publishing runbook

Scheduled runs follow this file to publish one guide per scheduled day. Rogenie Cordero chose fully automatic publishing: nothing waits for review, so every run must pass the checks below before anything goes live.

## Each run

1. Get today's date in America/Los_Angeles.
2. Open `_src/calendar.json` and list every item whose `date` is today **or earlier** and whose status is `written` or `todo`. These are due. Items marked `published` are done; items marked `held` wait for Rogenie. Skip both.
   - Nothing due: stop. Make no commits and send no message.
3. Work through the due items oldest first, one at a time, running the full process below (fact check, Publish, run log) for each before starting the next. An earlier date means a scheduled run was missed; catch it up now. In its run record, say in `note` that it was a catch-up and on what date.
4. If the status is `written`, the article is already in `_src/articles.py` with its scheduled date. Go to "Publish".
5. If the status is `todo`, write the article (below), pass the fact check, and add it to the end of the `ARTICLES` list in `_src/articles.py` using the `article(...)` helper, with `published` set to the item's scheduled date (the build only publishes dates that have arrived). Then go to "Publish".

Never publish an item dated in the future.

## Fetching sources and pages

Scheduled runs have nobody to approve a web fetch, and fetching a URL that didn't come from a search result is refused there. So: find each official page with a web search first (limit it to the official domain, for example `irs.gov` or `ftb.ca.gov`), then fetch the URL the search returned. Do the same for the live-page check: search `site:bookbytellc.com <title>` or fetch the URL only after a search has returned it; if that still fails, use the GitHub Pages run status as the live check and set `live_verified` to false.

## If the run can't finish

If anything stops the run before a due guide is live (a fetch or push is refused, the build fails, a tool is missing), send a push notification right away naming the guide, its date and what failed. Don't stop silently: the next run will retry any guide still due.

## Writing standards

- **Audience:** self-employed people and small-business owners anywhere in the US. Add a state note (`<div class="callout"><b>State note.</b> …</div>`) where a state's rules differ. California is the usual example.
- **AI articles** (most of the calendar): show the exact prompt in a callout, a sample run on made-up data labeled "Example (made-up data)", and how to check the output. Teach methods that work in any AI tool. Name a product only in comparison articles, check its features on the vendor's own pages that day, and date the article.
- **Accounting substance:** every AI tip must rest on a correct bookkeeping or tax rule. AI never replaces reconciling, keeping receipts, or the taxpayer's responsibility for their return.
- **Length:** 700–1,300 words. Short sentences and plain words. Use numbered steps where the reader follows along.
- **Byline:** articles are credited "By: Computatio" (set in the `article()` helper). Never put Rogenie's name on an article; it appears only on the About page, as founder.
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
4. If the article can't stand without an unconfirmed item, don't publish. Set the item's status to `held`, add a `note` explaining why, add a run record with `"result": "held"` and the reason (see "Run log"), run `python3 _src/build.py`, commit and push only those changes (`_src/calendar.json`, `_src/runs.json`, `status.json`), and report "HELD" with the reason.
5. Re-read the finished HTML once against the "Never" list above.

## Publish

1. From the repo root, run `python3 _src/build.py`. Today's guide must appear in the output count.
2. Set the calendar item's status to `published` and add `"url": "https://bookbytellc.com<path>"`.
3. Commit with author `Rogenie Cordero <rogenie@gmail.com>` and the message `Publish: <title>`, then push to `main`.
4. Verify: wait for the latest "pages build and deployment" run to show `completed` / `success` (GitHub connector, `actions_list` → `list_workflow_runs`, owner `rogenie`; the repo was renamed from `bookbyte` to `bookbyte-site`, so try whichever name the session allows). Then fetch the live page once, as described under "Fetching sources and pages", to confirm the title appears.
5. Write a LinkedIn post for the Computatio company page and save it as `_src/social/linkedin/<date>-<slug>.md` in the same commit (or a follow-up commit). Rules: 120–200 words, a first line that names a specific problem, 3 short takeaways from the guide, then the link `https://bookbytellc.com<path>?utm_source=linkedin&utm_medium=social&utm_campaign=<slug>`. Keep the same "Never" rules. No hashtag walls (3 at most). Write in first person plural ("we") as Computatio. Keep exactly one link in the post so LinkedIn shows a link preview.
5a. Auto-post it to LinkedIn through Metricool. Rogenie approved this as a standing workflow on 2026-10-23: post without waiting for review, but only after step 4 shows the Pages deploy succeeded.
   1. Load the Metricool connector's tools (search for "metricool"). Call getBrandSettings and use the brand labeled `computatio_` (id 6431543). Post only if its `linkedinData` is a company page (`urn:li:organization:...`). As of 2026-10-23 it is Rogenie's personal profile (`urn:li:person:...`), and she chose to wait for the company page rather than post there. While it is still a personal profile, don't post, set `linkedin_scheduled` to false with the note "Computatio LinkedIn page not connected in Metricool", and don't send a push notification for this alone. Once a company page appears, post every published guide not yet posted, as described in item 5.
   2. Call getScheduledPosts and check that no post already contains this guide's URL. Never post the same guide twice.
   3. Call createScheduledPost for that LinkedIn account only, with the exact text of the saved post file, a publish time about 15 minutes from now in America/Los_Angeles, and "show link preview" turned on if the tool offers it. No images.
   4. Call getScheduledPosts again and confirm the post is listed. Record the result as `linkedin_scheduled` in the run record.
   5. If the connector isn't available, refuses, or the post isn't listed, the guide stays live: send a push notification naming the guide and what failed, set `linkedin_scheduled` to false, and carry on. The next run posts any published guide that's still missing from Metricool (oldest first, at most 2 per run, spaced at least 2 hours apart).
6. Save a review copy to Google Drive. Run `python3 _src/export_docx.py <date>` (needs `pandoc`; if it's missing, `apt-get install -y pandoc` or `pip install --break-system-packages pypandoc_binary`). Upload the `.docx` it prints with the Google Drive connector's create_file tool. Use parentId `1FeqmZTfDW38R1wsP5hH6fDqaMdITYqjr` (folder "BookByte Articles"), the file name as title, contentMimeType `application/vnd.openxmlformats-officedocument.wordprocessingml.document`, `disableConversionToGoogleType: true`, and the contents of `/tmp/bookbyte_drive/<date>.b64` as the base64 content. Never let Drive convert it to a Google Doc: conversion deletes dollar amounts. If the Drive connector isn't available in this run, say so in the summary and continue; the article is still live.
7. Add a run record (see "Run log"), run `python3 _src/build.py` again so `status.json` includes it, then commit with the message `Run log: <date>` and push.
8. Finish with a short summary: the title, the live URL, the facts that were checked, anything removed for lack of a source, whether the Drive copy was saved, whether the LinkedIn post was scheduled in Metricool (and for when), and the full LinkedIn post text.

## Run log

Every run that reaches "Publish" or holds an item appends one record to the JSON list in `_src/runs.json`. The SEO scorecard at rogeniecordero.com/computatio reads it to show whether each scheduled guide went out. Never edit or delete earlier records.

```json
{"date": "YYYY-MM-DD", "at": "<ISO time with Pacific offset, when you finished>", "result": "published" | "held",
 "path": "<the item's path>", "facts_checked": <number of facts confirmed>, "removed": <number removed for lack of a source>,
 "live_verified": true | false, "linkedin_post": true | false, "linkedin_scheduled": true | false, "drive_copy": true | false, "note": "<one line: hold reason, or anything that failed>"}
```

`live_verified` is true only if the live page showed the title in step 4. `linkedin_scheduled` is true only if step 5a confirmed the post in Metricool. `drive_copy` is true only if the Drive upload in step 6 succeeded. If a step failed but the guide is live, keep `result` as `published` and say what failed in `note`.

## Newsletter

Every guide already carries the free "47 write-offs" download box through the `article()` helper. Don't add another newsletter link to the body.
