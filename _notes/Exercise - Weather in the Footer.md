---
date: 01-09-2026
date modified: 01-09-2026
feed: show
tag: exercise
title: "Exercise - Weather in the Footer"
---

### Put live weather in the footer of your own site

A small strip at the bottom of your page that knows what the sky is doing. Real data, from [Open-Meteo](https://open-meteo.com/), on the site you already shipped in [[Exercise - Ship a Page with GitHub Pages]].

It's a deliberately small piece of work. The API call is three lines and you'll have AI write them. The exercise is everything around those three lines: deciding what the widget says, what it looks like while it's waiting, and what it does when the internet doesn't answer.

### Steps

1. **Find your coordinates.** Search "Bengaluru latitude longitude", or right-click a spot in Google Maps. Two numbers, four decimal places is plenty.
2. **Build the URL by hand and open it in a browser tab.** No code yet. Start from the one in [[Lecture 5 - APIs]] and swap in your numbers:
   ```text
   https://api.open-meteo.com/v1/forecast?latitude=12.97&longitude=77.59&current=temperature_2m,weather_code,is_day&timezone=auto
   ```

   Read the JSON that comes back. Find the three values you asked for. `timezone=auto` means it works out the timezone from the coordinates, and `is_day` comes back as `1` or `0` — you'll want that later.

3. **Answer the questions below** — on paper, before you open your editor. This is the actual assignment.
4. **Decide your buckets.** Open-Meteo describes the sky with a [WMO code](https://open-meteo.com/en/docs) — 28 of them, from `0` (clear) to `99` (thunderstorm with heavy hail). You almost certainly don't want 28 icons. Group them into as few as you can live with, and write your table down before you build:

   | Codes | Means | You might call it |
   | --- | --- | --- |
   | 0, 1 | Clear, mainly clear | ☀️ |
   | 2, 3 | Partly cloudy, overcast | ⛅ |
   | 45, 48 | Fog | 🌫️ |
   | 51–57 | Drizzle | 🌦️ |
   | 61–67, 80–82 | Rain and rain showers | 🌧️ |
   | 71–77, 85, 86 | Snow | ❄️ |
   | 95–99 | Thunderstorm | ⛈️ |

   Six or seven buckets is a reasonable answer. Three is a defensible one. One — text only, no icon — is also a design decision, if you can argue for it.

5. **Have AI build it.** Give it: the exact URL, your bucket table, and how your site is already written (your class names, your CSS variables, your type scale). Ask for plain HTML/CSS/JS, no libraries. Then read what it gives you and find the `fetch`, the `.json()`, and the line that puts the value on the page.

6. **Design the three states it will actually be in.** Loading, loaded, failed. Test the failed one properly: change the URL to nonsense and reload. If your footer shows `undefined°` or `NaN`, that's a real bug your visitors will see, not a hypothetical.

7. **Ship it** and credit Open-Meteo in the footer — a small link is enough. Their licence asks for it, and reading a licence before you build on something is the habit here.

### Questions to answer first

Bring your written answers — we'll compare them, and they'll be more interesting than the code.

- **Whose weather is it?** Yours, fixed to your city, or the visitor's, from their location? Your city is a fact about you and works for everyone. Their weather needs a permission prompt and a fallback for when they say no. Which one is your site actually about?
- **Why is this in your footer at all?** What does it say about you that "© 2026" doesn't? If you can't answer this, that's a finding — you can still build it, but say so.
- **What's the smallest version that still feels alive?** Is it a number and an icon, or could it be one sentence — *"It's 27° and overcast in Bengaluru"* — set in your body typeface?
- **`26.7`, `27`, or "warm"?** Every extra decimal is a claim to precision. What level of precision does a portfolio footer have any business making?
- **What does it look like before the data arrives?** Blank space that shifts your layout when it fills? A dash? A skeleton? This is the state most students never design, and on a slow connection it's the state visitors see for longest.
- **What if it never arrives?** Hide the widget entirely, show the last thing you knew, or say something honest? There is no correct answer, but "show `undefined`" is the wrong one.
- **What happens at night?** Most icon sets assume daylight. A sun over a footer at 2am is a small lie — `is_day` tells you which it is.
- **Who decides °C or °F?** You, from where you are, or them, from where they are?
- **How often should it update?** Once when the page loads is probably right. If you're tempted by a timer, work out how many calls that is against their 10,000-a-day limit if your site gets shared.

### Icon sets

You need very few icons, so pick for fit, not for size of library. All of these are free to use — check each licence yourself, that's part of the exercise.

| Set | Style | Licence | Good for |
| --- | --- | --- | --- |
| [Meteocons](https://basmilius.github.io/meteocons/) | Purpose-built weather, line + filled + animated SVG | MIT | The obvious first stop — it has exactly the icons you need and the animated ones are lovely in a footer |
| [Weather Icons](https://erikflowers.github.io/weather-icons/) | 215 weather glyphs as a font | SIL OFL 1.1 (font), MIT (code) | Sets that already map to weather-service codes; useful if you want fine distinctions |
| [Lucide](https://lucide.dev/) | Minimal line icons, general purpose | ISC | Sites already using a clean line style — the weather icons match everything else |
| [Phosphor](https://phosphoricons.com/) | General purpose, six weights | MIT | Matching an existing type weight — pick Thin next to a light typeface |
| [Tabler](https://tabler.io/icons) | Minimal line icons, very large set | MIT | Same as Lucide; pick whichever grid suits your site |
| Emoji | Whatever the visitor's OS decides | None needed | Zero files, zero requests, works everywhere — and it looks different on every device, which you may love or hate |

Two things worth knowing before you pick:

- **No icon set maps to WMO codes for you.** You are writing that mapping either way. Choosing a set with 200 icons doesn't save you work; it just gives you more ways to be indecisive.
- **Emoji is a real answer, not a lazy one.** It costs nothing, it never fails to load, and it renders in the visitor's own system font. It's also completely outside your control typographically. Decide on purpose.

### Things to keep in mind

- **No API key here** — nothing to leak, which is why we're starting with this one. Later APIs won't be so relaxed; that's [[Exercise - Add an AI Feature]]'s problem.
- **Your footer loads on every page.** Whatever this widget does badly, it does badly site-wide.
- **A layout that jumps when the data lands is worse than no widget.** Reserve the space.

### Submission

- Live URL, with the widget in the footer.
- Your written answers to the questions above, and your bucket table.
- Screenshots of all three states: loading, loaded, and failed. Force the failure — don't wait for it.
- One sentence: what did you decide *not* to show, and why?
