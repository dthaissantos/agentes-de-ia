# Agentes de IA — estudos acadêmicos aplicados

Este repositório reúne estudos sobre desenvolvimento e avaliação de agentes de Inteligência Artificial, realizados no contexto do MBA em Dados & Análises para Negócios, a partir da disciplina **Dados & Analytics nas Organizações**.

O primeiro projeto é o **DiagOp Analytics**: um agente inicial, simples e funcional no ambiente em que foi configurado e testado. Seu papel é apoiar uma analista na investigação de atendimentos, utilizando dados fictícios e mantendo as decisões sob responsabilidade humana.

O objetivo é mostrar como os conteúdos das seis aulas foram conectados para construir esse primeiro agente: da definição do problema à análise dos dados, da configuração às revisões das respostas. A organização abaixo é uma síntese aplicada ao projeto, não uma transcrição das aulas nem uma declaração de avaliação formal pelo professor.

## Ponto de partida: Prática 12

Na prática de 17 de outubro de 2026, uma proprietária de um pequeno comércio eletrônico deseja automatizar todo o atendimento, estimado em 80 mensagens por dia. A tarefa é investigar a demanda antes de decidir se um agente é necessário. O caso é hipotético e não foi baseado em anúncio real verificado.

A atividade propõe diagnóstico, escolha da solução, desenho de autonomia e MVP com comunicação executiva. O [enunciado original](cases/diagop-analytics/docs/00-pratica-12.md) está preservado no projeto.

O agente desenvolvido foi o DiagOp, voltado a apoiar a analista nesse diagnóstico. O teste com CSV é uma etapa posterior; não corresponde à implantação de um atendente automático para a empresa do exercício.

## Das aulas ao primeiro agente

| Aula | Síntese do conteúdo | Aplicação no DiagOp |
|---|---|---|
| **1 — Por que usar dados?** | Decisões orientadas por evidências, contexto BANI e uso crítico de IA. Informação precisa ser interpretada antes de orientar uma decisão. | Definimos a finalidade do agente: apoiar uma investigação, sem presumir que existe sobrecarga ou aceitar a primeira resposta como conclusão. |
| **2 — O que medir?** | Indicadores, KPI, KRI, KCI, leading e lagging, OKRs e Lei de Goodhart. Uma medida precisa de objetivo, regra e contexto. | Escolhemos medidas de duração, consulta, espera e recontato. Explicitamos regras e limitações, sem transformar volume ou tempo elevado em prova de ineficiência. Não foi estabelecido um OKR operacional nem metas sem referência. |
| **3 — Como interpretar?** | Problema versus sintoma, hipóteses, qualidade dos dados, Data Centric e Analytics by Design: planejar a análise a partir da decisão que se deseja apoiar. | Estruturamos três hipóteses, verificamos a base antes dos cálculos e separamos o que foi observado das possíveis explicações. |
| **4 — Ética, proteção de dados e responsabilidade** | Uso responsável da IA, privacidade, governança e limites de autonomia. | Utilizamos dados simulados e IDs pseudonimizados. O agente não atende clientes, não altera processos e não toma decisões pela analista. |
| **5 — Pessoas, colaboração e liderança** | Stakeholders, trabalho entre áreas, liderança por influência e comunicação. | Definimos a analista como usuária e responsável pela validação. Tratamos a espera por outras áreas como tema de investigação, sem culpabilizar equipes. Adaptamos a linguagem para facilitar o entendimento. |
| **6 — Consolidação e comunicação dos resultados** | Integração dos conceitos, síntese executiva, pitch e reflexão sobre a aprendizagem. | Consolidamos o case, documentamos resultados e limitações e revisamos a abertura para que ela não afirme mais do que os dados sustentam. |

## Como os conteúdos se conectam

Primeiro definimos o problema e a decisão. Depois verificamos quais dados e indicadores poderiam ajudar. Só então organizamos o papel da IA, suas instruções e os prompts de teste. As respostas foram revisadas quanto à precisão, clareza e responsabilidade.

A contribuição das aulas aparece nesse processo completo. O agente é o resultado de uma investigação estruturada, com revisão humana ao longo do desenvolvimento.

## Primeiro projeto

| Projeto | Objetivo | Estágio |
|---|---|---|
| [DiagOp Analytics](cases/diagop-analytics/README.md) | Apoiar a investigação de dificuldades com sistemas, comunicação e espera por outras áreas | Agente por instruções, testado em conversa com uma base fictícia |

## O que está documentado

O case reúne as fases iniciais da análise, a base, as regras de cálculo, as instruções do agente, os prompts, os retornos e os ajustes. Transcrições e resumos são identificados. O script de conferência foi acrescentado posteriormente para reproduzir os principais cálculos.

## Escopo acadêmico

Este é um projeto educacional e de portfólio. Não houve treinamento de modelo próprio, implantação em empresa ou comprovação de benefício operacional. A base não representa uma empresa real. O funcionamento observado depende do ambiente e das ferramentas disponíveis; publicar os arquivos não cria um serviço autônomo.

Autoria do projeto: Thais Santos. Desenvolvimento, documentação e conferência dos cálculos com apoio de IA e revisão humana ao longo da conversa.
