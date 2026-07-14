#!/usr/bin/env python3
"""Generates dark.svg / light.svg — premium GitHub profile hero banner (pure SMIL, no JS)."""
import math, random, re, sys

W, H, RX = 1180, 610, 28
LX, LY, LW, LH = 28, 28, 420, 554          # left card
RCX, RCY, RCW, RCH = 468, 28, 684, 554     # right card
MONO = "'SF Mono','Cascadia Code','Fira Code','JetBrains Mono',Consolas,'DejaVu Sans Mono',monospace"
SANS = "-apple-system,'Segoe UI','Helvetica Neue',Arial,sans-serif"

PAL = {
  'dark': dict(
    bg='#030712', panel='#0F172A', panel2='#131E36',
    border='rgba(255,255,255,0.08)', borderCard='rgba(255,255,255,0.09)',
    text='#F8FAFC', muted='#94A3B8', faint='#64748B',
    a1='#7C3AED', a2='#22D3EE', a3='#10B981',
    asciiA='#22D3EE', asciiB='#7C3AED', asciiC='#10B981',
    link='#22D3EE',
    pillFill='rgba(255,255,255,0.045)', pillStroke='rgba(255,255,255,0.13)', pillText='#CBD5E1',
    headFill='rgba(255,255,255,0.03)', divFull='rgba(255,255,255,0.06)',
    divCol='#FFFFFF', divOp='0.18',
    glassCol='#FFFFFF', glassOp='0.07',
    sheenCol='#FFFFFF', sheenOp='0.06',
    scanCol='#FFFFFF', scanOp='0.045',
    stripeCol='#FFFFFF', stripeOp='0.05',
    bandCol='#22D3EE', bandOp='0.11',
    blobOps=('0.17', '0.14', '0.11'), auraOps='0.10;0.20;0.10',
    shCol='#000000', shOp='0.5', shStd='16', shDy='14',
    noiseC='1', noiseA='0.05', panelOp='0.88',
    shimOp='0.75',
  ),
  'light': dict(
    bg='#FFFFFF', panel='#F8FAFC', panel2='#F1F5F9',
    border='rgba(15,23,42,0.08)', borderCard='rgba(15,23,42,0.09)',
    text='#0F172A', muted='#475569', faint='#64748B',
    a1='#2563EB', a2='#06B6D4', a3='#10B981',
    asciiA='#2563EB', asciiB='#06B6D4', asciiC='#10B981',
    link='#2563EB',
    pillFill='rgba(15,23,42,0.035)', pillStroke='rgba(15,23,42,0.11)', pillText='#334155',
    headFill='rgba(15,23,42,0.025)', divFull='rgba(15,23,42,0.06)',
    divCol='#0F172A', divOp='0.14',
    glassCol='#FFFFFF', glassOp='0.55',
    sheenCol='#2563EB', sheenOp='0.045',
    scanCol='#2563EB', scanOp='0.035',
    stripeCol='#0F172A', stripeOp='0.055',
    bandCol='#2563EB', bandOp='0.07',
    blobOps=('0.08', '0.07', '0.06'), auraOps='0.04;0.09;0.04',
    shCol='#475569', shOp='0.14', shStd='12', shDy='8',
    noiseC='0', noiseA='0.03', panelOp='0.92',
    shimOp='0.5',
  ),
}

NAME = "Abhinand SD"
ROLES = ["Software Engineer", "Full Stack Developer", "Open Source Contributor", "UI Engineer", "AI Enthusiast"]
ROWS = [
  ('pin',    'location',  'Bangalore, India',        False),
  ('cap',    'education', 'B.Tech CSE',              False),
  ('target', 'focus',     'Software Development',    False),
  ('globe',  'portfolio', 'abhinandsdin.vercel.app', True),
  ('mail',   'email',     'abhinandsd49@gmail.com',  True),
]
SKILLS = ["React", "Next.js", "Node.js", "TypeScript", "Tailwind", "Python", "Docker", "Postgres", "AWS", "Git", "Figma"]

GH = "M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"
LI = "M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.225 0z"
XP = "M18.901 1.153h3.68l-8.04 9.19L24 22.846h-7.406l-5.8-7.584-6.638 7.584H.474l8.6-9.83L0 1.154h7.594l5.243 6.932ZM17.61 20.644h2.039L6.486 3.24H4.298Z"

EASE = 'calcMode="spline" keySplines="0.25 0.6 0.3 1" keyTimes="0;1"'

def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

# ---------------------------------------------------------------- ASCII portrait
def ascii_portrait(cols=36, rows=24):
    chars = " .:-=+*#%@"
    rnd = random.Random(7)
    out = []
    def ring(nx, ny, cx, cy, rx, ry, wd):
        d = math.hypot((nx - cx) / rx, (ny - cy) / ry)
        return math.exp(-((d - 1.0) / wd) ** 2)
    for r in range(rows):
        ny = (r / (rows - 1)) * 2 - 1
        line = ''
        for c in range(cols):
            nx = (c / (cols - 1)) * 2 - 1
            b = 0.0
            b += 1.15 * ring(nx, ny, 0, -0.16, 0.60, 0.66, 0.13)     # hood outline
            b += 0.20 * ring(nx, ny, 0, -0.16, 0.47, 0.52, 0.12)     # inner rim glow
            for ex in (-0.24, 0.24):                                  # eyes
                gx = (nx - ex) / 0.13
                gy = (ny + 0.22) / 0.06
                b += 1.7 * math.exp(-(gx * gx + gy * gy))
            gx = nx / 0.15                                            # mouth
            gy = (ny - 0.16) / 0.04
            b += 0.55 * math.exp(-(gx * gx + gy * gy))
            if ny > 0.50:                                             # shoulders
                b += 1.0 * ring(nx, ny, 0, 1.32, 0.95, 0.60, 0.11)
            b += rnd.uniform(-0.02, 0.02)
            b = max(0.0, min(1.0, b))
            idx = 0 if b < 0.055 else int(round(b * 9))
            line += chars[min(idx, 9)]
        out.append(line)
    while out and not out[0].strip():                                 # trim blank edges
        out.pop(0)
    while out and not out[-1].strip():
        out.pop()
    return out

# ---------------------------------------------------------------- helpers
def reveal(t, inner, dy=10, dur=0.5, debug=False):
    """Fade + rise entrance."""
    if debug:
        return f'<g>{inner}</g>'
    t = round(t, 3)
    return (f'<g opacity="0" transform="translate(0,{dy})">'
            f'<animate attributeName="opacity" values="0;1" dur="{dur}s" begin="{t:g}s" fill="freeze" {EASE}/>'
            f'<animateTransform attributeName="transform" type="translate" values="0,{dy};0,0" dur="{dur + 0.1:g}s" begin="{t:g}s" fill="freeze" {EASE}/>'
            f'{inner}</g>')

def reveal_x(t, inner, dx=-10, dur=0.5, debug=False):
    if debug:
        return f'<g>{inner}</g>'
    t = round(t, 3)
    return (f'<g opacity="0" transform="translate({dx},0)">'
            f'<animate attributeName="opacity" values="0;1" dur="{dur}s" begin="{t:g}s" fill="freeze" {EASE}/>'
            f'<animateTransform attributeName="transform" type="translate" values="{dx},0;0,0" dur="{dur + 0.1:g}s" begin="{t:g}s" fill="freeze" {EASE}/>'
            f'{inner}</g>')

def type_vals(n, cw, reverse=False):
    seq = [f'{i * cw:g}' for i in range(n + 1)]
    if reverse:
        seq.reverse()
    return ';'.join(seq)

# ---------------------------------------------------------------- build
def build(theme, debug=False):
    p = PAL[theme]
    A = []
    A.append('<?xml version="1.0" encoding="UTF-8"?>')
    A.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{NAME} — Software Engineer">')
    A.append(f'<title>{NAME} — Software Engineer</title>')

    # ============================================================ defs
    d = ['<defs>']
    d.append(f'<clipPath id="rootClip"><rect x="0" y="0" width="{W}" height="{H}" rx="{RX}"/></clipPath>')
    d.append(f'<clipPath id="clipL"><rect x="{LX}" y="{LY}" width="{LW}" height="{LH}" rx="20"/></clipPath>')
    d.append(f'<clipPath id="clipR"><rect x="{RCX}" y="{RCY}" width="{RCW}" height="{RCH}" rx="20"/></clipPath>')

    # accent gradient (animated hue cycle)
    def cyc(c1, c2, c3, dur):
        return (f'<stop offset="0" stop-color="{c1}"><animate attributeName="stop-color" values="{c1};{c2};{c3};{c1}" dur="{dur}s" repeatCount="indefinite"/></stop>'
                f'<stop offset="0.5" stop-color="{c2}"><animate attributeName="stop-color" values="{c2};{c3};{c1};{c2}" dur="{dur}s" repeatCount="indefinite"/></stop>'
                f'<stop offset="1" stop-color="{c3}"><animate attributeName="stop-color" values="{c3};{c1};{c2};{c3}" dur="{dur}s" repeatCount="indefinite"/></stop>')
    d.append(f'<linearGradient id="accent" x1="0" y1="0" x2="1" y2="0">{cyc(p["a1"], p["a2"], p["a3"], 9)}</linearGradient>')
    d.append(f'<linearGradient id="agrad" gradientUnits="userSpaceOnUse" x1="78" y1="100" x2="398" y2="460">{cyc(p["asciiA"], p["asciiB"], p["asciiC"], 12)}</linearGradient>')

    d.append(f'<linearGradient id="panelG" x1="0" y1="0" x2="0" y2="1">'
             f'<stop offset="0" stop-color="{p["panel2"]}"/><stop offset="1" stop-color="{p["panel"]}"/></linearGradient>')
    d.append(f'<linearGradient id="glassG" x1="0" y1="0" x2="0" y2="1">'
             f'<stop offset="0" stop-color="{p["glassCol"]}" stop-opacity="{p["glassOp"]}"/>'
             f'<stop offset="1" stop-color="{p["glassCol"]}" stop-opacity="0"/></linearGradient>')
    d.append(f'<linearGradient id="sheenG" x1="0" y1="0" x2="1" y2="0">'
             f'<stop offset="0" stop-color="{p["sheenCol"]}" stop-opacity="0"/>'
             f'<stop offset="0.5" stop-color="{p["sheenCol"]}" stop-opacity="{p["sheenOp"]}"/>'
             f'<stop offset="1" stop-color="{p["sheenCol"]}" stop-opacity="0"/></linearGradient>')
    d.append(f'<linearGradient id="scanG" x1="0" y1="0" x2="0" y2="1">'
             f'<stop offset="0" stop-color="{p["scanCol"]}" stop-opacity="0"/>'
             f'<stop offset="0.5" stop-color="{p["scanCol"]}" stop-opacity="{p["scanOp"]}"/>'
             f'<stop offset="1" stop-color="{p["scanCol"]}" stop-opacity="0"/></linearGradient>')
    d.append(f'<linearGradient id="bandG" x1="0" y1="0" x2="0" y2="1">'
             f'<stop offset="0" stop-color="{p["bandCol"]}" stop-opacity="0"/>'
             f'<stop offset="0.5" stop-color="{p["bandCol"]}" stop-opacity="{p["bandOp"]}"/>'
             f'<stop offset="1" stop-color="{p["bandCol"]}" stop-opacity="0"/></linearGradient>')
    d.append(f'<linearGradient id="divG" x1="0" y1="0" x2="1" y2="0">'
             f'<stop offset="0" stop-color="{p["divCol"]}" stop-opacity="0"/>'
             f'<stop offset="0.5" stop-color="{p["divCol"]}" stop-opacity="{p["divOp"]}"/>'
             f'<stop offset="1" stop-color="{p["divCol"]}" stop-opacity="0"/></linearGradient>')

    shim = ('' if debug else '<animateTransform attributeName="gradientTransform" type="translate" values="-1300,0;1300,0" dur="6s" repeatCount="indefinite"/>')
    d.append(f'<linearGradient id="shimmer" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="1180" y2="80">'
             f'<stop offset="0.35" stop-color="{p["a2"]}" stop-opacity="0"/>'
             f'<stop offset="0.5" stop-color="{p["a2"]}" stop-opacity="{p["shimOp"]}"/>'
             f'<stop offset="0.65" stop-color="{p["a2"]}" stop-opacity="0"/>{shim}</linearGradient>')

    for i, (col, op) in enumerate(zip((p['a1'], p['a2'], p['a3']), p['blobOps'])):
        d.append(f'<radialGradient id="blob{i}"><stop offset="0" stop-color="{col}" stop-opacity="{op}"/>'
                 f'<stop offset="1" stop-color="{col}" stop-opacity="0"/></radialGradient>')
    d.append(f'<radialGradient id="auraG"><stop offset="0" stop-color="{p["a2"]}" stop-opacity="0.7"/>'
             f'<stop offset="1" stop-color="{p["a2"]}" stop-opacity="0"/></radialGradient>')

    d.append('<filter id="softGlow" x="-40%" y="-40%" width="180%" height="180%">'
             '<feGaussianBlur stdDeviation="6" result="b"/>'
             '<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>')
    d.append('<filter id="asciiGlow" x="-25%" y="-25%" width="150%" height="150%">'
             '<feGaussianBlur stdDeviation="2.2" result="b"/>'
             '<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>')
    d.append(f'<filter id="cardShadow" x="-15%" y="-15%" width="130%" height="140%">'
             f'<feGaussianBlur in="SourceAlpha" stdDeviation="{p["shStd"]}"/>'
             f'<feOffset dy="{p["shDy"]}" result="ob"/>'
             f'<feFlood flood-color="{p["shCol"]}" flood-opacity="{p["shOp"]}"/>'
             f'<feComposite in2="ob" operator="in" result="sh"/>'
             f'<feMerge><feMergeNode in="sh"/><feMergeNode in="SourceGraphic"/></feMerge></filter>')
    d.append(f'<filter id="noiseF" x="0" y="0" width="100%" height="100%">'
             f'<feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" stitchTiles="stitch" result="n"/>'
             f'<feColorMatrix in="n" type="matrix" values="0 0 0 0 {p["noiseC"]}  0 0 0 0 {p["noiseC"]}  0 0 0 0 {p["noiseC"]}  0 0 0 {p["noiseA"]} 0"/></filter>')

    # ---- ASCII line clips
    art = ascii_portrait()
    art_lh, art_cx = 15, LX + LW / 2
    art_y0 = 100 + (24 - len(art)) * art_lh / 2   # vertically center trimmed art
    for i in range(len(art)):
        y = art_y0 + i * art_lh
        if debug:
            d.append(f'<clipPath id="al{i}"><rect x="78" y="{y - 13:g}" width="320" height="16"/></clipPath>')
        else:
            d.append(f'<clipPath id="al{i}"><rect x="78" y="{y - 13:g}" width="0" height="16">'
                     f'<animate attributeName="width" values="{type_vals(10, 32)}" dur="0.32s" begin="{0.8 + i * 0.095:.3f}s" fill="freeze" calcMode="discrete"/></rect></clipPath>')

    # ---- whoami clip
    if debug:
        d.append('<clipPath id="wc"><rect x="518" y="92" width="49" height="17"/></clipPath>')
    else:
        d.append(f'<clipPath id="wc"><rect x="518" y="92" width="0" height="17">'
                 f'<animate id="wt" attributeName="width" values="{type_vals(6, 8.1)}" dur="0.5s" begin="1.1s" fill="freeze" calcMode="discrete"/></rect></clipPath>')

    # ---- role phrase clips + chained typing/deleting
    r_cw, r_x = 9, 522
    for i, ph in enumerate(ROLES):
        n = len(ph)
        if debug:
            w0 = n * r_cw if i == 0 else 0
            d.append(f'<clipPath id="pc{i}"><rect x="520" y="205" width="{w0}" height="19"/></clipPath>')
            continue
        tb = '2.7s;d4.end+0.45s' if i == 0 else f'd{i - 1}.end+0.35s'
        tdur = max(0.4, n * 0.055)
        ddur = max(0.3, n * 0.028)
        d.append(f'<clipPath id="pc{i}"><rect x="520" y="205" width="0" height="19">'
                 f'<animate id="t{i}" attributeName="width" values="{type_vals(n, r_cw)}" dur="{tdur:.3f}s" begin="{tb}" fill="freeze" calcMode="discrete"/>'
                 f'<animate id="d{i}" attributeName="width" values="{type_vals(n, r_cw, True)}" dur="{ddur:.3f}s" begin="t{i}.end+1.6s" fill="freeze" calcMode="discrete"/>'
                 f'</rect></clipPath>')

    # ---- footer typing clip
    FOOT = './render --portrait'
    fn = len(FOOT)
    f_cw = 7.5
    if debug:
        d.append(f'<clipPath id="fc"><rect x="66" y="506" width="{fn * f_cw:g}" height="18"/></clipPath>')
    else:
        d.append(f'<clipPath id="fc"><rect x="66" y="506" width="0" height="18">'
                 f'<animate id="ft" attributeName="width" values="{type_vals(fn, f_cw)}" dur="1.05s" begin="3.6s" fill="freeze" calcMode="discrete"/></rect></clipPath>')

    d.append('</defs>')
    A.extend(d)

    # ============================================================ scene
    A.append('<g clip-path="url(#rootClip)">')
    A.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="{p["bg"]}"/>')

    # floating background blobs
    blob_geo = [(160, 120, 280, '0,0;70,45;-25,80;0,0', 27), (1030, 130, 260, '0,0;-60,70;30,110;0,0', 32), (640, 590, 270, '0,0;-80,-40;60,-70;0,0', 24)]
    for i, (bx, by, br, vals, dur) in enumerate(blob_geo):
        anim = '' if debug else f'<animateTransform attributeName="transform" type="translate" values="{vals}" keyTimes="0;0.35;0.7;1" dur="{dur}s" repeatCount="indefinite"/>'
        A.append(f'<circle cx="{bx}" cy="{by}" r="{br}" fill="url(#blob{i})">{anim}</circle>')

    # glow pulse behind portrait
    aura_anim = '' if debug else f'<animate attributeName="opacity" values="{p["auraOps"]}" dur="7s" repeatCount="indefinite"/>'
    A.append(f'<circle cx="238" cy="300" r="185" fill="url(#auraG)" opacity="{p["auraOps"].split(";")[0]}">{aura_anim}</circle>')

    # particles
    prt = [(95, 515, 1.6, 'a2', 16), (340, 88, 1.3, 'a1', 21), (556, 300, 1.8, 'a3', 18), (724, 78, 1.4, 'a2', 24),
           (884, 470, 1.9, 'a1', 19), (1098, 318, 1.5, 'a3', 26), (1032, 556, 1.3, 'a2', 22), (204, 296, 1.2, 'a1', 28), (648, 540, 1.5, 'a2', 20)]
    for i, (px, py, pr, pc, pdur) in enumerate(prt):
        tw = '' if debug else (f'<animate attributeName="opacity" values="0.15;0.7;0.15" dur="{pdur / 4:.1f}s" repeatCount="indefinite"/>'
                               f'<animateMotion path="M0 0 c 18 -24 42 -8 27 13 c -11 17 -36 9 -27 -13 z" dur="{pdur}s" repeatCount="indefinite"/>')
        A.append(f'<circle cx="{px}" cy="{py}" r="{pr}" fill="{p[pc]}" opacity="0.4">{tw}</circle>')

    # ============================================================ LEFT CARD
    left = []
    left.append(f'<rect x="{LX}" y="{LY}" width="{LW}" height="{LH}" rx="20" fill="url(#panelG)" fill-opacity="{p["panelOp"]}" stroke="{p["borderCard"]}" stroke-width="1" filter="url(#cardShadow)"/>')
    left.append(f'<g clip-path="url(#clipL)"><rect x="{LX + 1}" y="{LY + 1}" width="{LW - 2}" height="130" rx="19" fill="url(#glassG)"/></g>')
    # header
    left.append(f'<text x="52" y="61" font-family="{MONO}" font-size="12" fill="{p["faint"]}">// ascii · portrait</text>')
    live_pulse = '' if debug else '<animate attributeName="opacity" values="1;0.25;1" dur="1.6s" repeatCount="indefinite"/>'
    left.append(f'<circle cx="416" cy="57" r="3" fill="{p["a3"]}">{live_pulse}</circle>')
    left.append(f'<text x="408" y="61" text-anchor="end" font-family="{MONO}" font-size="10.5" fill="{p["a3"]}" opacity="0.85">live</text>')

    # ascii art (glow filter outside, float inside)
    flt = '' if debug else '<animateTransform attributeName="transform" type="translate" values="0,0;0,-6;0,0" dur="6.5s" calcMode="spline" keySplines="0.4 0 0.6 1;0.4 0 0.6 1" keyTimes="0;0.5;1" repeatCount="indefinite"/>'
    lines = []
    for i, ln in enumerate(art):
        y = art_y0 + i * art_lh
        lines.append(f'<g clip-path="url(#al{i})"><text x="{art_cx:g}" y="{y:g}" text-anchor="middle" xml:space="preserve" font-family="{MONO}" font-size="14" font-weight="600" textLength="302.4" lengthAdjust="spacing" fill="url(#agrad)">{esc(ln)}</text></g>')
    left.append(f'<g filter="url(#asciiGlow)"><g>{flt}{"".join(lines)}</g></g>')

    # scanlines + moving band over art
    stripes = ''.join(f'<rect x="84" y="{yy}" width="308" height="1" fill="{p["stripeCol"]}" opacity="{p["stripeOp"]}"/>' for yy in range(96, 456, 18))
    left.append(f'<g>{stripes}</g>')
    band_anim = '' if debug else '<animate attributeName="y" values="92;428;92" dur="6s" repeatCount="indefinite"/>'
    left.append(f'<rect x="80" y="92" width="316" height="26" fill="url(#bandG)">{band_anim}</rect>')

    # footer typed command
    left.append(f'<text x="52" y="520" font-family="{MONO}" font-size="12.5" fill="{p["a3"]}">$</text>')
    left.append(f'<g clip-path="url(#fc)"><text x="66" y="520" font-family="{MONO}" font-size="12.5" xml:space="preserve" textLength="{fn * f_cw:g}" lengthAdjust="spacing" fill="{p["muted"]}">{esc(FOOT)}</text></g>')
    ok_t = reveal(4.85, f'<text x="216" y="520" font-family="{MONO}" font-size="12.5" fill="{p["a3"]}">✓</text>', dy=0, dur=0.4, debug=debug)
    left.append(ok_t)
    if debug:
        left.append(f'<rect x="{66 + fn * f_cw + 4:g}" y="508" width="7.5" height="14" fill="{p["a2"]}" opacity="0.85"/>')
    else:
        left.append(f'<g opacity="0"><animate attributeName="opacity" values="0;1" dur="0.1s" begin="3.6s" fill="freeze"/>'
                    f'<rect x="66" y="508" width="7.5" height="14" fill="{p["a2"]}" opacity="0.85">'
                    f'<animate attributeName="x" values="{";".join(f"{66 + k * f_cw + 4:g}" for k in range(fn + 1))}" dur="1.05s" begin="ft.begin" fill="freeze" calcMode="discrete"/>'
                    f'<animate attributeName="opacity" values="0.85;0" dur="1.1s" begin="4.7s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.5"/></rect></g>')

    # sheen sweep
    if not debug:
        left.append(f'<g clip-path="url(#clipL)"><rect x="-140" y="{LY - 40}" width="120" height="{LH + 80}" fill="url(#sheenG)" transform="skewX(-18)">'
                    f'<animateTransform attributeName="transform" type="translate" additive="sum" values="0,0;760,0;760,0" keyTimes="0;0.3;1" dur="9s" begin="2s" repeatCount="indefinite"/></rect></g>')
    A.append(reveal(0.2, ''.join(left), dy=14, dur=0.7, debug=debug))

    # ============================================================ RIGHT CARD
    right = []
    right.append(f'<rect x="{RCX}" y="{RCY}" width="{RCW}" height="{RCH}" rx="20" fill="url(#panelG)" fill-opacity="{p["panelOp"]}" stroke="{p["borderCard"]}" stroke-width="1" filter="url(#cardShadow)"/>')
    right.append(f'<g clip-path="url(#clipR)"><rect x="{RCX + 1}" y="{RCY + 1}" width="{RCW - 2}" height="44" fill="{p["headFill"]}"/>'
                 f'<rect x="{RCX + 1}" y="{RCY + 1}" width="{RCW - 2}" height="120" rx="19" fill="url(#glassG)" opacity="0.6"/></g>')
    # traffic lights + title
    for j, dc in enumerate(('#FF5F57', '#FEBC2E', '#28C840')):
        right.append(f'<circle cx="{494 + j * 17}" cy="50" r="5" fill="{dc}" opacity="0.95"/>')
    right.append(f'<text x="810" y="54" text-anchor="middle" font-family="{MONO}" font-size="11.5" fill="{p["faint"]}">abhinand@dev: ~/portfolio — zsh</text>')
    right.append(f'<rect x="{RCX + 1}" y="71" width="{RCW - 2}" height="1" fill="{p["divFull"]}"/>')

    # $ whoami
    right.append(f'<text x="502" y="105" font-family="{MONO}" font-size="13.5" fill="{p["a3"]}">$</text>')
    right.append(f'<g clip-path="url(#wc)"><text x="518" y="105" font-family="{MONO}" font-size="13.5" textLength="48.6" lengthAdjust="spacing" fill="{p["muted"]}">whoami</text></g>')
    if debug:
        right.append(f'<rect x="570" y="93" width="8" height="14" fill="{p["a2"]}" opacity="0.85"/>')
    else:
        right.append(f'<g><animate attributeName="opacity" values="1;0" dur="0.2s" begin="1.85s" fill="freeze"/>'
                     f'<rect x="521" y="93" width="8" height="14" fill="{p["a2"]}" opacity="0.85">'
                     f'<animate attributeName="x" values="{";".join(f"{518 + k * 8.1 + 3:g}" for k in range(7))}" dur="0.5s" begin="wt.begin" fill="freeze" calcMode="discrete"/>'
                     f'<animate attributeName="opacity" values="0.85;0" dur="1.1s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.5"/></rect></g>')

    # greeting + name
    right.append(reveal(1.8, f'<text x="502" y="143" font-family="{MONO}" font-size="15" fill="{p["muted"]}">Hi 👋, I&#39;m</text>', dy=8, debug=debug))
    right.append(reveal(2.05, f'<text x="500" y="185" font-family="{SANS}" font-size="34" font-weight="800" letter-spacing="-0.5" fill="url(#accent)" filter="url(#softGlow)">{NAME}</text>', dy=12, dur=0.6, debug=debug))

    # animated roles
    roles_g = [f'<text x="502" y="220" font-family="{MONO}" font-size="15" font-weight="700" fill="url(#accent)">❯</text>']
    for i, ph in enumerate(ROLES):
        roles_g.append(f'<g clip-path="url(#pc{i})"><text x="{r_x}" y="220" font-family="{MONO}" font-size="15" font-weight="500" textLength="{len(ph) * r_cw:g}" lengthAdjust="spacing" fill="{p["text"]}">{esc(ph)}</text></g>')
    if debug:
        roles_g.append(f'<rect x="{r_x + len(ROLES[0]) * r_cw + 3:g}" y="206" width="8.5" height="16" fill="{p["a2"]}" opacity="0.9"/>')
    else:
        cursor_anims = []
        for i, ph in enumerate(ROLES):
            n = len(ph)
            tdur = max(0.4, n * 0.055)
            ddur = max(0.3, n * 0.028)
            cursor_anims.append(f'<animate attributeName="x" values="{";".join(f"{r_x + k * r_cw + 3:g}" for k in range(n + 1))}" dur="{tdur:.3f}s" begin="t{i}.begin" fill="freeze" calcMode="discrete"/>')
            cursor_anims.append(f'<animate attributeName="x" values="{";".join(f"{r_x + k * r_cw + 3:g}" for k in range(n, -1, -1))}" dur="{ddur:.3f}s" begin="d{i}.begin" fill="freeze" calcMode="discrete"/>')
        roles_g.append(f'<rect x="{r_x + 3}" y="206" width="8.5" height="16" fill="{p["a2"]}" opacity="0.9">{"".join(cursor_anims)}'
                       f'<animate attributeName="opacity" values="0.9;0" dur="1.05s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.55"/></rect>')
    right.append(reveal(2.55, ''.join(roles_g), dy=6, debug=debug))

    # dividers
    def divider(x, y, w, t):
        if debug:
            return f'<rect x="{x}" y="{y}" width="{w}" height="1" fill="url(#divG)"/>'
        return (f'<g transform="translate({x},{y})"><g transform="scale(0,1)">'
                f'<animateTransform attributeName="transform" type="scale" values="0,1;1,1" dur="0.7s" begin="{t}s" fill="freeze" {EASE}/>'
                f'<rect x="0" y="0" width="{w}" height="1" fill="url(#divG)"/></g></g>')
    right.append(divider(502, 243, 616, 2.5))

    # info rows
    icons16 = {
      'pin':    '<path d="M8 1.8C5.5 1.8 3.5 3.8 3.5 6.3 3.5 9.6 8 14.2 8 14.2s4.5-4.6 4.5-7.9C12.5 3.8 10.5 1.8 8 1.8Z"/><circle cx="8" cy="6.2" r="1.7"/>',
      'cap':    '<path d="M1.5 5.8 8 2.6l6.5 3.2L8 9 1.5 5.8Z"/><path d="M4.2 7.3v3.2c0 .9 1.7 1.9 3.8 1.9s3.8-1 3.8-1.9V7.3"/><path d="M14.5 5.8v3.4"/>',
      'target': f'<circle cx="8" cy="8" r="5.6"/><circle cx="8" cy="8" r="2" fill="{p["a2"]}" stroke="none"/>',
      'globe':  '<circle cx="8" cy="8" r="5.8"/><ellipse cx="8" cy="8" rx="2.6" ry="5.8"/><path d="M2.2 8h11.6"/>',
      'mail':   '<rect x="2" y="3.5" width="12" height="9" rx="1.6"/><path d="m2.5 4.5 5.5 4 5.5-4"/>',
    }
    for i, (ic, key, val, is_link) in enumerate(ROWS):
        y = 272 + i * 31
        vcol = p['link'] if is_link else p['text']
        row = (f'<g transform="translate(502,{y - 12})" fill="none" stroke="{p["a2"]}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" opacity="0.85">{icons16[ic]}</g>'
               f'<text x="530" y="{y}" font-family="{MONO}" font-size="13" fill="{p["muted"]}">{key}</text>'
               f'<text x="632" y="{y}" font-family="{MONO}" font-size="13" font-weight="500" fill="{vcol}">{esc(val)}</text>')
        right.append(reveal_x(2.9 + i * 0.3, row, dx=-12, debug=debug))
    right.append(divider(502, 419, 616, 4.25))

    # skills
    right.append(reveal(4.45, f'<text x="502" y="444" font-family="{MONO}" font-size="12" fill="{p["faint"]}">~ stack</text>', dy=6, debug=debug))
    px_, py_ = 502, 469
    pill_i = 0
    pills = []
    for label in SKILLS:
        w = len(label) * 7.2 + 26
        if px_ + w > RCX + RCW - 30:
            px_, py_ = 502, py_ + 34
        cx = px_ + w / 2
        t = 4.55 + pill_i * 0.07
        hover = (f'<animateTransform attributeName="transform" type="scale" values="1;1.07" dur="0.18s" begin="pill{pill_i}.mouseover" fill="freeze" {EASE}/>'
                 f'<animateTransform attributeName="transform" type="scale" values="1.07;1" dur="0.22s" begin="pill{pill_i}.mouseout" fill="freeze" {EASE}/>')
        stroke_h = (f'<animate attributeName="stroke" values="{p["pillStroke"]};{p["a2"]}" dur="0.18s" begin="pill{pill_i}.mouseover" fill="freeze"/>'
                    f'<animate attributeName="stroke" values="{p["a2"]};{p["pillStroke"]}" dur="0.25s" begin="pill{pill_i}.mouseout" fill="freeze"/>')
        body = (f'<rect x="{-w / 2:g}" y="-14" width="{w:g}" height="28" rx="14" fill="{p["pillFill"]}" stroke="{p["pillStroke"]}" stroke-width="1">{stroke_h if not debug else ""}</rect>'
                f'<text x="0" y="4.5" text-anchor="middle" font-family="{MONO}" font-size="12" font-weight="500" fill="{p["pillText"]}">{esc(label)}</text>')
        if debug:
            pills.append(f'<g id="pill{pill_i}" transform="translate({cx:g},{py_})"><g>{body}</g></g>')
        else:
            pills.append(f'<g id="pill{pill_i}" transform="translate({cx:g},{py_})"><g>{hover}'
                         f'<g opacity="0" transform="scale(0.6)">'
                         f'<animate attributeName="opacity" values="0;1" dur="0.3s" begin="{t:.2f}s" fill="freeze"/>'
                         f'<animateTransform attributeName="transform" type="scale" values="0.6;1.05;1" keyTimes="0;0.7;1" dur="0.45s" begin="{t:.2f}s" fill="freeze" calcMode="spline" keySplines="0.2 0.7 0.3 1;0.4 0 0.6 1"/>'
                         f'{body}</g></g></g>')
        px_ += w + 10
        pill_i += 1
    right.append(''.join(pills))

    # social icons
    socials = [('gh', GH), ('li', LI), ('x', XP), ('web', None)]
    for i, (nm, pth) in enumerate(socials):
        cx = 519 + i * 50
        t = 5.5 + i * 0.12
        if pth:
            hover_fill = ('' if debug else f'<animate attributeName="fill" values="{p["muted"]};{p["a2"]}" dur="0.18s" begin="soc{i}.mouseover" fill="freeze"/>'
                                           f'<animate attributeName="fill" values="{p["a2"]};{p["muted"]}" dur="0.25s" begin="soc{i}.mouseout" fill="freeze"/>')
            inner_icon = f'<g transform="translate(-9,-9) scale(0.75)"><path d="{pth}" fill="{p["muted"]}">{hover_fill}</path></g>'
        else:
            inner_icon = (f'<g fill="none" stroke="{p["muted"]}" stroke-width="1.6"><circle cx="0" cy="0" r="7.2"/>'
                          f'<ellipse cx="0" cy="0" rx="3.2" ry="7.2"/><path d="M-7 0h14"/></g>')
        pulse = '' if debug else (f'<circle r="17" fill="none" stroke="{p["a2"]}" stroke-opacity="0">'
                                  f'<animate attributeName="stroke-opacity" values="0;0.4;0" keyTimes="0;0.15;0.6" dur="3.6s" begin="{6 + i * 0.9:g}s" repeatCount="indefinite"/>'
                                  f'<animate attributeName="r" values="17;21.5" dur="3.6s" begin="{6 + i * 0.9:g}s" repeatCount="indefinite"/></circle>')
        hover = '' if debug else (f'<animateTransform attributeName="transform" type="scale" values="1;1.1" dur="0.18s" begin="soc{i}.mouseover" fill="freeze" {EASE}/>'
                                  f'<animateTransform attributeName="transform" type="scale" values="1.1;1" dur="0.22s" begin="soc{i}.mouseout" fill="freeze" {EASE}/>')
        icon = (f'<g id="soc{i}" transform="translate({cx},546)"><g>{hover}'
                f'<circle r="17" fill="{p["pillFill"]}" stroke="{p["pillStroke"]}" stroke-width="1"/>{pulse}{inner_icon}</g></g>')
        right.append(reveal(t, icon, dy=8, debug=debug))

    # sheen sweep (right)
    if not debug:
        right.append(f'<g clip-path="url(#clipR)"><rect x="240" y="{RCY - 40}" width="130" height="{RCH + 80}" fill="url(#sheenG)" transform="skewX(-18)">'
                     f'<animateTransform attributeName="transform" type="translate" additive="sum" values="0,0;1030,0;1030,0" keyTimes="0;0.32;1" dur="10s" begin="4.5s" repeatCount="indefinite"/></rect></g>')
    A.append(reveal(0.35, ''.join(right), dy=14, dur=0.7, debug=debug))

    # ============================================================ overlays
    if not debug:
        A.append(f'<rect x="0" y="-130" width="{W}" height="110" fill="url(#scanG)">'
                 f'<animateTransform attributeName="transform" type="translate" values="0,0;0,760" dur="10s" repeatCount="indefinite"/></rect>')
        A.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="#ffffff" fill-opacity="0" filter="url(#noiseF)"/>')
    A.append('</g>')  # end rootClip

    # border + shimmer
    A.append(f'<rect x="0.75" y="0.75" width="{W - 1.5}" height="{H - 1.5}" rx="{RX - 0.75}" fill="none" stroke="{p["border"]}" stroke-width="1.5"/>')
    A.append(f'<rect x="0.75" y="0.75" width="{W - 1.5}" height="{H - 1.5}" rx="{RX - 0.75}" fill="none" stroke="url(#shimmer)" stroke-width="1.5"/>')
    A.append('</svg>')
    return ''.join(A)

# ---------------------------------------------------------------- validate
def validate(svg):
    import xml.etree.ElementTree as ET
    ET.fromstring(svg)
    ids = set(re.findall(r'id="([^"]+)"', svg))
    for ref in re.findall(r'begin="([^"]+)"', svg):
        for tok in ref.split(';'):
            m = re.match(r'\s*([A-Za-z_][\w-]*)\.(end|begin|mouseover|mouseout)', tok)
            if m and m.group(1) not in ids:
                raise SystemExit(f'ERROR: begin references missing id: {m.group(1)}')
    for ref in set(re.findall(r'url\(#([^)]+)\)', svg)):
        if ref not in ids:
            raise SystemExit(f'ERROR: url references missing id: {ref}')
    dup = [i for i in ids if svg.count(f'id="{i}"') > 1]
    if dup:
        raise SystemExit(f'ERROR: duplicate ids: {dup}')

if __name__ == '__main__':
    if '--art' in sys.argv:
        print('\n'.join(ascii_portrait()))
        sys.exit(0)
    for th in ('dark', 'light'):
        s = build(th)
        validate(s)
        open(f'{th}.svg', 'w', encoding='utf-8').write(s)
        open(f'{th}_debug.svg', 'w', encoding='utf-8').write(build(th, debug=True))
        print(f'{th}.svg  {len(s)} bytes  OK')
# eof
