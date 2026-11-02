import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
BANCO_PATH = BASE_DIR / "data" / "banco_questoes_v3.json"
CHUNKS_DIR = BASE_DIR / "data" / "chunks_pendentes"
CHUNKS_DIR.mkdir(parents=True, exist_ok=True)

def split_db(chunk_size=50):
    banco = json.loads(BANCO_PATH.read_text(encoding="utf-8"))
    
    for i in range(0, len(banco), chunk_size):
        lote = banco[i:i + chunk_size]
        lote_id = (i // chunk_size) + 1
        arquivo_saida = CHUNKS_DIR / f"lote_{lote_id:03d}.json"
        arquivo_saida.write_text(json.dumps(lote, ensure_ascii=False, indent=2), encoding="utf-8")
        
    print(f"Divisão concluída: {len(banco)} questões divididas em {(len(banco)//chunk_size)+1} lotes de {chunk_size} em {CHUNKS_DIR}")

if __name__ == "__main__":
    split_db() 