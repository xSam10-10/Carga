# Decisões do projeto (e o motivo de cada uma)

Registre aqui toda decisão nova, com data, para não voltar a discutir o que já foi decidido.

| Data | Decisão | Motivo / contexto |
|---|---|---|
| out/2026 | PWA de página única, sem servidor nem login | Uso pessoal no celular; dados no aparelho; funciona offline |
| out/2026 | Sem rede social e sem compartilhar em apps sociais | O app é só para treino, desempenho e sugestões |
| out/2026 | Dois perfis separados (Samuel e Carol) | Cada um no seu celular, com histórico próprio |
| out/2026 | Hevy como referência principal de comportamento | O usuário vinha do Hevy; importação de CSV do Hevy incluída |
| out/2026 | 15 cores de destaque e 6 temas; sem "Preto" nem "Automático" | Pedido do usuário; cada tema sugere uma cor, mas a cor fica livre |
| out/2026 | Tema Escuro abre com destaque verde | Pedido do usuário |
| out/2026 | ~~Sem batimento cardíaco nem calorias~~ (revisto em 17/10) | Substituído pela decisão de calorias pela FC média, abaixo |
| out/2026 | Indicadores de saúde com fonte citada (OMS, Mifflin-St Jeor, EFSA, NICE, ISSN, ACE) | Confiabilidade; sempre com aviso de que não substituem um profissional |
| out/2026 | Gráficos com 7 dias, mês, ano e desde o início; padrão Mês; por dia ou por semana | Pedido do usuário |
| out/2026 | Avatar de água com as silhuetas de contorno aprovadas | Fidelidade total à arte enviada; cor segue o destaque |
| out/2026 | Logo: C de anilha com halter rompendo a abertura + "carga" em itálico preto | Aprovada pelo usuário ("ficou muito bom") |
| out/2026 | Abertura igual à do Hevy: preto, só o símbolo parado, esmaecimento curto | A versão animada em etapas foi recusada por falta de fluidez |
| out/2026 | Mapa corporal hiper-realista com as 17 artes do usuário; cor por `mix-blend-mode: color` | Preserva o sombreamento; acompanha a cor de destaque |
| out/2026 | Sem treino no período, o corpo fica cinza | O usuário pediu para manter assim |
| out/2026 | Início mostra só os últimos 10 treinos, com mapa corporal em cada cartão | Pedido do usuário; o histórico completo fica no Perfil |
| out/2026 | Ícones pequenos de músculo continuam com o desenho simples | O realista fica ilegível em ~30 px |
| out/2026 | Marca (logo, ícone, abertura) sempre no verde, independente do tema | Reconhecimento da marca |
| out/2026 | Skill `carga-app` guardada no repositório (`.claude/skills/`) | Para migrar de chat ou ambiente perdendo o mínimo |
| out/2026 | Todas as sugestões 💡 do roadmap foram aprovadas para implementar aos poucos | O usuário gostou das sugestões; a ordem fica em "Próximos passos" |
| out/2026 | Painel visual do roadmap (artifact Dashboard) alimentado por `roadmap.json` | Acompanhar a evolução do projeto em barras de progresso |
| 17/10/2026 | Senha de entrada fixa (8 dígitos), igual nos dois celulares, pedida a cada abertura do app | Pedido do usuário. O código guarda só o hash PBKDF2-SHA256 (sal `carga-v1-lock`, 150 mil iterações), porque o repositório é público. **Nunca escreva a senha em texto puro no código, na skill ou em commits**; quem precisar dela pergunta ao usuário |
| 17/10/2026 | ~~Calorias estimadas pela FC média (Keytel)~~ (removido no mesmo dia) | Substituído pelo registro direto das calorias do relógio |
| 17/10/2026 | Calorias do treino digitadas a partir do relógio, num pop-up no fim do treino; frequência cardíaca removida do app | O relógio (Samsung/Apple) já calcula as calorias e é mais fiel que uma fórmula |
| 17/10/2026 | Nutrição no modelo do Samsung Health (vídeo do usuário), com a identidade do Carga | Referência escolhida pelo usuário; 5ª aba "Nutrição" |
| 17/10/2026 | Base de alimentos: TACO 4ª ed. (NEPA/UNICAMP), valores por 100 g; dados do projeto taco-api (MIT) | Gratuita, brasileira, funciona offline; o Samsung usa FatSecret, que não tem dados abertos |
| 17/10/2026 | Tendências da nutrição usam o seletor de período do app em vez de Dias/Semanas/Meses | Mantém o padrão dos outros gráficos (pedido anterior do usuário) |
| 17/10/2026 | Ícone "any" do manifesto só com o símbolo, no tamanho da nossa abertura | O Android mostrava primeiro o quadrado verde e depois o símbolo; o usuário quer que já comece no símbolo sobre fundo preto |
| 17/10/2026 | Objetivos: Perder peso (−20%), Manter (0), Ganhar peso (+400 kcal), Ganhar massa muscular (+10%) | Helms et al. 2014 (JISSN, perda de 0,5–1% do peso/semana); ISSN 2017 (dietas e composição corporal); NHS (ganho de peso: +300–500 kcal); Iraki et al. 2019 (Sports, superávit de 10–20%, 0,25–0,5%/semana). Piso de segurança: TMB e 1.200/1.500 kcal |
| 17/10/2026 | TMB por Mifflin-St Jeor | Frankenfield et al. 2005 (J Am Diet Assoc): a mais precisa das equações comuns, erro dentro de 10% na maioria |
| 17/10/2026 | Gasto do dia em dois modos: relógio (TMB × 1,2 + calorias ativas registradas) ou nível de atividade (TMB × fator); automático escolhe o relógio quando há calorias registradas | O usuário vai registrar as calorias do relógio; o modo evita contar o exercício duas vezes. Pedir calorias ATIVAS (as totais já incluem a basal) |
| 17/10/2026 | Níveis de atividade: Sedentário, Levemente ativo, Normal, Ativo, Muito ativo (1,2 / 1,375 / 1,55 / 1,725 / 1,9) por dias de exercício na semana | Fatores de McArdle/Katch usados com Mifflin; "Normal" ≈ recomendação da OMS 2020 (150–300 min/semana) |
| 17/10/2026 | Macros: proteína em g/kg por objetivo, gordura 25% (mín. 0,6 g/kg), carboidrato no restante | ISSN 2017 (proteína 1,4–2,0 g/kg; mais em déficit); Iraki 2019 (1,6–2,2 g/kg; gordura 0,5–1,5 g/kg); IOM AMDR (gordura 20–35%, carboidrato 45–65%, proteína 10–35%) |
| 17/10/2026 | Início abre com o cartão "Meta de hoje": falta em kcal e barras de quanto falta de cada macro | Pedido do usuário: acompanhar a meta do dia alimentada pela aba Nutrição |
| 17/10/2026 | Exercício do relógio entra cheio na meta: meta = (rotina ± ajuste do objetivo) + exercício; Falta = meta base + exercício − consumido | Pedido do usuário: o valor do relógio tem que aparecer igual na conta; o déficit/superávit fica fixo no dia |
| 17/10/2026 | Modo "Pelo relógio" é o padrão do gasto do dia | Pedido do usuário (opção A): a conta é meta + exercício do relógio − consumido |
| 17/10/2026 | Dias de treino por semana escolhidos no perfil (0 a 7+) definem o fator de atividade, em vez de nível fixo | Pedido do usuário: não deixar fixo; mudar quando a rotina mudar |
| 17/10/2026 | Reset geral de todos os perfis (uma vez por aparelho), com os dados antigos guardados em `carga.old.*` e botão para restaurar | Pedido do usuário para testar preenchendo tudo do zero |
| 17/10/2026 | Aba Exercícios só com registro manual e offline; calorias obrigatórias | Pedido do usuário: nada que dependa de relógio, GPS ou mapa |
| 18/10/2026 | Atualização automática do app instalado (service worker com `no-cache`, `update()` ao voltar para a tela, recarga no `controllerchange`) | O app instalado ficava preso na versão antiga |
| 18/10/2026 | Pictogramas próprios dos exercícios, filtros com corpo hiper-realista e ilustrações de equipamento | Prints do Samsung Health e do Hevy como referência; desenhos próprios |
| 18/10/2026 | Painel de atalhos no Início; formulários só na aba Perfil | Pedido do usuário |
| 18/10/2026 | Evolução do corpo com histórico e comparações (inclui altura com histórico `S.hLog`) | Pedido do usuário: comparar semana a semana, mês a mês, ano contra ano |

