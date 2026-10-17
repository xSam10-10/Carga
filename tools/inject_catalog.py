"""Copia tools/catalog.js para dentro do app.html, entre os marcadores /*CAT-START*/ e /*CAT-END*/."""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app = os.path.join(ROOT, 'app.html')
s = open(app, encoding='utf-8').read()
js = open(os.path.join(ROOT, 'tools', 'catalog.js'), encoding='utf-8').read()
s2 = re.sub(r'/\*CAT-START\*/.*?/\*CAT-END\*/', lambda m: '/*CAT-START*/\n' + js + '/*CAT-END*/', s, flags=re.S)
assert s2 != s or '/*CAT-START*/' in s
open(app, 'w', encoding='utf-8').write(s2)
print('catálogo injetado')
