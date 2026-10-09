---
date: 24-07-2026
date modified: 08-08-2026
feed: show
title: "Syllabus"
---

See also: [[Lectures]] · [[Class Schedule]] · [[Grading]] · [[AI Policy]]

**Course Title:** Tech 1 — Web & Mobile Ecosystem Fundamentals

**Course Objective:** Gain a foundational understanding of the core technologies, platforms, and concepts that underpin the modern web and mobile ecosystems, essential for product and design professionals.

**Format:** 13 lectures, 2 hours each, once a week.

### How this course works

This is not a coding course. You will not be asked to memorise syntax or write programs from scratch. Instead:

- **You will build from week one.** Using AI tools, you will generate, modify, and deploy real web applications — starting with a personal webpage in the very first session.
- **Fundamentals follow experience.** Each week we dissect something you have already built.
- **AI is the medium, not a module.** You are expected to generate most of your code with AI tools. The skill we are building is *directing* these tools well — which requires understanding the stack conceptually.
- **The course converges into a final project.** The last weeks are a build sprint ending in a Demo Day.

### Course structure

<div class="syllabus-list">
{%- for l in site.data.lectures -%}
  <div class="syllabus-row">
    <div class="syllabus-head">
      <span class="syllabus-num">L{{ l.num }}</span>
      <a class="syllabus-title" href="{{ site.baseurl }}/{{ l.slug }}">{{ l.title }}</a>
      <span class="syllabus-date">{{ l.date }}</span>
    </div>
    {%- if l.key_areas.size > 0 -%}
    <ul class="key-areas">
      {%- for ka in l.key_areas -%}
      <li>{{ ka }}</li>
      {%- endfor -%}
    </ul>
    {%- endif -%}
  </div>
{%- endfor -%}
</div>

### Key areas, and where they're covered

<div class="coverage">
{%- assign areas = "" | split: "" -%}
{%- for l in site.data.lectures -%}
  {%- for ka in l.key_areas -%}
    {%- assign areas = areas | push: ka -%}
  {%- endfor -%}
{%- endfor -%}
{%- assign areas = areas | uniq | sort -%}
{%- for area in areas -%}
  <div class="coverage-row">
    <span class="coverage-area">{{ area }}</span>
    <span class="coverage-links">
      {%- for l in site.data.lectures -%}
        {%- if l.key_areas contains area -%}
        <a href="{{ site.baseurl }}/{{ l.slug }}">L{{ l.num }}</a>
        {%- endif -%}
      {%- endfor -%}
    </span>
  </div>
{%- endfor -%}
</div>
