import json
import os
import re

ROOT = os.getcwd()
banco_path = os.path.join(ROOT, "banco_questoes_extraidas.json")

with open(banco_path, "r", encoding="utf-8") as f:
    banco = json.load(f)

# Agrupar questoes por target_file e target_section
file_candidates = {}

for q in banco["questoes"]:
    tf = q["target_file"]
    file_candidates.setdefault(tf, []).append(q)

print(f"Total questoes no banco: {len(banco['questoes'])}")
print(f"Total arquivos alvo: {len(file_candidates)}")

# Salvar candidatos estruturados por arquivo em scratch/candidates_by_file.json
out_path = os.path.join(ROOT, "scratch", "candidates_by_file.json")
os.makedirs(os.path.dirname(out_path), exist_ok=True)

with open(out_path, "w", encoding="utf-8") as f:
    json.dump(file_candidates, f, ensure_ascii=False, indent=2)

print(f"Arquivo gerado: {out_path}")

