---
date: 08-09-2026
date modified: 24-07-2026
feed: show
tag: exercise
title: "Exercise - API Mashup"
---
### Build a page powered by someone else's data

Use a public API to make a small, well-designed page that displays live data — and understand the request/response loop underneath it.

### Ideas

- Weather for your city, designed beautifully (the classic)
- "What's playing" — movies from TMDB
- Local transit departures
- ISS location, air quality, currency rates, a random-poetry API

### Steps

1. **Choose an API** with a free tier and readable docs. Skim the docs yourself first — what can you ask it for?
2. **Make one request by hand** (browser or an API tool) before any code. Look at the raw JSON. Find the 3 fields you actually want.
3. **Design the display.** Sketch what the data should look like — hierarchy, units, empty states. Don't let the JSON structure dictate the design.
4. **Build it with AI.** Give it the API, your key, and your design intent.
5. **Handle failure.** Turn off wifi / use a bad key. What does your page show? Ask the AI to design for the error case — then redesign it yourself, better.

### Things to keep in mind

- Your API key is a password. If it's visible in your page source, it will get stolen. Ask the AI how it's handled.
- Rate limits are why your page breaks during the demo. Cache or refresh gently.

### Submission

- Live URL + one paragraph explaining how a simple API works, written for a non-technical client. (This doubles as the official "API Concept Explanation" assignment.)
