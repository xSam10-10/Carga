# O que o app já faz (estado em 17/10/2026, versão do cache carga-v22)

## Abertura e perfis
- **Senha de entrada** logo após a abertura: teclado numérico de 8 dígitos sobre o mesmo fundo preto, pedida a cada abertura do app (não pede de novo ao recarregar na mesma sessão). Senha errada faz os pontos tremerem e mostra um aviso. Código: `LOCK` e `lockHash` em `app.html`.
- **Abertura no estilo do Hevy:** tela preta e o símbolo parado no centro por 2,6 s, depois um esmaecimento curto até o app.
- **Escolha de perfil** ("Quem vai treinar neste celular?"):
  - cada perfil tem dados totalmente separados;
  - dá para adicionar, renomear, trocar e excluir;
  - foto ou iniciais como avatar.

## Início
- **Meta de hoje** (primeiro cartão, `homeNutri`):
  - objetivo (toque leva a Dados pessoais) e quanto **falta** em kcal, com anel de %;
  - Meta, Consumido (soma da aba Nutrição) e Exercício (calorias do relógio no dia);
  - a conta da meta escrita por extenso;
  - aviso quando há treino de hoje sem calorias registradas;
  - barras de **Proteína, Carboidrato e Gordura** com "Faltam X g".
- Faixa da semana: dias com treino ficam marcados com a cor de destaque, e o dia de hoje é destacado.
- Botão "Retomar treino em andamento".
- **Cartão de saúde**, que se atualiza quando os dados mudam: IMC, TMB, gasto diário, meta de água e outros indicadores.
- Lembrete de backup ("Fazer backup" ou "Lembrar depois").
- **Seus treinos:**
  - os **últimos 10 treinos**, cada um num cartão com mapa corporal (frente e costas) e os grupos treinados acesos;
  - no cartão: dia, nome, tempo, séries, volume e as etiquetas dos grupos com o número de séries;
  - botão para ver todos no Perfil.

## Treino
- **Rotinas e pastas:** criar, editar, duplicar, reordenar e recolher. "Explorar" traz modelos prontos. Também dá para iniciar um treino vazio.
- **Sessão ao vivo:**
  - séries com tipos (normal, aquecimento etc.) e coluna "Anterior" pareada corretamente;
  - marcar a série feita, cronômetro de descanso com som, vibração e notificação, e a tela fica acesa;
  - superséries com rolagem automática;
  - notas fixas por exercício;
  - sugestão de progressão de carga (`overloadHint`), gerador de aquecimento (40%, 60% e 80%) e calculadora de anilhas;
  - recorde ao vivo, como no Hevy (`livePR`, `prPop`, `confetti`):
    - a série que bate recorde ganha uma medalha dourada no lugar do número;
    - uma bolinha com a medalha salta no topo e se abre num balão com a foto e o nome do exercício, alternando os recordes batidos na ordem do Hevy (Maior peso, Melhor volume de série, Melhor 1RM; Mais repetições em peso corporal), cerca de 1,6 s cada;
    - **som do recorde** (`prChime`), tocado 0,38 s após o toque, como no Hevy: arpejo em Fá maior (Fá4 349 Hz, Lá4 440, Dó5 523, Fá6 1.397) com timbre de sino (parciais 1×, 2× e 4×, decaimento τ≈0,3 s). Foi medido do vídeo do Hevy e é **sintetizado** com Web Audio, sem usar o arquivo de áudio deles. Respeita a opção de som;
    - confetes nas cores da medalha e do destaque (o Hevy não tem; foram um pedido do usuário; desligados com "reduzir movimento") e vibração;
    - só conta quando já existe histórico do exercício;
  - tipos de registro por exercício: peso e repetições, peso corporal, assistido, duração, distância e duração.
- **Finalizar:** resumo, recordes batidos e opção de salvar como rotina. Ao abrir, um pop-up pede as **calorias gastas** que o relógio mostrou (dá para pular). O valor fica em `w.kcal` e aparece no resumo, no detalhe do treino (dá para informar ou alterar depois pelo menu ⋯) e nos cartões. Código: `kcalSheet`, `kcalBox`, ações `kcalLive` e `kcalSaved`.
- **Detalhe do treino:** editar ou excluir.

## Exercícios
- Catálogo com ~465 exercícios em português e fotos de execução animadas (2 quadros).
- Passo a passo e dicas por equipamento.
- **Filtros por equipamento e por grupo muscular** (folha com ícones), mais busca.
- **Criar exercício** próprio: nome, equipamento, músculo principal, secundários e tipo.
- **Detalhe do exercício:** histórico, gráficos (melhor série, volume, 1RM estimado etc.), recordes e músculos trabalhados no mapa corporal.

## Nutrição (aba própria, referência: Samsung Health › Refeição)
- **Tela do dia** (‹ Hoje ›):
  - calorias consumidas, meta e faixa recomendada (±10%), com barra e marcador da meta;
  - cartão de macronutrientes: gramas × meta e barra "Real × Recomendado" em %;
  - as 6 refeições (Café da manhã, Lanche da manhã, Almoço, Lanche da tarde, Jantar, Ceia), com kcal e alimentos;
  - mini gráfico dos últimos 7 dias.
- **Editor de refeição:**
  - tipo de refeição (se trocar para um tipo que já tem registro no dia, os itens são juntados) e hora;
  - total de kcal e macros;
  - alimentos com − e + (meia porção por toque) e toque no item para a folha de porção;
  - "Adicionar alimento", "Adicionar calorias" (calorias rápidas, sem alimento), "Salvar como refeição pessoal" e "Excluir".
- **Seletor de alimentos:**
  - busca sem acento e filtro por categoria da TACO;
  - abas Todos, Favoritos, Meus alimentos e Minhas refeições;
  - seleção múltipla com botão fixo "Adicionar N item(ns)";
  - fora do modo de seleção, mostra só a ficha do alimento.
- **Folha de porção:** quantidade em g **digitável** (o toque seleciona o número inteiro, a tabela e as macros recalculam enquanto digita, Enter salva), mais −/+, atalhos 50/100/150/200 g e "1 porção" para alimentos próprios, barra de macros em %, tabela nutricional completa e estrela de favorito.
- **Criar alimento:** valores da embalagem por porção; o app converte para 100 g.
- **Nutrientes do dia:**
  - proteína, fibras, saturada, colesterol, sódio, potássio, cálcio, ferro, magnésio, zinco e vitaminas C e A;
  - barra com faixas abaixo, dentro e acima, com mínimo e máximo por sexo (DRI/IOM; sódio 2.300 mg; saturada até 10% das kcal);
  - os 3 alimentos que mais contribuíram.
- **Tendências:** o mesmo seletor de período do app (7 dias, Mês, Ano, Tudo; por dia, semana ou mês).
  - Calorias: média por dia registrado, média por refeição e barras com linha da meta.
  - Macronutrientes: média em g e %, e barras empilhadas em kcal.
- **Metas:**
  - automática: Mifflin × atividade × objetivo, proteína pela faixa ISSN, gordura 25%, carboidrato no resto;
  - personalizada: kcal e % de cada macro.
- **No Início:** cartão "Nutrição hoje" com kcal e macros do dia.

## Água (aba própria)
- **Meta diária calculada:**
  - 35 ml/kg para homens e 31 ml/kg para mulheres (EFSA);
  - mais 500 ml por hora de treino no dia;
  - dá para ajustar à mão.
- Copos rápidos (200, 300, 500 e 750 ml) e "Outro". Os registros do dia podem ser apagados.
- **Avatar de água** com a silhueta aprovada, masculina ou feminina, enchendo com onda na cor de destaque.
- Sequência de dias batendo a meta e gráfico por período.

## Perfil
- Cabeçalho com foto, número de treinos e gráfico (duração, volume ou repetições) com seletor de período.
- **Estatísticas:**
  - mapa corporal dos últimos 7 dias, que filtra pelo dia tocado;
  - séries por grupo muscular, radar por região e evolução por músculo;
  - exercícios mais feitos;
  - todos os gráficos com período de 7 dias, mês, ano ou desde o início, por dia ou por semana.
- **Relatório mensal e calendário** (dias treinados, sequência de semanas).
- **Medidas:** peso, cintura e outras, com gráficos.
- **Dados pessoais:** sexo, nascimento, altura, peso, nível de atividade (5 níveis por frequência semanal; automático pelos treinos), **objetivo** (Perder peso, Manter peso, Ganhar peso, Ganhar massa muscular) e **como calcular o gasto** (Automático, Pelo relógio, Pelo nível), com a conta resumida (basal, gasto, ajuste, meta e macros).
- **Saúde:** IMC, TMB, "Gasto e meta de hoje" com a meta dos 4 objetivos e a variação esperada por semana, macronutrientes por dia, água, cintura/altura, composição e evolução do peso, sempre com fonte citada.
- **Configurações:**
  - tema (6) e cor de destaque (15);
  - início da semana, modo da coluna "Anterior", recorde ao vivo, dicas, descanso padrão, som, vibração, notificações;
  - **Dados:** backup (JSON), exportar CSV, cópias automáticas no aparelho, restaurar, **importar histórico do Hevy (CSV)**.

## PWA
- Instalável, funciona offline (service worker com cache versionado) e tem ícones para Android e iPhone.
- O ícone do app é verde com o símbolo branco.

## Meus dados (central de dados do perfil) — 17/10/2026
- **Regra do usuário:** todo dado que a pessoa preenche fica concentrado em **Perfil → Meus dados** (view `dados`): corpo (sexo, nascimento, altura, peso), medidas, dias de treino por semana, objetivo e modo de cálculo, meta de nutrição, meta de água, nome/foto/aparência. Outros lugares só levam para lá.
- Cartão `myDataCard()` no topo do Perfil, com o progresso de `myDataChecks()` (6 itens) ou o resumo quando completo.
- **Reset geral (17/10/2026):** `RESET_ID` zera todos os perfis uma vez por aparelho; os dados antigos vão para `carga.old.*` e voltam em Configurações → "Restaurar dados de antes do reset". Testes Playwright precisam gravar `localStorage['carga.reset']=RESET_ID` antes de semear dados.
- **Assinatura:** "by Samuel Costa" discreto (`.byline`) no rodapé de Configurações.

## Aba Exercícios (view `ativ`) — 17/10/2026
- Referência: "Meus exercícios" do Samsung Health (vídeos do usuário). **Só o que funciona offline**: nada de GPS, mapa, cronômetro ao vivo ou leitura do relógio.
- 6ª aba da barra (`ativ`); a antiga tile "Exercícios" do Perfil (catálogo de musculação) virou "Catálogo".
- Catálogo `AEX` (53 itens em 8 categorias `ACAT`; unidade de distância km, m ou nenhuma) + criados pelo usuário em `S.exCustom`; favoritos em `profile.exFav` (padrão caminhada, corrida, bicicleta, natação).
- Registro `ativForm`: **calorias obrigatórias** (não salva sem); duração, distância (só nos que têm unidade), frequência cardíaca média e notas são opcionais. Salvo em `S.extra` `{id,t,ex,name,kcal,dur,dist(km),hr,notes}`; natação digita metros e guarda km.
- `exKcalOn` soma `S.extra` na meta do dia (exercício entra por inteiro); a meta de água soma +500 ml por hora também desses exercícios.
- Tela da aba: resumo de hoje, favoritos (todos; o atalho do Início mostra até 12 + "Mais"), gráfico de calorias por período (`perCtl('ativ')`) e registros por dia, incluindo os treinos de musculação. Detalhe `ativDet` com ritmo/velocidade calculados. Atalho "Exercício" no Início (`homeAtiv`).
- Frequência cardíaca aqui é só informação opcional pedida pelo usuário; não entra em nenhum cálculo (regra 6 continua).


## Evolução do corpo (view `medidas`, título "Evolução do corpo") — 18/10/2026
- Regra do usuário: tudo o que é preenchido e pode mudar precisa de histórico com gráfico e comparação (semana a semana, mês a mês, desde o início, ano contra ano).
- Séries (`EVO`, `evoSeries`): peso, IMC, gordura corporal, massa magra, massa gorda, cintura, cintura/altura, peito, braço, coxa, quadril, panturrilha, altura e taxa basal. Os derivados usam a altura da data (`heightAt`); a altura tem histórico próprio em `S.hLog`, gravado a cada alteração em Meus dados (`logHeight`). O peso de Meus dados grava em `S.measures`.
- Tela: chips de medida, valor atual, gráfico com `perCtl('med')` (registros, média por semana ou por mês), "Comparar com" (1 semana, 1 mês, 3 e 6 meses, 1 ano, primeiro registro), "Mês a mês" (média do mês, variação vs mês anterior e vs mesmo mês do ano anterior) e lista de registros.
- Acesso: tile "Evolução" no Painel do Início, cartão `evoCard()` em Estatísticas, "Ver evolução" em Meus dados.
- 18/10/2026: a seção **Painel** (Estatísticas, Catálogo, Evolução, Calendário, Saúde, Meus dados) saiu do Perfil e fica no **Início**, logo abaixo do cartão "Esta semana" (pedido do usuário).
- 18/10/2026 (regra do usuário): **todo formulário de preenchimento fica só na aba Perfil.** Links de outras abas usam a ação `goPf` (troca para a aba Perfil e abre Meus dados, metas de nutrição ou configurações por dentro dela). Removidos: tile "Meus dados" do Painel do Início, engrenagem da Água, "Metas de nutrição" do menu da Nutrição, "Registrar" e edição de linhas na Evolução. Medidas se registram/corrigem em Meus dados → Medidas → "Editar registros" (view `medLista`). A Evolução é só consulta.
