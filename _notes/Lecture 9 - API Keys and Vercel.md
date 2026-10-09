---
date: 13-10-2026
date modified: 09-10-2026
feed: show
key_areas:
  - "API keys and environment variables"
  - "LLM APIs"
  - "Serverless functions"
  - "Hosting and deployment"
  - "Startups and MVPs"
tag: lecture
title: "Lecture 9 - API Keys and Vercel"
---

## Homework Review

- [[Exercise - Sign in with Google]]: show one. What do signed-out visitors see?
- Your [[Exercise - Final Project Ideas|project ideas]]: read out "They'd sign up because ___" for one. Does the room believe it?

---

## API keys: how a program proves who it is

- Sign-in is for people. When your server asks Jev/Gemini for an answer, there's no person to sign in, so the program shows a **key** instead. Back to "How API keys work" in L5.
- In the three kinds of proof from L8, a key is "something you know", for a program. Whoever has it *is* you as far as Google is concerned. No second factor, no "was this you?" email.
- So keeping it secret is its only protection. Google trusts the key, and it's your job to make sure only your server has it.
- Where it can and can't live:

| Where | Safe? |
| --- | --- |
| In your page or `scripts.js` | No. Anyone can View Source (L5). |
| Committed to your repo | No. Bots scan GitHub, and history keeps it after you delete it. |
| Pasted into a chat with your AI agent | No. It's sent to the AI company and can end up in your code. |
| In `.env` on your laptop, ignored by Git | Yes |
| In Vercel's environment variables | Yes |

- Tell your agent the key's **name** (`GEMINI_API_KEY`), never its value.
- If it leaks, delete it and make a new one. Unlike your Google password, a key takes a minute to replace, so don't hesitate.
- We'll put all of this into practice today, with two real keys.

## Where does the key go?

L7 ended with Jev picking your theme, and one problem: every model API needs a key. In L5 we said a key in your front-end code is a key you've published. But in L6 your Firebase config sat in your HTML and that was fine. What's the difference?

| | Firebase config | Model API key |
| --- | --- | --- |
| What it is | An address: which database to use | A password that spends your money |
| What protects you | Your database rules | Nothing, once someone has it |
| Safe in your page? | Yes | No |

So the key has to live somewhere visitors can't read: a **server**. Your page asks your server, and your server asks the model. It's the round trip from L5 with a model where the database was:

```text
   BROWSER                    YOUR SERVER                 MODEL
   (their phone)              (holds the key)             (Google's computer)

   types a question ───────▶  adds the system prompt ───▶ writes an answer
                              and the key                        │
   sees the answer  ◀──────── sends back JSON ◀────────────────┘
```

Visitors never see the key or your system prompt.

You don't have to rent a computer for this. On [Vercel](https://vercel.com), a JavaScript file in a folder called `api` becomes server code: `api/ask.js` in your repo runs at `your-project.vercel.app/api/ask`. This is called a **serverless function**. There is a server, but Vercel looks after it.

The key goes in an **environment variable**, a value you type into Vercel's dashboard. Your server code can read it, and it never goes in your repo. The Anything API reads its key with `process.env.ANTHROPIC_API_KEY`.

## On your laptop: `.env`

- The live site reads keys from Vercel. But you, and the AI agent you build with, need them on your laptop too, to test before you push.
- They go in a file called **`.env`**: one key per line, `NAME=value`. Your server code reads it with the same `process.env.NAME` it uses on Vercel.
- **`.gitignore`** tells Git to pretend `.env` doesn't exist, so it never reaches GitHub. Make `.gitignore` first, before the key exists.
- You make `.env` yourself, in your editor, and paste the key into it. Not through your agent.
- Tell your agent only the key's name. "My key is in `.env` as `GEMINI_API_KEY`. Don't open or print `.env`."
- Before every commit, look at GitHub Desktop's list of changed files. `.env` should never be there.
- The full version, step by step: [[Exercise - Keep Your Keys Out of Git]].

## Class Activity: your own AI server

You'll make a page with one text box. It sends a question to your server, your server asks Gemini, and the answer comes back. The key lives in `.env` on your laptop and in Vercel, and never reaches the browser or GitHub.

### 1. Get a free key

1. Go to [aistudio.google.com/apikey](https://aistudio.google.com/apikey) and click **Create API key**.
2. Don't add a billing account. Without one, the worst case is hitting the day's free limit. You can't get a bill.
3. Don't paste it into your code, the class group, or a chat with your AI agent. It goes into `.env` in step 3.
4. Copy the exact name of the model you used in AI Studio. Model names change every few months, so take it from there, not from these notes.

On the free tier, Google may use what you send to improve its products. Don't send anything private, yours or anyone else's.

### 2. Make a repo

Create a new repo from [web-starter](https://github.com/gyanl/web-starter), like in [[Lecture 1 - Welcome to Tech1]]. Call it something like `ask-me` and clone it. This will be your first project on Vercel.

### 3. Keep the key in `.env`

1. In the top folder of the repo, make `.gitignore`:

```text
.env
.env.local
.vercel
```

2. Next to it, make `.env` by hand and paste your key in. No quotes, no spaces around the `=`:

```text
GEMINI_API_KEY=paste-your-key-here
```

3. Open GitHub Desktop. `.gitignore` should be in the list of changes, and `.env` shouldn't. Commit `.gitignore`.

Files starting with a dot are hidden in Finder. Press **⌘⇧.** to see them.

### 4. Add the server

Make a folder called `api` with a file called `ask.js` inside it:

```js
// This file runs on Vercel's computer, never in the visitor's browser.

const MODEL = "PASTE-THE-MODEL-NAME-HERE";

const SYSTEM_PROMPT = "PASTE THE SYSTEM PROMPT YOU WROTE IN AI STUDIO HERE";

module.exports = async (req, res) => {
  const text = (req.body && req.body.text) || "";

  if (text.trim() === "" || text.length > 500) {
    return res.status(400).json({ error: "Ask something under 500 characters." });
  }

  const response = await fetch(
    `https://generativelanguage.googleapis.com/v1beta/models/${MODEL}:generateContent`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "x-goog-api-key": process.env.GEMINI_API_KEY
      },
      body: JSON.stringify({
        systemInstruction: { parts: [{ text: SYSTEM_PROMPT }] },
        contents: [{ parts: [{ text: text }] }],
        generationConfig: { maxOutputTokens: 1000 }
      })
    }
  );

  if (!response.ok) {
    return res.status(502).json({ error: "The model didn't answer. Try again in a minute." });
  }

  const data = await response.json();
  const answer = data.candidates?.[0]?.content?.parts?.[0]?.text;
  res.json({ answer: answer || "The model didn't return anything. Try asking differently." });
};
```

Read it out loud:

1. **`MODEL`, `SYSTEM_PROMPT`**: your two decisions, at the top. The system prompt stays on the server.
2. **`req.body.text`**: what the visitor typed. The `if` turns away empty or very long questions before they cost anything.
3. **`fetch`**: the same `fetch` from L5, as a `POST` because we're sending something. The key comes from `process.env`, not from the file.
4. **`maxOutputTokens`**: a limit on the answer's length, which is a limit on cost.
5. **`data.candidates[0].content.parts[0].text`**: dig the answer out of the JSON, like `temperature_2m` in the weather reply. `?.` means *if a step is missing, stop instead of crashing*.
6. **`res.json`**: send the answer back to the page.

### 5. Add the page

In `index.html`, inside `<main>`:

```html
<form id="ask-form">
  <input id="question" type="text" placeholder="Ask me something" maxlength="500">
  <button>Ask</button>
</form>
<p id="answer"></p>
```

In `scripts.js`:

```js
const form = document.querySelector("#ask-form");
const answer = document.querySelector("#answer");

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  answer.textContent = "Thinking…";

  const response = await fetch("/api/ask", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text: document.querySelector("#question").value })
  });
  const data = await response.json();

  answer.textContent = data.answer || data.error;
});
```

Read it out loud:

1. **`event.preventDefault()`**: stop the form reloading the page.
2. **`"Thinking…"`**: show something straight away.
3. **`fetch("/api/ask")`**: ask your own server. No Google address, no key.
4. **`data.answer || data.error`**: show the answer, or the error if there isn't one.

### 6. Put it on Vercel

1. Commit and push.
2. Import the repo into Vercel, following [[Help - Host on Vercel]].
3. In the project, go to **Settings → Environment Variables**. Open `.env` in your editor, copy everything, and paste it into the **Key** box. Vercel splits it into a name and a value. If it doesn't, add `GEMINI_API_KEY` by hand. Save.
4. Go to **Deployments**, click **⋯** on the latest one and **Redeploy**. A new variable only reaches deployments made after you add it.

Open your `vercel.app` URL and ask it something. Then check:

- **View Source** and search for your key. It isn't there.
- **DevTools → Network**: the request went to `/api/ask`, not to Google.
- **Your phone**: same page, same server.

It won't work on `github.io`, in Simple Web Server, or from a double-clicked `index.html`. Those only serve files, so there's nothing to run `api/ask.js`.

## Add the Jev key

- Jev from L7 needs a key too: the class key I'll share in the class group. Same rules, one more line.
- Add it to `.env` on a new line, under the name used in [[Exercise - Build with Jev]]:

```text
GEMINI_API_KEY=your-gemini-key
AI_GATEWAY_API_KEY=the-class-key
```

- Paste the whole `.env` into Vercel again, the same way, and redeploy.
- Add the `api/decide.js` server from [[Exercise - Build with Jev]] to the same repo. One project, two servers, two keys.
- It's shared by the whole class and has a spending limit, so one call when someone presses a button, never on every keystroke. If you think it's leaked, tell me and I'll replace it.
- Make `.env.example` with both names and fake values, and commit it. That's how a teammate, or an agent, knows which keys the project needs.

Check it:

- Your repo on github.com has `.gitignore` and `.env.example`, and no `.env`.
- Vercel's **Environment Variables** page lists both names.
- Both servers answer on your `vercel.app` URL.

---

## Your final project: start a startup

### What a startup is

- A small team trying to find something people want, quickly, before the time or money runs out.
- Bengaluru examples they know: Swiggy, Zerodha, Zepto. Each started as one small thing for one group of people.
- A product is only part of it. A startup also has to answer: who is it for, how do they hear about it, why do they sign up, why do they come back?
- That's why the final project is a product *and* a landing page.

### Start small: the MVP

- **MVP** (minimum viable product): the smallest thing that tests whether people want it.
- Dropbox's first "product" was a video showing how it would work, and the sign-up list grew overnight. Back to Dropbox from L2.
- A landing page with a sign-up button is often the first MVP. If nobody signs up, you've saved months.
- For their project: what is the one flow that has to work? Everything else is "nice to have".

### The brief

- Walk through [[Project - Final Project]]: a product people sign in to, a landing page that gets them to sign up, deployed on Vercel. An AI feature if it earns its place.
- Everything so far is a part of it: pages (L1–L4), APIs (L5), a database (L6), sign-in (L8), keys and a server (today).
- Teams form in L10. Until then, sharpen your [[Exercise - Final Project Ideas|project ideas]].

---

## Homework

- Finish your AI server with both keys, live on Vercel.
- [[Exercise - Keep Your Keys Out of Git]]
- Rewrite your best two [[Exercise - Final Project Ideas|project ideas]] as startups. Fill in "They'd sign up because ___" for each, and think about who you'd want to work with.

### Reading: who makes the models

The models behind every AI feature, where they came from, and who owns them.

#### A short history

| When | What happened | Why it mattered |
| --- | --- | --- |
| 2017 | Google researchers publish "Attention Is All You Need", describing the **transformer** | The T in GPT. Almost every model on this page is built on it. |
| 2019 | OpenAI's GPT-2. At first they held back the full model, saying it could be misused | The first time generated text felt worryingly real |
| 2020 | GPT-3, with 175 billion parameters | Mostly the same method, just much bigger, and it could suddenly do tasks from a couple of examples |
| Nov 2022 | ChatGPT | A model you'd already heard of, with a chat box and assistant training. About 100 million people used it within two months. |
| 2023 | GPT-4, the first Claude, and Meta's Llama | Models started passing professional exams, and anyone could download a strong model |
| 2024 | GPT-4o talks and sees in real time. OpenAI's o1 thinks before answering. | One model for text, voice and images, and the start of reasoning models |
| Jan 2025 | DeepSeek R1, an open-weights reasoning model from China, reportedly trained for a fraction of what others spent | Nvidia's share price fell about 17% in a day |
| 2025 | Coding agents like Claude Code, Codex and Cursor's agent mode edit files and run commands for you | The tools you've been building with all semester |
| Feb 2026 | Sarvam releases 30B and 105B as open weights, trained from scratch in India | A Bengaluru company competing on Indian languages |
| 2026 | New frontier models from the big companies every few weeks, and new kinds like Jev | Anything in these notes with a version number is already out of date |

> **Sidenote:** Which of these did you notice happening at the time? What's the first AI product you remember using?
#### Who makes them

| Company | Models | Based in | Can you download it? |
| --- | --- | --- | --- |
| OpenAI | GPT, used in ChatGPT | San Francisco | Mostly no |
| Anthropic | Claude | San Francisco | No |
| Google DeepMind | Gemini, and the smaller Gemma | London and California | Gemini no, Gemma yes |
| Meta | Llama | California | Yes |
| xAI | Grok | California | Mostly no |
| Mistral | Mistral | Paris | Some |
| DeepSeek | DeepSeek | Hangzhou | Yes |
| Alibaba | Qwen | Hangzhou | Yes |
| Sarvam AI | Sarvam | Bengaluru | Yes |

#### Open weights vs closed

The last column is the big split.

| | Closed (ChatGPT, Claude, Gemini) | Open weights (Llama, DeepSeek, Qwen, Sarvam) |
| --- | --- | --- |
| How you use it | Only through the company's app or API | Download it and run it yourself, or use any company that hosts it |
| How good | Usually the best available | Often a few months behind, sometimes level |
| Where your data goes | To the company | It can stay on your own computer |
| What you pay | Per token | For the computer it runs on |
| Can you change it? | Only with a prompt | You can train it further on your own data |

"Open weights" isn't quite the same as open source. You get the finished file of numbers, but usually not the training data or the code that made it, so you can use it and adjust it but not rebuild it. Small open models can run on a laptop with apps like [LM Studio](https://lmstudio.ai), with no internet and no key.
