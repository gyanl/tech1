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
title: "Lecture 6 - WIP"
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

### Class Exercise: Weather in your Footer

Spend some time working on [[Exercise - Weather in the Footer]]

### REST: nouns in the URL, verbs as methods

Most APIs you'll meet are **REST**. The idea is small: the URL names a *thing*, the method says what to *do* to it.

```text
GET    /posts        →  give me all the posts
GET    /posts/42     →  give me post 42
POST   /posts        →  here's a new post, save it
DELETE /posts/42     →  get rid of post 42
```

You already met `GET` without noticing — it's what your browser does every time you open a page. Read a URL as a sentence and it usually tells you what it does.

The server answers with a **status code**. Three worth knowing:

- **200** — fine, here it is
- **404** — no such thing (the same 404 you got waiting for GitHub Pages)
- **500** — the server broke; not your fault

### JSON: what the data looks like

APIs don't send back pages. They send back **JSON** — data with no styling and no opinion about how it should look. Making it look like something is your job, and that's the good news.

```json
{
  "city": "Bengaluru",
  "temp": 24,
  "conditions": "cloudy",
  "forecast": [
    { "day": "Tue", "high": 27 },
    { "day": "Wed", "high": 25 }
  ]
}
```

Read it like a Figma layer panel: `{ }` is a group with named properties, `[ ]` is a list of things. `temp` is `24`. `forecast` is a list of two objects, each with a `day` and a `high`.

> **Sidenote:** When an AI tool builds you something API-powered and it renders blank, open the Network tab and look at the JSON. Nine times out of ten the data arrived fine and the code reached for a field name that doesn't exist.

### GraphQL, in one idea

REST gives you whatever the endpoint gives you — often much more than you need, sometimes less, so you make three calls. **GraphQL** flips it: one endpoint, and the *request* says exactly which fields you want back.

```text
{ user(id: 42) { name, avatar } }   →   just the name and the avatar
```

Fewer round trips, no wasted data. More work to set up. You should be able to tell them apart in a conversation; you don't need to write either by hand today.

## Databases: where it all sits

A database is a program whose entire job is to store data safely and hand it back fast. It isn't a file you open — you talk to it through code.

There are two broad families, and you should be able to tell them apart in a meeting:

**SQL** databases (Postgres, MySQL, SQLite) store **tables** — rows and columns, like a spreadsheet, except the rules are enforced. You declare up front that a `users` table has an `email` that is text and unique, and the database refuses anything else.

| id | name | email | joined |
| --- | --- | --- | --- |
| 1 | Ada | ada@example.com | 2026-08-04 |
| 2 | Grace | grace@example.com | 2026-08-11 |

**NoSQL** databases (Firebase, MongoDB) store **documents** — basically the JSON from earlier, each free to have a slightly different shape.

Rough rule of thumb: **SQL** when the shape of your data is known and things relate to each other — most serious products. **NoSQL** when the shape varies, or you're moving fast and don't know it yet. Teams argue about this far more than it deserves.

We're using NoSQL, specifically **Firebase Realtime Database**, for one reason: it is the shortest path from a static page to something that remembers. No server, no card, no SQL to learn.

## Firebase Realtime Database

### It's one big JSON tree

You already read JSON earlier in this lecture. That's the entire data model — your whole database is a single JSON object, and you read and write at **paths** inside it.

```json
{
  "guestbook": {
    "-Nx8kQ2p": { "name": "Ada",   "message": "hello!",  "at": 1756089600000 },
    "-Nx8kR7t": { "name": "Grace", "message": "nice site", "at": 1756089900000 }
  }
}
```

`guestbook/-Nx8kQ2p/name` is a path, and it points at `"Ada"`. There are no tables, no columns, and no `SELECT`. If you can navigate a Figma layer panel, you can navigate this.

Those ugly keys — `-Nx8kQ2p` — are generated for you when you `push` a new item. They're unique and they sort chronologically, which is why lists here are objects rather than arrays: two people posting at once can't fight over index `3`.

### The "realtime" part is the good bit

This is what makes it worth teaching you. You don't fetch the data — you **subscribe** to it. Firebase pushes changes to every connected browser as they happen.

Open your guestbook on your laptop and your phone. Type on the phone. The laptop updates. Nobody refreshed anything. That is the thing your pages have never been able to do.

### This breaks the diagram you just learnt

Look back at the round trip: browser → server → database. Now count the boxes in what we're about to build. There is no server. Your page talks to the database *directly*.

That's not a shortcut we're taking because you're beginners — it's what Firebase is for, and it makes it an unusual database in four ways worth knowing:

| Normal database | Firebase Realtime Database |
| --- | --- |
| Your back-end talks to it; the browser never does | The browser holds a connection straight to it |
| You **request**, it **responds**, done | You **subscribe**, it **pushes**, forever |
| Tables, rows, and a query language | One JSON tree, addressed by path |
| Writes go to the server, then come back | Writes apply on your device first, sync after |

Two consequences you should carry out of this room:

- **Security rules are the back-end.** With no server in the middle, the only thing standing between a stranger and your data is that rules file. Everywhere else, that job is done by code someone wrote and reviewed. Here it's a config you will be tempted to leave on `true`.
- **Querying is deliberately weak.** No joins, no filtering on two fields at once. That poverty is the price of the live updates — it's a trade Firebase made on your behalf, not a feature they forgot.

> **Sidenote:** It also works offline. Writes queue on the device and sync when the connection comes back, which is why the reply appears in your UI before the server has heard about it. Lovely when it works, confusing the first time a value appears and then changes a second later.

### Setting it up

1. Go to [console.firebase.google.com](https://console.firebase.google.com) and **Add project**. Skip Google Analytics.
2. In the left sidebar, **Build → Realtime Database → Create Database**. Pick a location.
3. Choose **Start in test mode** for now. Read the warning in the next section before you leave it that way.
4. Back on the project overview, click the **`</>`** (web) icon to register a web app. Firebase gives you a config snippet — copy it.

> **Sidenote:** The console will try to steer you to **Cloud Firestore**, which is Firebase's newer, more capable database. It's the better choice for a real product. We're using Realtime Database because it's a JSON tree you can look at and understand in one sitting, which is the point this week.

### Writing and reading

Copy the version numbers from the snippet the console gave you rather than from here — they change.

```html
<script type="module">
  import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-app.js";
  import { getDatabase, ref, push, onValue }
    from "https://www.gstatic.com/firebasejs/10.12.0/firebase-database.js";

  const app = initializeApp({ /* the config object from the console */ });
  const db  = getDatabase(app);
  const guestbook = ref(db, "guestbook");

  // WRITE — add one entry
  document.querySelector("#form").addEventListener("submit", (event) => {
    event.preventDefault();
    push(guestbook, {
      name:    document.querySelector("#name").value,
      message: document.querySelector("#message").value,
      at:      Date.now()
    });
    event.target.reset();
  });

  // READ — runs now, and again every time anything changes
  onValue(guestbook, (snapshot) => {
    const entries = Object.values(snapshot.val() || {});
    document.querySelector("#list").innerHTML = entries
      .map(e => `<li><strong>${e.name}</strong> ${e.message}</li>`)
      .join("");
  });
</script>
```

Six things are happening, and you know most of them already:

- **`ref(db, "guestbook")`** — a pointer to a path in the tree. Same instinct as `querySelector`, but for data instead of the page.
- **`push`** — add a child with a generated key.
- **`onValue`** — the subscription. Firebase calls your function immediately with the current data, then again on every change, forever. This is why nothing refreshes.
- **`snapshot.val()`** — the plain JSON at that path. `|| {}` covers the empty database, which is otherwise `null` and a very common first bug.
- **`Object.values(...)`** — turn `{key: entry, key: entry}` into a plain list you can map over.
- **`event.preventDefault()`** — stop the browser doing its default form thing, which is to reload the page.

### Security rules, and the key that isn't a secret

Two things that look contradictory, so read both:

**Your Firebase config is public, and that's fine.** It goes straight into your HTML. It is not a password — it's an address, telling the browser which project to talk to. Everyone can see it and Google intends that.

**Which means your database is protected only by its rules.** Rules are a small JSON document deciding who may read and write where. Test mode gives you this:

```json
{ "rules": { ".read": true, ".write": true } }
```

That reads: *anyone on the internet may read everything and write anything.* Fine for a class exercise this week; genuinely dangerous for anything real. Firebase makes test mode expire after 30 days on purpose, and when it does your app will stop working and you will have forgotten why.

Before your final project goes anywhere near real people, the rules need tightening — at minimum so that people can add entries but not delete each other's, and so nobody can dump the whole tree. Ask AI to write rules for your specific shape and *read what it gives you.*

> If strangers can write to your database, strangers will write anything to your database. Deciding what your app does about that is design work, and we'll come back to it.

### Two habits that will save you

- **Keep your tree shallow.** Reading a path downloads *everything underneath it*. Nesting all your messages inside each user means fetching one user fetches every message they ever wrote.
- **Store what you'll display.** No joins here. If your list shows an author name, store the name on the entry, even though it's "duplicated". This is called denormalisation and in this world it's correct, not lazy.

### The schema is a design decision

The **schema** is the list of fields a thing has. Firebase won't enforce one — which makes deciding it deliberately more important, not less:

> What is a "user" in your product? Name — one field or two? Is email required? Is there a pronouns field, and is it a dropdown or free text? Can someone have no photo?

Every one of those choices shows up later as a form field, an empty state, or a bug. You have all seen a form that demanded a title from a list of four and none of them fit — that's a schema decision, made by someone who wasn't thinking about people.

> **Sidenote:** Sketch the schema before anyone builds anything. It is much cheaper to add a field on paper than in a live database with ten thousand entries in it.

## Class Activity — the class wall

We're going to build one thing together, into **one shared database**, and put it on the projector.

It's a grid of squares. You click a square, it becomes your colour. It becomes your colour *on everyone else's screen too*, immediately. Thirty of you, one JSON tree, no refreshing.

> **Sidenote:** You already know what this feels like — it's the thing that makes Figma feel like Figma. Today you find out that multiplayer is not magic, it's a database that pushes.

### How this works

I've made one Firebase project for the class and I'll put the config on the screen. **Everyone uses my config**, so we're all pointed at the same tree. You each build your own page against it.

The data model is about as small as a data model gets — one colour per square, keyed by its position:

```json
{
  "wall": {
    "0": "#ff4343",
    "1": "#2b6cb0",
    "47": "#1a1a1a"
  }
}
```

Note we're using `set` at a specific path here, not `push`. `push` is for *adding to a list* where the order matters and the keys should be unique. `set` is for *this exact path gets this exact value* — square 47 is one square, and writing to it replaces what was there. Which is why the last person to click a square wins it.

### The HTML

```html
<input type="color" id="colour" value="#ff4343">
<div id="wall"></div>
```

### The CSS

```css
#wall {
  display: grid;
  grid-template-columns: repeat(32, 1fr);
  gap: 1px;
  background: #ddd;
  border: 1px solid #ddd;
}

#wall button {
  aspect-ratio: 1;
  border: 0;
  padding: 0;
  background: #fff;
  cursor: pointer;
}
```

That's the `grid` I mentioned in passing last week. A wall of equal squares is exactly what it's for — this is a genuine two-dimensional grid, not a row that wraps, so flexbox would be the wrong tool.

### The JavaScript

```html
<script type="module">
  import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-app.js";
  import { getDatabase, ref, set, onValue }
    from "https://www.gstatic.com/firebasejs/10.12.0/firebase-database.js";

  const app = initializeApp({ /* the class config, from the screen */ });
  const db  = getDatabase(app);

  const COLS = 32, ROWS = 18;
  const wallEl = document.querySelector("#wall");

  // draw the empty grid once
  for (let i = 0; i < COLS * ROWS; i++) {
    const cell = document.createElement("button");
    cell.dataset.index = i;
    wallEl.append(cell);
  }

  // WRITE — one click, one square
  wallEl.addEventListener("click", (event) => {
    const i = event.target.dataset.index;
    if (i === undefined) return;
    set(ref(db, "wall/" + i), document.querySelector("#colour").value);
  });

  // READ — runs now, and again on every change anyone makes anywhere
  onValue(ref(db, "wall"), (snapshot) => {
    const pixels = snapshot.val() || {};
    for (const cell of wallEl.children) {
      cell.style.background = pixels[cell.dataset.index] || "#ffffff";
    }
  });
</script>
```

Nothing here is new except `set`. It's the same three moves as the guestbook: point at a path, write to it, subscribe to it.

### Things to notice while we're doing it

- **Nobody wrote any code to receive other people's clicks.** You subscribed to a path. That's the whole of multiplayer.
- **Turn off the wifi and keep clicking.** Your squares still fill in — that's the local cache. Turn it back on and watch them arrive on the projector at once.
- **Somebody is going to draw something rude on the projector.** Good. That's `.write: true` in the rules, on a database with no server in front of it, and it's the most memorable security lesson available. What would you have to change to stop it?
- **Watch what happens when two people click the same square.** Last write wins. Nobody's edit is merged — compare that to what Git did for you in week two.

### Then, on your own

Make your own Firebase project — your own config, your own tree — and get a **guestbook** working on your github.io page: a name, a message, a list that updates live. That's the shape you'll extend for homework.

## Homework

- **Exercise:** [[Exercise - Add a Database]] — build something small that more than one person can use at the same time. Something must survive a refresh, and something must show up on someone else's screen without them refreshing.
- Sketch the data model of an app you use every day. What are its tables, and what fields does each one have? Bring the sketch — we'll compare.
