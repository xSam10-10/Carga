---
name: carga-app
description: Memória completa do projeto Carga, o app (PWA) de treino e saúde do Samuel e da Carol. Inclui objetivo, regras do produto, arquitetura do código, identidade visual (logo, temas, cores de destaque, abertura), mapa corporal hiper-realista, avatar de água, rotina de publicação e roadmap. Use SEMPRE que o assunto for o app Carga ou o repositório carga, mesmo sem citar a skill. Isso vale para criar ou alterar telas e funcionalidades, mexer no mapa corporal, avatares, logo ou temas, planejar dieta, macros, metas, medidas ou água, publicar no GitHub Pages, gerar os zips, ou continuar o projeto num chat ou ambiente novo.
---

# Carga — memória do projeto

O Carga é um app pessoal de treino e saúde para duas pessoas: **Samuel** e **Carol**. Cada um usa o próprio celular e tem o próprio perfil. Começou como um "Hevy melhorado" e quer chegar ao **app de saúde mais completo do mercado**, reunindo treino, dieta, água, medidas, metas e gráficos num só lugar. Leia esta página inteira antes de mexer no projeto. Os detalhes estão nos arquivos de `references/`, indicados em cada seção.

## Objetivo (visão do produto)

Ser o app mais completo para acompanhar a saúde:
- **Treino:** todos os grupos musculares, rotinas, personalização, recordes, progressão e mapa corporal.
- **Nutrição:** dietas, macronutrientes, micronutrientes, refeições e metas.
- **Hidratação:** meta diária e acompanhamento (já existe).
- **Corpo:** medidas, peso, IMC, % de gordura, fotos de evolução.
- **Metas e gráficos:** semanais, mensais, anuais e desde o início.

O que já existe e o que falta está em `references/roadmap.md`. Lá também estão as **sugestões aprovadas pelo usuário** (marcadas com 💡), para implementar aos poucos. **Atualize o roadmap sempre que entregar algo**, como descrito em "Roadmap e painel visual" mais abaixo.

## Regras que o usuário definiu (não quebrar)

1. **Sem rede social.** Nada de feed de outras pessoas, seguidores, curtidas ou comentários. Também nada de compartilhar em WhatsApp, Instagram ou outros apps sociais. O app serve só para treino, desempenho e sugestões de melhoria.
2. **Sem login nem servidor.** Os dados ficam no aparelho (localStorage e IndexedDB). Backup e importação são por arquivo.
3. **Perfis separados.** Samuel e Carol têm dados 100% separados e alternam pelo Perfil.
4. **Tudo em português do Brasil**, com tom direto e amigável, sem jargão técnico na interface.
5. **Referências: Hevy (treino) e Samsung Health (Nutrição, Exercícios, pictogramas).** Quando o usuário mandar prints ou vídeos, analise quadro a quadro e reproduza o comportamento com fidelidade, mas com desenhos próprios (nunca copiar imagens dos apps). Exemplo: a abertura atual foi copiada do vídeo dele.
6. **Calorias vêm do relógio.** No fim do treino, um pop-up pede as calorias **ativas** que o relógio mostrou (Samsung Health ou app Fitness), e o valor é salvo direto no treino. Nos exercícios avulsos (aba Exercícios) as calorias são **obrigatórias** para salvar; distância, duração e frequência cardíaca média são opcionais e só informativas. **Nenhuma fórmula usa frequência cardíaca**; o número do relógio é o que vale.
7. **Cor de destaque e tema mandam em tudo.** Realces, gráficos, mapa corporal e avatar de água seguem a cor de destaque. A exceção é a marca: logo, ícone e abertura ficam sempre no verde da marca.
8. **O sexo do perfil define as figuras.** O perfil feminino usa as figuras femininas (mapa corporal, avatar de água, miniaturas de filtro) e o masculino as masculinas. Enquanto o sexo não for preenchido, `visSex()` usa feminino para o perfil da Carol.
9. **Senha de entrada.** É fixa e igual nos dois celulares. O código guarda só o hash; nunca registre a senha em texto puro em lugar nenhum, porque o repositório é público.
10. **Todo preenchimento fica só na aba Perfil** (Meus dados, medidas, metas de nutrição e de água, configurações). Outras abas só mostram avisos que levam para lá pela ação `goPf`, que troca para a aba Perfil. Lançamentos do dia (refeições, copos de água, exercícios, calorias do treino) ficam nas próprias abas.
11. **Só o que funciona offline.** Nada que dependa de GPS, mapa, cronômetro ao vivo ou leitura do relógio/Health Connect. Integração com Health Connect só exigiria app nativo Android; está aguardando decisão do usuário.
12. **A meta do dia é: meta base (rotina × objetivo) + exercício do relógio por inteiro − consumido.** Modo "Pelo relógio" é o padrão; os dias de treino por semana são escolhidos no perfil e só mexem nas calorias no modo "Pelo nível".
13. **Tudo o que muda com o tempo tem histórico e comparação** (Evolução do corpo: semana a semana, mês a mês, desde o início e ano contra ano).
14. **Assinatura discreta** "by Samuel Costa" no rodapé de Configurações. Não remover.
15. **Datas:** todo campo de data é digitado só com números (máscara DD/MM/AAAA, classe `.dmask`); os demais também têm botão de calendário, mas a **data de nascimento é só digitação**.
16. **Produtos de marca** que o usuário mandar por foto da tabela nutricional entram no código (`BRAND` em `app.html`, valores da porção) para valer nos dois perfis; nunca invente valores — se a foto for ambígua (ex.: tabela de outro produto no anúncio), registre e avise para conferir.
17. **Painel do dia** tem layout fixo definido pelo usuário: Proteína/Carboidratos/Gordura; Consumidas/Gastas/Déficit-Superávit (com a meta do objetivo); Água/Treino/Exercício.
18. **Receitas são do aparelho, não do perfil:** valem para Samuel e Carol no mesmo celular. Entre celulares, só por código "Enviar/Receber receitas" (sem servidor). Sincronização automática entre aparelhos exigiria um servidor — decisão do usuário.

## Como o usuário trabalha

- O usuário fala por áudio transcrito, então algumas palavras chegam trocadas. Exemplos: "Haiku" é **Hevy**, "alter" é **halter**.
- Ele testa pelo celular e prefere ver o resultado. Depois de cada mudança, mande prints de teste com SendUserFile e os zips atualizados.
- Ele gosta de recomendações claras: proponha, implemente e mostre. Pergunte só quando a decisão for realmente dele.
- Ele manda imagens prontas (feitas em outro ambiente) para trocar visuais e espera **fidelidade total** à arte.

## Arquitetura em 30 segundos

- Página única: `app.html` (HTML + CSS + JS). `python3 build.py` gera `dist/index.html` e copia manifesto, service worker, ícones e `img/`.
- Estado global `S`, com configurações do perfil em `S.profile`. Cada tela é uma função em `VIEWS.<nome>` que devolve HTML. As ações usam `data-a="..."` e são tratadas no objeto `A`.
- Abas (6), nesta ordem: Início, Treino, Exercícios, Nutrição, Água e Perfil (Exercícios ao lado de Treino, pedido do usuário).
- Versão atual visível no rodapé de Configurações (`APP_V`, vem do `CACHE` do `sw.js`). Desde a v59 o app compara com `version.json` publicado ao abrir/voltar e se recarrega sozinho (`checkUpdate`/`hardReload`); botão manual "Verificar e atualizar o app" em Configurações. Detalhes em `references/publicacao-github.md`.
- Dados por perfil em `carga.v1.<id>`; dados do aparelho compartilhados entre perfis em `carga.shared` (receitas).
- Prévia publicada como Artifact: https://claude.ai/artifact/VtiM8zsMVrkBCHTSnkvoJ6. Republique com o mesmo `file_path`. Quando as imagens mudarem, passe `files` com `img/...`.
- Detalhes, convenções e armadilhas: `references/arquitetura.md`.

## Rotina de entrega (a cada mudança)

1. Edite `app.html` ou os geradores em `tools/`.
2. Aumente o número do `CACHE` em `sw.js` (`carga-vNN`), senão o celular continua com a versão antiga.
3. Rode `python3 build.py`.
4. Teste com Playwright em `dist/`. Sirva com `python3 -m http.server 8765` dentro de `dist/` (em segundo plano) e use `NODE_PATH=$(npm root -g)`. Para pular a senha, grave `sessionStorage['carga.ok']` com o hash de `LOCK`; para não cair no reset geral, grave `localStorage['carga.reset']='2026-10-17'` antes de semear dados. Confira erros de console e tire prints.
5. Faça o commit com autor `Samuel Costa <samuel.costa@unilever.com>`, seguindo as regras de atribuição da sessão, e `git push origin main`. O GitHub Actions publica no Pages; confira com `gh run list -R xSam10-10/Carga --limit 1`.
6. Republique o Artifact de prévia.
7. Mande prints ao usuário (zips só se ele pedir).
8. Atualize o roadmap e o painel visual (seção abaixo) e, se aprendeu algo novo, esta skill.

GitHub e Pages (site no ar em https://xsam10-10.github.io/Carga/): `references/publicacao-github.md`.

## Roadmap e painel visual

- **Fonte única:** `references/roadmap.json`, com módulos (progresso de 0 a 1), itens (status `pronto`, `parcial`, `a fazer` ou `sugestão`), próximos passos, referências de outros apps e entregas. O `roadmap.md` é **gerado**; não o edite à mão.
- **Painel** "Roadmap do Carga" (artifact do tipo Dashboard): https://claude.ai/artifact/T86Moh6PbAnUH4K5Hr6Bk6. Ele mostra o progresso geral, as barras por módulo, os itens por situação (com filtro), os próximos passos e as entregas. O código da página está em `scripts/painel-roadmap.html`, gravado no documento `files/index.html` do painel.
- **Para atualizar depois de uma entrega:**
  1. Edite `roadmap.json`: mude o status dos itens, o progresso do módulo e acrescente a entrega com a data.
  2. Rode `python3 scripts/roadmap.py <pasta>`. Isso regenera o `roadmap.md` e cria `modulos.json`, `itens.json`, `proximos.json` e `entregas.json` na pasta.
  3. Suba cada JSON como asset do painel: Artifact `publish` com `url` do painel, `asset: true` e `file_path`, um arquivo por chamada.
  4. Com ArtifactData, faça `update` em `datasets/<id>` com o novo `source.url` (devolvido pelo upload), `source.name` e `updated: {at, by}`. Leia antes para obter a versão.
  5. Apague os assets antigos (Artifact `delete` com `path` igual ao id).
- **Se a página do painel mudar:** grave `{text: <conteúdo de scripts/painel-roadmap.html>}` em `files/index.html`.

## Onde está cada conhecimento

| Assunto | Arquivo |
|---|---|
| Código, estado, telas, ações, armazenamento, testes | `references/arquitetura.md` |
| Logo, abertura, temas, cores, tipografia, componentes | `references/identidade-visual.md` |
| Mapa corporal hiper-realista, avatar de água, imagens de exercícios, ícones | `references/imagens-e-avatares.md` |
| Tudo que o app já faz, tela por tela | `references/funcionalidades.md` |
| Visão, status de cada módulo, próximos passos e sugestões | `references/roadmap.md` |
| GitHub, Pages, zips, instalação no celular | `references/publicacao-github.md` |
| Decisões tomadas e o motivo de cada uma | `references/decisoes.md` |

## Arquivos-fonte guardados nesta skill (`assets/`)

Ficam aqui para reconstruir os visuais mesmo se o repositório se perder:
- `assets/musculos/*.webp`: as 17 artes hiper-realistas aprovadas, uma por grupo muscular. Os nomes de arquivo são os que `tools/build_body.py` espera.
- `assets/silhuetas-agua.webp`: arte aprovada das silhuetas masculina e feminina do avatar de água.
- `assets/logo-carga.svg` (símbolo + palavra) e `assets/icon.svg` (ícone do app).

## Mantendo esta skill viva

Sempre que uma decisão nova for tomada, uma tela nova entrar ou um processo mudar:
- atualize a referência certa e o roadmap;
- se a mudança for grande, registre em `references/decisoes.md` com a data e o motivo;
- a cópia oficial fica no repositório em `.claude/skills/carga-app/`, junto do código. Para levar ao perfil do usuário, reempacote e mande o `.skill`.
