# Identidade visual

## Marca

- **Nome:** Carga. No manifesto aparece "Carga Treinos" e, como nome curto, "Carga".
- **Símbolo:** um "C" grosso em forma de anilha (arco com pontas arredondadas e abertura à direita). Um **halter inclinado a −35°** sobe e rompe a abertura do C, passando a ideia de subir a carga e progredir.
  - Anel: raio 172, espessura 72, abertura entre 36° e 324°.
  - Halter: centro em (270, 256), barra de 210×30, anilhas de 44×156 e 28×104, com recorte de 16 px separando o halter do anel.
  - Tudo é gerado por `tools/logo.py` (viewBox 512).
- **Palavra:** "carga" em minúsculas, **Inter Display Black Italic** (licença SIL OFL), espaçamento −30, convertida em contorno. Branca sobre fundo escuro.
- **Cores da marca:**
  - degradê do símbolo em fundo escuro: `#6BFFB0` → `#10B873`;
  - fundo do ícone do app: `#22D481` → `#0A7A4E`, com o símbolo branco.
- **A marca não muda com o tema nem com a cor de destaque.** Isso foi decidido de propósito, para ser reconhecível.
- **Arquivos:**
  - `icon.svg` (favicon: cantos arredondados, escala 0,9);
  - `tools/icon-any.svg` → `icon-192.png` e `icon-512.png`, os ícones "any" do manifesto: **só o símbolo, fundo transparente**, escala 0,314 e deslocado 24 unidades para baixo. O Android usa esse ícone na própria tela de abertura do app instalado, sobre o fundo preto. Com essas medidas (tiradas do vídeo do celular do usuário), ela fica idêntica à nossa abertura e não aparece mais o quadrado verde. Não volte a usar o quadrado verde aqui;
  - `icon-maskable.svg` → `icon-maskable-512.png` (sangrado, escala 0,74, cabe na zona segura do Android): é o ícone da **tela inicial** do celular;
  - `tools/icon-apple.svg` (sangrado, escala 0,86);
  - `tools/logo-carga.svg` (símbolo + palavra, fundo preto).

## Abertura (splash): modelo Hevy

Analisada quadro a quadro a partir do vídeo do usuário abrindo o Hevy.
- **Fundo preto (`#000`) desde o primeiro quadro.** `build.py` põe `class="sp-on"` no `<html>` e `theme-color #000000`, e o manifesto usa `background_color #000000`. A barra de status fica preta durante a abertura e volta à cor do tema depois.
- **Só o símbolo** no centro, com 76 px, parado, sem animação de desenho. A fluidez do Hevy vem justamente de não ter etapas encenadas. A primeira versão (C se desenhando, halter girando, palavra entrando) foi recusada como pouco fluida.
- A logo fica visível **2,6 s**. Depois vem um **esmaecimento de 0,24 s** que revela o app, que parece "acender" a partir do escuro. Um toque na tela pula a abertura.
- A expansão a partir do ícone é feita pelo sistema do celular. Imitar isso no navegador foi testado e removido, porque mostrava o app em volta.
- Código: CSS `#splash` e `.sp-mark` em `app.html`. O HTML da abertura é injetado por `tools/logo.py`. O temporizador fica no fim do script.

## Temas (6)

Formato de cada linha de `THEMES`: `[chave, nome, tipo, fundo, superfície, superfície2, linha, texto, texto suave, corpo, músculo vazio, cor sugerida]`.

| Chave | Nome | Tipo | Fundo | Superfície | Cor de destaque padrão |
|---|---|---|---|---|---|
| claro | Claro | claro | #F1F3EF | #FFFFFF | verde |
| escuro | Escuro | escuro | #0D1110 | #161B1A | verde |
| areia | Areia | claro | #F3EEE6 | #FFFCF7 | laranja |
| lavanda | Lavanda | claro | #F1EFF8 | #FFFFFF | roxo |
| meianoite | Meia-noite | escuro | #0A0F1E | #121A2E | ciano |
| mocha | Mocha | escuro | #16110E | #211A16 | mocha |

- Ao trocar o tema, a cor de destaque vai para a sugerida, mas o usuário pode escolher outra.
- Os temas "Preto" e "Automático" foram removidos a pedido. Perfis antigos com `preto` caem em `escuro`.

## Cores de destaque (15)

Cada cor tem uma variante para tema claro e outra para tema escuro: `[cor, cor suave, texto sobre a cor]`.

| Nome | Variante clara | Variante escura |
|---|---|---|
| Verde | #0D7556 | #33C391 |
| Petróleo | #0B6E80 | #3BC0D4 |
| Ciano | #0279A3 | #38C8F2 |
| Azul | #1F5FD1 | #6EA0FF |
| Índigo | #3D47B8 | #8B95FF |
| Roxo | #6A3FC6 | #A98BFF |
| Magenta | #A8279A | #EE7BE0 |
| Rosa | #C2367A | #FF7DB7 |
| Vinho | #8E2445 | #E2729A |
| Vermelho | #C0362C | #FF7A6B |
| Laranja | #B4520C | #FF9A4D |
| Dourado | #946700 | #F2B83A |
| Mocha | #7A4E36 | #D6A283 |
| Oliva | #5B7A12 | #A8D84A |
| Grafite | #3D4A55 | #A7B6C4 |

**Tokens CSS** (use sempre, nunca cor fixa): `--bg`, `--surface`, `--surface-2`, `--line`, `--fg`, `--muted`, `--accent`, `--accent-soft`, `--accent-ink`, `--amber` (recordes), `--danger`, `--violet`, `--body`, `--muscle-0`, `--r:14px`.

## Tipografia

- Títulos e números: **Barlow Condensed** (`--display`), 600–700, títulos de seção em maiúsculas.
- Texto: **Barlow** (`--text`).
- Ambas vêm do Google Fonts, com fallback para fontes do sistema.

## Componentes recorrentes

- **Cartão:** `.card` / `.wcard` com borda `--line`, raio 14 e fundo `--surface`.
- **Botões:** `.btn.pri` (preenchido com a cor de destaque), `.btn.sec` (superfície), `.btn.ghost`, `.sm`, `.wide`.
- **Faixa dos 7 dias:** `.days7` com `.dchip`. Dia com treino: número num círculo cheio na cor de destaque (`.has`). Hoje: letra do dia da semana na cor de destaque. Selecionado: borda.
- **Etiquetas de grupo muscular:** `.mchip`; os dois principais usam `.top` (fundo `--accent-soft`).
- **Folhas que sobem de baixo** (`sheet`), toasts, caixa vazia `.emptybox` com borda tracejada.
- Ícones de traço fino num conjunto próprio (`I`), no estilo dos do Hevy.

## Tom de texto

- Português do Brasil, frases curtas, sem jargão.
- Sempre explique o que um número significa, por exemplo "IMC de 18,5 a 24,9 é…".
- Citações de fonte nos cálculos de saúde (OMS, EFSA, NICE, ISSN, ACE) e o aviso de que não substituem um profissional.

## Pictogramas dos exercícios avulsos (aba Exercícios)
- Estilo dos ícones do Samsung Health (referência enviada pelo usuário em 18/10/2026): figuras de traço grosso (membros 2,5, tronco 3,3, pontas redondas) com cabeça cheia, numa cor só. **Desenho próprio**, não copiado.
- Gerados por `tools/exicons.py` (49 pictogramas, um por exercício; esportes de raquete parecidos compartilham o de tênis). O script injeta `AIC` e `AIC_OF` (exercício → pictograma) em `app.html` entre `/*AIC-START*/` e `/*AIC-END*/` e grava a prancha `tools/exicons.html` para conferir.
- Nas listas: só o pictograma na cor de destaque, sem círculo (como no Samsung). Nos favoritos: círculo `--accent-soft`. Musculação usa `--violet`.

## Organização das telas (18/10/2026)
- Barra de abas: Início · Treino · Exercícios · Nutrição · Água · Perfil.
- Início em capítulos (v66, aprovado pelo usuário): **Meu dia** (v81: 1º bloco, com Treino e Metas de longo prazo no fim; Metas de hoje removido) → **Minha semana** (`homeWeek`) (`homeMyDay`: meta, consumido, gasto, saldo, macros, água, sono, "Como calculamos?") → **Meu gasto** (`homeSpend`: anéis das calorias ativas + barra basal/rotina/treino/exercícios = gasto do dia) → **Meu corpo** (`homeBody`: peso com tendência, IMC, taxa basal, gordura) → **Explorar** (atalhos). Cada número aparece uma vez só. Vocabulário único: Meta (quanto comer), Gasto (total do dia), Ativas (treino + exercícios), Saldo (comido − gasto). Semáforo: em andamento (cor padrão), dentro da meta (verde #2E9E5B), um pouco acima (âmbar), bem acima (vermelho).
- Aba Treino: primeiro bloco é **Seus treinos** (últimos 10 + "Ver todos" no Perfil), depois Iniciar treino vazio / Retomar e Rotinas.

