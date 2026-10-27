---
date: 27-10-2026
date modified: 27-10-2026
feed: show
key_areas:
  - "Landing pages"
  - "Software development lifecycle"
  - "Agile / Scrum"
  - "Version control (Git)"
slug: "lecture-10-lets-start-a-startup"
tag: lecture
title: "Lecture 10 - Let's Start a Startup"
---

## Homework Review

- Vercel deployed sites
- Discuss Final project teams and your startup ideas

---

## Landing pages

A **landing page** is the first page someone sees when they look up your product. Its job is to get the right people to sign up.

In a few seconds, the visitor needs to know:

1. What is this?
2. Is it for me?
3. What do I do next?

### Class Activity: take apart some landing pages

In pairs, open three landing pages: one Indian consumer app (Swiggy, Zepto, CRED), one tool you use (Figma, Notion, Linear), and one small startup you've never heard of. For each one:

- Say what the product does, out loud, in one sentence. How long did it take you to be able to?
- Find the sign-up button. How many are there on the page?
- What does it show you of the actual product: screenshots, a video, nothing?
- Scroll to the bottom. What's there?

> **Sidenote:** Which one did you understand fastest? What did it do that the others didn't?

### What's usually on one

| Section                     | What it does                                                      | For your project                                           |
| --------------------------- | ----------------------------------------------------------------- | ---------------------------------------------------------- |
| Headline and sign-up button | Says what it is and who it's for, in one line                     | Your "They'd sign up because ___", rewritten as a headline |
| The product                 | Screenshots or a short video, so people see it before they commit | Screenshots of your core flow                              |
| How it works                | Three steps, each with a picture                                  | Landing page, sign in, first use                           |
| Sign-up again               | For the people who scrolled to the end                            | The same button                                            |

Some things to note:

**What is your Call to Action?**
What is the one thing your landing page wants a visitor to do? There should usually be a button for this action in the first fold of the page.
"Sign in with Google" can be your sign-up button.

**Be honest.**
No fake testimonials, and no "trusted by 10,000 teams" when it's you and two friends. A real quote from one of the three people who tried it is better anyway.

**Design it for mobile and desktop**
Many people will open your link from WhatsApp.

**The landing page is the start of a flow.**
After the button comes sign-in (L8), then the first screen a new person sees, before they've added anything. That whole flow is what you'll demo.

### Landing page and app in one repo

Keep the landing page at `/` and the product at `/app/`:
If someone is signed in, send them straight to the app.

```text
index.html        ← the landing page
app/index.html    ← the product, for signed-in people
api/              ← your servers (L9)
```

People who are already signed in don't need to see the landing page again. On the landing page:

```js
onAuthStateChanged(auth, (user) => {
  if (user) window.location.href = "/app/";
});
```

---

## How software gets made

The **software development lifecycle** (SDLC) is the order software gets made in. Every team goes through these stages, whether or not they call them that:

| Stage | What happens | What comes out | Where the designer is |
| --- | --- | --- | --- |
| Idea | Someone notices a problem | One sentence: "This is for ___" | Often the one who noticed |
| Requirements | Decide what it must do | User stories, a list of must-haves | Talking to the people it's for |
| Design | Decide how it works and looks | Flows, screens in Figma | Leading |
| Build | Write the code | A working version | Checking it matches, adjusting |
| Test | Find what's broken or confusing | A bug list | Watching real people use it |
| Ship | Put it live | A URL, a store listing | Checking the live version |
| Maintain | Fix, improve, repeat | Updates | Watching how it's actually used |

You've been doing this every week, just very quickly. The weather footer in L5 was an idea, a design, a build with AI, a test on your phone, and ship to Github Pages.

## What's a startup?

A startup is a newly formed, temporary business or project launched by an entrepreneur to search for, develop, and validate a repeatable, scalable business model.

Startups rely on the idea that a small, highly motivated team can frequently be more flexible, try more radical ideas, and iterate faster to achieve great outcomes compared to a larger organisation.

A successful startup is one that finds Product Market Fit (PMF). This means that you have made something that solves a problem or fulfils a real need that people have, and they want to use your product.

The design process recommends talking to users as a first step before any prototyping, and many successful startups stay tightly in communication with their customers.

### Waterfall vs Agile

There are two broad ways to go through those stages:

| | Waterfall | Agile |
| --- | --- | --- |
| How it goes | Each stage finishes before the next one starts | Go round the whole loop in small pieces, every week or two |
| When it works | The requirements can't change: a bridge, a bank's core system | You're still finding out what people want |
| Design | Finished before the build starts | Designed, built, tried, redesigned |
| If you got it wrong | You find out at the end | You find out next week |

Almost every startup works in some version of Agile, because most of what a startup does is find out what it got wrong.

## Scrum, for three people in four weeks

**Scrum** is the most common way of doing Agile. Most of it is designed for teams of ten. This is the part that's useful for three:

| Term | What it is | For your project |
| --- | --- | --- |
| **Backlog** | Everything you might build, in order of importance | A list in GitHub Issues or FigJam, not in someone's head |
| **Sprint** | A fixed stretch of time where you build the top of the backlog | Two: today to L11, and L11 to L12 |
| **Standup** | A few minutes: what I did, what I'm doing next, what's stuck | A message in your team's WhatsApp group each day |
| **Review** | Show what works | The check-ins at the start of L11 and L12 |
| **Retro** | What to change about how you work together | Five minutes after each check-in |

Write the backlog as **user stories**:

> As a ___, I want to ___, so that ___.

"As a hostel resident, I want to see who's ordering dinner tonight, so that I can join their order." It's the same idea as your "This is for ___" sentences, broken into pieces small enough to build in a day.

Then split the backlog into **must have** and **nice to have**. Sign-in, the core flow and the landing page are must-haves for every team. Decide the rest today, together, so that cutting something in L11 isn't an argument.

## Estimating time

Once you have a backlog, someone will ask "how long will this take?" Every team gets this wrong, including teams of very experienced engineers. It helps to know why.

**You're estimating something you haven't done before.**

If you'd built this exact thing already, you'd just reuse it. A new product is mostly new problems, and you can't time a problem you haven't met yet.

**The last 10% takes the longest.**

Getting sign-in to work on your laptop takes an hour. Getting it to work on your teammate's phone, on the `vercel.app` domain, with the right errors and edge cases when someone cancels the Google popup, takes the rest of the day.

**AI makes the first version fast, and you only estimate the parts you can see.**

An agent can give you a working core flow in twenty minutes, and that makes it feel like the whole project will take an afternoon. As designers, you'll think of the screens. You won't think of the empty state, the loading state, what happens with no internet, or the hour you lose to a key missing from `.env`.

**Other people's time is the hardest part.**

Waiting for a teammate's pull request, or for users to try your app and give feedback, doesn't show up in anyone's estimate.

> **Sidenote:** Think of a design project where you ran out of time. What did you not see coming?

---

## Working on one repo as a team

In L2 I said merge conflicts start "the moment you are working with other people in a repo". This is that moment.

| | Alone (since L2) | As a team |
| --- | --- | --- |
| Where you work | On `main` | On your own branch |
| Saving | Commit | Commit |
| Sharing | Push to `main` | Push your branch and open a pull request |
| Going live | Every push | When a pull request is merged into `main` |

- A **branch** is your own copy of the project, where you can work without breaking `main`. In GitHub Desktop: **Current Branch → New Branch**.
- A **pull request** asks to merge your branch into `main`, so a teammate can look at it first. After you push a branch, GitHub Desktop shows a **Create Pull Request** button.
- **Vercel deploys every branch to its own preview URL**, and posts the link on the pull request. Your teammate can try your change on their phone before it goes live.
- On the free tier, Vercel deploys automatically from the **main** branch, but only when the Github commit is from the same email ID as the Vercel account. 

### Habits that avoid most conflicts

- **Pull before you start**, every time you sit down to work.
- **Small commits, pushed often.** A day's work in one commit is a day's work to untangle.
- **Split the work by file or by page** where you can: one person on the landing page, one on the app, one on the server.

### Shared accounts and keys

- **GitHub:** add your teammates under the repo's **Settings → Collaborators**.
- **Vercel:** the free plan is for one person, so one of you owns the Vercel project. Everyone else still gets a preview link on every pull request.
- **Firebase:** add teammates under **Project settings → Users and permissions**.
- **Keys:** each person keeps their own `.env`. Never share keys in the WhatsApp group. The `.env.example` from L9 tells a teammate which names they need.

---

## Final project kickoff

Open [[Project - Final Project]]. We'll go through it together: a product people sign in to, a landing page that gets them to sign up, check-ins at L11 and L12, and Demo Day on Friday 27 November.

### Pitch round

Everyone reads their best idea, in the form from [[Exercise - Final Project Ideas]]:

```text
This is for ___, who currently ___.
It lets them ___.
They'd sign up because ___.
```

The class gets one question per idea. Write down the ones you'd want to work on.

### Set up before you leave

- One GitHub repo, made from [web-starter](https://github.com/gyanl/web-starter), with everyone as a collaborator
- A Vercel project connected to it, with your keys added
- A Firebase project with Google sign-in on, your `vercel.app` domain authorised, and your teammates added

## Homework

- **Proposal**, one page per team, before L11:
  - the problem, and who it's for
  - why they'd sign up (roughly your landing page headline)
  - the core flow, from landing page to first use
  - a stack sketch: where the data lives, how sign-in works, where it's hosted, which keys you need
  - your backlog, split into the two sprints
- **Sprint 1:** sign-in and the core flow working end to end, however ugly.
- [[Exercise - SDLC Stage Mapping]], using one feature from your own project.

### Prompts for checking your idea

Before you write the proposal, ask an AI (Claude, ChatGPT, Gemini) whether your idea can be built in four weeks, and with what. Paste in your pitch from the pitch round first, then try these:

**Is it feasible?**

```text
Here's my product idea: [paste your pitch].
I'm a design student with a team of 3. We have 4 weeks, and we build
with AI help, using plain HTML, CSS and JavaScript.
What's the hardest part to build? What would you cut to make it
possible in 4 weeks? What's the smallest version that still
proves people want it?
```

**What stack would it use?**

```text
So far we've used: GitHub and GitHub Pages, Vercel (with serverless
functions in an api/ folder), Firebase Realtime Database and Firebase
Google sign-in, Sarvam's API (we have Rs. 100 of free credits), and Jev.
For my idea, tell me where the data lives, how sign-in works, where it's
hosted, and which API keys we need. Only add a new tool if none of these
can do the job, and tell me why.
```

**What will I underestimate?**

```text
Here's my core flow: [landing page → sign in → first use, step by step].
List everything I'll need to build that isn't on a screen in my design:
states, errors, permissions, data rules. Mark which ones are must-haves.
```

**Break it into stories**

```text
Turn this idea into user stories ("As a ___, I want to ___, so that ___"),
each small enough for one person to build in a day.
Split them into must have and nice to have.
```

Some things to note:

- Push back on the answers. If it suggests React, a database you haven't used, or "a simple machine learning model", ask whether the tools above could do it instead.
- AI is optimistic about time, for the same reasons you are. Treat its estimates as the low end of the range.
- Feasible to build is not the same as people wanting it. Only the people it's for can tell you that.

### Things you might want to look up

Depending on your idea, some of these will come up. Ask AI to explain them in the context of your project, the same way you did with the prompts above.

| If your idea needs… | Look up |
| --- | --- |
| Data only the signed-in person can see | Firebase Realtime Database security rules, using `auth.uid` |
| A list that updates for everyone at once | Firebase `onValue` listeners (you used these in L6) |
| Images or files people upload | Firebase Storage, or Cloudinary |
| AI that writes, translates or speaks Indian languages | Sarvam's text, translation and text-to-speech APIs, and how fast Rs. 100 of credits runs out |
| AI that picks from options you designed | Jev's `choice`, `boolean` and `score` questions |
| Keeping a key off the page | Vercel environment variables and serverless functions (L9) |
| Something that happens at a set time, like a daily reminder | Vercel cron jobs |
| Sending an email or WhatsApp message | Resend for email; the WhatsApp Business API (slow to get approved) |
| Payments | Razorpay test mode, and what it takes to go live |
| Maps or location | The Google Maps JavaScript API, or Leaflet with OpenStreetMap |
| Working on phones like an app | Progressive Web Apps (PWA), "Add to Home Screen" |
| Your own domain instead of `vercel.app` | Adding a custom domain on Vercel, and adding it to Firebase's authorised domains |
| Knowing if anyone uses it | Vercel Analytics, or Google Analytics |
