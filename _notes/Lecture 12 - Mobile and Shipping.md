---
date: 17-11-2026
date modified: 09-10-2026
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
title: "Lecture 12 - Mobile and Shipping"
---

## Project check-in

Ten days to Demo Day. Each team gets three minutes, and this time you start on a phone:

1. Open your landing page the way a stranger would, from a link.
2. Sign up, and show the first screen a new person sees.
3. Do the core thing.

Feedback follows [[Rules for Class Crits]]. Then, in your team: what's left on your must-have list, and what are you cutting? This week is your feature freeze. After it, you only fix and polish.

---

## Your site already works on a phone

Open your project on your phone. It's responsive (L4), it's on the internet, and you can put it on your home screen:

- **iPhone:** in Safari, tap **Share → Add to Home Screen**.
- **Android:** in Chrome, tap **⋮ → Add to Home screen** (sometimes **Install app**).

It gets its own icon and opens like an app. A website that does this well is called a **progressive web app** (PWA). A small file called `manifest.json`, with your app's name, icon and colours, makes it look even more like one.

So why does anyone make an app?

## Three ways to make a mobile product

| | Web app | Cross-platform app | Native app |
| --- | --- | --- | --- |
| Built with | HTML, CSS and JavaScript, like everything this semester | One codebase (React Native or Flutter) that becomes an iPhone app and an Android app | Swift for iPhone and Kotlin for Android: two separate codebases |
| Examples | Your final project | Google Pay (Flutter), Discord (React Native) | Apple's own apps, Google Maps |
| How people get it | A link | The App Store and Play Store | The App Store and Play Store |
| How updates reach people | Every push, straight away | After store review, when people update | After store review, when people update |
| Camera, notifications, working offline | Some. On iPhone, notifications only work once it's on the home screen | Most | All |
| Cost to build | One team | One team, plus some work per platform | Two teams |
| Feels like the phone | Close, if it's designed well | Close | Exactly |

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
- **Alt text** on every image that means something. A model can write a first draft (L11), but read it.
- **Text size.** `rem`, not `px` (L4). Turn up your phone's text size and look again.
- **A screen reader.** On a Mac, **⌘F5** turns VoiceOver on and off. Listen to your landing page for thirty seconds.

### Speed

- In DevTools, open **Lighthouse** and click **Analyze page load**. Read the Performance and Accessibility scores and the first few suggestions.
- Throttle to Slow 3G and reload, as in [[Exercise - Trace a Request]]. What does someone see while it loads?
- The usual cause is images: a 5 MB photo straight from your phone. Resize it before it goes in the repo.

### Security and privacy

- **Rules.** Rerun the `fetch` from [[Exercise - Hack the Wall]] against your own database. Signed out, can you write? Can you read anything you shouldn't?
- **Keys.** Search your repo on github.com for `AIza`, and check `.env` isn't there (L9).
- **Your server.** Does it turn away empty and very long requests (L11)?
- **What you collect.** List every piece of personal data you store. Do you need all of it? Who can see it? India's Digital Personal Data Protection Act (2023) expects you to collect only what you need and tell people what it's for.

### A real domain (optional)

`your-project.vercel.app` works, but a name like `hostelorders.in` is easier to say out loud on Demo Day.

1. Buy one from a domain registrar. A `.in` or `.com` costs a few hundred to a thousand rupees a year.
2. In Vercel, go to **Settings → Domains** and add it. Vercel tells you which DNS records to add at your registrar.
3. Add the new domain to Firebase's **Authorized domains**, or sign-in will fail on it.

This is DNS from [[Exercise - Trace a Request]]: you're telling the internet's address book that your name points to Vercel's computers. It can take anywhere from a few minutes to a few hours to reach everyone.

---

## Demo Day

Friday 27 November. Seven minutes per team, then three minutes of questions.

- **Start from your landing page**, the way a stranger would, and go through sign-up to the core thing.
- **Tell the story of how you made it:** what you cut, what broke, and what you'd do differently. That's the process documentation from the brief.
- **Have a backup.** Record your screen going through the whole flow, in case the Wi-Fi, a key or a quota fails on the day.
- **Practise once with a timer.** Seven minutes goes quickly.

## Homework

- Everything on your ship-ready list.
- [[Exercise - Mobile Ecosystem Comparison]], with your own product as the lens.
- Rehearse your demo.
