---
date: 22-09-2026
date modified: 22-09-2026
feed: show
key_areas:
  - "Browser storage"
  - "Databases — SQL"
  - "Databases — NoSQL"
  - "Server-side languages"
  - "Understanding data flow"
tag: lecture
title: "Lecture 6 - localStorage and Databases"
---

## Homework Review

Let's look at your submissions!

- [[Exercise - Weather in the Footer]]

All the sites you have made so far (even with interactivity) reset on refresh.

Imagine if Gmail forgot that an email is read after each refresh. Or that Instagram forgot that you liked a photo when you opened the app again.

Adding some way to remember things allows us to build interactions where the state persists.

## localStorage and sessionStorage

The simplest way to remember something is to save it in the visitor's browser. Every browser lets each website keep a small amount of data, called **localStorage**. Anything your page saves there is still there the next time the page loads, even if they close the tab or restart their laptop.

Browsers also have a second, similar store called **sessionStorage**. It works the same way, but it's limited to your current tab and gets cleared when you close the tab.

You can store pairs of names and values like this:

```js
localStorage.setItem("theme", "dark");
localStorage.getItem("theme");
localStorage.removeItem("theme");
```

1. **`setItem`** — save the value `"dark"` under the name `"theme"`.
2. **`getItem`** — give me whatever is saved under `"theme"`. Here, `"dark"`.
3. **`removeItem`** — forget it.

You can see what any site has saved: open DevTools → **Application**, expand **Local storage**, and click the site's address underneath it.

### Try it: localStorage and sessionStorage

Type something into each box and click Save. Then:

1. **Refresh the page.** Both values are still there.
2. **Open this page in a new tab.** Only the localStorage value is there — a new tab is a new session.
3. **Close this tab and open the page again.** The localStorage value is still there. The sessionStorage one is gone.

Open DevTools while you do this. Under **Application**, expand **Local storage** and **Session storage** and click this site's address under each one. You'll see a key called `tech1-demo` with whatever you typed.

<div class="storage-demo">
  <div class="storage-demo-row">
    <label for="demo-local">localStorage</label>
    <input id="demo-local" type="text" placeholder="Type something">
    <button type="button" data-store="local" data-action="save">Save</button>
    <button type="button" data-store="local" data-action="clear">Clear</button>
    <p class="storage-demo-status" id="demo-local-status"></p>
  </div>
  <div class="storage-demo-row">
    <label for="demo-session">sessionStorage</label>
    <input id="demo-session" type="text" placeholder="Type something">
    <button type="button" data-store="session" data-action="save">Save</button>
    <button type="button" data-store="session" data-action="clear">Clear</button>
    <p class="storage-demo-status" id="demo-session-status"></p>
  </div>
</div>
<style>
.storage-demo { border: 1px solid var(--color-border); border-radius: 8px; padding: 1rem; margin: 1.5rem 0; display: grid; gap: 1rem; }
.storage-demo-row { display: flex; flex-wrap: wrap; align-items: center; gap: 0.5rem; }
.storage-demo-row label { font-family: var(--font-mono); font-size: 0.9rem; min-width: 9rem; }
.storage-demo-row input { flex: 1 1 10rem; font: inherit; padding: 0.4rem 0.6rem; border: 1px solid var(--color-border); border-radius: 6px; background: var(--color-bg-main); color: var(--color-text-main); }
.storage-demo-row button { font: inherit; padding: 0.4rem 0.8rem; border: 1px solid var(--color-border); border-radius: 6px; background: var(--color-bg-sub); color: var(--color-text-main); cursor: pointer; }
.storage-demo-status { flex-basis: 100%; margin: 0; font-size: 0.85rem; color: var(--color-text-sub); }
</style>
<script>
(function () {
  const stores = { local: window.localStorage, session: window.sessionStorage };
  const key = "tech1-demo";
  function show(name) {
    const saved = stores[name].getItem(key);
    document.getElementById("demo-" + name).value = saved || "";
    document.getElementById("demo-" + name + "-status").textContent =
      saved ? "Saved: \"" + saved + "\"" : "Nothing saved yet.";
  }
  document.querySelectorAll(".storage-demo button").forEach(function (button) {
    button.addEventListener("click", function () {
      const name = button.dataset.store;
      if (button.dataset.action === "save") {
        stores[name].setItem(key, document.getElementById("demo-" + name).value);
      } else {
        stores[name].removeItem(key);
      }
      show(name);
    });
  });
  show("local");
  show("session");
})();
</script>

Some things to note:

- **It's only on this browser, on this device.** Something saved on your laptop will not be available on your phone. Each website visitor has their own storage, and you can't see theirs.
- **Values are always text.** If you save the number `18`, you get back `"18"`.
- **Anyone using the browser can read it**, so don't keep anything private in it.

This makes localStorage good for preferences — a theme, a font size, a dismissed banner. It can't help with the Instagram example, because a like has to be seen by other people on other devices. For that you need a database.

## Class Exercise: A Theme That Remembers

Add a few colour themes to your site and save the visitor's choice in localStorage, so it's still there after a refresh.

[[Exercise - A Theme That Remembers]]

## Databases: memory for your app

A database is a program that stores data safely and hands it back fast. There are two main types:

**SQL** (pronounced Sequel) databases (Postgres, MySQL, SQLite) store **tables** — rows and columns, like a spreadsheet, except the rules are enforced. You declare up front that a `users` table has an `email` that is text and unique, and the database refuses anything else. Most serious products when the shape of your data is known and things relate to each other use **SQL**.

| id | name | email | joined |
| --- | --- | --- | --- |
| 1 | Aditya | aditya@jsid.com | 2026-08-04 |
| 2 | Nidharna | nidharna@jsid.com | 2026-08-11 |

**NoSQL** databases (Firebase, MongoDB) store **documents** — basically the JSON from earlier, each free to have a slightly different shape. **NoSQL** makes sense when the shape varies, or you're moving fast and don't know it yet.

Here are the same two users as NoSQL documents:

```json
{
  "name": "Aditya",
  "email": "aditya@jsid.com",
  "joined": "2026-08-04"
}
```

```json
{
  "name": "Nidharna",
  "email": "nidharna@jsid.com",
  "joined": "2026-08-11",
  "portfolio": {
    "url": "https://nidharna.github.io",
    "projects": [
      { "title": "Weather widget", "year": 2026 },
      { "title": "Brand identity", "year": 2025 }
    ]
  },
  "skills": ["Figma", "CSS"]
}
```

Nidharna has two fields Aditya doesn't, and `portfolio` has more data nested inside it: a URL and a list of projects. In a SQL table you'd have to add columns for everyone first, and the projects would need a separate table of their own. Here, each document just has whatever it needs.

We will explore a NoSQL database, specifically **Firebase Realtime Database**.

## Firebase Realtime Database

Firebase is a set of back-end services run by Google.

**Realtime Database** is one of them: a database that Google hosts for you, which your page can read from and write to directly with a few lines of JavaScript. You don't have to set up or run a server, and the free plan is more than enough for class projects.

The "realtime" part means that when the data changes, every open page that's reading it gets the new version straight away, without a refresh. Most databases only answer when you ask. Realtime Database keeps a connection open and tells you when something changes. It's how chat apps and live cursors in Figma feel instant.

We're using it because it's the shortest way to take the static sites you've built so far and give them data that's saved and shared between visitors.

### It's one big JSON tree

We looked at JSON responses from APIs in the last lecture. When using Firebase Realtime Database, the whole database is a single JSON object, and you read and write at **paths** inside it.

Suppose you wanted a guestbook where a vistor on your site could leave a message. The data might look something like this.

```json
{
  "guestbook": {
    "-Nx8kQ2p": {
      "name": "Upasna",
      "message": "hello!",
      "at": 1756089600000
    },
    "-Nx8kR7t": {
      "name": "Shivangi",
      "message": "nice site",
      "at": 1756089900000
    }
  }
}
```

`guestbook/-Nx8kQ2p/name` is a path, and it points at `"Upasna"`. There are no tables, no columns, and no `SELECT`. If you can navigate a Figma layer panel, you can navigate this.

Those random numbers (like 0Nx8kQ2p) are keys — are generated for you when you `push` a new item. They are unique and they sort chronologically (oldest first).

In code, you point at a path with `ref`, and then read what's there with `get`:

```js
const nameRef = ref(db, "guestbook/-Nx8kQ2p/name");
const snapshot = await get(nameRef);
snapshot.val();   // "Upasna"
```

Read it out loud:

1. **`ref(db, "guestbook/-Nx8kQ2p/name")`** — point at that path in the tree. It's the same path, written the same way.
2. **`get(nameRef)`** — go and fetch whatever is there. Like `fetch` in L5, it comes over the internet, so we `await` it.
3. **`snapshot.val()`** — the value itself.

The path can stop at any level. `ref(db, "guestbook/-Nx8kQ2p")` gives you Upasna's whole entry — name, message and time. `ref(db, "guestbook")` gives you every entry. Whatever is below the path comes back with it, so point at the smallest part of the tree you need.

`get` reads once. Further down, we'll use `onValue` instead, which reads now and again every time the data changes.

### The "realtime" part

You don't fetch the data — you **subscribe** to it. Firebase pushes changes to every connected browser as they happen.

Open your guestbook on your laptop and your phone. Type on the phone. The laptop updates. Nobody refreshed anything. Without something like Realtime Database this would be a lot harder to do.

### Firebase Realtime Database is a bit different from a standard database

Some unusual things to keep in mind.

| Normal database | Firebase Realtime Database |
| --- | --- |
| Your back-end talks to it; the browser never does | The browser holds a connection straight to it |
| You **request**, it **responds**, done | You **subscribe**, it **pushes**, forever |
| Tables, rows, and a query language | One JSON tree, addressed by path |
| Writes go to the server, then come back | Writes apply on your device first, sync after |

### Security rules, and the key that isn't a secret

**Your Firebase config is public, and that's fine.** It goes straight into your HTML. It is not a password — it's an address, telling the browser which project to talk to. Everyone can see it and Google intends that.

**Which means your database is protected only by its rules.** Rules are a small JSON document deciding who may read and write where. Test mode gives you this:

```json
{ "rules": { ".read": true, ".write": true } }
```

That reads: *anyone on the internet may read everything and write anything.* Fine for a class exercise this week; genuinely dangerous for anything real. Firebase makes test mode expire after 30 days on purpose, and when it does your app will stop working and you will have forgotten why.

Before your final project goes anywhere near real people, the rules need tightening — at minimum so that people can add entries but not delete each other's, and so nobody can dump the whole tree. Ask AI to write rules for your specific shape and *read what it gives you.*

> If strangers can write to your database, strangers will write anything to your database. Deciding what your app does about that is design work, and we'll come back to it.

## Class Activity — The Wall

It's a grid of squares. You click a square, it becomes your colour. It becomes your colour *on everyone else's screen too*, immediately. All the students editing one JSON tree, no refreshing.

> **Sidenote:** You already know what this feels like — it's the thing that makes Figma feel like Figma. Today you find out that multiplayer is not magic, it's a database that pushes.

- The wall is at [gyanl.com/wall](https://gyanl.com/wall), and its code is public at [github.com/gyanl/wall](https://github.com/gyanl/wall).

- When you open the page, it asks for your name and a colour. It saves them in localStorage, so it only asks once.

- The data is small: one entry per square, keyed by its position, with the colour and the name of whoever painted it last:

```json
{
  "wall": {
    "0": { "colour": "#ff4343", "name": "Upasna" },
    "1": { "colour": "#6694ff", "name": "Shivangi" },
    "47": { "colour": "#ff4343", "name": "Upasna" }
  }
}
```

- It uses Firebase Realtime Database. The database's address is in `firebase-config.js`, so anyone who looks can find it.

- The leaderboard counts how many squares each name owns.

### Things to notice while we're doing it

- **Nobody wrote any code to receive other people's clicks.** You subscribed to a path. That's the whole of multiplayer.
- **Turn off the wifi and keep clicking.** Your squares still fill in — that's the local cache. Turn it back on and watch them arrive on the projector at once.
- **Somebody is going to draw something rude on the projector.** Good. That's `.write: true` in the rules, on a database with no server in front of it, and it's the most memorable security lesson available. What would you have to change to stop it?
- **Watch what happens when two people click the same square.** Last write wins. Nobody's edit is merged — compare that to what Git did for you in week two.

That's everything a stranger would have too.

## Class Activity 2 - Hack the Wall!

The [class wall](https://gyanl.com/wall) is open on purpose. The page only lets you paint one square at a time in your own colour, but the page isn't what protects the data. The database rules are.

Your goal is to get to the top of the leaderboard, by any means. You won't do it by clicking. You'll get your AI agent (Claude Code, Cursor, or whatever you use) to talk to the database directly, the way anyone on the internet could. Then we'll switch on some rules and try again.

By the end you should be able to answer two questions for any app: **who should be able to read this data, and who should be able to write it?**

> **Only do this to the class wall, and only in class.** It's our database and you have permission. Doing the same thing to someone else's site without permission could be illegal and chances are your AI agent will refuse.

The wall is at [gyanl.com/wall](https://gyanl.com/wall), and the code is at [github.com/gyanl/wall](https://github.com/gyanl/wall). Open the page on your laptop and your phone.

Open `script.js` and you'll find the same three moves as the guestbook: `ref` to point at a path, `set` to write to it, and `onValue` to subscribe to it. The CSS uses `grid` rather than flexbox, because a wall of equal squares is a real two-dimensional grid, not a row that wraps.

## Homework

- **Exercise:** [[Exercise - Realtime Web Experience]] — build something that more than one person can use at the same time. It can be a game or another interactive experience.
