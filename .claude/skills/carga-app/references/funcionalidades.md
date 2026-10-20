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
- Tela da aba: resumo de hoje, favoritos (todos; o atalho do Início mostra até 12 + "Mais"), gráfico de calorias por período (`perCtl('ativ')`) e registros por dia, incluindo os treinos de musculação. Detalhe `ativDet` com ritmo/velocidade calculados. O atalho "Exercício" (`homeAtiv`) saiu do Início em 18/10/2026 (v63).
- Frequência cardíaca aqui é só informação opcional pedida pelo usuário; não entra em nenhum cálculo (regra 6 continua).


## Evolução do corpo (view `medidas`, título "Evolução do corpo") — 18/10/2026
- Regra do usuário: tudo o que é preenchido e pode mudar precisa de histórico com gráfico e comparação (semana a semana, mês a mês, desde o início, ano contra ano).
- Séries (`EVO`, `evoSeries`): peso, IMC, gordura corporal, massa magra, massa gorda, cintura, cintura/altura, peito, braço, coxa, quadril, panturrilha, altura e taxa basal. Os derivados usam a altura da data (`heightAt`); a altura tem histórico próprio em `S.hLog`, gravado a cada alteração em Meus dados (`logHeight`). O peso de Meus dados grava em `S.measures`.
- Tela: chips de medida, valor atual, gráfico com `perCtl('med')` (registros, média por semana ou por mês), "Comparar com" (1 semana, 1 mês, 3 e 6 meses, 1 ano, primeiro registro), "Mês a mês" (média do mês, variação vs mês anterior e vs mesmo mês do ano anterior) e lista de registros.
- Acesso: tile "Evolução" no Painel do Início, cartão `evoCard()` em Estatísticas, "Ver evolução" em Meus dados.
- 18/10/2026: a seção **Painel** (Estatísticas, Catálogo, Evolução, Calendário, Saúde, Meus dados) saiu do Perfil e fica no **Início**, logo abaixo do cartão "Esta semana" (pedido do usuário).
- 18/10/2026 (regra do usuário): **todo formulário de preenchimento fica só na aba Perfil.** Links de outras abas usam a ação `goPf` (troca para a aba Perfil e abre Meus dados, metas de nutrição ou configurações por dentro dela). Removidos: tile "Meus dados" do Painel do Início, engrenagem da Água, "Metas de nutrição" do menu da Nutrição, "Registrar" e edição de linhas na Evolução. Medidas se registram/corrigem em Meus dados → Medidas → "Editar registros" (view `medLista`). A Evolução é só consulta.

## Entrega de 18/10/2026: Nutrição v2, Central de metas, Fotos, Painel do dia, Lembretes de água
- **Copiar de ontem:** chip "Copiar do dia anterior" na Nutrição (e no menu ⋯) copia todas as refeições do dia anterior para o dia mostrado; no editor da refeição, "Copiar de ontem" copia só aquela refeição (`copyMeals`, `prevKey`).
- **Planos de dieta** (view `planos`, menu ⋯ e chip da Nutrição): 3 planos sugeridos (A/B/C) gerados com alimentos TACO (`PLAN_T`, `PLAN_SH` calorias e `PLAN_PSH` proteína por refeição, `genPlan`) para a meta do dia; porções calculadas priorizando a proteína e fechando as calorias pelo carboidrato (ficam ~±10% da meta). "Usar no dia" (substituir ou somar), "Salvar em meus planos", e "Salvar este dia como plano" (menu). Dados em `S.plans`.
- **Código de barras:** câmera com `BarcodeDetector` (offline) ou número digitado. Código já conhecido (`S.barcodes`) → alimento na hora, sem internet. Novo → Open Food Facts quando há internet (cria em Meus alimentos por 100 g); sem internet ou não encontrado → cadastro com o código já ligado. Botão em Alimentos, no editor da refeição, no chip e no menu da Nutrição.
- **Central de metas** (view `metas`, tile "Metas" no Painel do Início): peso, gordura e cintura com progresso desde que a meta foi definida e **previsão de chegada** pela regressão linear das últimas 6 semanas (`trendPerWeek`, `goalForecast`); treinos por semana (semanas batidas das últimas 8, contando exercícios avulsos); proteína média (meta própria ou do plano); hábitos de 7 dias (água e calorias na faixa). Metas definidas em Meus dados → Metas (`profile.goals` {weight, fat, waist, prot, wpw, since}).
- **Fotos de evolução:** adicionar/excluir em Meus dados → Fotos de evolução (posição frente/lado/costas, data); guardadas no IndexedDB `carga` v2, loja `fotos` (JPEG até 1280 px; **não entram no backup**). Comparação antes/depois por posição, com o peso de cada data, na Evolução do corpo (`fotoCompare`, só consulta).
- **Painel do dia** (`homeDay`, primeiro cartão do Início), layout definido pelo usuário: 1ª linha Proteína, Carboidratos, Gordura (consumido x meta); 2ª linha Calorias consumidas (x meta), Calorias gastas (rotina + exercício, `E.gasto`) e Déficit/Superávit = consumido − gasto, com a meta do objetivo (`E.adj`); 3ª linha Água (x meta), Treino e Exercício. Sono fica num botão abaixo dos anéis. Sono é registrado tocando no anel (`S.sleep[dkey]`, horas); meta de sono em Meus dados → Metas (`profile.sleepGoal`, padrão 8 h).
- **Lembretes de água** (Meus dados → Água): liga/desliga, intervalo (1 h, 1h30, 2 h, 3 h) e horário. Avisa quando passa o intervalo desde o último copo, dentro da janela, até bater a meta (`profile.wr`, `wrNext`, `wrTick` a cada minuto e ao voltar para o app). Notificação do sistema quando o app está em segundo plano e a permissão foi dada; toast dentro do app. Limitação: sem servidor de push, não dispara com o app totalmente fechado.

## Entrega de 18/10/2026 (v44): Resumo, volume semanal, recuperação, ciclo de carboidrato, conquistas
- **Resumo de saúde** (view `resumo`, tile "Resumo" no Painel do Início): semana ou mês, navegável para trás; treino (sessões, tempo, volume, calorias de exercício, recordes), alimentação (média de kcal e proteína dos dias registrados, dias na faixa), água (média e dias com meta), sono (média) e peso (variação). Compara com o período anterior; no período em andamento compara com os mesmos dias do anterior (`periodStats`, `rangeOf`).
- **Volume semanal por músculo** (Estatísticas, `volSection`): séries dos últimos 7 dias contra a faixa recomendada (10–20 nos grandes, 4–12 nos auxiliares; Schoenfeld 2017), cores abaixo/na faixa/acima e alerta de **grupo esquecido** (músculo grande sem série em 14 dias).
- **Recuperação muscular** (Estatísticas, `recSection`): mapa hiper-realista colorido pelo quanto falta recuperar e lista com % e horas restantes; 36 h (<6 séries), 48 h (6–9) ou 72 h (≥10) desde o último treino do músculo.
- **Ciclo de carboidrato** (Meus dados → Nutrição, `profile.carbCycle`): dia com treino (musculação ou avulso) +15% de carboidrato, dia sem treino −20%; a gordura compensa (mínimo 0,6 g/kg) e as calorias não mudam. Aplicado em `energyPlan` (`carbCycle`, campo `cyc`).
- **Conquistas** (view `conquistas`, tile no Painel): 33 conquistas em níveis (treinos, semanas seguidas, recordes, toneladas, exercícios avulsos, km, água, sequência de água, diário, sono, meta de peso), com medalha, progresso e "Mais perto". Aviso (toast) ao desbloquear, checado ao abrir o Início (`achCheck`, `S.achSeen`). Sem rede social: nada é publicado.
- 18/10/2026: data de nascimento em Meus dados é um campo de texto numérico com máscara DD/MM/AAAA (digita só os números, as barras entram sozinhas; `pdBirth`), gravada em ISO em `profile.birth` quando válida; data inválida fica em vermelho com aviso.
- 18/10/2026: **todas as datas digitáveis** usam a mesma máscara DD/MM/AAAA só com números (classe `.dmask`, helpers `dmask`, `isoOf`, `brDate`): nascimento, data das medidas, das fotos de evolução e dos exercícios avulsos. Não há mais `type="date"` no app; datas futuras ou impossíveis ficam em vermelho e não são gravadas.
- 18/10/2026: nas datas de medidas, fotos e exercícios avulsos, além de digitar há um **botão de calendário** dentro do campo (`.dwrap`, `.dcal`, ação `dPick` com `showPicker()` num `input type=date` oculto `.dhid`, que devolve a data para o campo de texto). A data de nascimento fica **só com digitação** (pedido do usuário).
- 18/10/2026: treino sem nenhuma série marcada pode ser encerrado: "Finalizar" pergunta "Encerrar sem salvar?" e descarta (`discardNow`), sem ir para o histórico. Na aba Treino e no Início, abaixo de "Retomar treino em andamento", há "Descartar treino em andamento" (com confirmação).
- 18/10/2026 **Receitas** (Nutrição → Adicionar alimento → aba **Receitas**, view `receita`): criar/editar/excluir receitas juntando alimentos (ingredientes com gramas), peso da receita pronta opcional e rendimento em porções. Salva em `S.foods` com `recipe:true`, `ing`, `cooked`, `serv` e nutrientes por 100 g (porção = peso/porções); entra na dieta como um alimento só (aparece também na busca e em Meus alimentos). A folha de porção ganhou **"Ou digite as calorias"** (`n:pkc`), que converte kcal em gramas — vale para qualquer alimento.
- 18/10/2026 **Produtos de marca embutidos** (`BRAND`, `brandRows`, ids `x-…`): cadastrados no código a partir da foto da tabela nutricional enviada pelo usuário (valores da porção convertidos para 100 g), valem para **todos os perfis** e aparecem na busca e em Meus alimentos. Atuais: Whey Protein Concentrado · DUX (porção 30 g: 123 kcal, carb 5,9 g, prot 20 g, gord 2,1 g, sat 1,3 g, sódio 116 mg) e Whey Protein Concentrado · Black Skull (porção 30 g: 115 kcal, carb 2,5 g, prot 25 g, gord 0,6 g, sat 0, sódio 65 mg; tabela tirada de um print de loja, conferir com a embalagem).
- 18/10/2026 **Atividade diária** (`homeActivity`, logo abaixo de "Esta semana" no Início; referência visual: "Atividade diária" do Samsung Health). **Sem passos** (o usuário não terá esse dado): semana com mini corações por dia e coração grande com 3 anéis de **calorias do relógio** — Calorias gastas (verde, treino + exercícios), Em treino (azul, musculação) e Em exercícios (roxo, avulsos). Metas (`actGoals`) estimadas: calorias ativas = (MET − 1) × taxa basal/24 × horas; treino 5 MET (6 MET com 6+ dias/semana) por 60 min; exercício 4,5 MET (3,5 com menos de 3 dias) por 30 min (OMS 150–300 min/sem); METs do Compêndio (Ainsworth 2011). Editáveis em Meus dados → Metas (`profile.actGoals` {treino, ex}; em branco = automático). Mostra também o **gasto basal (só para viver)** = TMB, o total gasto no dia (`E.gasto`), tempo ativo e distância.
- 18/10/2026: na receita, cada ingrediente tem **campos de gramas e de calorias editáveis na própria lista** (`n:rci`, um acompanha o outro; o toque seleciona o número para digitar por cima), com macros do ingrediente e resumo atualizados na hora. O alimento entra com a porção padrão, mas é só ajustar.
- 18/10/2026: o **editor da refeição** usa a mesma linha da receita (`qtyRow`): gramas e calorias editáveis em cada alimento, ligados por proporção (kcal = g × kcal/100 g; nutrientes proporcionais aos gramas), macros do item e total da refeição (`mealTot`, `#m-tot`) atualizados na hora; tocar no nome abre a folha com todos os nutrientes. Na folha de porção, os campos de gramas e de calorias ficam sincronizados.
- 18/10/2026 **Banco de alimentos** (view `banco`; Nutrição → chip "Banco de alimentos" ou menu ⋯): lista os ~593 alimentos (TACO, marcas, meus e receitas) com busca e filtros (Todos, Meus, Receitas, Marcas, TACO, Excluídos), valores por 100 g e porção; criar alimento/receita/código de barras; **editar** alimentos próprios (`bkEdit` reaproveita `novoAlimento` com `p.edit`) e receitas; **excluir** = ocultar (`S.foodHidden`): some da busca/listas de escolha, mas refeições já registradas mantêm os valores; restaurar em "Excluídos".
- 18/10/2026 **Receitas compartilhadas**: ficam no espaço do aparelho `localStorage['carga.shared'].recipes` (`shd`, `shRec`, `shSave`), visível para **todos os perfis do mesmo celular**; receitas antigas dentro do perfil migram sozinhas (`nS`). Excluir uma receita tira dos dois perfis. O backup leva `sharedRecipes` e, ao restaurar, elas voltam para o espaço compartilhado.
- **Entre celulares não há sincronização automática** (o app não tem servidor — regra 2). Banco de alimentos → **"Enviar receitas"** gera um código de texto `CARGA1:…` (receitas + alimentos próprios usados nelas) para copiar e mandar; no outro celular, **"Receber receitas"** e colar: importa (novas) ou atualiza (mesmo id).
- 18/10/2026 (v63): ordem do Início: Painel de atalhos → Seu resumo de saúde (`homeHealth`) → Meta de hoje (`homeNutri`) → Painel do dia (`homeDay`) → Esta semana → Atividade diária (`homeActivity`). Removido o bloco Exercício (`homeAtiv`). "Seus treinos" (`homeCard`) passou a ser o primeiro bloco da aba Treino.
- 18/10/2026 (v64): corrigido o filtro de **grupo muscular/equipamento** em Adicionar exercícios. A ação `fPick` do filtro era sobrescrita pela `fPick` da lista de alimentos (mesmo nome em `A`); a dos alimentos virou `foodPick`. Regra: nomes de ação em `A` são globais — antes de criar uma, `grep` para evitar colisão. Com músculo filtrado, os exercícios em que ele é o principal vêm primeiro (os de músculo secundário depois).
- 18/10/2026 (v65): **cadastro obrigatório**. `gate()` (chamado no fim de `render`) mostra a tela "Antes de começar" (`#gate`, z-index 50, acima das abas e das folhas, abaixo do aviso de atualização e do toast) enquanto `gateMiss()` não estiver vazio: sexo, data de nascimento (idade 10–100), altura (100–250 cm), peso (20–400 kg, gravado em Medidas), dias de treino por semana e objetivo — os mesmos itens de `myDataChecks()`. Usa as mesmas ações de Meus dados (`pdSex`, `pdBirth`, `pd` altura, `pdWeight`, `pdDays`, `pdGoal`). Uma vez aberta, fica até "Começar a usar" (`gateOk`), mesmo que tudo já esteja preenchido (`UI.gate` = id do perfil). "Trocar perfil" leva à lista de perfis, que não é bloqueada. Valores digitados são preservados nas re-renderizações.
- 18/10/2026 (v66): **Início em capítulos** (revisão didática). `homeLead` (frase-resumo que muda ao longo do dia: meta do dia / faltam X kcal e Y g de proteína / dentro da meta ✓ / passou X kcal), `homeMyDay` (substitui Meta de hoje + Painel do dia: kcal que faltam, Meta·Consumido·Gasto, **Saldo do dia** — sem refeições mostra "Se comer a meta: +alvo"; depois o saldo real e o alvo —, macros com semáforo, água com copos rápidos, sono, "Como calculamos?" = `calcSheet` com a conta da meta, do gasto e do saldo), `homeSpend` (Atividade diária renomeada "Meu gasto": anel/caixa "Ativas" em vez de "Calorias gastas"; barra empilhada basal + rotina e digestão + treino + exercícios = gasto do dia), `homeBody` (Resumo de saúde enxuto: peso com variação de 30 dias ou desde o 1º registro, IMC, taxa basal, gordura ou altura). Saíram do Início as repetições de meta, gasto, proteína e água. Semáforo: `zKcal` (dentro = P.lo..P.hi, ±5%; âmbar até +15%; vermelho acima), `zMacro` (proteína é mínimo; carbo/gordura ±10%, âmbar até +25%). `homeHealth`, `homeNutri`, `homeDay` e `homeActivity` ficaram no código sem uso no Início.
- 18/10/2026 (v67): Água — todos os copos rápidos no verde forte; só "+ Outro" fica claro (antes o 1º copo ficava claro por sobra de layout, sem significado).
- 18/10/2026 (v68): o app sempre abre (e recarrega) no **Início**, inclusive ao trocar de perfil (antes abria em Treino quando não havia treinos). Perfil sem os dados das metas abre direto na tela de cadastro obrigatório (`gate`), por cima do Início.
- 18/10/2026 (v69): Meus dados e cadastro obrigatório — rótulo "Data de nascimento" sem a idade (quebrava em 2 linhas e desalinhava da Altura); a idade aparece abaixo do campo (`.fage`). `.row2` com align-items:start.
- 18/10/2026 (v70): primeiro bloco do Início virou **Metas de hoje** (`homeLead` + `homeLeadTxt`): frase-resumo + checklist com contador "N de M batidas" — Calorias (semáforo `zKcal`), Proteína (mínimo), Água, **Treino de hoje** (só musculação; mostra o nome do treino, "semana já batida" ou "ainda não · fez corrida"), **Treinos da semana** (treinos + exercícios; meta = `goals.wpw` ou dias de treino de Meus dados; vermelho se faltam mais treinos do que dias), Calorias ativas (vs `actGoals`), Sono (vs `sleepGoal`, padrão 8 h). Abaixo, **Metas de longo prazo** cadastradas (peso, gordura, cintura via `goalForecast`). Cada linha leva à tela correspondente.
- 18/10/2026 (v71): **Minha semana** (`homeWeek`) virou quadro de metas da semana (domingo a hoje): dias marcados (treinos e exercícios), Sessões/Tempo/Volume e checklist "N de 8 em dia": Treinos (vs `goals.wpw` ou dias de treino), Calorias na meta, Proteína na meta e Água na meta (X de N dias — conta só dias fechados, ou hoje se já bateu), Calorias ativas (semana vs soma das metas diárias), Sono (média vs meta), **Saldo da semana** (comido − gasto nos dias fechados com registro vs soma dos alvos do objetivo, com equivalência em gramas/kg) e Peso na semana (variação desde o último registro antes do domingo; verde se na direção do objetivo).
- 18/10/2026 (v72): Minha semana subiu para logo abaixo de Metas de hoje. Ordem: Metas de hoje → Minha semana → Meu dia → Meu gasto → Meu corpo → Explorar.
- 18/10/2026 (v73): **sono removido do app** (pedido do usuário: sem relógio integrado, não dá para lançar). Saíram: linha Sono de Metas de hoje e de Minha semana, botão de registro no Meu dia, ação `sleepLog`, `sleepOn`, meta de sono em Meus dados → Metas, "Sono por noite" no Resumo de saúde (seção virou "Água e corpo") e a conquista de noites registradas. Dados antigos em `S.sleep`/`profile.sleepGoal` ficam no armazenamento, sem uso. Textos "Início → Painel" viraram "Início → Explorar".
- 18/10/2026 (v74) — revisão aplicada (itens 1–5): data dos registros da aba Exercícios sem "De" maiúsculo; Nutrição com "dentro da meta: X a Y", semáforo na barra de calorias e nas metas dos macros, e **ordem única Proteína · Carboidrato · Gordura** (`MAC3`) em caixas, barra Real/Recomendado, gráfico de tendências, totais da refeição e tabela de nutrientes (o formulário de alimento novo segue a ordem do rótulo); aba Treino mostra os **3 últimos** treinos + "Ver todos" → nova tela **Todos os treinos** (`historico`); cartões de treino escondem Séries/Volume zerados; gráfico do histórico da Água começa no 1º dia com registro; **Perfil** sem tema/cor (já ficam em Configurações) e sem a lista de treinos — no lugar, atalhos "Todos os treinos" e "Configurações".
- 18/10/2026 (v75) — funcionalidades 6 a 10:
  - **Sugestão de carga** (`overloadHint`, progressão dupla): no início de cada exercício de carga mostra Suba / Mantenha / Reduza / Semana leve, com "Na última vez: kg × reps (RIR)". Faixa de reps = faixa da rotina (ex. 8-12) → senão a da fase → senão 8 a 12. Sobe se todas as séries chegaram ao topo ou RIR médio ≥ 3; reduz se metade das séries ficou abaixo da faixa com RIR ≤ 1; Semana leve = 90% da carga e 1–2 séries a menos. Toque aplica a carga (com vírgula). Passo por equipamento: `incOf`.
  - **RIR por série** (`st.rir` 0–4, "4+"): ao concluir série de carga/peso corporal aparece "Reps na reserva 0 1 2 3 4+"; depois vira etiqueta "RIR n" (toque para corrigir). Salvo em `cleanSet`; CSV exporta como RPE (10 − RIR) e importa a coluna `rpe`. Desligável em Configurações ("Perguntar reps na reserva").
  - **Fases de treino** (`PHASES`, `profile.block` {ph, start, weeks}, `blockNow`): Hipertrofia (8–12, 6 sem), Força (3–6, 4 sem), Semana leve (1 sem), em ciclo. Escolha e duração em Meus dados → Treino e objetivo; cartão "Fase de treino" na aba Treino com semana X de N e botão para começar a próxima ao terminar.
  - **Bi-set/supersérie**: já existia (menu ⋯ do exercício → "Supersérie com…", no treino e na rotina).
  - **Suplementos** (`profile.supps`, `S.suppLog[dkey]`): cadastro em Meus dados → Suplementos; marcação diária na linha "Suplementos N de M" de Metas de hoje (folha `suppSheet`) e "Suplementos X de N dias" em Minha semana.
  - Descartados pelo usuário: itens 11–16 da revisão (bebidas, bioimpedância, medidas por região, PDF, correlações, foto do prato) e todas as sugestões da pesquisa de mercado.
- 19/10/2026 (v76): **tempo das séries em min:seg**. Antes o cronômetro gravava minutos decimais (32 s = "0.54"), lido como 0 min 54 s. Agora `mmss` grava "0:32", `minIn` lê "m:ss" e o formato antigo, e a digitação usa máscara de micro-ondas (`tmask`: "130" → "1:30"). Cabeçalho "Min" virou "Tempo". **Descanso**: a barra inferior mostra "Descanso · faltam 1:24 de 1:30" (contagem regressiva, âmbar nos últimos 5 s) e a barra "Treino em andamento" das outras telas mostra "Descanso: 1:21" enquanto o descanso corre.
- 19/10/2026 (v77): "Criar" saiu da tela Adicionar exercícios (picker). A aba Treino ganhou os botões **Catálogo** (lista completa de exercícios, com "Criar" no topo) e **Novo exercício** (abre direto o formulário de exercício personalizado), ao lado de Nova rotina e Explorar.
- 19/10/2026 (v78): **estrela amarela de favorito** (`favBtn`, ação `favT`) ao lado de cada alimento no editor da refeição/receita (antes do X) e em cada linha da lista de Adicionar alimento (`.frw`). Toque marca/desmarca; o alimento aparece na aba Favoritos. Desmarcada = contorno cinza; marcada = estrela amarela preenchida (#F2B705).
- 19/10/2026 (v79): Metas de hoje — Calorias, Proteína, **Carboidrato**, **Gordura** (novas linhas) e Água mostram ao lado a diferença consumido − meta (`dif`, etiqueta ".lg-d"): negativa = quanto falta (ex.: 1.500 / 2.530 kcal −1.030); positiva = passou (âmbar).
- 19/10/2026 (v80): iPhone — barra de abas "andava" para o meio da tela durante a rolagem por inércia (bug do WebKit com elementos position:fixed). Barras fixas (.nav, .mini, .restbar, .stickyb, .fdock e a faixa do topo) ganharam camada própria (translate3d(0,0,0), backface-visibility:hidden, will-change:transform). Não reproduzível no Chromium; confirmar no iPhone.
- 20/10/2026 (v82 base v81): bloco **Metas de hoje** (`homeLead`) saiu do Início por repetir o Meu dia. **Meu dia** (`homeMyDay`) virou o 1º bloco e ganhou no fim (`homeGoalsMini`) as seções **Treino** (Treino de hoje, Treinos da semana, Suplementos) e **Metas de longo prazo** (peso, gordura, cintura). Ordem do Início: Meu dia → Minha semana → Meu gasto → Meu corpo → Explorar. `homeLead` fica no código sem uso.
- 20/10/2026 (v82): nomes das categorias — aba **Treino → Musculação** e aba **Exercícios → Cardio** (barra de abas e títulos). Também: Meu gasto ("Em musculação", "Em cardio", barra Musculação/Cardio), Como calculamos ("Musculação e cardio"), Meus dados → Metas ("Calorias em musculação/cardio"), Meu dia ("Musculação de hoje"), telas da aba Cardio (Registrar cardio, Escolher atividade, Mais atividades, Calorias do cardio), títulos da sessão (Registrar musculação, Salvar musculação), catálogo de exercícios titulado "Catálogo". Mantidos: "exercício" quando é o movimento (Supino, Remada…) e "treino" como sessão (Seus treinos, Todos os treinos, Iniciar treino vazio, Treinos da semana, que soma musculação e cardio).
- 20/10/2026 (v83): bloco **Minha semana** (`homeWeek`) saiu do Início (redundante com Meu dia). No Meu dia, a seção "Treinos · esta semana" ganhou Sessões, Tempo e Volume da semana (domingo a hoje, musculação + cardio no tempo; volume só da musculação). Ordem do Início: Meu dia → Meu gasto → Meu corpo → Explorar.
- 20/10/2026 (v84): **Meu gasto** — os corações viraram **anéis circulares concêntricos** (estilo anéis do relógio da Apple; `heartRings` redesenhada, cores em `RINGS`): verde = Ativas, azul = Musculação, roxo = Cardio; trilho apagado, arco com degradê e ponta arredondada começando no topo; acima de 100% o arco dá mais uma volta com sombra na ponta. Vale para o anel grande e para os mini anéis dos dias da semana.
- 20/10/2026 (v85): **Meu corpo** (`homeBody`) saiu do Início. No lugar, seção **Métricas de saúde** com 5 blocos da tela Saúde (`healthCore`, extraída de `VIEWS.saude` e usada nas duas telas): IMC, Taxa metabólica basal, Gasto e meta de hoje, Água por dia, Macronutrientes por dia. Ordem do Início: Meu dia → Meu gasto → Métricas de saúde → Explorar.
- 20/10/2026 (v86): Macronutrientes por dia (Início e Saúde) — caixas na ordem Carboidrato, Proteína, Gordura (pedido do usuário; o destaque continua em g de proteína).
- 20/10/2026 (v87): **Explorar** (Início) ficou só com Resumo, Conquistas e Evolução. Saíram Metas, Calendário e Saúde (Calendário segue no ícone do topo do Início; a Central de metas abre pelas linhas "Treinos da semana" e "Metas de longo prazo" do Meu dia; a tela Saúde não tem mais atalho — seus 5 blocos principais estão no Início). **Catálogo** e **Estatísticas** passaram para a aba Musculação (quadro Nova rotina · Explorar · Catálogo · Novo exercício · Estatísticas).
- 20/10/2026 (v88): Macronutrientes por dia — número de destaque passou a ser as **calorias** da meta de hoje (`E.meta`, a mesma de Meu dia), no lugar de g de proteína.
- 20/10/2026 (v89): Macronutrientes por dia — caixas de volta à ordem Proteína, Carboidrato, Gordura (pedido do usuário; revoga a v86).
- 20/10/2026 (v90): atalho **Meus dados** saiu da aba Perfil (cartão `myDataCard`) e virou um quadro no **Explorar** do Início, ao lado de Evolução (Resumo · Conquistas · Evolução · Meus dados). Abre o formulário dentro da aba Perfil (`goPf`), mantendo a regra de formulários no Perfil.
- 20/10/2026 (v91): cartão **Fase de treino** saiu da aba Musculação (`blockCard` sem uso). A fase continua configurável em Meus dados → Treino e objetivo e segue valendo para a sugestão de carga.
- 20/10/2026 (v92): aba Musculação → Rotinas: quadro na ordem Nova rotina · Novo exercício · Iniciar treino vazio · Catálogo · Estatísticas · Explorar. "Iniciar treino vazio" deixou de ser um botão solto acima das Rotinas; com treino em andamento, "Retomar" e "Descartar" seguem no topo.
- 20/10/2026 (v93): **Seus treinos** (aba Musculação) virou carrossel horizontal (`.wcar`, scroll-snap): até os 10 treinos mais recentes lado a lado, um por vez; desliza com o dedo ou pelas setas ‹ › (ação `carStep`), com contador "N de M" atualizado na rolagem. Abaixo, "Ver todos os N treinos". Com 1 treino só, mostra o cartão sem setas.
- 20/10/2026 (v94): cartão **Evolução do corpo** saiu da tela Estatísticas (`evoCard` sem uso). A Evolução segue no Explorar do Início.
- 20/10/2026 (v95): **Estatísticas unificada com o Relatório mensal** (pedido: limpo, didático, sem repetição). Um único seletor de período no topo (7 dias · Mês · Ano · Tudo, `perOf('st')`) vale para: **Resumo** (Treinos, Tempo, Volume, Séries com ↑↓ / "= igual" vs período anterior de mesmo tamanho + sequência de semanas), **Frequência** (treinos por dia/semana/mês conforme o período), **Músculos trabalhados** (um mapa corporal + barras de séries por grupo, top 8), **Exercícios mais feitos** (top 5 + Ver mais) e **Evolução por músculo** (até 3, granularidade automática). Seção **Agora** (não depende do período): Volume semanal por músculo (faixa recomendada) e Recuperação muscular (só a lista, sem o 2º mapa). Saíram: link e conteúdo do Relatório mensal (resumo e frequência absorvidos; calendário do mês já existe em Calendário), mapa por dia dos últimos 7 dias, radar de distribuição (repetia as barras), "Desde o começo" (= período Tudo) e os seletores de período de cada bloco. `VIEWS.relatorio` fica no código sem atalho.
- 20/10/2026 (v97): Estatísticas — **Distribuição muscular** (radar por grupo, período escolhido × período anterior) voltou, entre Músculos trabalhados e Exercícios mais feitos.
