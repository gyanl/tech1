---
date: 01-09-2026
date modified: 25-08-2026
feed: show
key_areas:
  - "How the internet works"
  - "HTTP / HTTPS"
  - "IP addresses"
  - "Web browsers and their role"
tag: lecture
title: "Lecture 5"
---

## Shipping Software

From "a page that works" to "an interface that's designed."

#### Hour 1 — The front-end as a design material
- Responsive design: one design, every screen (viewports, breakpoints, mobile-first)
- Design systems in code: components, tokens, why engineers keep saying "reusable"
- Frameworks in one slide each: what React/Next.js actually are and why AI tools default to them
- Figma to code: what translates cleanly, what doesn't, and why "make it look like the mockup" fails
- Accessibility as a design responsibility, not an engineering checkbox

#### Hour 2 — Studio
- **Exercise:** [[Exercise - Figma to Code]] — take one of your own Figma designs and get an AI tool to build it; document where it diverged
- Crit: compare generated results across tools (v0, Lovable, Claude, Figma Make)

#### Homework
- Iterate your build until it matches your design intent. Keep a log of the prompts that worked.

## Internet Infrastructure

Everything before this week disappeared when you refreshed. Let's fix that.

#### Hour 1 — Where data lives
- What a back-end is: code that runs on someone else's computer, not in the browser
- Server-side languages exist (Python, Node.js) — what you need to know as a director, not a writer
- Databases: tables you can't see — SQL (spreadsheet with rules) vs NoSQL (folder of documents)
- The full round trip: form → request → server → database → response → screen
- Designers and data models: the schema *is* a design decision (what fields does a "user" have?)

#### Hour 2 — Studio
- **Exercise:** [[Exercise - Add a Database]] — use AI to add persistence (e.g. Supabase) to a simple app: a guestbook, a poll, an RSVP page
- Look at your data sitting in the database dashboard — it's just rows

#### Homework
- Sketch the data model of an app you use daily (what are its "tables"?). Bring the sketch.
