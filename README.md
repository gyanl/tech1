# Tech 1 — Web & Mobile Ecosystem Fundamentals

Course website for **Tech 1**, a course that gives design students a foundational understanding of the core technologies, platforms, and concepts that underpin the modern web and mobile ecosystems.

The course is AI-heavy by design: students **generate code with AI tools** instead of writing it by hand, shipping a live webpage in the very first session and using each thing they build to understand what's happening under the hood — HTML/CSS/JS, HTTP and DNS, back-ends and databases, APIs, mobile ecosystems, cloud computing, and the software development lifecycle. The course converges into a final group project presented at a Demo Day.

## Structure

- `_notes/` — all course content: syllabus, grading, 13 lecture notes, exercises, and the final project brief
- `assets/` — images, css, js
- `pages/` — index and utility pages

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
