---
date: 24-07-2026
date modified: 08-08-2026
feed: show
tag: lecture
title: "Lectures"
---

See also: [[Syllabus]] · [[Class Schedule]] · [[Grading]]

One 2-hour session per week, Tuesdays 2:15–4:15pm. No class on 8 and 15 September.

<div class="syllabus-list">
{%- for l in site.data.lectures -%}
  {%- assign target_url = "/" | append: l.slug -%}
  {%- assign note = site.notes | where: "url", target_url | first -%}
  <div class="syllabus-row">
    <div class="syllabus-head">
      <span class="syllabus-num">L{{ l.num }}</span>
      {%- if note -%}
      <a class="syllabus-title" href="{{ site.baseurl }}/{{ l.slug }}">{{ l.title }}</a>
      {%- else -%}
      <span class="syllabus-title is-upcoming">{{ l.title }}</span>
      {%- endif -%}
      <span class="syllabus-date">{{ l.date }}</span>
    </div>
    {%- if l.summary -%}
    <p class="syllabus-summary">{{ l.summary }}</p>
    {%- endif -%}
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
