---
date: 24-07-2026
date modified: 04-08-2026
feed: show
title: "AI Policy"
---

See also: [[Grading]] · [[Syllabus]]

In many courses, an AI policy is a list of things you can't do. This course is different: **using AI to generate code is the expected way of working here.** The skill this course teaches is *directing* AI tools well — which means the policy is less about restriction and more about honesty.

Design as a career is changing - along with many other lines of work. Using AI is becoming the default way of working. You will spend your career working with AI tools. Employers will not ask whether you used AI; they will ask whether the thing works, whether it's well-designed, and whether you understand it. This policy is practice for that reality.

### The short version

> Use AI for everything. Understand everything you ship. Show your process. Never present work you can't explain.
>
> **AI writes the code. You write the words.**

### What is encouraged

- **Generating code with AI** — Claude, Cursor, v0, Lovable, Figma Make, Copilot, whatever works. Switching tools mid-project is fine; tool fluency is part of the point.
- **Using AI to learn** — asking it to explain code it (or someone else) wrote, decode error messages, compare approaches, or quiz you before a presentation.
- **Using AI as a research assistant** — for exercises like [[Exercise - Mobile Ecosystem Comparison]], with the caveat below about verification.
- **Iterating in plain language** — a well-written prompt log is a design artifact. Keep yours.

### Writing is different from code

AI will write most of your code in this course. It should not write most of your words.

Code is judged by whether it works. Writing is judged by whether it gets an idea from your head into someone else's — and a model can't do that for you, because it doesn't know what you were trying to say.

- **Stand behind every sentence.**
  If I ask "what did you mean here?", *"the AI wrote that, ignore it"* is not an answer. Everything you hand in should represent your actual thinking. Readers either notice the parts that aren't yours, or — worse — believe them.
- **Writing is thinking.**
  Your proposal, your process documentation, your reflection: the document is not the point, the thinking is. Deciding what matters and what order to say it in is how you come to understand your own project. Outsource the writing and you skip the understanding.
- **Respect your reader's time.**
  Generating a long document from a short prompt doesn't save work, it moves work from you to your reader — and one person writes while everyone reads. If your document says less than the prompt that produced it, share the prompt instead.
- **Longer is not better.**
  Pascal: *"I have made this letter longer than usual because I have not had time to make it shorter."* There is no lossless rewrite — every rephrasing shifts the meaning, and when it's done by something that doesn't know what you meant, meaning is lost. I would rather read your words than polished ones.
- **Quoting AI is fine if you mark it.**
  *"Claude suggested this approach — worth exploring?"* is honest and often useful. The same sentence presented as your own thinking is not.

**This applies to:** proposals, process documentation, reflections, comparison write-ups, crit feedback, and anything you present.
**Not to:** code, boilerplate, and the plumbing nobody writes by hand any more.

### What is required

1. **Understanding**
   If you submitted it, you should be able to explain it (at the level this course teaches). "Where does this data live?", "What happens when I click this?", "Why is this an API call?" are fair questions about *your own* project, in any presentation or exam, and "the AI did it" is not an answer.
2. **Process documentation**
   Every submission includes your prompts: key prompts, major iterations, dead ends. This is how I will grade your process. If I ask how you arrived at something, you should be able to show me the path.
3. **Verification**
   AI states things confidently and is sometimes wrong. Any number, fee, policy, or fact that an AI gives you gets checked against a primary source before it goes in your work. Stale App Store fees in a submission tell me you didn't check.
4. **Attribution**
   Cite references, templates, fonts, images, substantial code you took from other humans, and the work of classmates. AI-generated code doesn't need a citation — but the *inputs* you gave it (someone else's design, someone's copyrighted assets) keep their original owners.

### What is dishonest

- Presenting work you can't explain at the level this course teaches.
- Hiding or fabricating your process
- Submitting another student's project, prompts, or documentation with cosmetic changes
- Having AI (or anyone) impersonate you in things that must be your own voice — peer feedback, reflections, exam answers where stated
- Handing in AI-written prose as your own thinking, unmarked, in a proposal, write-up or reflection

### Practical safety rules

These aren't academic-integrity rules - just general best practices

- **Never put API keys or secrets in front-end code or a public repo.**
  Ask the AI "are any secrets exposed to the client?" — then verify yourself.
- **Don't paste personal data** (yours or anyone else's) into AI tools or deploy it to public projects. Class-collected data stays anonymised.
- **You are responsible for what your product does.** If your AI-built guestbook lets strangers post anything to a public page, that was a design decision you made by not making it.
