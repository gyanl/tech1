---
date: 10-08-2026
date modified: 24-07-2026
feed: show
tag: lecture
title: "Lecture 2"
---

## Anatomy of a Web Page

Last week you shipped a page. This week we open the hood.

#### Hour 1 — The three languages
- View Source: what the AI actually wrote for you
- **HTML** — structure and meaning (headings, lists, links, semantics)
- **CSS** — styling (selectors, the box model as a layout designer's mental model, typography on the web)
- **JavaScript** — interactivity (events, changing the page after it loads)
- Why this separation exists — content vs presentation vs behaviour
- Browser DevTools as a designer's x-ray machine

The same button, in all three languages:

```html
<!-- HTML: what it IS -->
<button id="say-hi" class="primary">Say hi</button>
```

```css
/* CSS: what it LOOKS like */
.primary {
  background: #16181d;
  color: white;
  padding: 12px 24px;
  border-radius: 6px;
}
```

```js
// JavaScript: what it DOES
const button = document.getElementById("say-hi");
button.addEventListener("click", () => {
  alert("Hello from Lecture 2!");
});
```

#### Hour 2 — Dissection lab
- **Exercise:** [[Exercise - Web Page Anatomy]] — pick a complex real-world page, identify its structure, styling, and interactions using DevTools
- Editing your own page's generated code by hand: change a colour, a font, a word — prove to yourself it's not magic

#### Homework
- Ask an AI to explain three things you found in DevTools that you didn't understand. Bring the best explanation to class.
