import json
import os
from collections import Counter

data = json.load(open('banco_questoes_extraidas.json', 'r', encoding='utf-8'))
folder = 'fontes_de_estudo/conhecimentos_gerais/01_lingua_portuguesa/'
counts = Counter()
for q in data['questoes']:
    tf = q.get('target_file', '')
    if q.get('status_integracao') == 'pendente' and tf.startswith(folder):
        counts[os.path.basename(tf)] += 1

for k, v in sorted(counts.items()):
    print(f"{k}: {v} pendentes")

