---
date: 01-09-2026
date modified: 25-08-2026
feed: show
tag: exercise
title: "Exercise - Add a Database"
---
### Make something two people can use at once

Everything you built before this week forgets on refresh, and none of it knows anyone else exists. Fix both. Build a small thing backed by Firebase Realtime Database, live on your github.io URL.

The bar is deliberately specific:

- Something **survives a refresh**.
- Something **appears on another person's screen without them refreshing**.

If you can't demo the second one with a friend's phone next to your laptop, it isn't done.

### Pick something small

One path in the tree. Resist anything bigger — the interesting part is the liveness, not the feature list.

- **Guestbook** — name, message, live list
- **Class poll** — four options, counts that move while people vote
- **Reaction wall** — buttons that fire an emoji onto everyone's screen
- **Shared to-do** — anyone can add, anyone can tick
- **Now playing** — one person sets the song, everyone sees it
- **Queue** — put your name down, watch the list reorder

### Steps

1. **Sketch the tree on paper first.** What paths exist, and what's at each one? A guestbook that stores email addresses is a different — and worse — product than one that doesn't. This is the design decision, and it takes five minutes.
2. **Make your own Firebase project.** Not the class one. Realtime Database, test mode for now, register a web app, copy the config.
3. **Build it.** Use AI freely, but you write the tree structure. When it hands you code, find the three moves from class: the `ref` to a path, the write (`push` or `set`), the `onValue` subscription.
4. **Look at your data in the console.** Add an entry *from the Firebase console* and watch it appear in your app without you touching the page. Screenshot that.
5. **Push it live and test it properly.** Your github.io URL, open on two devices at once.
6. **Let the class at it.** Share your URL. Watch what people actually do to your assumptions.

### Then answer these

Write a short paragraph on each — this is the graded thinking, not the code:

- **What did people do to your data that you didn't expect?** Rudeness, spam, empty submissions, thousand-character messages, all of the above?
- **Your rules are currently `true` for read and write.** In plain language: what could a stranger do to this if they wanted to? Name one rule you'd add before this went in front of real people.
- **What happens when it's empty?** Before anyone has posted, what does your page show? "Nothing at all" is a design failure, not a neutral default.

### Things to keep in mind

- Your Firebase config goes in your HTML and that's fine — it's an address, not a password. Your **rules** are the security. Don't confuse the two.
- Test mode expires after 30 days and your app will silently stop working. Note the date somewhere.
- Keep the tree shallow. Reading a path downloads everything under it.
- Design the empty state, the loading state and the too-long-message state. Those are the ones AI skips and users find in ten seconds.

### Submission

- Live URL
- Your paper sketch of the tree
- A screenshot of your data in the Firebase console
- The three paragraphs above
