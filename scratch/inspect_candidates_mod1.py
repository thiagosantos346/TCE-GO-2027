import json, re

with open('scratch/candidates_by_file.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

f1 = 'fontes_de_estudo/conhecimentos_gerais/01_lingua_portuguesa/01_compreensao_e_interpretacao_de_texto.md'
qs = data.get(f1, [])

print(f"Total questions in 01_compreensao: {len(qs)}")

# Let's search for keywords in enunciado
keywords = {
    'genero': ['gênero', 'editorial', 'crônica', 'notícia', 'artigo de opinião'],
    'tipologia': ['dissertativo', 'narrativo', 'descritivo', 'injuntivo', 'tipologia'],
    'argumentacao': ['tese', 'argumento', 'estratégia argumentativa', 'ponto de vista'],
    'pressuposto': ['pressupost', 'subentendid', 'infere-se', 'depreende-se'],
    'intertextualidade': ['intertextual', 'citação', 'paráfrase', 'alud'],
    'figuras': ['metáfora', 'metonímia', 'ironia', 'antítese', 'paradoxo']
}

for kw_cat, words in keywords.items():
    print(f"\n=== CATEGORIA: {kw_cat} ===")
    matches = []
    for q in qs:
        text = (q.get('enunciado', '') + ' ' + json.dumps(q.get('alternativas', {}))).lower()
        if any(w in text for w in words):
            matches.append(q)
    print(f"Encontrados: {len(matches)}")
    for m in matches[:3]:
        print(f"  - [{m.get('banca')}] {m.get('id')} ({m.get('orgao')}, {m.get('ano')}): {m.get('enunciado')[:90].replace(chr(10), ' ')}")
