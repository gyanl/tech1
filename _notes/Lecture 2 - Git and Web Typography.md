---
date: 11-08-2026
date modified: 25-08-2026
feed: show
key_areas:
  - "Version control (Git)"
  - "Hosting and deployment"
  - "CSS — styling"
tag: lecture
title: "Lecture 2 - Git and Web Typography"
---

## Designing your Website

Last week we shipped a page! This week we'll figure out how to ship your page.

> **Sidenote:** Can anyone tell me why do we *ship* software?

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
4. About a minute later your updated website is live at `https://yourusername.github.io/your-repo-name/`

> Your URL only drops the repo name if you named the repo exactly `yourusername.github.io`. Most of you didn't, so expect the repo name in the address.

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

```text
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

# Web Typography

Pushing to Github Pages means you can now start seeing your work on your phone over the internet at your github.io URL. But it takes a while to push to Github and then for Github to update the live version of your site. There is a faster way to do this - you can just run a server on your laptop!

**Download Simple Web Server app**
[Download Simple Web Server](https://simplewebserver.org/)
This app is a quick and easy way to start a server on your computer, and allows you to test your website on your computer or any other device on the same wifi network - like your phone.

1. Click New Server
2. Choose folder and pick the repo folder you cloned
3. Enable "Accessible on local network"
4. Click "Create Server"
5. Pick the server from the list, make sure the toggle is turned on
6. One of the two links should work on your phone as long as you are on the same wifi

## CSS Properties

### Font name

The font-family property specifies the font you want to use.

```css
p {
  font-family: "Work Sans", Times, "Times New Roman", serif;
}
```

### Font Stack

If the first font in the stack is not available, the second one is used and so on. It is good practice to specify `serif` or `sans-serif` as a fallback in case your custom font doesn’t load.

```css
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
- The font name in your CSS must match the name in the link exactly, spelling and capitalisation.
- Fonts you buy or download elsewhere can be self-hosted with `@font-face` — same idea, but the file lives in your repo. Ask AI to set it up when you need it.

### Color

The color of the text in the block.

```css
p {
  color: #ff4343;
}
```

### Background color

The background color of the block.

```css
p {
  background-color: #ff4343;
}
```

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

```css
p {
  font-family: "Roboto Condensed";
  font-weight: 800;
}
```

### Font size

The size of the font you want to use.

```css
p {
  font-family: "Roboto Condensed";
  font-size: 12px;
}
```

### Text alignment

Left, center, right or justify alignment.

```css
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

```css
p {
  text-indent: 50px;
}
```

### Tracking

The letter-spacing property controls the tracking between characters. It is convenient to use em as em is dependent on the current text size.

```css
p {
  letter-spacing: 0.1em;
}
```

### Leading

The line-height property can be used to control the leading of the text. It is convenient to use em as em is dependent on the current text size.

```css
p {
  line-height: 1.5em; //1.5 em is 150% of text size.
}
```

### Text Decoration

Add an underline, overline or strikethrough to text. You can specify the type and color of the line.

```css
p {
  text-decoration: underline;
  text-decoration: underline overline wavy red;
}
```

### Text Transform

Capitalise the first letter of each word, or convert to upper or lower case. Note the CSS keyword is spelled `capitalize`, American-style — `capitalise` does nothing.

```css
p {
  text-transform: capitalize;
  text-transform: uppercase;
  text-transform: lowercase;  
}
```

## Homework

- **Exercise:** [[Exercise - Figma to Code]] — build your Figma design as a real page: a Google Font loaded properly, `rem` for type and spacing, and at least 5 commits with real messages. Includes making Git diverge on purpose and fixing it.
