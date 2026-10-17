"""Mapa corporal hiper-realista a partir das artes em tools/musculos/<grupo>.webp.

Cada arte traz as 4 figuras (homem frente/costas, mulher frente/costas) sobre a mesma base cinza,
com um grupo muscular pintado de verde. O script:
  1. tira a base limpa pela mediana das artes (o verde de cada uma some na mediana);
  2. recorta as 4 figuras com fundo transparente -> img/body-{mf,mb,ff,fb}.webp;
  3. detecta o verde de cada arte, vetoriza por figura e injeta os caminhos em app.html
     entre /*BODY-START*/ e /*BODY-END*/ (o app pinta esses caminhos na cor de destaque).
Uso: python3 tools/build_body.py
"""
import json, os, re, glob
import numpy as np, cv2
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'tools', 'musculos')
NAMES = {  # arquivo -> grupo muscular do app
    'peito': 'Peito', 'costas-superiores': 'Costas superiores', 'dorsais': 'Dorsais', 'lombar': 'Lombar',
    'trapezio': 'Trapézio', 'ombros': 'Ombros', 'biceps': 'Bíceps', 'triceps': 'Tríceps', 'antebracos': 'Antebraços',
    'abdomen': 'Abdômen', 'pescoco': 'Pescoço', 'gluteos': 'Glúteos', 'quadriceps': 'Quadríceps',
    'posteriores': 'Posteriores de coxa', 'adutores': 'Adutores', 'abdutores': 'Abdutores', 'panturrilhas': 'Panturrilhas',
}
H = 720          # altura de cada figura exportada (px)
PAD = 6


def load(f):
    return np.array(Image.open(f).convert('RGB')).astype(np.int16)


# Divisa entre homem-frente e homem-costas: as mãos se encostam e o polegar da frente cruza a palma de trás
SPLIT = [(412, 0), (412, 466), (419, 474), (427, 488), (431, 500), (420, 506), (415, 520), (415, 1024)]


def split_x(h):
    ys = np.arange(h)
    return np.interp(ys, [p[1] for p in SPLIT], [p[0] for p in SPLIT])


def green(a):
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    m = ((g - r > 35) & (g - b > 8)).astype(np.uint8) * 255
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((7, 7), np.uint8))
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    return m


def fmt(v):
    s = ('%.1f' % v).rstrip('0').rstrip('.')
    return '0' if s == '-0' else s


def paths(mask, ox, oy, k):
    cs, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    out = ''
    for c in cs:
        if cv2.contourArea(c) < 60:
            continue
        c = cv2.approxPolyDP(c, 1.2, True).reshape(-1, 2)
        pts = [(round((x - ox) * k, 1), round((y - oy) * k, 1)) for x, y in c]
        d = 'M%s %s' % (fmt(pts[0][0]), fmt(pts[0][1]))
        for (x, y), (px, py) in zip(pts[1:], pts):
            d += 'l%s %s' % (fmt(x - px), fmt(y - py))
        out += d + 'z'
    return out


def main():
    files = sorted(glob.glob(os.path.join(SRC, '*.webp')) + glob.glob(os.path.join(SRC, '*.png')) + glob.glob(os.path.join(SRC, '*.jpg')))
    arts = {}
    for f in files:
        key = os.path.splitext(os.path.basename(f))[0]
        assert key in NAMES, 'nome de arquivo desconhecido: %s (use um de %s)' % (key, ', '.join(NAMES))
        arts[NAMES[key]] = load(f)
    imgs = list(arts.values())
    base = np.median(np.stack(imgs), 0).astype(np.int16) if len(imgs) > 2 else imgs[0]
    # onde ainda houver verde na base (só 1-2 artes), troca pelo cinza da vizinhança
    gm = green(base)
    if gm.any():
        base = cv2.inpaint(base.astype(np.uint8), gm, 5, cv2.INPAINT_TELEA).astype(np.int16)
    lum = base.mean(2)
    h, w = lum.shape
    # rótulos das 4 figuras: colunas fixas + divisa traçada entre as duas masculinas
    xs = split_x(h)
    col = np.arange(w)[None, :].repeat(h, 0)
    fig = np.where(col < xs[:, None], 0, np.where(col < 775, 1, np.where(col < 1165, 2, 3)))
    body = lum > 42
    body = cv2.morphologyEx(body.astype(np.uint8), cv2.MORPH_OPEN, np.ones((3, 3), np.uint8)).astype(bool)
    alpha = np.clip((lum - 30) / 34, 0, 1)
    out = {}
    for i, key in enumerate(['mf', 'mb', 'ff', 'fb']):
        sel = body & (fig == i)
        n, lab, st, _ = cv2.connectedComponentsWithStats(sel.astype(np.uint8))
        keep = np.zeros_like(sel)
        for j in range(1, n):
            if st[j, 4] > 400:
                keep |= lab == j
        keep = cv2.dilate(keep.astype(np.uint8), np.ones((5, 5), np.uint8)).astype(bool) & (fig == i)
        ys, xx = np.where(keep)
        x0, x1, y0, y1 = xx.min() - PAD, xx.max() + PAD, ys.min() - PAD, ys.max() + PAD
        k = H / (y1 - y0)
        rgba = np.dstack([base, (alpha * keep * 255)]).astype(np.uint8)[y0:y1, x0:x1]
        im = Image.fromarray(rgba, 'RGBA')
        W = round((x1 - x0) * k)
        im.resize((W, H), Image.LANCZOS).save(os.path.join(ROOT, 'img', 'body-%s.webp' % key), 'WEBP', quality=82, method=6)
        mus = {}
        for name, a in arts.items():
            m = green(a)
            m[~keep] = 0
            p = paths(m, x0, y0, k)
            if p:
                mus[name] = p
        out[key] = {'w': W, 'h': H, 'm': mus}
        print(key, W, H, sorted(mus), sum(len(v) for v in mus.values()), 'chars')
    js = '/*BODY-START*/const BODY=' + json.dumps(out, ensure_ascii=False, separators=(',', ':')) + ';/*BODY-END*/'
    p = os.path.join(ROOT, 'app.html')
    s = open(p, encoding='utf-8').read()
    s, n = re.subn(r'/\*BODY-START\*/.*?/\*BODY-END\*/', lambda _: js, s, flags=re.S)
    assert n == 1, 'marcadores /*BODY-START*/ /*BODY-END*/ não encontrados'
    open(p, 'w', encoding='utf-8').write(s)
    print('grupos com arte: %d de %d' % (len(arts), len(NAMES)))


if __name__ == '__main__':
    main()
