---
date: 18-08-2026
date modified: 25-08-2026
feed: show
key_areas:
  - "Responsive web design"
  - "CSS — styling"
tag: lecture
title: "Lecture 3 - Divs, Dark Mode, Flexbox"
---

## Responsive Web Design

Last week you used CSS to style your *text*. This week we will look into layouts - how you arrange things on a page. Then we will make that arrangement work for every screen size it lands on (desktop, tablet, mobile).

To do that you need three things: a way to group elements (**divs**), a way to name them (**classes**), and a way to lay them out (**flexbox**).

## Divs: Frames to group things

So far your CSS has targeted tags — like `body` or `h1/2/3`. That doesn't work anymore if you want *these three* things treated as a unit - like if I wanted to make a card with a heading, body text and an image.

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

`<div>` says nothing about what's inside it. HTML also gives you a few boxes that *mean* something:

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

The `.` in CSS means "class". So `.card` targets every element with `class="card"`. You write the rule once, then use it on twenty cards.

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

### Test it properly

- **Drag your window.** Fastest possible feedback loop.
- **DevTools device toolbar** — the phone/tablet icon in Inspect, or ⌘⇧M / Ctrl+Shift+M.
- **Your actual phone.** Use Simple Web Server from earlier, or your live github.io URL. Nothing else tells you how it really feels in the hand.

## Homework

- Rebuild your home page layout using divs, classes and flexbox. You are free to use AI coding agents for this exercise. See [[Exercise - Build the Page You Designed]] for more details.
