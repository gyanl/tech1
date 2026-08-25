---
date: 25-08-2026
date modified: 25-08-2026
feed: show
key_areas:
  - "DNS"
  - "Server-side languages"
  - "Software development lifecycle"
tag: lecture
title: "Lecture 4 - Units and Responsiveness"
---

## Units: px, em, rem, %, vw, vh

In Figma everything is in pixels. A web page has to work on a 6-inch phone and a 27-inch monitor. So CSS gives you more options for units that *respond* to something.

| Unit        | Relative to                                 | Use it for                                    |
| ----------- | ------------------------------------------- | --------------------------------------------- |
| `px`        | Nothing — fixed                             | Borders, small fixed details                  |
| `rem`       | The page's base font size (16px by default) | **Font sizes, spacing — your default choice** |
| `em`        | The font size of *this* element             | Spacing that should scale with its own text   |
| `%`         | The parent element's size                   | Widths inside a layout                        |
| `vw` / `vh` | 1% of the window's width / height           | Full-screen sections, huge display type       |

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

The good news: HTML is (kind of) responsive by default. A paragraph already fills whatever width it's given and rewraps. You mostly break responsiveness by fixing widths in `px` — then fix it back with a couple of rules.

### First, one line you can't skip

Put this in the `<head>` of your HTML. This is necessary because without this line phones pretend to be a desktop sized device and shrink your whole page down to fit at an unreadable size.

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

### Mobile first or desktop?

Notice the base styles are the *phone* layout, and each media query adds complexity as the screen grows. This is called **mobile first**, and it's the convention because:

- The simplest layout is the one that works everywhere, so it's a safe default.
- Phones do the least work — they never even read the desktop rules.
- It's easier to add columns as you gain space than to unpick them as you lose it.

### Choosing breakpoints

Don't copy a list of device sizes. iPhone 15, iPad Pro, MacBook Air — that list changes every year and you'll never catch them all.

> **Add a breakpoint where *your design* stops looking right.** Drag your browser window slowly narrower and watch. The width where your line lengths go silly or your grid gets cramped — that's your breakpoint.

Most sites need two or three. Common starting points are `40rem` (640px), `48rem` (768px) and `64rem` (1024px).

## Class Activity

Finish building your home page designs. Instructor will help with any issues you are running into.

## Homework

[[Exercise - Build the Page You Designed]]