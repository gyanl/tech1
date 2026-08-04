---
date: 03-08-2026
date modified: 04-08-2026
feed: show
tag: exercise
title: "Exercise - Ship a Page with GitHub Pages"
---
### Put your website on the real internet — free, today

You already have a repo made from [web-starter](https://github.com/gyanl/web-starter). Now we tell GitHub to serve it as a live website. This is called **GitHub Pages** — free hosting for static sites.

### Steps

1. **Make the page yours first.** In VS Code, put your actual name in `index.html`, change a colour in `style.css`. Save.
2. **Commit and push.** In GitHub Desktop: write a short summary of what you changed → **Commit to main** → **Push origin**. (Commit = save a snapshot. Push = send it to GitHub.)
3. **Turn on GitHub Pages.** On your repo's page on github.com:
	- **Settings → Pages**
	- Under *Build and deployment*, set Source to **Deploy from a branch**
	- Choose branch **main**, folder **/ (root)** → **Save**
4. **Wait a minute, then find your URL.** Refresh the Pages settings page — it will show:
	`https://YOUR-USERNAME.github.io/YOUR-REPO-NAME/`
5. **Open it on your phone.** Not on the college wifi — use mobile data. It's really on the internet.
6. **Make one more change and push again.** Watch the live site update a minute later. This is your publish loop now:
	**edit → save → commit → push → live**

### Things to keep in mind

- This page is public and Google can find it. No phone numbers, no addresses, nothing you wouldn't put on a poster.
- If the URL shows a 404, wait a minute and refresh — the first deploy is slow. Still broken? Check that your homepage file is called exactly `index.html`.
- Your username and repo name are part of the URL. This is why we chose sensible ones.

### Submission

- Your live `github.io` URL, posted to the class group before you leave.
