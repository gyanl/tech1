---
date: 13-10-2026
date modified: 08-10-2026
feed: show
key_areas:
  - "Startups and MVPs"
  - "Software development lifecycle"
  - "Agile / Scrum"
  - "Version control (Git)"
  - "Landing pages"
  - "iOS vs Android platforms"
  - "Native vs hybrid vs web apps"
  - "App stores and distribution"
  - "IaaS, PaaS, SaaS"
  - "Scaling and cost"
slug: "lecture-9-lets-start-a-startup"
tag: lecture
title: "Lecture 9 - Let's Start a Startup"
---

## Homework Review

- Your AI server from L8: show one. What happened when you tried to break it?
- Sign in with Google on your multiplayer experience: show one. What do signed-out visitors see?
- Your [[Exercise - Final Project Ideas|project ideas]]: read out "They'd sign up because ___" for one. Does the room believe it?

---

## What a startup is

- A small team trying to find something people want, quickly, before the time or money runs out.
- Bengaluru examples they know: Swiggy, Zerodha, Zepto. Each started as one small thing for one group of people.
- A product is only part of it. A startup also has to answer: who is it for, how do they hear about it, why do they sign up, why do they come back?
- That's why the final project is a product *and* a landing page.

### Start small: the MVP

- **MVP** (minimum viable product): the smallest thing that tests whether people want it.
- Dropbox's first "product" was a video showing how it would work, and the sign-up list grew overnight. Back to Dropbox from L2.
- A landing page with a sign-up button is often the first MVP. If nobody signs up, you've saved months.
- For their project: what is the one flow that has to work? Everything else is "nice to have".

## Two early decisions

- Every startup decides early where the product lives (web, app, or both) and whose computer it runs on. Both change what you can build in three weeks and what it costs.

## Your site already works on a phone

- Open your own site on your phone. It's responsive (L4), it loads over the internet, it can even be on your home screen.
- Do it: **Add to Home Screen** on iOS (Share menu) or Android (Chrome menu). That's a **PWA** in its simplest form.
- So why does anyone make an app?

## Three ways to make a mobile product

- Table: **web app** vs **hybrid / cross-platform** vs **native**.
  - Examples of each from their phones (Twitter/X web, Instagram, Swiggy, Notion, Figma's mobile app, Apple Notes).
  - Rows: what it's built with, one codebase or two, reach, offline, notifications, camera and sensors, cost to build, how updates reach users.
- React Native and Flutter in one line each: one codebase that becomes two apps.
- The design angle: native apps should feel native. Back gestures, tab bars, share sheets differ between platforms.

## iOS and Android are different products

- Market share: Android dominates India, iPhone dominates the US. Who are your users?
- Device range: a few iPhone sizes vs thousands of Android phones, many of them cheap and slow (the Slow 3G throttle from Trace a Request).
- Design languages: Apple's Human Interface Guidelines vs Material Design. Same screen, both ways.

### The stores are gatekeepers

- Apple App Store vs Google Play: developer fees, review, how long it takes.
- The cut they take on payments, and why Spotify and Kindle won't let you buy inside the iOS app.
- A website ships when you push. An app ships when Apple says yes, and users update when they feel like it.
- Exercise: [[Exercise - Mobile Ecosystem Comparison]], for homework.

---

## Whose computer is it?

- Everything this semester ran on someone else's computer. List them: GitHub Pages, Firebase, Vercel, Gemini, the Anything API.
- "The cloud" is renting those computers, at different levels of "we'll handle it for you".

## IaaS, PaaS, SaaS

- Table using what they've used:
  - **IaaS**: rent a raw computer (AWS EC2, Google Cloud). You install and run everything.
  - **PaaS**: give it your code, it runs it (Vercel, where your `api/ask.js` from L8 runs).
  - **Backend as a service**: Firebase. Database and logins without a server.
  - **SaaS**: you just use the finished product (Gmail, Figma, Notion).
- The design angle: each step up is less control and less work.

## Scale and cost

- 10 users vs 10,000: what breaks first?
- Free tiers and usage pricing. Firebase and Vercel are free until they suddenly aren't.
- AI features cost per call (L8). Cost is a design constraint.
- When AWS or Cloudflare goes down, half the internet goes with it. One recent example.

> **Sidenote:** Pick an app on your phone. Guess what it runs on and what it costs them per user.

---

## The software development lifecycle

- The **SDLC** is the order software gets made in: idea → requirements → design → build → test → ship → maintain.
- Table: each stage, what comes out of it (a brief, user stories, Figma, code, bug list, a live URL), and where the designer is.
- They've been doing this every week, compressed into a few hours. Map one past exercise onto it, e.g. the weather footer.

### Waterfall vs Agile

- Table:
  - **Waterfall**: each stage finishes before the next starts. Good when requirements can't change (a bridge, a bank's core system).
  - **Agile**: go round the whole loop in small pieces, every week or two, and change course as you learn.
- Most software teams, and every startup, work in some version of Agile.
- The design angle: in Waterfall the design is "done" before build starts. In Agile you design, see it built, and redesign.

## Scrum, as you'll actually use it

- One line each, and what it means for 3 people in 3 weeks:
  - **Backlog**: the list of everything you might build, in order of importance.
  - **Sprint**: a fixed stretch of time where you build the top of the backlog. Yours are L10 and L11.
  - **Standup**: a few minutes daily: what I did, what I'm doing, what's stuck. A WhatsApp message works.
  - **Review / demo**: show what works. The studio crits.
  - **Retro**: what to change about how you work next sprint.
- **User stories**: "As a ___, I want ___, so that ___." Same idea as the "This is for ___" sentences from your project ideas.
- Must have vs nice to have. Sign-in, the core flow and the landing page are must-haves. Decide the rest now so cutting it in L10 isn't a fight.
- Where to keep the backlog: GitHub Issues on your repo, or a FigJam board. Not in someone's head.

---

## Working on one repo as a team

- L2 said merge conflicts start "the moment you are working with other people in a repo". This is that moment.
- Alone vs together table: what you did in L2 (commit, push) vs what a team does (branch, pull request, review, merge).
- **Branch**: your own copy to work on without breaking `main`.
- **Pull request**: asking to merge your branch into `main`, so a teammate can look first. Vercel gives every pull request its own preview URL.
- Live demo: two people change the same line, one merges, the other gets a conflict. Resolve it with the markers from L2.
- Habits that avoid most conflicts:
  - pull before you start
  - small commits, pushed often
  - split work by file or by page where you can
  - don't let three AI agents rewrite `index.html` at the same time
- Shared accounts: add teammates to the GitHub repo, the Vercel project and the Firebase project. Keys go in Vercel's environment variables (L8), not in the repo or the WhatsApp group.

---

## Landing pages

- The landing page's job, in about five seconds: what is this, who is it for, why should I sign up? Then one button.
- Class activity: open three landing pages (one Indian consumer app, one tool they use like Figma or Notion, one small startup). For each:
  - Time how long it takes to say what the product does.
  - Find the sign-up button. How many are there?
  - What does it show of the actual product?
- Common sections, top to bottom: headline and sign-up button, the product in screenshots or a short video, how it works in three steps, sign-up again at the bottom.
- Be honest. No fake testimonials or "trusted by 10,000 teams" when it's three friends.
- After the button: sign in (L8), then the first screen a new person sees. The landing page, sign-up and first use are one flow, and that's what you'll demo.
- Structure in the repo: the landing page at `/`, the product at `/app`. Signed-in visitors can skip straight to the app.

---

## Final project kickoff

- Walk through [[Project - Final Project]]: product with sign-in, landing page, the schedule to Demo Day, the marks.
- Pitch round: each person reads their best "This is for ___" idea. The class asks one question each.
- Form teams of up to 3, around the ideas, not just friends.
- Set up before you leave:
  - one GitHub repo with everyone as a collaborator
  - a Vercel project connected to it
  - a Firebase project with Google sign-in on and teammates added
  - a backlog, with sprint 1 and sprint 2 marked

## Homework

- **Proposal**, one page per team, before L10:
  - the problem, and who it's for
  - why they'd sign up (your landing page headline, roughly)
  - the core flow, from landing page to first use
  - a stack sketch: where data lives, how sign-in works, where it's hosted
  - your backlog, split into the two sprints
- [[Exercise - SDLC Stage Mapping]], using one feature from your own project.
- [[Exercise - Mobile Ecosystem Comparison]]
- [[Exercise - Add an AI Feature]]
