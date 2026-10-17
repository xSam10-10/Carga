# Imagens, mapa corporal e avatares

## 1. Mapa corporal hiper-realista (aprovado pelo usuário)

**Origem:** 17 artes que o usuário gerou em outro ambiente, todas com o **mesmo padrão**:
- tamanho 1536×1024, fundo verde-escuro (~#101A14);
- 4 figuras cinza (homem de frente, homem de costas, mulher de frente, mulher de costas);
- **um** grupo muscular pintado de verde-água (~rgb(67,176,135)).

A base cinza é **idêntica** entre as artes; a única diferença é ruído de compressão. As fontes ficam em `tools/musculos/` e há uma cópia em `assets/musculos/` desta skill.

**Arquivo → grupo** (os nomes que `tools/build_body.py` espera):

| Arquivo | Grupo | Vistas |
|---|---|---|
| peito.webp | Peito | frente |
| costas-superiores.webp | Costas superiores | costas |
| dorsais.webp | Dorsais | costas |
| lombar.webp | Lombar | costas |
| trapezio.webp | Trapézio | frente e costas |
| ombros.webp | Ombros | frente e costas |
| biceps.webp | Bíceps | frente |
| triceps.webp | Tríceps | frente e costas |
| antebracos.webp | Antebraços | frente e costas |
| abdomen.webp | Abdômen | frente |
| pescoco.webp | Pescoço | frente e costas (pequeno na mulher de costas por causa do cabelo) |
| gluteos.webp | Glúteos | costas |
| quadriceps.webp | Quadríceps | frente |
| posteriores.webp | Posteriores de coxa | costas |
| adutores.webp | Adutores | frente |
| abdutores.webp | Abdutores | frente e costas |
| panturrilhas.webp | Panturrilhas | costas |

**Pipeline (`python3 tools/build_body.py`):**
1. **Base limpa:** mediana pixel a pixel de todas as artes (o verde de cada uma some). Se sobrar algum verde, é preenchido com `cv2.inpaint`.
2. **Separação das 4 figuras:** cortes fixos em x=775 e x=1165. Entre o homem de frente e o de costas, as mãos se tocam e o polegar da frente cruza a palma de trás, então há uma **divisa traçada à mão** (`SPLIT`, polilinha em torno de x≈412–431, y≈466–520).
3. **Recorte e exportação:** fundo transparente com alfa calculado pela luminância (`(lum-30)/34`), recorte e redução para **720 px de altura** → `img/body-{mf,mb,ff,fb}.webp` (~40 KB cada).
4. **Máscaras dos grupos:** verde detectado por `g-r>35 && g-b>8`, mais fechamento e abertura morfológicos. A máscara é recortada pela figura, vetorizada (`findContours` + `approxPolyDP` 1,2) e convertida em caminhos SVG nas coordenadas da figura exportada.
5. **Injeção:** `const BODY={mf:{w,h,m:{Grupo:'path…'}},…}` entra em `app.html` entre `/*BODY-START*/` e `/*BODY-END*/`.

**Renderização no app (`realBody`, `bodyMap`):**
- Desenha `<image>` da base e, por cima, um `<path class="rm">` para cada grupo com séries.
- O caminho usa `fill: var(--accent)` com **`mix-blend-mode: color`**. Isso aplica o tom da cor de destaque e **preserva o sombreamento e as fibras** da arte; foi escolhido depois de comparar com multiply, hard-light e normal.
- Intensidade: `fill-opacity = .5 + .5 × (séries / máximo)`.
- A grade das duas figuras usa colunas proporcionais à largura de cada imagem, para frente e costas ficarem com a mesma altura.
- O sexo do perfil escolhe `m*` ou `f*`.
- **Onde aparece:**
  - Estatísticas: mapa dos últimos 7 dias, que filtra por dia ao tocar;
  - cartões do Início: os últimos 10 treinos;
  - detalhe do exercício: "Músculos trabalhados" e a falta de animação.
- **Sem séries:** o corpo fica cinza, com o aviso "Nenhuma série registrada neste período". O usuário escolheu manter assim.
- **Ícones pequenos de músculo** (listas e filtros) continuam com o desenho simples `bodySVG`. Isso é proposital, porque o realista fica ilegível em ~30 px.

**Para trocar ou incluir uma arte:** salve o arquivo em `tools/musculos/<nome>.webp` no mesmo padrão e rode `build_body.py`, depois `build.py`. Republique o Artifact passando `files` com os 4 `img/body-*.webp`, porque a mediana muda a base.

## 2. Avatar de água (aba Água)

- **Arte aprovada:** `assets/silhuetas-agua.webp`. Duas figuras em pé, de contorno único e suave: homem careca e de ombros largos, mulher com cabelo chanel e cintura e quadril marcados. Traço verde-acinzentado (#769F92) sobre branco, sem roupa desenhada.
- **Vetorização:** `tools/silhueta.py` (canal alfa → contorno ampliado 4×) gera:
  - `SIL.m` / `SIL.f`, com `w`, `h`, `t` e `b` (topo e base do corpo para o nível da água);
  - `body`: região interna, usada como `clipPath`;
  - `line`: o traço, preenchido com `evenodd`.
- **Cores:**
  - traço: `color-mix(accent 70%, --fg)`, que continua visível mesmo com o avatar cheio;
  - interior: `color-mix(accent 7%, --surface)`;
  - água: degradê da cor de destaque com uma onda animada (`.wave`, `@keyframes wv`).
- O nível sobe com transição de 0,9 s desde o valor anterior (`UI.wPrev`).
- Perfil `f` usa a figura feminina; os demais usam a masculina.

## 3. Imagens dos exercícios

- **Fonte:** free-exercise-db (domínio público). `tools/build_catalog.py` baixa duas fotos por exercício, corta em 200×134 e monta folhas de 10×10 → `img/ex-0..6.webp`.
- No app, `sprBg` / `sprPct` posicionam o sprite. A "animação" alterna os 2 quadros (`exAnim`).
- O catálogo tem ~465 exercícios, com nomes em português, equivalência de nomes do Hevy (`ALIAS` → `HEVY_PT`) e instruções passo a passo por família de movimento (`tools/instrucoes.py`).

## 4. Logo e ícones

`python3 tools/logo.py` gera os SVG e a abertura. Depois rode `NODE_PATH=$(npm root -g) node tools/icons.js` para gerar os PNG 192, 512, maskable-512 e 180. Detalhes de forma e cor estão em identidade-visual.md.

## 5. Foto de perfil

`makePhoto` reduz e recorta a foto escolhida (quadrada) e guarda como dataURL em `S.profile.photo`. O `avaIn` mostra a foto ou as iniciais.

## Ferramentas no ambiente

Python com PIL, numpy e opencv-python-headless (`pip install opencv-python-headless`) e fontTools (`pip install fonttools`). As fontes Inter estão em `/usr/share/fonts/opentype/inter/`. O Chromium do Playwright está em `/opt/pw-browsers`.
