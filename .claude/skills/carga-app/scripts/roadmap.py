"""Roadmap do Carga: uma fonte (references/roadmap.json), duas saídas.

1. references/roadmap.md — o texto do roadmap, regenerado por inteiro (não edite o .md à mão).
2. <pasta>/{modulos,itens,proximos,entregas}.json — os dados do painel visual
   (artifact "Roadmap do Carga", https://claude.ai/artifact/T86Moh6PbAnUH4K5Hr6Bk6).

Uso: python3 scripts/roadmap.py [pasta-de-saida-do-painel]
Depois, suba cada .json como asset do painel e atualize o dataset de mesmo nome (ver SKILL.md).
"""
import json, os, sys, datetime

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(HERE, 'references', 'roadmap.json')
ICON = {'pronto': '✅', 'parcial': '🟡', 'a fazer': '⬜', 'sugestão': '💡'}


def status_of(p):
    return 'pronto' if p >= .85 else 'parcial' if p > 0 else 'a fazer'


def main():
    r = json.load(open(SRC, encoding='utf-8'))
    mods = sorted(r['modulos'], key=lambda m: m['ordem'])
    itens = [{'id': i + 1, 'modulo': m, 'status': s, 'item': t} for i, (m, s, t) in enumerate(r['itens'])]
    names = {m['modulo'] for m in mods}
    bad = [i for i in itens if i['modulo'] not in names or i['status'] not in ICON]
    assert not bad, ('item com módulo ou status desconhecido', bad)

    # 1. roadmap.md
    geral = sum(m['progresso'] for m in mods) / len(mods)
    md = ['# Roadmap do Carga: acompanhamento do desenvolvimento', '',
          '> Gerado por `scripts/roadmap.py` a partir de `references/roadmap.json`. Edite o JSON, não este arquivo.',
          '> Painel visual: https://claude.ai/artifact/T86Moh6PbAnUH4K5Hr6Bk6', '',
          '**Objetivo:** ' + r['objetivo'], '',
          'Legenda: ✅ pronto · 🟡 parcial · ⬜ a fazer · 💡 sugestão aprovada para implementar aos poucos.', '',
          '## Visão geral (progresso geral: %d%%)' % round(geral * 100), '',
          '| Módulo | Status | Progresso | Resumo |', '|---|---|---|---|']
    for m in mods:
        md.append('| %d. %s | %s | %d%% | %s |' % (m['ordem'], m['modulo'], ICON[status_of(m['progresso'])], round(m['progresso'] * 100), m['resumo']))
    for m in mods:
        md += ['', '## %d. %s' % (m['ordem'], m['modulo'])]
        md += ['- %s %s' % (ICON[i['status']], i['item']) for i in itens if i['modulo'] == m['modulo']]
    md += ['', '## Ordem dos próximos passos', '']
    md += ['%d. **%s:** %s' % (k + 1, mo, p) for k, (mo, p) in enumerate(r['proximos'])]
    md += ['', '## Referências de outros apps', '', '| App | O que inspira | Status |', '|---|---|---|']
    md += ['| %s | %s | %s |' % tuple(x) for x in r['referencias']]
    md += ['', '## Histórico de entregas', '', '| Data | Entrega |', '|---|---|']
    md += ['| %s | %s |' % (datetime.date.fromisoformat(d).strftime('%d/%m/%Y'), e) for d, e in r['entregas']]
    open(os.path.join(HERE, 'references', 'roadmap.md'), 'w', encoding='utf-8').write('\n'.join(md) + '\n')

    # 2. dados do painel
    out = sys.argv[1] if len(sys.argv) > 1 else None
    if out:
        os.makedirs(out, exist_ok=True)
        files = {
            'modulos': [dict(m, pct=round(m['progresso'] * 100), status=status_of(m['progresso'])) for m in mods],
            'itens': itens,
            'proximos': [{'ordem': k + 1, 'modulo': mo, 'passo': p} for k, (mo, p) in enumerate(r['proximos'])],
            'entregas': [{'n': k + 1, 'data': d, 'entrega': e} for k, (d, e) in enumerate(r['entregas'])],
        }
        for k, v in files.items():
            json.dump(v, open(os.path.join(out, k + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('roadmap.md atualizado; progresso geral %d%%; %d itens' % (round(geral * 100), len(itens)) + ('; painel em ' + out if out else ''))


if __name__ == '__main__':
    main()
