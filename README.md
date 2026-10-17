# Carga

Registro de treinos de musculação que roda no navegador e pode ser instalado no celular como app (PWA). Funciona offline e guarda os dados só no aparelho.

- `app.html`: código do app
- `build.py`: gera `dist/` (página completa, manifesto, service worker e ícones)
- O GitHub Pages publica a pasta `dist/` pelo workflow em `.github/workflows/pages.yml`

## Catálogo de exercícios

- `tools/catalogo.txt`: lista de exercícios (nome, músculos, equipamento, tipo de registro, imagem e família de instruções)
- `tools/instrucoes.py`: passo a passo em português por padrão de movimento
- `python3 tools/build_catalog.py && python3 tools/inject_catalog.py` regenera `img/ex-*.webp` e o catálogo dentro do `app.html`
- Imagens de execução: [free-exercise-db](https://github.com/yuhonas/free-exercise-db) (domínio público, Unlicense)

## Memória do projeto e roadmap

- `.claude/skills/carga-app/`: skill com objetivo, regras, arquitetura, identidade visual, pipeline de imagens e decisões. É lida automaticamente pelo Claude Code neste repositório.
- `.claude/skills/carga-app/references/roadmap.json`: acompanhamento do desenvolvimento (fonte); `roadmap.md` e o painel visual https://claude.ai/artifact/T86Moh6PbAnUH4K5Hr6Bk6 saem dele via `scripts/roadmap.py`.
