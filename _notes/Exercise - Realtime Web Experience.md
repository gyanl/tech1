---
date: 22-09-2026
date modified: 22-09-2026
feed: show
tag: exercise
title: "Exercise - Realtime Web Experience"
---

### Build something several people use at the same time

Create your own Firebase project and build a small realtime feature with it, live on your github.io URL. By using Realtime Database, you will get something that:

- survives a refresh
- appears on another person's screen without them refreshing

You should be able to demo the second one with a friend's phone next to your laptop.

### Setting it up

1. Go to [console.firebase.google.com](https://console.firebase.google.com) and **Add project**. Skip Google Analytics.
2. In the left sidebar, **Build → Realtime Database → Create Database**. Pick a location.
3. Choose **Start in test mode** for now.
4. Back on the project overview, click the **`</>`** (web) icon to register a web app. Firebase gives you a config snippet — copy it.
5. Paste the config into your AI coding agent and tell it to help you set up a feature. Some ideas below:

### Some possible ideas

You don't have to use any of these, and I would love to see more fun ones.

| Idea | What it does | What's in the tree |
| --- | --- | --- |
| **Live Q&A for a talk** | The audience posts questions and upvotes them. The speaker's screen shows the top ones. | `questions/{id}` with the text and a vote count |
| **Crit board** | Everyone pins a link to their work. Classmates leave short comments that appear on the projector as they're written. | `projects/{id}` and `comments/{projectId}/{id}` |
| **Group order** | One link for the table. Everyone adds what they want from the menu, and the total updates for everyone. | `order/{id}` with name, item and price |
| **Watch party remote** | One person presses play or pause, and the video pauses on everyone's screen. | `player` with `playing` and the current time |
| **Collaborative moodboard** | Anyone can drop an image URL onto a shared canvas and drag it around. Everyone sees it move. | `images/{id}` with URL and x, y position |
| **Live scoreboard** | Keep score for a match or a quiz night from your phone. The big screen updates. | `teams/{id}` with name and score |
| **Seat or slot booker** | A grid of slots. Tap one to claim it; it's greyed out for everyone else straight away. | `slots/{id}` with who booked it |
| **Presence** | A small "3 people are looking at this page" indicator for your portfolio. | `online/{visitorId}` — added on arrival, removed on leaving |

Some things to think about:

- **What does the page show before anyone has done anything?**
People don't automatically expect websites to behave like this - do you need to explain how your app works?
- **Who's allowed to change what?**
  In the watch party, should everyone control the video, or only the host?
- **What happens when two people do the same thing at once?**
  Two people trying to fill squares on the wall is part of the fun. But two people trying to edit a document is messier.
- **What should the page remember, and for how long?**
Should old Q&A questions disappear after the talk?
- **What does everyone see, and what's private?**
  Everyone's name on the crit board is fine. Everyone's phone number on the slot booker isn't.
- **How does someone know it's live?**
  A new comment appearing with no sign it just arrived is easy to miss. Think about a highlight, a sound or a counter.
- **What happens when it gets busy?**
Q&A with 5 questions is easy. What does it look like with 200?
- **What if someone leaves halfway?**
  If the host of the watch party closes their laptop, can anyone still pause the video? What happens to a booked slot nobody turns up for?
- **What if someone's connection drops?**
  Their change might arrive late, or after someone else's. Does it matter for your idea?


### Building it with AI

You'll have AI write most of the Firebase code. These prompts work in Claude, Cursor or ChatGPT. Replace the parts in square brackets. Each one asks for small steps and explanations, so you can follow what the code does and spot when it's wrong.

**1. Plan the data before any code**

```text
I'm building [detailed description of your idea] as a static website.

I want to use HTML, CSS, JavaScript, no framework and will use Firebase Realtime Database.

Before writing any code, suggest the shape of the JSON tree: which paths exist and what goes at each one. Keep it as shallow and small as possible. Show an example of the tree with 2–3 items of sample data, and explain each choice in one line.
```

**2. Connect the page to Firebase**

```text
Here is my Firebase config:
[paste the firebaseConfig object from the Firebase console]

Write the smallest possible code to connect my index.html to Firebase Realtime Database, using the Firebase JavaScript SDK loaded from the CDN in a <script type="module">.

Write the simplest version of the working code that I can test across multiple devices.
```

**3. Design the states AI usually skips**

```text
Improve this page so it handles:
- responsiveness
- the empty state, before anyone has added anything
- the loading state, while data is still arriving
- an empty or very long submission
- losing the internet connection

Tell me what you changed.
```

**4. Lock it down**

```text
My Realtime Database rules are currently read and write "true" in test mode. It will expire after 30 days and the app will stop working. 

Write security rules that make sense for this project. Explain each rule in plain language, and then help me update and test the rules on Firebase Console.
```

When something doesn't work, paste the error from the browser console (DevTools → **Console**) into the chat along with the code.

### Where to host it

Your site doesn't need anything new to use Realtime Database. The page talks to Firebase directly from the visitor's browser, so it works on GitHub Pages as it is. The Firebase config in your code is fine to publish — it says which database to use, and your rules decide what anyone can do with it.


### Then answer these

Write a short paragraph on each, and share it on whatsapp along with your link before next class.

- **What did people do to your data that you didn't expect?** Rudeness, spam, empty submissions, thousand-character messages, all of the above?
- **What did you set your rules to?** In plain language: what is the logic for who can read and write to your db?
- **How do you explain to users how it works?** Is there anything a new user needs to understand about what you made? Did you put this into the app?


### Submission

- Live URL
- The 3 paragraphs
