---
date: 01-09-2026
date modified: 25-08-2026
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
title: "Lecture 5 - Databases and APIs"
---

## Recap

Four weeks in, here's what you can do:

- **L1** — HTML is content, CSS is looks, JS is behaviour. You shipped a page to a real URL.
- **L2** — Git tracks versions, GitHub stores and serves them. You set type properly.
- **L3** — Divs group, classes name, flexbox arranges. Colours live once in `:root`.
- **L4** — `rem` for type, `%` and `max-width` for widths, media queries for the rest.

Everything you have built so far has one thing in common: **it forgets.**

Your page is the same three files for every visitor, and nothing anyone does on it is remembered. Refresh, and it's back to how it started. Today we fix that — and the fix is where most real products actually live.

> **Sidenote:** Every site you use daily is a fairly plain page plus a large pile of data. Instagram is a grid of divs. What makes it Instagram is the database behind it.

## Two kinds of website

| | **Static** (what you've built) | **Dynamic** (today) |
| --- | --- | --- |
| What the server sends | The same files to everyone | A page built for *you*, right now |
| Where the content lives | In your HTML, typed by you | In a database, fetched when asked |
| To change it | Edit, commit, push | Someone types something and hits Save |
| Examples | Your portfolio, this course site | Instagram, Gmail, your bank |

Static is not the lesser option — this course site is static and that's the right call. But the moment your product needs a login, a comment, a booking, or a saved anything, you need the other half.

## The two halves

**Front-end** is code that runs in the visitor's browser, on their laptop or phone. HTML, CSS and JavaScript. You can read all of it — right-click any site and View Source. That's everything you've written so far.

**Back-end** is code that runs on a computer you control, somewhere else. The visitor never sees it. It's written in whatever the team likes — Python, Node.js, Ruby, Go — and its job is to hold the data and decide who gets what.

> Front-end is the shop floor. Back-end is the stockroom and the till. Customers only ever see one of them, and you design both.

You are not going to write a back-end from scratch in this course. You need to know it exists, what it's responsible for, and how to ask for things from it — because "who does this bit, the front or the back?" is a design question you'll be in the room for.

## The round trip

This is the single most useful diagram in the course. Everything from here on is a variation of it:

```text
   BROWSER                    SERVER                  DATABASE
   (their phone)              (your back-end)         (the storage)

   types a name  ──────────▶  receives request ─────▶ INSERT the row
                                                             │
   sees the list ◀─────────── sends back JSON ◀──────── here's every row
```

Six steps. A guestbook, a checkout, a login and a social feed are all this shape. When something is broken, your first question is *which arrow failed?*

## APIs: how you ask for the data

An **API** is the set of things one program will let another program ask it to do. Not a technology — an agreement.

The useful mental model is a counter with a menu. You can order anything on the menu, in the format the menu specifies. You cannot walk into the kitchen and rummage.

Two things follow from that:

- **The menu is a design decision.** Somebody chose what could be asked for and what comes back. That somebody should include a designer.
- **You don't need to know how the kitchen works.** Which is exactly why APIs let you build far more than you could write yourself.

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

### Asking for it from your page

Here is the JavaScript we skipped in week one. Three lines do the whole job:

```js
const response = await fetch("https://api.example.com/weather?city=Bengaluru");
const data = await response.json();
document.querySelector("#temp").textContent = data.temp;
```

Read it out loud:

1. **`fetch`** — go and ask that URL for something. `await` means *wait for the answer before carrying on*, because it's coming over the internet and that takes time.
2. **`.json()`** — turn the reply into data JavaScript can use.
3. **`querySelector("#temp")`** — find the element with `id="temp"` and put the value in it.

`querySelector` takes the exact same selectors you learnt in L3 — `#temp` for an id, `.card` for a class, `h1` for a tag. That's the whole reason we did selectors properly.

You will mostly have AI write this. But when it hands you fifty lines, you now know which three are doing the work.

### GraphQL, in one idea

REST gives you whatever the endpoint gives you — often much more than you need, sometimes less, so you make three calls. **GraphQL** flips it: one endpoint, and the *request* says exactly which fields you want back.

```text
{ user(id: 42) { name, avatar } }   →   just the name and the avatar
```

Fewer round trips, no wasted data. More work to set up. You should be able to tell them apart in a conversation; you don't need to write either by hand today.

### API keys — read this bit twice

Most useful APIs make you register and give you a **key**: a long string that identifies you, tracks your usage, and gets billed to you.

**A key in your front-end code is a key you have published.** Your repo is public. View Source is one click. People run bots that scan GitHub for keys, and they will spend your credits.

So:

- Never paste a key into `scripts.js`, and never commit one.
- Keys belong on the back-end, or in the environment variables of a host like Vercel or Netlify.
- If you leak one, **revoke it immediately** and issue a new one. Deleting the commit does not help — it's in the history, which is exactly what L2 was about.
- "Free" APIs have rate limits. Read them before you design something that calls the API on every keystroke.

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

## Class Activity

**First**, pick a public API — weather, movies, transit, cat pictures — and open its URL directly in your browser. Look at the raw JSON. Find one field you'd want on a page and say which element you'd put it in.

**Then**, get a Firebase project created and a guestbook writing to it. Get it live on your github.io URL, open it on your laptop and your phone at once, and type on one.

## Homework

- **Exercise:** [[Exercise - Add a Database]] — use AI to add persistence to a small page: a guestbook, a poll, or an RSVP. Something must survive a refresh.
- Sketch the data model of an app you use every day. What are its tables, and what fields does each one have? Bring the sketch — we'll compare.
