---
date: 11-08-2026
date modified: 08-08-2026
feed: show
key_areas:
  - "CSS — styling"
  - "Responsive web design"
  - "Hosting and deployment"
  - "Version control (Git)"
tag: lecture
title: "Lecture 2"
---

## Designing your Website

Last week you shipped a page. This week we open the hood.

#### Hour 1 — The three languages
- View Source: what the AI actually wrote for you
- **HTML** — structure and meaning (headings, lists, links, semantics)
- **CSS** — styling (selectors, the box model as a layout designer's mental model, typography on the web)
- **JavaScript** — interactivity (events, changing the page after it loads)
- Why this separation exists — content vs presentation vs behaviour
- Browser DevTools as a designer's x-ray machine

#### Hour 2 — Dissection lab
- **Exercise:** [[Exercise - Web Page Anatomy]] — pick a complex real-world page, identify its structure, styling, and interactions using DevTools
- Editing your own page's generated code by hand: change a colour, a font, a word — prove to yourself it's not magic

#### Homework
- Ask an AI to explain three things you found in DevTools that you didn't understand. Bring the best explanation to class.

#### What's a Computer?

A whirlwind history of computing — not for the dates, but for what each moment adds to your mental model of the machine in front of you.

<iframe class="video-embed" src="https://www.youtube.com/embed/3S5BLs51yDQ" title="What's a Computer?" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

---
#### 1801 — Machines can follow instructions

- Jacquard's loom weaves patterns from **punched cards**
- The pattern isn't in the machine — it's in the card
- First separation of **machine** and **instructions**

---
#### 1837 — Machines can compute anything

- Babbage designs the Analytical Engine; Ada Lovelace writes what may be the first program
- Her bigger insight: a computing machine could manipulate **any symbols** — music, text, not just numbers

---
#### 1936 — One machine to rule them all

- Turing: one machine that can imitate **any other machine**, given the right instructions
- This is why your laptop can be a typewriter, a cinema, a studio, and a piano
- Software = the machine pretending

---
#### 1947 — Instructions get fast and cheap

- The transistor: a switch with no moving parts
- Then the chip: billions of switches, effectively free
- Everything since is mostly *more, smaller, cheaper*

---
#### 1984 — Computers for people

- Xerox PARC → Macintosh: the GUI
- Designers enter the story: the interface becomes a **designed artifact**
- The machine adapts to humans, not the other way around

---
#### The mental model

> **input → processing → memory/storage → output**

- Every device you own is this loop: phone, smartwatch, ATM, washing machine
- Memory (fast, forgets when off) vs storage (slow, remembers)

---
#### The machine is fast and dumb

- The CPU does billions of tiny, stupid steps per second — it never "understands"
- Software is just instructions; the OS is the manager juggling them
- **Live:** open Activity Monitor / Task Manager — look at what your machine is doing *right now*
w