import os
import re

target_files = [
    # Módulo 15 (6 arquivos)
    "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/15_nocoes_de_direito_administrativo/01_regime_juridico_principios_e_lindb.md",
    "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/15_nocoes_de_direito_administrativo/02_organizacao_administrativa_e_poderes.md",
    "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/15_nocoes_de_direito_administrativo/03_atos_administrativos_e_processo_estadual.md",
    "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/15_nocoes_de_direito_administrativo/04_servicos_publicos_bens_e_responsabilidade_civil.md",
    "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/15_nocoes_de_direito_administrativo/05_controle_da_administracao_e_improbidade_administrativa.md",
    "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/15_nocoes_de_direito_administrativo/06_acesso_a_informacao_e_contratos_publicidade.md",
    # Módulo 16 (4 arquivos)
    "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/16_licitacoes_e_contratos_administrativos/01_governanca_planejamento_etp_tr_e_matriz_riscos.md",
    "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/16_licitacoes_e_contratos_administrativos/02_fases_modalidades_e_criterios_de_julgamento.md",
    "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/16_licitacoes_e_contratos_administrativos/03_procedimentos_auxiliares_e_contratacao_direta.md",
    "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/16_licitacoes_e_contratos_administrativos/04_contratos_administrativos_fiscalizacao_alteracoes_e_sancoes.md",
    # Módulo 17 (5 arquivos)
    "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/17_nocoes_de_direito_constitucional/01_aplicabilidade_das_normas_e_principios_fundamentais.md",
    "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/17_nocoes_de_direito_constitucional/02_direitos_e_garantias_fundamentais_e_politicos.md",
    "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/17_nocoes_de_direito_constitucional/03_organizacao_do_estado_e_reparticao_de_competencias.md",
    "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/17_nocoes_de_direito_constitucional/04_poder_legislativo_processo_legislativo_e_fiscalizacao_tce.md",
    "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/17_nocoes_de_direito_constitucional/05_poder_executivo_poder_judiciario_e_funcoes_essenciais.md",
    # Módulo 18 (4 arquivos)
    "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/18_nocoes_de_controle_externo/01_sistema_constitucional_e_jurisdicao_dos_tcs.md",
    "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/18_nocoes_de_controle_externo/02_instrumentos_e_tipos_de_auditoria_governamental_nbasp.md",
    "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/18_nocoes_de_controle_externo/03_planejamento_amostragem_procedimentos_e_achados.md",
    "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/18_nocoes_de_controle_externo/04_relatorios_processo_de_controle_externo_e_sancoes.md"
]

print(f"Total target files to audit: {len(target_files)}")
print("="*80)

total_questions_all = 0
all_passed = True

results = []

for idx, fpath in enumerate(target_files, 1):
    assert os.path.exists(fpath), f"File not found: {fpath}"
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    questions = re.findall(r"### Questão (\d+)", content)
    q_count = len(questions)
    total_questions_all += q_count
    
    # Check mermaid
    mermaid_count = len(re.findall(r"```mermaid", content))
    
    # Check original 01 to 05 preserved
    orig_preserved = all(f"### Questão 0{i}" in content for i in range(1, 6))
    
    # Check gabarito counts
    gabaritos = re.findall(r">\s*\*\*Gabarito:\s*([A-E])\*\*", content)
    
    status = "OK" if (10 <= q_count <= 12 and orig_preserved and len(gabaritos) == q_count) else "FAIL"
    if status == "FAIL":
        all_passed = False
        
    fname = os.path.basename(fpath)
    module_name = fpath.split("/")[2]
    
    results.append({
        "num": idx,
        "module": module_name,
        "file": fname,
        "q_count": q_count,
        "mermaid": mermaid_count,
        "gabaritos": len(gabaritos),
        "orig_preserved": orig_preserved,
        "status": status,
        "questions_list": questions
    })
    
    print(f"[{idx:02d}/19] {fname} | Questões: {q_count} | Gabaritos: {len(gabaritos)} | Mermaid: {mermaid_count} | Status: {status}")

print("="*80)
print(f"AUDITORIA GERAL CONCLUÍDA! Sucesso em todos os 19 arquivos? {all_passed}")
print(f"Total global de questões nos 19 arquivos: {total_questions_all} questões")
