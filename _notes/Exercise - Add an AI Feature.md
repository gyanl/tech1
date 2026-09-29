---
date: 29-09-2026
date modified: 28-09-2026
feed: show
tag: exercise
title: "Exercise - Add an AI Feature"
---
### Put a model inside something you've built

Add one AI feature to something you've already made this semester, through your own server on Vercel, as in [[Lecture 7 - AI Features]]. The bar: it should be better because it uses a model, not just have a model in it.

### Ideas

- Your weather footer describes the day the way a friend would, instead of a number and an icon.
- Your realtime Q&A board groups similar questions together, or summarises what people are asking.
- Your crit board flags comments that aren't about the work.
- Your portfolio has an ask-me-anything box that answers only from your bio.
- Your theme switcher picks one of your themes from a sentence the visitor types.

### Steps

1. **Write the feature as one sentence.** "When the user ___, the model ___, so that ___." If the last part is weak, pick another feature.
2. **Write the system prompt in AI Studio first.** Tone, length, format, and what to do when it doesn't know. Save each version in a doc with a line on what you changed and why.
3. **Build the server.** Start from the `api/ask.js` in the lecture, with your own system prompt and model name. The key goes in Vercel's environment variables, never in your repo.
4. **Connect your page to it.** If your project is on GitHub Pages, import the same repo into Vercel ([[Help - Host on Vercel]]) and use the `vercel.app` URL from now on. The `github.io` copy can't run the server.
5. **Try to break it.** Nonsense, other languages, empty input, very long input, "ignore your instructions". Screenshot what happens.
6. **Design the failure states.** What does the visitor see while it's slow, when it's wrong, when it returns nothing, and when you're out of quota?

To check it worked: View Source and search for your key (it shouldn't be there), and in DevTools → **Network**, the request should go to `/api/...`, not to Google.

### Things to keep in mind

- **No billing account on your key.** On the free tier you'll hit a daily limit instead of a bill. Notice how "how often does this run?" changes what you build.
- **Tell people it's a model.** A small label near anything the model wrote.
- **Same input, different output.** Anything that must be the same every time, pin down in the prompt and check in code when it arrives.
- **Your `/api` URL is public.** Keep the length limit and `maxOutputTokens` from the lecture, and keep the system prompt on the server.

### Submission

- Live `vercel.app` URL
- Your one-sentence feature
- Your system prompt, with at least two versions and what you changed between them
- Your 3 best breakage screenshots, each with the change you made because of it
