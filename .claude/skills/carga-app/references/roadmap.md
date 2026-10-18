# Roadmap do Carga: acompanhamento do desenvolvimento

> Gerado por `scripts/roadmap.py` a partir de `references/roadmap.json`. Edite o JSON, não este arquivo.
> Painel visual: https://claude.ai/artifact/T86Moh6PbAnUH4K5Hr6Bk6

**Objetivo:** O app de saúde mais completo do mercado: treino, dieta (macros e micros), água, medidas, metas e gráficos num lugar só, para o Samuel e a Carol.

Legenda: ✅ pronto · 🟡 parcial · ⬜ a fazer · 💡 sugestão aprovada para implementar aos poucos.

## Visão geral (progresso geral: 92%)

| Módulo | Status | Progresso | Resumo |
|---|---|---|---|
| 1. Treino | ✅ | 98% | Rotinas, sessão ao vivo, recordes, catálogo de 465 exercícios, mapa corporal e aba Exercícios (avulsos com calorias do relógio). |
| 2. Hidratação | ✅ | 92% | Meta por peso e sexo, copos rápidos, avatar animado, gráficos e lembretes de água. |
| 3. Corpo e medidas | ✅ | 85% | Meus dados, Evolução do corpo com comparações e fotos de evolução lado a lado. |
| 4. Nutrição | ✅ | 94% | Diário, TACO, macros e micros, metas, planos, código de barras, receitas compartilhadas, banco de alimentos, gramas/calorias ligados e produtos de marca. |
| 5. Metas e hábitos | ✅ | 88% | Objetivo com meta calórica, Central de metas com previsão, Painel do dia, sono e conquistas pessoais. |
| 6. Gráficos e relatórios | ✅ | 90% | Todos os gráficos com períodos, Evolução do corpo, Resumo de saúde da semana e do mês, volume semanal e recuperação muscular. |
| 7. Identidade e plataforma | ✅ | 95% | Logo, abertura, senha, 6 temas, 15 cores, perfis separados, pictogramas próprios, Painel no Início e formulários concentrados no Perfil. |
| 8. Publicação | ✅ | 95% | Site no ar com atualização automática forçada pela versão publicada; falta reinstalar para trocar o ícone da abertura. |

## 1. Treino
- ✅ Rotinas, pastas, modelos prontos e treino vazio
- ✅ Sessão ao vivo: tipos de série, coluna Anterior, descanso, superséries, notas
- ✅ Recordes ao vivo, progressão de carga, aquecimento, calculadora de anilhas
- ✅ Catálogo de 465 exercícios com fotos, passo a passo, filtros e criar exercício
- ✅ Mapa corporal hiper-realista com 17 grupos
- ✅ Importar histórico do Hevy
- ✅ Calorias do treino registradas do relógio (pop-up no fim do treino)
- ✅ Animação de recorde ao vivo: medalha, balão e confetes (estilo Hevy)
- 💡 Periodização em blocos (força, hipertrofia, deload)
- ✅ Volume semanal por grupo com faixa recomendada e alerta de grupo esquecido
- ✅ Mapa de recuperação muscular
- 💡 RPE e RIR por série
- 💡 Animações próprias para exercícios sem foto
- ✅ Aba Exercícios: 53 exercícios avulsos (caminhada, corrida, bicicleta, natação…), favoritos, criar exercício, calorias obrigatórias e distância/FC opcionais
- 💡 Integração com Health Connect (exige app Android nativo; aguardando decisão)
- ✅ Encerrar treino vazio sem salvar e descartar treino em andamento pela aba Treino

## 2. Hidratação
- ✅ Meta por peso, sexo e treino do dia
- ✅ Copos rápidos, avatar animado, sequência e gráficos
- ✅ Lembretes ao longo do dia
- 💡 Ajuste da meta em dias quentes
- 💡 Outras bebidas com fator de hidratação

## 3. Corpo e medidas
- ✅ Peso e medidas com gráfico
- ✅ IMC, TMB, gasto diário, cintura/altura, proteína sugerida
- 🟡 % de gordura com histórico próprio
- ✅ Fotos de evolução lado a lado
- 💡 Medidas por região no mapa corporal
- 💡 Bioimpedância manual
- ✅ Meus dados: todos os lançamentos pessoais concentrados no Perfil
- ✅ Evolução do corpo: gráfico por semana/mês, comparação com 1 semana, 1 mês, 1 ano e mês a mês ano contra ano

## 4. Nutrição
- ✅ Meta calórica pela TMB, atividade e objetivo
- ✅ Macronutrientes com meta diária
- ✅ Micronutrientes com metas por sexo e idade
- ✅ Base de alimentos TACO em português
- ✅ Diário por refeição, favoritos e copiar de ontem
- ✅ Planos de dieta por objetivo
- ✅ Leitor de código de barras (Open Food Facts)
- ✅ Ciclo de carboidrato ligado aos dias de treino
- 💡 Foto do prato com estimativa assistida
- ✅ Alimentos próprios, refeições pessoais salvas e calorias rápidas
- ✅ Tendências de calorias e macronutrientes por período
- ✅ Receitas: combinar alimentos num prato só, com peso pronto e porções
- ✅ Porção por calorias: digitar kcal e o app calcula os gramas
- ✅ Produtos de marca embutidos para os dois perfis (whey DUX e Black Skull)
- ✅ Gramas e calorias editáveis em cada alimento da refeição e da receita, ligados por proporção
- ✅ Banco de alimentos: listar, criar, editar e excluir (ocultar) alimentos
- ✅ Receitas compartilhadas entre os perfis do celular e envio por código para o outro celular

## 5. Metas e hábitos
- ✅ Meta de água e sequência de semanas treinadas
- ✅ Objetivo com déficit/superávit calculado por fontes científicas (4 objetivos)
- ✅ Meta de hoje no Início: falta em kcal e por macronutriente
- ✅ Gasto do dia pelo relógio (calorias ativas) ou pelo nível de atividade
- ✅ Central de metas: peso, gordura, carga-alvo, treinos por semana, proteína
- ✅ Tendência e previsão de chegada à meta
- ✅ Conquistas pessoais (sem rede social)
- 🟡 Hábitos diários: sono (pronto), passos e suplementos
- ✅ Painel do dia num único cartão
- ✅ Painel do dia: macros, consumidas x gastas com déficit/superávit e meta, água, treino e exercício
- ✅ Atividade diária: anéis de calorias gastas, em treino e em exercícios, metas estimadas e gasto basal

## 6. Gráficos e relatórios
- ✅ Períodos de 7 dias, mês, ano e desde o início em todos os gráficos
- ✅ Relatório mensal, calendário, radar e evolução por músculo
- ✅ Gráficos de nutrição e aderência à meta
- ✅ Painel Saúde da semana e do mês
- 💡 Relatório em PDF para nutricionista ou médico
- 💡 Correlações: proteína × carga, sono × desempenho

## 7. Identidade e plataforma
- ✅ Logo, ícones e abertura no estilo do Hevy
- ✅ 6 temas, 15 cores de destaque, foto de perfil
- ✅ Perfis separados, backup, cópias automáticas
- 💡 Sincronizar os dois celulares
- ✅ Senha de entrada nos dois celulares
- ✅ Pictogramas próprios para 53 exercícios avulsos (estilo Samsung Health)
- ✅ Filtros de músculo com corpo hiper-realista e ilustrações de equipamento
- ✅ Painel de atalhos no Início e todo preenchimento concentrado no Perfil
- ✅ Assinatura discreta "by Samuel Costa" e versão visível em Configurações
- ✅ Datas digitadas só com números (DD/MM/AAAA) e calendário opcional (exceto nascimento)
- 💡 Sincronização automática entre os celulares (exige servidor; aguardando decisão)
- ✅ Início com a Meta de hoje no topo e abas na ordem Início, Treino, Exercícios, Nutrição, Água, Perfil

## 8. Publicação
- ✅ Site no ar pelo GitHub Pages, publicado a cada envio
- ⬜ App instalado nos dois celulares pelo Pages
- ✅ Atualização automática do app instalado (sem reinstalar)
- ⬜ Reinstalar nos celulares para trocar o ícone da abertura (sem quadrado verde)
- ✅ Atualização forçada pela versão publicada (version.json) e botão "Verificar e atualizar o app"

## Ordem dos próximos passos

1. **Publicação:** Reinstalar o app nos dois celulares (ícone da abertura); se o quadrado verde continuar, trocar o ícone da tela inicial
2. **Treino:** Periodização em blocos e RPE/RIR por série
3. **Corpo e medidas:** Medidas por região no mapa corporal e bioimpedância manual
4. **Gráficos e relatórios:** Relatório em PDF para nutricionista ou médico
5. **Hidratação:** Outras bebidas com fator de hidratação e ajuste em dias quentes

## Referências de outros apps

| App | O que inspira | Status |
|---|---|---|
| Hevy | Treino, sessão ao vivo, estatísticas, mapa corporal, abertura | aplicado |
| Apple Watch (atividade) | Visual do avatar de água | aplicado |
| Samsung Health (Refeição) | Diário de refeições, porção, nutrientes, tendências de calorias e macros | aplicado |

## Histórico de entregas

| Data | Entrega |
|---|---|
| 17/10/2026 | App de treino completo, aba Água, temas e cores, perfis, saúde no Início |
| 17/10/2026 | Avatar de água com as silhuetas aprovadas |
| 17/10/2026 | Logo, ícones e abertura no estilo do Hevy |
| 17/10/2026 | Mapa corporal hiper-realista (17 grupos) e Início com os últimos 10 treinos |
| 17/10/2026 | Skill carga-app com toda a memória do projeto |
| 17/10/2026 | Painel visual do roadmap |
| 17/10/2026 | Projeto enviado ao GitHub (xSam10-10/Carga) |
| 17/10/2026 | Site publicado no GitHub Pages |
| 17/10/2026 | Senha de entrada e calorias do treino pela frequência cardíaca |
| 17/10/2026 | Calorias do treino passam a vir do relógio; frequência cardíaca removida |
| 17/10/2026 | Aba Nutrição: diário de refeições, TACO, macros, micronutrientes, metas e tendências |
| 17/10/2026 | Abertura do app instalado já começa só com o símbolo (sem o quadrado verde) |
| 17/10/2026 | Animação de recorde no treino: medalha, balão e confetes |
| 17/10/2026 | Som do recorde igual ao do Hevy e tempos da animação ajustados |
| 17/10/2026 | Objetivos e metas: déficit/superávit, macros e o que falta hoje no Início |
| 17/10/2026 | Meta do dia: exercício do relógio somado por inteiro; relógio como padrão; dias de treino por semana |
| 17/10/2026 | Meus dados no Perfil, reset geral com restauração e assinatura |
| 17/10/2026 | Aba Exercícios: exercícios avulsos com calorias, distância e frequência cardíaca |
| 18/10/2026 | Atualização automática do app instalado, figuras femininas da Carol, filtros hiper-realistas e ilustrados |
| 18/10/2026 | Evolução do corpo com histórico e comparações de todas as medidas |
| 18/10/2026 | Até 12 favoritos de exercício no Início |
| 18/10/2026 | Painel no Início e formulários só no Perfil |
| 18/10/2026 | Nutrição v2 (copiar de ontem, planos de dieta, código de barras), Central de metas, fotos de evolução, Painel do dia e lembretes de água |
| 18/10/2026 | Resumo de saúde (semana/mês), volume semanal por músculo, recuperação muscular, ciclo de carboidrato e conquistas |
| 18/10/2026 | Painel do dia reorganizado (macros, calorias consumidas/gastas e déficit/superávit, água, treino, exercício) |
| 18/10/2026 | Datas com máscara DD/MM/AAAA e calendário opcional |
| 18/10/2026 | Encerrar treino vazio e descartar treino em andamento |
| 18/10/2026 | Receitas na Nutrição, porção por calorias e whey DUX e Black Skull embutidos |
| 18/10/2026 | Atividade diária no Início (calorias gastas, treino, exercícios e gasto basal) |
| 18/10/2026 | Gramas e calorias editáveis nas refeições e receitas |
| 18/10/2026 | Banco de alimentos |
| 18/10/2026 | Atualização automática forçada (v59) |
| 18/10/2026 | Receitas compartilhadas e envio por código (v60) |
| 18/10/2026 | Meta de hoje no topo do Início (v61) |
| 18/10/2026 | Aba Exercícios ao lado de Treino (v62) |
