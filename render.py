#!/usr/bin/env python3
"""Render the front page of THE WORLD TODAY for Monday 23 November 2026.

Draws a one-page newspaper front page with Pillow from the story file below.
Every story was compiled on 23 Nov 2026 from wire reporting (AFP, Reuters,
AP, BBC, The Guardian); sources are listed in README.md. The output is
entry.png, which main.py copies to /output/entry.png unchanged.

Run:  python3 render.py
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1000, 1024
M = 34                      # page margin
CW = W - 2 * M              # content width

PAPER = (246, 241, 229)
INK = (22, 19, 14)
MUTED = (92, 83, 66)
RED = (158, 27, 27)
NAVY = (20, 45, 74)
NAVY_TX = (240, 236, 222)
GOLD = (198, 152, 62)
RULE = (22, 19, 14)

FD = "/usr/share/fonts/truetype/"
F_DISPLAY = FD + "noto/NotoSerifDisplay-Black.ttf"
F_SERIF_B = FD + "noto/NotoSerif-Bold.ttf"
F_SERIF = FD + "noto/NotoSerif-Regular.ttf"
F_SERIF_I = FD + "noto/NotoSerif-Italic.ttf"
F_SANS_B = FD + "dejavu/DejaVuSans-Bold.ttf"
F_SANS = FD + "dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)


def text_w(s, f):
    return d.textlength(s, font=f)


def wrap(s, f, width):
    """Greedy word wrap; returns a list of lines."""
    lines, cur = [], ""
    for word in s.split():
        trial = word if not cur else cur + " " + word
        if text_w(trial, f) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(x, y, s, f, width, leading=1.28, fill=INK, align="left"):
    """Draw a wrapped paragraph; returns the y just below it."""
    for line in wrap(s, f, width):
        lx = x
        if align == "center":
            lx = x + (width - text_w(line, f)) / 2
        d.text((lx, y), line, font=f, fill=fill)
        y += f.size * leading
    return y


def centered(y, s, f, fill=INK):
    d.text(((W - text_w(s, f)) / 2, y), s, font=f, fill=fill)
    return y + f.size


def hrule(y, thick=1, fill=RULE, x0=M, x1=W - M):
    d.rectangle([x0, y, x1, y + thick - 1], fill=fill)
    return y + thick


def kicker(x, y, s, fill=RED, size=15, align="left", width=CW):
    f = font(F_SANS_B, size)
    lx = x if align == "left" else x + (width - text_w(s, f)) / 2
    d.text((lx, y), s, font=f, fill=fill)
    return y + size + 6


def headline(x, y, s, size, width, align="left", fill=INK, leading=1.08):
    f = font(F_SERIF_B, size)
    return para(x, y, s, f, width, leading=leading, fill=fill, align=align)

# ---------------------------------------------------------------- stories ---
LEAD_BODY = (
    "ANTALYA \u2014 The COP31 climate summit ended in failure on Monday after "
    "negotiators failed to agree a deal on fossil fuels, the question that "
    "split the talks from the start. T\u00fcrkiye's final draft did not "
    "mention the words \u201cfossil fuels\u201d at all. Australian Prime "
    "Minister Anthony Albanese, whose country co-hosted the summit, called "
    "the collapse a sign of \u201cdifficult geopolitical times\u201d. "
    "\u201cThat is the reality,\u201d he told reporters in Canberra. "
    "Delegates from some 200 nations had pushed the summit into record "
    "overtime, but the gulf between producer states and the countries "
    "demanding a rapid phase-out proved too wide to bridge."
)

UKRAINE_BODY = (
    "A Russian drone smashed into a five-storey apartment block in Dymer, "
    "in the Kyiv region, killing at least 12 people as rescuers searched "
    "the rubble for the missing. Zelensky said Russia fired 165 "
    "missiles, some 2,700 attack drones and nearly 1,460 glide bombs at "
    "Ukraine in a single week, calling US delays in supplying Patriot "
    "missiles \u201cdifficult to understand\u201d."
)

GULF_BODY = (
    "An Iranian strike wounded two people in Bahrain, drawing a furious "
    "response from Saudi Arabia, which condemned Tehran's \u201ccriminal\u201d "
    "attacks. The Saudi-led coalition said it had intercepted a Houthi "
    "missile fired toward the kingdom's western region, as the "
    "confrontation widens around the Strait of Hormuz \u2014 chokepoint "
    "for a fifth of the world's oil."
)

INDONESIA_BODY = (
    "The search resumes today for dozens of workers missing after fire "
    "gutted the PT Fonusa Agung Mulia candy factory in Cikande, west of "
    "Jakarta. Police removed 24 body bags on Sunday; some 300 staff "
    "were on shift on Saturday. Victims are unidentifiable; DNA "
    "testing may take weeks."
)

COURT_BODY = (
    "The International Court of Justice has found Myanmar committed "
    "genocide against the Rohingya in 2017 \u2014 a first for the court. "
    "By nine votes to six, it ordered reparations. Yangon calls ASEAN "
    "criticism \u201cunfair and imbalanced\u201d."
)

SPORT_BODY = (
    "India posted a record 720 for nine declared against New Zealand in "
    "the Wellington Test, seizing control on day four at the Basin "
    "Reserve. In snooker, Anupama successfully defended her IBSF World "
    "Women's Championship crown."
)

BRIEFS = [
    ("SEOUL", "South Korea's education minister quits over an AI exam-cheating scandal."),
    ("SINALOA", "Mexico captures \u201cEl Chapo Isidro\u201d, the FBI most-wanted cartel boss; 11 die in firefights."),
    ("BRAS\u00cdLIA", "Former president Bolsonaro is \u201cstable\u201d in intensive care."),
    ("NEW DELHI", "Nepal's PM Balendra Shah holds talks with India's PM Modi on a state visit."),
]

# ----------------------------------------------------------------- layout ---
y = 12
f_strip = font(F_SANS_B, 15)
d.text((M, y), "VOL. IX \u2014 No. 328", font=f_strip, fill=MUTED)
centered(y, "MONDAY, 23 NOVEMBER 2026", f_strip, fill=INK)
d.text((W - M - text_w("GLOBAL EDITION", f_strip), y),
       "GLOBAL EDITION", font=f_strip, fill=MUTED)
y += 24
y = hrule(y, 1)
y += 3
y = hrule(y, 3)
y += 10

centered(y, "THE WORLD TODAY", font(F_DISPLAY, 84))
y += 90
y = hrule(y, 3)
y += 3
y = hrule(y, 1)
y += 12

# Lead story ---------------------------------------------------------------
y = kicker(M, y, "CLIMATE SUMMIT \u2014 ANTALYA, T\u00dcRKIYE", align="center")
y = headline(M, y, "COP31 TALKS COLLAPSE WITHOUT A DEAL", 42, CW,
             align="center", leading=1.04)
y += 6
y = para(M + 60, y,
         "Co-host Albanese blames \u201cdifficult geopolitical times\u201d.",
         font(F_SERIF_I, 19), CW - 120, leading=1.22, align="center")
y += 8
col_w = (CW - 2 * 26) // 3
col_words = LEAD_BODY.split()
third = (len(col_words) + 2) // 3
chunks = [" ".join(col_words[i * third:(i + 1) * third]) for i in range(3)]
lead_top = y
for i, chunk in enumerate(chunks):
    cy = para(M + i * (col_w + 26), lead_top, chunk, font(F_SERIF, 14),
              col_w, leading=1.26)
    y = max(y, cy)
y += 6
y = hrule(y, 2)
y += 12

# Two-column row: Ukraine | Gulf -------------------------------------------
half = (CW - 30) // 2
row_top = y
uy = kicker(M, row_top, "WAR IN UKRAINE \u2014 DYMER, KYIV REGION", size=13)
uy = headline(M, uy, "RUSSIAN STRIKES KILL 12 NEAR KYIV", 24, half)
uy = para(M, uy + 4, UKRAINE_BODY, font(F_SERIF, 14.5), half, leading=1.22)
gy = kicker(M + half + 30, row_top, "GULF ESCALATION \u2014 MANAMA \u00b7 RIYADH",
            size=13)
gy = headline(M + half + 30, gy, "IRAN STRIKE WOUNDS TWO IN BAHRAIN", 24,
              half)
gy = para(M + half + 30, gy + 4, GULF_BODY, font(F_SERIF, 14.5), half,
          leading=1.22)
d.line([M + half + 15, row_top, M + half + 15, max(uy, gy)], fill=MUTED,
       width=1)
y = max(uy, gy) + 12

# Markets band ---------------------------------------------------------------
band_top = y
d.rectangle([M, band_top, W - M, band_top + 124], fill=NAVY)
by = band_top + 11
by = kicker(M + 20, by, "MARKETS \u2014 FRIDAY'S CLOSE \u00b7 THE WEEK IN REVIEW",
            fill=GOLD, size=14)
f_mh = font(F_SERIF_B, 29)
d.text((M + 20, by), "TECH SELLOFF PUSHES WALL ST INTO CORRECTION",
       font=f_mh, fill=NAVY_TX)
by += 34
figs = [("NASDAQ", "\u22125.3%"), ("S&P 500", "\u22123.7%"),
        ("NVIDIA", "\u221213.7%"), ("ANTHROPIC", "\u22128.5%"),
        ("DOW", "\u22121.9%")]
fx = M + 20
f_fig = font(F_SANS_B, 22)
f_lab = font(F_SANS_B, 12)
for lab, val in figs:
    d.text((fx, by), val, font=f_fig, fill=(255, 120, 100))
    d.text((fx, by + 25), lab, font=f_lab, fill=GOLD)
    fx += (CW - 40) // 5
by += 60
d.text((M + 20, band_top + 105),
       "Anthropic's record IPO fails to calm the AI rout \u00b7 Nasdaq erases "
       "its 2026 gains \u00b7 Asia's worst week since 2020",
       font=font(F_SERIF_I, 14.5), fill=NAVY_TX)
y = band_top + 124 + 10

# Three-column row: Indonesia | World Court | Sport -------------------------
third_w = (CW - 2 * 28) // 3
row_top = y
cols = [
    ("INDONESIA \u2014 CIKANDE, BANTEN", "DOZENS MISSING IN FACTORY FIRE",
     INDONESIA_BODY),
    ("THE HAGUE \u2014 ICJ FALLOUT", "MYANMAR COMMITTED GENOCIDE \u2014 ICJ",
     COURT_BODY),
    ("SPORT \u2014 WELLINGTON", "INDIA'S RECORD 720/9 STUNS NEW ZEALAND",
     SPORT_BODY),
]
ends = []
for i, (kick, head, body) in enumerate(cols):
    x = M + i * (third_w + 28)
    cy = kicker(x, row_top, kick, size=13)
    cy = headline(x, cy, head, 20, third_w, leading=1.12)
    cy = para(x, cy + 4, body, font(F_SERIF, 13.5), third_w, leading=1.24)
    ends.append(cy)
    if i:
        d.line([x - 14, row_top, x - 14, max(ends)], fill=MUTED, width=1)
y = max(ends) + 12
y = hrule(y, 2)
y += 8

# Briefs ---------------------------------------------------------------------
y = kicker(M, y, "ALSO IN TODAY'S NEWS", fill=INK, size=14)
bcol_w = (CW - 3 * 20) // 4
b_end = y
for j, (place, txt) in enumerate(BRIEFS):
    x = M + j * (bcol_w + 20)
    byy = para(x, y, f"{place} \u2014 {txt}", font(F_SANS, 12),
               bcol_w, leading=1.22)
    b_end = max(b_end, byy)
y = b_end + 6
y = hrule(y, 3)
y += 6
centered(y, "Compiled from AFP \u00b7 Reuters \u00b7 AP \u00b7 BBC \u00b7 The "
            "Guardian reporting \u2014 sources in README.md \u00b7 "
            "THE WORLD TODAY, Monday 23 November 2026",
         font(F_SANS, 12.5), fill=MUTED)
y += 18

print("final y:", y, "of", H)
img.save("entry.png", optimize=True)
import os
print("entry.png bytes:", os.path.getsize("entry.png"))
