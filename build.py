"""Gera dist/ (PWA instalável) a partir de app.html."""
import pathlib, shutil
root = pathlib.Path(__file__).parent
dist = root / 'dist'
dist.mkdir(exist_ok=True)
app = (root / 'app.html').read_text(encoding='utf-8')
head = '''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#0D7556">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="icon-192.png">
<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top);padding-bottom:env(safe-area-inset-bottom)}img{max-width:100%}[hidden]{display:none!important}</style>
</head>
<body>
'''
(dist / 'index.html').write_text(head + app + '\n</body>\n</html>\n', encoding='utf-8')
for f in ['manifest.webmanifest', 'sw.js', 'icon.svg', 'icon-192.png', 'icon-512.png']:
    shutil.copy(root / f, dist / f)
if (root/'img').exists():
    shutil.copytree(root/'img', dist/'img', dirs_exist_ok=True)
print('ok', (dist / 'index.html').stat().st_size, 'bytes')
