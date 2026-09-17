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
title: "Lecture 6 - Databases"
---

## Homework Review

Let's look at your submissions!

- [[Exercise - Weather in the Footer]]


## Databases: memory for your app

A database is a program whose entire job is to store data safely and hand it back fast. It isn't a file you open — you talk to it through code.

There are two broad families, and you should be able to tell them apart in a meeting:

**SQL** databases (Postgres, MySQL, SQLite) store **tables** — rows and columns, like a spreadsheet, except the rules are enforced. You declare up front that a `users` table has an `email` that is text and unique, and the database refuses anything else. most serious products when the shape of your data is known and things relate to each other use **SQL**.

| id | name | email | joined |
| --- | --- | --- | --- |
| 1 | Ada | ada@example.com | 2026-08-04 |
| 2 | Grace | grace@example.com | 2026-08-11 |

**NoSQL** databases (Firebase, MongoDB) store **documents** — basically the JSON from earlier, each free to have a slightly different shape. **NoSQL** makes sense when the shape varies, or you're moving fast and don't know it yet. 

We're using NoSQL, specifically **Firebase Realtime Database**, for one reason: it is the shortest path from a static page to something that remembers, and it has the added advantage of making it very easy to make real-time apps. 

## Firebase Realtime Database

### It's one big JSON tree

We looked at JSON responses from APIs in the last lecture. When using Firebase Realtime Database, the whole database is a single JSON object, and you read and write at **paths** inside it.

```json
{
  "guestbook": {
    "-Nx8kQ2p": { "name": "Ada",   "message": "hello!",  "at": 1756089600000 },
    "-Nx8kR7t": { "name": "Grace", "message": "nice site", "at": 1756089900000 }
  }
}
```

`guestbook/-Nx8kQ2p/name` is a path, and it points at `"Ada"`. There are no tables, no columns, and no `SELECT`. If you can navigate a Figma layer panel, you can navigate this.

Those ugly keys — `-Nx8kQ2p` — are generated for you when you `push` a new item. They're unique and they sort chronologically (oldest first), which is why lists here are objects rather than arrays: two people posting at once can't fight over index `3`.

### The "realtime" part is the fun bit

You don't fetch the data — you **subscribe** to it. Firebase pushes changes to every connected browser as they happen.

Open your guestbook on your laptop and your phone. Type on the phone. The laptop updates. Nobody refreshed anything. Without something like Realtime Database this would be a lot harder to do.

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
