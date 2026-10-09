---
date: 09-10-2026
date modified: 09-10-2026
feed: show
tag: exercise
title: "Exercise - Sign in with Google"
---

### Add Sign in with Google to your multiplayer experience

Take what you built in [[Exercise - Realtime Web Experience]] and make people sign in with Google before they can change anything. Same Firebase project, same github.io URL.

It proves that your rules can finally tell people apart. The Realtime exercise asked "who's allowed to change what?", and until now the honest answer was "anyone". By the end, people can only change their own things.

### 1. Switch it on in Firebase

1. In the [Firebase console](https://console.firebase.google.com), open your project and go to **Build → Authentication → Get started**.
2. Under **Sign-in method**, choose **Google**, turn on **Enable**, pick your email as the support email, and save.
3. Go to **Authentication → Settings → Authorized domains** and add `yourusername.github.io`.

The sign-in popup only opens on domains in that list. Without step 3 it works on your laptop and fails on your live site.

### 2. Ask AI to add it

Paste this into Claude, Cursor or ChatGPT along with your current code, and fill in the brackets:

```text
My site is a [describe your multiplayer experience] using Firebase Realtime Database, in plain HTML, CSS and JavaScript with no framework.

Add Firebase Authentication with Sign in with Google, loaded from the CDN in my existing <script type="module">.
- Show a Sign in button when nobody is signed in.
- When someone is signed in, show their name and photo and a Sign out button.
- Use user.uid and user.displayName wherever I currently use a name people type.
- Don't change anything else.

Explain each new part in one line.
```

In what comes back, find these three and read them out loud:

- **`signInWithPopup`**: opens Google's sign-in window.
- **`onAuthStateChanged`**: runs whenever someone signs in or out, including when the page first loads. This is where your page decides what to show.
- **`signOut`**: signs them out.

Push it, open your github.io URL, and sign in.

### 3. Change the rules

Signing in on the page doesn't protect anything yet. The database rules from L6 still say anyone can write. Change them in two steps:

1. **Only signed-in people can write.** Replace `".write": true` with `".write": "auth != null"`.
2. **Only the person who made something can change it.** Save the `uid` with each item you write, and have the rule check it against `auth.uid`.

Ask AI to write the second step for your own tree:

```text
Here is the shape of my Realtime Database tree: [paste an example with 2–3 items].
Each item now has a uid field with the Firebase Auth uid of the person who made it.

Write security rules so that anyone can read, only signed-in people can add items, and only the person who made an item can change or delete it. Explain each rule in plain language.
```

Read every line before you publish it in **Realtime Database → Rules**. You should be able to point at the line that stops someone editing your things.

### 4. Check it worked

- **Signed out:** try to do something. What does the page say? It should tell you to sign in, not fail silently.
- **Someone else:** open it on a friend's phone, signed in as them. They can add their own things but can't change yours.
- **No page at all:** rerun the "paint as someone else" `fetch` from [[Exercise - Hack the Wall]] against your own database URL. It should come back `Permission denied`.

### Things to try

- Show who did what: put each person's photo next to the things they made.
- Decide what a signed-out visitor sees. Everything read-only, a preview, or nothing until they sign in? See "Sign-in is a design decision" in [[Lecture 8 - Authentication & Authorisation]].
- Add a second provider, like GitHub. Which one would your users actually pick?

### Submission

- Your live URL
