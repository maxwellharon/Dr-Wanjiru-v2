#!/usr/bin/env python3
"""Logo system for Dr. Wanjiru MD, built from the client-approved logo:
terracotta arch + crossed-stroke "W", spaced serif name, hairline rule, two-line spaced tagline.
All text is converted to outlines so the SVGs need no fonts.
Run: python3 _build/logos.py"""
import os, glob
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'logos')

# ------------------------------------------------------------------ brand constants (flip here)
NAME = 'DR. WANJIRU MD'          # the approved artwork reads "DR. WANJIRU M"; brief says MD
TAG = ['PLASTIC, RECONSTRUCTIVE', '& AESTHETIC SURGEON']

# palette sampled from the approved logo + planned extras
P = dict(terracotta='#9F5C53', blush='#F1DDD4', title='#9C625A', cocoa='#4F3B32',
         deep='#7E4540', cream='#FBF3EE', ivory='#FFFDF9', night='#2B1D19', rose='#D9A596', white='#FFFFFF')

# ------------------------------------------------------------------ fonts (closest installed match to Cormorant Garamond / Jost)
_c = {}
def font(key):
    if key not in _c:
        _c[key] = TTFont({
            'serif': '/usr/share/texmf/fonts/opentype/public/lm/lmroman12-regular.otf',
            'sans': '/usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf',
            'sans-l': '/usr/share/fonts/truetype/google-fonts/Poppins-Regular.ttf',
        }[key])
    return _c[key]

def measure(key, s, size, tracking=0):
    f = font(key); cm = f.getBestCmap(); upm = f['head'].unitsPerEm
    return sum(f['hmtx'][cm.get(ord(c)) or cm[ord('?')]][0] for c in s) * size / upm + tracking * (len(s) - 1)

def text(key, s, size, x, y, fill, tracking=0, anchor='start', sw=None):
    sw = size * 0.012 if sw is None else sw
    f = font(key); gs = f.getGlyphSet(); cm = f.getBestCmap(); upm = f['head'].unitsPerEm
    sc = size / upm; total = measure(key, s, size, tracking)
    cx = {'start': x, 'middle': x - total / 2, 'end': x - total}[anchor]
    d = []
    for ch in s:
        g = cm.get(ord(ch)) or cm[ord('?')]
        pen = SVGPathPen(gs); gs[g].draw(TransformPen(pen, (sc, 0, 0, -sc, cx, y)))
        if pen.getCommands(): d.append(pen.getCommands())
        cx += f['hmtx'][g][0] * sc + tracking
    return f'<path d="{" ".join(d)}" fill="{fill}" stroke="{fill}" stroke-width="{sw}" stroke-linejoin="round"/>'

# ------------------------------------------------------------------ the mark
def crossed_w(cx, cy, width, fill):
    """Two overlapping V's: thick down-strokes, hairline up-strokes, small flat serifs.
    Drawn in a 100 x 72 box, centred on (cx, cy)."""
    a, b, H = 16, 4.6, 72
    def v(x0, xb, x1):
        thick = f'M{x0-a/2},0 L{x0+a/2},0 L{xb+a*0.30},{H} L{xb-a*0.30},{H} Z'
        thin = f'M{xb-b*0.2},{H} L{xb+b*0.9},{H} L{x1+b/2},0 L{x1-b/2},0 Z'
        sr = f'M{x0-10},0 h20 v3.4 h-20 Z M{x1-8},0 h16 v3 h-16 Z'
        return thick + thin + sr
    d = v(8, 35, 61) + v(39, 66, 92)
    s = width / 100
    return f'<path transform="translate({cx-50*s:.2f} {cy-36*s:.2f}) scale({s:.4f})" d="{d}" fill="{fill}"/>'

def arch(x, y, w, h, fill):
    r = w / 2
    return f'<path d="M{x},{y+h} V{y+r} A{r},{r} 0 0 1 {x+w},{y+r} V{y+h} Z" fill="{fill}"/>'

def mark(x, y, w, c):
    """Arch with W. (x,y)=top-left, w=width; height = 1.285*w like the approved artwork."""
    h = w * 1.285
    cxw, cyw, ww = x + w / 2, y + h * 0.60, w * 0.70
    if c['w'] == 'cut':
        mid = f'cut{abs(hash((round(x), round(y), round(w), c["arch"]))) % 99999}'
        big = 4000
        mask = f'<mask id="{mid}" maskUnits="userSpaceOnUse" x="-{big}" y="-{big}" width="{2*big}" height="{2*big}"><rect x="-{big}" y="-{big}" width="{2*big}" height="{2*big}" fill="#fff"/>{crossed_w(cxw, cyw, ww, "#000")}</mask>'
        return f'<defs>{mask}</defs>' + arch(x, y, w, h, c['arch']).replace('/>', f' mask="url(#{mid})"/>'), h
    return arch(x, y, w, h, c['arch']) + crossed_w(cxw, cyw, ww, c['w']), h

# ------------------------------------------------------------------ lockups
def horizontal(c, tag=TAG, w=1000, h=420, rule=True):
    mw = 132; mx = 78
    m, mh = mark(mx, (h - mw * 1.285) / 2, mw, c)
    tx = mx + mw + 62
    nsize, ntrack = 56, 8.5
    nwid = measure('serif', NAME, nsize, ntrack)
    cy = h / 2
    tsize, ttrack, lead = 15.2, 3.9, 29
    block_h = nsize * 0.70 + 26 + 1 + 30 + (len(tag) - 1) * lead
    top = cy - block_h / 2
    ny = top + nsize * 0.70
    out = m + text('serif', NAME, nsize, tx, ny, c['name'], ntrack)
    ry = ny + 26
    out += f'<rect x="{tx}" y="{ry}" width="{nwid:.1f}" height="1.3" fill="{c["rule"]}"/>'
    for i, line in enumerate(tag):
        out += text('sans', line, tsize, tx + 1, ry + 36 + i * lead, c['tag'], ttrack)
    return out, nwid + tx + 50

def stacked(c, tag=TAG, w=720, h=620):
    mw = 150; m, mh = mark(w / 2 - mw / 2, 58, mw, c)
    nsize, ntrack = 46, 7.5
    ny = 58 + mh + 78
    out = m + text('serif', NAME, nsize, w / 2, ny, c['name'], ntrack, 'middle')
    nwid = measure('serif', NAME, nsize, ntrack)
    out += f'<rect x="{w/2-nwid/2:.1f}" y="{ny+22}" width="{nwid:.1f}" height="1.2" fill="{c["rule"]}"/>'
    for i, line in enumerate(tag):
        out += text('sans', line, 14, w / 2, ny + 58 + i * 27, c['tag'], 3.6, 'middle')
    return out

def wordmark(c, w=1000, h=260):
    nsize, ntrack = 62, 9.5
    nwid = measure('serif', NAME, nsize, ntrack)
    x = (w - nwid) / 2
    out = text('serif', NAME, nsize, x, 112, c['name'], ntrack)
    out += f'<rect x="{x:.1f}" y="140" width="{nwid:.1f}" height="1.4" fill="{c["rule"]}"/>'
    out += text('sans', ' '.join(TAG).replace('RECONSTRUCTIVE &', 'RECONSTRUCTIVE &'), 14.5, w / 2, 182, c['tag'], 4.2, 'middle')
    return out

def svg(inner, bg, w, h, rx=0, circle=False):
    shape = ''
    if bg:
        shape = (f'<circle cx="{w/2}" cy="{h/2}" r="{w/2}" fill="{bg}"/>' if circle
                 else f'<rect width="{w}" height="{h}" rx="{rx}" fill="{bg}"/>')
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="Dr. Wanjiru MD">{shape}{inner}</svg>'

# ------------------------------------------------------------------ colourways
def cw(bg, arch_, w, name, rule, tag):
    return dict(bg=bg, arch=arch_, w=w, name=name, rule=rule, tag=tag)

WAYS = {
  'blush':      cw(P['blush'], P['terracotta'], P['blush'], P['title'], P['title'], P['cocoa']),   # the approved version
  'ivory':      cw(P['ivory'], P['terracotta'], P['ivory'], P['title'], P['title'], P['cocoa']),
  'terracotta': cw(P['terracotta'], P['blush'], P['terracotta'], P['cream'], P['rose'], P['blush']),
  'cocoa':      cw(P['night'], P['rose'], P['night'], P['blush'], P['rose'], P['rose']),
  'transparent':cw(None, P['terracotta'], P['blush'], P['title'], P['title'], P['cocoa']),
}
SIZES = dict(horizontal=(1000, 420), stacked=(720, 620), wordmark=(1000, 260))

def build():
    os.makedirs(OUT, exist_ok=True)
    for f in glob.glob(OUT + '/*.svg') + glob.glob(OUT + '/png/*'):
        os.remove(f)
    os.makedirs(OUT + '/png', exist_ok=True)
    files = []
    def put(name, s):
        open(f'{OUT}/{name}.svg', 'w').write(s); files.append(name)

    # 1 primary horizontal in every colourway + stacked
    for way, c in WAYS.items():
        inner, _ = horizontal(c)
        put(f'primary-{way}', svg(inner, c['bg'], 1000, 420))
    for way in ('blush', 'ivory', 'terracotta', 'cocoa'):
        c = WAYS[way]
        put(f'stacked-{way}', svg(stacked(c), c['bg'], 720, 620))
        put(f'wordmark-{way}', svg(wordmark(c), c['bg'], 1000, 260))

    # 2 one-colour transparent (W is a true cut-out)
    for nm, col in (('terracotta', P['terracotta']), ('cocoa', P['cocoa']), ('white', P['white'])):
        c = dict(arch=col, w='cut', name=col, rule=col, tag=col)
        inner, _ = horizontal(c)
        put(f'primary-mono-{nm}', svg(inner, None, 1000, 420))

    # 3 tagline variants (service-led)
    alt = {'burns': ['BURNS & RECONSTRUCTIVE', 'SURGERY'], 'scars': ['SCARS, KELOIDS &', 'SKIN OF COLOUR'],
           'hair': ['HAIR LOSS &', 'RESTORATION'], 'aesthetics': ['AESTHETIC MEDICINE &', 'WEIGHT LOSS']}
    for k, t in alt.items():
        inner, _ = horizontal(WAYS['blush'], tag=t)
        put(f'tagline-{k}', svg(inner, WAYS['blush']['bg'], 1000, 420))

    # 4 mark alone, avatar, app icon
    def square(c, size=400, rx=0, circle=False, scale=0.46):
        mw = size * scale
        m, mh = mark((size - mw) / 2, (size - mw * 1.285) / 2, mw, c)
        return svg(m, c['bg'], size, size, rx=rx, circle=circle)
    for way in ('blush', 'terracotta', 'cocoa', 'ivory'):
        put(f'mark-{way}', square(WAYS[way], 400, 0, False, 0.40))
        put(f'avatar-{way}', square(WAYS[way], 400, 0, True, 0.40))
    put('app-icon', square(WAYS['terracotta'], 512, 112, False, 0.42))
    # favicon: terracotta rounded square with blush mark (reads at 16px)
    c = WAYS['terracotta']
    put('favicon', square(c, 64, 14, False, 0.56))
    c = dict(arch=P['terracotta'], w='cut', name='', rule='', tag='')
    m, mh = mark(20, 20, 200, c)
    put('mark-transparent', svg(m, None, 240, 300))
    return files

# ------------------------------------------------------------------ inline mark for site header (CSS-variable coloured)
def inline_mark():
    w = 100; h = w * 1.285
    body = arch(0, 0, w, h, 'var(--accent)') + crossed_w(w / 2, h * 0.60, w * 0.70, 'var(--bg)')
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h:.1f}" aria-hidden="true" focusable="false">{body}</svg>'

if __name__ == '__main__':
    for f in build():
        print(f)
