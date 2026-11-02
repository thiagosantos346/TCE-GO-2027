import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
CHUNKS_DONE_DIR = BASE_DIR / "data" / "chunks_processados"
BANCO_FINAL_PATH = BASE_DIR / "data" / "banco_questoes_v3_limpo.json"

def merge_db():
    banco_consolidado = []
    lixo_count = 0
    
    arquivos = sorted(CHUNKS_DONE_DIR.glob("lote_*.json"))
    for arquivo in arquivos:
        lote = json.loads(arquivo.read_text(encoding="utf-8"))
        for q in lote:
            if q.get("target_topico") in ["LIXO", "DESCARTADA"]:
                lixo_count += 1
            else:
                banco_consolidado.append(q)
                
    BANCO_FINAL_PATH.write_text(json.dumps(banco_consolidado, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Recombinação concluída. {len(banco_consolidado)} questões válidas salvas. {lixo_count} questões descartadas expurgadas.")

if __name__ == "__main__":
    merge_db()
