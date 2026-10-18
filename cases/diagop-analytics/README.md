# DiagOp Analytics — projeto de estudo acadêmico

Desenvolvido no contexto do MBA em Dados & Análises para Negócios, este estudo aplica os conteúdos da disciplina Dados & Analytics nas Organizações à construção de um primeiro agente de IA simples, testado em conversa.

## O case original: Prática 12

Uma pequena empresa de comércio eletrônico recebe aproximadamente **80 mensagens diárias por diferentes canais**. A proprietária deseja automatizar todo o atendimento com IA: responder perguntas, consultar pedidos e reduzir o trabalho manual.

Porém, ainda faltam informações sobre os processos, a qualidade dos dados e os motivos de contato. A missão acadêmica é **realizar o diagnóstico e recomendar uma solução viável antes de construir o agente**, comparando IA, automação convencional e melhoria do processo.

Esse é o caso hipotético da **Prática 12, de 17 de outubro de 2026 — Diagnóstico de uma demanda e desenho de agente de IA**. Não foi utilizado anúncio real verificado. As 80 mensagens são uma premissa do exercício.

Leia o [enunciado da prática](docs/00-pratica-12.md) e a [relação entre o case e o agente desenvolvido](docs/01-case.md).

## O que desenvolvemos a partir do estudo

O **DiagOp Analytics** é um agente de apoio à analista responsável pelo diagnóstico. Ele verifica registros, calcula indicadores possíveis e aponta o que precisa de investigação. Não executa o atendimento automático solicitado pela proprietária.

O CSV com 240 registros fictícios é um material posterior de teste do agente. Não substitui o case original e não representa dados reais da empresa do enunciado. O teste não encerra a decisão sobre automatizar o atendimento.

## Fases iniciais: a análise antes dos prompts

### 1. Entender o contexto e separar problema de sintoma

O ponto de partida foi questionar o pedido da proprietária para automatizar todo o atendimento e investigar a situação antes de escolher uma tecnologia. Tempo alto, consultas demoradas e contatos repetidos são sinais a examinar; isoladamente, não explicam a causa nem confirmam sobrecarga.

### 2. Definir a decisão e quem é responsável

A decisão apoiada é escolher o que merece investigação e quais dados adicionais devem ser coletados. A analista é a usuária principal e valida as interpretações. O agente organiza informações, calcula indicadores quando há suporte e aponta limites.

### 3. Formular hipóteses sem antecipar a conclusão

- **Sistemas:** consultar várias plataformas pode aumentar o esforço.
- **Comunicação:** lacunas de informação podem contribuir para novos contatos.
- **Outras áreas:** depender de uma resposta pode prolongar a espera.

Essas explicações precisam ser confrontadas com os registros. Outras causas continuam possíveis.

### 4. Conhecer e conferir os dados

Foram inspecionados 240 registros e 18 campos, com inícios entre 12 e 14/10/2026. Cada registro foi tratado como um atendimento, identificado por seu ID.

A conferência identificou campos ausentes, uma duração negativa, divergência na quantidade de sistemas, uma categoria de motivo a validar e respostas posteriores ao encerramento que dependem da regra do processo. O original foi preservado, sem correções silenciosas.

### 5. Definir indicadores e suas limitações

Antes de interpretar resultados, foram explicitados os cálculos possíveis. O tempo entre início e fim não foi chamado de trabalho ativo. A classificação de recontato não foi tratada como uma taxa validada de reincidência. A espera foi comparada com e sem os dois registros que exigem conferência.

Sem capacidade, fila e metas, não é possível confirmar sobrecarga. Sem uma janela e um vínculo claro do problema, não é possível validar reincidência.

### 6. Definir a atuação da IA

O assistente deve explicar o que encontrou, mostrar os registros que sustentam o achado e informar o que precisa de confirmação. Deve usar linguagem simples, preservar a responsabilidade humana e não alterar processos ou decidir em nome da analista.

Essas definições orientam a configuração e os prompts apresentados a seguir. Esta sequência organiza o raciocínio do case; não representa um diário literal da ordem de todas as mensagens.

## Configuração, prompts e testes

Com o objetivo e os limites definidos, as instruções foram organizadas para conduzir a conferência da base, os cálculos e a investigação das hipóteses. O teste utilizou a base fictícia e um pedido de análise completa.

O primeiro retorno foi revisado em quatro pontos: coerência entre abertura e evidências, critérios para priorizar a investigação da espera, tratamento das datas e clareza da linguagem. As versões disponíveis e os ajustes estão documentados nos materiais abaixo.

O agente foi funcional para esse teste no ambiente de conversa. Não houve treinamento de modelo próprio nem implantação de uma aplicação independente.

## Principal aprendizado

Um assistente útil precisa mostrar o que encontrou, o que ainda é uma possível explicação e o que a analista deve conferir. O estudo não se resume ao primeiro retorno da IA: os ajustes feitos após a revisão fazem parte do resultado.

## Materiais

- [Enunciado original — Prática 12](docs/00-pratica-12.md)
- [Contexto e decisões](docs/01-case.md)
- [Como a análise foi realizada](docs/02-metodologia.md)
- [Dicionário dos dados](dados/dicionario.md)
- [Base original simulada](dados/atendimentos_simulados.csv)
- [Instruções documentadas do assistente](agente/instrucoes.md)
- [Prompts usados](prompts/01-prompts-utilizados.md)
- [Retorno inicial: registro estruturado](retornos/01-retorno-inicial.md)
- [Retorno revisado: transcrição](retornos/02-retorno-revisado.md)
- [Relatório consolidado](resultados/relatorio.md)
- [Ajustes e validação humana](docs/03-validacao-e-evolucao.md)
- [Limites e próximos passos](docs/04-limitacoes.md)
- [Procedência e cobertura do histórico](docs/05-proveniencia.md)

## Reproduzir os cálculos

Requer Python 3.10 ou superior, apenas biblioteca padrão. Na raiz do repositório:

```bash
python cases/diagop-analytics/scripts/analisar.py
```

O comando confere a base sem alterá-la e imprime os principais resultados em JSON. O script foi acrescentado para este portfólio; não é apresentado como o programa original usado em toda a conversa.
