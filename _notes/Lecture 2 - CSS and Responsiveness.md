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

## Steps for using Github Pages

1. Make changes.
2. Use Github to commit changes. This creates a checkpoint "locally".
3. Push to Github to push your changes online to Github.
4. Your updated website is now live at yourgithubusername.github.io

**Download Simple Web Server app**
[Download Simple Web Server](https://simplewebserver.org/)
This app is a quick and easy way to start a server on your computer, and allows you to test your website on your computer or any other device on the same wifi network - like your phone!

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
- **Test both.** Your OS has a toggle, or use DevTools → the three dots → More tools → Rendering → *Emulate prefers-color-scheme*.
- **Images and screenshots** with white backgrounds will glow in dark mode. Consider a PNG with a transparent background.

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

