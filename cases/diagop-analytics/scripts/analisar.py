"""Reprodução posterior dos principais cálculos do case. Apenas biblioteca padrão."""
from pathlib import Path
from datetime import datetime
from collections import Counter, defaultdict
import csv
import json
import statistics

path = Path(__file__).resolve().parents[1] / 'dados/atendimentos_simulados.csv'
with path.open(encoding='utf-8-sig', newline='') as f:
    rows = list(csv.DictReader(f, delimiter=';'))

def date(value):
    return datetime.strptime(value, '%Y-%m-%d %H:%M') if value else None

def minutes(a, b):
    return (date(b)-date(a)).total_seconds()/60 if a and b else None

def summary(values):
    return {'n': len(values), 'soma_min': round(sum(values), 6),
            'media_min': round(statistics.mean(values), 6) if values else None,
            'mediana_min': statistics.median(values) if values else None}

durations=[]
waits=[]
without=[]
consult=[]
areas=defaultdict(list)
systems=defaultdict(list)
issues=defaultdict(list)
keys=set()
repeat_count=0
for r in sorted(rows, key=lambda r: r['inicio_atendimento']):
    ident=r['id_atendimento']
    dur=minutes(r['inicio_atendimento'],r['fim_atendimento'])
    wait=minutes(r['encaminhamento_em'],r['resposta_departamento_em'])
    if dur is not None:
        if dur>=0: durations.append(dur)
        else: issues['duracao_negativa'].append(ident)
    if r['fim_atendimento'] and r['resposta_departamento_em'] and date(r['resposta_departamento_em'])>date(r['fim_atendimento']):
        issues['resposta_apos_fim'].append(ident)
    if wait is not None and wait>=0:
        waits.append(wait)
        areas[r['departamento_acionado']].append(wait)
        if ident not in {'ATD-0115','ATD-0202'}: without.append(wait)
    listed=len([s for s in r['sistemas_consultados'].split(';') if s.strip()])
    if listed!=int(r['quantidade_sistemas']): issues['quantidade_sistemas_divergente'].append(ident)
    if r['tempo_consulta_min']:
        value=float(r['tempo_consulta_min'])
        consult.append(value)
        if ident!='ATD-0171': systems[r['quantidade_sistemas']].append(value)
    if r['id_pedido']:
        key=(r['id_cliente_pseudo'],r['id_pedido'],r['motivo_contato'])
        repeat_count+=key in keys
        keys.add(key)

result={
    'registros':len(rows),
    'campos':len(rows[0]),
    'ausentes':{k:sum(not r[k] for r in rows) for k in rows[0]},
    'ids_duplicados':len(rows)-len({r['id_atendimento'] for r in rows}),
    'linhas_duplicadas':len(rows)-len({tuple(r.values()) for r in rows}),
    'status':dict(Counter(r['status'] for r in rows)),
    'duracao':summary(durations),
    'consulta':summary(consult),
    'espera_todos':summary(waits),
    'espera_sem_dois_ids':summary(without),
    'espera_por_area':{k:summary(v) for k,v in areas.items()},
    'consulta_por_quantidade_sem_ATD_0171':{k:summary(v) for k,v in sorted(systems.items())},
    'recontatos_informados':sum(r['tipo_contato']=='Recontato - mesmo motivo/pedido' for r in rows),
    'posteriores_por_cliente_pedido_motivo_sem_janela':repeat_count,
    'ocorrencias':dict(issues),
}
print(json.dumps(result,ensure_ascii=False,indent=2))
