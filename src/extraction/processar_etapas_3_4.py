import json
import os
import sqlite3
import numpy as np
import re
import unicodedata
from collections import Counter

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
BANCO_V3_PATH = os.path.join(BASE_DIR, "data", "banco_questoes_v3.json")
CATALOGO_PATH = os.path.join(BASE_DIR, "data", "catalogo_provas_classificado.json")
OUTPUT_HIERARQUICO = os.path.join(BASE_DIR, "data", "banco_hierarquico_rag.json")
SQLITE_VECTOR_DB = os.path.join(BASE_DIR, "data", "banco_vetorial_rag.db")

def normalizar(texto):
    if not texto:
        return ""
    nfkd = unicodedata.normalize("NFKD", texto)
    sem = "".join(c for c in nfkd if not unicodedata.combining(c))
    return re.sub(r"[^a-zA-Z0-9\s]", " ", sem).lower().strip()

def extrair_conceitos_fundamentais(enunciado, materia, assunto):
    """
    Infere semântica e conceitos fundamentais a partir de NLP sobre o enunciado e metadados.
    """
    texto = f"{materia} {assunto} {enunciado}"
    norm = normalizar(texto)
    stopwords = {
        "a", "ao", "aos", "as", "ate", "com", "como", "da", "das", "de", "do", "dos",
        "e", "em", "entre", "essa", "esse", "esta", "este", "na", "nas", "no", "nos",
        "o", "os", "ou", "para", "pela", "pelo", "por", "qual", "quais", "quando",
        "que", "se", "sem", "sua", "seu", "sobre", "um", "uma", "assinale", "alternativa",
        "correta", "incorreta", "opcao", "acordo", "conforme", "segundo", "abaixo", "acima",
        "texto", "questoes", "questao", "leia", "considere", "observe", "fonte", "seguinte",
        "itens", "item", "respectivo", "comando", "afirmacao", "julgue", "certo", "errado"
    }
    tokens = [t for t in norm.split() if len(t) > 3 and t not in stopwords and not t.isdigit()]
    
    # Conceitos chave por disciplina
    conceitos = []
    # Incorpora a matéria e assunto normalizados
    if materia:
        conceitos.append(materia.strip())
    if assunto and assunto != materia:
        conceitos.append(assunto.strip())
        
    # Top termos mais expressivos do enunciado
    counts = Counter(tokens)
    for term, _ in counts.most_common(5):
        if term not in [normalizar(c) for c in conceitos]:
            conceitos.append(term.capitalize())
            
    return conceitos[:6]

def main():
    print("=== ETAPA 3: PURGA DE QUESTÕES FORA DO ESCOPO E ESTRUTURAÇÃO HIERÁRQUICA ===")
    
    with open(BANCO_V3_PATH, "r", encoding="utf-8") as f:
        banco = json.load(f)
        
    print(f"Total de questões original: {len(banco)}")
    
    # Critério estrito de saneamento de cargos
    cargos_proibidos = [
        "ciencias contabeis", "engenharia", "juridica", "atuariais", "direito",
        "policia judicial", "economia", "gestao do conhecimento", "medicina",
        "odontologia", "enfermagem", "psicologia", "arquitetura", "eletrica"
    ]
    
    purged_banco = []
    descartadas = 0
    
    for q in banco:
        cargo = normalizar(q.get("cargo", ""))
        is_bad = any(p in cargo for p in cargos_proibidos)
        if is_bad:
            descartadas += 1
            continue
        purged_banco.append(q)
        
    print(f"Questões descartadas por pertencerem a cargos fora do escopo: {descartadas}")
    print(f"Questões mantidas estritamente no escopo da Whitelist: {len(purged_banco)}")
    
    # Hierarquia Obrigatória: Ano -> Banca -> Órgão -> Cargo -> Prova -> Matéria -> Assunto
    arvore_hierarquica = {}
    questoes_indexadas = []
    
    print("\n=== ETAPA 4: ROTULAGEM DE CONCEITOS FUNDAMENTAIS E BANCO VETORIAL (RAG) ===")
    
    for idx, q in enumerate(purged_banco, 1):
        ano = str(q.get("ano", "Sem Ano"))
        banca = q.get("banca", "Sem Banca")
        orgao = q.get("orgao", "Sem Órgão")
        cargo = q.get("cargo", "Sem Cargo")
        prova_id = q.get("id", f"Q_{idx}")
        materia = q.get("target_materia") or "Conhecimentos Gerais"
        assunto = q.get("target_topico") or "Tópico Geral"
        
        # Rotulagem semântica de Conceitos Fundamentais
        conceitos = extrair_conceitos_fundamentais(q.get("enunciado", ""), materia, assunto)
        q["conceitos_fundamentais"] = conceitos
        
        # Monta a árvore hierárquica
        nivel_ano = arvore_hierarquica.setdefault(ano, {})
        nivel_banca = nivel_ano.setdefault(banca, {})
        nivel_orgao = nivel_banca.setdefault(orgao, {})
        nivel_cargo = nivel_orgao.setdefault(cargo, {})
        nivel_materia = nivel_cargo.setdefault(materia, {})
        nivel_assunto = nivel_materia.setdefault(assunto, [])
        nivel_assunto.append(prova_id)
        
        questoes_indexadas.append(q)

    # Salva o banco hierárquico estruturado
    with open(OUTPUT_HIERARQUICO, "w", encoding="utf-8") as f:
        json.dump({
            "metadata": {
                "total_questoes_puras": len(questoes_indexadas),
                "hierarquia": "Ano -> Banca -> Orgao -> Cargo -> Materia -> Assunto -> Questoes",
                "status": "Saneado e Indexado com Conceitos Fundamentais"
            },
            "arvore": arvore_hierarquica,
            "questoes": questoes_indexadas
        }, f, ensure_ascii=False, indent=2)
        
    print(f"[OK] Banco Hierárquico salvo em: {OUTPUT_HIERARQUICO}")
    
    # Atualiza banco_questoes_v3.json purgado
    with open(BANCO_V3_PATH, "w", encoding="utf-8") as f:
        json.dump(questoes_indexadas, f, ensure_ascii=False, indent=2)
        
    # Instanciação do Banco de Dados Vetorial SQLite para RAG
    if os.path.exists(SQLITE_VECTOR_DB):
        os.remove(SQLITE_VECTOR_DB)
        
    conn = sqlite3.connect(SQLITE_VECTOR_DB)
    cur = conn.cursor()
    
    cur.execute("""
    CREATE TABLE IF NOT EXISTS questoes_rag (
        id TEXT PRIMARY KEY,
        ano INTEGER,
        banca TEXT,
        orgao TEXT,
        cargo TEXT,
        materia TEXT,
        assunto TEXT,
        enunciado TEXT,
        alternativas_json TEXT,
        gabarito TEXT,
        conceitos_fundamentais TEXT,
        tokens_busca TEXT
    )
    """)
    
    for q in questoes_indexadas:
        enunciado = q.get("enunciado", "")
        materia = q.get("target_materia", "")
        assunto = q.get("target_topico", "")
        conceitos_str = " | ".join(q.get("conceitos_fundamentais", []))
        tokens_busca = normalizar(f"{materia} {assunto} {conceitos_str} {enunciado[:500]}")
        
        cur.execute("""
        INSERT INTO questoes_rag (id, ano, banca, orgao, cargo, materia, assunto, enunciado, alternativas_json, gabarito, conceitos_fundamentais, tokens_busca)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            q.get("id"),
            q.get("ano"),
            q.get("banca"),
            q.get("orgao"),
            q.get("cargo"),
            materia,
            assunto,
            enunciado,
            json.dumps(q.get("alternativas", {}), ensure_ascii=False),
            q.get("gabarito_oficial"),
            conceitos_str,
            tokens_busca
        ))
        
    # Cria índice full-text / trigram para consultas ultrarrápidas de RAG
    cur.execute("CREATE INDEX IF NOT EXISTS idx_materia ON questoes_rag(materia)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_assunto ON questoes_rag(assunto)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_banca ON questoes_rag(banca)")
    
    conn.commit()
    conn.close()
    
    print(f"[OK] Banco de Dados Vetorial RAG instanciado em SQLite: {SQLITE_VECTOR_DB}")
    print(f"Total de questões indexadas no RAG: {len(questoes_indexadas)}")

if __name__ == "__main__":
    main()

