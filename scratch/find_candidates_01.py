import json
import os
import re

with open("scratch/candidates_by_file.json", "r", encoding="utf-8") as f:
    cand_by_file = json.load(f)

with open("banco_questoes_extraidas.json", "r", encoding="utf-8") as f:
    banco = json.load(f)

def find_best_candidates(file_key, keywords_dict):
    # Check candidates already allocated to this file
    allocated = cand_by_file.get(file_key, [])
    # Also check whole banco if needed
    all_qs = allocated + banco["questoes"]
    
    seen_texts = set()
    results = {}
    
    for topic, kw_list in keywords_dict.items():
        results[topic] = []
        for q in all_qs:
            txt = (q.get("enunciado", "") + " " + " ".join(q.get("alternativas", {}).values())).lower()
            enun_clean = q.get("enunciado", "").strip()[:80]
            if enun_clean in seen_texts:
                continue
            
            # check match
            matches = sum(1 for kw in kw_list if kw.lower() in txt)
            if matches >= 1:
                # check if it has valid alternatives and gabarito
                alts = q.get("alternativas", {})
                gab = q.get("gabarito_oficial")
                if len(alts) >= 4 and gab in ["A", "B", "C", "D", "E"]:
                    results[topic].append((matches, q))
        
        # Sort by match score and recency
        results[topic].sort(key=lambda x: (x[0], x[1].get("ano", 2000)), reverse=True)
        # deduplicate
        unique_topic = []
        for score, q in results[topic]:
            enun_clean = q.get("enunciado", "").strip()[:80]
            if enun_clean not in seen_texts:
                seen_texts.add(enun_clean)
                unique_topic.append(q)
                if len(unique_topic) >= 5:
                    break
        results[topic] = unique_topic
    
    return results

fkey_01 = "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/15_nocoes_de_direito_administrativo/01_regime_juridico_principios_e_lindb.md"
kw_01 = {
    "1. Sentido de Administração Pública": ["sentido subjetivo", "sentido objetivo", "órgãos e entidades", "função administrativa", "critério formal"],
    "2. Regime Jurídico e Bipolaridade": ["supremacia do interesse público", "indisponibilidade do interesse público", "interesse público primário", "prerrogativas e sujeições"],
    "3.1 Legalidade Estrita": ["princípio da legalidade", "não há crime sem lei", "autonomia da vontade", "subordinação à lei"],
    "3.5 Princípio da Eficiência": ["princípio da eficiência", "avaliação de desempenho", "emenda constitucional nº 19", "reforma administrativa"],
    "4.4 Teoria dos Motivos Determinantes": ["motivos determinantes", "motivação do ato", "inexistência do motivo", "falsidade do motivo"],
    "5. LINDB Consequencialismo / Segurança Jurídica": ["art. 20", "consequências práticas", "art. 21", "art. 22", "obstáculos reais", "art. 23", "regime de transição", "lindb"]
}

res = find_best_candidates(fkey_01, kw_01)
for topic, qs in res.items():
    print(f"\n=== TOPIC: {topic} (Found: {len(qs)}) ===")
    for idx, q in enumerate(qs[:2]):
        print(f"  [{idx+1}] {q.get('id')} | {q.get('banca')} {q.get('ano')} {q.get('orgao')} | Gab: {q.get('gabarito_oficial')}")
        print(f"      Enunciado: {q.get('enunciado', '').replace(chr(10), ' ')[:140]}...")
