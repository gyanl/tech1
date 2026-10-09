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
{%- if l.num == 12 -%}
| — | 10 November 2026 | *No class (Diwali break, 6–15 November)* |
{% endif -%}
{%- if l.num == 10 -%}
| — | 20 October 2026 | *No class (Dussehra)* |
{% endif -%}
{%- if l.num == 8 -%}
| — | 6 October 2026 | *No class (moved to Friday 9 October)* |
{% endif -%}
{%- if l.num == 6 -%}
| — | 8 September 2026 | *No class (travelling)* |
| — | 15 September 2026 | *No class (travelling)* |
{% endif -%}
| {{ l.num }} | {{ l.date }} | [{{ l.title }}]({{ site.baseurl }}/{{ l.slug }}) |
{% endfor %}
