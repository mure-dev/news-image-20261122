#!/usr/bin/env python3
"""Render the news poster for Sunday 22 November 2026.

Draws a 1024x1024 newspaper-style front page with six verified stories
from the day, using Pillow. Run: python3 draw_poster.py  ->  entry.png
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (250, 247, 240)
INK = (20, 20, 20)
MUTED = (90, 88, 84)
NAVY = (15, 42, 74)
GOLD = (198, 158, 62)
RED = (179, 38, 30)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(f"{FONT_DIR}/{name}", size)


F_SERIF = lambda s: font("DejaVuSerif-Bold.ttf", s)      # noqa: E731
F_SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)      # noqa: E731
F_SANS = lambda s: font("DejaVuSans.ttf", s)             # noqa: E731


def wrap(draw, text, fnt, width):
    """Greedy word wrap returning a list of lines fitting `width` px."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_block(draw, x, y, w, h, story):
    accent, kicker, headline, body = story
    # card background + top accent rule
    draw.rectangle([x, y, x + w, y + h], fill=(255, 255, 255),
                   outline=(210, 206, 198), width=2)
    draw.rectangle([x, y, x + w, y + 8], fill=accent)
    tx = x + 22
    tw = w - 44
    cy = y + 20
    # kicker
    draw.text((tx, cy), kicker, font=F_SANS_B(21), fill=accent)
    cy += 32
    # headline, up to 2 lines
    for line in wrap(draw, headline, F_SANS_B(32), tw)[:2]:
        draw.text((tx, cy), line, font=F_SANS_B(32), fill=INK)
        cy += 40
    cy += 6
    # body, up to 3 lines
    for line in wrap(draw, body, F_SANS(23), tw)[:3]:
        draw.text((tx, cy), line, font=F_SANS(23), fill=(52, 50, 47))
        cy += 30


STORIES = [
    ((179, 38, 30), "CLIMATE  ·  ANTALYA",
     "COP31 collapses with no deal at all",
     "The UN climate summit ended with no agreement after the EU "
     "objected to a final text with no mention of fossil fuels."),
    ((176, 92, 8), "CONFLICT  ·  BAHRAIN",
     "Iran strikes US-linked targets in Bahrain",
     "Iran fired missiles and drones at US bases in Bahrain and hit "
     "tankers near Hormuz; a civilian site was hit, two hurt."),
    ((109, 40, 217), "JUSTICE  ·  MEXICO",
     "Cartel boss 'El Chapo Isidro' captured",
     "Mexican special forces seized Fausto Isidro Meza Flores in "
     "Sinaloa; 11 people were killed in the raid."),
    ((14, 116, 144), "WAR  ·  UKRAINE",
     "Russian missile hits Zelenskyy's hometown",
     "A strike on Kryvyi Rih killed a boy of 7 and a woman of 20 and "
     "wounded 60; a drone hit a Kyiv apartment block."),
    ((29, 78, 216), "TRADE  ·  BRUSSELS",
     "EU and Indonesia sign landmark trade deal",
     "After almost ten years of talks, the EU and Indonesia signed a "
     "deal scrapping tariffs on up to 98.5% of goods."),
    ((21, 128, 61), "DISASTER  ·  NIGERIA",
     "Boat capsizes in Nigeria; at least 24 dead",
     "A boat carrying people to a funeral capsized in Nigeria, "
     "killing at least 24."),
]


def main():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)

    # ---- masthead ----
    draw.rectangle([0, 0, W, 148], fill=NAVY)
    draw.text((40, 22), "THE WORLD IN ONE DAY", font=F_SANS_B(26),
              fill=GOLD)
    draw.text((40, 56), "Sunday, 22 November 2026",
              font=F_SERIF(58), fill=(255, 255, 255))
    draw.rectangle([40, 132, W - 40, 135], fill=GOLD)

    # ---- 3x2 grid of stories ----
    margin, gap = 40, 16
    bw = (W - 2 * margin - gap) // 2
    bh = 250
    y0 = 168
    for i, story in enumerate(STORIES):
        x = margin + (i % 2) * (bw + gap)
        y = y0 + (i // 2) * (bh + gap)
        draw_block(draw, x, y, bw, bh, story)

    # ---- footer ----
    fy = y0 + 3 * bh + 2 * gap + 6
    draw.rectangle([margin, fy, W - margin, fy + 2], fill=(180, 176, 168))
    draw.text((margin, fy + 10),
              "World news of Sunday 22 November 2026 — six stories, as reported on the day.",
              font=F_SANS(22), fill=MUTED)

    img.save("entry.png", "PNG")
    print("wrote entry.png")


if __name__ == "__main__":
    main()
