import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
BANCO_PATH = BASE_DIR / "data" / "banco_questoes_v3.json"
DOCS_DIR = BASE_DIR / "docs"

BLACKLIST = [
    "06_engenharia_software_ia_e_sistemas_agentivos",
    "04_lei_complementar_estadual_205_2025.md",
    "06_politicas_institucionais_e_resolucoes_normativas.md"
]

def formatar_questao(q, num):
    alt_str = "\n".join([f"* **{k})** {v}" for k, v in q["alternativas"].items()])
    return f"""

<div class="question-card">
<h3 id="topic_teste_{num}">Teste {num:03d}</h3>
<p><strong>({q['banca']} – {q['orgao']} – {q['ano']} – {q['cargo']})</strong><br>
{q['enunciado']}</p>
<ul class="options-list">
{alt_str}
</ul>
</div>

<blockquote>
<p><strong>Gabarito Oficial: {q['gabarito_oficial']}</strong></p>
</blockquote>
"""

def injetar_questoes():
    banco = json.loads(BANCO_PATH.read_text(encoding="utf-8"))
    
    # Agrupar questões por tópico
    mapa_questoes = {}
    for q in banco:
        if q.get("target_topico") == "LIXO":
            continue
        topico = q.get("target_topico", "").strip()
        if topico not in mapa_questoes:
            mapa_questoes[topico] = []
        mapa_questoes[topico].append(q)

    injetadas = 0
    contador_global = 1

    for md_file in DOCS_DIR.rglob("*.md"):
        if any(b in str(md_file) for b in BLACKLIST):
            continue

        texto = md_file.read_text(encoding="utf-8")
        
        # Encontra todos os tópicos no arquivo (## 1. Titulo)
        matches = list(re.finditer(r'^## (\d+\.\d+.*?)$', texto, flags=re.MULTILINE))
        
        if not matches:
            continue
            
        novo_texto = texto
        offset = 0

        for match in matches:
            titulo_topico = match.group(1).strip()
            
            # Buscar no mapa de questões se existe algo para este título (parcial ou exato)
            questoes_alvo = []
            for chave, lista_q in mapa_questoes.items():
                if chave.lower() in titulo_topico.lower():
                    questoes_alvo.extend(lista_q)
                    
            if questoes_alvo:
                # Localizar o fim desta seção (próximo ## ou EOF)
                pos_atual = match.end() + offset
                proximo_h2 = re.search(r'\n## ', novo_texto[pos_atual:])
                
                fim_secao = pos_atual + proximo_h2.start() if proximo_h2 else len(novo_texto)
                
                bloco_injecao = ""
                for q in questoes_alvo:
                    bloco_injecao += formatar_questao(q, contador_global)
                    contador_global += 1
                    injetadas += 1
                
                novo_texto = novo_texto[:fim_secao] + bloco_injecao + novo_texto[fim_secao:]
                offset += len(bloco_injecao)
        
        if texto != novo_texto:
            md_file.write_text(novo_texto, encoding="utf-8")

    print(f"Injeção concluída. {injetadas} questões anexadas aos markdowns limpos.")

if __name__ == "__main__":
    injetar_questoes()