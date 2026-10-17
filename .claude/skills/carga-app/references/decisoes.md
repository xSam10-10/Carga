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
