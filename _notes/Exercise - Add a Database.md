---
date: 24-07-2026
date modified: 24-07-2026
feed: show
tag: exercise
title: "Exercise - Add a Database"
---
### Make something that remembers

Everything you've built so far forgets on refresh. Build a small app where data persists — a guestbook, a class poll, an RSVP page, a tiny leaderboard.

### Steps

1. **Pick a one-table idea.** Guestbook (name + message), poll (option + votes), RSVP (name + yes/no). Resist anything bigger.
2. **Design the schema first, on paper.** What fields? What types? This is a design decision — a guestbook that stores email addresses is a different (worse) product.
3. **Ask AI to build it** with a hosted database (Supabase or similar free tier). Let it wire up the form → database → display loop.
4. **Find your data.** Open the database dashboard and look at the actual rows. Add a row *from the dashboard* and watch it appear in your app.
5. **Test with the class.** Share your URL; let others write to your database. Watch what real users do to your assumptions (and your data).

### Things to keep in mind

- If strangers can write to it, strangers will write *anything* to it. What does your app do about that? (This is your first content-moderation and security conversation.)
- Never let the AI put secret keys in front-end code. Ask it "are any secrets exposed in the client?" and see what it says.

### Submission

- Live URL + a screenshot of your database rows + your paper schema sketch.
