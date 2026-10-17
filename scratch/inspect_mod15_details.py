import json
import re

with open("scratch/candidates_by_file.json", "r", encoding="utf-8") as f:
    cand_by_file = json.load(f)

mod15_files = [
    "01_regime_juridico_principios_e_lindb.md",
    "02_organizacao_administrativa_e_poderes.md",
    "03_atos_administrativos_e_processo_estadual.md",
    "04_servicos_publicos_bens_e_responsabilidade_civil.md",
    "05_controle_da_administracao_e_improbidade_administrativa.md",
    "06_acesso_a_informacao_e_contratos_publicidade.md"
]

base_dir = "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/15_nocoes_de_direito_administrativo"

for fname in mod15_files:
    fpath = f"{base_dir}/{fname}"
    with open(fpath, "r", encoding="utf-8") as f:
        text = f.read()
    
    # get sections without questions
    sections = re.findall(r"(###? \d+[\.\d]* [^\n]+)", text)
    existing_qs = re.findall(r"### Questão (\d+)", text)
    cands = cand_by_file.get(fpath, [])
    
    print("="*70)
    print(f"FILE: {fname}")
    print(f"Existing questions: {existing_qs}")
    print(f"Available candidates in json: {len(cands)}")
    print("Key theoretical sections:")
    for s in sections[:12]:
        print("  *", s)
