"""Shared template + components for the static site build."""
import json, html as _h, datetime, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import logos

SITE_URL = 'https://www.drwanjirumd.com'   # PLACEHOLDER: replace with the real domain before launch
SITE_NAME = 'Dr. Wanjiru MD'
TODAY = datetime.date(2026, 11, 6).isoformat()
MARK = logos.inline_mark()
FAQ = []          # collected per page
PAGES = []        # (path, priority, changefreq) for sitemap

def esc(s): return _h.escape(s, quote=True)

# ------------------------------------------------------------------ components
RATIOS = {'r45': (800, 1000), 'r169': (1200, 750), 'r11': (800, 800), 'r34': (900, 1200)}

def img(slot, alt, ratio='r45', cls='', eager=False, cap=''):
    w, h = RATIOS[ratio]
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    c = f'<figcaption>{cap}</figcaption>' if cap else ''
    return (f'<figure class="img {ratio} {cls}"><img src="images/{slot}.jpg" alt="{esc(alt)}" width="{w}" height="{h}" {load} decoding="async" '
            f'onerror="this.onerror=null;this.src=\'images/art/{slot}.svg\'">{c}</figure>')

def ba(slug, title, caption):
    a = lambda s, side: (f'<img src="images/{slug}-{side}.jpg" alt="{esc(title)} {side}" width="800" height="1000" loading="lazy" '
                         f'onerror="this.onerror=null;this.src=\'images/art/{slug}-{side}.svg\'">')
    return (f'<div class="reveal"><div class="ba" data-ba role="slider" tabindex="0" aria-label="Before and after: {esc(title)}" aria-valuemin="0" aria-valuemax="100" aria-valuenow="50">'
            f'{a(slug, "before")}<div class="after-wrap">{a(slug, "after")}</div><span class="lbl l">Before</span><span class="lbl r">After</span><div class="handle"></div></div>'
            f'<p class="ba-cap"><b>{title}</b>{caption}</p></div>')

DISCLAIMER = ('<p class="disclaimer reveal">Layout preview. Images shown are illustrative placeholders. Replace with real photographs only where the patient has given '
              'written consent, shot with identical lighting, angle and distance, unretouched. Individual results vary.</p>')

def faq(items, cat='general'):
    out = ''
    for q, a in items:
        FAQ.append((q, a))
        out += f'<details data-cat="{cat}"><summary>{q}</summary><p>{a}</p></details>'
    return f'<div class="faq reveal">{out}</div>'

def cta(h, p='', btn='Book a consultation', href='contact.html', alt_btn=None):
    b2 = f'<a class="btn" href="{alt_btn[1]}">{alt_btn[0]}</a>' if alt_btn else ''
    return (f'<section class="section section--dark cta"><div class="container reveal"><span class="eyebrow">Begin here</span><h2>{h}</h2>'
            f'{"<p class=lead>"+p+"</p>" if p else ""}<div class="btn-row"><a class="btn btn--solid" href="{href}">{btn}</a>{b2}</div></div></section>')

def related(links, title='Keep exploring'):
    cards = ''.join(f'<a class="card reveal d{i%3}" href="{u}"><span class="num">{i+1:02d}</span><h3>{t}</h3><p>{d}</p></a>' for i, (u, t, d) in enumerate(links))
    return f'<section class="section section--alt"><div class="container"><div class="center reveal"><span class="eyebrow">Related</span><h2>{title}</h2></div><div class="grid g3 mt2">{cards}</div></div></section>'

def hero_inner(crumbs, eyebrow, h1, lead, slot, alt):
    cr = '<nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a>' + ''.join(
        f'<span><a href="{u}">{n}</a></span>' if u else f'<span aria-current="page">{n}</span>' for n, u in crumbs) + '</nav>'
    return (f'<section class="page-hero"><div class="container page-hero-grid"><div>{cr}<span class="eyebrow reveal">{eyebrow}</span>'
            f'<h1 class="reveal d1">{h1}</h1><p class="lead reveal d2">{lead}</p></div>{img(slot, alt, "r34", "arch reveal d2", eager=True)}</div></section>')

def facts(items):
    return '<div class="facts reveal">' + ''.join(f'<div class="fact"><b>{n}</b><span>{t}</span></div>' for n, t in items) + '</div>'

def tabs(items, label='Options'):
    """items: (id, label, html). Returns tab list + panels (JS handles activation)."""
    tl = ''.join(f'<button class="tab" role="tab" data-tab="{i}" aria-selected="false">{l}</button>' for i, l, _ in items)
    pn = ''.join(f'<div class="tab-panel" role="tabpanel" data-panel="{i}">{b}</div>' for i, _, b in items)
    return f'<div class="tab-list" role="tablist" aria-label="{label}">{tl}</div>{pn}'

def dl(rows):
    return '<dl>' + ''.join(f'<dt>{k}</dt><dd>{v}</dd>' for k, v in rows) + '</dl>'

def table(head, rows):
    h = ''.join(f'<th>{c}</th>' for c in head)
    r = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in row) + '</tr>' for row in rows)
    return f'<div class="table-wrap reveal"><table><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'

def myths(pairs):
    return '<div class="myth-grid reveal">' + ''.join(f'<div class="m"><i>The myth</i>{m}</div><div class="t"><i>The truth</i><p>{t}</p></div>' for m, t in pairs) + '</div>'

def timeline(steps):
    return '<div class="timeline">' + ''.join(f'<div class="step reveal"><span class="when">{w}</span><h3>{t}</h3><p>{d}</p></div>' for w, t, d in steps) + '</div>'

def callout(title, body, warn=False):
    return f'<div class="callout{" callout--warn" if warn else ""} reveal"><b>{title}</b><p>{body}</p></div>'

def tile(href, n, title, text, slot, cls=''):
    return (f'<a class="tile reveal {cls}" href="{href}"><img src="images/{slot}.jpg" alt="" width="800" height="800" loading="lazy" decoding="async" onerror="this.onerror=null;this.src=\'images/art/{slot}.svg\'">'
            f'<span class="n">{n}</span><span class="go">↗</span><div class="in"><h3>{title}</h3><p>{text}</p></div></a>')

def post_card(slug, title, desc, mins, i=0):
    return (f'<a class="post-card reveal d{i%3}" href="{slug}.html">{img("article-"+slug, title, "r169")}<div><span class="meta">Journal · {mins} min read</span>'
            f'<h3>{title}</h3><p>{desc}</p></div></a>')

# ------------------------------------------------------------------ diagrams
def skin_diagram():
    return '''<div class="diagram"><svg viewBox="0 0 760 400" role="img" aria-label="Cross-section of skin showing epidermis, dermis and fat, with burn depth highlighted">
<defs><linearGradient id="gd" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#EBC6A4"/><stop offset="1" stop-color="#E2AE86"/></linearGradient>
<pattern id="fat" width="34" height="30" patternUnits="userSpaceOnUse"><ellipse cx="17" cy="15" rx="13" ry="11" fill="#F8E7BC" stroke="#E6CC8E" stroke-width="1.5"/></pattern>
<pattern id="char" width="8" height="8" patternUnits="userSpaceOnUse"><rect width="8" height="8" fill="#2B1A12"/><path d="M0 8L8 0" stroke="#5A3A28" stroke-width="1.5"/></pattern></defs>
<rect x="40" y="92" width="560" height="140" fill="url(#gd)"/><rect x="40" y="232" width="560" height="120" fill="url(#fat)"/><rect x="40" y="232" width="560" height="120" fill="#F8E7BC" opacity=".5"/>
<rect x="40" y="70" width="560" height="22" fill="#B77A50"/><rect x="40" y="66" width="560" height="4" fill="#8F5934"/>
<path d="M190 70 Q 176 44 168 24" stroke="#1E0F08" stroke-width="4" fill="none" stroke-linecap="round"/>
<path d="M190 70 C 192 120 204 160 202 200" stroke="#6B3F27" stroke-width="11" fill="none" stroke-linecap="round"/><circle cx="202" cy="208" r="15" fill="#5A331B"/>
<ellipse cx="226" cy="150" rx="12" ry="22" fill="#F4DCA8" stroke="#D9B873" stroke-width="2"/>
<path d="M430 70 L 430 168" stroke="#C98F5E" stroke-width="3" fill="none"/><path d="M430 168 c -22 4 -22 22 0 22 c 22 0 22 18 0 22 c -22 4 -22 -14 0 -18" stroke="#B77A50" stroke-width="5" fill="none" stroke-linecap="round"/>
<g stroke="#D8B24A" stroke-width="2" fill="none"><path d="M510 94 v 38"/><path d="M526 94 v 26"/><path d="M544 94 v 44"/></g>
<circle cx="320" cy="262" r="13" fill="#C0392B" opacity=".85"/><circle cx="364" cy="276" r="9" fill="#C0392B" opacity=".85"/><g fill="#C0392B" opacity=".7"><circle cx="300" cy="150" r="3"/><circle cx="330" cy="120" r="3"/><circle cx="480" cy="170" r="3"/><circle cx="560" cy="200" r="3"/></g>
<g data-for="d1" class="pulse"><rect x="40" y="70" width="560" height="22" fill="#E74C3C" opacity=".62"/></g>
<g data-for="d2a" class="pulse"><rect x="40" y="70" width="560" height="62" fill="#E74C3C" opacity=".5"/></g>
<g data-for="d2b" class="pulse"><rect x="40" y="70" width="560" height="132" fill="#B03A2E" opacity=".52"/></g>
<g data-for="d3"><rect x="40" y="70" width="560" height="168" fill="url(#char)" opacity=".78"/></g>
<g data-for="d1"><path d="M628 81 H 600" stroke="#E74C3C" stroke-width="2"/><text x="636" y="85">Depth reached</text></g>
<g data-for="d2a"><path d="M628 101 H 600" stroke="#E74C3C" stroke-width="2"/><text x="636" y="105">Depth reached</text></g>
<g data-for="d2b"><path d="M628 136 H 600" stroke="#B03A2E" stroke-width="2"/><text x="636" y="140">Depth reached</text></g>
<g data-for="d3"><path d="M628 154 H 600" stroke="#2B1A12" stroke-width="2"/><text x="636" y="158">Depth reached</text></g>
<g><text x="622" y="364" opacity=".0">.</text></g>
<text x="40" y="52" style="font-size:11px">Hair shaft</text><text x="640" y="42">Skin surface ↓</text>
<text x="40" y="385" style="font-size:11px">Layers: epidermis · dermis (follicles, glands, vessels, nerves) · fat</text>
</svg></div>'''

def scalp_diagram():
    ring = lambda cx, cy, r, op: f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="var(--accent)" opacity="{op}"/>'
    return f'''<div class="diagram"><svg viewBox="0 0 400 440" role="img" aria-label="Top view of a head showing where different types of hair loss usually begin">
<polygon points="200,36 186,62 214,62" fill="#7A4A2D"/><ellipse cx="64" cy="232" rx="13" ry="28" fill="#7A4A2D"/><ellipse cx="336" cy="232" rx="13" ry="28" fill="#7A4A2D"/>
<ellipse cx="200" cy="232" rx="134" ry="170" fill="#8F5934"/><ellipse cx="200" cy="238" rx="120" ry="152" fill="#1E0F08"/>
<g fill="none" stroke="#3A2216" stroke-width="2" opacity=".7"><circle cx="150" cy="150" r="9"/><circle cx="250" cy="150" r="9"/><circle cx="130" cy="230" r="9"/><circle cx="270" cy="230" r="9"/><circle cx="170" cy="340" r="9"/><circle cx="230" cy="340" r="9"/><circle cx="200" cy="110" r="9"/><circle cx="200" cy="200" r="9"/></g>
<g data-for="traction" class="pulse"><path d="M88 150 C 132 82 268 82 312 150 L 292 162 C 252 118 148 118 108 162 Z" fill="var(--accent)" opacity=".75"/><ellipse cx="98" cy="176" rx="14" ry="30" fill="var(--accent)" opacity=".75"/><ellipse cx="302" cy="176" rx="14" ry="30" fill="var(--accent)" opacity=".75"/></g>
<g data-for="ccca" class="pulse">{ring(200,262,22,.85)}{ring(200,262,50,.45)}{ring(200,262,80,.22)}</g>
<g data-for="te" class="pulse"><ellipse cx="200" cy="238" rx="120" ry="152" fill="var(--accent)" opacity=".28"/><ellipse cx="200" cy="238" rx="120" ry="152" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="3 9" opacity=".8"/></g>
<g data-for="aga" class="pulse"><path d="M96 162 C 118 118 150 108 172 126 L 200 150 L 228 126 C 250 108 282 118 304 162 L 288 172 C 272 140 252 136 236 150 L 200 180 L 164 150 C 148 136 128 140 112 172 Z" fill="var(--accent)" opacity=".8"/>{ring(200,274,34,.55)}<rect x="193" y="170" width="14" height="140" rx="7" fill="var(--accent)" opacity=".5"/></g>
<g data-for="areata" class="pulse">{ring(150,200,22,.8)}{ring(256,286,28,.8)}{ring(206,350,16,.8)}{ring(260,170,12,.8)}</g>
<text x="200" y="22" text-anchor="middle">Front</text><text x="200" y="430" text-anchor="middle">Back</text>
</svg></div>'''

# ------------------------------------------------------------------ chrome
SERVICES = [
    ('burns.html', 'Burn care &amp; recovery', 'Signature'), ('scars.html', 'Scars &amp; keloids', ''),
    ('hair.html', 'Hair loss clinic', ''), ('hair-restoration.html', 'Hair restoration', ''),
    ('skin.html', 'Skin of colour', ''), ('aesthetics.html', 'Non-surgical aesthetics', ''), ('weight-loss.html', 'Weight loss &amp; GLP-1', '')]

def header(cur):
    mk = MARK
    sv = ''.join(f'<a href="{u}"{" aria-current=page" if u==cur else ""}>{n}<small>{t}</small></a>' for u, n, t in SERVICES)
    cp = lambda u: ' aria-current="page"' if u == cur else ''
    return (f'<header class="site-header" id="site-header"><div class="container nav">'
            f'<a class="brand" href="index.html" aria-label="{SITE_NAME} home"><span class="brand-mark">{mk}</span><span><span class="brand-name">Dr. Wanjiru MD</span><span class="brand-sub">Plastic, reconstructive &amp; aesthetic surgeon</span></span></a>'
            f'<nav aria-label="Main"><ul class="nav-list" id="nav-list">'
            f'<li class="has-menu"><a class="nl" href="services.html"{cp("services.html")}>Services</a><div class="menu">{sv}</div></li>'
            f'<li><a class="nl" href="journal.html"{cp("journal.html")}>Journal</a></li><li><a class="nl" href="faq.html"{cp("faq.html")}>FAQ</a></li>'
            f'<li><a class="nl" href="about.html"{cp("about.html")}>About</a></li>'
            f'<li><a class="btn btn--sm btn--solid" href="contact.html">Book</a></li></ul></nav>'
            f'<button class="menu-btn" id="menu-btn" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button></div></header>')

def footer():
    mk = MARK
    sv = ''.join(f'<li><a href="{u}">{n}</a></li>' for u, n, _ in SERVICES)
    return (f'<footer class="site-footer"><div class="container"><div class="footer-grid"><div>'
            f'<div class="footer-brand"><span class="brand-mark">{mk}</span><span><span class="brand-name">Dr. Wanjiru MD</span><span class="brand-sub">Plastic, reconstructive &amp; aesthetic surgeon</span></span></div>'
            f'<p style="max-width:36ch">Burn recovery, scar care, hair restoration, skin and medical weight loss, designed around Black and melanin-rich skin. Upper Hill, Nairobi.</p></div>'
            f'<div><h4>Services</h4><ul>{sv}</ul></div>'
            f'<div><h4>Learn</h4><ul><li><a href="journal.html">Journal</a></li><li><a href="burn-first-aid.html">Burn first aid</a></li><li><a href="traction-alopecia.html">Traction alopecia</a></li>'
            f'<li><a href="sunscreen-black-skin.html">Sunscreen for Black skin</a></li><li><a href="faq.html">FAQ</a></li><li><a href="about.html">About Dr. Wanjiru</a></li></ul></div>'
            f'<div><h4>Clinic</h4><ul><li>Upper Hill, Nairobi, Kenya</li><li>[Building · Floor · Suite]</li><li>[Mon–Sat · opening hours]</li><li>[+254 phone / WhatsApp]</li><li><a href="contact.html">Book a consultation →</a></li></ul></div></div>'
            f'<div class="legal"><span>© 2026 Dr. Wanjiru MD. Plastic &amp; reconstructive surgery, Upper Hill, Nairobi.</span>'
            f'<span>Educational content only, not a substitute for medical advice. Individual results vary. Concept preview: details to be confirmed by Dr. Wanjiru.</span></div></div></footer>'
            f'<div class="sticky-cta"><a href="contact.html" class="p">Book</a><a href="tel:+254000000000">Call</a><a href="contact.html">WhatsApp</a></div>')


# ------------------------------------------------------------------ page wrapper
def schema_graph(path, title, desc, kind, crumbs, article=None):
    url = f'{SITE_URL}/{path}'
    g = [{
        '@type': 'Physician', '@id': f'{SITE_URL}/#clinic', 'name': SITE_NAME, 'url': SITE_URL + '/',
        'description': 'Plastic and reconstructive surgeon in Upper Hill, Nairobi, focused on burn recovery, scar revision, hair restoration, skin of colour and medical weight loss.',
        'medicalSpecialty': 'PlasticSurgery', 'image': f'{SITE_URL}/images/og-default.png',
        'address': {'@type': 'PostalAddress', 'addressLocality': 'Nairobi', 'addressRegion': 'Upper Hill', 'addressCountry': 'KE'},
        'areaServed': [{'@type': 'City', 'name': 'Nairobi'}, {'@type': 'Country', 'name': 'Kenya'}],
        'availableService': [{'@type': 'MedicalProcedure', 'name': n} for n in
                             ['Burn scar revision', 'Keloid and scar management', 'Hair transplantation and hair loss treatment', 'Skin of colour treatments for hyperpigmentation and acne scarring',
                              'Non-surgical aesthetic treatments', 'Medical weight loss with GLP-1 therapy']]},
        {'@type': 'WebSite', '@id': f'{SITE_URL}/#website', 'url': SITE_URL + '/', 'name': SITE_NAME, 'inLanguage': 'en-KE', 'publisher': {'@id': f'{SITE_URL}/#clinic'}}]
    if article:
        g.append({'@type': 'Article', 'headline': title, 'description': desc, 'url': url, 'datePublished': TODAY, 'dateModified': TODAY,
                  'image': f'{SITE_URL}/images/og-default.png', 'inLanguage': 'en-KE', 'author': {'@id': f'{SITE_URL}/#clinic'},
                  'publisher': {'@id': f'{SITE_URL}/#clinic'}, 'mainEntityOfPage': url})
    else:
        g.append({'@type': kind, 'name': title, 'description': desc, 'url': url, 'inLanguage': 'en-KE', 'isPartOf': {'@id': f'{SITE_URL}/#website'}, 'about': {'@id': f'{SITE_URL}/#clinic'}})
    items = [{'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': SITE_URL + '/'}]
    for i, (n, u) in enumerate(crumbs, 2):
        items.append({'@type': 'ListItem', 'position': i, 'name': n.replace('&amp;', '&'), 'item': f'{SITE_URL}/{u or path}'})
    g.append({'@type': 'BreadcrumbList', 'itemListElement': items})
    if FAQ:
        strip = lambda s: _h.unescape(s.replace('<b>', '').replace('</b>', '')).replace('&amp;', '&')
        g.append({'@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': strip(q), 'acceptedAnswer': {'@type': 'Answer', 'text': strip(a)}} for q, a in FAQ]})
    return json.dumps({'@context': 'https://schema.org', '@graph': g}, ensure_ascii=False, separators=(',', ':'))

def page(path, title, desc, body, crumbs=(), kind='MedicalWebPage', priority='0.7', article=False, og_slot=None, noindex=False):
    url = f'{SITE_URL}/{path}' if path != 'index.html' else SITE_URL + '/'
    ld = schema_graph(path, title, desc, kind, crumbs, article)
    og = f'{SITE_URL}/images/og-default.png'
    robots = 'noindex, follow' if noindex else 'index, follow, max-image-preview:large, max-snippet:-1'
    out = f'''<!doctype html>
<html lang="en-KE" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en-ke" href="{url}"><link rel="alternate" hreflang="x-default" href="{url}">
<meta name="theme-color" content="#FBF3EE">
<meta property="og:type" content="{'article' if article else 'website'}"><meta property="og:site_name" content="{SITE_NAME}"><meta property="og:locale" content="en_KE">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{url}">
<meta property="og:image" content="{og}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="{SITE_NAME}, plastic and reconstructive surgeon, Upper Hill, Nairobi">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{esc(title)}"><meta name="twitter:description" content="{esc(desc)}"><meta name="twitter:image" content="{og}">
<link rel="icon" href="favicon.svg" type="image/svg+xml"><link rel="icon" href="favicon-32.png" sizes="32x32" type="image/png"><link rel="apple-touch-icon" href="apple-touch-icon.png"><link rel="manifest" href="site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
<script type="application/ld+json">{ld}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{header(path)}
<main id="main">
{body}
</main>
{footer()}
<script src="main.js" defer></script>
</body>
</html>
'''
    PAGES.append((path, priority))
    FAQ.clear()
    return out
