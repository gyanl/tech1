---
date: 11-08-2026
date modified: 08-08-2026
feed: show
key_areas:
  - "CSS — styling"
  - "Responsive web design"
  - "Hosting and deployment"
  - "Version control (Git)"
tag: lecture
title: "Lecture 2 - CSS and Responsiveness"
---

## Designing your Website

Last week we shipped a page! This week we'll figure out how to ship your page.

> **Sidenote:** Can anyone tell me why do we *ship* software?

## What's a commit?

![](assets/img/Pasted image 20260811131706.png)

**Commit:** Make a checkpoint (locally)

**Fetch:** Check if any changes have been made on Github online since you last fetched, download them locally. This matters more when you are working collaboratively with other people on a repo. So far it's just you.

**Pull:** Bring those changes down and merge them into your copy.

**Push:** Upload your changes to Github online

## Steps for using Github Pages

1. Make changes.
2. Use Github to commit changes. This creates a checkpoint "locally".
3. Push to Github to push your changes online to Github.
4. Your updated website is now live at yourgithubusername.github.io


**Download Simple Web Server app**
[Download Simple Web Server](https://simplewebserver.org/)
This app is a quick and easy way to start a server on your computer, and allows you to test your website on your computer or any other device on the same wifi network - like your phone!

## Your computer and GitHub are two different places

This is the idea everything else depends on, and it's the one Figma has trained out of you.

In Figma, there is **one file** and everyone is inside it at once. You see other people's cursors. You never "send" your work anywhere.

Git is the opposite. There are **two separate copies** of your project — the one on your laptop, and the one on GitHub — and they only talk to each other when you tell them to. Nothing is automatic.

> **Sidenote:** Why would anyone want this? Because you can work offline, try something terrible, and throw it away without anyone seeing. The copies are a feature.

### What "origin" means

You'll notice every button says *origin*: **Fetch origin**, **Pull origin**, **Push origin**.

`origin` is just a **nickname for the GitHub copy** of your project.

When you cloned the repo, Git saved its web address and needed something to call it. The default nickname is `origin` — as in *the place this originally came from*. That's the whole story. There's no magic in the word.

So read the buttons like this:

- **Push origin** → send my commits to GitHub
- **Pull origin** → bring GitHub's commits down to me

### Commits are a chain, not a pile

Each commit records what came before it. Your project's history is a chain of checkpoints in a specific order.

This matters because it's why Git can't just mash two versions together — it needs to know what order things happened in.

### Your computer only *remembers* what's on GitHub

Here's the part that surprises people.

GitHub Desktop is not watching GitHub. It's showing you what GitHub looked like **the last time it checked**. It has no live connection.

**Fetch** is the act of asking, rather than assuming:

- **Fetch** — "GitHub, anything new?" Changes nothing in your files. Completely safe.
- **Pull** — "Send it down, and merge it into my work."
- **Push** — "Here are my commits."

### Why a push sometimes gets rejected

If GitHub has commits you don't have, *and* you have commits GitHub doesn't have, the chain has **forked**. Two versions of history now exist.

Git refuses to push, because to accept it, it would have to throw one side away — and it doesn't know which one is precious to you.

> **A rejected push is Git protecting your work, not Git breaking.** Read the message, don't start clicking buttons.

The fix is always the same: **pull first**, let the two histories merge, then push.

### A merge conflict is a question, not an error

Most of the time Git merges the two sides by itself — if you changed the CSS and someone else changed the HTML, there's nothing to argue about.

It only stops and asks when **the same lines** changed on both sides. It can't know whose version is right, so it shows you both and waits:

```
<<<<<<< YOUR VERSION
background: #ff4343;
=======
background: #2b6cb0;
>>>>>>> THE VERSION FROM GITHUB
```

Delete the markers, keep the lines you want, save, commit. That's it.

### When this will actually happen to you

Right now you're one person on one laptop, so this may never bite. It will the moment any of these is true:

1. **You edit a file on github.com** — fixing a typo in the browser is the fastest way to make the two copies disagree. This one gets people in week one.
2. **You use two computers** — a lab machine and your own.
3. **Your final project is a team of up to three.** This is the real reason we're covering it now: by Week 11 it needs to be a reflex.

### The habit

Not "fetch before you push" — that's fixing the problem. Do this instead:

> **Before you start working, hit Fetch origin. If the button changes to Pull origin, pull before you touch anything.**

Sync at the start, not at the end. Then a rejected push mostly stops happening.

### Let's break it on purpose

*(In class — watch, then do it yourself.)*

1. On **github.com**, edit `index.html` in the browser and commit the change there.
2. In **VS Code**, edit a *different* line of the same file. Commit in GitHub Desktop.
3. Hit **Push**. Watch it get rejected — the two copies have diverged.
4. **Pull**. Git merges both changes by itself, because they touched different lines.
5. **Push** again. It works.

Now do it a second time, but in step 2 edit **the same line** you edited in the browser. This time you get a conflict, and you decide who wins.

## Colour variables, and dark mode

Before we style anything: decide your colours **once**, in one place.

CSS lets you name a value and reuse it. These are called *custom properties*, or just variables:

```css
:root {
  --bg: #ffffff;
  --text: #1a1a1a;
  --accent: #ff4343;
}

body {
  background: var(--bg);
  color: var(--text);
}

a {
  color: var(--accent);
}
```

`:root` just means "the whole page". Now changing `--accent` in one line recolours every link on your site. This is a design system in four lines — the same idea as styles in Figma.

### Dark mode is (almost) free

Because your colours are named, you can hand the browser a second set for people whose device is in dark mode:

```css
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #0a0a0a;
    --text: #f0f0f0;
    --accent: #ff7a7a;
  }
}
```

Nothing else changes. Every rule already says `var(--bg)`, so the whole page flips.

**Things to watch out for**

- **Don't just invert.** Pure white text on pure black is harsh. Use a near-black and a near-white — like `#0a0a0a` and `#f0f0f0`.
- **Your accent probably needs adjusting.** A colour with enough contrast on white is often too dark on black. That's why `--accent` is lighter in the dark set above.
- **Test both.** Your OS has a toggle - for now just use that. It's also possible to have a manual toggle but we'll cover that later.
- **Images and screenshots** with white backgrounds will look very bright in dark mode. Consider a png/webp with a transparent background.

This site does exactly this — try the ☀ toggle at the top and then look at `style.css`.

## CSS Properties

### Font name

The font-family property specifies the font you want to use.

```
p {
  font-family: "Roboto Condensed";
}
```

### Font Stack

If the first font in the stack is not available, the second one is used and so on. It is good practice to specify ‘serif’ or ‘sans-serif’ as a fallback in case your custom font doesn’t load.

```
body {
  font-family: Georgia, Times, "Times New Roman", serif;
}
```

### Loading fonts from Google Fonts

Your computer has fonts installed. Your visitor's computer probably doesn't have the same ones. So if you write `font-family: "Roboto Condensed"` and they don't have it, they get a fallback — your design breaks on someone else's machine.

The fix: tell the browser where to *download* the font from. [Google Fonts](https://fonts.google.com) hosts hundreds for free.

1. Go to [fonts.google.com](https://fonts.google.com) and pick a font.
2. Choose the weights you actually need (each one is another download — don't tick all nine).
3. Copy the `<link>` it gives you into the `<head>` of your HTML, above your stylesheet:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Roboto+Condensed:wght@400;700&display=swap" rel="stylesheet">
```

4. Now use it in your CSS, with a fallback in case it fails to load:

```css
body {
  font-family: "Roboto Condensed", sans-serif;
}
```

**Things worth knowing**

- The font is downloaded on every visit, so more weights means a slower page. Two or three is plenty.
- `display=swap` in that URL means text shows in a fallback font immediately, then swaps when the real one arrives — better than staring at invisible text.
- The font name in your CSS must match the name in the link exactly, spelling and capitalisation.
- Fonts you buy or download elsewhere can be self-hosted with `@font-face` — same idea, but the file lives in your repo. Ask AI to set it up when you need it.

### Font weight

The weight of the font you want to use. Typical nomenclature is:

- 100 Thin
- 200 Extra Light
- 300 Light
- 400 Normal
- 500 Medium
- 600 Semi Bold
- 700 Bold
- 800 Extra Bold
- 900 Ultra Bold

If the font family doesn’t provide the requested weight, it will use the closest available one.

```
p {
  font-family: "Roboto Condensed";
  font-weight: 800;
}
```

### Font size

The size of the font you want to use.

```
p {
  font-family: "Roboto Condensed";
  font-size: 12px;
}
```

### Text alignment

Left, center, right or justify alignment.

```
.center{
  text-align: center;
}

.left{
  text-align: left;
}

.right{
  text-align: right;
}

.justify{
  text-align: justify;
}
```

### Text indentation

The text-indent property indents the first line of a text block.

```
p {
  text-indent: 50px;
}
```

### Tracking

The letter-spacing property controls the tracking between characters. It is convenient to use em as em is dependent on the current text size.

```
p {
  letter-spacing: 0.1em;
}
```

### Leading

The line-height property can be used to control the leading of the text. It is convenient to use em as em is dependent on the current text size.

```
p {
  line-height: 1.5em; //1.5 em is 150% of text size.
}
```

### Text Decoration

Add an underline, overline or strikethrough to text. You can specify the type and color of the line.

```
p {
  text-decoration: underline;
  text-decoration: underline overline wavy red;
}
```

### Text Transform

Capitalise first word, convert to upper or lowecase.

```
p {
  text-transform: capitalise;
  text-transform: uppercase;
  text-transform: lowercase;  
}
```

### Color

The color of the text in the block.

```
p {
  color: #ff4343;
}
```

### Background color

The background color of the block.

```
p {
  background-color: #ff4343;
}
```

## Pseudo classes

### :hover

Add this to a class and these rules will be activated only when the mouse pointer is hovering over the class.

```
p:hover {
  background-color: #ff4343;
}
```

### :first-letter

Affects only the first letter of the div.

```
p::first-letter {
  font-weight: bold;
  text-transform: uppercase;
}
```

### :first-line

Affects only the first line of the div.

```
p::first-line {
  font-weight: bold;
  text-transform: uppercase;
}
```

## Links

Links can be styled using the following properties

```
a:link { color: #666666; text-decoration: none; }
a:visited { color: #333333; }
a:hover { text-decoration: underline; }
a:active { color: #000000; }
```

### Responsive Design

### Breakpoints

