#!/usr/bin/env python3
"""Builds the static BookByte site from _src/pages.py into the repo root.
Run from the repo root:  python3 _src/build.py
Jekyll ignores folders starting with "_", so _src is not published."""
import os, json, html, datetime, sys
sys.path.insert(0, os.path.dirname(__file__))
from pages import SITE, PAGES
from articles import ARTICLES
import re
from zoneinfo import ZoneInfo

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = os.environ.get("BOOKBYTE_TODAY") or datetime.datetime.now(ZoneInfo("America/Los_Angeles")).date().isoformat()

def esc(s): return html.escape(s, quote=True)

SPARK = '<svg class="spark" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l2.2 6.3L20.5 10.5l-6.3 2.2L12 19l-2.2-6.3L3.5 10.5l6.3-2.2zM19 15l.9 2.1L22 18l-2.1.9L19 21l-.9-2.1L16 18l2.1-.9z" fill="currentColor"/></svg>'

def layout(p):
    url = SITE["url"] + p["path"]
    crumbs = [{"@type":"ListItem","position":1,"name":"Home","item":SITE["url"]+"/"}]
    if p.get("hub"):
        crumbs.append({"@type":"ListItem","position":2,"name":p["hub_name"],"item":SITE["url"]+p["hub"]})
    if p["path"] != "/":
        crumbs.append({"@type":"ListItem","position":len(crumbs)+1,"name":p["h1"],"item":url})
    ld = [{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":crumbs}]
    if p["path"] == "/":
        ld.append({"@context":"https://schema.org","@type":"WebSite","name":SITE["name"],"url":SITE["url"]+"/","description":SITE["desc"]})
    if p.get("article"):
        ld.append({"@context":"https://schema.org","@type":"Article","headline":p["h1"],"description":p["desc"],
                   "author":{"@type":"Organization","name":SITE["author"],"url":"https://computatio.io/"},"publisher":{"@type":"Organization","name":SITE["name"]},
                   "datePublished":p["published"],"dateModified":p.get("reviewed",p["published"]),"mainEntityOfPage":url})
    nav = "".join(f'<a href="{h}"{" aria-current=\"page\"" if p["path"].startswith(h) else ""}>{esc(n)}</a>' for h,n in SITE["nav"])
    robots = '<meta name="robots" content="noindex">' if p.get("noindex") else ""
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(p["title"])}</title>
<meta name="description" content="{esc(p["desc"])}">
<link rel="canonical" href="{url}">
{robots}
<meta property="og:type" content="{"article" if p.get("article") else "website"}">
<meta property="og:site_name" content="{SITE["name"]}">
<meta property="og:title" content="{esc(p["title"])}">
<meta property="og:description" content="{esc(p["desc"])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE["url"]}{p.get("og_image", "/assets/og/default.png")}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{esc(html.unescape(re.sub(r"<[^>]+>", "", p["h1"])))}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(p["title"])}">
<meta name="twitter:description" content="{esc(p["desc"])}">
<meta name="twitter:image" content="{SITE["url"]}{p.get("og_image", "/assets/og/default.png")}">
<meta name="theme-color" content="#111111">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/assets/fonts.css">
<link rel="stylesheet" href="/assets/style.css">
<link rel="alternate" type="application/rss+xml" title="BookByte" href="/feed.xml">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site"><div class="wrap bar">
<a class="brand" href="/"><img src="/assets/favicon.svg" alt="" width="32" height="32"><span>BookByte</span></a>
<nav aria-label="Main">{nav}<a class="ai-btn{" on" if p["path"].startswith(SITE["ai"][0]) else ""}" href="{SITE["ai"][0]}">{SPARK}{esc(SITE["ai"][1])}</a></nav>
</div></header>
<main id="main">
{p["body"]}
</main>
<footer class="site"><div class="wrap">
<div class="fgrid">
<div><b>BookByte</b><p>Plain-English bookkeeping, tax and AI accounting guides for the self-employed.</p><a href="{SITE["newsletter"]}?utm_source=bookbyte&amp;utm_medium=referral&amp;utm_campaign=footer">Free guide: 47 write-offs</a><a href="/feed.xml">RSS feed</a></div>
<div><b>Guides</b><a href="{SITE["ai"][0]}">{esc(SITE["ai"][1])}</a>{"".join(f'<a href="{h}">{esc(n)}</a>' for h,n in SITE["nav"][:4])}</div>
<div><b>Would rather not do it yourself?</b><p><a href="{SITE["cta_url"]}utm_source=bookbyte&amp;utm_medium=referral&amp;utm_campaign=footer">Computatio</a> keeps your books and prepares your return, with a person reviewing every account.</p></div>
</div>
<p class="legal">Guides are general information, not financial, tax or legal advice. We can make mistakes and rules change; check the date and sources on each guide. &middot; <a href="/about/">About</a> &middot; <a href="/privacy/">Privacy</a> &middot; &copy; {datetime.date.today().year} BookByte</p>
</div></footer>
<script>window.goatcounter={{path:function(p){{return location.host+p}}}}</script>
<script data-goatcounter="https://computatio.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>
</body>
</html>
'''

def card_list(arts):
    return '<div class="cards">' + "".join(
        f'<a class="card" href="{a["path"]}"><h3>{a["h1"]}</h3><p>{a["desc"]}</p></a>' for a in arts) + '</div>'

def main():
    live = sorted([a for a in ARTICLES if a["published"] <= TODAY], key=lambda a: a["published"], reverse=True)
    live_paths = {a["path"] for a in live}
    all_paths = {a["path"] for a in ARTICLES}
    # planned calendar guides that aren't live yet are unlinked too (see PUBLISHING.md "Links")
    import json as _json
    all_paths |= {i["path"] for i in _json.load(open(os.path.join(ROOT, "_src", "calendar.json"), encoding="utf-8"))["items"]}
    def unlink_future(body):
        # turn links to not-yet-published guides into plain text
        def f(m):
            return m.group(2) if (m.group(1) in all_paths and m.group(1) not in live_paths) else m.group(0)
        return re.sub(r'<a href="(/[^"]+)">(.*?)</a>', f, body)
    pages = []
    for p in PAGES:
        p = dict(p)
        if "<!--HUB_ARTICLES-->" in p["body"]:
            mine = [a for a in live if a["hub"] == p["path"]]
            p["body"] = p["body"].replace("<!--HUB_ARTICLES-->", ("<h2>Guides</h2>" + card_list(mine)) if mine else "")
        if "<!--LATEST-->" in p["body"]:
            p["body"] = p["body"].replace("<!--LATEST-->", ('<section><div class="wrap"><h2>Latest guides</h2>' + card_list(live[:6]) + '</div></section>') if live else "")
        pages.append(p)
    # share images: one per live guide, plus a site default (see og.py)
    from og import make_card
    og_dir = os.path.join(ROOT, "assets", "og")
    make_card(os.path.join(og_dir, "default.png"), "Plain-English bookkeeping and tax guides for the self-employed")
    # section and info pages get their own card too (the home page keeps the default)
    for p in pages:
        if p["path"] not in ("/", "/404") and not p.get("noindex"):
            img = "page-" + p["path"].strip("/").replace("/", "-") + ".png"
            if make_card(os.path.join(og_dir, img), p["h1"], "Guides" if p["path"] in {h for h, _ in SITE["nav"]} | {SITE["ai"][0]} and p["path"] != "/about/" else "") or os.path.exists(os.path.join(og_dir, img)):
                p["og_image"] = "/assets/og/" + img
    for a in live:
        a = dict(a); a["body"] = unlink_future(a["body"])
        img = a["path"].strip("/").split("/")[-1] + ".png"
        if make_card(os.path.join(og_dir, img), a["h1"], a["hub_name"]) or os.path.exists(os.path.join(og_dir, img)):
            a["og_image"] = "/assets/og/" + img
        pages.append(a)
    # remove pages for articles that are not live (e.g. date moved later)
    for a in ARTICLES:
        if a["path"] not in live_paths:
            f = os.path.join(ROOT, a["path"].strip("/"), "index.html")
            if os.path.exists(f): os.remove(f)
    urls=[]
    for p in pages:
        out = os.path.join(ROOT, p["path"].strip("/"), "index.html") if p["path"]!="/404" else os.path.join(ROOT,"404.html")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out,"w",encoding="utf-8").write(layout(p))
        if not p.get("noindex"): urls.append((SITE["url"]+p["path"], p.get("reviewed",TODAY)))
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + \
         "".join(f"  <url><loc>{u}</loc><lastmod>{d}</lastmod></url>\n" for u,d in urls) + "</urlset>\n"
    open(os.path.join(ROOT,"sitemap.xml"),"w").write(sm)
    items = "".join(
        f"<item><title>{esc(html.unescape(a['h1']))}</title><link>{SITE['url']}{a['path']}</link><guid>{SITE['url']}{a['path']}</guid>"
        f"<pubDate>{datetime.datetime.fromisoformat(a['published']).strftime('%a, %d %b %Y 06:00:00 -0800')}</pubDate>"
        f"<description>{esc(html.unescape(a['desc']))}</description></item>" for a in live[:30])
    open(os.path.join(ROOT,"feed.xml"),"w",encoding="utf-8").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0"><channel>'
        f"<title>BookByte</title><link>{SITE['url']}/</link><description>{esc(SITE['desc'])}</description><language>en-us</language>"
        + items + "</channel></rss>\n")
    open(os.path.join(ROOT,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE['url']}/sitemap.xml\n")
    # status.json: read by the Computatio SEO dashboard (rogeniecordero.com/computatio).
    # Future guides list date, topic and writing status only; titles appear once live.
    import json
    cal = json.load(open(os.path.join(ROOT, "_src", "calendar.json"), encoding="utf-8"))
    written = {a["path"] for a in ARTICLES}
    items = []
    for i in cal["items"]:
        st = "held" if i.get("status") == "held" else ("written" if i["path"] in written or i.get("status") in ("written", "published") else "todo")
        row = {"date": i["date"], "hub": i["hub"], "status": st}
        if i["path"] in live_paths:
            row.update(title=html.unescape(re.sub(r"<[^>]+>", "", i["title"])), url=SITE["url"] + i["path"])
        items.append(row)
    runs_path = os.path.join(ROOT, "_src", "runs.json")
    runs = json.load(open(runs_path, encoding="utf-8")) if os.path.exists(runs_path) else []
    json.dump({"built": TODAY, "cadence": cal.get("cadence"), "items": items, "runs": runs},
              open(os.path.join(ROOT, "status.json"), "w", encoding="utf-8"), indent=1)
    print("built", len(pages), "pages;", len(live), "live guides; today", TODAY)
if __name__=="__main__": main()
