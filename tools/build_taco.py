"""Base de alimentos do Carga: TACO 4ª edição (NEPA/UNICAMP, 2011), valores por 100 g.

CSVs normalizados do projeto taco-api (github.com/raulfdm/taco-api, licença MIT) em tools/taco/.
Injeta `const TACO_CAT=[...]` e `const TACO="..."` em app.html entre /*TACO-START*/ e /*TACO-END*/.
Cada linha de TACO: nome|categoria|kcal|prot|gord|carb|fibra|saturada|colesterol|sódio|potássio|cálcio|ferro|magnésio|zinco|vitC|vitA(RAE)
(vazio = sem dado na tabela; tratado como 0 nas somas). Uso: python3 tools/build_taco.py
"""
import csv, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'tools', 'taco')
COLS = ['kcal', 'protein', 'lipids', 'carbohydrates', 'dietaryFiber', 'saturated', 'cholesterol', 'sodium',
        'potassium', 'calcium', 'iron', 'magnesium', 'zinc', 'vitaminC', 'rae']


def num(v):
    v = (v or '').strip()
    try:
        x = float(v)
    except ValueError:
        return ''
    s = ('%.2f' % x).rstrip('0').rstrip('.')
    return '0' if s in ('-0', '') else s


def main():
    cats = {r['id']: r['name'] for r in csv.DictReader(open(os.path.join(SRC, 'categories.csv'), encoding='utf-8'))}
    nut = {r['foodId']: r for r in csv.DictReader(open(os.path.join(SRC, 'nutrients.csv'), encoding='utf-8'))}
    fat = {r['foodId']: r for r in csv.DictReader(open(os.path.join(SRC, 'fatty-acids.csv'), encoding='utf-8'))}
    cat_ids = sorted(cats, key=int)
    rows = []
    for f in csv.DictReader(open(os.path.join(SRC, 'food.csv'), encoding='utf-8')):
        n = dict(nut[f['id']]); n['saturated'] = fat.get(f['id'], {}).get('saturated', '')
        if not num(n['kcal']):
            continue
        name = re.sub(r'\s+', ' ', f['name'].replace('|', '/')).strip()
        rows.append('|'.join([name, str(cat_ids.index(f['categoryId']))] + [num(n[c]) for c in COLS]))
    js = ('/*TACO-START*/const TACO_CAT=' + str([cats[k] for k in cat_ids]).replace("'", '"') + ';\n'
          'const TACO=`' + '\n'.join(rows).replace('`', "'") + '`;/*TACO-END*/')
    p = os.path.join(ROOT, 'app.html'); s = open(p, encoding='utf-8').read()
    s, k = re.subn(r'/\*TACO-START\*/.*?/\*TACO-END\*/', lambda _: js, s, flags=re.S)
    assert k == 1, 'marcadores /*TACO-START*/ /*TACO-END*/ não encontrados'
    open(p, 'w', encoding='utf-8').write(s)
    print('%d alimentos, %d categorias, %.0f KB' % (len(rows), len(cats), len(js) / 1024))


if __name__ == '__main__':
    main()
