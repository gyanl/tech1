// Tech 1 — list / board view switch for the notes feed.
(function () {
  var KEY = 'tech1-feed-view';

  function apply(view) {
    document.body.classList.toggle('view-board', view === 'board');
    document.querySelectorAll('.vs-btn').forEach(function (b) {
      b.classList.toggle('is-active', b.dataset.view === view);
    });
  }

  function init() {
    var saved = localStorage.getItem(KEY) || 'list';
    apply(saved);
    document.querySelectorAll('.vs-btn').forEach(function (b) {
      b.addEventListener('click', function () {
        var v = b.dataset.view;
        localStorage.setItem(KEY, v);
        apply(v);
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
