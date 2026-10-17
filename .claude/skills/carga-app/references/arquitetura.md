# Arquitetura do código

## Arquivos do repositório

```
app.html                 o app inteiro (CSS + HTML + JS), ~320 KB
build.py                 monta dist/index.html (head + app.html) e copia manifesto, sw, ícones, img/
sw.js                    service worker; CACHE='carga-vNN' (aumente a cada entrega)
manifest.webmanifest     PWA: nome "Carga Treinos", fundo #000000 (casa com a abertura preta)
icon.svg, icon-192/512.png, icon-maskable.svg/-512.png, icon-180.png (iPhone)
img/ex-0..6.webp         folhas de sprites das fotos de exercício (2 quadros por exercício)
img/body-{mf,mb,ff,fb}.webp  base cinza do mapa corporal (homem/mulher × frente/costas)
tools/                   geradores (ver imagens-e-avatares.md)
  catalogo.txt           catálogo de exercícios (fonte, ~465 linhas)
  instrucoes.py          passo a passo por "família" de movimento
  build_catalog.py       baixa fotos (free-exercise-db), monta sprites e tools/catalog.js
  inject_catalog.py      injeta o catálogo em app.html entre /*CAT-START*/ e /*CAT-END*/
  build_body.py          mapa corporal: injeta BODY entre /*BODY-START*/ e /*BODY-END*/
  musculos/*.webp        17 artes aprovadas (fonte do mapa corporal)
  silhueta.py            vetoriza a arte das silhuetas do avatar de água
  logo.py                gera ícones SVG e a abertura (<!--SPLASH-START-->…<!--SPLASH-END-->)
  icons.js               rasteriza os ícones em PNG (Playwright)
  logo-carga.svg         marca completa (símbolo + palavra)
.github/workflows/pages.yml  publica dist/ no GitHub Pages a cada push na main
.claude/skills/carga-app/    esta skill
```

`dist/` é gerado. Nunca edite `dist/` à mão, rode `build.py`.

## Estado e armazenamento

- **Registro de perfis:** `localStorage['carga.perfis'] = {list:[{id,name}], current}`.
- **Dados de cada perfil:** `localStorage['carga.v1.<id>']`, com o objeto `S`:
  ```
  {v:1, profile:{...}, exercises:[], folders:[], routines:[], workouts:[], measures:[], water:{}, active:null}
  ```
  - `profile` guarda: `name`, `sex` ('m'|'f'), `birth`, `height`, `theme`, `accent`, `photo` (dataURL reduzida), `rest`, `sound`, `vibrate`, `wake`, `notify`, `weekStart`, `prevMode`, `livePR`, `hints`, `ssScroll`, `water` (config), dados de atividade e objetivo, `lastBackup`, `lastBackupN`, `backupSnooze`, `collapsed`.
  - `workouts[]`: `{id, name, start, end, exercises:[{exId, sets:[{type:'n'|'w'|..., kg, reps, km, min, done}]}], prs}`.
  - `water`: `{ 'AAAA-MM-DD': [{t, ml}] }`.
  - `measures[]`: registros de medidas (peso, cintura etc.) com data.
  - `active`: treino em andamento (sobrevive ao fechar o app).
- **Cópias automáticas:** IndexedDB `carga`, store `snaps` (`snapshot`, `autoSnapshot`, `restoreFrom`).
- **Backup e importação:** exporta JSON e CSV; importa CSV do Hevy (`importHevy`, com `HEVY_PT` traduzindo nomes).
- Persistência por `save()` e `persist()`. `switchProfile` troca `S` inteiro.

## Renderização

- `render()` / `rerender()` redesenham a tela atual. A navegação usa `go(view)`, `back()` e `tab(nome)`. As abas são `inicio`, `treino`, `agua` e `perfil`.
- Cada tela é `VIEWS.<nome> = () => htmlString`. Se a tela precisar de trabalho depois de desenhar (animações), use `VIEWS.<nome>.after`.
  - Telas atuais: inicio, treino, sessao, finish, treinoDetalhe, exercicios, exercicio, explorar, novoEx, picker, perfil, perfis, config, dados, estatisticas, relatorio, calendario, medidas, medidaForm, saude, agua.
- **Ações:** delegação de eventos. `data-a="nome"` chama `A.nome(dataset)`. `data-f` trata entradas de texto. Folhas que sobem de baixo: `sheet(html)` e `closeSheet()`. Também há `menu()`, `ask()`, `askText()` e `toast()`.
- Estado de interface que não é salvo: o objeto `UI` (aba de gráfico, dia selecionado nas estatísticas etc.).
- Ícones: o objeto `I` (SVG inline). `muIcon(m)` faz o ícone pequeno de músculo com o desenho simples `bodySVG`, porque o realista fica ilegível em ~30 px.

## Partes importantes

- **Catálogo:** `CAT_RAW` (linhas `nome|músculo|secundários|equipamento|tipo|imagem|família`), `INSTR`, `EQ_TIPS`, `SPR` (geometria dos sprites). `ex(id)` acha o exercício (do usuário ou do catálogo, via `BMAP`).
- **Tipos de série** (`TYPES`): `wr` (peso e repetições), `bw` (peso corporal), `as` (assistido), `t` (duração), `dt` (distância e duração). Aquecimento usa `type:'w'`.
- **Músculos:**
  - `MUSCLES` tem 17 grupos mais Cardio, Corpo inteiro e Outro.
  - `GROUPS` agrupa para o radar: Peito, Costas, Ombros, Braços, Pernas e Core.
  - `muscleSets(workouts)` conta séries por grupo (secundário vale 0,5).
- **Recordes:** `prsOf`, `recomputePRs`, `livePR` (aviso ao vivo durante o treino).
- **Coluna "Anterior":** `prevFor` pareia aquecimento com aquecimento e série válida com série válida.
- **Gráficos:**
  - `barChart`, `lineChart`, `multiLine`, `radar`, `waterChart`.
  - Seletor de período (`perCtl`, `perRange`, `buckets`, `PER`, `GRANS`) com 7 dias, mês, ano e desde o início; o padrão é Mês. A granularidade é dia ou semana.
- **Saúde:** `bodyData()`, `homeHealth()`, `waterGoal()`.
  - IMC pelas faixas da OMS.
  - TMB por Mifflin-St Jeor.
  - Água: 35 ml/kg para homens e 31 ml/kg para mulheres (EFSA), mais 500 ml por hora de treino no dia.
  - Cintura/altura pela NICE NG246.
  - Proteína pela ISSN 2017.
- **Tema:** `THEMES`, `ACCENTS`, `applyAccent()` (escreve `#accent-style`, `data-theme` e a meta theme-color). Ver identidade-visual.md.

## Convenções de código

- JS compacto, no mesmo estilo do arquivo: funções curtas numa linha, template strings, sem framework e sem dependências externas (só a fonte Barlow do Google Fonts).
- Comentários curtos em português, só onde explicam o "porquê".
- Escape o texto do usuário sempre com `esc()`.
- Prefira tokens CSS (`var(--accent)` etc.) a cores fixas, para respeitar tema e cor de destaque.

## Armadilhas já encontradas

- **Colisão de classes CSS.** Já deram conflito: `.sec`, `.bar`, `.wcard`, `.mini` (a barra fixa do treino) e spans dentro de `.wcard`, que recebem margem. Em componentes novos, use prefixo próprio e confira o estilo computado.
- **Regras de mesma especificidade:** a última vence. Exemplo: `.wcard{display:flex}` passou por cima de `.hcard`, e a correção foi usar `.wcard.hcard`.
- **`clipPath` com `<use>`** não funciona bem. Desenhe as formas explicitamente.
- **`content-visibility`** escondia linhas nas capturas. Ficou só em `#exlist .exrow`.
- **Testes no Playwright:**
  - funções do app ficam dentro de uma IIFE, então `page.evaluate` não as enxerga; teste pela interface ou semeando o `localStorage` com `addInitScript`;
  - a abertura (splash) cobre a tela por 2,6 s; clique em `#splash` para pular;
  - a tela de senha (`#lock`) fica por baixo da abertura; libere com o `sessionStorage` `carga.ok` (ver a receita de teste).

## Como testar (receita)

```bash
cd dist && python3 -m http.server 8765 &   # (re)suba sempre antes de testar
NODE_PATH=$(npm root -g) node teste.js
```

No script de teste:
1. Crie um contexto de 390×844 com `deviceScaleFactor` 2.
2. Use `addInitScript` para gravar `carga.perfis` e `carga.v1.x` com o perfil, os treinos e os exercícios de teste.
3. Clique em `#splash` para pular a abertura. A **senha de entrada** vem logo depois: para pular nos testes, no `addInitScript` grave `sessionStorage.setItem('carga.ok', <LOCK.hash>)` (o hash está em `LOCK.hash` no `app.html`). Não use a senha em si.
4. Navegue pelos `[data-a=tab][data-t=...]` e pelos `[data-a=go][data-v=...]`.
5. Colete `pageerror` e os erros de console, e tire prints.
6. Teste temas e sexos diferentes: claro, escuro, areia, lavanda, meianoite e mocha, com perfis 'm' e 'f'.
