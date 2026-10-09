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

## Follow up: how can a site check a password it never saves?

Real apps never store your password, only a hash of it. Someone asked how the site can tell whether you typed the right password.

A **hash function** turns any text into a fixed-length string, like a fingerprint. Open [this SHA-256 demo](https://andersbrownworth.com/blockchain/hash) and type into the box. SHA-256 is one of the most common hash functions. Type `Nidharna123!`, then change the first letter to lowercase:

```text
Nidharna123!  →  ef5a24be5e696b0670a070bb376616d2f4673d2b29d357dc78eac245221d21bc
nidharna123!  →  bd65af5ab064cfc8431fd8304209ef57d9d4fbc4a2e6dfdabc42a8648c85f43b
```

Some things to note:

- **The same text always gives the same hash.** Type `Nidharna123!` again and you get exactly the same string.
- **One small change gives a completely different hash.** Nothing about the second one looks like the first.
- **You can't work backwards.** There's no way to get `Nidharna123!` from the hash, except by guessing passwords and hashing each one.
- **Two different pieces of text are, for all practical purposes, never going to have the same hash.**
  This would be called a "collision"

So this is what a site does with your password:

| When you | The site |
| --- | --- |
| Sign up | Hashes your password and saves only the hash |
| Sign in | Hashes whatever you just typed, and compares it with the saved hash |
| Type the right password | Gets the same hash, so it lets you in |
| Type anything else | Gets a different hash, so it doesn't |

The site sees your password for a moment while it hashes it, but never keeps it. If someone steals its database, they get hashes, not passwords.

Real sites go a bit further. They add some random text to each password before hashing it (called a **salt**), and use hash functions that are deliberately slow, so that guessing millions of passwords takes too long. The Computerphile video at the end of L8 covers this. With Sign in with Google, none of it is your problem: Google stores the hash, and your app never sees a password at all.

### Hash functions do get broken

SHA-256's older sibling, **SHA-1**, was the standard for years. In February 2017, researchers at Google and CWI Amsterdam published [two different PDF files with the same SHA-1 hash](https://shattered.io). Finding them took about nine quintillion attempts, roughly what one processor would do in 6,500 years. Once two different files can share a hash, the hash can't be trusted to tell them apart, so browsers, GitHub and others moved to SHA-256. Git named every commit with SHA-1 and is still slowly moving off it.

"Broken" here means two inputs with the same hash. It doesn't mean anyone can work backwards from a hash to a password.

### Could AI break SHA-256?

- **It's an unlikely job for AI.** Models are good at finding patterns, and a good hash function is designed so its output has none. SHA-1 was broken by people finding a weakness in how it was designed, not by learning from examples.
- **If SHA-256 did break**, a lot would have to move at once: Bitcoin, HTTPS certificates, the checks that make sure a software update is genuine. There's already a replacement, SHA-3, standardised in 2015.
- **The more realistic long-term worry is quantum computers**, and they threaten encryption like RSA far more than they threaten hash functions.

---

## Homework Review

- [[Exercise - Unusual Interactions]]
- [[Exercise - Realtime Web Experience]]
- [[Exercise - Sign in with Google]]
- [[Exercise - Build with Jev]]

---

## API keys

- Sign-in is for people. When your app makes a request to an API that is not free, the program uses a **key** instead of an ID and password.
- In the three kinds of proof from L8, a key is "something you know", for a program. Whoever has the key is should be able to access the service, as far as the API server is concerned. No second factor, no confirmation email.
- So keeping it secret is its only protection. The API server trusts the key, and it's your job to make sure only your app has it.

### What happens to a key

An **API key** is a long, random string of letters and numbers. It works like an ID card and a password at once: it says which account is asking, and proves that account is allowed to. The company uses it to let you in, count how much you use, and bill you.

From the dashboard to an answer, it goes through four steps:

1. **You make it** in the company's dashboard - today we will use Google AI Studio. Their computer generates a random key. Many companies keep only a hashed copy of it (same idea as passwords in L8), which is why some dashboards, like OpenAI's, only show you a key once.
2. **You keep it** in `.env` on your laptop and in Vercel's environment variables. Nowhere else.
3. **Your server sends it with every request**, in a header. This line is in the `api/ask.js` you'll write later today:

   ```js
   "x-goog-api-key": process.env.GEMINI_API_KEY
   ```

   *Send the key from Vercel along with the question.* Jev's server does the same with `Authorization: Bearer ...`: a different label, the same idea.

4. **The company checks it.** Their server looks the key up, checks it's still active and what it's allowed to do, counts the request against your limit, and only then answers. A missing or wrong key gets turned away, usually with `401 Unauthorized`, one of the status codes from [[Exercise - Trace a Request]]. Gemini answers a bad key with a `400` and "API key not valid".

### Where it can and can't live

**You can't commit your API key to your Github repo**
- Github Pages free tier requires your projects to be public. Bots scan GitHub for things that look like API keys and they will steal it in minutes. Git commit history keeps a copy even if you delete it with a new commit.

**Even if you don't use a public repo, you can't put your API key into your project.**
- Anyone can View Source and find it and then start using your API billing.

**You shouldn't paste your API key into a chat with your AI agent.**
Your chat history is sent to the AI company and can end up in your code. Most AI agents will tell you to "rotate" a key if they think you have sent them an API key in the chat - this means disable the key from your API dashboard, then generate a new one.

- Tell your agent the key's **name** (`GEMINI_API_KEY`), never its value.
- Save the value in the .env file using your text editor. This is one of the few things that you have to do manually instead of using an agent (for security reasons). Agents are told to specifically never read a .env directly.

**Then where can an API key be stored?**
In a special type of file called `.env` (short for environment) on your laptop, ignored by Git using a file called `.gitignore` that tells Github to ignore some files in your project.

![[Add to Gitignore.png]]

When you run the project locally, the code uses the .env saved only on your computer to access the API. When you deploy to Vercel, Vercel will not have the API key since it it's not in your repo, and you need to separately add the API key to Vercel in your project settings.

- If it leaks, delete it and make a new one. Unlike your Google password, a key is quick to replace, so don't hesitate even if you are uncertain. Better safe than sorry.
- **A leaked key spends your money.** Without billing, the worst case is someone using up your daily limit. With billing on, it's a bill.

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

By the end of today, yours will look something like this. These keys are fake:

```text
# Gemini, from Google AI Studio
GEMINI_API_KEY=fake-gemini-key-8f3k2m9x7q1w4e6r

# Jev, the class key from the class group
AI_GATEWAY_API_KEY=fake-gateway-key-2b7n5v1c9z3x8l4k
```

Some things to note:

- **No quotes, and no spaces around the `=`.**
- **Lines starting with `#` are notes to yourself.** Nothing reads them.
- **The name on the left has to match exactly**, in your code (`process.env.GEMINI_API_KEY`) and in Vercel.
- **Real keys look less friendly.** A Gemini key is 39 characters and starts with `AIza`. If you ever see `AIza...` in a file that isn't `.env`, it shouldn't be there.

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
- Shaadi.com, Swiggy, Zerodha, Zepto. Each started as one small thing for one group of people.
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
