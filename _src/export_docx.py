"""Export one BookByte article (and its LinkedIn post, if saved) to a Word file for the
Google Drive "BookByte Articles" review folder.

Usage (from the repo root):  python3 _src/export_docx.py <published-date YYYY-MM-DD>
Writes to /tmp/bookbyte_drive/:  "<date> <title>.docx"  and  "<date>.b64" (base64 of the .docx).

Why Word, not a Google Doc: Drive's HTML-to-Doc conversion drops text between "$" signs,
which deletes dollar amounts. Upload the .docx with conversion turned off.
"""
import base64, glob, html, os, re, subprocess, sys

sys.path.insert(0, os.path.dirname(__file__))
from articles import ARTICLES  # noqa: E402

SITE = "https://bookbytellc.com"
OUT = "/tmp/bookbyte_drive"


def clean_title(t):
    return html.unescape(re.sub(r"<[^>]+>", "", t)).replace("/", "-").strip()


def main(date):
    arts = [a for a in ARTICLES if a["published"] == date]
    if not arts:
        sys.exit(f"No article with published date {date}")
    os.makedirs(OUT, exist_ok=True)
    for a in arts:
        body = a["body"]
        # drop the hero wrapper and byline; keep the lede and the prose
        body = re.sub(r'<p class="eyebrow">.*?</p>', "", body, flags=re.S)
        body = re.sub(r"<h1>.*?</h1>", "", body, flags=re.S)
        body = re.sub(r'<p class="muted" style="color:#bbb">.*?</p>', "", body, flags=re.S)
        body = body.replace('href="/', f'href="{SITE}/')
        slug = a["path"].strip("/").split("/")[-1]
        post = ""
        for f in glob.glob(os.path.join(os.path.dirname(__file__), "social", "linkedin", f"{date}-*.md")):
            with open(f) as fh:
                post = "<hr><h2>LinkedIn post</h2>" + "".join(
                    f"<p>{html.escape(p)}</p>" for p in fh.read().split("\n\n") if p.strip())
        doc = f"""<html><body>
<h1>{a['h1']}</h1>
<p><b>Publish date:</b> {date} &middot; <b>Live URL:</b> {SITE}{a['path']}</p>
<p><b>Search title:</b> {a['title']}<br><b>Search description:</b> {a['desc']}</p>
<hr>
{body}
{post}
</body></html>"""
        name = f"{date} {clean_title(a['h1'])}"
        src = os.path.join(OUT, f"{date}.html")
        with open(src, "w") as fh:
            fh.write(doc)
        docx = os.path.join(OUT, f"{name}.docx")
        subprocess.run(["pandoc", src, "-f", "html", "-o", docx], check=True)
        with open(docx, "rb") as fh, open(os.path.join(OUT, f"{date}.b64"), "w") as out:
            out.write(base64.b64encode(fh.read()).decode())
        print(docx)


if __name__ == "__main__":
    main(sys.argv[1])
