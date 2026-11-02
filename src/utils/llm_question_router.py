import json
import os
import time
from pathlib import Path
from pydantic import BaseModel
from google import genai
from google.genai import types

BASE_DIR = Path(__file__).resolve().parents[2]
BANCO_PATH = BASE_DIR / "data" / "banco_questoes_v3.json"
EDITAL_PATH = BASE_DIR / "data" / "edital_estruturado.json"

class QuestionClassification(BaseModel):
    id_questao: str
    target_area: str
    target_materia: str
    target_topico: str

def load_edital_tree():
    data = json.loads(EDITAL_PATH.read_text(encoding="utf-8"))
    linhas = []
    for area in data.get("areas", []):
        linhas.append(f"\n# ÁREA: {area.get('nome_area')}")
        for mat in area.get("materias", []):
            linhas.append(f"  ## MATÉRIA: {mat.get('nome_materia')}")
            for top in mat.get("topicos", []):
                linhas.append(f"    - {top}")
    return "\n".join(linhas)

def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("ERRO: GEMINI_API_KEY não configurada.")
        return

    client = genai.Client(api_key=api_key)
    banco = json.loads(BANCO_PATH.read_text(encoding="utf-8"))
    arvore_edital = load_edital_tree()

    print(f"Processando {len(banco)} questões via LLM (gemini-1.5-flash)...")
    processadas = 0

    for q in banco:
        q_id = q.get("id")
        
        prompt = f"""Você é um classificador de questões de concurso público. Analise o ID: {q_id}. Leia o enunciado e as alternativas. 
        PASSO 1: Identifique a disciplina real da questão (Direito, Contabilidade, TI, etc.). 
        PASSO 2: Verifique se essa disciplina existe na árvore do edital fornecida. Se a questão for sobre Contabilidade, Direito Civil, ou qualquer tema ausente na árvore de TI/Administrativo, defina 'target_topico' obrigatoriamente como 'LIXO'. Se pertencer ao edital, extraia a area, materia e topico exatos. 
        Você DEVE retornar o campo 'id_questao' exatamente igual ao fornecido para garantir a integridade dos dados.
        
        === ÁRVORE DO EDITAL ===
        {arvore_edital}

        === QUESTÃO ===
        Enunciado: {q.get('enunciado')}
        Alternativas: {json.dumps(q.get('alternativas'), ensure_ascii=False)}
        """

        success = False
        retries = 0
        while not success and retries < 3:
            try:
                response = client.models.generate_content(
                    model='gemini-3.5-flash',
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        response_mime_type="application/json",
                        response_schema=QuestionClassification,
                        temperature=0.0,
                    ),
                )
                result = json.loads(response.text)
                
                # ID Locking para evitar Race Conditions/Alucinações
                if result.get("id_questao") == q_id:
                    q["target_area"] = result.get("target_area")
                    q["target_materia"] = result.get("target_materia")
                    q["target_topico"] = result.get("target_topico")
                    q["llm_classified"] = True
                    print(f"[{q_id}] -> {q['target_topico'][:40]}")
                    success = True
                else:
                    print(f"[{q_id}] Mismatch de ID. Re-tentando...")
                    retries += 1
                    time.sleep(2)
                    
            except Exception as e:
                print(f"[{q_id}] Erro API: {e}. Aguardando rate limit...")
                retries += 1
                time.sleep(5)
        
        processadas += 1
        # Checkpoint a cada 100 questões
        if processadas % 100 == 0:
            BANCO_PATH.write_text(json.dumps(banco, ensure_ascii=False, indent=2), encoding="utf-8")

    # Purga defintiva do LIXO e gravação final
    banco_limpo = [q for q in banco if q.get("target_topico") != "LIXO"]
    BANCO_PATH.write_text(json.dumps(banco_limpo, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n[+] Classificação Concluída. {len(banco) - len(banco_limpo)} questões excluídas. Restaram {len(banco_limpo)} questões puras.")

if __name__ == "__main__":
    main()