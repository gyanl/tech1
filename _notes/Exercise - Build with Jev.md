---
date: 29-09-2026
date modified: 29-09-2026
feed: show
tag: exercise
title: "Exercise - Build with Jev"
---

### Make something where a model decides, not writes

In [[Lecture 7 - What are LLMs?]] you tried the emoji picker: you type a sentence, and Jev picks from a fixed list. Now make your own. Your page asks Jev one question with answers you wrote, and does something with the answer.

It proves two things: that you can keep a key on a server, and that you can design a feature where the model can only choose outcomes you've already designed.

### Ideas

- **Your theme switcher** from [[Exercise - A Theme That Remembers]] picks one of your themes from a mood the visitor types.
- **Your realtime Q&A** sorts each new question into a topic, or flags duplicates.
- **Your crit board** checks whether a comment is actually about the work, and holds back the ones that aren't.
- **A contact form on your portfolio** that sorts messages into job, collaboration, hello, or spam.
- **A to-do list** that scores each task from "whenever" to "today".

Or anything else where one of Jev's three question types fits: yes or no, pick one, or a score on a scale.

### Steps

1. **Write the question first.** Choose the type (`boolean`, `choice` or `score`), write the instruction in one line, and write every possible answer with a few words describing it. That list is your design. Anything not on it can never happen.
2. **Try it in the terminal.** Before any page, send one request with `curl` (below) and read what comes back.
3. **Build the server and the page** from the code below. Use a new repo made from [web-starter](https://github.com/gyanl/web-starter), or add it to a project you already have on Vercel.
4. **Use the probabilities.** Decide what your page does when Jev isn't sure. Showing the top two, or asking the visitor, is often better than acting on a guess.
5. **Break it.** Nonsense, another language, an empty box, something that fits none of your answers, something that fits two.
6. **Ship it** on Vercel ([[Help - Host on Vercel]]).

### The key

I'll share a class key in the class group. It has a spending limit, and it's shared by everyone, so:

- **It only ever goes in Vercel**, under **Settings → Environment Variables**, named `AI_GATEWAY_API_KEY`. Never in your page, your repo, a screenshot or a chat with an AI tool.
- **Every call spends from the same pot.** A small question costs a fraction of a paisa. The emoji picker, with 255 options, costs about 2 paise a pick. When the limit runs out, it stops working for the whole class.
- **Don't call it on every keystroke, and don't loop it.** One call when someone presses a button.
- If you think the key has leaked, tell me straight away and I'll replace it.

### Try it in the terminal first

Paste the key in for this one terminal session only (it disappears when you close the window):

```bash
export AI_GATEWAY_API_KEY="paste-the-key-here"
```

Then ask Jev something:

```bash
curl https://ai-gateway.vercel.sh/v1/evaluate \
  -H "Authorization: Bearer $AI_GATEWAY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "typesafe-ai/jev",
    "state": "Hi! Loved your weather footer. Are you free for a project in November?",
    "questions": {
      "kind": {
        "type": "choice",
        "instructions": "What kind of message is this?",
        "criteria": {
          "job": "a job or internship offer",
          "collab": "asking to work together on a project",
          "hello": "just saying hi or giving feedback",
          "spam": "selling something or unrelated"
        }
      }
    }
  }'
```

You should get back something like `"choice": "collab"`, with a probability for every option.

### The server

`api/decide.js`:

```js
// Runs on Vercel, never in the visitor's browser.

module.exports = async (req, res) => {
  const text = ((req.body && req.body.text) || "").trim();
  if (text === "" || text.length > 500) {
    return res.status(400).json({ error: "Type something under 500 characters." });
  }

  const response = await fetch("https://ai-gateway.vercel.sh/v1/evaluate", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: "Bearer " + process.env.AI_GATEWAY_API_KEY
    },
    body: JSON.stringify({
      model: "typesafe-ai/jev",
      state: text,
      questions: {
        kind: {
          type: "choice",
          instructions: "What kind of message is this?",
          criteria: {
            job: "a job or internship offer",
            collab: "asking to work together on a project",
            hello: "just saying hi or giving feedback",
            spam: "selling something or unrelated"
          }
        }
      }
    })
  });

  if (!response.ok) {
    return res.status(502).json({ error: "Jev didn't answer. Try again in a minute." });
  }

  const data = await response.json();
  res.json(data.answers.kind);
};
```

Read it out loud:

1. **The `if`**: turn away empty or very long input before it costs anything.
2. **`fetch`**: send the text as `state`, and your question with every allowed answer in `criteria`.
3. **`process.env.AI_GATEWAY_API_KEY`**: the key comes from Vercel, not from this file.
4. **`res.json(data.answers.kind)`**: send the page Jev's choice and the probabilities.

### The page

In `index.html`:

```html
<form id="decide-form">
  <input id="message" type="text" placeholder="Write me a message" maxlength="500">
  <button>Send</button>
</form>
<p id="result"></p>
```

In `scripts.js`:

```js
const form = document.querySelector("#decide-form");
const result = document.querySelector("#result");

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  result.textContent = "Deciding…";

  const response = await fetch("/api/decide", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text: document.querySelector("#message").value })
  });
  const data = await response.json();

  if (!response.ok) {
    result.textContent = data.error;
    return;
  }
  const sure = Math.round(data.probabilities[data.choice] * 100);
  result.textContent = data.choice + " (" + sure + "% sure)";
});
```

To check it worked: open your `vercel.app` URL and send a message. View Source and search for the key: it shouldn't be there. In DevTools → **Network**, the request should go to `/api/decide`.

### Things to try

- Change the page, not just the text: a different colour, a different next step, or a different section shown depending on the choice.
- Ask two questions in one request, like a `choice` and a `boolean`. They're answered together, for the price of one.
- A `score` question instead: `"criteria": ["whenever", "this week", "today"]` returns a number along that scale.

### Things to keep in mind

- **Keep the list short and the descriptions clear.** Every option is sent with every call, so a long list costs more. Jev allows at most 255.
- **Jev can pick the wrong option, but never a new one.** Design for the wrong-but-allowed answer: can the visitor correct it?
- **Say it's a model.** A small line telling people a model sorted their message.

### Submission

- Live `vercel.app` URL
- Your question, written out: the type, the instruction, and every option with its description
- Screenshots of one confident answer, one unsure answer, and one you broke on purpose, each with what your page did
- One sentence on what your page does when Jev isn't sure, and why
