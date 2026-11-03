"""Artes hiper-realistas dos exercícios (EXR).

Entrada: tools/exr/<id-do-exercicio>.webp — arte 1536×1024, fundo verde-escuro (~#0C1913), homem à esquerda e
mulher à direita, músculo principal pintado de verde.
Saída: img/exr/<id>-m.webp e img/exr/<id>-f.webp (figura + equipamento sem fundo, 560 px de altura, músculo em cinza)
e o bloco `const EXR={id:{m:{w,h,p,u},f:{...}}}` entre /*EXR-START*/ e /*EXR-END*/ em app.html, onde `p` é o
contorno do músculo (SVG, coordenadas da imagem) que o app pinta com a cor de destaque (mix-blend-mode: color).

Uso: python3 tools/build_exr.py            (todas as artes de tools/exr)
     python3 tools/build_exr.py --preview  (só gera prévias em /tmp/exr-prev)
"""
import sys, json, pathlib, re, base64
import numpy as np, cv2
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / 'tools' / 'exr'
OUT = ROOT / 'img' / 'exr'
H = 560


def green_mask(rgb):
    r, g, b = [rgb[..., i].astype(int) for i in range(3)]
    m = ((g - r > 35) & (g - b > 8) & (g > 90)).astype(np.uint8)
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    return m


def fg_mask(rgb):
    """Figura + equipamento. O fundo é escuro e levemente esverdeado; o equipamento é cinza neutro."""
    f = cv2.medianBlur(rgb, 5).astype(int)
    r, g, b = f[..., 0], f[..., 1], f[..., 2]
    lum = (r + g + b) / 3
    chroma = g - (r + b) / 2
    bgc = np.median(np.concatenate([f[:8].reshape(-1, 3), f[-8:].reshape(-1, 3), f[:, :8].reshape(-1, 3), f[:, -8:].reshape(-1, 3)]), axis=0)
    dist = np.abs(f - bgc).sum(-1)
    sure_fg = (lum > 70) | ((chroma < 3) & (lum > 18)) | (green_mask(rgb) > 0)
    # fundo: perto da cor da borda, ou escuro com o tom verde do cenário (chão e sombras); equipamento é cinza neutro
    sure_bg = ((dist < 14) & (chroma > 5)) | ((chroma > 4.5) & (lum < 85))
    gc = np.full(rgb.shape[:2], cv2.GC_PR_BGD, np.uint8)
    gc[sure_bg] = cv2.GC_BGD
    gc[(~sure_bg) & (dist > 22)] = cv2.GC_PR_FGD
    gc[sure_fg] = cv2.GC_FGD
    gc[:3], gc[-3:], gc[:, :3], gc[:, -3:] = cv2.GC_BGD, cv2.GC_BGD, cv2.GC_BGD, cv2.GC_BGD
    bgd, fgd = np.zeros((1, 65), np.float64), np.zeros((1, 65), np.float64)
    cv2.grabCut(cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR), gc, None, bgd, fgd, 4, cv2.GC_INIT_WITH_MASK)
    m = np.isin(gc, (cv2.GC_FGD, cv2.GC_PR_FGD)).astype(np.uint8)
    # só os componentes grandes (tira sujeira e sombras soltas)
    n, lab, st, _ = cv2.connectedComponentsWithStats(m, 8)
    keep = np.zeros_like(m)
    for i in range(1, n):
        if st[i, cv2.CC_STAT_AREA] > 1500:
            keep[lab == i] = 1
    keep = cv2.morphologyEx(keep, cv2.MORPH_CLOSE, np.ones((3, 3), np.uint8))
    # buracos pequenos dentro da figura
    inv = 1 - keep
    n, lab, st, _ = cv2.connectedComponentsWithStats(inv, 4)
    for i in range(1, n):
        x, y, w, h, a = st[i]
        if a < 400 and x > 0 and y > 0 and x + w < m.shape[1] and y + h < m.shape[0]:
            keep[lab == i] = 1
    return keep


def split_x(fg):
    w = fg.shape[1]
    col = fg.sum(0).astype(float)
    a, b = int(w * .40), int(w * .60)
    k = np.convolve(col, np.ones(15) / 15, 'same')
    return a + int(np.argmin(k[a:b]))


def degreen(rgb, gm):
    """Troca o verde do músculo por cinza com o mesmo brilho da pele."""
    out = rgb.astype(float).copy()
    g = rgb.astype(float)
    lum = 0.30 * g[..., 0] + 0.50 * g[..., 1] + 0.20 * g[..., 2]
    lum = lum * 0.86
    gray = np.stack([lum * 1.03, lum * 1.0, lum * 0.95], -1)
    # inclui a franja: pixels levemente verdes perto do músculo pintado
    near = cv2.dilate(gm, np.ones((11, 11), np.uint8)) > 0
    fringe = near & ((g[..., 1] - np.maximum(g[..., 0], g[..., 2])) > 4)
    w = cv2.GaussianBlur((cv2.dilate(gm, np.ones((5, 5), np.uint8)) | fringe).astype(float), (5, 5), 0)[..., None]
    out = out * (1 - w) + gray * w
    return np.clip(out, 0, 255).astype(np.uint8)


def path_of(mask, scale, ox, oy):
    cs, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    d = []
    for c in cs:
        if cv2.contourArea(c) < 30:
            continue
        c = cv2.approxPolyDP(c, 1.2, True)
        pts = [(round((p[0][0] - ox) * scale), round((p[0][1] - oy) * scale)) for p in c]
        d.append('M' + 'L'.join(f'{x} {y}' for x, y in pts) + 'Z')
    return ''.join(d)


def figure(rgb, fg, gm, x0, x1):
    sub = fg[:, x0:x1]
    ys, xs = np.nonzero(sub)
    pad = 4
    t, bt = max(0, ys.min() - pad), min(rgb.shape[0], ys.max() + pad + 1)
    l, r = max(0, xs.min() - pad) + x0, min(x1, xs.max() + pad + 1 + x0)
    crop = degreen(rgb[t:bt, l:r], gm[t:bt, l:r])
    a = cv2.GaussianBlur((fg[t:bt, l:r] * 255).astype(np.uint8), (3, 3), 0)
    sc = H / (bt - t)
    w = round((r - l) * sc)
    im = Image.fromarray(np.dstack([crop, a]), 'RGBA').resize((w, H), Image.LANCZOS)
    m = (gm[t:bt, l:r] & fg[t:bt, l:r]).astype(np.uint8)
    return im, {'w': w, 'h': H, 'p': path_of(m, sc, 0, 0)}


def build(path):
    rgb = np.array(Image.open(path).convert('RGB'))
    fg, gm = fg_mask(rgb), green_mask(rgb)
    sx = split_x(fg)
    res = {}
    for k, (a, b) in {'m': (0, sx), 'f': (sx, rgb.shape[1])}.items():
        res[k] = figure(rgb, fg, gm, a, b)
    return res


def main():
    prev = '--preview' in sys.argv
    pd = pathlib.Path('/tmp/exr-prev') if prev else None
    if prev:
        pd.mkdir(exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)
    app = ROOT / 'app.html'
    s = app.read_text(encoding='utf-8')
    m = re.search(r'/\*EXR-START\*/const EXR=(.*?);/\*EXR-END\*/', s, re.S)
    exr = json.loads(m.group(1)) if m else {}
    # artes antigas embutidas como data URL viram arquivos em img/exr (o HTML fica leve)
    for eid, v in exr.items():
        for k, meta in v.items():
            if meta['u'].startswith('data:'):
                (OUT / f'{eid}-{k}.webp').write_bytes(base64.b64decode(meta['u'].split(',', 1)[1]))
                meta['u'] = f'img/exr/{eid}-{k}.webp'
    for f in sorted(SRC.glob('*.webp')):
        eid = f.stem
        res = build(f)
        exr[eid] = {}
        for k, (im, meta) in res.items():
            if prev:
                bg = Image.new('RGBA', im.size, (255, 0, 255, 255)); bg.alpha_composite(im); bg.convert('RGB').save(pd / f'{eid}-{k}.png')
                continue
            fn = OUT / f'{eid}-{k}.webp'
            im.save(fn, 'WEBP', quality=78, method=6)
            meta['u'] = f'img/exr/{eid}-{k}.webp'
            exr[eid][k] = meta
            print(eid, k, im.size, fn.stat().st_size // 1024, 'KB')
    if prev:
        print('prévias em', pd)
        return
    s = re.sub(r'/\*EXR-START\*/.*?/\*EXR-END\*/', lambda _: '/*EXR-START*/const EXR=' + json.dumps(exr, ensure_ascii=False, separators=(',', ':')) + ';/*EXR-END*/', s, flags=re.S)
    app.write_text(s, encoding='utf-8')
    print(len(exr), 'artes em EXR')


if __name__ == '__main__':
    main()
