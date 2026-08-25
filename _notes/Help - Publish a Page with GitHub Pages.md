---
date: 25-08-2026
date modified: 25-08-2026
feed: show
tag: help
title: "Help - Publish a Page with GitHub Pages"
---
### What you'll end up with

A live website at `https://YOUR-USERNAME.github.io/YOUR-REPO-NAME/` that anyone can open, made from a single `index.html` file.

You need: a GitHub account, and [GitHub Desktop](https://desktop.github.com/) installed and signed in.

---

## Part 1 — Make the repo (github.com)

1. Go to [github.com](https://github.com) and sign in.
2. Click the **+** in the top right → **New repository**.
3. Fill in:
	- **Repository name:** lowercase, no spaces — e.g. `my-first-site`. This becomes part of your URL, so pick something short and sensible
	- **Description:** optional.
	- **Public.** Github Pages only works with public repos on a free account, and you want people to see it anyway.
	- Tick **Add a README file.** (This gives the repo one file to start with, which makes the next step easier.)
4. Click **Create repository**.

You now have an empty-ish project living on GitHub. It's not on your computer yet.

---

## Part 2 — Get it onto your computer (GitHub Desktop)

1. On your new repo's page, click the green **Code** button → **Open with GitHub Desktop**. Your browser will ask permission to open the app — allow it.
	*(If that doesn't work: in GitHub Desktop, **File → Clone repository → GitHub.com**, pick your repo from the list.)*
2. GitHub Desktop shows a **Clone** dialog with a **Local path** — this is where the folder will live on your computer. Note it, or change it to somewhere you'll find again. Click **Clone**.
3. You now have a real folder on your computer that is connected to GitHub. **Clone** = make a local copy that stays linked.

### Add your index.html

4. In GitHub Desktop, click **Repository → Show in Finder** (Mac) or **Show in Explorer** (Windows) to open the folder.
5. Create a new file in that folder called exactly `index.html` — all lowercase, no `.txt` on the end. Open it in VS Code (or any text editor) and paste:

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Your Name</title>
</head>
<body>
	<h1>Hello, I'm Your Name</h1>
	<p>This page is on the actual internet.</p>
</body>
</html>
```

6. Put your real name in it. Save.

`index.html` is the magic filename — it's the page a web server shows when someone visits the address with nothing after it.

### Commit and push

7. Switch back to GitHub Desktop. Your new file appears in the left column under **Changes**.
8. Bottom left, in the **Summary** box, type what you did: `Add index.html`.
9. Click **Commit to main.** (Commit = save a labelled snapshot. It's still only on your computer.)
10. Click **Push origin** at the top. (Push = send those commits up to GitHub.)
11. Refresh your repo page on github.com — `index.html` is there.

---

## Part 3 — Turn on GitHub Pages (github.com)

1. On your repo page, click **Settings** (top row, far right).
2. In the left sidebar, click **Pages**.
3. Under **Build and deployment → Source**, choose **Deploy from a branch**.
4. Under **Branch**, choose **main** and folder **/ (root)**. Click **Save**.
5. Wait around 2-3 minutes, then refresh that page. A banner appears with your URL:
	`https://YOUR-USERNAME.github.io/YOUR-REPO-NAME/`
6. Open it on your phone and laptop to test.

---

## Your loop from now on

**edit → save → commit → push → live in a minute**

Make one small change to `index.html`, save, commit and push in GitHub Desktop, then refresh your site. Watching that change appear is the whole point — you now have a way to put anything you make in front of anyone.

---

## When it doesn't work

- **404 on the URL.** Usually just slowness — wait a minute or two and refresh. If it persists, check the file is called exactly `index.html` (not `Index.html`, not `index.html.txt`) and that it's in the top level of the repo, not inside another folder.
- **Nothing under Changes in GitHub Desktop.** You saved the file somewhere other than the cloned folder. Use **Repository → Show in Finder/Explorer** to confirm where that folder actually is.
- **Push origin is greyed out.** You haven't committed yet — do step 9 first.
- **Site shows the README instead of your page.** No `index.html` at the root; GitHub falls back to the README.
- **Your changes aren't showing up live.** Committed but not pushed, or the deploy is still running. Check the **Actions** tab on github.com for an orange dot (running) or a green tick (done). A hard refresh (Cmd/Ctrl + Shift + R) clears a cached old version.

## Keep in mind

This page is public and searchable. No phone numbers, no addresses, nothing you wouldn't put on a poster.
