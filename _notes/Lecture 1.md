---
date: 03-08-2026
date modified: 04-08-2026
feed: show
tag: lecture
title: "Lecture 1"
---

# Welcome to Tech 1!

- Some of you might remember me from your Ergonomics course last year
- This time the course site is even better! Check [gyanl.com/tech1](https://gyanl.com/tech1)
- Our weekly slot is 2:15-4:15pm on Tuesdays.
- I will be travelling so some classes may get rescheduled. Not as much as last year though, and I will give as much advance notice as possible.

---
## In this Course

The title for this course is:

**Web & Mobile Ecosystem Fundamentals**

**Course Objective:**
Gain a foundational understanding of the core technologies, platforms, and concepts that underpin the modern web and mobile ecosystems, essential for product and design professionals.

I will not follow the syllabus too strictly - this will be a hands on course where you will build working apps and websites. I don't expect you to become engineers in one course over a semester, but we'll use AI to generate code and build high-fidelity, working prototypes.

- [[Syllabus]]
- [[AI Policy]]

---
## How this course works

- **You will build from week one.** Using AI tools, you will generate, modify, and deploy real web applications — starting with a personal webpage in the very first session.
- **Fundamentals follow experience.** Each week we dissect something you have already built: "you made this — now let's understand what HTML, hosting, and DNS actually did for you."
- **AI is the medium, not a module.** You are expected to generate most of your code with AI tools (Claude, Cursor, v0, Lovable, etc.). The skill we are building is *directing* these tools well — which requires understanding the stack conceptually.
- **The course converges into a final project.** The final project of the course is a build sprint where you take a product idea to a working, deployed application, presented at a Demo Day.

---
## Admin

- Who is the Class Rep?
- Create a WhatsApp group for the class

---
## Setup (30 min)

Get your toolkit working — we use all of this every week:

1. **Create a GitHub account** — [github.com](https://github.com) (use an email you'll keep; your username will be public and part of your project URLs)
2. **Apply for the GitHub Student Developer Pack** — [GitHub Education · GitHub](https://github.com/education) (free credits and tools; needs your university email/ID)
3. **Download GitHub Desktop** — [desktop.github.com](https://desktop.github.com) (Mac/Windows)
4. **Download a code editor** — [VS Code](https://code.visualstudio.com) (or Cursor if you want AI built in)

---
## Create a repo from this template

# [gyanl/web-starter](https://github.com/gyanl/web-starter)

![](assets/img/use-gh-template.png)

> Use this template -> Create a new repository

- **What's Github?**
  A code storing and sharing site. You can also use it to make your website live on the internet.

- **What's a repo?**
  A repository is a folder of code. You can store it on GitHub. There are some very good reasons to do this that we'll get into later.

---
## HTML, CSS and JS

- **HTML** — structure and meaning (headings, lists, links, semantics)
- **CSS** — styling (selectors, the box model as a layout designer's mental model, typography on the web)
- **JavaScript** — interactivity (events, changing the page after it loads)

---

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


--- 

#### Ship something (rest of class)

- **Exercise:** [[Exercise - Ship a Page]] — use an AI tool to build and deploy a personal webpage, live in class
- Everyone leaves with a URL that works on their phone

---
#### Homework

- Finish any setup that got stuck (Student Pack approval can take a few days — apply today)
- Polish your page and bring the URL next week — we're going to dissect it
