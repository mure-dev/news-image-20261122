#!/usr/bin/env python3
"""Front page for Sunday 22 November 2026, drawn with Pillow.

Six stories from the day are laid out as a newspaper front page on a
1024 by 1024 canvas. Run from this directory:

    python3 draw_poster.py

and the finished page is saved as entry.png next to this script.
"""

from PIL import Image, ImageDraw, ImageFont

CANVAS = (1024, 1024)
BACKGROUND = (250, 247, 240)
CARD = (255, 255, 255)
CARD_EDGE = (210, 206, 198)
BODY_INK = (52, 50, 47)
HEAD_INK = (20, 20, 20)
FOOT_INK = (90, 88, 84)
MASTHEAD = (15, 42, 74)
RULE = (198, 158, 62)

DEJAVU = "/usr/share/fonts/truetype/dejavu"


def typeface(filename, points):
    return ImageFont.truetype(DEJAVU + "/" + filename, points)


SERIF_BOLD = lambda pts: typeface("DejaVuSerif-Bold.ttf", pts)
SANS_BOLD = lambda pts: typeface("DejaVuSans-Bold.ttf", pts)
SANS = lambda pts: typeface("DejaVuSans.ttf", pts)


def fit_lines(pen, sentence, face, max_px):
    """Split a sentence into lines no wider than max_px."""
    wrapped = []
    current = ""
    for word in sentence.split():
        candidate = (current + " " + word).strip()
        if pen.textlength(candidate, font=face) <= max_px:
            current = candidate
        else:
            if current:
                wrapped.append(current)
            current = word
    if current:
        wrapped.append(current)
    return wrapped


# Each story: accent colour, section label, headline, two-sentence deck.
NEWS = [
    {
        "tone": (179, 38, 30),
        "tag": "CLIMATE  ·  ANTALYA",
        "head": "COP31 collapses with no deal at all",
        "deck": "The UN climate summit ended with no agreement after the EU "
                "rejected a final text silent on fossil fuels.",
    },
    {
        "tone": (176, 92, 8),
        "tag": "CONFLICT  ·  BAHRAIN",
        "head": "Iran strikes US-linked targets in Bahrain",
        "deck": "Iran fired missiles and drones at US bases in Bahrain and hit "
                "tankers near Hormuz; a civilian site was hit, two hurt.",
    },
    {
        "tone": (109, 40, 217),
        "tag": "JUSTICE  ·  MEXICO",
        "head": "Cartel boss 'El Chapo Isidro' captured",
        "deck": "Mexican special forces seized Fausto Isidro Meza Flores in "
                "Sinaloa; 11 people were killed in the raid.",
    },
    {
        "tone": (14, 116, 144),
        "tag": "WAR  ·  UKRAINE",
        "head": "Russian missile hits Zelenskyy's hometown",
        "deck": "A strike on Kryvyi Rih killed a boy of 7 and a woman of 20 and "
                "wounded 60; a drone hit a Kyiv apartment block.",
    },
    {
        "tone": (29, 78, 216),
        "tag": "TRADE  ·  BRUSSELS",
        "head": "EU and Indonesia sign landmark trade deal",
        "deck": "After almost ten years of talks, the EU and Indonesia signed a "
                "deal scrapping tariffs on up to 98.5% of goods.",
    },
    {
        "tone": (21, 128, 61),
        "tag": "DISASTER  ·  NIGERIA",
        "head": "Boat capsizes in Nigeria; at least 24 dead",
        "deck": "A boat carrying people to a funeral capsized in Nigeria, "
                "killing at least 24.",
    },
]


def story_card(pen, left, top, width, height, item):
    pen.rectangle([left, top, left + width, top + height],
                  fill=CARD, outline=CARD_EDGE, width=2)
    pen.rectangle([left, top, left + width, top + 8], fill=item["tone"])
    inner_left = left + 22
    inner_width = width - 44
    cursor = top + 20
    pen.text((inner_left, cursor), item["tag"],
             font=SANS_BOLD(21), fill=item["tone"])
    cursor += 32
    for line in fit_lines(pen, item["head"], SANS_BOLD(32),
                          inner_width)[:2]:
        pen.text((inner_left, cursor), line, font=SANS_BOLD(32),
                 fill=HEAD_INK)
        cursor += 40
    cursor += 6
    for line in fit_lines(pen, item["deck"], SANS(23), inner_width)[:3]:
        pen.text((inner_left, cursor), line, font=SANS(23), fill=BODY_INK)
        cursor += 30


def build_page():
    page = Image.new("RGB", CANVAS, BACKGROUND)
    pen = ImageDraw.Draw(page)

    # Masthead: paper name, the date, and a gold rule.
    pen.rectangle([0, 0, 1024, 148], fill=MASTHEAD)
    pen.text((40, 22), "THE WORLD IN ONE DAY", font=SANS_BOLD(26),
             fill=RULE)
    pen.text((40, 56), "Sunday, 22 November 2026",
             font=SERIF_BOLD(58), fill=(255, 255, 255))
    pen.rectangle([40, 132, 1024 - 40, 135], fill=RULE)

    # Six stories in a 3-by-2 grid.
    outer, gutter = 40, 16
    card_w = (1024 - 2 * outer - gutter) // 2
    card_h = 250
    first_row = 168
    for index, item in enumerate(NEWS):
        col = index % 2
        row = index // 2
        story_card(pen,
                   outer + col * (card_w + gutter),
                   first_row + row * (card_h + gutter),
                   card_w, card_h, item)

    # Footer line under the grid.
    rule_y = first_row + 3 * card_h + 2 * gutter + 6
    pen.rectangle([outer, rule_y, 1024 - outer, rule_y + 2],
                  fill=(180, 176, 168))
    pen.text((outer, rule_y + 10),
             "World news of Sunday 22 November 2026 — six stories, "
             "as reported on the day.",
             font=SANS(22), fill=FOOT_INK)
    return page


if __name__ == "__main__":
    build_page().save("entry.png", "PNG")
    print("wrote entry.png")
