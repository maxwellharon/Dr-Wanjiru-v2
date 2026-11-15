#!/usr/bin/env python3
"""Build everything: python3 _build/build.py  (run from anywhere)"""
import os, sys, json, glob
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..'))
sys.path.insert(0, HERE)
import art, logos, lib
import content_main as cm, content_more as co, content_misc as cx

os.chdir(ROOT)
art.build(); logos.build()

pages = {'index.html': cm.home(), 'services.html': cm.services(), 'burns.html': cm.burns(), 'scars.html': cm.scars(),
         'hair.html': co.hair(), 'hair-restoration.html': co.restoration(), 'skin.html': co.skin(), 'aesthetics.html': co.aesthetics(), 'weight-loss.html': co.weight(),
         'about.html': cx.about(), 'journal.html': cx.journal(), 'faq.html': cx.faq_page(), 'contact.html': cx.contact(), '404.html': cx.not_found()}
arts = cx.articles()
for (slug, *_), html in zip(__import__('data').ARTICLES, arts):
    pages[slug + '.html'] = html
for name, html in pages.items():
    open(name, 'w').write(html)

# SEO files
U = lib.SITE_URL
prio = {p: pr for p, pr in lib.PAGES}
urls = ''
for p, pr in lib.PAGES:
    if p == '404.html': continue
    loc = U + '/' if p == 'index.html' else f'{U}/{p}'
    urls += f'<url><loc>{loc}</loc><lastmod>{lib.TODAY}</lastmod><changefreq>monthly</changefreq><priority>{pr if p != "index.html" else "1.0"}</priority></url>\n'
open('sitemap.xml', 'w').write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
open('robots.txt', 'w').write(f'User-agent: *\nAllow: /\nDisallow: /_build/\n\nSitemap: {U}/sitemap.xml\n')
open('site.webmanifest', 'w').write(json.dumps({'name': 'Dr. Wanjiru MD', 'short_name': 'Wanjiru MD', 'start_url': '/', 'display': 'standalone', 'background_color': '#FBF3EE', 'theme_color': '#FBF3EE',
                                                  'icons': [{'src': 'icon-192.png', 'sizes': '192x192', 'type': 'image/png'}, {'src': 'icon-512.png', 'sizes': '512x512', 'type': 'image/png'}]}, indent=2))
fav = open('logos/favicon.svg').read()
open('favicon.svg', 'w').write(fav)

# PNG renders (favicon, share image, logo PNGs, presentation board)
from playwright.sync_api import sync_playwright
os.makedirs('logos/png', exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch()
    def shot(html, out, w, h, scale=1):
        pg = b.new_page(viewport={'width': w, 'height': h}, device_scale_factor=scale)
        open(os.path.join(HERE,'_tmp.html'),'w').write(html); pg.goto('file://'+os.path.join(HERE,'_tmp.html')); pg.wait_for_timeout(250); pg.screenshot(path=out, omit_background=False); pg.close()
    def img(path, px_w, px_h, out, scale=1, bg='transparent'):
        shot(f'<body style="margin:0;background:{bg}"><img src="file://{ROOT}/{path}" width="{px_w}" height="{px_h}" style="display:block"></body>', out, px_w, px_h, scale)
    img('logos/favicon.svg', 32, 32, 'favicon-32.png'); img('logos/app-icon.svg', 180, 180, 'apple-touch-icon.png')
    img('logos/app-icon.svg', 192, 192, 'icon-192.png'); img('logos/app-icon.svg', 512, 512, 'icon-512.png')
    # open-graph share image 1200x630: approved primary logo on blush
    shot(f'<body style="margin:0;background:#F1DDD4;display:grid;place-items:center;width:1200px;height:630px"><img src="file://{ROOT}/logos/primary-blush.svg" style="width:1200px"></body>', 'images/og-default.png', 1200, 630)
    # every logo as PNG at 2x (transparent where the SVG is transparent)
    for f in sorted(glob.glob('logos/*.svg')):
        n = os.path.basename(f)[:-4]
        import re
        vb = re.search(r'viewBox="0 0 (\d+) (\d+)"', open(f).read()); w, h = int(vb.group(1)), int(vb.group(2))
        pg = b.new_page(viewport={'width': w, 'height': h}, device_scale_factor=2)
        open(os.path.join(HERE, '_tmp.html'), 'w').write(f'<body style="margin:0;background:transparent"><img src="file://{ROOT}/{f}" width="{w}" height="{h}" style="display:block"></body>')
        pg.goto('file://' + os.path.join(HERE, '_tmp.html')); pg.wait_for_timeout(120); pg.screenshot(path=f'logos/png/{n}.png', omit_background=True); pg.close()
    # presentation board
    def sec(title, names, cls):
        return f'<h2>{title}</h2><div class="r {cls}">' + ''.join(f'<figure><img src="file://{ROOT}/logos/{n}.svg"><figcaption>{n}</figcaption></figure>' for n in names) + '</div>'
    html = ('<style>body{margin:0;padding:56px;background:#2B1D19;font-family:Georgia,serif;color:#FBF3EE;width:2000px}h1{font-weight:400;font-size:48px;margin:0 0 6px}'
            'p{margin:0 0 20px;color:#D9A596;font-family:Arial;letter-spacing:3px;font-size:13px;text-transform:uppercase}h2{font-weight:400;font-size:26px;margin:46px 0 14px;color:#D9A596}'
            '.r{display:flex;gap:18px;flex-wrap:wrap}figure{margin:0}figcaption{font:12px Arial;letter-spacing:2px;color:#b99a8f;margin-top:6px;text-transform:uppercase}'
            '.p img{width:470px;border-radius:10px}.s img{width:300px;border-radius:10px}.m img{width:190px;border-radius:10px}.sw{display:flex;gap:14px}.sw div{width:150px;height:110px;border-radius:10px;padding:12px;font:12px Arial;letter-spacing:1px;box-sizing:border-box}</style>'
            '<h1>Dr. Wanjiru MD · Logo system</h1><p>Approved arch mark · primary, stacked, wordmark, mark, one-colour</p>'
            + sec('Primary lockup', ['primary-blush', 'primary-ivory', 'primary-terracotta', 'primary-cocoa'], 'p')
            + sec('Service taglines', ['tagline-burns', 'tagline-scars', 'tagline-hair', 'tagline-aesthetics'], 'p')
            + sec('Stacked', ['stacked-blush', 'stacked-ivory', 'stacked-terracotta', 'stacked-cocoa'], 's')
            + sec('Wordmark only', ['wordmark-blush', 'wordmark-terracotta', 'wordmark-cocoa'], 'p')
            + sec('Mark, avatar and app icons', ['mark-blush', 'mark-terracotta', 'mark-cocoa', 'avatar-blush', 'avatar-terracotta', 'avatar-cocoa', 'app-icon', 'favicon'], 'm')
            + '<h2>Palette</h2><div class="sw">' + ''.join(f'<div style="background:{c};color:{t}">{n}<br>{c}</div>' for n, c, t in [
                ('Terracotta', '#9F5C53', '#FBF3EE'), ('Blush', '#F1DDD4', '#3E2C26'), ('Title rose', '#9C625A', '#FBF3EE'), ('Cocoa', '#4F3B32', '#FBF3EE'),
                ('Deep terracotta', '#7E4540', '#FBF3EE'), ('Cream', '#FBF3EE', '#3E2C26'), ('Rose gold', '#D9A596', '#3E2C26'), ('Night', '#2B1D19', '#FBF3EE')]) + '</div>')
    shot(html, 'logos/LOGO-BOARD.png', 2112, 2600)
    b.close()
os.remove(os.path.join(HERE,'_tmp.html')) if os.path.exists(os.path.join(HERE,'_tmp.html')) else None
print('built', len(pages), 'pages')
