import json

data = json.load(open('banco_questoes_extraidas.json', 'r', encoding='utf-8'))
questoes = [q for q in data['questoes'] if q.get('status_integracao') == 'pendente']

def find_best(keywords, pref_banca='FCC'):
    candidates = []
    for q in questoes:
        text = (q['enunciado'] + ' ' + ' '.join(q['alternativas'].values())).lower()
        if any(w in text for w in keywords):
            candidates.append(q)
    # sort by pref_banca
    candidates.sort(key=lambda q: (0 if q['banca'] == pref_banca else 1, -q['ano']))
    return candidates

topics = [
    ("Teste 001: Compreensão / Interpretação Textual", ['depreende-se', 'compreensão', 'infere-se', 'de acordo com o texto']),
    ("Teste 002: Gêneros Textuais (Editorial, Crônica, Artigo, Ensaio)", ['gênero textual', 'editorial', 'crônica', 'ensaio', 'artigo de opinião']),
    ("Teste 003: Tipologia Textual (Narrativo, Descritivo, Dissertativo, Injuntivo)", ['tipo de texto', 'tipo textual', 'tipologia', 'texto narrativo', 'texto descritivo', 'texto dissertativo', 'texto injuntivo']),
    ("Teste 004: Tese e Estratégia Argumentativa", ['tese defendida', 'estratégia argumentativa', 'argumento principal', 'objetivo argumentativo', 'tese']),
    ("Teste 005: Pressupostos e Subentendidos", ['pressuposto', 'subentendido', 'pressupõe', 'implícito']),
    ("Teste 006: Denotação e Conotação (Sentido Figurado)", ['sentido figurado', 'linguagem figurada', 'conotativo', 'denotativo']),
    ("Teste 007: Discurso Direto e Indireto", ['discurso direto', 'discurso indireto', 'fala da personagem', 'voz do narrador']),
    ("Teste 008: Transposição de Discurso", ['transposição para o discurso', 'passando para o discurso indireto', 'discurso indireto']),
    ("Teste 009: Intertextualidade / Paráfrase", ['paráfrase', 'mantém o sentido original', 'reescritura', 'redação correta e coerente']),
    ("Teste 010: Figuras de Linguagem (Metáfora, Metonímia)", ['metáfora', 'metonímia', 'figura de linguagem']),
    ("Teste 011: Figuras de Linguagem (Ironia, Antítese, Paradoxo)", ['ironia', 'antítese', 'paradoxo', 'eufemismo'])
]

for title, kws in topics:
    res = find_best(kws)
    print("=" * 60)
    print(f"{title} -> Encontradas: {len(res)}")
    if res:
        best = res[0]
        print(f"Escolhido: ID={best['id']} | {best['banca']} - {best['orgao']} - {best['cargo']} - {best['ano']}")
        print(f"Enunciado: {best['enunciado'][:200]}...")
        print(f"Gabarito: {best['gabarito_oficial']}")
