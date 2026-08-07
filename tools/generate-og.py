#!/usr/bin/env python3
"""
Generate a 1200x630 Open Graph image for every published note.

    python3 tools/generate-og.py            # only notes without an image
    python3 tools/generate-og.py --force    # re-render everything

Images land in assets/img/og/<slug>.png. The script also writes
_data/og.yml so the layout knows which slugs have one.

Rendering is done by headless Chrome, so the images use the real site
fonts (TASA Orbiter + JetBrains Mono) and need a network connection
the first time they're fetched.
"""

import argparse
import html
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTES = os.path.join(ROOT, "_notes")
OUT_DIR = os.path.join(ROOT, "assets", "img", "og")
DATA_FILE = os.path.join(ROOT, "_data", "og.yml")

CHROME_CANDIDATES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
    shutil.which("google-chrome") or "",
    shutil.which("chromium") or "",
]

BG = "#0A0B0E"
FG = "#F2F4F8"
DIM = "#A2A9B8"
ACCENT = "#A8E6B8"
LINE = "#23262D"


def find_chrome():
    for c in CHROME_CANDIDATES:
        if c and os.path.exists(c):
            return c
    sys.exit("Could not find Chrome. Edit CHROME_CANDIDATES in this script.")


def slugify(name):
    """Match Jekyll's :slug for a filename."""
    s = os.path.splitext(name)[0].lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def parse_front_matter(text):
    """Minimal YAML front matter reader: scalars plus one level of lists."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    raw, body = text[3:end], text[end + 4:]

    data, key = {}, None
    for line in raw.splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        item = re.match(r"\s*-\s+(.*)$", line)
        if item and key:
            data.setdefault(key, []).append(item.group(1).strip().strip('"\''))
            continue
        m = re.match(r"([A-Za-z0-9_ -]+):\s*(.*)$", line)
        if m:
            key = m.group(1).strip()
            val = m.group(2).strip().strip('"\'')
            data[key] = val if val else []
    return data, body


def load_lecture_titles():
    """Descriptive titles from _data/lectures.yml, keyed by slug."""
    path = os.path.join(ROOT, "_data", "lectures.yml")
    titles = {}
    if not os.path.exists(path):
        return titles
    slug = None
    for line in open(path):
        m = re.match(r'\s*slug:\s*"?([^"\n]+)"?', line)
        if m:
            slug = m.group(1).strip()
        t = re.match(r'\s*title:\s*"?([^"\n]+)"?', line)
        if t:
            pending = t.group(1).strip()
            titles["__pending__"] = pending
        if slug and "__pending__" in titles:
            titles[slug] = titles.pop("__pending__")
            slug = None
    return titles


def pretty_date(raw):
    """DD-MM-YYYY (the vault's format) -> '4 Aug 2026'."""
    m = re.match(r"(\d{2})-(\d{2})-(\d{4})$", raw.strip())
    if not m:
        return raw
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    d, mo, y = int(m.group(1)), int(m.group(2)), m.group(3)
    return f"{d} {months[mo - 1]} {y}"


def first_heading(body):
    for line in body.splitlines():
        m = re.match(r"#{1,3}\s+(.*)", line.strip())
        if m:
            return m.group(1).strip().rstrip("!").strip()
    return ""


def build_html(eyebrow, title, subtitle, chips):
    chip_html = "".join(
        f'<li>{html.escape(c)}</li>' for c in chips[:6]
    )
    chips_block = f'<ul class="chips">{chip_html}</ul>' if chip_html else ""
    sub_block = f'<div class="sub">{html.escape(subtitle)}</div>' if subtitle else ""

    # Long titles step down a size so they never overflow the card.
    size = 78 if len(title) <= 28 else (64 if len(title) <= 46 else 52)

    return f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=TASA+Orbiter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html, body {{ width:1200px; height:630px; }}
  body {{
    background:{BG}; color:{FG};
    font-family:'TASA Orbiter',-apple-system,sans-serif;
    display:flex; flex-direction:column; justify-content:center;
    padding:0 96px; position:relative; overflow:hidden;
  }}
  .flag {{
    position:absolute; top:-40px; right:-60px;
    width:520px; height:300px; --cell:30px;
    background-image:conic-gradient({ACCENT} 90deg, transparent 90deg 180deg,
                                    {ACCENT} 180deg 270deg, transparent 270deg);
    background-size:calc(var(--cell)*2) calc(var(--cell)*2);
    opacity:0.11;
  }}
  .brand {{
    position:absolute; top:54px; left:96px;
    font-family:'JetBrains Mono',monospace; font-size:22px; font-weight:500;
    letter-spacing:0.04em; display:flex; align-items:center; gap:6px;
  }}
  .cursor {{ display:inline-block; width:9px; height:20px; background:{ACCENT}; }}
  .eyebrow {{
    font-family:'JetBrains Mono',monospace; font-size:19px;
    letter-spacing:0.16em; text-transform:uppercase; color:{ACCENT};
    margin-bottom:22px;
  }}
  .title {{
    font-size:{size}px; font-weight:700; letter-spacing:-0.025em;
    line-height:1.08; max-width:940px;
  }}
  .sub {{
    font-size:30px; color:{DIM}; margin-top:16px; max-width:880px; line-height:1.25;
  }}
  .chips {{ list-style:none; display:flex; flex-wrap:wrap; gap:10px; margin-top:38px; max-width:940px; }}
  .chips li {{
    font-size:21px; color:{DIM};
    border:1px solid {LINE}; border-left:3px solid {ACCENT};
    padding:8px 14px;
  }}
</style></head><body>
  <div class="flag"></div>
  <div class="brand">TECH 1<span class="cursor"></span></div>
  <div class="eyebrow">{html.escape(eyebrow)}</div>
  <div class="title">{html.escape(title)}</div>
  {sub_block}
  {chips_block}
</body></html>"""


def render(chrome, html_text, out_path):
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
        f.write(html_text)
        tmp = f.name
    try:
        subprocess.run(
            [chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars",
             "--force-device-scale-factor=1", "--window-size=1200,630",
             "--virtual-time-budget=6000",
             f"--screenshot={out_path}", f"file://{tmp}"],
            capture_output=True, check=True,
        )
    finally:
        os.unlink(tmp)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true", help="re-render existing images")
    args = ap.parse_args()

    chrome = find_chrome()
    os.makedirs(OUT_DIR, exist_ok=True)
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    lecture_titles = load_lecture_titles()

    slugs, made, skipped = [], 0, 0

    for name in sorted(os.listdir(NOTES)):
        if not name.endswith(".md") or name.startswith("_"):
            continue
        fm, body = parse_front_matter(open(os.path.join(NOTES, name)).read())
        if fm.get("feed") != "show":
            continue

        slug = slugify(name)
        slugs.append(slug)
        out = os.path.join(OUT_DIR, slug + ".png")
        if os.path.exists(out) and not args.force:
            skipped += 1
            continue

        tag = (fm.get("tag") or "").strip()
        eyebrow = {"lecture": "Lecture", "exercise": "Exercise",
                   "project": "Project"}.get(tag, "Tech 1")
        if fm.get("date"):
            eyebrow += " · " + pretty_date(fm["date"])

        title = lecture_titles.get(slug) or fm.get("title", slug)
        # exercises read better without the "Exercise - " prefix
        title = re.sub(r"^Exercise\s*-\s*", "", title)

        subtitle = ""
        heading = first_heading(body)
        if heading and heading.lower() != title.lower():
            subtitle = heading

        chips = fm.get("key_areas") or []
        if not isinstance(chips, list):
            chips = []

        render(chrome, build_html(eyebrow, title, subtitle, chips), out)
        made += 1
        print(f"  ✓ {slug}.png")

    with open(DATA_FILE, "w") as f:
        f.write("# Generated by tools/generate-og.py — do not edit by hand.\n")
        f.write("slugs:\n")
        for s in slugs:
            f.write(f"  - {s}\n")

    print(f"\n{made} generated, {skipped} already existed. "
          f"{len(slugs)} slugs written to _data/og.yml")
    if skipped and not args.force:
        print("Run with --force to re-render everything.")


if __name__ == "__main__":
    main()
