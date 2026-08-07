# Tech 1 — Web & Mobile Ecosystem Fundamentals

Course website for **Tech 1**, a course that gives design students a foundational understanding of the core technologies, platforms, and concepts that underpin the modern web and mobile ecosystems.

The course is AI-heavy by design: students **generate code with AI tools** instead of writing it by hand, shipping a live webpage in the very first session and using each thing they build to understand what's happening under the hood — HTML/CSS/JS, HTTP and DNS, back-ends and databases, APIs, mobile ecosystems, cloud computing, and the software development lifecycle. The course converges into a final group project presented at a Demo Day.

## Structure

- `_notes/` — all course content: syllabus, grading, 13 lecture notes, exercises, and the final project brief
- `assets/` — images, css, js
- `pages/` — index and utility pages

## Social preview (OG) images

Every published note gets its own 1200×630 share image, generated from its
title, date and key areas.

```
python3 tools/generate-og.py            # render any that are missing
python3 tools/generate-og.py --force    # re-render everything
```

Images are written to `assets/img/og/<slug>.png` and the script updates
`_data/og.yml`, which the layout reads to decide whether a page has one.
Pages without an image fall back to `assets/img/OGImg.png` (built from
`assets/og-template.html`).

The generator runs automatically before every Jekyll build, but only renders
what's missing, so normal builds are unaffected. Control it with:

```
OG=skip bundle exec jekyll serve     # don't run it at all
OG=force bundle exec jekyll build    # re-render everything
```

Rendering uses headless Chrome, so it only works locally — commit the PNGs
so deployed builds (e.g. GitHub Pages) serve them.

## Running locally

This site is built with [Jekyll](https://jekyllrb.com/) using the [Jekyll Garden](https://github.com/Jekyll-Garden/jekyll-garden.github.io) theme, which publishes an [Obsidian](https://obsidian.md/) vault as a static website.

```
bundle install
bundle exec jekyll serve
```

Then open `http://localhost:4000`. Alternatively, with Docker:

```
docker-compose up -d
```

## License

Course content (notes, exercises) is licensed under [CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/). The Jekyll Garden theme is MIT-licensed — see [LICENSE](LICENSE) and credits to [Hiran Venugopalan](https://github.com/hfactor).

## Favicon

Icons are generated the same way as the OG images, from
`assets/favicon-template.html` (full mark, for large sizes) and
`assets/favicon-small-template.html` (simplified, for 16/32px):

```
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
"$CHROME" --headless=new --window-size=512,512 --virtual-time-budget=8000 \
  --screenshot=/tmp/icon512.png assets/favicon-template.html
sips -z 180 180 /tmp/icon512.png --out assets/img/apple-touch-icon.png
sips -z 512 512 /tmp/icon512.png --out assets/img/icon-512.png

"$CHROME" --headless=new --window-size=512,512 --virtual-time-budget=8000 \
  --screenshot=/tmp/small512.png assets/favicon-small-template.html
sips -z 32 32 /tmp/small512.png --out assets/img/favicon-32.png
sips -z 16 16 /tmp/small512.png --out assets/img/favicon-16.png
```
