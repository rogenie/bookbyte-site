# Social share images (1200x630) for link previews on LinkedIn, X, Facebook, Slack, etc.
# build.py calls make_card() for every live article and the site default.
# Fonts are vendored in _src/fonts so every run renders identical images.
import os, html, re

W, H = 1200, 630
INK, GOLD, SOFT, MUTED = (17, 17, 17), (184, 134, 11), (246, 243, 236), (170, 164, 150)
HERE = os.path.dirname(os.path.abspath(__file__))
SERIF = os.path.join(HERE, "fonts", "Lora-Variable.ttf")
SANS = os.path.join(HERE, "fonts", "Inter-SemiBold.otf")


def _serif(size):
    from PIL import ImageFont
    f = ImageFont.truetype(SERIF, size)
    f.set_variation_by_name("Bold")
    return f


def _wrap(draw, text, font, width):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= width:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def make_card(out, title, eyebrow="", footer="By: Computatio  ·  bookbytellc.com"):
    """Render one card to `out` (PNG). Returns True if written, False if Pillow is missing."""
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        return False
    title = html.unescape(re.sub(r"<[^>]+>", "", title))
    img = Image.new("RGB", (W, H), INK)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 18, H], fill=GOLD)                       # gold edge
    x, maxw = 90, W - 180
    sans = ImageFont.truetype(SANS, 30)
    d.text((x, 70), "BookByte", font=sans, fill=SOFT)
    if eyebrow:
        d.text((x + d.textlength("BookByte", font=sans) + 24, 70), "/  " + eyebrow.upper(), font=sans, fill=GOLD)
    # largest title size that fits in 4 lines
    for size in (78, 70, 62, 56, 50, 44):
        f = _serif(size)
        lines = _wrap(d, title, f, maxw)
        lh = int(size * 1.2)
        if len(lines) <= 4 and lh * len(lines) <= 320:
            break
    block = lh * len(lines)
    y = 150 + (330 - block) // 2
    for ln in lines:
        d.text((x, y), ln, font=f, fill=(255, 255, 255))
        y += lh
    d.line([x, H - 120, x + 120, H - 120], fill=GOLD, width=4)
    d.text((x, H - 95), footer, font=ImageFont.truetype(SANS, 28), fill=MUTED)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    img.save(out, "PNG", optimize=True)
    return True
