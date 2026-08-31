---
date: 08-09-2026
date modified: 01-09-2026
feed: show
tag: exercise
title: "Exercise - Build with the Anything API"
---
### Make a small app powered by an API that returns anything you ask for

`api.gyanl.com` is a made-up API. Whatever path you request, it invents a JSON response for it. `api.gyanl.com/pokemon/pikachu` returns a Pikachu. `api.gyanl.com/excuse/late-to-class` returns an excuse. Nobody wrote those endpoints — an AI model makes up the answer each time.

That makes it perfect for practice: you get a real request/response loop, with real JSON and real failure, without signing up for anything or handling an API key.

### How it works

Ask for any path, and optionally name the fields you want back:

```
https://api.gyanl.com/coffee/order
https://api.gyanl.com/pokemon/pikachu?fields=name,type,power
https://api.gyanl.com/plant/monstera?fields=water_every,light,mood_today
```

And in your page, it's the same `fetch` from [[Lecture 5 - Databases and APIs]]:

```js
const response = await fetch("https://api.gyanl.com/plant/monstera?fields=water_every,light,mood_today");
const data = await response.json();
console.log(data);
```

### Steps

1. **Open a few endpoints in your browser first.** Before any code. Invent three paths of your own and look at the raw JSON that comes back.
2. **Request the same endpoint twice.** Note what changes. This is a machine that invents an answer each time, not a database looking one up — decide now whether that matters for your idea.
3. **Pin down your shape.** Use `?fields=` to name exactly the fields you want, so your page knows what it's getting. Write those field names down; that's your contract.
4. **Design the display.** Sketch it before you build. What's the headline, what's secondary, what does it look like while it's loading? Don't let the JSON structure decide your layout.
5. **Build the page.** One input or one button is enough. Fetch, then render — no framework needed.
6. **Break it on purpose.** Request a nonsense path, throttle the network to Slow 3G, and turn wifi off mid-request. Your page should say something useful in all three cases instead of sitting blank.
7. **Ship it** to GitHub Pages ([[Help - Publish a Page with GitHub Pages]]).

### Ideas

- A tarot / fortune reader that takes a question and returns a card
- A pet name generator with a trait and a backstory
- A fake weather app for imaginary cities
- A "what should I cook" card from three ingredients you type in
- A museum label generator for objects around you

### Things to keep in mind

- **The API is slow.** It thinks before it answers — a second or two, sometimes more. A loading state isn't polish here, it's most of the experience. Design it properly.
- **It can return something you didn't expect**, including fields you didn't ask for or a value where you assumed a list. Look at what you actually got before you trust it. This is true of every API; this one just makes it obvious sooner.
- **The content is invented, and confidently so.** Fine for a pet name, not fine for a medication dose. That distinction is the whole lesson from [[Lecture 7 - AI Features]], arriving early.
- **It's my personal API and it costs me money to run**, so keep it to a handful of requests. Don't put a fetch inside a loop or a `setInterval`.
- If it goes down mid-exercise, tell me — and handle the error case in your page anyway.

### Submission

- Live URL of your page.
- A screenshot of the raw JSON from your endpoint, next to your rendered design. The point is the distance between the two.
- One sentence on what your page does when the API fails, and why you chose that over a blank screen.
