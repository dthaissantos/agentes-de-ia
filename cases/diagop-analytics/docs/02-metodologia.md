# Como a análise foi realizada

## 1. Preservar a fonte

O CSV original foi mantido, sem preencher lacunas ou corrigir categorias silenciosamente. O separador é ponto e vírgula. Cada registro é rastreado por id_atendimento.

## 2. Conferir a qualidade

Foram verificadas ausências, duplicidades completas e de ID, categorias, datas e ordem dos eventos. A lista de sistemas foi separada por ponto e vírgula e comparada à quantidade informada. As notas de qualidade foram confrontadas com os demais campos, sem aceitar seu conteúdo como verdade automática.

## 3. Definir o que pode ser medido

| Medida | Regra | Limite |
|---|---|---|
| Volume | Contar IDs únicos | Não mede capacidade disponível |
| Pendentes | Status Pendente / 240 | Retrato do arquivo; não é taxa de resolução por prazo |
| Tempo decorrido | Fim menos início; média dos 217 com tempo não negativo | Não é tempo de trabalho ativo |
| Consulta | Soma de tempo_consulta_min / 239 preenchidos | Interpretação provisória como minutos por atendimento |
| Espera | Resposta menos encaminhamento, minutos corridos | Não mede trabalho da área e não desconta expediente |
| Recontato informado | 53 registros classificados / 240 | Não é reincidência validada por janela e problema |

Para a espera, foram apresentados todos os 86 tempos calculáveis e uma comparação separada sem ATD-0115 e ATD-0202. Resposta após encerramento depende da regra do processo. Já o tempo negativo entre início e fim de ATD-0202 continua excluído da duração.

## 4. Comparar sem confundir diferença com causa

Foram observados canal, motivo, quantidade de sistemas e área acionada. A quantidade de sistemas foi comparada ao tempo de consulta sem ATD-0171, cuja quantidade diverge da lista. Não foram somados consulta, espera e duração, pois os tempos podem se sobrepor.

Para conferir repetições, foram ordenados os registros por início e agrupados por cliente, pedido e motivo, usando apenas pedidos preenchidos. Isso verifica coerência interna, mas não resolve a falta de janela e identificação do problema.

## 5. Revisar a própria resposta

A revisão avaliou se a abertura era mais forte que as evidências, se a prioridade tinha critérios explícitos e se exclusões dependiam de regras ainda não confirmadas. A linguagem também foi simplificada para que uma analista iniciante pudesse compreender os achados.
