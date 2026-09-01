---
date: 06-10-2026
date modified: 25-08-2026
feed: show
key_areas:
  - "iOS vs Android platforms"
  - "Native vs hybrid vs web apps"
  - "App stores and distribution"
  - "IaaS, PaaS, SaaS"
  - "Scaling and cost"
tag: lecture
title: "Lecture 8 - Mobile and the Cloud"
---

## Recap

Two loose ends to tie off before the final project, and they're both about *where your product actually lives*.

You've built a site that reshapes itself for a phone ([[Lecture 4 - Units and Responsiveness]]), remembers things ([[Lecture 5 - APIs]]), and can call a model ([[Lecture 7 - AI Features]]). It runs on machines you've never seen, in places you've never chosen.

So: **if your site already works on a phone, why do apps exist?** And **whose computers is all of this running on?**

# Part 1 — Mobile

## Your site already works on a phone

Genuinely — open your github.io URL on your phone. It's responsive, it's on the internet, anyone can reach it, and it cost nothing to distribute. That's a real mobile product.

So the question isn't "web or app," it's **what do you get for the enormous extra cost of an app**, and is it worth it for *this* product? That's a decision you will be in the room for, so let's make it properly.

## Three ways to make a mobile product

| | **Native** | **Cross-platform** | **Web / PWA** |
| --- | --- | --- | --- |
| Written in | Swift (iOS), Kotlin (Android) | React Native, Flutter | HTML/CSS/JS — what you know |
| Codebases | **Two** | One | One |
| Feels like the platform | Completely | Mostly | Not really |
| Full device access | Yes | Most | Limited |
| Distribution | App stores | App stores | A URL |
| Updates | Store review, then users update | Store review | You push; everyone has it |
| Cost | Highest | Middle | Lowest |

**Native** is two teams, two codebases, two release cycles, and it's still the right answer when the product *is* the interaction — a camera app, a game, anything that must feel perfect.

**Cross-platform** is the common commercial compromise. One team, both stores, a small tax in fidelity and a large saving in money. Most apps on your phone that aren't made by giants are built this way.

**Web** reaches everyone instantly, costs the least, updates in seconds, and can't do a handful of things that matter.

> **Sidenote:** Notice how much of this table is about *organisational* cost, not technical capability. "Which platform" is usually a budget and staffing decision wearing a technology costume. Knowing that is most of what makes you useful in the meeting.

### PWAs: when a website pretends to be an app

A **Progressive Web App** is your website plus two extra files: a **manifest** (name, icon, colours, how it should launch) and a **service worker** (a script that can cache files and serve them offline).

Add those and your site can be installed to the home screen, launched with its own icon, and open without browser chrome. Most people can't tell.

You are one afternoon away from this with what you already have. We'll do the install in class.

Where it stops:

- **Push notifications on iOS** are limited and arrived late and grudgingly.
- **No store presence.** Nobody discovers you by browsing. You need a URL in front of people some other way.
- **Deep hardware access** — bluetooth, background location, health data — is patchy to absent.
- **Users don't know they can.** "Add to Home Screen" is buried in a share sheet, which is a distribution problem no amount of design fixes.

## iOS and Android are different products

Not just two skins on the same job. They differ in ways that change what you should design.

**Design language.** Apple's **Human Interface Guidelines** and Google's **Material Design** disagree about navigation, tab bars, back behaviour, typography and motion. Android has a system back gesture; iOS doesn't, so iOS apps carry their own back affordance. Ship one design to both and it will feel subtly wrong on one of them — and users won't be able to say why, only that it's off.

**Device diversity.** iOS is a handful of screen sizes from one company. Android is thousands of devices across a decade of hardware, at every price point. Your beautiful design has to survive a cheap phone with a small screen and an old browser — which is, incidentally, the same discipline as the responsive work in L4, just with less forgiving hardware.

**Audience.** Market share differs enormously by country, and so does spending: iOS users historically pay more per head, Android reaches far more people, and which of those matters depends entirely on where your users are and how you make money. Look it up for *your* market rather than repeating what an American tech blog said.

### The stores are gatekeepers

This is the part designers underestimate.

- **Review.** A human (and increasingly a model) checks your app against a rulebook before it reaches anyone. It can be rejected — for a policy you missed, a permission you didn't justify, a subscription flow they don't like.
- **Fees.** Stores take a cut of purchases made through them. There are reduced rates for small developers and it has been the subject of years of litigation and regulation, so check current numbers rather than trusting the figure you half-remember.
- **You can be removed.** Your entire distribution channel belongs to someone else, and they can close it.

Compare that to your github.io URL, which nobody approved and nobody can take down. That's the actual trade: **reach and credibility in exchange for permission.**

> **Sidenote:** Update speed is a design constraint people forget. On the web you can fix a confusing label at 2pm and everyone has it at 2:01. In an app, that fix waits for review, and then for users to update — some of whom never will. Design accordingly.

# Part 2 — The Cloud

## "Someone else's computer" — but which one?

You've been using the cloud all semester without calling it that. Everything you've built runs on hardware owned by someone else, and you've already touched three different *layers* of that.

| Layer | You get | You still handle | You've used |
| --- | --- | --- | --- |
| **IaaS** | A bare machine | OS, runtime, server, scaling, security | — |
| **PaaS** | "Here's my code, run it" | Your code | GitHub Pages, Vercel |
| **BaaS** | A ready-made back-end | Your data model and rules | Firebase |
| **SaaS** | A finished product, via API or UI | Nothing | AI Studio, Figma, Slack |

Each step up trades control for convenience, and money for time. The whole industry has been drifting up this table for twenty years, because engineers are more expensive than servers.

**Where your semester actually runs:** your HTML and CSS sit on GitHub's servers (PaaS). Your class wall data sits in a Google datacentre (BaaS). Your AI feature runs on Google's machines and answers over an API (SaaS). You wrote none of the infrastructure and you own none of the hardware — which is exactly why a class of designers could ship all three.

## Scale: 10 users to 10,000

Your class wall works beautifully for thirty people. What breaks at ten thousand?

Mostly, not what you'd guess. The page itself is fine — static files are cheap and a CDN copies them near everyone. What strains is everything with state: simultaneous database connections, bytes downloaded, and API calls.

Remember the two rules from L5 — keep the tree shallow, because reading a path downloads everything under it. At thirty users that's a style note. At ten thousand it's the bill.

**Vertical scaling** is a bigger machine, and it's simple until you hit the biggest machine. **Horizontal scaling** is more machines with something distributing work between them, and it's how everything large actually works. Managed platforms do this for you, which is most of what you're paying them for.

## Cost is a design constraint

This is the through-line of the last four weeks, and it's the thing that makes you different from a designer who's never seen a bill:

- **L5** — you pay for bytes downloaded and connections held. *Data shape is a cost decision.*
- **L7** — you pay per token, on the way in and the way out. *How often a feature runs is a cost decision.*
- **Today** — free tiers end, and usage pricing has no ceiling by default.

Free tiers are generous and real; build on them without embarrassment. But know where the edge is, and know what happens when you cross it — some services degrade, some bill you, and a badly-designed feature that fires on every keystroke can produce a genuinely alarming invoice overnight. Set spend limits before you need them.

> **Sidenote:** "How often does this run?" is the single most valuable question you can ask in a product meeting once there's usage pricing anywhere in the stack. Very few designers ask it. Be one who does.

## When the cloud goes down

Concentration is the hidden risk. A handful of providers host a large fraction of the internet, so when one has a bad morning, thousands of unrelated products fail together — including, often, the status page meant to tell you about it.

You can't engineer around that at your scale. But you can notice that "we're down" and "our provider is down" are different conversations, and that a product which fails *gracefully* — cached content, an honest message, a degraded but working core — is a design achievement, not an engineering one.

## Class Activity

**Install your own site.** Add a manifest and an icon to your page, push it, then open the site on your phone and add it to your home screen. Launch it from there. Discuss: what feels app-like now, and what immediately gives it away?

**Map a stack.** In pairs, pick a well-known product and work out what it's built on — where the files are served from, where the data lives, what it calls out to. Then do the same for your own final project idea, and mark which layer of the table above each piece sits in.

## Homework

- **Exercise:** [[Exercise - Mobile Ecosystem Comparison]] — iOS vs Android for a specific product, with a recommendation you can defend.
- Come to [[Lecture 10 - Start a Startup]] with **1–2 final project ideas** and who you'd like to work with. Teams and topics get settled that week, so arrive with an opinion.
