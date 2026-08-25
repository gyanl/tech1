---
date: 29-09-2026
date modified: 25-08-2026
feed: show
tag: exercise
title: "Exercise - Add an AI Feature"
---
### Put a model inside your product

Add one genuinely useful AI feature to something you've already built this semester. The bar: it must be better *because* it's AI, not AI for its own sake.

### Ideas

- Your guestbook summarises the vibe of all messages
- Your API mashup explains the weather like a friend, not a table
- Your personal site has a "ask me anything" that answers from your bio
- Your poll generates a neutral summary of why people voted each way

### Steps

1. **Write the feature as a sentence first.** "When the user ___, the model ___, so that ___." If the sentence is unconvincing, pick another feature.
2. **Design the prompt.** The system prompt is a design spec: tone, format, refusals, length. Draft it in a doc before any code.
3. **Build it with AI tools** (yes, using AI to add AI). Use a free key from [Google AI Studio](https://aistudio.google.com/apikey), in a **separate throwaway repo**, with **no billing account attached**.
4. **Try to break it.** Feed it nonsense, hostile input, other languages. Screenshot the failures.
5. **Design the failure states.** What does the user see when the model is slow, wrong, or refuses?

### Things to keep in mind

- API calls are billed per token — you're on a free tier, so you'll hit a *quota* rather than a bill, but notice how "how often does this run?" changes your design choices.
- Disclose the AI. Users should know when they're reading a model's words.
- **The key in your page is a deliberate exception for this exercise**, and only safe because it's a free-tier key with no card on it, in a repo you'll delete. **Revoke it in AI Studio when you submit.** Deleting the commit does not help — you know why from week two.
- The same input gives different output every time. Anything that must be consistent, you pin down in the prompt and validate when it arrives.

### Submission

- Live URL
- Your system prompt, as a written artifact, with at least two versions so I can see what you changed and why
- Your 3 best breakage screenshots, each with the change you made because of it
- One sentence confirming the key is revoked
