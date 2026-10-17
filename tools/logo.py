"""Logomarca do Carga: um "C" de anilha com um halter subindo e rompendo a abertura.

Gera icon.svg, icon-maskable.svg e a tela de abertura (splash) injetada em app.html
entre <!--SPLASH-START--> e <!--SPLASH-END-->. Os PNG saem de tools/icons.js (Playwright): NODE_PATH=$(npm root -g) node tools/icons.js
Uso: python3 tools/logo.py
Palavra "carga": Inter Display Black Italic (SIL OFL), convertida em contorno.
"""
import math, os, re
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT = '/usr/share/fonts/opentype/inter/InterDisplay-BlackItalic.otf'
G0, G1 = '#6BFFB0', '#10B873'          # degradê da marca (fundo escuro)
B0, B1 = '#22D481', '#0A7A4E'          # fundo do ícone
R, SW, GAP = 172, 72, (36, 324)        # anel do "C"
CX, CY, ANG = 270, 256, -35            # centro e inclinação do halter
BAR, BT, PLATES, KO = 210, 30, [(44, 156), (28, 104)], 16


def arc(cx, cy, r, a0, a1):
    p = lambda a: (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
    (x0, y0), (x1, y1) = p(a0), p(a1)
    return 'M%.1f %.1fA%d %d 0 %d 1 %.1f %.1f' % (x0, y0, r, r, 1 if (a1 - a0) % 360 > 180 else 0, x1, y1)


def dumbbell():
    d = '<rect x="%g" y="%g" width="%g" height="%g" rx="%g"/>' % (-BAR / 2, -BT / 2, BAR, BT, BT / 2)
    x = BAR / 2 - 14
    for w, h in PLATES:
        rx = round(w * .42)
        d += '<rect x="%g" y="%g" width="%g" height="%g" rx="%d"/>' % (x, -h / 2, w, h, rx)
        d += '<rect x="%g" y="%g" width="%g" height="%g" rx="%d"/>' % (-x - w, -h / 2, w, h, rx)
        x += w + 5
    return d


def mark(col, bg=None, ring_cls='', db_cls=''):
    """bg=None recorta o anel com máscara (fundo em degradê); com cor sólida, usa um contorno dessa cor."""
    t = 'translate(%d %d) rotate(%d)' % (CX, CY, ANG)
    db = dumbbell()
    ring = '<path%s d="%s" fill="none" stroke="%s" stroke-width="%d" stroke-linecap="round"%s/>' % (
        ring_cls, arc(256, 256, R, *GAP), col, SW, '' if bg else ' mask="url(#ko)"')
    if bg:
        ko = '<g fill="%s" stroke="%s" stroke-width="%d" stroke-linejoin="round" transform="%s">%s</g>' % (bg, bg, KO * 2, t, db)
        return ring + '<g%s>%s<g fill="%s" transform="%s">%s</g></g>' % (db_cls, ko, col, t, db)
    mask = ('<mask id="ko" maskUnits="userSpaceOnUse" x="0" y="0" width="512" height="512"><rect width="512" height="512" fill="#fff"/>'
            '<g fill="#000" stroke="#000" stroke-width="%d" stroke-linejoin="round" transform="%s">%s</g></mask>' % (KO * 2, t, db))
    return mask + ring + '<g fill="%s" transform="%s">%s</g>' % (col, t, db)


def word(text='carga', track=-30):
    f = TTFont(FONT); gs = f.getGlyphSet(); cmap = f.getBestCmap()
    x, d = 0, ''
    for ch in text:
        g = cmap[ord(ch)]; pen = SVGPathPen(gs, lambda v: '%.0f' % v)
        gs[g].draw(TransformPen(pen, (1, 0, 0, -1, x, 0)))
        d += pen.getCommands(); x += gs[g].width + track
    return d, x - track


def icon(maskable=False, k=None):
    bg = '<defs><linearGradient id="b" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient></defs>' % (B0, B1)
    rect = '<rect width="512" height="512" fill="url(#b)"/>' if maskable else '<rect width="512" height="512" rx="112" fill="url(#b)"/>'
    m = mark('#FFFFFF')
    k = k or (.74 if maskable else .9)  # maskable: a marca cabe na zona segura (círculo de 80%)
    m = '<g transform="translate(256 256) scale(%g) translate(-256 -256)">%s</g>' % (k, m)
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">%s%s%s</svg>' % (bg, rect, m)


def splash():
    # Como no Hevy: só o símbolo, parado, no centro da tela preta
    grad = '<defs><linearGradient id="spg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient></defs>' % (G0, G1)
    return '<div id="splash" aria-hidden="true"><svg class="sp-mark" viewBox="0 0 512 512">%s%s</svg></div>' % (grad, mark('url(#spg)', '#000'))


def lockup():
    """Marca + palavra (arquivo de identidade, para uso fora do app)."""
    wd, ww = word(); k = 300 / 1640
    grad = '<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient></defs>' % (G0, G1)
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d 860"><rect width="100%%" height="100%%" fill="#000"/>%s'
            '<g transform="translate(%g 60)">%s</g><path fill="#fff" transform="translate(40 %g) scale(%g)" d="%s"/></svg>') % (
        ww * k + 80, grad, (ww * k + 80) / 2 - 256, mark('url(#g)', '#000'), 600 + 1180 * k, k, wd)


def main():
    open(os.path.join(ROOT, 'icon.svg'), 'w').write(icon())
    open(os.path.join(ROOT, 'icon-maskable.svg'), 'w').write(icon(True))
    open(os.path.join(ROOT, 'tools', 'logo-carga.svg'), 'w').write(lockup())
    open(os.path.join(ROOT, 'tools', 'icon-apple.svg'), 'w').write(icon(True, .86))  # iOS arredonda sozinho
    p = os.path.join(ROOT, 'app.html'); s = open(p, encoding='utf-8').read()
    s, n = re.subn(r'<!--SPLASH-START-->.*?<!--SPLASH-END-->', lambda _: '<!--SPLASH-START-->' + splash() + '<!--SPLASH-END-->', s, flags=re.S)
    assert n == 1, 'marcadores do splash não encontrados em app.html'
    open(p, 'w', encoding='utf-8').write(s)
    print('ok: icon.svg, icon-maskable.svg, splash')


if __name__ == '__main__':
    main()
