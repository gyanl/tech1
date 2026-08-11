---
date: 18-08-2026
date modified: 11-08-2026
feed: show
key_areas:
  - "Responsive web design"
  - "CSS — styling"
tag: lecture
title: "Lecture 3 - Responsive Web Design"
---

## Responsive Web Design

Last week you styled *text*. This week you arrange things on a page — and make that arrangement survive every screen size it lands on.

To do that you need three things: a way to group elements (**divs**), a way to name them (**classes**), and a way to lay them out (**flexbox**).

## Divs: boxes to group things

So far your CSS has targeted tags — every `p`, every `h1`. That falls apart the moment you want *these three* things treated as a unit.

A `<div>` is a plain box with no meaning and no styling of its own. It exists to group things so you can move, space and arrange them together.

```html
<div>
  <h2>Bengaluru</h2>
  <p>A project about the city.</p>
</div>
```

Nothing looks different yet. But that heading and paragraph are now one object — which is exactly what you need before you can lay anything out.

> **Sidenote:** Divs are the Frames of the web. You already do this in Figma without thinking about it — you group a title and a caption so you can move them together. Same instinct.

### Semantic tags: divs with a name

`<div>` says nothing about what's inside it. HTML also gives you boxes that *mean* something:

```html
<header>  the top of the page   </header>
<nav>     your links            </nav>
<main>    the actual content    </main>
<footer>  the bottom            </footer>
```

They behave identically to a div. The difference is that screen readers, search engines and the next person to read your code all understand them. Use them where they fit, use `<div>` for everything else.

## Classes: naming your boxes

A class is a label you put on an element so you can style it:

```html
<div class="card">
  <h2>Bengaluru</h2>
  <p>A project about the city.</p>
</div>
```

```css
.card {
  padding: 1.5rem;
  background: var(--bg-sub);
  border-radius: 8px;
}
```

The `.` in CSS means "class". So `.card` targets every element with `class="card"`.

**This is the moment CSS becomes useful.** Write the rule once, use it on twenty cards.

### Classes vs tags vs ids

| Selector | Written as | Use it when |
| --- | --- | --- |
| Tag | `p { }` | You mean *every* paragraph on the site |
| Class | `.card { }` | You mean *these particular* elements — the normal case |
| Id | `#header { }` | Exactly one element on the page. Rare. |

An element can carry several classes, which is how you compose styles:

```html
<div class="card featured">
```

That div gets `.card` **and** `.featured`. Very close to how you'd combine a base component with a variant in Figma.

> **Naming:** call it what it *is*, not what it looks like. `.card` and `.intro` age well. `.big-red-box` becomes a lie the first time you change the colour.

## Flexbox: putting things in a row

By default HTML stacks everything vertically — one block under another. **Flexbox** is how you say "put these side by side" and control the spacing.

Add `display: flex` to the *container*, and its children line up:

```css
.cards {
  display: flex;
  gap: 1rem;
}
```

```html
<div class="cards">
  <div class="card">...</div>
  <div class="card">...</div>
  <div class="card">...</div>
</div>
```

Three properties do most of the work:

```css
.row {
  display: flex;
  justify-content: space-between;  /* spacing along the row */
  align-items: center;             /* alignment across the row */
  gap: 1rem;                       /* space between items */
}
```

- `justify-content` — `flex-start`, `center`, `space-between`, `space-around`
- `align-items` — `flex-start`, `center`, `flex-end`, `stretch`
- `gap` — just space between children. Use this instead of margins.

If you have used auto-layout in Figma, you already know flexbox. Auto-layout **is** flexbox, with a different interface:

| Figma auto-layout | CSS flexbox |
| --- | --- |
| Horizontal / vertical | `flex-direction: row` / `column` |
| Space between items | `gap` |
| Packed / space between | `justify-content` |
| Alignment | `align-items` |
| Padding | `padding` |

### Making a nav bar

The classic use, and one you need for your own site:

```css
nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 0;
}
```

Logo left, links right, vertically centred. Four lines.

### Wrapping is free responsiveness

Add one property and your row becomes several rows when there isn't space:

```css
.cards {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}

.card {
  flex: 1 1 16rem;   /* grow, shrink, but never narrower than 16rem */
}
```

That `flex: 1 1 16rem` reads as: *take a fair share of the space, shrink if you must, but at 16rem wide, wrap to the next line instead.*

Three cards on a laptop, two on a tablet, one on a phone — **with no media query at all**. Try to get this far before reaching for breakpoints.

## More CSS Properties

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

## Homework

- Rebuild your home page layout using divs, classes and flexbox. Get as far as you can with `flex-wrap` before adding a breakpoint.
