#!/usr/bin/env python3
"""Generates illustrative placeholder art (SVG) for every image slot.
Real photos: drop images/<name>.jpg next to the page; the site automatically prefers the photo."""
import os, math, random

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'images', 'art')
os.makedirs(ROOT, exist_ok=True)

TONES = ['#2A160D', '#47291A', '#6B3F27', '#8F5934', '#B27847', '#CE9A66', '#E4B98B', '#F1D3AE']
GRAIN = ('<filter id="gr" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" seed="4"/>'
         '<feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .10 0"/></filter>'
         '<filter id="bl"><feGaussianBlur stdDeviation="38"/></filter><filter id="bl2"><feGaussianBlur stdDeviation="14"/></filter>'
         '<filter id="bl3"><feGaussianBlur stdDeviation="5"/></filter>')

def svg(w, h, body, defs=''):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" preserveAspectRatio="xMidYMid slice">'
            f'<defs>{GRAIN}{defs}</defs>{body}<rect width="{w}" height="{h}" filter="url(#gr)"/></svg>')

def lg(i, c1, c2, x1=0, y1=0, x2=1, y2=1):
    return f'<linearGradient id="{i}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>'

PALS = {
    'warm':   ('#F8E6DD', '#E3B3A6', '#B8756B', '#6E3B34'),
    'sand':   ('#FBF3EE', '#EBCFC3', '#C99488', '#8A5249'),
    'plum':   ('#F7E2DA', '#E0A99C', '#9F5C53', '#4A2824'),
    'green':  ('#F4E8E1', '#DDBFB2', '#A8665C', '#5A302B'),
    'night':  ('#4A2E29', '#3A2420', '#8A4F46', '#201210'),
    'gold':   ('#FFF0E6', '#F0CBBB', '#C98B7C', '#7E4540'),
}

def scene(w, h, pal, seed, shapes=6, rings=True):
    r = random.Random(seed)
    a, b, c, d = PALS[pal]
    defs = lg('bg', a, b, 0, 0, 1, 1)
    body = f'<rect width="{w}" height="{h}" fill="url(#bg)"/>'
    for i in range(shapes):
        cx, cy = r.uniform(0, w), r.uniform(0, h)
        rad = r.uniform(.18, .42) * max(w, h)
        col = r.choice([b, c, c, d])
        body += f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{rad:.0f}" fill="{col}" opacity="{r.uniform(.25,.6):.2f}" filter="url(#bl)"/>'
    if rings:
        cx, cy = r.uniform(.3, .7) * w, r.uniform(.3, .7) * h
        for k in range(1, 8):
            body += f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{k*min(w,h)*.09:.0f}" fill="none" stroke="{d}" stroke-width="1.4" opacity="{0.28-k*0.03:.2f}"/>'
    return body, defs

LOTUS = ('M 0,-112 C 8,-80 52,-52 58,-4 C 64,50 34,104 0,106 C -34,104 -64,56 -58,6 '
         'C -56,-18 -42,-34 -30,-48 C -28,-26 -14,-16 -4,-18 C -14,-56 -10,-88 0,-112 Z')
PETAL = 'M 0,108 C -78,108 -118,48 -106,-12 C -66,-4 -20,40 0,108 Z'

def flame_scene(w, h, seed, dark=True):
    r = random.Random(seed)
    defs = (lg('fb', '#241411' if dark else '#FBEFE0', '#3F211B' if dark else '#F2C69E', 0, 0, 0, 1)
            + lg('f1', '#7E3A2E', '#D9805F', 0, 1, 0, 0) + lg('f2', '#D9805F', '#F6C9A8', 0, 1, 0, 0)
            + '<radialGradient id="gl"><stop offset="0" stop-color="#FFB45A" stop-opacity=".75"/><stop offset="1" stop-color="#FFB45A" stop-opacity="0"/></radialGradient>')
    cx, cy = w * .5, h * .56
    s = min(w, h) / 300
    body = f'<rect width="{w}" height="{h}" fill="url(#fb)"/>'
    body += f'<circle cx="{cx}" cy="{cy}" r="{190*s:.0f}" fill="url(#gl)"/>'
    body += f'<g transform="translate({cx} {cy}) scale({s*1.5:.2f})">'
    body += f'<path d="{PETAL}" fill="#7A2410" opacity=".95"/><path d="{PETAL}" fill="#7A2410" opacity=".95" transform="scale(-1 1)"/>'
    body += f'<path d="{LOTUS}" fill="url(#f1)"/>'
    body += f'<g transform="translate(0 34) scale(.64)"><path d="{LOTUS}" fill="url(#f2)"/></g>'
    body += f'<g transform="translate(0 62) scale(.32)"><path d="{LOTUS}" fill="#FFF3D2"/></g></g>'
    for _ in range(46):
        x, y = r.gauss(cx, w * .2), r.uniform(0, h * .8)
        body += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r.uniform(1.2,4):.1f}" fill="#FFC37A" opacity="{r.uniform(.2,.8):.2f}"/>'
    return svg(w, h, body, defs)

def coil_scene(w, h, seed, pal='night'):
    r = random.Random(seed)
    a, b, c, d = PALS[pal]
    defs = lg('bg', a, b, 0, 0, 1, 1)
    body = f'<rect width="{w}" height="{h}" fill="url(#bg)"/>'
    body += f'<circle cx="{w*.7:.0f}" cy="{h*.25:.0f}" r="{w*.5:.0f}" fill="{c}" opacity=".35" filter="url(#bl)"/>'
    body += f'<g transform="rotate(-18 {w/2} {h/2})">'
    rows = 24
    for i in range(rows):
        y0 = -h * .2 + i * (h * 1.5 / rows)
        rad = r.uniform(13, 20)
        length = w * 1.7
        adv = rad * 1.3
        turns = length / adv
        n = int(turns * 9)
        pts = []
        ph = r.uniform(0, 6.28)
        for k in range(n + 1):
            t = k / n
            ang = ph + t * turns * 2 * math.pi
            x = -w * .35 + t * length + rad * math.cos(ang)
            y = y0 + rad * math.sin(ang) + 5 * math.sin(t * 7 + i)
            pts.append(f'{x:.0f},{y:.0f}')
        dd = 'M ' + ' L '.join(pts)
        body += f'<path d="{dd}" fill="none" stroke="{d}" stroke-width="{r.uniform(6,8):.1f}" stroke-linecap="round" stroke-linejoin="round"/>'
        body += f'<path d="{dd}" fill="none" stroke="{c}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" opacity=".6" transform="translate(-1.5 -2)"/>'
    body += '</g>'
    return svg(w, h, body, defs)

def ripple_scene(w, h, seed, pal='gold'):
    r = random.Random(seed)
    a, b, c, d = PALS[pal]
    defs = lg('bg', a, b, 0, 0, 1, 1) + f'<radialGradient id="dr" cx=".35" cy=".3"><stop offset="0" stop-color="#fff" stop-opacity=".9"/><stop offset=".25" stop-color="{b}" stop-opacity=".6"/><stop offset="1" stop-color="{c}" stop-opacity=".9"/></radialGradient>'
    body = f'<rect width="{w}" height="{h}" fill="url(#bg)"/>'
    for _ in range(5):
        body += f'<circle cx="{r.uniform(0,w):.0f}" cy="{r.uniform(0,h):.0f}" r="{r.uniform(.15,.35)*w:.0f}" fill="{r.choice([b,c])}" opacity=".35" filter="url(#bl)"/>'
    cx, cy = w * .5, h * .55
    for k in range(1, 9):
        body += f'<ellipse cx="{cx}" cy="{cy}" rx="{k*w*.07:.0f}" ry="{k*w*.07*.78:.0f}" fill="none" stroke="{d}" stroke-width="1.5" opacity="{.4-k*.04:.2f}"/>'
    body += f'<circle cx="{cx}" cy="{cy}" r="{w*.17:.0f}" fill="url(#dr)"/>'
    body += f'<ellipse cx="{cx-w*.06:.0f}" cy="{cy-w*.07:.0f}" rx="{w*.04:.0f}" ry="{w*.025:.0f}" fill="#fff" opacity=".85" transform="rotate(-30 {cx-w*.06:.0f} {cy-w*.07:.0f})"/>'
    for _ in range(26):
        body += f'<circle cx="{r.uniform(0,w):.0f}" cy="{r.uniform(0,h):.0f}" r="{r.uniform(2,9):.1f}" fill="#fff" opacity="{r.uniform(.1,.4):.2f}"/>'
    return svg(w, h, body, defs)

def ribbon_scene(w, h, seed, pal='sand'):
    r = random.Random(seed)
    a, b, c, d = PALS[pal]
    defs = lg('bg', a, b, 0, 0, 0, 1)
    body = f'<rect width="{w}" height="{h}" fill="url(#bg)"/>'
    cols = [c, d, b, c, '#FFFFFF']
    for i in range(9):
        y0 = h * (.1 + i * .1)
        amp = r.uniform(.05, .13) * h
        ph = r.uniform(0, 6)
        top = ' '.join(f'{x:.0f},{y0+amp*math.sin(x/w*5.4+ph):.0f}' for x in range(-20, w + 40, 20))
        bot = ' '.join(f'{x:.0f},{y0+h*.13+amp*math.sin(x/w*5.4+ph+.6):.0f}' for x in range(w + 20, -40, -20))
        body += f'<polygon points="{top} {bot}" fill="{cols[i%len(cols)]}" opacity="{r.uniform(.18,.5):.2f}"/>'
    body += f'<circle cx="{w*.75:.0f}" cy="{h*.2:.0f}" r="{w*.18:.0f}" fill="#fff" opacity=".35" filter="url(#bl2)"/>'
    return svg(w, h, body, defs)

def arch_scene(w, h, seed, pal='sand'):
    a, b, c, d = PALS[pal]
    defs = lg('bg', a, b, 0, 0, 0, 1) + lg('ar', '#FFFFFF', b, 0, 0, 0, 1)
    body = f'<rect width="{w}" height="{h}" fill="url(#bg)"/>'
    base = h * .82
    for i, (x, ww, col, op) in enumerate([(w * .08, w * .34, c, .55), (w * .42, w * .5, d, .35), (w * .6, w * .3, b, .9)]):
        body += f'<path d="M {x:.0f},{base:.0f} L {x:.0f},{h*.35+i*30:.0f} A {ww/2:.0f} {ww/2:.0f} 0 0 1 {x+ww:.0f},{h*.35+i*30:.0f} L {x+ww:.0f},{base:.0f} Z" fill="{col}" opacity="{op}"/>'
    body += f'<rect y="{base:.0f}" width="{w}" height="{h-base:.0f}" fill="{d}" opacity=".18"/>'
    body += f'<line x1="0" y1="{base:.0f}" x2="{w}" y2="{base:.0f}" stroke="{c}" stroke-width="2"/>'
    body += f'<circle cx="{w*.2:.0f}" cy="{base-w*.07:.0f}" r="{w*.07:.0f}" fill="#5E7F57" opacity=".85"/><rect x="{w*.2-4:.0f}" y="{base-w*.02:.0f}" width="8" height="{w*.02:.0f}" fill="{d}"/>'
    body += f'<rect x="{w*.58:.0f}" y="{base-w*.09:.0f}" width="{w*.24:.0f}" height="{w*.09:.0f}" rx="14" fill="{c}" opacity=".7"/>'
    body += f'<circle cx="{w*.8:.0f}" cy="{h*.18:.0f}" r="{w*.14:.0f}" fill="#FFF3D0" opacity=".7" filter="url(#bl2)"/>'
    return svg(w, h, body, defs)

def portrait_scene(w, h, seed, pal='warm', coat=True, label=True):
    a, b, c, d = PALS[pal]
    defs = lg('bg', a, b, 0, 0, 1, 1) + lg('sk', '#8F5934', '#5A331B', 0, 0, 1, 1)
    body = f'<rect width="{w}" height="{h}" fill="url(#bg)"/>'
    body += f'<circle cx="{w*.3:.0f}" cy="{h*.3:.0f}" r="{w*.5:.0f}" fill="#fff" opacity=".35" filter="url(#bl)"/>'
    cx = w * .5
    body += f'<path d="M {cx-w*.42:.0f},{h} C {cx-w*.42:.0f},{h*.72} {cx-w*.2:.0f},{h*.66} {cx:.0f},{h*.66} C {cx+w*.2:.0f},{h*.66} {cx+w*.42:.0f},{h*.72} {cx+w*.42:.0f},{h} Z" fill="{"#FBF3EE" if coat else d}"/>'
    body += f'<path d="M {cx-w*.08:.0f},{h*.66} L {cx:.0f},{h*.8} L {cx+w*.08:.0f},{h*.66} Z" fill="#6B3F27"/>'
    body += f'<rect x="{cx-w*.05:.0f}" y="{h*.56:.0f}" width="{w*.1:.0f}" height="{h*.12:.0f}" rx="12" fill="url(#sk)"/>'
    body += f'<ellipse cx="{cx:.0f}" cy="{h*.42:.0f}" rx="{w*.17:.0f}" ry="{h*.15:.0f}" fill="url(#sk)"/>'
    body += f'<path d="M {cx-w*.2:.0f},{h*.42:.0f} C {cx-w*.24:.0f},{h*.2:.0f} {cx+w*.24:.0f},{h*.2:.0f} {cx+w*.2:.0f},{h*.42:.0f} C {cx+w*.15:.0f},{h*.3:.0f} {cx-w*.15:.0f},{h*.3:.0f} {cx-w*.2:.0f},{h*.42:.0f} Z" fill="#1E0F08"/>'
    if label:
        body += f'<text x="{w/2:.0f}" y="{h-26:.0f}" text-anchor="middle" font-family="Arial,sans-serif" font-size="{w*.028:.0f}" letter-spacing="4" fill="{d}" opacity=".6">PORTRAIT PLACEHOLDER</text>'
    return svg(w, h, body, defs)

# ---------------- before / after
def ba_scene(w, h, kind, after, seed=7):
    r = random.Random(seed)
    skin = ['#7A4A2D', '#8F5934'] if kind != 'pigment' else ['#8A5532', '#9C6840']
    defs = lg('bg', '#F1DDD4', '#DDB8AA', 0, 0, 1, 1) + lg('sk', skin[1], skin[0], 0, 0, 1, 1)
    body = f'<rect width="{w}" height="{h}" fill="url(#bg)"/>'
    if kind == 'scar':
        body += f'<g transform="rotate(-24 {w/2} {h/2})"><rect x="{-w*.2:.0f}" y="{h*.28:.0f}" width="{w*1.4:.0f}" height="{h*.44:.0f}" rx="{h*.22:.0f}" fill="url(#sk)"/>'
        n, op = (3, .35) if after else (7, 1)
        for i in range(n):
            x = w * (.2 + i * (.7 / n)); wd = (5 if after else r.uniform(12, 20))
            body += f'<path d="M {x:.0f},{h*.34:.0f} C {x+30:.0f},{h*.45:.0f} {x-26:.0f},{h*.55:.0f} {x+14:.0f},{h*.66:.0f}" fill="none" stroke="{"#5A331B" if not after else "#6F4328"}" stroke-width="{wd:.0f}" stroke-linecap="round" opacity="{op}"/>'
            if not after:
                body += f'<path d="M {x-5:.0f},{h*.34:.0f} C {x+25:.0f},{h*.45:.0f} {x-31:.0f},{h*.55:.0f} {x+9:.0f},{h*.66:.0f}" fill="none" stroke="#B27847" stroke-width="3" stroke-linecap="round" opacity=".8"/>'
        body += '</g>'
    elif kind == 'pigment':
        body += f'<ellipse cx="{w/2:.0f}" cy="{h*.5:.0f}" rx="{w*.38:.0f}" ry="{h*.38:.0f}" fill="url(#sk)"/>'
        n = 4 if after else 16
        for _ in range(n):
            x, y = w * r.uniform(.25, .75), h * r.uniform(.3, .7)
            body += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r.uniform(14,34) if not after else r.uniform(10,18):.0f}" fill="#3E2214" opacity="{.7 if not after else .18}" filter="url(#bl3)"/>'
    elif kind == 'texture':
        body += f'<ellipse cx="{w/2:.0f}" cy="{h*.5:.0f}" rx="{w*.38:.0f}" ry="{h*.38:.0f}" fill="url(#sk)"/>'
        n = 5 if after else 38
        for _ in range(n):
            x, y = w * r.uniform(.22, .78), h * r.uniform(.28, .72)
            rr = r.uniform(6, 14) if not after else r.uniform(3, 6)
            body += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{rr:.0f}" fill="#4A2A18" opacity="{.75 if not after else .25}"/><circle cx="{x-1:.0f}" cy="{y-2:.0f}" r="{rr*.55:.0f}" fill="#B27847" opacity=".25"/>'
    elif kind == 'hair':
        body += f'<rect y="{h*.3:.0f}" width="{w}" height="{h*.7:.0f}" fill="url(#sk)"/>'
        if after:
            hair = f'M 0,0 L {w},0 L {w},{h*.34:.0f} C {w*.8:.0f},{h*.28:.0f} {w*.2:.0f},{h*.28:.0f} 0,{h*.34:.0f} Z'
        else:
            hair = (f'M 0,0 L {w},0 L {w},{h*.4:.0f} C {w*.92:.0f},{h*.44:.0f} {w*.86:.0f},{h*.46:.0f} {w*.8:.0f},{h*.38:.0f} '
                    f'C {w*.65:.0f},{h*.3:.0f} {w*.35:.0f},{h*.3:.0f} {w*.2:.0f},{h*.38:.0f} C {w*.14:.0f},{h*.46:.0f} {w*.08:.0f},{h*.44:.0f} 0,{h*.4:.0f} Z')
        body += f'<path d="{hair}" fill="#140B07"/>'
        for _ in range(180 if after else 90):
            x, y = r.uniform(0, w), r.uniform(0, h * .3)
            body += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r.uniform(3,7):.1f}" fill="#3A2216" opacity=".7"/>'
    elif kind == 'body':
        cx = w / 2
        sh, wa, hp = (.21, .12, .19) if after else (.22, .19, .27)
        P = lambda dx, y: (cx + dx * w, y * h)
        pts_r = [P(sh, .31), P(sh + .01, .42), P(wa, .50), P(wa, .56), P(hp, .68), P(hp + .01, .84), P(hp - .02, 1.0)]
        right = f'M {cx:.0f},{h*.30:.0f} L {pts_r[0][0]:.0f},{pts_r[0][1]:.0f} C {pts_r[1][0]:.0f},{pts_r[1][1]:.0f} {pts_r[2][0]:.0f},{pts_r[2][1]-30:.0f} {pts_r[3][0]:.0f},{pts_r[3][1]:.0f} C {pts_r[3][0]:.0f},{pts_r[3][1]+40:.0f} {pts_r[4][0]:.0f},{pts_r[4][1]-40:.0f} {pts_r[4][0]:.0f},{pts_r[4][1]:.0f} L {pts_r[6][0]:.0f},{pts_r[6][1]:.0f}'
        left = ' '.join(f'L {2*cx-x:.0f},{y:.0f}' for x, y in reversed(pts_r[4:]))
        mirror = f'L {2*cx-pts_r[6][0]:.0f},{pts_r[6][1]:.0f} L {2*cx-pts_r[4][0]:.0f},{pts_r[4][1]:.0f} C {2*cx-pts_r[4][0]:.0f},{pts_r[4][1]-40:.0f} {2*cx-pts_r[3][0]:.0f},{pts_r[3][1]+40:.0f} {2*cx-pts_r[3][0]:.0f},{pts_r[3][1]:.0f} C {2*cx-pts_r[2][0]:.0f},{pts_r[2][1]-30:.0f} {2*cx-pts_r[1][0]:.0f},{pts_r[1][1]:.0f} {2*cx-pts_r[0][0]:.0f},{pts_r[0][1]:.0f} Z'
        body += f'<rect x="{cx-w*.04:.0f}" y="{h*.2:.0f}" width="{w*.08:.0f}" height="{h*.12:.0f}" rx="12" fill="url(#sk)"/>'
        body += f'<ellipse cx="{cx:.0f}" cy="{h*.16:.0f}" rx="{w*.085:.0f}" ry="{h*.07:.0f}" fill="url(#sk)"/>'
        body += f'<path d="{right} {mirror}" fill="#8A7766"/>'
    body += f'<text x="{w/2:.0f}" y="{h-22:.0f}" text-anchor="middle" font-family="Arial,sans-serif" font-size="{w*.026:.0f}" letter-spacing="3" fill="#3B2A20" opacity=".55">ILLUSTRATIVE PLACEHOLDER</text>'
    return svg(w, h, body, defs)

def write(name, s):
    with open(os.path.join(ROOT, name + '.svg'), 'w') as f:
        f.write(s)

def build():
    W4, H4 = 800, 1000
    WW, HW = 1200, 800
    # hero collage
    write('hero-1', portrait_scene(W4, H4, 1, 'warm', label=False))
    write('hero-2', flame_scene(600, 600, 2))
    write('hero-3', ripple_scene(600, 600, 3, 'plum'))
    write('hero-portrait', portrait_scene(W4, H4, 1, 'warm'))
    write('about-portrait', portrait_scene(W4, H4, 5, 'sand'))
    # page heroes
    write('burns-hero', flame_scene(W4, H4, 11))
    write('burns-detail', flame_scene(WW, HW, 12, dark=False))
    write('scars-hero', ripple_scene(W4, H4, 13, 'warm'))
    write('hair-hero', coil_scene(W4, H4, 14))
    write('hair-restoration-hero', coil_scene(WW, HW, 15, 'sand'))
    write('skin-hero', ripple_scene(W4, H4, 16, 'gold'))
    write('aesthetics-hero', scene(W4, H4, 'plum', 17)[0] and svg(W4, H4, *scene(W4, H4, 'plum', 17)))
    write('weight-hero', ribbon_scene(W4, H4, 18, 'green'))
    write('contact-hero', arch_scene(WW, HW, 19))
    for i in range(1, 5):
        write(f'clinic-{i}', arch_scene(WW if i % 2 else W4, HW if i % 2 else H4, 20 + i, ['sand', 'warm', 'plum', 'green'][i - 1]))
    # article thumbs
    arts = {'burn-first-aid': flame_scene(WW, HW, 31), 'traction-alopecia': coil_scene(WW, HW, 32, 'sand'),
            'glp1-hair-skin': ribbon_scene(WW, HW, 33, 'green'), 'sunscreen-black-skin': ripple_scene(WW, HW, 34, 'gold'),
            'keloids-explained': ripple_scene(WW, HW, 35, 'warm')}
    for k, v in arts.items():
        write('article-' + k, v)
    # service tiles
    write('tile-burns', flame_scene(800, 800, 41)); write('tile-hair', coil_scene(800, 800, 42))
    write('tile-skin', ripple_scene(800, 800, 43, 'gold')); write('tile-weight', ribbon_scene(800, 800, 44, 'green'))
    write('tile-aesthetics', svg(800, 800, *scene(800, 800, 'plum', 45)))
    write('tile-scars', ripple_scene(800, 800, 46, 'warm'))
    # before / after
    pairs = [('burn-scar-1', 'scar'), ('burn-scar-2', 'scar'), ('keloid-1', 'scar'), ('hair-ba-1', 'hair'), ('hair-ba-2', 'hair'),
             ('skin-ba-1', 'pigment'), ('skin-ba-2', 'texture'), ('weight-ba-1', 'body'), ('aesthetics-ba-1', 'texture'), ('scars-ba-1', 'texture')]
    for i, (n, k) in enumerate(pairs):
        write(n + '-before', ba_scene(W4, H4, k, False, 70 + i))
        write(n + '-after', ba_scene(W4, H4, k, True, 70 + i))

if __name__ == '__main__':
    build()
    print(len(os.listdir(ROOT)), 'art files')
