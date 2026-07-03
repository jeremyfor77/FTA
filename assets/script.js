(function () {
  var root = document.documentElement;
  var stored = localStorage.getItem('fta-theme');
  if (stored) root.setAttribute('data-theme', stored);

  var btn = document.getElementById('themeToggle');
  function label() {
    var dark = root.getAttribute('data-theme') === 'dark' ||
      (!root.getAttribute('data-theme') && window.matchMedia('(prefers-color-scheme: dark)').matches);
    if (btn) {
      btn.textContent = dark ? 'Day Edition' : 'Night Edition';
      btn.setAttribute('aria-pressed', String(dark));
    }
  }
  label();
  if (btn) {
    btn.addEventListener('click', function () {
      var current = root.getAttribute('data-theme');
      var isDark = current === 'dark' ||
        (!current && window.matchMedia('(prefers-color-scheme: dark)').matches);
      var next = isDark ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      localStorage.setItem('fta-theme', next);
      label();
    });
  }

  var dateEl = document.getElementById('todayDate');
  if (dateEl) {
    var d = new Date();
    var months = ['January','February','March','April','May','June','July','August','September','October','November','December'];
    dateEl.textContent = d.getDate() + ' ' + months[d.getMonth()] + ' ' + d.getFullYear();
  }
})();
