---
date: 11-08-2026
date modified: 11-08-2026
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

## Git terms

**Git:** The tool that tracks changes to your files and lets you go back to any earlier version. It runs **on your computer**, works with no internet, and needs no account. Made in 2005 to manage the code of Linux.

**Github:** A **website** that stores Git projects online — so you have a backup, other people can see your work, and a team can work on the same project. Owned by Microsoft. It's not the only one: GitLab and Bitbucket do the same job.

**Github Desktop:** The **app** we're using. Git itself has no buttons — it was built to be typed at in a terminal. GitHub Desktop is a friendly face on top of it, so you can click Commit and Push instead of memorising commands. It's optional; the Git underneath is the real thing.

> Git is the tool. GitHub is a place that keeps what the tool makes. GitHub Desktop is just a nicer way to use the tool.

**Repo:** A folder (usually code files) synced to Github

**Clone:** Download a repo from Github onto your computer for the first time, set up so the two stay connected.

**Commit:** Make a checkpoint (locally)

**Fetch:** Check if any changes have been made on Github online, download them locally. This matters more when you are working collaboratively with other people on a repo. So far it's just you.

**Pull:** Bring those changes down and merge them into your copy.

**Push:** Upload your changes to Github online

## Steps for using Github Pages

1. Make changes.
2. Use Github to commit changes. This creates a checkpoint "locally".
3. Push to Github to push your changes online to Github.
4. Your updated website is now live at yourgithubusername.github.io

## Your computer and GitHub are two different places

In Figma, there is **one cloud file** and everyone is inside it at once. You see other people's cursors. You never "send" your work anywhere.

Git is the opposite. There are **two separate copies** of your project — the one on your laptop, and the one on GitHub — and they only talk to each other when you tell them to. Nothing is automatic.

> **Sidenote:** Why would anyone want this? Because you can work offline, try something terrible, and throw it away without anyone seeing. The copies are a feature.

### What "origin" means

You'll notice every button says *origin*: **Fetch origin**, **Pull origin**, **Push origin**.

`origin` is just a **nickname for the GitHub copy** of your project.

When you cloned the repo, Git saved its web address and needed something to call it. The default nickname is `origin` — as in *the place this originally came from*.

So read the buttons like this:

- **Push origin** → send my commits to GitHub
- **Pull origin** → bring GitHub's commits down to me

### Isn't this just cloud storage then?

Cloud storage options like Google Drive, Dropbox, iCloud Drive and OneDrive also keep one copy on your machine and one in the cloud.

The differences are the whole point:

| | Dropbox / iCloud / OneDrive | Git + GitHub |
| --- | --- | --- |
| When it syncs | Constantly, by itself | Only when you say so |
| What it keeps | The current version of the file | Every checkpoint you made, with a message and your name on it |
| Going back | One file, recent versions | The **whole project**, at any point in its history |
| Two people edit one file | `index (conflicted copy 2).html` — good luck | Merges line by line; only asks you if the *same lines* changed |
| Trying something risky | Everyone sees it immediately | Stays on your machine until you push |

You have all seen `Document (conflicted copy 2).docx`. That file is Dropbox admitting defeat: it can't work out how to combine two versions, so it keeps both and makes it your problem. Git actually reads what changed on each side and puts them together.

## So why not just use Dropbox for a website?

Honestly, for one person, you nearly could. What you'd be giving up:

- GitHub **serves** your site to the internet. Dropbox only stores it.
- Checkpoints *you* chose, labelled with why you made them — not just "3:47pm".
- Three people working on one project without overwriting each other. That's your final project.
- The thing every design studio and engineering team already uses.

### Commits are a chain, not a pile

Each commit records what came before it. Your project's history is a chain of checkpoints in a specific order. This matters because it's why Git can't just mash two versions together — it needs to know what order things happened in, which option you want to keep.

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

Right now you're one person on one laptop, so this may never happen. It will start to happen the moment any of these is true:

1. **You edit a file on github.com** — this change doesn't automatically get synced to your laptop
2. **You use two computers** — a college machine and your own.
3. **You are working with other people in a repo.** — group projects

# CSS, Responsiveness, Color Theming

Pushing to Github Pages means you can now start seeing your work on your phone over the internet at username.github.io. But it takes a while to push to Github and then for Github to update the live version of your site. There is a faster way to do this - you can just run a server on your laptop!

**Download Simple Web Server app**
[Download Simple Web Server](https://simplewebserver.org/)
This app is a quick and easy way to start a server on your computer, and allows you to test your website on your computer or any other device on the same wifi network - like your phone.

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

## Units: px, em, rem, %, vw, vh

In Figma everything is in pixels, because a Figma frame is one fixed size. A web page isn't — it has to work on a 6-inch phone and a 27-inch monitor. So CSS gives you units that *respond* to something.

| Unit | Relative to | Use it for |
| --- | --- | --- |
| `px` | Nothing — fixed | Borders, small fixed details |
| `rem` | The page's base font size (16px by default) | **Font sizes, spacing — your default choice** |
| `em` | The font size of *this* element | Spacing that should scale with its own text |
| `%` | The parent element's size | Widths inside a layout |
| `vw` / `vh` | 1% of the window's width / height | Full-screen sections, huge display type |

### The short version

Use **`rem`** for type and spacing. Use **`px`** for hairlines and borders. Use **`%`** for widths. Reach for `vw`/`vh` only when you mean "a portion of the screen".

```css
h1 {
  font-size: 2rem;      /* 32px, but scales if the user changes their font size */
  margin-bottom: 1rem;  /* 16px */
  border-bottom: 1px solid black;   /* hairline — px is right here */
}
```

### Why rem instead of px?

`1rem` = the base font size of the page, normally **16px**. So `2rem` is 32px — until someone who can't read small text turns their browser font up to 20px, at which point your whole layout grows with them.

Sizes in `px` ignore that setting completely. Using `rem` is an accessibility decision, not a style preference.

> **Sidenote:** `rem` stands for *root em* — an em measured against the root of the document instead of the current element.

### em is relative to itself

`em` is measured against the element's *own* font size, which is why it's handy inside a component:

```css
.button {
  font-size: 1.2rem;
  padding: 0.5em 1em;   /* padding grows automatically with the text */
}
```

Make that button bigger and the padding scales too — nothing else to change. The catch is that `em` compounds when elements nest, which is why it's a bad default for font sizes and a good one for local spacing.

### vw and vh

`100vh` is exactly the height of the window, `100vw` its width. Great for a full-screen hero section:

```css
.hero {
  height: 100vh;
}
```

Careful on phones: `100vh` used to be taller than the visible area because of the address bar. If you hit that, `100dvh` (*dynamic* viewport height) is the modern fix.

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

- The font is downloaded on every visit, so more weights means a slower page. Two or three is usually enough.
- `display=swap` in that URL means text shows in a fallback font immediately, then swaps when the real one arrives — better than staring at invisible text.
- The font name in your CSS must match the name in the link exactly, spelling and capitalisation.w
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

## Responsive Design

You designed one artboard. Your visitor could be on a phone held in one hand, a laptop, or a TV. **Responsive design** means one page that reshapes itself to fit, instead of you making three separate sites.

The good news: HTML is responsive by default. A paragraph already fills whatever width it's given and rewraps. You mostly break responsiveness by fixing widths in `px` — then fix it back with a couple of rules.

### First, one line you can't skip

Put this in the `<head>` of your HTML. Without it phones pretend to be a 980px-wide desktop and shrink your whole page down to unreadable:

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

It's already in your `index.html` from web-starter. Don't delete it.

### Two habits that do most of the work

```css
/* let things shrink, but not stretch too wide to read */
.container {
  width: 100%;
  max-width: 40rem;
  margin: 0 auto;
}

/* images never overflow their container */
img {
  max-width: 100%;
  height: auto;
}
```

`max-width` instead of `width` is the whole idea: *"be as wide as you can, up to this limit."*

### Breakpoints

A **breakpoint** is a screen width at which your layout needs to change — a point where the design breaks if you don't do something.

You write them with a **media query**: a block of CSS the browser only applies when a condition is true.

```css
/* base styles — written for narrow screens first */
.cards {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
}

/* from 40rem (640px) and up, go to two columns */
@media (min-width: 40rem) {
  .cards {
    grid-template-columns: 1fr 1fr;
  }
}

/* from 64rem (1024px) and up, three */
@media (min-width: 64rem) {
  .cards {
    grid-template-columns: 1fr 1fr 1fr;
  }
}
```

Read `@media (min-width: 40rem)` as: **"from 640px wide and upwards, also apply these rules."**

### Mobile first

Notice the base styles are the *phone* layout, and each media query adds complexity as the screen grows. This is called **mobile first**, and it's the convention because:

- The simplest layout is the one that works everywhere, so it's a safe default.
- Phones do the least work — they never even read the desktop rules.
- It's easier to add columns as you gain space than to unpick them as you lose it.

### Choosing breakpoints

Don't copy a list of device sizes. iPhone 15, iPad Pro, MacBook Air — that list changes every year and you'll never catch them all.

> **Add a breakpoint where *your design* stops looking right.** Drag your browser window slowly narrower and watch. The width where your line lengths go silly or your grid gets cramped — that's your breakpoint.

Most sites need two or three. Common starting points are `40rem` (640px), `48rem` (768px) and `64rem` (1024px).

### Test it properly

- **Drag your window.** Fastest possible feedback loop.
- **DevTools device toolbar** — the phone/tablet icon in Inspect, or ⌘⇧M / Ctrl+Shift+M.
- **Your actual phone.** Use Simple Web Server from earlier, or your live github.io URL. Nothing else tells you how it really feels in the hand.

