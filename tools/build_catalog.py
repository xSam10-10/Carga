"""Gera o catálogo de exercícios (catalog.js) e as imagens de execução (img/ex-N.webp).

Imagens: free-exercise-db (domínio público, Unlicense) — github.com/yuhonas/free-exercise-db
Uso: python3 tools/build_catalog.py  (precisa de rede na primeira vez para baixar as fotos)
"""
import json, os, re, sys, unicodedata, urllib.request, urllib.parse, io
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from instrucoes import F, TIPS

CACHE = os.path.join(ROOT, 'tools', '.cache')
OUT_IMG = os.path.join(ROOT, 'img')
BASE = 'https://raw.githubusercontent.com/yuhonas/free-exercise-db/main/'
FW, FH, COLS, PER = 200, 134, 10, 100  # quadro, colunas por folha, quadros por folha

# Nomes do Hevy (em português) que equivalem a exercícios que já existem no catálogo
ALIAS = {
 'Agachamento (Barra)': 'Agachamento Livre (Barra)', 'Agachamento Frontal': 'Agachamento Frontal (Barra)',
 'Agachamento Goblet': 'Agachamento Goblet (Halter)', 'Tríceps Pulley': 'Tríceps Pulley (Cabo)',
 'Tríceps na Polia': 'Tríceps Pulley (Cabo)', 'Tríceps na Polia com Corda': 'Tríceps Corda (Cabo)',
 'Desenvolvimento de Ombros Sentado (Máquina)': 'Desenvolvimento (Máquina)', 'Face Pull': 'Face Pull (Cabo)',
 'Swing com Kettlebell': 'Kettlebell Swing', 'Simulador de Escadas (Andares)': 'Escada (Máquina)',
 'Peito na Paralela': 'Paralelas (Peito)', 'Tríceps na Paralela': 'Paralelas (Tríceps)', 'Flexão': 'Flexão de Braço',
 'Crossover na Polia': 'Crossover (Cabo)', 'Crucifixo Invertido (Máquina)': 'Crucifixo Inverso (Máquina)',
 'Crucifixo Invertido (Halter)': 'Crucifixo Inverso (Halter)', 'Remada na Barra T': 'Remada Cavalinho (Barra T)',
 'Extensão Lombar (Hiperextensão)': 'Hiperextensão Lombar', 'Abdominal': 'Abdominal Crunch',
 'Elevação de Pernas na Barra Fixa': 'Elevação de Pernas Suspenso', 'Abdominal na Polia (Corda)': 'Abdominal na Polia (Cabo)',
 'Giro Russo (Peso Corporal)': 'Russian Twist', 'Abdominal Invertido': 'Abdominal Infra',
 'Extensão de Tríceps (Halter)': 'Tríceps Francês (Halter)', 'Extensão de Tríceps Acima da Cabeça (Cabo)': 'Tríceps Overhead (Cabo)',
 'Extensão de Tríceps (Máquina)': 'Tríceps (Máquina)', 'Extensão de Tríceps (Cabo)': 'Tríceps Overhead (Cabo)',
 'Rosca Inclinada Sentado (Halter)': 'Rosca Inclinada (Halter)', 'Rosca de Punho Sentado (Barra)': 'Rosca de Punho (Barra)',
 'Rosca Invertida (Barra)': 'Rosca Inversa (Barra)', 'Desenvolvimento (Máquina Smith)': 'Desenvolvimento (Smith)',
 'Elevação Frontal com Anilha': 'Elevação Frontal (Anilha)', 'Puxada com Braços Estendidos (Cabo)': 'Pulldown Braços Estendidos (Cabo)',
 'Remada Serrote (Halter)': 'Remada Unilateral (Halter)', 'Remada Sentada (Máquina)': 'Remada Baixa (Máquina)',
 'Remada Sentada com Pegada Aberta (Cabo)': 'Remada Sentada Pegada Aberta (Cabo)', 'Puxada Alta - Pegada Fechada (Cabo)': 'Puxada Alta Pegada Fechada (Cabo)',
 'Puxada Supinada (Cabo)': 'Puxada Alta Supinada (Cabo)', 'Supino Inclinado (Máquina Smith)': 'Supino Inclinado (Smith)',
 'Coice no Cabo em Pé': 'Glúteo na Polia (Cabo)', 'Coice de Glúteo (Máquina)': 'Glúteo 4 Apoios (Máquina)', 'Coice (Máquina)': 'Glúteo 4 Apoios (Máquina)',
 'Passada Caminhando (Halter)': 'Passada (Halter)', 'Panturrilha no Leg Press': 'Panturrilha no Leg Press (Máquina)',
 'Panturrilha em Pé (Smith)': 'Panturrilha (Smith)', 'Crucifixo Reto (Halter)': 'Crucifixo (Halter)', 'Crucifixo Baixo (Cabo)': 'Crossover Baixo (Cabo)',
 'Levantamento Terra com Pernas Estendidas': 'Stiff (Barra)', 'Elevação Pélvica (Máquina Smith)': 'Elevação Pélvica (Smith)',
 'Supino Reto': 'Supino Reto (Barra)', 'Tríceps Testa': 'Tríceps Testa (Barra)', 'Tríceps Coice': 'Tríceps Coice (Halter)',
 'Rosca Martelo': 'Rosca Martelo (Halter)', 'Desenvolvimento Arnold': 'Desenvolvimento Arnold (Halter)',
}

def norm(s):
    return unicodedata.normalize('NFD', s).encode('ascii', 'ignore').decode().lower().strip()

def main():
    os.makedirs(CACHE, exist_ok=True); os.makedirs(OUT_IMG, exist_ok=True)
    fedb_path = os.path.join(CACHE, 'exercises.json')
    if not os.path.exists(fedb_path):
        urllib.request.urlretrieve(BASE + 'dist/exercises.json', fedb_path)
    fedb = {x['id']: x for x in json.load(open(fedb_path))}
    rows = []
    for ln in open(os.path.join(ROOT, 'tools', 'catalogo.txt'), encoding='utf-8'):
        ln = ln.strip()
        if not ln or ln.startswith('#'):
            continue
        p = [c.strip() for c in ln.split('|')]
        assert len(p) == 7, ln
        rows.append(p)
    names = [r[0] for r in rows]
    dup = {n for n in names if names.count(n) > 1}
    assert not dup, dup
    for a, b in ALIAS.items():
        assert b in names, ('alias aponta para nome inexistente', a, b)
    imgs, idx = [], {}
    for r in rows:
        if r[6] not in F:
            raise SystemExit('família desconhecida: %s (%s)' % (r[6], r[0]))
        if r[5] and (r[5] not in fedb or not fedb[r[5]].get('images')):
            print('imagem inexistente, ignorando:', r[5], r[0]); r[5] = ''
        if r[5] and r[5] not in idx:
            idx[r[5]] = len(imgs); imgs.append(r[5])
    # baixar e montar folhas
    frames = []
    for fid in imgs:
        for k in (0, 1):
            fp = os.path.join(CACHE, fid.replace('/', '_') + '_%d.jpg' % k)
            if not os.path.exists(fp):
                ims = fedb[fid].get('images') or []
                rel = ims[min(k, len(ims) - 1)]
                urllib.request.urlretrieve(BASE + 'exercises/' + urllib.parse.quote(rel), fp)
            im = Image.open(fp).convert('RGB')
            # recorte central para 3:2 e redução
            w, h = im.size; tw = h * FW / FH
            if w > tw:
                x = (w - tw) / 2; im = im.crop((x, 0, x + tw, h))
            else:
                th = w * FH / FW; y = (h - th) / 2; im = im.crop((0, y, w, y + th))
            frames.append(im.resize((FW, FH), Image.LANCZOS))
    for f in os.listdir(OUT_IMG):
        if f.startswith('ex-'): os.remove(os.path.join(OUT_IMG, f))
    nsheets = (len(frames) + PER - 1) // PER
    for s in range(nsheets):
        chunk = frames[s * PER:(s + 1) * PER]
        rws = (len(chunk) + COLS - 1) // COLS
        sheet = Image.new('RGB', (COLS * FW, rws * FH), 'white')
        for i, im in enumerate(chunk):
            sheet.paste(im, ((i % COLS) * FW, (i // COLS) * FH))
        sheet.save(os.path.join(OUT_IMG, 'ex-%d.webp' % s), 'WEBP', quality=58, method=6)
    total = sum(os.path.getsize(os.path.join(OUT_IMG, f)) for f in os.listdir(OUT_IMG))
    # JS
    raw = '\n'.join('|'.join([r[0], r[1], r[2], r[3], r[4], str(idx[r[5]]) if r[5] else '', r[6]]) for r in rows)
    js = ('/* Catálogo gerado por tools/build_catalog.py — não edite à mão. Imagens: free-exercise-db (domínio público). */\n'
          'const CAT_RAW=`' + raw.replace('`', "'") + '`;\n'
          'const INSTR=' + json.dumps({k: [v[0], v[1]] for k, v in F.items()}, ensure_ascii=False, separators=(',', ':')) + ';\n'
          'const EQ_TIPS=' + json.dumps(TIPS, ensure_ascii=False, separators=(',', ':')) + ';\n'
          'const HEVY_PT=' + json.dumps({norm(a): b for a, b in ALIAS.items()}, ensure_ascii=False, separators=(',', ':')) + ';\n'
          'const SPR={w:%d,h:%d,cols:%d,per:%d,sheets:%d,rows:%s};\n' % (FW, FH, COLS, PER, nsheets, json.dumps([(min(PER, len(frames) - s * PER) + COLS - 1) // COLS for s in range(nsheets)])))
    open(os.path.join(ROOT, 'tools', 'catalog.js'), 'w', encoding='utf-8').write(js)
    print('%d exercícios, %d com imagem (%d quadros), %d folhas, %.0f KB de imagens' % (len(rows), sum(1 for r in rows if r[5]), len(frames), nsheets, total / 1024))

main()
