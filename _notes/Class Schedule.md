---
date: 04-08-2026
date modified: 08-08-2026
feed: show
title: "Class Schedule"
---

See also: [[Syllabus]] · [[Lectures]] · [[Grading]]

Tuesdays, **2:15–4:15pm**. Dates may shift if I'm travelling — I'll give as much notice as possible, and this page stays up to date.

| Week | Date | Lecture |
| ---- | ---- | ------- |
{% for l in site.data.lectures -%}
{%- if l.num == 6 -%}
| — | 8 September 2026 | *No class (travelling)* |
| — | 15 September 2026 | *No class (travelling)* |
{% endif -%}
| {{ l.num }} | {{ l.date }} | [{{ l.title }}]({{ site.baseurl }}/{{ l.slug }}) |
{% endfor %}
