---
date: 22-09-2026
date modified: 22-09-2026
feed: show
tag: exercise
title: "Exercise - A Theme That Remembers"
---

### Save a colour theme in localStorage

In [[Lecture 3 - Divs, Dark Mode, Flexbox]] you defined your colours once in `:root`. Now you'll add a few themes to your site, let visitors switch between them, and save their choice in localStorage so it's still there after a refresh.

### The CSS

Keep your `:root` colours as the default, and add a block for each extra theme. Each one only changes the variables:

```css
:root {
  --bg: #ffffff;
  --text: #1a1a1a;
  --accent: #ff4343;
}

[data-theme="dark"] {
  --bg: #111111;
  --text: #f2f2f2;
  --accent: #ff7a7a;
}

[data-theme="sand"] {
  --bg: #f4ecdf;
  --text: #3a2e22;
  --accent: #b5542d;
}
```

`[data-theme="dark"]` is a selector for any element with the attribute `data-theme="dark"`. We'll put that attribute on the `<html>` tag, so every variable on the page changes with it.

### The HTML

```html
<div class="theme-picker">
  <button data-theme-choice="light">Light</button>
  <button data-theme-choice="dark">Dark</button>
  <button data-theme-choice="sand">Sand</button>
</div>
```

### The JavaScript

```js
function applyTheme(name) {
  document.documentElement.dataset.theme = name;
  localStorage.setItem("theme", name);
}

const saved = localStorage.getItem("theme");
if (saved) {
  applyTheme(saved);
}

document.querySelectorAll("[data-theme-choice]").forEach((button) => {
  button.addEventListener("click", () => {
    applyTheme(button.dataset.themeChoice);
  });
});
```

Read it out loud:

1. **`applyTheme`** — put the theme name on the `<html>` tag, and save it in localStorage.
2. **When the page loads** — if a theme was saved last time, apply it.
3. **When a button is clicked** — apply the theme that button is for.

To check it works: pick a theme, then refresh. It should stay. Then open your site on your phone — it'll be on the default theme, because your phone has its own localStorage.

### Things to try

- Design your own theme for your site, and add a button for it.
- Look at the saved value in DevTools: under **Application**, expand **Local storage** and click your site's address. Delete it and refresh.
- You might see the default colours flash for a moment before your theme appears. That's because your script runs after the page has started drawing. Ask AI how to fix it.

Back to [[Lecture 6 - localStorage and Databases]].
