# Tech 1 course site

Jekyll site for Gyan's Tech 1 course (Web & Mobile Ecosystem Fundamentals), taught to design students. Lectures live in `_notes/Lecture N - Title.md`; the course plan (titles, dates, slugs, key areas) lives in `_data/lectures.yml`. Serve locally with the `jekyll` launch config; the site is under `/tech1/`.

## Tone of voice for lecture notes

The notes are Gyan talking to the class. They are read on the projector and again at home. Match the voice of Lectures 1–5 and the parts of Lecture 6 Gyan wrote directly.

### Who's talking, and to whom

- First person singular for the teacher ("I will frequently make you do something and explain later"), second person for students ("You already know this from design").
- The reader is a design student, not a future engineer. They need to understand enough to direct AI and make product decisions, not to memorise syntax.
- Speak to the room: "Let's look at your submissions!", "What do you see?", a `> **Sidenote:**` that asks the class a question.

### Say it plainly

- Plain, conversational sentences. Define a term in one line the first time it appears, then use it.
- Start from something concrete they already use: Gmail, Instagram, Figma, Dropbox, their own portfolio page. A comparison should be to a real product or tool, not an invented metaphor.
- One metaphor is enough, and only if it carries the explanation (the API "restaurant counter"). Don't stack cute images ("a little notebook", "memory for your app", "multiplayer is not magic").
- Be honest about limits and simplifications: "HTML is (kind of) responsive by default", "Honestly, for one person, you nearly could."
- No punchy closing aphorisms, rhetorical flourishes, or dramatic one-line paragraphs ("It's gone." "That's this week."). End a section when the information ends.
- Go easy on em dashes, bold and italics. Bold a term where it's defined, or the one thing to remember in a section. Not whole phrases in every paragraph.
- No jokes at the student's expense or snark in instructions ("name it something better than…").

### Build on what came before

- Continue the framing the lecture already sets up. If Gyan's intro raises a problem (sites reset on refresh; Gmail forgetting what's read), the next section answers that problem instead of restarting with a new hook.
- Refer back to earlier lectures by number ("the selectors you learnt in L3", "exactly what L2 was about").
- Do first, explain after: get them doing something, then say why it worked.

### Shape of a section

- Heading → a short plain explanation → a small code block or example → what to notice.
- For code, read it out loud: numbered steps or a one-line *italic paraphrase* of what each part does.
- Use a table when comparing two or more things (static vs dynamic, Dropbox vs Git, units).
- "Some things to note:" bullets for observations, each one short and concrete.
- Keep sections small. Prefer one working example to a list of every caveat; cover the caveats that will actually bite them.
- Say the design angle out loud where there is one ("The menu is a design decision", "Using rem is an accessibility decision").

### Exercises

- State what they'll make and what it proves, in a sentence or two.
- Give the minimum HTML/CSS/JS to get it working, in separate labelled blocks.
- Say how to check it worked (refresh, open on your phone, look in DevTools).
- "Things to try" extensions are optional and practical, not a checklist of everything the feature can do.
- Longer exercises get their own `Exercise - Name.md` note linked with `[[…]]`.

### Specifics

- Use Gyan's real examples: `gyanl`, Bengaluru, the course site, the web-starter template, `#ff4343`.
- Spelling in existing notes mixes British and American ("colour", "color" in code). Follow whatever the surrounding lecture uses in prose; CSS is always `color`.
