---
date: 09-10-2026
date modified: 09-10-2026
feed: show
key_areas:
  - "Authentication"
  - "Authorisation"
  - "Identity providers"
tag: lecture
title: "Lecture 8 - Authentication & Authorisation"
---

## Homework

- [[Exercise - Unusual Interactions]]
- [[Exercise - Realtime Web Experience]]
- [[Exercise - Build with Jev]]

Any thoughts for final projects?

---

## Who are you?

- How can you prove that you are you?

---

## Proving Identity Offline

- How do you prove who you are at the airport, the bank, a new SIM shop? ID card, signature, Aadhaar fingerprint, your face against the photo.

---

- When we tried The Wall from L6, anyone could paint as anyone, because "join with your name" was just a name you typed.
- Rules can only check who someone is if the app knows who they are.
- Every product they use has this: Instagram, Gmail, Swiggy, Google Flights, IRCTC. What does each one let you do before you sign in?

### Two words: authentication and authorisation

- **Authentication**: proving who you are (signing in).
- **Authorisation**: what you're allowed to do once we know (the rules).
- Table: wall with no login vs wall with login. Who can paint, who can erase, what a stranger sees.

### How do you prove who you are?

- Online there are only three kinds of proof:

| Kind | Examples | How it fails |
| --- | --- | --- |
| Something you **know** | Password, PIN, UPI PIN, API Key, "mother's maiden name" | Guessed, reused, phished, written on a sticky note |
| Something you **have** | Your phone (SMS OTP, an authenticator app), a security key, your laptop | Lost, stolen, SIM swapped |
| Something you **are** | Face ID, fingerprint | Can't be changed if it leaks |

- **Two-factor** means two different kinds, not two passwords. Password plus OTP is two factors; password plus security question is still one.

- **Passkeys**: your phone or laptop proves it's you with Face ID or your fingerprint, and nothing is typed. No password to steal or reuse. Google, Apple and GitHub already offer them.

- Which of these does UPI use when you pay? Which does Instagram use? Why are they different?

### Trust

- No login actually proves *who* you are. It proves you have something that someone trusted earlier: the password you set, the phone number the telecom company gave you, the Google account Google let you make.
- So every login is a **chain of trust**. "Sign in with Google" means your app trusts Google, Google trusts your password and phone, and the phone OTP trusts Jio or Airtel. A SIM swap scam breaks the last link.
- **Trust should match the stakes.** The wall can trust a Google account. A bank asks again before every transfer. Zerodha and PhonePe need KYC with Aadhaar and PAN because the law needs a real person. More proof means more friction, and choosing how much is a design decision.
- **Identity isn't always a real name.** Reddit is pseudonymous and LinkedIn wants your real name. Which does your product need?
- **Trust goes the other way too.** Users have to trust your site before they type anything into it: the domain, HTTPS, a sign-in page that looks right. Phishing is a fake page that looks right. The blue tick on Instagram was a trust signal until anyone could buy one.
> **Sidenote:** Think of the last time an app asked you to prove who you are and it felt like too much. Was it?

### Don't store passwords yourself

- Passwords are the most dangerous data an app holds. Real apps never store the password itself - they instead "hash" the password and save the result.
- Use someone else's proof instead: Sign in with Google or Apple, a magic link by email, an OTP by SMS.
- Phone OTP is the norm in India (Swiggy, Zomato, PhonePe). Why? Who does that leave out?

### Sign in with Google, and other identity providers

- An **identity provider** is a company that vouches for you to other apps: Google, Apple, Microsoft, GitHub, Facebook. It's the chain of trust from the last section, as a button.
- What happens when you click it (do it live, watch the address bar):
  1. The app sends you to `accounts.google.com`. The app's page is gone, so the app never sees your Google password.
  2. Google checks it's you, the way it always does (password, phone, passkey).
  3. Google asks what to share with the app: name, email, photo (the first time, or if what the app is asking for has changed).
  4. Google sends you back with a signed note: "this is user 1234, their email is ___". The app trusts the note because it trusts Google.
- The standard behind this is called **OAuth**.

### Why do so many sites offer Login with Google/Apple?

- Why users pick it:
  - One tap, no new password to make up and forget.
  - Already signed in to Google on their phone.
  - Google's security (two-factor, "was this you?" alerts) now protects this account too.
- Why companies offer it:
  - More people finish signing up. Every form field loses some of them.
  - No passwords to store, no "forgot password" emails, a verified email for free.
  - Fewer fake accounts than a plain email form.
- What it costs:
  - If you lose your Google account, you lose every app you signed in to with it.
  - Google learns which apps you use.
  - The app depends on Google. If Google changes the rules or goes down, sign-in goes down.
- **Sign in with Apple** offers "Hide My Email": the app gets a made-up address that forwards to you. Apple pushes iOS apps that offer Google sign-in to also offer a privacy-focused option, which is why Apple's button keeps appearing. (More on app stores in L12.)

### Which type of login is a design decision

Depends on who your users are:

  - Indian consumer apps: phone OTP, and maybe Google.
  - Developer tools (Vercel, Figma plugins): GitHub.
  - Workplaces: Microsoft, or "Sign in with SSO", which is how Figma and Slack work at a company.
  - Six buttons is too many, and people forget which one they used last time. Some sites now label "Last used".

> **Sidenote:** Which identity providers have you used? Have you ever been stuck because you couldn't remember which one?

### How the site remembers you're signed in

- After you sign in, the browser keeps a **token**: a signed pass saying who you are, stored in the browser securely.
- Every request to the database or your server carries the token. That's how a rule knows "this is gyanl" without needing the password again constantly.

### Sign-in is a design decision

Ask these about your multiplayer experience once it has sign-in:

- When to ask: let people try first (Figma files you can view, Swiggy menus you can browse) vs a wall at the door.
- What can a signed-out visitor see? Read-only, a preview, or nothing?
- What you ask for: Google gives you name, email and photo. Do you need all three?
- Whose names and photos does everyone see? The Realtime exercise asked "what's private?", and Google just gave you everyone's face.
- Signing out, and deleting an account, need to exist and be findable.
- Does it need sign-in at all? Anonymous questions might be the whole point of a live Q&A. Your final project will need it, so this is practice for deciding what signed-in people get that visitors don't.

---
## Homework

- [[Exercise - Sign in with Google]]