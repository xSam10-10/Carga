# O que o app já faz (estado em 17/10/2026, versão do cache carga-v22)

## Abertura e perfis
- **Senha de entrada** logo após a abertura: teclado numérico de 8 dígitos sobre o mesmo fundo preto, pedida a cada abertura do app (não pede de novo ao recarregar na mesma sessão). Senha errada faz os pontos tremerem e mostra um aviso. Código: `LOCK` e `lockHash` em `app.html`.
- **Abertura no estilo do Hevy:** tela preta e o símbolo parado no centro por 2,6 s, depois um esmaecimento curto até o app.
- **Escolha de perfil** ("Quem vai treinar neste celular?"):
  - cada perfil tem dados totalmente separados;
  - dá para adicionar, renomear, trocar e excluir;
  - foto ou iniciais como avatar.

## Início
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
  - recorde ao vivo;
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
- **Folha de porção:** quantidade em g (−/+, atalhos 50/100/150/200 g e "1 porção" para alimentos próprios), barra de macros em %, tabela nutricional completa e estrela de favorito.
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
- **Saúde:** dados corporais (sexo, nascimento, altura, nível de atividade, objetivo) e os indicadores com fonte citada.
- **Configurações:**
  - tema (6) e cor de destaque (15);
  - início da semana, modo da coluna "Anterior", recorde ao vivo, dicas, descanso padrão, som, vibração, notificações;
  - **Dados:** backup (JSON), exportar CSV, cópias automáticas no aparelho, restaurar, **importar histórico do Hevy (CSV)**.

## PWA
- Instalável, funciona offline (service worker com cache versionado) e tem ícones para Android e iPhone.
- O ícone do app é verde com o símbolo branco.
