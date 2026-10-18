# Case original e desenvolvimento do projeto

## Origem: Prática 12

O projeto começou na **Prática 12, de 17 de outubro de 2026 — Diagnóstico de uma demanda e desenho de agente de IA**, um exercício acadêmico de 20–25 minutos. O [enunciado da atividade](00-pratica-12.md) é a fonte do contexto inicial.

Uma pequena empresa de comércio eletrônico recebe aproximadamente **80 mensagens diárias por diferentes canais**. A proprietária quer uma IA para responder perguntas, consultar pedidos e reduzir o trabalho manual. Sua proposta é automatizar todo o atendimento.

Ainda faltam informações sobre processos, qualidade dos dados e motivos de contato. A missão da analista é diagnosticar a demanda e recomendar uma solução viável antes de construir um agente.

O caso é **hipotético**. Não foi utilizado anúncio real verificado. As 80 mensagens são uma premissa didática, não uma contagem obtida do CSV.

## Questão inicial

A automatização completa é necessária e adequada? Antes dessa decisão, é preciso entender o trabalho da equipe e comparar agente de IA, automação convencional e melhoria do processo. O pedido de tecnologia da proprietária não comprova a causa do problema nem a adequação da solução.

## As quatro etapas propostas

1. Diagnosticar problema, sintomas, hipóteses e dados necessários.
2. Identificar stakeholders e condições para escolher a solução.
3. Se justificável, desenhar o agente e definir autonomia para perguntas frequentes, consulta de pedidos, reclamações, reembolsos e atualização cadastral.
4. Propor um MVP, indicadores, riscos e pitch executivo.

O enunciado propõe essas etapas. As respostas completas da autora às quatro etapas não foram recuperadas nesta conversa e não são reconstruídas como decisões históricas.

## Agente desenvolvido: DiagOp Analytics

O agente documentado no projeto apoia a **analista no diagnóstico**. Ele recebe registros, verifica qualidade, calcula indicadores e aponta o que merece investigação. Não responde ao cliente final nem executa a automatização completa pedida pela proprietária.

No desenvolvimento documentado foram utilizadas três hipóteses: sistemas, comunicação e espera por outras áreas. O enunciado inicial solicitava duas hipóteses; as três pertencem ao escopo posterior do DiagOp.

Esse protótipo permite exercitar o apoio da IA à análise. Seu teste não demonstra que a escolha da solução final para a empresa tenha sido concluída.

## Teste posterior com dados simulados

O arquivo atendimentos_simulados.csv contém 240 registros e 18 campos. Foi utilizado para testar a qualidade da análise e o comportamento do assistente. Não é uma coleta real da empresa hipotética nem comprovação da premissa de 80 mensagens diárias.

A analista mantém a responsabilidade de validar campos, cálculos, interpretações e qualquer recomendação. Não há implantação em produção ou integração automática neste estudo.
