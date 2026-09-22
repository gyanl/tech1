---
date: 22-09-2026
date modified: 22-09-2026
feed: show
tag: exercise
title: "Exercise - Hack the Wall"
---

### Find out what a stranger could do to the class wall

The [class wall](https://gyanl.com/wall) is open on purpose. The page only lets you paint squares in your own colour, but the page isn't what protects the data. The database rules are.

In this exercise you'll skip the page and talk to the database directly, the way anyone on the internet could. Then we'll switch on some rules and try again. By the end you should be able to answer two questions for any app: **who should be able to read this data, and who should be able to write it?**

> **Only do this to the class wall, and only in class.** It's our database and you have permission. Doing the same thing to someone else's site without permission is illegal in most countries, including India.

### Setup

1. Open [gyanl.com/wall](https://gyanl.com/wall) and join with your name.
2. Open DevTools and go to the **Console** tab. You'll type everything here.
3. Paste this in and press Enter:

```js
const DB = "https://rtdb-test-7f656-default-rtdb.asia-southeast1.firebasedatabase.app";
```

That's the database's address. It's in the page's code, in `firebase-config.js`, so anyone who looks can find it.

Firebase lets you reach any path in the tree as a URL. Add `.json` to the end of the path, like the API URLs from [[Lecture 5 - APIs]]:

| Path in the tree | URL |
| --- | --- |
| `wall` | `DB + "/wall.json"` |
| `wall/47` | `DB + "/wall/47.json"` |
| the whole tree | `DB + "/.json"` |

You can read a URL with `fetch`, and write to it by adding a method: `PUT` replaces what's at a path, `PATCH` changes some of it, and `DELETE` removes it.

### Round 1: no rules

The database is in test mode: anyone can read and write anything. Try each of these, and keep the wall open on the projector or on your phone to see what happens.

**1. Read everything**

```js
await (await fetch(DB + "/.json")).json();
```

You get the whole database, not just what the page shows.

**2. Paint a square without clicking it**

```js
await fetch(DB + "/wall/0.json", {
  method: "PUT",
  body: JSON.stringify({ colour: "#00ff00", name: "YOUR NAME" })
});
```

**3. Paint as someone else**

Change `name` to a classmate's name and paint a square. The leaderboard gives them the point.

**4. Take the lead**

```js
const squares = {};
for (let i = 0; i < 100; i++) {
  squares[i] = { colour: "#00ff00", name: "YOUR NAME" };
}
await fetch(DB + "/wall.json", { method: "PATCH", body: JSON.stringify(squares) });
```

One request, and you own 100 squares.

**5. Break the page**

Try writing things the page would never write:

- a colour that isn't a colour: `{ colour: "hello", name: "YOUR NAME" }`
- a name that's 500 characters long: `"a".repeat(500)`
- a square that doesn't exist: `/wall/99999.json`
- something that isn't part of the wall at all: `/graffiti.json`

Watch what the page does with each one.

**6. Erase**

Delete one square:

```js
await fetch(DB + "/wall/0.json", { method: "DELETE" });
```

Don't delete the whole wall. We'll do that once, together, at the end.

### Round 2: with rules

Now I'll switch on these rules in the Firebase console:

```json
{
  "rules": {
    "wall": {
      ".read": true,
      "$square": {
        ".write": true,
        ".validate": "newData.hasChildren(['colour', 'name'])",
        "colour": { ".validate": "newData.isString() && newData.val().matches(/^#[0-9a-fA-F]{6}$/)" },
        "name": { ".validate": "newData.isString() && newData.val().length > 0 && newData.val().length <= 20" },
        "$other": { ".validate": false }
      }
    }
  }
}
```

Read them out loud:

1. **`"wall": { ".read": true }`** — anyone can read the wall. Nothing else in the tree is readable.
2. **`"$square": { ".write": true }`** — anyone can write to one square at a time. `$square` stands for any key under `wall`.
3. **`.validate`** — every square must have a `colour` and a `name`. The colour must look like `#ff4343`, the name must be 1–20 characters, and no other fields are allowed.

Run all six attacks again, and fill in this table:

| Attack | Round 1 | Round 2 |
| --- | --- | --- |
| Read everything | | |
| Paint a square without clicking | | |
| Paint as someone else | | |
| Take the lead with a script | | |
| Break the page | | |
| Erase a square | | |

### Then answer these

- **Which attacks did the rules stop, and which still work?** For each one that still works, why can't these rules stop it?
- **The rules can check what the data looks like, but not who sent it.** Anyone can type any name. What would the database need to know about the person writing, to stop someone painting as you?
- **Who should be able to read the wall, and who should be able to write to it?** Answer for the wall as it is now, and again for a version where only students in this class can paint.
- **Would you ever want the same rules for a real product?** Pick one of the [[Lecture 6 - localStorage and Databases#Project ideas|project ideas]] and write, in plain language, who should be able to read and write each part of its tree.

### Things to notice

- **The page was never the security.** Everything you did in Round 1, the page had no say in. Hiding a button doesn't stop anyone. Only the database can say no.
- **Rules can't know who you are without sign-in.** To stop impersonation, people have to log in first. Firebase Authentication gives each person an ID, and rules can then say things like *"you can only change squares you painted"*. That's also how you'd stop one person owning the whole wall.
- **Open isn't always wrong.** A wall anyone can paint is the point of this one. The mistake is leaving things open without deciding to.
