---
date: 11-08-2026
date modified: 08-08-2026
feed: show
tag: exercise
title: "Exercise - Build the Page You Designed"
---
### Make the real page match your Figma

Last week you designed your home page in Figma. This week you build it. The design already exists, so this is a translation exercise — which is exactly the job.

### What it must have

1. **Colour variables.** Every colour defined once in `:root`, used everywhere with `var()`. No hex codes scattered through the file.
2. **A working dark mode.** Using `prefers-color-scheme`. Adjust your accent colour if it doesn't hold up on a dark background.
3. **A font from Google Fonts,** loaded with a `<link>`, with a fallback in your `font-family`. Only the weights you actually use.
4. **`rem` for type and spacing.** `px` only where it belongs — borders and hairlines.
5. **At least one breakpoint** that you chose by dragging your window until the design stopped working. Not a number you copied from a blog post.
6. **At least 5 commits** with messages that say what changed and why. "update" ×5 doesn't count.
7. **One deliberate divergence, resolved.** Details below.

### The Git part

You've been pushing in a straight line so far. This week you make the two copies disagree on purpose, and fix it — so the first time it happens by accident, in your group project, it's boring.

1. Work locally as usual. Commit as you go.
2. At some point, go to **github.com** and edit a file **in the browser** — change a line of your CSS, commit it there.
3. Back in GitHub Desktop, make a change locally too, and commit.
4. Try to **Push**. It should be rejected — GitHub has a commit you don't.
5. **Pull**, deal with whatever Git says, then push.

Do it once where the two edits touch **different lines** (Git merges it for you), and once where they touch **the same line** (you get a conflict and decide who wins).

**Write down what you saw.** What did the rejection message say? What did the conflict markers look like? Which version did you keep?

> **Commit messages:** write them for the version of you that comes back in three weeks. *"Add dark mode colours"* is useful. *"changes"* is not. This is the "checkpoints labelled with why" thing from class — practise it here where nothing is at stake.

### Steps

1. Open your Figma file next to your editor. Start with the type and colours before you touch layout.
2. Get it right at **one width first** — narrow. Then widen your window until it looks wrong, and add your breakpoint there.
3. Test on your actual phone, over your github.io URL or Simple Web Server. Things always feel different in the hand.
4. Push. Check the live site, not just your laptop.

### Things to keep in mind

- **It will not match perfectly, and that's the interesting part.** Text renders differently, your Figma spacing may not survive contact with a browser. Note where you had to compromise — that's the discussion for next class.
- **If you're stuck, ask AI** — but ask it to explain the CSS it gives you. You should be able to point at any line and say what it does.
- **Design decisions still matter.** Line length, hierarchy, contrast. A responsive page that's ugly is not a pass.

### Submission

- Your live URL
- Two screenshots: narrow and wide
- One screenshot of your commit history
- One line: at what width is your breakpoint, and what broke there?
- A few lines on the Git part: what the rejected push said, what the conflict looked like, and how you resolved it
