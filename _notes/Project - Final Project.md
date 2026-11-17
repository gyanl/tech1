---
date: 09-10-2026
date modified: 18-11-2026
feed: show
tag: project
title: "Project - Final Project"
---

See also: [[Grading]]

### Start collecting ideas for your final project

Your final project is a startup: a digital product that people sign in to and use, and a landing page that tells them about it and lets them sign up. You'll build it in the last three weeks of the course. Teams and topics get decided in Lecture 10, so start collecting ideas now.

Bring three, each written like this:

```text
This is for ___, who currently ___.
It lets them ___.
They'd sign up because ___.
It uses ___.
```

- **Who it's for** should be a group you can actually reach this month: your class, your hostel, your family, a club you're in. "Everyone" isn't a group.
- **Who currently** is what they do today without your app: a WhatsApp group, a spreadsheet, shouting across the corridor.
- **They'd sign up because** is the one line your landing page has to get across. If you can't fill it in, people won't sign up.
- **It uses** is which parts of this course it needs besides sign-in: saved data, data shared between people, an API, an AI feature. Most good ideas need at least two.

Some things to note:

- Small is better. One thing that fully works beats five that half work, and you'll have about four weeks to build it.
- The best ideas usually come from something you or your friends find annoying every week.
- If one of your ideas has an AI feature, write its "When the user ___, the model ___, so that ___" sentence too.

### Brief

In teams of up to 3, start a startup. You'll make two things:

1. **A digital product** that people sign in to and use. It can have AI features, but it doesn't have to.
2. **A landing page** that tells people what your product is, lets them sign up, and takes them straight into using it.

Both should be deployed, built mostly by directing AI tools, and presented at Demo Day.

### The shape of it

- **Introduced (L9, 13 October):** the brief, and what a startup is. Sharpen your ideas.
- **Kickoff (L10, 27 October):** form teams, pitch ideas, submit a one-page proposal: the problem, who it's for, the core flow, and a sketch of your stack.
- **Sprint 1 (L11, Wednesday 4 November):** sign in and the core flow working end to end, however ugly. Live crit.
<<<<<<< HEAD
- **Sprint 2 (L12, 19 November):** the landing page, and the product made ship-ready: empty and error states, a security check, polish. Feature freeze at the end of the week.
=======
- **Sprint 2 (L12, Wednesday 18 November, 11am–1pm IST):** the landing page, and the product made ship-ready: empty and error states, a security check, polish. Feature freeze at the end of the week.
>>>>>>> 28d287896449773ebffe9a471eaea278bf6c7e41
- **Demo Day (L13, Friday 27 November, from 2:15pm):** a 7-minute live demo, starting from your landing page, plus your process story, and 3 minutes of Q&A.

### Requirements

1. **Deployed and public.** A URL that works on a phone on the day of the demo.
2. **Sign in.** People sign in to use the product, with Sign in with Google or another provider, as in [[Lecture 8 - Authentication & Authorisation]] and [[Exercise 11 - Sign in with Google]]. Your database rules use it, so people can only change their own things.
3. **Has a back-end.** It stores or fetches real data: a database, an external API, or both.
4. **A landing page** that:
   - says what the product is and who it's for, in the first screen
   - shows the product, with screenshots or a short video, not just describing it
   - has one clear sign-up button that leads into the product
   - works on a phone
5. **The first five minutes are designed.** Landing page → sign up → first use is one flow. What does someone see the first time they sign in, before they've added anything?
6. **Process documentation.** Your proposal, sprint plans, prompt logs, dead ends, and what you'd do differently.
7. **You understand your stack.** Every team member can answer "where does this data live?", "what happens when I click this?" and "how does the app know who I am?"

An AI feature is welcome if it earns its place, but it's not required.

### Scope advice

The best projects are one small thing that fully works. "Splitwise for hostels" beats "a social network." You will cut scope in L11. Teams that pick a small idea get to spend L12 on the landing page and polish instead of fixing things.

A startup needs people who'll actually sign up. Pick a group you can reach this month, and get a few of them to sign up before Demo Day.

### Evaluation

| Criteria | Marks | Description |
| --- | --- | --- |
| Timeliness | 2 | Proposal and sprint milestones hit on time. |
| Concept | 3 | Clarity of the problem, fit of the solution, sensible scope. |
| Working Product | 5 | Deployed, sign-in works, core flow works, handles errors, works on mobile. |
| Landing Page & Sign-up | 3 | Explains the product clearly, and takes a stranger from first visit to using it. |
| Design & Polish | 3 | Visual quality, states, coherence: the design work AI skips. |
| Stack Understanding | 2 | The team can explain how their own product works, at this course's depth. |
| Presentation & Process | 2 | Demo quality, and honesty and completeness of process documentation. |
| **Total** | **20** | |
