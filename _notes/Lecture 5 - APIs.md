---
date: 01-09-2026
date modified: 01-09-2026
feed: show
key_areas:
  - "JavaScript — interactivity"
  - "APIs — REST"
  - "APIs — GraphQL"
  - "Databases — SQL"
  - "Databases — NoSQL"
  - "Server-side languages"
  - "Understanding data flow"
tag: lecture
title: "Lecture 5 - APIs"
---

## Homework Review

Let's look at your submissions!

- [[Exercise - Figma to Code]]
- [[Exercise - Unusual Interactions]]

## Two kinds of website

There are 2 types of websites: static sites and dynamic sites.

Static sites are the same exact site for every viewer. The sites you have built so far are all static sites - even the ones with interactivity like button presses.

Dynamic sites are different based on the viewer - for eg. Instagram (when you use the website version). They frequently have an account login and a database that saves information.

|                         | **Static**                       | **Dynamic**                           |
| ----------------------- | -------------------------------- | ------------------------------------- |
| What the server sends   | The same files to everyone       | A page built for *you*, right now     |
| Where the content lives | In your HTML, typed by you       | Usually in a database, fetched when asked     |
| Where to deploy        | Github Pages     | Vercel, Netlify, Firebase, Cloudflare, etc. |
| Examples                | Your portfolio, this course site | Instagram, Gmail, your bank           |

Static sites are simpler to work with - they can be opened directly if you double click on the .html files, and the Simple Web Server app is "simple" because it serves static sites only. This course site is a static site as well (usually search needs a dynamic site - but there are some workarounds). But the moment your product needs a login, a comments system, booking, payments, or saved anything, you need to make a dynamic site.

## The two halves

**Front-end** is code that runs in the visitor's browser, on their laptop or phone. HTML, CSS and JavaScript. React is also a js-based frontend technology. You can read all of it — right-click any site and View Source. That's everything you've written so far.

**Back-end** is code that runs on the server - which is another computer you control, somewhere else. This code doesn't run on the visitor's computer and the visitor only sees the results. It's written in whatever the team likes — Python, Node.js (js based backed technology), Ruby, Go — and its job is to hold the data and decide who gets what.

## The round trip

```text
   BROWSER                    SERVER                  DATABASE
   (their phone)              (your back-end)         (the storage)

   types a name  ──────────▶  receives request ─────▶ INSERT the row
                                                             │
   sees the list ◀─────────── sends back JSON ◀──────── here's every row
```

However, it's not necessary to maintain your own server and backend - for simpler things, it's possible to use an API running on someone else's server with your static site to achieve some of the behaviour of dynamic sites.

## APIs

An API is an Application Programming Interface. It lets one computer system ask another system to do something (like give it some data) without needing to fully understand how the other system works.

The useful mental model is a restaurant counter with a menu. You can order anything on the menu, in the format the menu specifies. You cannot walk into the kitchen, you can only pick up what they put on the counter when you order.

For example, a weather API. Nobody at [Open-Meteo](https://open-meteo.com/) knows you, but their computer will answer questions from yours. Open this in a browser tab:

```text
https://api.open-meteo.com/v1/forecast?latitude=12.97&longitude=77.59&current=temperature_2m,relative_humidity_2m,weather_code&timezone=Asia/Kolkata
```

Copy and paste this API URL into your browser. What do you see?

### JSON format

JSON stands for JavaScript Object notation. It's a data format that is easy to use on the web, because JavaScript "objects" are defined in this way.

You’ll frequently see APIs returning JSON:

While API URLs look similiar to regular URLs, they return data in JSON (or some other format) instead of an HTML page. You get no fonts, no layout, no page.

Everything a person would actually *see* — that it's `27°`, that it's humid at 56%, whether that deserves a grey sky or a bright one — is still your job on the frontend. The weather API gives you data, but you still need to figure out how to design the weather app.

~~~
{
  "name": "Gyan",
  "age": 30,
  "projects": [
    "Website",
    "Brand identity"
  ]
}
~~~

### API Response

That URL is an order, and it has parts:

| Part | What it is |
| --- | --- |
| `api.open-meteo.com` | which counter you're ordering from |
| `/v1/forecast` | what you want — a forecast |
| `?latitude=12.97&longitude=77.59` | where |
| `&current=temperature_2m,...` | which specific things, from a list they publish |

What comes back for Bengaluru, right now:

```json
{
  "latitude": 12.970123,
  "longitude": 77.56364,
  "generationtime_ms": 0.13208389282226562,
  "utc_offset_seconds": 19800,
  "timezone": "Asia/Kolkata",
  "timezone_abbreviation": "GMT+5:30",
  "elevation": 914,
  "current_units": {
    "time": "iso8601",
    "interval": "seconds",
    "temperature_2m": "°C",
    "relative_humidity_2m": "%",
    "weather_code": "wmo code"
  },
  "current": {
    "time": "2026-09-01T13:00",
    "interval": 900,
    "temperature_2m": 28.2,
    "relative_humidity_2m": 52,
    "weather_code": 53
  }
}
```

Some things to note:

- **We asked for latitude `12.97` and got back `12.970123`.** The forecast comes from a grid, so it answered for the nearest point it actually has. APIs answer the question they *can* answer, and tell you what they did.
- **It says `"weather_code": 53`, not `"moderate drizzle"`.** A number is the same in every language and every app; the word is a presentation choice. They hand you the code and a table to look it up in — and leave the wording to you. (53 is moderate drizzle in this case.)
- **It sends `current_units` alongside `current`.** They could have assumed Celsius. Instead the response says what the numbers mean, so your code can label them without guessing.

### How APIs work

The open-meteo API is a free API.

- no API Key needed
- no sign-up
- 10,000 calls a day free for non-commercial use
- you credit them under a CC BY licence.

It costs money to run servers, so many APIs are paid and will require you to sign up and create an API Key - which is like an auto-generated password that lets you use your paid API. Every API has terms like these. Read them before you build on top of one.

Two things follow from that:

- **The menu is a design decision.** Somebody chose what could be asked for and what comes back. That somebody should include a designer.
- **You don't need to know how the kitchen works.** Which is exactly why APIs let you build far more than you could write yourself.

### How API keys work

Most useful APIs make you register and give you a **key**: a long string that identifies you, tracks your usage, and gets billed to you.

**A key in your front-end code is a key you have published.** Your repo is public. View Source is one click. People run bots that scan GitHub for keys, and they will spend your credits.

So:

- Never paste a key into `scripts.js`, and never commit one.
- Keys belong on the back-end, or in the environment variables of a host like Vercel or Netlify.
- If you leak one, **revoke it immediately** and issue a new one. Deleting the commit does not help — it's in the history, which is exactly what L2 was about.
- "Free" APIs have rate limits. Read them before you design something that calls the API on every keystroke.

### Putting API data into your page

```js
const response = await fetch("https://api.example.com/weather?city=Bengaluru");
const data = await response.json();
document.querySelector("#temp").textContent = data.temp;
```

Read it out loud:

1. **`fetch`** — go and ask that URL for something. `await` means *wait for the answer before carrying on*, because it's coming over the internet and that takes time.
2. **`.json()`** — turn the reply into data JavaScript can use.
3. **`querySelector("#temp")`** — find the element with `id="temp"` and put the value in it.

`querySelector` takes the exact same selectors you learnt in L3 — `#temp` for an id, `.card` for a class, `h1` for a tag.

You will mostly have AI write this. But when it hands you fifty lines, you now know which three are doing the work.

### Class Exercise: Weather in the Footer

[[Exercise - Weather in the Footer]]


### Class Exercise: Anything API

[[Exercise - Build with the Anything API]]