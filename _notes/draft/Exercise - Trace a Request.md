---
date: 18-08-2026
date modified: 24-07-2026
feed: show
tag: exercise
title: "Exercise - Trace a Request"
---
### Watch your website load, piece by piece

Use the browser's Network tab to observe everything that happens between typing your URL and seeing your page.

### Steps

1. **Open your own site** (from [[Exercise - Ship a Page]]) with DevTools → Network tab open. Hard refresh.
2. **Count the requests.** Your "one page" is probably 10–50 separate requests. Identify: the HTML document, CSS files, JavaScript files, images, fonts.
3. **Read one request fully.** Click the first one: find the request URL, the method (GET), the status code (200), and the response body (your HTML!).
4. **Break something.** Edit the URL to a page that doesn't exist. Find the 404. Now you know what a status code is.
5. **Look up your DNS.** Use an online DNS lookup tool on your domain — find the IP address your name resolves to.
6. **Time it.** Note the total load time. Then throttle to "Slow 3G" in DevTools and reload. This is your site on bad hotel wifi.

### Things to keep in mind

- The waterfall chart *is* client-server architecture, drawn live.
- HTTPS padlock ≠ trustworthy site. It only means the conversation is encrypted.

### Submission

- A screenshot of your site's network waterfall with 5 annotations: document, a stylesheet, a script, an image, and the slowest request.
