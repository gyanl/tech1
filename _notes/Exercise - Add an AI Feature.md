---
date: 14-09-2026
date modified: 24-07-2026
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
3. **Build it with AI tools** (yes, using AI to add AI). Use any LLM API with a free/cheap tier.
4. **Try to break it.** Feed it nonsense, hostile input, other languages. Screenshot the failures.
5. **Design the failure states.** What does the user see when the model is slow, wrong, or refuses?

### Things to keep in mind

- API calls cost money per token — this is the first time your design decisions have a per-use price tag. Notice how that changes your choices.
- Disclose the AI. Users should know when they're reading a model's words.
- Keys live on the server, never in the page. Verify.

### Submission

- Live URL, your system prompt (as written artifact), and your 3 best breakage screenshots with what you changed because of them.
