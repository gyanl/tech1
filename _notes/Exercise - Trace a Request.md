---
date: 22-09-2026
date modified: 25-08-2026
feed: show
tag: exercise
title: "Exercise - Trace a Request"
---
### Watch your website load, piece by piece

Use the browser's Network tab to observe everything that happens between typing your URL and seeing your page.

### Steps

1. **Open your own site** (from [[Exercise - Ship a Page with GitHub Pages]]) with DevTools → Network tab open. Hard refresh — **⌘⇧R** / **Ctrl+Shift+R** — so nothing comes from cache.
2. **Count the requests.** Your "one page" is probably 10–50 separate requests. Identify: the HTML document, CSS files, JavaScript files, images, fonts.
3. **Read one request fully.** Click the first one: find the request URL, the method (GET), the status code (200), and the response body (your HTML!).
4. **Break something.** Edit the URL to a page that doesn't exist. Find the 404, and note which *family* it's in — is this your fault or the server's?
5. **Reload without the hard refresh.** Watch how many requests come from cache instead of the network, and compare the total time. That's the answer to "why didn't my CSS change show up?" 
6. **Look up your DNS.** Use an online DNS lookup tool on `yourusername.github.io` — find the IP address the name resolves to. You are looking at GitHub's servers.
7. **Time it.** Note the total load time. Then throttle to "Slow 3G" in DevTools and reload. This is your site on bad hotel wifi, and it is the experience a lot of your users actually have.

### Things to keep in mind

- The waterfall chart *is* the round trip from [[Lecture 5 - APIs]], drawn live on your own work.
- Count your requests before you start optimising. Most "slow" pages are slow because there are too many things to fetch, not because any one of them is big.
- HTTPS padlock ≠ trustworthy site. It only means the conversation is encrypted.

### Submission

- A screenshot of your site's network waterfall with 5 annotations: the document, a stylesheet, a script, an image, and the slowest request.
- Your total request count and load time, normal vs Slow 3G.
- One sentence: if you had to make this page twice as fast, what would you do first, and why that?
