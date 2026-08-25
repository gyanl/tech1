---
date: 11-08-2026
date modified: 25-08-2026
feed: show
tag: exercise
title: "Exercise - Figma to Code"
---
### Make the real page match your Figma

Last week you designed your home page in Figma. This week you build it. The design already exists, so the exercise is to translate your designs into implementations in code.

### What it must have

1. **Colour variables.** Every colour defined once in `:root`, used everywhere with `var()`. No hex codes scattered through the file.
2. **A working dark mode.** Using `prefers-color-scheme`. Adjust your accent colour if it doesn't hold up on a dark background.
3. **A font from Google Fonts,** loaded with a `<link>`, with a fallback in your `font-family`. Only the weights you actually use.
4. **`rem` for type and spacing.** `px` only where it belongs — borders and hairlines.
5. **At least one breakpoint** that you chose by dragging your window until the design stopped working. Not a number you copied from a blog post.
6. **At least descriptive 10 commits** with messages that say what changed and why. "update" ×5 doesn't count.

### Steps

1. Open your Figma file next to your editor. Start with the type and colours before you touch layout.
2. Get it right at **one width first** — you can start on narrow/phone. Then widen your window until it looks wrong, and add your breakpoint there.
3. Test on your actual phone, over your github.io URL or Simple Web Server. Things can feel different on an actual device.
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
