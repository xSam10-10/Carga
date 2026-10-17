# O que o app já faz (estado em 17/10/2026, versão do cache carga-v22)

## Abertura e perfis
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
- **Finalizar:** resumo, recordes batidos e opção de salvar como rotina.
- **Detalhe do treino:** editar ou excluir.

## Exercícios
- Catálogo com ~465 exercícios em português e fotos de execução animadas (2 quadros).
- Passo a passo e dicas por equipamento.
- **Filtros por equipamento e por grupo muscular** (folha com ícones), mais busca.
- **Criar exercício** próprio: nome, equipamento, músculo principal, secundários e tipo.
- **Detalhe do exercício:** histórico, gráficos (melhor série, volume, 1RM estimado etc.), recordes e músculos trabalhados no mapa corporal.

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
