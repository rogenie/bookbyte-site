#!/usr/bin/env python3
"""Builds the static BookByte site from _src/pages.py into the repo root.
Run from the repo root:  python3 _src/build.py
Jekyll ignores folders starting with "_", so _src is not published."""
import os, json, html, datetime, sys
sys.path.insert(0, os.path.dirname(__file__))
from pages import SITE, PAGES

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = datetime.date.today().isoformat()

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
                   "author":{"@type":"Person","name":SITE["author"],"url":SITE["url"]+"/about/","sameAs":["https://www.linkedin.com/in/rogenie"]},"publisher":{"@type":"Organization","name":SITE["name"]},
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
<meta name="theme-color" content="#111111">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,600;8..60,700&family=Inter:wght@400;500;600&display=swap">
<link rel="stylesheet" href="/assets/style.css">
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
<div><b>BookByte</b><p>Plain-English bookkeeping, tax and AI accounting guides for the self-employed.</p></div>
<div><b>Guides</b><a href="{SITE["ai"][0]}">{esc(SITE["ai"][1])}</a>{"".join(f'<a href="{h}">{esc(n)}</a>' for h,n in SITE["nav"][:4])}</div>
<div><b>Would rather not do it yourself?</b><p><a href="{SITE["cta_url"]}utm_source=bookbyte&amp;utm_medium=referral&amp;utm_campaign=footer">Computatio</a> keeps your books and prepares your return, with a person reviewing every account.</p></div>
</div>
<p class="legal">Guides are general information, not tax or legal advice. Rules change; check the date on each guide. &middot; <a href="/about/">About</a> &middot; <a href="/privacy/">Privacy</a> &middot; &copy; {datetime.date.today().year} BookByte</p>
</div></footer>
</body>
</html>
'''

def main():
    urls=[]
    for p in PAGES:
        out = os.path.join(ROOT, p["path"].strip("/"), "index.html") if p["path"]!="/404" else os.path.join(ROOT,"404.html")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out,"w",encoding="utf-8").write(layout(p))
        if not p.get("noindex"): urls.append((SITE["url"]+p["path"], p.get("reviewed",TODAY)))
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + \
         "".join(f"  <url><loc>{u}</loc><lastmod>{d}</lastmod></url>\n" for u,d in urls) + "</urlset>\n"
    open(os.path.join(ROOT,"sitemap.xml"),"w").write(sm)
    open(os.path.join(ROOT,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE['url']}/sitemap.xml\n")
    print("built", len(PAGES), "pages")
if __name__=="__main__": main()
