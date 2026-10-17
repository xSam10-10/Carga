# Roadmap do Carga: acompanhamento do desenvolvimento

> Gerado por `scripts/roadmap.py` a partir de `references/roadmap.json`. Edite o JSON, não este arquivo.
> Painel visual: https://claude.ai/artifact/T86Moh6PbAnUH4K5Hr6Bk6

**Objetivo:** O app de saúde mais completo do mercado: treino, dieta (macros e micros), água, medidas, metas e gráficos num lugar só, para o Samuel e a Carol.

Legenda: ✅ pronto · 🟡 parcial · ⬜ a fazer · 💡 sugestão aprovada para implementar aos poucos.

## Visão geral (progresso geral: 70%)

| Módulo | Status | Progresso | Resumo |
|---|---|---|---|
| 1. Treino | ✅ | 92% | Rotinas, sessão ao vivo, recordes, catálogo de 465 exercícios e mapa corporal hiper-realista. |
| 2. Hidratação | ✅ | 85% | Meta por peso e sexo, copos rápidos, avatar animado, sequência e gráficos. |
| 3. Corpo e medidas | 🟡 | 55% | Peso, medidas, IMC, TMB e indicadores; faltam fotos de evolução e medidas por região. |
| 4. Nutrição | 🟡 | 60% | Aba Nutrição no modelo do Samsung Health: diário com 6 refeições, TACO (591 alimentos), macros e micronutrientes, metas e tendências. Faltam planos de dieta e código de barras. |
| 5. Metas e hábitos | 🟡 | 15% | Já há meta de água e sequências; falta a central de metas com previsão. |
| 6. Gráficos e relatórios | 🟡 | 72% | Períodos de 7 dias a desde o início em todos os gráficos; faltam os de nutrição e o painel da semana. |
| 7. Identidade e plataforma | ✅ | 92% | Logo, abertura, senha de entrada, 6 temas, 15 cores, perfis separados, backup. |
| 8. Publicação | ✅ | 85% | Site no ar em xsam10-10.github.io/Carga, atualizado a cada envio; falta instalar nos dois celulares. |

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
- 💡 Volume semanal por grupo com faixa recomendada e alerta de grupo esquecido
- 💡 Mapa de recuperação muscular
- 💡 RPE e RIR por série
- 💡 Animações próprias para exercícios sem foto

## 2. Hidratação
- ✅ Meta por peso, sexo e treino do dia
- ✅ Copos rápidos, avatar animado, sequência e gráficos
- 💡 Lembretes ao longo do dia
- 💡 Ajuste da meta em dias quentes
- 💡 Outras bebidas com fator de hidratação

## 3. Corpo e medidas
- ✅ Peso e medidas com gráfico
- ✅ IMC, TMB, gasto diário, cintura/altura, proteína sugerida
- 🟡 % de gordura com histórico próprio
- 💡 Fotos de evolução lado a lado
- 💡 Medidas por região no mapa corporal
- 💡 Bioimpedância manual

## 4. Nutrição
- ✅ Meta calórica pela TMB, atividade e objetivo
- ✅ Macronutrientes com meta diária
- ✅ Micronutrientes com metas por sexo e idade
- ✅ Base de alimentos TACO em português
- 🟡 Diário por refeição e favoritos (falta "copiar de ontem")
- ⬜ Planos de dieta por objetivo
- 💡 Leitor de código de barras (Open Food Facts)
- 💡 Ciclo de carboidrato ligado aos dias de treino
- 💡 Foto do prato com estimativa assistida
- ✅ Alimentos próprios, refeições pessoais salvas e calorias rápidas
- ✅ Tendências de calorias e macronutrientes por período

## 5. Metas e hábitos
- ✅ Meta de água e sequência de semanas treinadas
- ⬜ Central de metas: peso, gordura, carga-alvo, treinos por semana, proteína
- ⬜ Tendência e previsão de chegada à meta
- 💡 Conquistas pessoais (sem rede social)
- 💡 Hábitos diários: sono, passos, suplementos
- 💡 Painel do dia num único cartão

## 6. Gráficos e relatórios
- ✅ Períodos de 7 dias, mês, ano e desde o início em todos os gráficos
- ✅ Relatório mensal, calendário, radar e evolução por músculo
- ✅ Gráficos de nutrição e aderência à meta
- ⬜ Painel Saúde da semana e do mês
- 💡 Relatório em PDF para nutricionista ou médico
- 💡 Correlações: proteína × carga, sono × desempenho

## 7. Identidade e plataforma
- ✅ Logo, ícones e abertura no estilo do Hevy
- ✅ 6 temas, 15 cores de destaque, foto de perfil
- ✅ Perfis separados, backup, cópias automáticas
- 💡 Sincronizar os dois celulares
- ✅ Senha de entrada nos dois celulares

## 8. Publicação
- ✅ Site no ar pelo GitHub Pages, publicado a cada envio
- ⬜ App instalado nos dois celulares pelo Pages

## Ordem dos próximos passos

1. **Publicação:** Instalar o app nos celulares do Samuel e da Carol
2. **Nutrição:** Nutrição v2: copiar de ontem, planos de dieta e leitor de código de barras
3. **Metas e hábitos:** Central de metas com previsão de chegada
4. **Corpo e medidas:** Fotos de evolução e medidas por região
5. **Metas e hábitos:** Painel do dia: treino, água, calorias, proteína e sono num cartão
6. **Hidratação:** Lembretes de água, hábitos e conquistas

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
