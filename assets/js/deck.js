// Tech 1 — Present mode: turn a note's #### sections into full-screen slides.
document.addEventListener("DOMContentLoaded", function () {
  var content = document.querySelector(".note-page-section .content");
  if (!content) return;
  var headings = content.querySelectorAll("h4");
  if (headings.length < 2) return; // nothing deck-worthy

  var btn = document.createElement("button");
  btn.id = "present-toggle";
  btn.textContent = "▶ Present";
  btn.setAttribute("aria-label", "Toggle presentation mode");
  document.querySelector(".note-page-section").prepend(btn);

  var built = false;

  function buildSlides() {
    var deck = document.createElement("div");
    deck.id = "deck";

    // Title slide from the page h1 + anything before the first h4
    var slide = document.createElement("section");
    slide.className = "slide slide-title";
    var h1 = document.querySelector(".note-page-section h1");
    if (h1) slide.appendChild(h1.cloneNode(true));

    var nodes = Array.prototype.slice.call(content.childNodes);
    nodes.forEach(function (node) {
      if (node.nodeType === 1 && node.tagName === "H4") {
        deck.appendChild(slide);
        slide = document.createElement("section");
        slide.className = "slide";
      }
      slide.appendChild(node.cloneNode(true));
    });
    deck.appendChild(slide);

    // Slide counters
    var slides = deck.querySelectorAll(".slide");
    slides.forEach(function (s, i) {
      var n = document.createElement("div");
      n.className = "slide-number";
      n.textContent = (i + 1) + " / " + slides.length;
      s.appendChild(n);
    });

    document.body.appendChild(deck);
    built = true;
  }

  function enter() {
    if (!built) buildSlides();
    document.body.classList.add("deck-mode");
    btn.textContent = "✕ Exit";
    var d = document.getElementById("deck");
    d.scrollTop = 0;
    d.focus();
  }

  function exit() {
    document.body.classList.remove("deck-mode");
    btn.textContent = "▶ Present";
  }

  btn.addEventListener("click", function () {
    document.body.classList.contains("deck-mode") ? exit() : enter();
  });

  document.addEventListener("keydown", function (e) {
    if (!document.body.classList.contains("deck-mode")) return;
    var deck = document.getElementById("deck");
    var h = window.innerHeight;
    if (e.key === "Escape") exit();
    if (e.key === "ArrowDown" || e.key === "ArrowRight" || e.key === " " || e.key === "PageDown") {
      e.preventDefault();
      deck.scrollBy({ top: h, behavior: "smooth" });
    }
    if (e.key === "ArrowUp" || e.key === "ArrowLeft" || e.key === "PageUp") {
      e.preventDefault();
      deck.scrollBy({ top: -h, behavior: "smooth" });
    }
  });
});
