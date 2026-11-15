/* Dr. Wanjiru MD — site behaviour (no dependencies) */
(function () {
  'use strict';
  // Set these when known. Leave empty to keep the contact form in demo mode.
  var CLINIC = { whatsapp: '', email: '' }; // e.g. whatsapp: '2547XXXXXXXX'

  var doc = document.documentElement;
  doc.classList.remove('no-js');
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ----- header, menu, progress, to-top -----
  var header = $('#site-header'), list = $('#nav-list'), btn = $('#menu-btn');
  var bar = document.createElement('div'); bar.className = 'progress'; document.body.appendChild(bar);
  var top = document.createElement('button'); top.className = 'to-top'; top.setAttribute('aria-label', 'Back to top'); top.textContent = '↑';
  top.onclick = function () { window.scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' }); }; document.body.appendChild(top);
  function onScroll() {
    var y = window.scrollY, h = doc.scrollHeight - doc.clientHeight;
    if (header) header.classList.toggle('scrolled', y > 40);
    bar.style.width = (h > 0 ? (y / h) * 100 : 0) + '%';
    top.classList.toggle('show', y > 900);
  }
  onScroll(); window.addEventListener('scroll', onScroll, { passive: true });
  if (btn && list) {
    btn.addEventListener('click', function () {
      var open = list.classList.toggle('open'); btn.classList.toggle('open', open); btn.setAttribute('aria-expanded', open);
      document.body.style.overflow = open ? 'hidden' : '';
    });
    $$('a', list).forEach(function (a) { a.addEventListener('click', function () { list.classList.remove('open'); btn.classList.remove('open'); document.body.style.overflow = ''; }); });
  }

  // ----- reveal on scroll -----
  var revs = $$('.reveal');
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }); }, { threshold: .12, rootMargin: '0px 0px -40px 0px' });
    revs.forEach(function (el) { io.observe(el); });
  } else { revs.forEach(function (el) { el.classList.add('in'); }); }

  // ----- count-up -----
  var counters = $$('[data-count]');
  if (counters.length && 'IntersectionObserver' in window) {
    var cio = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return; cio.unobserve(e.target);
        var el = e.target, end = parseFloat(el.dataset.count), pre = el.dataset.prefix || '', suf = el.dataset.suffix || '', t0 = performance.now();
        (function tick(t) { var p = Math.min((t - t0) / 1500, 1), v = Math.round(end * (1 - Math.pow(1 - p, 3))); el.textContent = pre + v + suf; if (p < 1) requestAnimationFrame(tick); })(t0);
      });
    }, { threshold: .6 });
    counters.forEach(function (c) { cio.observe(c); });
  }

  // ----- tabs (also toggles [data-for] elements, e.g. diagrams) -----
  $$('[data-tabs]').forEach(function (root) {
    var tabs = $$('[role="tab"]', root), panels = $$('[role="tabpanel"]', root);
    function activate(id, focus) {
      tabs.forEach(function (t) { var on = t.dataset.tab === id; t.setAttribute('aria-selected', on); t.tabIndex = on ? 0 : -1; if (on && focus) t.focus(); });
      panels.forEach(function (p) { p.hidden = p.dataset.panel !== id; });
      $$('[data-for]', root).forEach(function (el) { el.classList.toggle('on', el.dataset.for.split(' ').indexOf(id) > -1); });
    }
    tabs.forEach(function (t, i) {
      t.addEventListener('click', function () { activate(t.dataset.tab); });
      t.addEventListener('keydown', function (e) {
        var n = e.key === 'ArrowRight' ? i + 1 : e.key === 'ArrowLeft' ? i - 1 : null;
        if (n !== null) { e.preventDefault(); var x = tabs[(n + tabs.length) % tabs.length]; activate(x.dataset.tab, true); }
      });
    });
    if (tabs.length) activate(tabs[0].dataset.tab);
  });

  // ----- before / after sliders -----
  $$('[data-ba]').forEach(function (ba) {
    var wrap = $('.after-wrap', ba), handle = $('.handle', ba), pct = 50, drag = false;
    function set(p) { pct = Math.max(0, Math.min(100, p)); wrap.style.clipPath = 'inset(0 0 0 ' + pct + '%)'; handle.style.left = pct + '%'; ba.setAttribute('aria-valuenow', Math.round(pct)); }
    function fromX(x) { var r = ba.getBoundingClientRect(); set(((x - r.left) / r.width) * 100); }
    ba.addEventListener('pointerdown', function (e) { drag = true; ba.setPointerCapture(e.pointerId); fromX(e.clientX); });
    ba.addEventListener('pointermove', function (e) { if (drag) fromX(e.clientX); });
    ba.addEventListener('pointerup', function () { drag = false; }); ba.addEventListener('pointercancel', function () { drag = false; });
    ba.addEventListener('keydown', function (e) { if (e.key === 'ArrowLeft') set(pct - 5); if (e.key === 'ArrowRight') set(pct + 5); });
    set(50);
  });

  // ----- card glow follows cursor -----
  $$('.card').forEach(function (c) { c.addEventListener('pointermove', function (e) { var r = c.getBoundingClientRect(); c.style.setProperty('--mx', (e.clientX - r.left) + 'px'); c.style.setProperty('--my', (e.clientY - r.top) + 'px'); }); });

  // ----- hero collage parallax -----
  var col = $('.collage');
  if (col && !reduce && window.matchMedia('(pointer: fine)').matches) {
    var items = $$('.img', col);
    window.addEventListener('pointermove', function (e) {
      var x = (e.clientX / innerWidth - .5), y = (e.clientY / innerHeight - .5);
      items.forEach(function (el, i) { var d = (i + 1) * 9; el.style.transform = 'translate(' + (-x * d) + 'px,' + (-y * d) + 'px)'; });
    }, { passive: true });
  }

  // ----- table of contents highlighting -----
  var toc = $$('.toc a');
  if (toc.length && 'IntersectionObserver' in window) {
    var map = {}; toc.forEach(function (a) { map[a.getAttribute('href').slice(1)] = a; });
    var tio = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { toc.forEach(function (a) { a.classList.remove('on'); }); var a = map[e.target.id]; if (a) a.classList.add('on'); } }); }, { rootMargin: '-20% 0px -70% 0px' });
    Object.keys(map).forEach(function (id) { var el = document.getElementById(id); if (el) tio.observe(el); });
  }

  // ----- FAQ search + category filter -----
  var fs = $('#faq-search');
  if (fs) {
    var items = $$('.faq details'), cat = 'all', chips = $$('.chip');
    function filter() { var q = fs.value.trim().toLowerCase(); items.forEach(function (d) { var ok = (cat === 'all' || d.dataset.cat === cat) && (!q || d.textContent.toLowerCase().indexOf(q) > -1); d.hidden = !ok; }); }
    fs.addEventListener('input', filter);
    chips.forEach(function (c) { c.addEventListener('click', function () { cat = c.dataset.cat; chips.forEach(function (x) { x.setAttribute('aria-pressed', x === c); }); filter(); }); });
  }

  // ----- contact form -----
  var form = $('form.contact');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var f = new FormData(form), note = $('.form-note', form);
      var msg = 'Hello Dr. Wanjiru, I am ' + f.get('name') + '. Interested in: ' + f.get('topic') + '. ' + (f.get('msg') || '') + ' (Phone: ' + f.get('phone') + ')';
      if (CLINIC.whatsapp) { window.open('https://wa.me/' + CLINIC.whatsapp + '?text=' + encodeURIComponent(msg), '_blank', 'noopener'); note.textContent = 'Opening WhatsApp…'; }
      else if (CLINIC.email) { location.href = 'mailto:' + CLINIC.email + '?subject=Consultation%20request&body=' + encodeURIComponent(msg); }
      else { note.textContent = 'Thank you. This is a demo form: add the clinic WhatsApp number or email at the top of main.js to go live.'; }
      form.reset();
    });
  }
})();
