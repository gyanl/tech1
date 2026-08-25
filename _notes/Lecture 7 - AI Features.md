---
date: 29-09-2026
date modified: 25-08-2026
feed: show
key_areas:
  - "LLM APIs"
  - "AI features in products"
  - "AI-assisted development"
  - "Prompting as design"
tag: lecture
title: "Lecture 7 - AI Features"
---

## Recap

You've used AI to *build* every week of this course. Today it becomes an ingredient **inside** the thing you're building — a feature your users touch, not a tool you use in private.

The good news is you already know how. In [[Lecture 5 - Databases and APIs]] you learned that an API is a counter with a menu, that `fetch` is how you order from it, and that JSON is what comes back. An AI API is that same counter. The menu just has stranger items on it.

## What a language model actually is

A model is not a database and it is not a search engine. It has no table of facts to look things up in. It is a very large statistical machine that, given some text, predicts what text plausibly comes next — and then does that again, and again, one chunk at a time.

Everything odd about them follows from that one sentence:

- **They make things up.** Not as a malfunction — a plausible-sounding citation *is* the correct output of a plausibility machine. The model has no mechanism for knowing it doesn't know.
- **They're good at shape, bad at truth.** Ask for a polite refusal email and it will be excellent. Ask for last quarter's revenue and it will be confident and possibly fictional.
- **They can't count reliably, or do arithmetic**, for the same reason. Text prediction is the wrong tool.
- **They have a cutoff.** The model learned from text up to some date and knows nothing after it, including your product.

> **Sidenote:** "Hallucination" is a bad word for this — it implies a fault. The model is doing exactly what it does. The design failure is ours, when we put its output where a fact was required.

### What that means for you as a designer

| Good use of a model | Bad use of a model |
| --- | --- |
| Rewriting, summarising, tone-shifting | Anything where being wrong is expensive |
| Classifying, tagging, extracting | Arithmetic, counting, totals |
| Drafting, brainstorming, first passes | Facts about your own product or data |
| Turning messy input into structured output | Anything the user can't check at a glance |

The reliable pattern: **the model transforms text the user already has, and the user can see whether it worked.** The unreliable pattern: the model is the source of truth.

## The call is just `fetch`

Here's the whole thing. It's the same three moves from week five.

```js
const response = await fetch(
  "https://generativelanguage.googleapis.com/v1beta/models/MODEL-NAME:generateContent",
  {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "x-goog-api-key": KEY
    },
    body: JSON.stringify({
      systemInstruction: {
        parts: [{ text: "You are a blunt, funny museum guide. Two sentences maximum." }]
      },
      contents: [
        { parts: [{ text: userQuestion }] }
      ]
    })
  }
);

const data = await response.json();
const answer = data.candidates[0].content.parts[0].text;
```

Compare it to the weather API from L5 and the difference is small: it's a `POST` instead of a `GET`, because you're sending something substantial rather than just asking. The reply is JSON, and you dig the text out of it with the same dot-notation you used for `data.temp`.

> **Get the current model name from [aistudio.google.com](https://aistudio.google.com) and paste it in.** Model names change every few months and anything printed on a slide is out of date by the time you read it. This is true of every provider — checking the docs for the current model id is part of the job, not a sign you've forgotten something.

### Every provider looks like this

OpenAI, Anthropic and Google all take a system instruction, a list of messages, and return text. The field names differ; the shape does not.

```js
// OpenAI's version of the same idea
body: JSON.stringify({
  model: "MODEL-NAME",
  messages: [
    { role: "system", content: "You are a blunt, funny museum guide." },
    { role: "user",   content: userQuestion }
  ]
})
```

Learn one and you can read all of them. Switching providers is an afternoon, not a rewrite — worth remembering when someone tells you their startup is built *on* a particular model.

### The system prompt is a design artifact

That `systemInstruction` is not a technical setting. It's a spec, in English, for how your product speaks:

> "You are a blunt, funny museum guide. Two sentences maximum. Never invent a date — if you don't know when something was made, say so."

Tone, length, format, and what to do when it doesn't know. That's voice-and-tone guidelines, a content style guide, and an error-handling spec, in one paragraph — every one of them a design decision, and one you can actually write yourself. Draft it in a doc, iterate on it like copy, and keep the versions.

## Three things that make this API weird

Everything you've called until now behaved predictably. This one doesn't, in three specific ways you have to design around.

### 1. The same input gives different output

Ask twice, get two different answers. Every other API in this course is deterministic — `GET /posts/42` returns post 42 forever. A model is sampling from possibilities.

So: you cannot test it by checking it matches an expected string, you cannot promise a user the same result twice, and **anything that must be consistent has to be pinned down by you**, not hoped for. If you need JSON back in a fixed shape, ask for it explicitly and validate what arrives — the model will occasionally wrap it in an apology.

### 2. It's slow, and the slowness is visible

A database read is tens of milliseconds. A model reply is a few seconds — long enough that a spinner is not an acceptable answer.

This is why every AI product you use streams text as it's generated. It isn't a flourish; it's the only way to make a five-second wait feel like it started immediately. If you're not streaming, you need something else honest in that gap — and "nothing happens for four seconds" is how users conclude your button is broken and click it six more times.

### 3. It costs money per use

You're billed by **tokens** — roughly, chunks of text — counted on both what you send and what comes back. A token is about ¾ of a word.

This is new for you. Every design decision you've made so far has been free to repeat. Now:

- A long system prompt is paid for on **every single call**.
- Sending the whole conversation back for context — which is how a model "remembers" — means each turn costs more than the last.
- A feature that fires on every keystroke is a bill. One that fires on a button press is a rounding error.

> **Sidenote:** This is the first time in this course that a design choice has a per-use price tag. Get used to it — "how often does this run?" becomes a question you'll be asked in every product meeting for the rest of your career.

## About that key

Here's the tension. Your Firebase config could sit in your HTML because it's an address, protected by rules. **An API key is not an address. It's a bearer token — whoever holds it can spend on your behalf.** Your repo is public, View Source is one click, and there are bots scanning GitHub for keys around the clock.

**The correct pattern** is that the key lives on a server and your page talks to *your* server, which talks to the model. That's the missing box from L5's round trip, back where it belongs — and it's what you'd do at work.

**What we're doing today, deliberately:**

1. Get a free key from [Google AI Studio](https://aistudio.google.com/apikey). **Do not add a billing account.** A free-tier key with no card attached can burn through a quota; it cannot generate a bill.
2. Put it in a **separate, throwaway repo**. Not your portfolio, not your final project.
3. When the exercise is marked, **revoke the key** in AI Studio. Not delete the commit — revoke the key. You know from week two that the commit is in the history forever.

We're taking the shortcut because a serverless proxy is a whole other deployment target and you've got enough new things this month. It is a shortcut, it is scoped to a throwaway project with a key that can't cost you anything, and it is not how you'd ship this.

> If your final project has an AI feature in it, come and talk to me about doing the key properly. It's about fifteen lines and one free Vercel deploy.

## Designing the feature, not the demo

The technology is a day's work. The design is the hard part, and it's yours.

### Is it better *because* it's AI?

Write the feature as one sentence before you write any code:

> "When the user ___, the model ___, so that ___."

If the third blank is weak, the feature is decoration. Most bad AI features are a text box bolted onto a product that didn't need one — a chatbot where a dropdown was faster, a summary of six items the user could just read.

The strong ones are usually invisible: a thing that was tedious becomes automatic, and there's no chat interface anywhere.

### Design the failure states

The model will be slow, wrong, weird, or unavailable. Those aren't edge cases here — they're the normal operating range, and specifying them is the actual design work:

- **Slow** — stream it, or say something true about what's happening.
- **Wrong** — can the user tell? Can they edit it, regenerate, or undo? Never let model output be the last word on something that matters.
- **Refuses or returns nothing** — what's on screen? "undefined" is not a design.
- **Down** — does your whole product break, or just this feature?

### Tell people it's a model

Users should know when they're reading generated text. Not as legal cover — because it changes how carefully they read, which is exactly the behaviour you want. Quiet, consistent, not an apology.

## Class Activity

Two parts, and do them in this order.

**First, no code.** Open [aistudio.google.com](https://aistudio.google.com) and get a model to do something for your page — summarise your guestbook, rewrite your bio in three tones, generate alt text for your images. Get the *system prompt* good before any of it goes near an editor. Change one instruction, run it again, notice what moved.

**Then wire it up.** New repo, free key, the `fetch` above. Get one thing on a page that a person can type into and get an answer from.

Then break it: type nonsense, type in another language, type nothing at all, type a thousand words, ask it to ignore its instructions. Screenshot what happens.

## Homework

- **Exercise:** [[Exercise - Add an AI Feature]] — one genuinely useful AI feature, its system prompt as a written artifact, and its failure states designed.
- Revoke your key when you're done.
- Bring one AI feature you've used in a real product that you think is bad, and be ready to say what it should have been instead.
