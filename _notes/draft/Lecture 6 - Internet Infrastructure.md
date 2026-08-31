---
date: 22-09-2026
date modified: 01-09-2026
feed: show
key_areas:
  - "How the internet works"
  - "DNS"
  - "HTTP / HTTPS"
  - "IP addresses"
  - "Web browsers and their role"
tag: lecture
title: "Lecture 6 - Internet Infrastructure"
---

## Recap

Last time you wrote this and it worked:

```js
const response = await fetch("https://api.example.com/weather?city=Bengaluru");
```

You sent a request across the internet to a machine you've never seen, and got JSON back. You also drew the round trip — browser, server, database — and Firebase quietly held a connection open so your class wall could update without anyone refreshing.

Today we open up the arrows. Between pressing Enter and seeing a page there are about eight steps, and every single one of them is a place things go wrong. Knowing them is the difference between "the site is broken" and "the site is broken *at this specific point*."

> **Sidenote:** This is the most conceptual week of the course and the one you'll use most in meetings. Nothing new to build — but afterwards, when an engineer says "it's a DNS issue" or "that's a 500, not a 404," you'll know what's being claimed.

## Read the URL as a sentence

Start with the thing you've been typing for five weeks. Your own site:

```text
https :// gyanl.github.io / my-first-site / about.html ? theme=dark
└─┬──┘    └──────┬──────┘  └──────┬─────┘  └────┬────┘  └────┬───┘
protocol      domain            path          file        query
```

- **Protocol** — which language to speak. `https` is HTTP with encryption.
- **Domain** — *who* to talk to. A name, because humans are bad at numbers.
- **Path** — *what* to ask them for. Folders and a file, usually.
- **Query string** — extra instructions, as `key=value` pairs after a `?`. You used one last week: `?city=Bengaluru`.

Every URL you meet decomposes like this. When an API's docs give you a scary-looking address, take it apart this way and it stops being scary.

## Step 1 — DNS turns a name into a number

Computers don't route to names. They route to **IP addresses** — `140.82.121.4`, or in the newer IPv6 format, something long and hexadecimal. The number is the actual address; the name is a convenience for you.

**DNS** — the Domain Name System — is the system that translates one into the other. It's often called the internet's phonebook, which is close enough: you know the name, you need the number, and there's a distributed lookup that gets it for you in a few milliseconds.

Roughly what happens when you press Enter:

```text
1. Browser cache      "have I looked this up recently?"      → usually yes, stop here
2. Operating system   "have you?"
3. Your resolver      (your ISP, or 1.1.1.1, or 8.8.8.8)
4. Root & TLD servers "who's in charge of .io?"
5. Authoritative      "gyanl.github.io is 140.82.121.4"
```

Two consequences you will actually meet:

- **DNS is cached at every step**, with a time-to-live on each answer. This is why changing a domain's settings doesn't take effect instantly — the old answer is sitting in caches around the world until it expires. "Waiting for DNS to propagate" means "waiting for other people's caches to forget."
- **A domain is rented, not owned.** You pay a registrar annually. Let it lapse and the name points somewhere else, no matter how good your site is. It's the one part of your stack with an expiry date.

> **Sidenote:** When you attach a custom domain to GitHub Pages, all you're doing is adding a DNS record that says "this name points at GitHub's servers." That's the whole trick. Your files don't move.

## Step 2 — The request

Now the browser has a number, it opens a connection and sends an HTTP **request**. It's just text, and it's simpler than you'd expect:

```text
GET /my-first-site/about.html HTTP/1.1
Host: gyanl.github.io
User-Agent: Mozilla/5.0 ...
Accept: text/html
```

A **method** (`GET`), a **path**, and some **headers** — small labelled facts about the request. You already met methods in L5: `GET` to read, `POST` to send something substantial. Your browser has been sending `GET` requests on your behalf since week one; last week you sent a `POST` by hand.

## Step 3 — The response

The server answers in the same shape: a **status code**, headers, then the body — which for a web page is your HTML.

```text
HTTP/1.1 200 OK
Content-Type: text/html
Cache-Control: max-age=600

<!DOCTYPE html>
<html>...
```

The status codes come in families, and knowing the family is usually enough:

| Family | Means | Ones worth knowing |
| --- | --- | --- |
| **2xx** | Fine | **200** OK |
| **3xx** | It moved | **301** permanently, **302** temporarily |
| **4xx** | *You* got it wrong | **403** not allowed, **404** no such thing, **429** slow down |
| **5xx** | *They* got it wrong | **500** server broke, **503** overloaded |

The 4xx/5xx split is the one to remember, because it decides whose problem it is. A 404 on your github.io URL means GitHub is fine and your filename is wrong. A 500 means stop debugging your own code.

> **429** is the one that will bite you this term. It's what a free-tier API says when you've called it too often — you'll meet it in [[Lecture 7 - AI Features]].

## Step 4 — The browser builds the page

The response is text. Turning it into pixels is the browser's job, and it goes in a fixed order:

1. **Parse the HTML** into the **DOM** — a tree of objects, one per element. This is the thing `document.querySelector` searches. When you wrote `querySelector("#list").innerHTML = ...` last week, you were reaching into this tree and changing it, and the browser redrew.
2. **Parse the CSS** into its own tree of rules.
3. **Combine them** — every element paired with the styles that apply to it.
4. **Layout** — work out where everything goes and how big it is. This is where your `rem`, `%` and `max-width` from L4 get resolved into actual pixels, at this specific window size.
5. **Paint** — fill in the pixels.

Two behaviours you've already seen fall straight out of this:

- **CSS blocks rendering.** The browser won't paint until it has the stylesheet, because painting first would flash unstyled text. That's the right call, and it's why a slow stylesheet delays *everything*.
- **Fonts arrive late.** Your Google Font from L2 is a separate download, requested only after the CSS is read. `display=swap` says "paint in the fallback now, swap when it arrives" — that's why you sometimes see the text change shape a moment after load.

### Your one page is thirty requests

The HTML is only the beginning. As the browser parses it, it finds references to a stylesheet, some scripts, images, fonts — and fires off a request for each.

Open the Network tab on your own site and count. A "simple" page is routinely 20–50 requests, and the **waterfall** chart showing them is client-server architecture drawn live, on your own work.

Two things determine how long that takes, and people mix them up constantly:

- **Bandwidth** — how much data per second. Fixes big files.
- **Latency** — how long a single round trip takes, no matter how small. Fixes nothing; it's mostly distance and physics.

Thirty small requests on a high-latency connection is slower than one big one on the same pipe. This is why "just make the images smaller" sometimes doesn't help, and it's the whole reason CDNs exist — putting a copy of your files physically closer to the person asking.

### Caching, and why your change didn't show up

Responses come with instructions about how long they may be reused. Your browser keeps a copy and skips the request entirely next time.

This is why the second visit to any site is dramatically faster — and it's the real answer to a problem you've all already had. You pushed a CSS change, waited, refreshed, and saw the old page. GitHub had deployed it fine; your browser was showing you a copy it had saved. A hard refresh (**⌘⇧R** / **Ctrl+Shift+R**) says "ignore what you've got and ask again."

## HTTPS: what the padlock does and doesn't mean

The `s` is encryption. Everything between your browser and the server is scrambled, so anyone in between — the café wifi, the ISP, whoever — sees that you're talking to `gyanl.github.io` but not what you said.

**What it protects:** the conversation, in transit.

**What it does not protect:**

- **The site itself.** A phishing site can have a perfect padlock. It's free to get one. The padlock means "nobody is listening," not "these people are honest." This is the single most widely misunderstood symbol in software, and users have been trained to read it as a trust badge.
- **Anything after it arrives.** Your data is decrypted at the other end and stored however they store it.
- **What's in your page.** Your API key from [[Lecture 7 - AI Features]] travels beautifully encrypted, then sits in the page source for anyone to read. Encryption in transit does nothing about a secret you published.

> **Sidenote:** GitHub Pages gives you HTTPS free and on by default. Fifteen years ago this was expensive and fiddly and most small sites didn't bother. The web got meaningfully safer because someone made the secure option the lazy one — worth remembering next time you're designing a default.

## Not everything is request-response

One loose end from last week. HTTP is a conversation of turns: you ask, they answer, it's over. So how did your class wall update without anyone asking?

Firebase keeps a **persistent connection** open — a **WebSocket** — which stays alive and lets either side send whenever they like. That's the mechanism behind "subscribe, don't request," and behind every live thing you use: chat, cursors in Figma, live scores, notifications.

Two shapes, then. Ask-and-answer for almost everything; a held-open line when something needs to arrive unprompted.

## Class Activity

- **Exercise:** [[Exercise - Trace a Request]] — open the Network tab on your own site and take it apart, request by request.

We'll also do this together on a site you all know, and read a real waterfall on the projector.

## Homework

- Find the slowest-loading site you use regularly. Screenshot its network waterfall and come with a theory about *why* it's slow — too many requests, huge images, slow server, or far away? You'll need the vocabulary from today to answer.
- Optional, genuinely worth it: attach a custom domain to your GitHub Pages site and watch DNS do its thing. Bring questions.
