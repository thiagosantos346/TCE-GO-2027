import os
import re
import json

files = [
    "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/15_nocoes_de_direito_administrativo/01_regime_juridico_principios_e_lindb.md",
    "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/15_nocoes_de_direito_administrativo/02_organizacao_administrativa_e_poderes.md",
    "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/15_nocoes_de_direito_administrativo/03_atos_administrativos_e_processo_estadual.md",
    "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/15_nocoes_de_direito_administrativo/04_servicos_publicos_bens_e_responsabilidade_civil.md",
    "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/15_nocoes_de_direito_administrativo/05_controle_da_administracao_e_improbidade_administrativa.md",
    "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/15_nocoes_de_direito_administrativo/06_acesso_a_informacao_e_contratos_publicidade.md",
    "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/16_licitacoes_e_contratos_administrativos/01_governanca_planejamento_etp_tr_e_matriz_riscos.md",
    "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/16_licitacoes_e_contratos_administrativos/02_fases_modalidades_e_criterios_de_julgamento.md",
    "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/16_licitacoes_e_contratos_administrativos/03_procedimentos_auxiliares_e_contratacao_direta.md",
    "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/16_licitacoes_e_contratos_administrativos/04_contratos_administrativos_fiscalizacao_alteracoes_e_sancoes.md",
    "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/17_nocoes_de_direito_constitucional/01_aplicabilidade_das_normas_e_principios_fundamentais.md",
    "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/17_nocoes_de_direito_constitucional/02_direitos_e_garantias_fundamentais_e_politicos.md",
    "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/17_nocoes_de_direito_constitucional/03_organizacao_do_estado_e_reparticao_de_competencias.md",
    "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/17_nocoes_de_direito_constitucional/04_poder_legislativo_processo_legislativo_e_fiscalizacao_tce.md",
    "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/17_nocoes_de_direito_constitucional/05_poder_executivo_poder_judiciario_e_funcoes_essenciais.md",
    "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/18_nocoes_de_controle_externo/01_sistema_constitucional_e_jurisdicao_dos_tcs.md",
    "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/18_nocoes_de_controle_externo/02_instrumentos_e_tipos_de_auditoria_governamental_nbasp.md",
    "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/18_nocoes_de_controle_externo/03_planejamento_amostragem_procedimentos_e_achados.md",
    "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/18_nocoes_de_controle_externo/04_relatorios_processo_de_controle_externo_e_sancoes.md"
]

summary_data = []

for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Find all headings and existing questions
    lines = content.splitlines()
    h2_h3 = []
    for l in lines:
        if l.startswith("## ") or (l.startswith("### ") and not l.startswith("### Questão")):
            h2_h3.append(l)
    
    questions = re.findall(r"### Questão (\d+)", content)
    summary_data.append({
        "path": fpath,
        "filename": os.path.basename(fpath),
        "existing_questions": questions,
        "headings": h2_h3
    })

with open("scratch/headings_summary.json", "w", encoding="utf-8") as f:
    json.dump(summary_data, f, ensure_ascii=False, indent=2)

print("Saved scratch/headings_summary.json successfully.")
