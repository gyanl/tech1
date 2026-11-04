---
date: 04-11-2026
date modified: 04-11-2026
feed: show
key_areas:
  - "iOS vs Android platforms"
  - "Native vs hybrid vs web apps"
  - "App stores and distribution"
  - "Accessibility"
  - "Performance"
  - "Security and privacy"
  - "DNS"
tag: lecture
title: "Lecture 11 - Mobile and Shipping"
---

## Project check-in

Each team gets three minutes:

1. Read the first line of your proposal: who it's for, and why they'd sign up.
2. Show what works, live, from your `vercel.app` URL. Sign in and do the core thing, however ugly it is.
3. Say what's stuck.

The rest of us give feedback following [[Rules for Class Crits]]. Then take five minutes in your team for a retro (L10): what will you change about how you're working for sprint 2?

Your [[Exercise - SDLC Stage Mapping]] diagrams: we'll look at two. Where's the designer, and where are they missing?

---

## Your site already works on a phone

Open your project on your phone. It's responsive (L4), it's on the internet, and you can put it on your home screen:

- **iPhone:** in Safari, tap **Share → Add to Home Screen**.
- **Android:** in Chrome, tap **⋮ → Add to Home screen** (sometimes **Install app**).

It gets its own icon and opens like an app. A website that does this well is called a **progressive web app** (PWA). A small file called `manifest.json`, with your app's name, icon and colours, makes it look even more like one.

So why does anyone make an app?

## Three ways to make a mobile product

### 1. Web app

A web app uses HTML, CSS and JavaScript, like everything this semester. Your final project is one example. People open it through a link, and updates reach them as soon as you push.

- **Cost to build:** One team.
- **Device features:** Some access to the camera, notifications and offline use. On iPhone, notifications only work once the app is on the home screen.
- **How it feels:** Close to a phone app, if it's designed well.

### 2. Cross-platform app

A cross-platform app uses one codebase, built with React Native or Flutter, to make both an iPhone app and an Android app. Examples include Google Pay (Flutter) and Discord (React Native). People download it from the App Store or Play Store. Updates reach them after store review, when they update the app.

- **Cost to build:** One team, plus some work per platform.
- **Device features:** Access to most features, including the camera, notifications and offline use.
- **How it feels:** Close to the phone's own apps.

### 3. Native app

A native app uses Swift for iPhone and Kotlin for Android, with two separate codebases. Apple's own apps and Google Maps are examples. People download it from the App Store or Play Store. Updates reach them after store review, when they update the app.

- **Cost to build:** Two teams.
- **Device features:** Full access to features such as the camera, notifications and offline use.
- **How it feels:** Like the phone's own apps.

Some things to note:

- **For a startup, the web is usually the first version.** One link in a WhatsApp group, no review, no install. Many products only become apps once people are asking for one.
- **Native apps should feel native.** The back gesture, tab bars, share sheets and where the main button goes all differ between iPhone and Android. Apple's [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/) and Google's [Material Design](https://m3.material.io) are both public. Look up the same component in both.

## iOS and Android are different products

| | iPhone (iOS) | Android |
| --- | --- | --- |
| Who makes it | Apple makes the phones and the software | Google makes the software. Samsung, Xiaomi, OnePlus and many others make the phones |
| Share of phones in India | A few percent | Well over 90% |
| Share of phones in the US | More than half | Most of the rest |
| Range of devices | A handful of sizes, mostly recent | Thousands, from ₹7,000 phones to foldables |
| Design guidelines | Human Interface Guidelines | Material Design |

Who are your users? A product for Indian college students that only works well on an iPhone has picked a very small audience. Test on a cheap Android phone, and on Slow 3G ([[Exercise - Trace a Request]]).

### The stores are gatekeepers

| | Apple App Store | Google Play |
| --- | --- | --- |
| Cost to publish | $99 a year | $25, once |
| Review | Every update is reviewed by people, usually within a day or two | Mostly automated, usually faster |
| Cut of in-app payments | 15–30% | 15–30% |

Some things to note:

- **That cut is a design constraint.** It's why Netflix and Spotify have you pay on their websites rather than inside their iPhone apps.
- **A website ships when you push. An app ships when Apple says yes**, and reaches people when they update. A one-line bug fix can take days.
- **The stores also decide what's allowed.** Sign in with Apple, from L8, keeps appearing because of Apple's rules.

> **Sidenote:** Which apps on your phone could have been websites? Which ones really needed to be apps?

---

## Ship-ready

Most student projects skip this part, and most real products don't. In your team, go through each list on your own project and write down everything that fails. That list is your work until Demo Day.

### Accessibility

- **Contrast.** Body text needs a contrast ratio of at least 4.5:1 against its background. Inspect some text in DevTools and click its colour swatch to see the ratio. Check dark mode too (L3).
- **Keyboard.** Put the mouse away and use Tab and Enter. Can you sign up and do the core thing? Can you always see where you are?
- **Alt text** on every image that means something. A model can write a first draft, but read it.
- **Text size.** `rem`, not `px` (L4). Turn up your phone's text size and look again.
- **A screen reader.** On a Mac, **⌘F5** turns VoiceOver on and off. Listen to your landing page for thirty seconds.

### Security and privacy

- **Rules.** Rerun the `fetch` from [[Exercise - Hack the Wall]] against your own database. Signed out, can you write? Can you read anything you shouldn't?
- **Keys.** Search your repo on github.com for `AIza`, and check `.env` isn't there (L9).
- **Your server.** Does it turn away empty and very long requests? We'll try to break these in L12.
- **What you collect.** List every piece of personal data you store. Do you need all of it? Who can see it? India's Digital Personal Data Protection Act (2023) expects you to collect only what you need and tell people what it's for.

### A real domain (optional)

`your-project.vercel.app` works, but a name like `hostelorders.in` is easier to say out loud on Demo Day.

1. Buy one from a domain registrar. A `.in` or `.com` costs a few hundred to a thousand rupees a year.
2. In Vercel, go to **Settings → Domains** and add it. Vercel tells you which DNS records to add at your registrar.
3. Add the new domain to Firebase's **Authorized domains**, or sign-in will fail on it.

This is DNS from [[Exercise - Trace a Request]]: you're telling the internet's address book that your name points to Vercel's computers. It can take anywhere from a few minutes to a few hours to reach everyone.

## Homework

- **Sprint 2:** your landing page, everything on your must-have list working, and your ship-ready list.
- [[Exercise - Mobile Ecosystem Comparison]], with your own product as the lens.
