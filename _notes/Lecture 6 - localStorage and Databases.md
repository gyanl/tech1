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
title: "Lecture 6 - LocalStorage and Databases"
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

### Setting it up

1. Go to [console.firebase.google.com](https://console.firebase.google.com) and **Add project**. Skip Google Analytics.
2. In the left sidebar, **Build → Realtime Database → Create Database**. Pick a location.
3. Choose **Start in test mode** for now. Read the warning in the next section before you leave it that way.
4. Back on the project overview, click the **`</>`** (web) icon to register a web app. Firebase gives you a config snippet — copy it.
5. Paste the config into your AI coding agent and tell it to help you set up a feature. Some ideas below:

| Idea | What it does | What's in the tree |
| --- | --- | --- |
| **Live Q&A for a talk** | The audience posts questions and upvotes them. The speaker's screen shows the top ones. | `questions/{id}` with the text and a vote count |
| **Crit board** | Everyone pins a link to their work. Classmates leave short comments that appear on the projector as they're written. | `projects/{id}` and `comments/{projectId}/{id}` |
| **Group order** | One link for the table. Everyone adds what they want from the menu, and the total updates for everyone. | `order/{id}` with name, item and price |
| **Watch party remote** | One person presses play or pause, and the video pauses on everyone's screen. | `player` with `playing` and the current time |
| **Collaborative moodboard** | Anyone can drop an image URL onto a shared canvas and drag it around. Everyone sees it move. | `images/{id}` with URL and x, y position |
| **Live scoreboard** | Keep score for a match or a quiz night from your phone. The big screen updates. | `teams/{id}` with name and score |
| **Seat or slot booker** | A grid of slots. Tap one to claim it; it's greyed out for everyone else straight away. | `slots/{id}` with who booked it |
| **Presence** | A small "3 people are looking at this page" indicator for your portfolio. | `online/{visitorId}` — added on arrival, removed on leaving |

> **Sidenote:** The console will try to steer you to **Cloud Firestore**, which is Firebase's newer, more capable database. It's the better choice for a real product, but you can ignore it for now.

### Security rules, and the key that isn't a secret

**Your Firebase config is public, and that's fine.** It goes straight into your HTML. It is not a password — it's an address, telling the browser which project to talk to. Everyone can see it and Google intends that.

**Which means your database is protected only by its rules.** Rules are a small JSON document deciding who may read and write where. Test mode gives you this:

```json
{ "rules": { ".read": true, ".write": true } }
```

That reads: *anyone on the internet may read everything and write anything.* Fine for a class exercise this week; genuinely dangerous for anything real. Firebase makes test mode expire after 30 days on purpose, and when it does your app will stop working and you will have forgotten why.

Before your final project goes anywhere near real people, the rules need tightening — at minimum so that people can add entries but not delete each other's, and so nobody can dump the whole tree. Ask AI to write rules for your specific shape and *read what it gives you.*

> If strangers can write to your database, strangers will write anything to your database. Deciding what your app does about that is design work, and we'll come back to it.

## Class Activity — the class wall

We're going to build one thing together, into **one shared database**, and put it on the projector.

It's a grid of squares. You click a square, it becomes your colour. It becomes your colour *on everyone else's screen too*, immediately. Thirty of you, one JSON tree, no refreshing.

> **Sidenote:** You already know what this feels like — it's the thing that makes Figma feel like Figma. Today you find out that multiplayer is not magic, it's a database that pushes.

### How this works

I've made one Firebase project for the class and put a page on it. Everyone opens the same page, so we're all reading and writing the same tree.

![The class wall: a grid of dark squares, some coloured red, blue and green by different people](assets/img/class-wall.png)

Here's what happens when you click a square:

1. **Your page writes one entry.** Clicking square 47 saves your colour and name at the path `wall/47` in the database. Your own square changes straight away, without waiting for the database.
2. **Firebase tells everyone.** Every page that has the wall open is subscribed to the `wall` path. When anything under it changes, Firebase sends the new data to all of them.
3. **Every page repaints.** Each page gets the full list of coloured squares and colours its grid to match. That includes the projector, your phone, and your own page.
4. **Every page recounts the leaderboard.** The leaderboard isn't saved anywhere. Each page counts how many squares each name owns, every time the wall changes.

```text
   YOUR PAGE                  FIREBASE                         EVERYONE'S PAGES

   click square 47  ───────▶  wall/47 = { colour, name }  ───▶  repaint the grid
                                                                 and recount the leaderboard
```

Compare it to the round trip from L5. There's no server of our own in the middle, and nobody asks for the new data: Firebase sends it as soon as it changes.

When you open the page, it asks for your name and a colour. It saves them in localStorage, so it only asks once.

The data is small: one entry per square, keyed by its position, with the colour and the name of whoever painted it last:

```json
{
  "wall": {
    "0": { "colour": "#ff4343", "name": "Upasna" },
    "1": { "colour": "#6694ff", "name": "Shivangi" },
    "47": { "colour": "#ff4343", "name": "Upasna" }
  }
}
```

Note we're using `set` at a specific path here, not `push`. `push` is for *adding to a list* where the order matters and the keys should be unique. `set` is for *this exact path gets this exact value* — square 47 is one square, and writing to it replaces what was there. Which is why the last person to click a square wins it.

### The code

The wall is at [gyanl.com/wall](https://gyanl.com/wall), and the code is at [github.com/gyanl/wall](https://github.com/gyanl/wall). Open the page on your laptop and your phone.

Open `script.js` and you'll find the same three moves as the guestbook: `ref` to point at a path, `set` to write to it, and `onValue` to subscribe to it. The CSS uses `grid` rather than flexbox, because a wall of equal squares is a real two-dimensional grid, not a row that wraps.

### Things to notice while we're doing it

- **Nobody wrote any code to receive other people's clicks.** You subscribed to a path. That's the whole of multiplayer.
- **Turn off the wifi and keep clicking.** Your squares still fill in — that's the local cache. Turn it back on and watch them arrive on the projector at once.
- **Somebody is going to draw something rude on the projector.** Good. That's `.write: true` in the rules, on a database with no server in front of it, and it's the most memorable security lesson available. What would you have to change to stop it?
- **Watch what happens when two people click the same square.** Last write wins. Nobody's edit is merged — compare that to what Git did for you in week two.

### Then, on your own

Make your own Firebase project — your own config, your own tree — and get a **guestbook** working on your github.io page: a name, a message, a list that updates live. That's the shape you'll extend for homework.

## Project ideas

Some things you could build with Realtime Database. Each one works because several people see the same data change at the same time. The homework ([[Exercise - Add a Database]]) has smaller starting points; these are bigger, and some could grow into a final project.


When you pick one, start by sketching the tree. Some things to think about:

- **What happens when two people do the same thing at once?** Two people booking the same slot is a real problem. Two people adding to an order isn't.
- **Who's allowed to change what?** In the watch party, should everyone control the video, or only the host?
- **What does the page show before anyone has done anything?**

## Building it with AI

You'll have AI write most of the Firebase code. These prompts work in Claude, Cursor or ChatGPT. Replace the parts in square brackets. Each one asks for small steps and explanations, so you can follow what the code does and spot when it's wrong.

**1. Plan the data before any code**

```text
I'm building [a live Q&A board for a class talk] as a static website (HTML, CSS, JavaScript, no framework) using Firebase Realtime Database.

Before writing any code, suggest the shape of the JSON tree: which paths exist and what goes at each one. Keep it as shallow and small as possible. Show an example of the tree with 2–3 items of sample data, and explain each choice in one line.
```

**2. Connect the page to Firebase**

```text
Here is my Firebase config:
[paste the firebaseConfig object from the Firebase console]

Write the smallest possible code to connect my index.html to Firebase Realtime Database, using the Firebase JavaScript SDK loaded from the CDN in a <script type="module">. No npm, no build step. Then add one button that writes a test value to the path "test" so I can check it appears in the Firebase console.
```

**3. Build the feature**

```text
My database tree looks like this:
[paste your tree from prompt 1]

Write the HTML and JavaScript so that:
- [people can type a question and submit it]
- [everyone sees the list of questions update live, without refreshing]
- [clicking a question upvotes it]

Use push() for new items, set() or runTransaction() for updates, and onValue() to subscribe. Put the Firebase code in its own section and add a short comment above each part saying what it does.
```

**4. Design the states AI usually skips**

```text
Improve this page so it handles:
- the empty state, before anyone has added anything
- the loading state, while data is still arriving
- an empty or very long submission
- losing the internet connection

Keep my existing HTML and CSS classes. Tell me what you changed.
```

**5. Lock it down**

```text
My Realtime Database rules are currently read and write "true". Here's my tree:
[paste your tree]

Write security rules that allow anyone to read, and allow anyone to add new items, but stop people from deleting or editing other people's items, and limit text fields to 280 characters. Explain each rule in plain language.
```

When something doesn't work, paste the error from the browser console (DevTools → **Console**) into the chat along with the code. Most Firebase problems are a wrong path, a missing `await`, or rules that are blocking the read.

### Where to host it

Your site doesn't need anything new to use Realtime Database. The page talks to Firebase directly from the visitor's browser, so it works on GitHub Pages as it is. The Firebase config in your code is fine to publish — it says which database to use, and your rules decide what anyone can do with it.

If you want to try a different host, [[Help - Host on Vercel]] walks through deploying the same repo to Vercel. You'll need something like Vercel later, once a project has back-end code or secret API keys.

## Homework

- **Exercise:** [[Exercise - Add a Database]] — build something small that more than one person can use at the same time. Something must survive a refresh, and something must show up on someone else's screen without them refreshing.
- Sketch the data model of an app you use every day. What are its tables, and what fields does each one have? Bring the sketch — we'll compare.
