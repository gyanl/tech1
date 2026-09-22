---
date: 22-09-2026
date modified: 22-09-2026
feed: show
tag: help
title: "Help - Host on Vercel"
---
### What you'll end up with

Your site live at `https://YOUR-PROJECT.vercel.app`, updating by itself every time you push to GitHub.

GitHub Pages is fine for static sites. Vercel does the same job, and it can also run back-end code and keep secret keys out of your page ([[Lecture 5 - APIs]]), which you'll need once your projects get bigger. It's the host most teams using React and Next.js deploy to.

You need: a GitHub account, and a repo with your site in it (an `index.html` at the top level is enough).

---

## Part 1 — Make an account

1. Go to [vercel.com/signup](https://vercel.com/signup).
2. Choose the **Hobby** plan. It's free for personal, non-commercial projects.
3. Click **Continue with GitHub** and sign in with your GitHub account. Signing up this way is what lets Vercel see your repos.
4. When GitHub asks which repositories Vercel can access, you can pick **All repositories**, or **Only select repositories** and choose the one you want to deploy. You can change this later.

---

## Part 2 — Deploy your repo

1. On your Vercel dashboard, click **Add New… → Project**.
2. Find your repo in the list and click **Import**.
3. On the configure screen:
	- **Project Name:** this becomes your URL, so keep it short and lowercase.
	- **Framework Preset:** leave it as **Other** for a plain HTML/CSS/JS site. If you built it with React or Next.js, Vercel usually detects that for you.
	- Leave everything else as it is.
4. Click **Deploy**. After a few seconds you'll get a screenshot of your site and a link to it.

Open the link on your phone to check it works.

---

## Part 3 — Updating it

You don't deploy again by hand. The loop is the same as GitHub Pages:

> **edit → save → commit → push → live**

Every push to `main` makes Vercel build and publish a new version. You can watch it happen under **Deployments** on your project page. If something breaks, click an older deployment and **Promote to Production** to go back to it.

---

## If it doesn't work

- **404 on your URL:** check your homepage is called exactly `index.html` and is at the top level of the repo, not inside a folder.
- **Your repo isn't in the import list:** Vercel doesn't have access to it. Click **Adjust GitHub App Permissions** under the list and add the repo.
- **Your change isn't showing:** check the latest deployment under **Deployments** finished without an error, then hard-refresh the page (Cmd+Shift+R on a Mac, Ctrl+Shift+R on Windows).
