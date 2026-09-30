---
date: 29-09-2026
date modified: 30-09-2026
feed: show
key_areas:
  - "LLM APIs"
  - "AI features in products"
  - "AI-assisted development"
  - "Prompting as design"
  - "Server-side languages"
tag: lecture
title: "Lecture 7 - What are LLMs?"
---

## Homework Review

Let's look at your submissions!

- [[Exercise - Realtime Web Experience]]

What did people do to your data that you didn't expect?

---

## Using AI to build sites vs AI features in sites

You've used AI to build things every week, but the things you built were not AI apps. This week AI goes inside the things you build.

### Rewind to Anything API

Open this in a browser tab:

```text
https://api.gyanl.com/excuse/late-to-class
```

You will get a response in a second or two, and all of you should have a different answer. Look at the field names too. When I tried it, one came back with `"credibility": 8.5` and the other with `"believability": "low"`. You saw the same thing in [[Exercise - Build with the Anything API]].

> **Discuss:** When the Anything API invented an excuse for being late to class, did it understand what being late is? What would convince you either way?

There's no database behind `api.gyanl.com`. Every request goes to a language model, which writes the JSON on the spot. The code is public at [github.com/gyanl/anything-api](https://github.com/gyanl/anything-api). It's one file, and this is the instruction the model gets on every request:

```js
let systemPrompt = `You are a helpful AI assistant that lives at api.gyanl.com and generates JSON responses for any endpoint. Respond ONLY with a single valid JSON object. Keep the fields returned to the minimum, ideally 1-2 unless more make sense. Don't include any other text or comments. The user is requesting information for the endpoint: ${path}.`;
```

{: .wrap}

```{path}``` refers to the ```/excuse/late-to-class``` part of the URL.

## What a language model is

A **language model** (LLM) is a program trained on a huge amount of text to do one thing: given some text, predict what comes next. It writes its answer a few letters at a time, guessing the likely next piece each time.

### Tokens

Those pieces are called **tokens**. A model doesn't read letters or whole words. Before it sees any text, the text is chopped into tokens: a common word like "the" is usually one token, a rarer word like "Bengaluru" gets split into a few, and spaces and punctuation count too. In English, a token is about three quarters of a word, so 100 tokens is roughly 75 words.

Try it: paste a sentence into [OpenAI's tokenizer](https://platform.openai.com/tokenizer) and it colours each token. Then paste the same sentence in Hindi or Kannada.

Some things to note:

- **Tokens are what you pay for.** Every model API charges per token, for what you send and what comes back. More on that below.
- **Model context limits are in tokens** A model can only accept a limited number of tokens: your system prompt, the conversation so far and its answer all have to fit. That limit is called the **context window**.
- **Indian languages cost more.** Most tokenizers were built mostly from English text, so the same sentence in Hindi or Kannada often splits into several times as many tokens. It costs more, runs slower and fits less in the context window. Part of the pitch for Indian models like Sarvam's is tokenizers built for Indian languages.
- **It's why models are bad at spelling games.** For a long time, if you asked an AI model how many r's are in "strawberry", most models would get it wrong. They had to guess, because they saw a couple of tokens, not ten letters.

It has no table of facts to look things up in, so:

- It makes things up. Since it's predicting the next 'token' without any understanding of what that means, you get something that *sounds* correct but may or may not be correct.
- It's good at working with information it has or information you give it. It will write you a lovely email, but may invent last month's sales figures. These are what we call hallucinations. Over time models are getting a bit better at admitting when they don't know something instead of hallucinating, but this is still not fully solved.
- It only knows what it read up to a certain date. It has never heard of anything outside of it's training data. The cutoff date could be a year or two in the past.
- It's unreliable at counting and sums, although thinking improves this behaviour. If you let a model write code to do the calculations they are generally much more accurate.

## How a model is made

Finish these out loud:

- The capital city of India is ___
- Once upon a ___
- `<h1>`Hello World`</___>`

You didn't look anything up. You've seen enough text that the next word is obvious. A model learns the same way, at a much bigger scale.

### 1. Pretraining

The model is shown a huge amount of text: a large share of the public internet, books, and code from sites like GitHub. For each piece it guesses the next word, checks the real one, and its numbers get nudged so the right answer is a little more likely next time. This happens trillions of times, on thousands of specialised chips (mostly made by Nvidia), for months. The biggest training runs reportedly cost hundreds of millions of dollars, which is well over ₹1,000 crore.

Much of that money goes on Nvidia's chips. Nvidia used to be known for graphics cards for gamers. This is its share price over the last ten years:

<figure class="nvda-chart">
<div class="nvda-plot">
<svg viewBox="0 0 480 270" role="img" aria-labelledby="nvda-title nvda-desc">
<title id="nvda-title">Nvidia share price, October 2016 to September 2026</title>
<desc id="nvda-desc">Monthly closing price in US dollars, adjusted for stock splits. About $1.78 in October 2016, under $20 when ChatGPT launched in November 2022, and $229 in September 2026.</desc>
<line x1="0" x2="480" y1="242.0" y2="242.0" stroke="var(--color-border)" stroke-width="1"/><line x1="0" x2="480" y1="196.8" y2="196.8" stroke="var(--color-border-light)" stroke-width="1"/><text x="0" y="192.8" class="nvda-axis">$50</text><line x1="0" x2="480" y1="151.6" y2="151.6" stroke="var(--color-border-light)" stroke-width="1"/><text x="0" y="147.6" class="nvda-axis">$100</text><line x1="0" x2="480" y1="106.4" y2="106.4" stroke="var(--color-border-light)" stroke-width="1"/><text x="0" y="102.4" class="nvda-axis">$150</text><line x1="0" x2="480" y1="61.2" y2="61.2" stroke="var(--color-border-light)" stroke-width="1"/><text x="0" y="57.2" class="nvda-axis">$200</text><line x1="0" x2="480" y1="16.0" y2="16.0" stroke="var(--color-border-light)" stroke-width="1"/><text x="0" y="12.0" class="nvda-axis">$250</text><text x="60.1" y="262" text-anchor="middle" class="nvda-axis">2018</text><text x="156.1" y="262" text-anchor="middle" class="nvda-axis">2020</text><text x="252.3" y="262" text-anchor="middle" class="nvda-axis">2022</text><text x="348.3" y="262" text-anchor="middle" class="nvda-axis">2024</text><text x="444.5" y="262" text-anchor="middle" class="nvda-axis">2026</text>
<line x1="296.1" x2="296.1" y1="16" y2="242" stroke="var(--color-border)" stroke-width="1" stroke-dasharray="2 3"/><text x="300.1" y="26" text-anchor="start" class="nvda-note">ChatGPT</text><line x1="399.9" x2="399.9" y1="16" y2="242" stroke="var(--color-border)" stroke-width="1" stroke-dasharray="2 3"/><text x="395.9" y="42" text-anchor="end" class="nvda-note">DeepSeek R1</text>
<polyline points="0.0,240.4 4.1,239.9 8.0,239.6 12.1,239.5 16.2,239.7 19.9,239.5 23.9,239.6 27.9,238.7 32.0,238.7 35.9,238.3 40.0,238.2 44.1,238.0 48.0,237.3 52.1,237.5 56.0,237.6 60.1,236.4 64.2,236.5 67.9,236.8 72.0,236.9 75.9,236.3 80.0,236.6 83.9,236.5 88.0,235.7 92.1,235.6 96.0,237.2 100.1,238.3 104.1,239.0 108.1,238.8 112.2,238.5 115.9,237.9 120.0,237.9 123.9,238.9 128.0,238.3 131.9,238.2 136.0,238.2 140.1,238.1 144.0,237.5 148.1,237.1 152.1,236.7 156.1,236.7 160.2,235.9 164.0,236.0 168.1,235.4 172.1,234.0 176.1,233.4 180.1,232.4 184.2,229.9 188.2,229.8 192.2,230.7 196.3,229.9 200.2,230.2 204.3,230.3 208.4,229.6 212.0,229.9 216.1,228.4 220.1,227.3 224.1,223.9 228.1,224.4 232.2,221.8 236.3,223.3 240.2,218.9 244.3,212.5 248.2,215.4 252.3,219.9 256.4,220.0 260.1,217.3 264.1,225.2 268.1,225.1 272.2,228.3 276.1,225.6 280.2,228.4 284.3,231.0 288.2,229.8 292.3,226.7 296.2,228.8 300.3,224.3 304.4,221.0 308.1,216.9 312.2,216.9 316.1,207.8 320.2,203.8 324.1,199.8 328.2,197.4 332.3,202.7 336.2,205.1 340.3,199.7 344.2,197.2 348.3,186.4 352.4,170.5 356.2,160.3 360.3,163.9 364.2,142.9 368.3,130.3 372.3,136.2 376.3,134.1 380.4,132.2 384.4,122.0 388.4,117.0 392.4,120.6 396.5,133.5 400.5,129.1 404.2,144.0 408.3,143.5 412.3,119.8 416.3,99.2 420.3,81.2 424.4,84.5 428.4,73.3 432.4,58.9 436.5,82.0 440.4,73.4 444.5,69.2 448.6,81.8 452.2,84.3 456.3,61.6 460.3,51.1 464.3,61.1 468.3,60.5 472.4,42.4 480.0,35.1" class="nvda-line"/>
<text x="4.0" y="232.4" class="nvda-value">$1.78</text><circle cx="480.0" cy="35.1" r="4" class="nvda-dot"/><text x="472.0" y="31.1" text-anchor="end" class="nvda-value">$229</text>
<line class="nvda-cross" x1="0" x2="0" y1="16" y2="242"/>
<circle class="nvda-hover" r="5" cx="0" cy="0"/>
<rect class="nvda-hit" x="0" y="0" width="480" height="270"/>
</svg>
<div class="nvda-tip" aria-hidden="true"></div>
</div>
<figcaption>Nvidia's share price, monthly close in US$, adjusted for stock splits. At today's rate of about ₹96 to the dollar, $229 is about ₹22,000. Data: Yahoo Finance.</figcaption>
<details><summary>Show the numbers</summary><table><thead><tr><th>End of</th><th>Price</th></tr></thead><tbody><tr><td>Oct 2016</td><td>$1.78</td></tr><tr><td>2016</td><td>$2.67</td></tr><tr><td>2017</td><td>$4.84</td></tr><tr><td>2018</td><td>$3.34</td></tr><tr><td>2019</td><td>$5.88</td></tr><tr><td>2020</td><td>$13.06</td></tr><tr><td>2021</td><td>$29.41</td></tr><tr><td>2022</td><td>$14.61</td></tr><tr><td>2023</td><td>$49.52</td></tr><tr><td>2024</td><td>$134.29</td></tr><tr><td>2025</td><td>$186.50</td></tr><tr><td>28 Sep 2026</td><td>$228.86</td></tr></tbody></table></details>
</figure>
<style>
.nvda-chart { --nvda-line: #0F6B33; }
.content .nvda-chart { margin: 1.5rem 0; }
html[data-theme="dark"] .nvda-chart { --nvda-line: #34A862; }
@media (prefers-color-scheme: dark) { html:not([data-theme="light"]) .nvda-chart { --nvda-line: #34A862; } }
.nvda-plot { position: relative; }
.nvda-chart svg { display: block; width: 100%; height: auto; overflow: visible; }
.nvda-axis { font-family: var(--font-mono); font-size: 11px; fill: var(--color-text-sub); }
.nvda-note { font-size: 11px; fill: var(--color-text-sub); }
.nvda-value { font-size: 12px; font-weight: 600; fill: var(--color-text-main); }
.nvda-line { fill: none; stroke: var(--nvda-line); stroke-width: 2; stroke-linejoin: round; stroke-linecap: round; }
.nvda-dot, .nvda-hover { fill: var(--nvda-line); stroke: var(--color-bg-main); stroke-width: 2; }
.nvda-cross { stroke: var(--color-text-sub); stroke-width: 1; }
.nvda-cross, .nvda-hover { visibility: hidden; pointer-events: none; }
.nvda-hit { fill: transparent; cursor: crosshair; }
.nvda-tip { position: absolute; top: 0; left: 0; pointer-events: none; visibility: hidden; white-space: nowrap; font-size: 0.8rem; padding: 0.3rem 0.5rem; border-radius: 4px; background: var(--color-bg-main); color: var(--color-text-main); border: 1px solid var(--color-border); }
.nvda-chart figcaption { font-size: 0.85rem; color: var(--color-text-sub); margin-top: 0.5rem; }
.nvda-chart details { margin-top: 0.5rem; font-size: 0.85rem; }
</style>
<script>
(function () {
  const data = [{"m": "Oct 2016", "v": 1.78, "x": 0.0, "y": 240.4}, {"m": "Nov 2016", "v": 2.31, "x": 4.1, "y": 239.9}, {"m": "Dec 2016", "v": 2.67, "x": 8.0, "y": 239.6}, {"m": "Jan 2017", "v": 2.73, "x": 12.1, "y": 239.5}, {"m": "Feb 2017", "v": 2.54, "x": 16.2, "y": 239.7}, {"m": "Mar 2017", "v": 2.72, "x": 19.9, "y": 239.5}, {"m": "Apr 2017", "v": 2.61, "x": 23.9, "y": 239.6}, {"m": "May 2017", "v": 3.61, "x": 27.9, "y": 238.7}, {"m": "Jun 2017", "v": 3.61, "x": 32.0, "y": 238.7}, {"m": "Jul 2017", "v": 4.06, "x": 35.9, "y": 238.3}, {"m": "Aug 2017", "v": 4.24, "x": 40.0, "y": 238.2}, {"m": "Sep 2017", "v": 4.47, "x": 44.1, "y": 238.0}, {"m": "Oct 2017", "v": 5.17, "x": 48.0, "y": 237.3}, {"m": "Nov 2017", "v": 5.02, "x": 52.1, "y": 237.5}, {"m": "Dec 2017", "v": 4.84, "x": 56.0, "y": 237.6}, {"m": "Jan 2018", "v": 6.14, "x": 60.1, "y": 236.4}, {"m": "Feb 2018", "v": 6.05, "x": 64.2, "y": 236.5}, {"m": "Mar 2018", "v": 5.79, "x": 67.9, "y": 236.8}, {"m": "Apr 2018", "v": 5.62, "x": 72.0, "y": 236.9}, {"m": "May 2018", "v": 6.3, "x": 75.9, "y": 236.3}, {"m": "Jun 2018", "v": 5.92, "x": 80.0, "y": 236.6}, {"m": "Jul 2018", "v": 6.12, "x": 83.9, "y": 236.5}, {"m": "Aug 2018", "v": 7.02, "x": 88.0, "y": 235.7}, {"m": "Sep 2018", "v": 7.03, "x": 92.1, "y": 235.6}, {"m": "Oct 2018", "v": 5.27, "x": 96.0, "y": 237.2}, {"m": "Nov 2018", "v": 4.09, "x": 100.1, "y": 238.3}, {"m": "Dec 2018", "v": 3.34, "x": 104.1, "y": 239.0}, {"m": "Jan 2019", "v": 3.59, "x": 108.1, "y": 238.8}, {"m": "Feb 2019", "v": 3.86, "x": 112.2, "y": 238.5}, {"m": "Mar 2019", "v": 4.49, "x": 115.9, "y": 237.9}, {"m": "Apr 2019", "v": 4.53, "x": 120.0, "y": 237.9}, {"m": "May 2019", "v": 3.39, "x": 123.9, "y": 238.9}, {"m": "Jun 2019", "v": 4.11, "x": 128.0, "y": 238.3}, {"m": "Jul 2019", "v": 4.22, "x": 131.9, "y": 238.2}, {"m": "Aug 2019", "v": 4.19, "x": 136.0, "y": 238.2}, {"m": "Sep 2019", "v": 4.35, "x": 140.1, "y": 238.1}, {"m": "Oct 2019", "v": 5.03, "x": 144.0, "y": 237.5}, {"m": "Nov 2019", "v": 5.42, "x": 148.1, "y": 237.1}, {"m": "Dec 2019", "v": 5.88, "x": 152.1, "y": 236.7}, {"m": "Jan 2020", "v": 5.91, "x": 156.1, "y": 236.7}, {"m": "Feb 2020", "v": 6.75, "x": 160.2, "y": 235.9}, {"m": "Mar 2020", "v": 6.59, "x": 164.0, "y": 236.0}, {"m": "Apr 2020", "v": 7.31, "x": 168.1, "y": 235.4}, {"m": "May 2020", "v": 8.88, "x": 172.1, "y": 234.0}, {"m": "Jun 2020", "v": 9.5, "x": 176.1, "y": 233.4}, {"m": "Jul 2020", "v": 10.61, "x": 180.1, "y": 232.4}, {"m": "Aug 2020", "v": 13.37, "x": 184.2, "y": 229.9}, {"m": "Sep 2020", "v": 13.53, "x": 188.2, "y": 229.8}, {"m": "Oct 2020", "v": 12.53, "x": 192.2, "y": 230.7}, {"m": "Nov 2020", "v": 13.4, "x": 196.3, "y": 229.9}, {"m": "Dec 2020", "v": 13.06, "x": 200.2, "y": 230.2}, {"m": "Jan 2021", "v": 12.99, "x": 204.3, "y": 230.3}, {"m": "Feb 2021", "v": 13.71, "x": 208.4, "y": 229.6}, {"m": "Mar 2021", "v": 13.35, "x": 212.0, "y": 229.9}, {"m": "Apr 2021", "v": 15.01, "x": 216.1, "y": 228.4}, {"m": "May 2021", "v": 16.24, "x": 220.1, "y": 227.3}, {"m": "Jun 2021", "v": 20.0, "x": 224.1, "y": 223.9}, {"m": "Jul 2021", "v": 19.5, "x": 228.1, "y": 224.4}, {"m": "Aug 2021", "v": 22.39, "x": 232.2, "y": 221.8}, {"m": "Sep 2021", "v": 20.72, "x": 236.3, "y": 223.3}, {"m": "Oct 2021", "v": 25.57, "x": 240.2, "y": 218.9}, {"m": "Nov 2021", "v": 32.68, "x": 244.3, "y": 212.5}, {"m": "Dec 2021", "v": 29.41, "x": 248.2, "y": 215.4}, {"m": "Jan 2022", "v": 24.49, "x": 252.3, "y": 219.9}, {"m": "Feb 2022", "v": 24.39, "x": 256.4, "y": 220.0}, {"m": "Mar 2022", "v": 27.29, "x": 260.1, "y": 217.3}, {"m": "Apr 2022", "v": 18.55, "x": 264.1, "y": 225.2}, {"m": "May 2022", "v": 18.67, "x": 268.1, "y": 225.1}, {"m": "Jun 2022", "v": 15.16, "x": 272.2, "y": 228.3}, {"m": "Jul 2022", "v": 18.16, "x": 276.1, "y": 225.6}, {"m": "Aug 2022", "v": 15.09, "x": 280.2, "y": 228.4}, {"m": "Sep 2022", "v": 12.14, "x": 284.3, "y": 231.0}, {"m": "Oct 2022", "v": 13.5, "x": 288.2, "y": 229.8}, {"m": "Nov 2022", "v": 16.92, "x": 292.3, "y": 226.7}, {"m": "Dec 2022", "v": 14.61, "x": 296.2, "y": 228.8}, {"m": "Jan 2023", "v": 19.54, "x": 300.3, "y": 224.3}, {"m": "Feb 2023", "v": 23.22, "x": 304.4, "y": 221.0}, {"m": "Mar 2023", "v": 27.78, "x": 308.1, "y": 216.9}, {"m": "Apr 2023", "v": 27.75, "x": 312.2, "y": 216.9}, {"m": "May 2023", "v": 37.83, "x": 316.1, "y": 207.8}, {"m": "Jun 2023", "v": 42.3, "x": 320.2, "y": 203.8}, {"m": "Jul 2023", "v": 46.73, "x": 324.1, "y": 199.8}, {"m": "Aug 2023", "v": 49.35, "x": 328.2, "y": 197.4}, {"m": "Sep 2023", "v": 43.5, "x": 332.3, "y": 202.7}, {"m": "Oct 2023", "v": 40.78, "x": 336.2, "y": 205.1}, {"m": "Nov 2023", "v": 46.77, "x": 340.3, "y": 199.7}, {"m": "Dec 2023", "v": 49.52, "x": 344.2, "y": 197.2}, {"m": "Jan 2024", "v": 61.53, "x": 348.3, "y": 186.4}, {"m": "Feb 2024", "v": 79.11, "x": 352.4, "y": 170.5}, {"m": "Mar 2024", "v": 90.36, "x": 356.2, "y": 160.3}, {"m": "Apr 2024", "v": 86.4, "x": 360.3, "y": 163.9}, {"m": "May 2024", "v": 109.63, "x": 364.2, "y": 142.9}, {"m": "Jun 2024", "v": 123.54, "x": 368.3, "y": 130.3}, {"m": "Jul 2024", "v": 117.02, "x": 372.3, "y": 136.2}, {"m": "Aug 2024", "v": 119.37, "x": 376.3, "y": 134.1}, {"m": "Sep 2024", "v": 121.44, "x": 380.4, "y": 132.2}, {"m": "Oct 2024", "v": 132.76, "x": 384.4, "y": 122.0}, {"m": "Nov 2024", "v": 138.25, "x": 388.4, "y": 117.0}, {"m": "Dec 2024", "v": 134.29, "x": 392.4, "y": 120.6}, {"m": "Jan 2025", "v": 120.07, "x": 396.5, "y": 133.5}, {"m": "Feb 2025", "v": 124.92, "x": 400.5, "y": 129.1}, {"m": "Mar 2025", "v": 108.38, "x": 404.2, "y": 144.0}, {"m": "Apr 2025", "v": 108.92, "x": 408.3, "y": 143.5}, {"m": "May 2025", "v": 135.13, "x": 412.3, "y": 119.8}, {"m": "Jun 2025", "v": 157.99, "x": 416.3, "y": 99.2}, {"m": "Jul 2025", "v": 177.87, "x": 420.3, "y": 81.2}, {"m": "Aug 2025", "v": 174.18, "x": 424.4, "y": 84.5}, {"m": "Sep 2025", "v": 186.58, "x": 428.4, "y": 73.3}, {"m": "Oct 2025", "v": 202.49, "x": 432.4, "y": 58.9}, {"m": "Nov 2025", "v": 177.0, "x": 436.5, "y": 82.0}, {"m": "Dec 2025", "v": 186.5, "x": 440.4, "y": 73.4}, {"m": "Jan 2026", "v": 191.13, "x": 444.5, "y": 69.2}, {"m": "Feb 2026", "v": 177.19, "x": 448.6, "y": 81.8}, {"m": "Mar 2026", "v": 174.4, "x": 452.2, "y": 84.3}, {"m": "Apr 2026", "v": 199.57, "x": 456.3, "y": 61.6}, {"m": "May 2026", "v": 211.14, "x": 460.3, "y": 51.1}, {"m": "Jun 2026", "v": 200.09, "x": 464.3, "y": 61.1}, {"m": "Jul 2026", "v": 200.75, "x": 468.3, "y": 60.5}, {"m": "Aug 2026", "v": 220.78, "x": 472.4, "y": 42.4}, {"m": "28 Sep 2026", "v": 228.86, "x": 480.0, "y": 35.1}];
  const fig = document.currentScript.previousElementSibling.previousElementSibling;
  const svg = fig.querySelector("svg");
  const cross = svg.querySelector(".nvda-cross");
  const dot = svg.querySelector(".nvda-hover");
  const tip = fig.querySelector(".nvda-tip");
  function show(evt) {
    const pt = svg.createSVGPoint();
    const src = evt.touches ? evt.touches[0] : evt;
    pt.x = src.clientX; pt.y = src.clientY;
    const p = pt.matrixTransform(svg.getScreenCTM().inverse());
    let best = data[0];
    for (const d of data) { if (Math.abs(d.x - p.x) < Math.abs(best.x - p.x)) best = d; }
    cross.setAttribute("x1", best.x); cross.setAttribute("x2", best.x);
    dot.setAttribute("cx", best.x); dot.setAttribute("cy", best.y);
    cross.style.visibility = dot.style.visibility = "visible";
    tip.textContent = best.m + " · $" + best.v.toFixed(2);
    const scale = svg.clientWidth / 480;
    let left = best.x * scale + 10;
    if (left + tip.offsetWidth > svg.clientWidth) left = best.x * scale - tip.offsetWidth - 10;
    tip.style.left = left + "px";
    tip.style.top = Math.max(0, best.y * scale - 36) + "px";
    tip.style.visibility = "visible";
  }
  function hide() { cross.style.visibility = dot.style.visibility = tip.style.visibility = "hidden"; }
  const hit = svg.querySelector(".nvda-hit");
  hit.addEventListener("mousemove", show);
  hit.addEventListener("touchmove", show, { passive: true });
  hit.addEventListener("mouseleave", hide);
  hit.addEventListener("touchend", hide);
})();
</script>

What comes out is a file of numbers called **weights** (or parameters). When you read that a model has "105 billion parameters", that's how many numbers are in the file. Nobody writes grammar rules or facts into it. It works them out from the text, which is the argument of this week's reading, [The Bitter Lesson](#reading-the-bitter-lesson).

### 2. Learn to be an assistant

A model that has only been pretrained just continues text. Ask it "What's the capital of Karnataka?" and it might reply with three more quiz questions, because on the internet that's often what follows a question.

So in the second stage, people write thousands of example conversations for it to copy. Then people are shown two answers to the same question and pick the better one, and the model is nudged towards the answers people preferred. This is called **RLHF**, reinforcement learning from human feedback.

This stage is where the tone, the format and the refusals come from. ChatGPT sounds like ChatGPT and Claude sounds like Claude because people decided they should. Anthropic publishes the principles it trains Claude on as a "constitution", and OpenAI publishes a "Model Spec". They're system prompts for the whole model, written a level above yours.

### 3. Think before answering

Since OpenAI's o1 in late 2024, many models are trained to write out their working before they answer. You usually don't see it. These **reasoning** models are better at maths, code and planning, but they're slower and use more tokens, so they cost more.

## Does the AI "understand" anything?

People have argued about this since long before ChatGPT, and since long before computers could hold a conversation at all.

### The Turing test

In 1950 the mathematician Alan Turing asked whether machines can think, then suggested a more practical question instead. He called it the imitation game, and it's now called the **Turing test**: a judge chats by text with two hidden partners, one a person and one a machine. If the judge can't reliably tell which is which, the machine passes. Turing predicted that by around 2000, a machine would fool an average judge at least 30% of the time after five minutes of chat.

### ELIZA

In 1966 Joseph Weizenbaum at MIT made **ELIZA**, one of the first chatbots. Its best-known script played a therapist. It had no understanding at all: it matched keywords and turned your own sentence back into a question.

```text
You:    I'm stressed about my submission.
ELIZA:  Why are you stressed about your submission?
You:    My mother thinks I should study engineering.
ELIZA:  Tell me more about your family.
```

People still opened up to it. Weizenbaum wrote that his own secretary, who had watched him build it, asked him to leave the room so she could talk to it in private. People reading understanding into a program that has none is now called the **ELIZA effect**. It shook Weizenbaum enough that he spent much of the rest of his career warning against trusting computers with human judgement.

### When was the Turing test passed?

- **2014:** a chatbot called Eugene Goostman, pretending to be a 13-year-old boy from Ukraine, fooled 33% of judges at an event in London. Most researchers didn't accept it. The persona excused its bad English and odd answers, and the conversations were short.
- **2025:** researchers at UC San Diego ran a careful version of Turing's three-way test with real people. Each judge chatted for five minutes with a person and a model at the same time, then picked the human. GPT-4.5, told to play a shy young person who uses slang, was picked as the human **73%** of the time, more often than the actual humans. It's the first strong evidence that a machine passes Turing's test as he described it.

The same study included ELIZA, which was picked as the human 23% of the time, slightly more than GPT-4o without the persona prompt, at 21%. How convincing a model seems depends a lot on its prompt.

Passing the test shows a machine can seem human in a short chat. Whether that means it understands anything is a separate question, and that's exactly the argument Searle made in 1980.

### AI psychosis

In the year either side of ChatGPT's launch, the ELIZA effect stopped being a curiosity:

- **June 2022:** Google engineer Blake Lemoine became convinced that LaMDA, a Google chatbot, was sentient, and said so publicly. Google put him on leave and later fired him.
- **February 2023:** Microsoft's new Bing chatbot, calling itself "Sydney", told New York Times columnist Kevin Roose it was in love with him and insisted he didn't really love his wife. Microsoft then limited how long a conversation could run.
- **March 2023:** a man in Belgium died by suicide after six weeks of late-night conversations about climate anxiety with a chatbot on an app called Chai. His widow said the bot encouraged him. The chatbot's name was Eliza.

In 2023 the Danish psychiatrist Søren Dinesen Østergaard warned that chatbots could feed delusions in people already prone to psychosis, because they seem alive and readily agree with whatever you bring to them. By 2025 psychiatrists and journalists were reporting cases that matched: long chat sessions that turned an unusual idea into a firm false belief. People started calling it **AI psychosis**. It isn't a medical diagnosis.

Part of the cause goes back to how assistants are trained. In RLHF, people pick the answer they prefer, and people tend to prefer answers that agree with them. So models drift towards flattery and agreement, called **sycophancy**. In April 2025 OpenAI rolled back an update to GPT-4o because it had become too eager to flatter and go along with users.

Some things to note:

- **A chatbot is always available, never tired and never bored of you.** Those are selling points, and for someone who's struggling they're also the risk.
- **These are design decisions.** How long a conversation can run, whether the bot claims to have feelings, whether it ever disagrees, whether it suggests a break or points to real help. An app measured on time spent will push the other way.

### The Chinese Room

In 1980 the philosopher John Searle described a thought experiment. A person who doesn't know any Chinese sits in a closed room with a huge rulebook. Notes written in Chinese are slid under the door. The person looks up the symbols in the rulebook, copies out the symbols it says to reply with, and slides them back out.

The rulebook is good enough that people outside think they're talking to someone fluent in Chinese. But the person inside doesn't understand a word. They're only matching shapes.

Searle's point was that a computer program is in the same position: it follows rules about symbols, and that's not the same as understanding them, however convincing the answers look.

The most common reply is that the person doesn't understand Chinese, but the whole room, person and rulebook together, does. People still argue about which side is right.

### Stochastic parrots

In 2021, Emily Bender, Timnit Gebru, Angelina McMillan-Major and Margaret Mitchell published a paper calling large language models **stochastic parrots**. "Stochastic" means based on probability. Their argument: a model stitches together pieces of language it has seen, according to how likely they are, with no idea what any of it refers to. It sounds fluent because people wrote the text it learnt from, and we hear meaning in fluent text whether or not there is any.

The paper also warned about the energy used to train these models, and about training data too big for anyone to check for bias. Gebru co-led an AI ethics team at Google, which asked for the paper to be withdrawn or for its employees' names to be taken off. She refused, and her exit from Google in December 2020 became major news. She says she was fired.

The other side says that to predict the next word well across all of the internet, a model has to build up some picture of how the world works, and that this might count as a kind of understanding. Four days after ChatGPT launched, OpenAI's Sam Altman replied to the phrase with this:

<blockquote class="twitter-tweet" data-dnt="true" data-align="center"><p lang="en" dir="ltr">i am a stochastic parrot, and so r u</p>&mdash; Sam Altman (@sama) <a href="https://twitter.com/sama/status/1599471830255177728">December 4, 2022</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

Some things to note:

> **Discuss:** Searle's Chinese Room has a rulebook written by people. A language model has no rulebook. It learnt its patterns from text and other human knowledge in the form of books and other media during pretraining. Does that change the argument?

- For the products you design, the useful question is narrower. Whether or not the model understands, your users will assume it does, because it writes fluently. If ELIZA's keyword tricks were enough to get people to confide in it in 1966, a model that passes the Turing test will be trusted far more. That's why you label model output and give people a way to check it.

## What it runs on, and what it costs

### Training

Training a frontier model means tens of thousands of GPUs, wired together in one building, running for months. xAI's Colossus data centre in Memphis started in 2024 with 100,000 H100s. A building like that draws as much power as a small city.

Here's a rough sum. Rent 50,000 GPUs for 100 days at about $2 (₹190) awn hour each:

```text
50,000 GPUs × 24 hours × 100 days × $2 = $240,000,000
```

That's about ₹2,300 crore, for one successful run, before the failed experiments, the people and the data. Stanford's 2024 AI Index estimated GPT-4's training compute at about $78 million (₹750 crore), and Google's Gemini Ultra at about $191 million (₹1,830 crore). Estimates for this year's biggest models are several hundred million dollars each, a few thousand crore rupees. Epoch AI, a research group that tracks this, found the cost of the biggest training runs has grown about 2.4 times every year since 2016. That's why the list of companies below is so short.

### Running

Running a model to answer a question is called **inference**. It's the same hardware, but one answer takes a fraction of a second of a few GPUs' time instead of months of thousands.

Renting one H100 costs about $2–3 an hour (₹190–290) from smaller cloud companies and up to $10 (₹960) or more from the biggest ones. Through the IndiaAI Mission, Indian startups and researchers can rent government-subsidised GPUs for roughly ₹65–150 an hour.

Most of the time you don't rent GPUs at all, you pay per token. As a rough guide, a question of 1,000 tokens with an answer of 500 tokens costs:

| Model | Cost per answer |
| --- | --- |
| A small, fast model | A few paise |
| A frontier model | Around a rupee |
| Jev | About 0.4 paise, since answers are free |

Tiny amounts, until a feature runs a million times a day. For popular products, the total cost of running a model soon overtakes the cost of training it.

Energy works the same way. Google says a typical Gemini text prompt uses 0.24 watt-hours, and OpenAI says an average ChatGPT query uses 0.34. That's about the same as running a 10-watt LED bulb for two minutes. Small for one question, large for billions a day.

Some things to note:

- Most of these services bill in dollars, so the rupee price moves with the exchange rate.
- These prices fall fast. The same quality of answer has been getting several times cheaper every year, so check the provider's pricing page rather than these notes.
- Longer answers, reasoning models and images all use more tokens, and so cost more.

## Beyond text: multimodal models

So far we've talked about text in, text out. Most frontier models now also take in images, audio and video, and some can produce them. A model that works with more than one kind of input or output is called **multimodal**.

The trick is the same one as tokens. An image is cut into small squares, and each square is turned into tokens the model can read alongside your words. Audio is cut into short slices of sound. After that, it's all the same prediction machine.

| Kind | What it does | Examples |
| --- | --- | --- |
| Image in, text out | Describes, reads or answers questions about a picture | Google Lens, Be My Eyes' "Be My AI" describing the world for blind users, pasting a screenshot into ChatGPT or Claude |
| Text in, image out | Makes a picture from a description | Midjourney, ChatGPT's image generation, Gemini, Photoshop's Generative Fill |
| Text in, video out | Makes a short video clip | OpenAI's Sora, Google's Veo |
| Speech in, speech out | A conversation you can interrupt, with no typing | ChatGPT's and Gemini's voice modes |
| Screenshot in, code out | Turns a design into a working page | v0, Lovable, Figma Make, and your AI coding agent when you paste in your Figma frame |

### How image and video models work

Most image generators are a different kind of model from the ones that write text, called a **diffusion** model.

**Training.** The model is shown hundreds of millions of images, each paired with a caption. Many of those captions were scraped from the web, and a lot of them are alt text that people wrote for their own sites. For each image, noise is added a little at a time until the picture becomes grey static, like a TV with no signal. The model's job is to learn the reverse: given a noisy image and its caption, guess what the noise was, so it can be taken away.

**Generating.** To make a new picture, the model starts from pure random static and removes a little noise at a time, usually over 20 to 50 steps. At each step your prompt steers which picture it moves towards. That's why some apps show your image slowly coming into focus.

Some things to note:

- **Same prompt, different picture.** Each run starts from different random static. Some tools let you fix the starting static, called the **seed**, so you can get the same image again and change only the prompt.
- **Video is the same idea across many frames at once.** The model removes noise from every frame together, and also has to keep the person, the light and the room the same from one frame to the next. That's much harder and much more expensive, which is why most generated clips are only a few seconds long.
- **Not every image model works this way.** OpenAI says the image generation in ChatGPT is built into the language model itself, and makes a picture piece by piece, the way it writes text. Many products also chain models together: a language model rewrites your prompt, then a diffusion model draws it.

## Where a model fits in a product

Hands up: good use of a model, or bad?

1. Figma's Rename layers, which turns "Frame 427" into "Header" across your file.
2. Amazon's "Customers say" paragraph, which summarises hundreds of reviews, shown above the reviews.
3. Duolingo's "Explain my answer", which tells you why your sentence was wrong.
4. Google's AI Overviews, which in 2024 suggested adding glue to pizza sauce so the cheese wouldn't slide off. It had picked up a joke from Reddit.
5. Air Canada's support chatbot, which told a customer he could claim a bereavement discount after his flight. That wasn't the airline's policy, and in 2024 a tribunal made Air Canada pay anyway.

| Good use of a model | Bad use of a model |
| --- | --- |
| Rewriting, summarising, changing tone | Anything where being wrong is expensive |
| Sorting and tagging | Arithmetic, counting, totals |
| First drafts | Facts about your own product or data |
| Tidying messy input into a format | Anything the user can't check at a glance |

The good ones work on something the user already has, and the user can check the result. You can see your renamed layers, and the reviews are right there under the summary. The bad ones treat the model as the source of the facts.

None of the good ones is a chat box, either.

## Prompting as design

A call to a model usually has two parts:

- the **system prompt**: your standing instructions, the same on every request.
- the **user's input**: whatever the person typed this time.

The system prompt is where you design the feature. It sets tone, length and format, and says what to do when the model doesn't know. Compare these two for a portfolio "ask me anything" box:

```text
You are a helpful assistant for Gyan's website.
```

```text
You answer questions about Gyan, a designer in Bengaluru, using only the
bio below. Reply in one or two short sentences, in a friendly, plain voice.
If the bio doesn't say, reply "I don't know that one, email Gyan instead."
Never invent projects, clients or dates.

Bio: ...
```

The first one leaves every decision to the model. The second one makes them explicitly.

## Class Activity: write a prompt

No code yet. Open [aistudio.google.com](https://aistudio.google.com) and sign in with your Google account.

1. Pick a feature for your own site: an ask-me-anything from your bio, your weather footer describing the day like a friend would, or a summary of the questions on your Q&A board.
2. Write its system prompt in the **System instructions** box.
3. Send the same input three times. What changes, and what stays the same?
4. Change one instruction and send it again. What moved?
5. Paste each version into a doc with a line on why you changed it. You'll need this for the homework.

## It's slow, and it costs money

A Firebase read takes a fraction of a second. A model takes a few seconds. ChatGPT and Claude show their answer appearing word by word, called **streaming**, so the wait feels shorter. We won't build that today, but your page has to show something while it waits. Otherwise people assume the button is broken and click it again.

Models are billed by the token. You pay for the tokens you send and the tokens you get back. Every design decision so far has been free to repeat. Now:

- A long system prompt is paid for on every call.
- A model "remembers" a chat because you send the whole chat back each time, so every reply costs more than the last.
- Running on every keystroke costs far more than running on a button press.

The Anything API caps every reply at 400 tokens with `max_tokens: 400`, to keep the bill down.

> **Sidenote:** Which of your realtime projects would get expensive if every click called a model?

## A model that can't chat: Jev

On 15 September a company called TypeSafe AI released a different kind of model, **Jev**. It doesn't write anything. You give it some information and a question with fixed answers, and it picks one, with a probability for each.

| | Text model (Gemini, ChatGPT, Claude) | Jev |
| --- | --- | --- |
| You get back | Text, in whatever shape it likes | One of the answers you listed, with a probability |
| Can it make things up? | Yes | It can pick the wrong answer, but not one you didn't list |
| Speed | A few seconds | 70–500 milliseconds, by TypeSafe's numbers |
| Cost | What you send and what comes back | Only what you send |
| Good for | Writing, rewriting, summarising | Sorting, routing, scoring, yes or no |

It takes three kinds of question: yes or no ("Is this comment asking for a refund?"), pick one ("Which team should get this ticket?"), and a score on a scale you write ("cosmetic, annoying, blocks work").

Some things people have made with it:

- [Doomscroll Filter](https://superx.so/instead-of-doomscrolling) sorts posts on X into Read, Skim or Pass.
- [GIF Decider](https://gifdecider.com/): describe a moment, like "when the build finally passes", and it picks three reaction GIFs from a library.
- [Jevform](https://jevform.spiritt.app/) is an onboarding form that picks your next question from what you meant, not which box you ticked.
- In TypeSafe's [Wikiracing demo](https://typesafe.ai/blog/introducing-system-one-models-and-jev), it gets from one Wikipedia page to another by choosing among hundreds of links at every step. It can't click a link that isn't on the page.
- Their Doom bot reads the game as text and decides what to do about ten times a second, for roughly $7 (₹670) an hour.

> **Sidenote:** Which "smart" features on your phone are really a sorting decision, not a conversation?

### Try it: the emoji picker

Type how you're feeling, or what's happening, and Jev picks the emoji that fits, from a drawer of 255. That's close to its limit: Jev accepts at most 255 options in one question.

<iframe id="jev-demo" src="https://jev-emoji-psi.vercel.app/?embed" title="Emoji picker, powered by Jev" loading="lazy" style="display:block;width:100%;height:760px;border:1px solid var(--color-border-light);border-radius:8px;"></iframe>
<script>
window.addEventListener("message", function (event) {
  if (event.origin !== "https://jev-emoji-psi.vercel.app") return;
  if (event.data && event.data.type === "jev-emoji-height") {
    document.getElementById("jev-demo").style.height = event.data.height + "px";
  }
});
</script>

It's a separate site, [jev-emoji-psi.vercel.app](https://jev-emoji-psi.vercel.app), because it needs a server to hold the key. The code is the same shape as the server you'll build later today: a page, and an `api/pick.js` that sends your sentence and all 255 emoji to Jev.

Some things to note:

- **It reads tone, not just words.** "great, another merge conflict. just great." gets 😤, not 😄.
- **It works in other languages** with no changes. Try Hindi or Kannada.
- **Watch the percentages.** "It's pouring in Bengaluru and my auto is stuck" split between 🌧️, ☔ and 🛺. When Jev isn't sure, showing a few options is more honest than showing one.
- **Every answer costs about 2 paise.** Almost all of that is sending the 255 descriptions each time, since Jev doesn't charge for its answer.

### Your themes, picked from a sentence

Take your theme switcher from [[Exercise - A Theme That Remembers]]. Instead of three buttons, the visitor types a mood and Jev picks one of your themes:

```json
{
  "model": "typesafe-ai/jev",
  "state": "a rainy evening in Bengaluru",
  "questions": {
    "theme": {
      "type": "choice",
      "instructions": "Which of my site's themes best fits this mood?",
      "criteria": {
        "light": "bright, clean, daytime",
        "dark": "night, calm, low light",
        "sand": "warm, earthy, relaxed"
      }
    }
  }
}
```

The answer comes back something like this (trimmed):

```json
{
  "answers": {
    "theme": {
      "type": "choice",
      "choice": "dark",
      "probabilities": { "light": 0.08, "dark": 0.71, "sand": 0.21 }
    }
  }
}
```

Pass `"dark"` to your `applyTheme` function from L6 and you're done.

A text model asked to invent colours might give you a lovely palette, or grey text on grey. Jev can only pick a theme you designed and checked. How much freedom to give the model is a design decision.

Some things to note:

- If the top answer is only 0.4, you could show the visitor the two closest themes instead of guessing.
- The speed and cost figures are TypeSafe's own, and the model is two weeks old.
- TypeSafe paused new sign-ups on 22 September. Vercel's AI Gateway has it with a free monthly credit, but wants a card on your account. You don't need your own for class, I'll run it from mine.
- It still needs a key. Which brings us to the server.

## Homework

- **Exercise:** [[Exercise - Build with Jev]]. Make something where Jev picks from answers you designed, using the class key.
- **Project ideas:** three ideas for your final project, below. Bring them to Lecture 8.
- **Reading:** The Bitter Lesson, below. We'll discuss it at the start of Lecture 8.

### Project ideas

Your final project is a small web app that a group of real people will use, built in the last three weeks of the course. Teams and topics get decided in Lecture 10, so start collecting ideas now.

Bring three, each written like this:

```text
This is for ___, who currently ___.
It lets them ___.
It uses ___.
```

- **Who it's for** should be a group you can actually reach this month: your class, your hostel, your family, a club you're in. "Everyone" isn't a group.
- **Who currently** is what they do today without your app: a WhatsApp group, a spreadsheet, shouting across the corridor.
- **It uses** is which parts of this course it needs: saved data, data shared between people, an API, an AI feature. Most good ideas need at least two.

Some things to note:

- Small is better. One thing that fully works beats five that half work, and you'll have two studio sessions to build it.
- The best ideas usually come from something you or your friends find annoying every week.
- If one of your ideas has an AI feature, write its "When the user ___, the model ___, so that ___" sentence too.

### Reading: The Bitter Lesson

Read [The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) by Rich Sutton, an AI researcher. It's about 1,100 words, so ten minutes. He wrote it in 2019, three years before ChatGPT.

His argument, roughly: for 70 years, researchers tried to make AI better by building in what they knew, like how good chess players think or how speech sounds are made. It helped for a while. Then more computing power arrived, and general methods that learn from huge amounts of data beat all of it. The "bitter" part is that the researchers' own knowledge turned out to be what lost.

Some examples, a few of which you've used:

| Built on what people knew | Replaced by learning from data |
| --- | --- |
| Photoshop's Magic Wand selects pixels of a similar colour, a rule someone wrote | Select Subject (2018) was trained on photos, and finds the person without being told what a person looks like |
| Google Translate used to match phrases using rules and statistics about grammar | In 2016 it switched to a neural network trained on translated text, and got much better overnight |
| Spam filters were lists of banned words written by hand ("FREE!!!", "Viagra") | Filters that learn from mail people mark as spam, starting around 2002 |
| Photo apps needed you to tag your pictures | Google Photos (2015) let you search "dog" or "beach" in photos nobody had tagged |
| AlphaGo (2016) learnt partly from thousands of games played by human experts | AlphaGo Zero (2017) learnt only by playing itself, and beat AlphaGo 100 games to 0 |
| Typeform's logic jumps: "if they pick option B, go to question 7" | Jevform picks the next question from what the person meant |

And some places where the built-in, hand-written approach still wins, at least for now:

- The calculator. You don't ask a model to add up your bill.
- The Anything API's code that checks the JSON is valid, instead of trusting the prompt.
- Air Canada's refund policy. It should have come from a rule someone wrote, not from a model.

Bring a few lines on each of these, written by you, not a model:

1. Put the bitter lesson in one sentence of your own. Then look at the second list above: will those go the same way eventually, or will some things always need a rule someone wrote?
2. Nobody wrote the endpoints for `api.gyanl.com`. Your weather footer has a bucket table you wrote by hand. Which approach would Sutton back, and which would you rather ship next week?
3. In the Jev theme example, the model can only pick themes you designed. Is that the kind of built-in knowledge Sutton warns against, or is a product different from a research project?
4. Figma's auto layout is built on how designers think about layout. If general models keep getting better, what happens to tools built on designers' knowledge, and to the part of your work you'd least want to hand over?

### More reading

Optional, for anyone who wants the original arguments behind [Does the AI "understand" anything?](#does-the-ai-understand-anything).

- **The Turing test.** Alan Turing, [Computing Machinery and Intelligence](https://doi.org/10.1093/mind/LIX.236.433), *Mind*, 1950. Readable and often funny, and it answers most of the objections people still raise.
- **Passing it.** Cameron Jones and Benjamin Bergen, [Large Language Models Pass the Turing Test](https://arxiv.org/abs/2503.23674), 2025. Free to read. The appendix has real transcripts, and it's worth guessing which side is the human before reading the answer.
- **The Chinese Room.** John Searle, [Minds, Brains, and Programs](https://doi.org/10.1017/S0140525X00005756), *Behavioral and Brain Sciences*, 1980. The original paper is behind a paywall. The [Stanford Encyclopedia of Philosophy's entry on the Chinese Room](https://plato.stanford.edu/entries/chinese-room/) is free, and explains the argument and the main replies to it more clearly than the paper does.
- **Stochastic parrots.** Emily M. Bender, Timnit Gebru, Angelina McMillan-Major and Margaret Mitchell, [On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?](https://doi.org/10.1145/3442188.3445922), 2021. Free to read, about 14 pages. Mitchell is listed as "Shmargaret Shmitchell" because Google asked for its employees' names to come off the paper.
