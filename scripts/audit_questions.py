import json
import os
import glob
import re

def audit():
    with open('banco_questoes_extraidas.json', 'r', encoding='utf-8') as f:
        db = json.load(f)

    questoes_db = db.get('questoes', [])
    total_banco = len(questoes_db)
    injetadas_db = sum(1 for q in questoes_db if q.get('status_integracao') == 'injetada')
    pendentes_db = sum(1 for q in questoes_db if q.get('status_integracao') != 'injetada')

    all_mds = []
    for root, dirs, files in os.walk('fontes_de_estudo'):
        if 'resources' in root:
            continue
        for f in files:
            if f.endswith('.md') and not f.endswith('README.md'):
                all_mds.append(os.path.join(root, f).replace('\\', '/'))

    modules_stat = {}
    total_questoes_files = 0
    total_reais_files = 0
    total_sim_files = 0

    for path in sorted(all_mds):
        content = open(path, encoding='utf-8').read()
        headers = re.findall(r'### Teste \d+\s*\n([^\n]+)', content)
        
        parts = path.split('/')
        module = parts[2]
        
        if module not in modules_stat:
            modules_stat[module] = {"total": 0, "reais": 0, "simuladas": 0, "arquivos": 0}
        
        modules_stat[module]["arquivos"] += 1
        
        for h in headers:
            total_questoes_files += 1
            modules_stat[module]["total"] += 1
            if 'Simulada' in h or 'Inédita' in h:
                total_sim_files += 1
                modules_stat[module]["simuladas"] += 1
            else:
                total_reais_files += 1
                modules_stat[module]["reais"] += 1

    print("=" * 85)
    print(f"{'MÓDULO':<50} | {'REAIS':<6} | {'SIM':<6} | {'TOTAL':<6} | {'% REAL':<8}")
    print("=" * 85)
    for mod, stat in sorted(modules_stat.items()):
        pct = (stat['reais'] / stat['total'] * 100) if stat['total'] > 0 else 0
        print(f"{mod:<50} | {stat['reais']:<6} | {stat['simuladas']:<6} | {stat['total']:<6} | {pct:>6.1f}%")
    print("=" * 85)
    pct_global = (total_reais_files / total_questoes_files * 100) if total_questoes_files > 0 else 0
    print(f"{'TOTAL GERAL':<50} | {total_reais_files:<6} | {total_sim_files:<6} | {total_questoes_files:<6} | {pct_global:>6.1f}%")
    print("=" * 85)
    print(f"Banco de Questões: {total_banco} itens ({injetadas_db} marcadas injetadas, {pendentes_db} pendentes)")

if __name__ == '__main__':
    audit()
