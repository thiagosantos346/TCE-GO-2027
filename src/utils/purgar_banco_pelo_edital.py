"""Purga do banco V3: remove questões sem similaridade TF-IDF com a ementa do edital.

Uso: python src/utils/purgar_banco_pelo_edital.py [--limiar 0.06] [--dry-run]
Implementação TF-IDF em Python puro (sem dependência de sklearn).
"""
import argparse
import json
import math
import re
import unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BANCO = ROOT / "data" / "banco_questoes_v3.json"
EDITAL = ROOT / "data" / "edital_estruturado.json"

STOP = set("""a o as os um uma uns umas de do da dos das em no na nos nas por para com sem sobre entre e ou que se
ao aos à às é são ser foi como mais menos não seu sua seus suas este esta estes estas isso essa esse pelo pela
pelos pelas qual quais assinale alternativa afirmativa correta incorreta acordo considerando seguir item itens
afirmativas julgue pode podem deve devem apenas também ainda quando onde cada todo toda""".split())


def tokenizar(txt):
    txt = unicodedata.normalize("NFKD", txt.lower())
    txt = "".join(c for c in txt if not unicodedata.combining(c))
    toks = re.findall(r"[a-z0-9]{3,}", txt)
    stop = {unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode() for s in STOP}
    # stemming leve: trunca em 6 caracteres para casar flexões
    return [t[:6] for t in toks if t not in stop]


def textos_edital(edital):
    docs = []
    for area in edital["areas"]:
        for mat in area["materias"]:
            docs.append(mat["nome_materia"] + " " + " ".join(mat["topicos"]))
    return docs


def texto_questao(q):
    alts = q.get("alternativas") or {}
    alts = " ".join(alts.values()) if isinstance(alts, dict) else " ".join(map(str, alts))
    return f"{q.get('enunciado', '')} {alts}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limiar", type=float, default=0.06)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    banco = json.loads(BANCO.read_text(encoding="utf-8"))
    edital = json.loads(EDITAL.read_text(encoding="utf-8"))
    docs_ed = [tokenizar(t) for t in textos_edital(edital)]
    docs_q = [tokenizar(texto_questao(q)) for q in banco]

    n = len(docs_ed) + len(docs_q)
    df = Counter()
    for d in docs_ed + docs_q:
        df.update(set(d))
    idf = {t: math.log((1 + n) / (1 + c)) + 1 for t, c in df.items()}

    def vec(toks):
        tf = Counter(toks)
        v = {t: (1 + math.log(c)) * idf[t] for t, c in tf.items()}
        norm = math.sqrt(sum(x * x for x in v.values())) or 1.0
        return {t: x / norm for t, x in v.items()}

    vs_ed = [vec(d) for d in docs_ed]
    # índice invertido para velocidade
    inv = {}
    for i, v in enumerate(vs_ed):
        for t, w in v.items():
            inv.setdefault(t, []).append((i, w))

    mantidas, removidas = [], []
    for q, d in zip(banco, docs_q):
        v = vec(d)
        sims = Counter()
        for t, w in v.items():
            for i, w2 in inv.get(t, ()):
                sims[i] += w * w2
        score = max(sims.values()) if sims else 0.0
        q["score_edital"] = round(score, 4)
        (mantidas if score >= args.limiar else removidas).append(q)

    print(f"Total: {len(banco)} | mantidas: {len(mantidas)} | removidas: {len(removidas)} (limiar={args.limiar})")
    if args.dry_run:
        return
    for q in mantidas:
        q.pop("score_edital", None)
    BANCO.write_text(json.dumps(mantidas, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Banco salvo: {BANCO} ({BANCO.stat().st_size / 1024:.1f} KB)")
    print(f"DELETADAS: {len(removidas)}")


if __name__ == "__main__":
    main()

