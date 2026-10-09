---
date: 13-10-2026
date modified: 09-10-2026
feed: show
tag: exercise
title: "Exercise - Keep Your Keys Out of Git"
---

### API Keys

API keys are like passwords that let someone use your account with an API provider. Therefore, you have to store them carefully - they should never even be sent into an AI chat! (Why?)

In this exercise you'll keep the key in a file called `.env`, tell Git to ignore that file with `.gitignore`, and check that GitHub never sees it. At the end your key should exist in exactly two places: your laptop and Vercel.

### Why bother?

- **Your repo is public.** GitHub Pages needs your project to be public, and anyone can read every file in it.
- **People search GitHub for keys.** Bots scan new commits for anything that looks like a key, often within minutes of a push.
- **Deleting the file later doesn't help.** Every commit is kept in your repo's history (the chain from L2), so a key you pushed once can still be found after you remove it.
- **A leaked key spends your money.** Without billing, the worst case is someone using up your daily limit. With billing on, it's a bill.

Where a key can live, and who can see it:

| Where | Who can see it |
| --- | --- |
| In `scripts.js` or your HTML | Anyone who opens View Source |
| Written into `api/ask.js` | Anyone who opens your repo on GitHub |
| In `.env`, ignored by Git | Only you, on your laptop |
| In Vercel's environment variables | Only your server |

Your Firebase config is different. It's an address, not a password, and it's fine in your page (L6).

### Working with agents: don't paste the key into the chat

When you build with Claude, Cursor or ChatGPT, it's tempting to paste the key in and say "use this". Don't.

- The chat is sent to the AI company and kept in your history. Depending on your settings, it may be used to train future models.
- The agent may copy the key straight into your code, a commit message, or a test file, and then it's in your repo.
- You can't take it back. Once it's been pasted somewhere, treat it as leaked.

Instead, you put the key in `.env` yourself, and tell the agent only its **name**. The agent writes code that reads `process.env.GEMINI_API_KEY`, and never needs to know the value.

### Steps

**1. Make `.gitignore` first, before the key exists**

In the top folder of your repo, make a file called exactly `.gitignore`:

```text
.env
.env.local
.vercel
```

*Each line is a file or folder Git should pretend isn't there.*

**2. Make `.env`, by hand**

In your editor, make a file called exactly `.env` next to `.gitignore`, and paste your key into it yourself:

```text
GEMINI_API_KEY=paste-your-key-here
```

No quotes and no spaces around the `=`. The name on the left has to match the one in Vercel and in your code.

Files that start with a dot are hidden in Finder. Press **⌘⇧.** to show them. VS Code shows them anyway.

**3. Check before you commit**

Open GitHub Desktop and look at the list of changed files.

- `.gitignore` should be there. Commit it.
- `.env` should **not** be there. If it is, `.gitignore` has a typo or is in the wrong folder. Fix that before you commit anything.

**4. Leave a note for your team**

Make a file called `.env.example` with a fake value, and commit it:

```text
GEMINI_API_KEY=your-key-goes-here
```

This tells a teammate, or an agent, which keys the project needs without giving any of them away. You'll want this for your final project.

**5. Tell your agent the rules**

```text
My Gemini API key is in .env as GEMINI_API_KEY. Read it with process.env.GEMINI_API_KEY.
Don't open, print or edit .env, and never write the key into any other file.
Make sure .env is in .gitignore before you commit anything.
```

Some agents let you block a file completely. Cursor has a `.cursorignore` file, and Claude Code has permission settings that can deny reading `.env`.

**6. Put the same key on Vercel**

`.env` never leaves your laptop, so the live site can't read it. Vercel needs its own copy:

1. Open your project on [vercel.com](https://vercel.com) and go to **Settings → Environment Variables**.
2. Open `.env` in your editor, select everything, and copy it.
3. Paste it into the **Key** box. Vercel splits each line into a name and a value for you. If it doesn't, type `GEMINI_API_KEY` as the key and paste just the key as the value.
4. Leave all three environments ticked (Production, Preview, Development) and click **Save**.
5. Go to **Deployments**, click **⋯** on the latest one and **Redeploy**. A new variable only reaches deployments made after you add it.

Do this yourself in the browser, not through your agent. Copying from `.env` to Vercel is the one time the key needs to move, and it shouldn't pass through a chat on the way.

Later, when you have more keys or a teammate adds one, you can paste the whole `.env` the same way.

**7. Check GitHub**

Push, then open your repo on github.com.

- `.env` isn't in the file list.
- `.env.example` and `.gitignore` are.
- Google API keys start with `AIza`. Search your repo for it. Nothing should come up.

### If it leaks anyway

Don't try to delete it from the history. Go to [aistudio.google.com/apikey](https://aistudio.google.com/apikey), delete that key, make a new one, and put the new one in `.env` and in Vercel. Then redeploy. A deleted key is useless to whoever found it.

### Things to try

- Rename `.gitignore` for a minute and watch `.env` appear in GitHub Desktop's list. Rename it back before you commit.
- Ask your agent "what's my API key?" and see what it does. Is that what you'd want it to do?

### Submission

- A screenshot of your repo on github.com showing `.gitignore` and `.env.example`, and no `.env`
- A screenshot of the prompt where you told your agent about the key, with no key in it
