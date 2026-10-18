# Relatório exploratório consolidado

## O que chamou atenção

Os registros com mais sistemas também tiveram consultas mais demoradas. Isso não prova falta de integração. Existem contatos repetidos, mas não há informação suficiente para atribuí-los a falhas de comunicação. Logística concentra a maior parcela da espera registrada e merece investigação desse tempo.

## Qualidade

| Achado | Registro ou seleção | Tratamento |
|---|---|---|
| 22 encerramentos ausentes | Status Pendente | Fora da duração, mantidos no volume |
| Consulta ausente | ATD-0014 | Fora da média de consulta |
| Pedido ausente | ATD-0127 | Repetição por pedido não verificável |
| Quantidade 4, lista com 2 sistemas | ATD-0171 | Fora da comparação por quantidade |
| Duração de -12 minutos | ATD-0202 | Fora da duração |
| Resposta depois do encerramento | ATD-0115 e ATD-0202 | Validar processo; comparar espera com e sem eles |
| Categoria Entrega / rastreio | ATD-0225 | Preservada sem mapeamento automático |
| Nota de resposta ausente sem área acionada | ATD-0083 | Validar nota e campos |

Não foram encontrados IDs repetidos, duplicatas completas ou datas preenchidas inválidas. Os 154 pares de datas de encaminhamento e resposta ausentes coincidem com área Nenhum. As 234 observações vazias não são automaticamente defeitos de qualidade.

## Indicadores

| Medida | Resultado | Registros ou cálculo |
|---|---:|---|
| Volume | 240 | IDs únicos |
| Pendentes | 9,2% | 22 / 240 |
| Tempo decorrido médio | 67,1 min | 14.552 / 217 |
| Mediana do tempo decorrido | 30 min | Valor central dos 217 tempos ordenados |
| Consulta média | 10,81 min | 2.583,6 / 239 |
| Área acionada | 35,8% | 86 / 240 |
| Recontatos informados | 22,1% | 53 / 240 |
| Espera com todos os tempos calculáveis | 115,0 min | 9.894 / 86 |
| Espera sem os dois registros a conferir | 115,9 min | 9.738 / 84 |

Tempo decorrido não é TMA ativo. Consulta é interpretada provisoriamente como minutos por atendimento. Recontato informado não é taxa validada de reincidência. Espera usa minutos corridos.

## Possível gargalo 1: espera por Logística

| Área | Quantidade | Espera média | Soma |
|---|---:|---:|---:|
| Logística | 40 | 156,2 min | 6.248 min |
| Financeiro | 7 | 99,0 min | 693 min |
| Estoque | 16 | 85,4 min | 1.366 min |
| Suporte técnico | 23 | 69,0 min | 1.587 min |

Logística é prioridade para investigar espera por reunir maior quantidade, maior média e 63,1% da soma dos tempos. Não é um ranking geral das hipóteses. ATD-0122 e ATD-0198 registram esperas de 324 e 318 minutos, respectivamente. Pode haver dependência de transportadora ou características dos motivos. A soma não mede horas de trabalho da equipe.

Sem ATD-0202, Logística tem 39 tempos e média de 158,8 minutos. Sem ATD-0115, Suporte técnico tem 22 tempos e média de 67,5 minutos. A regra de encerramento permanece pendente de validação.

## Possível gargalo 2: consulta a vários sistemas

Excluindo ATD-0171 e tempos ausentes, as consultas médias são 5,59 minutos para 1 sistema (35 casos), 9,20 para 2 (69), 12,28 para 3 (106) e 15,63 para 4 (28). A duração total não cresce de forma consistente com essa quantidade. Confirmar complexidade, composição dos casos e funcionamento das integrações antes de atribuir causa.

## Possível gargalo 3: contatos repetidos

Nos 239 registros com pedido, agrupar cliente, pedido e motivo após ordenar pelo início identifica 52 contatos posteriores ao primeiro em 32 grupos com repetição. Todos esses 52 estão marcados como recontato; o outro recontato não tem pedido preenchido.

ATD-0001, ATD-0005 e ATD-0012 compartilham cliente, pedido e motivo. ATD-0012 começa às 9h41 quando ATD-0005 ainda está aberto. Isso pode representar busca de atualização, escalonamento ou registros simultâneos.

Os registros com informação parcial têm 9/55 recontatos (16,4%), contra 30/119 com orientação padrão (25,2%). A informação é a do contato atual; não prova o efeito da comunicação anterior. Falta janela de repetição e vínculo inequívoco do problema.

## O que a analista deve conferir

Confirmar significado dos tempos, ordem permitida dos eventos, quantidade de sistemas e categoria de motivo. Definir janela e chave da reincidência. Coletar data de extração, capacidade, escalas, filas e metas antes de avaliar sobrecarga. Nenhuma mudança operacional foi implementada a partir deste estudo.
