import json
from collections import defaultdict

data = json.load(open('banco_questoes_extraidas.json', 'r', encoding='utf-8'))
questoes = [q for q in data['questoes'] if q.get('status_integracao') == 'pendente']

keywords = {
    'compreensao': ['compreensão', 'interpretação', 'depreende-se', 'infere-se', 'conclui-se', 'de acordo com o texto'],
    'generos': ['gênero textual', 'editorial', 'crônica', 'ensaio', 'artigo de opinião'],
    'tipologia': ['narrativo', 'dissertativo', 'descritivo', 'injuntivo', 'tipo textual', 'tipologia'],
    'argumentacao': ['argumentativo', 'tese', 'pressuposto', 'subentendido', 'argumento'],
    'denotacao_conotacao': ['sentido figurado', 'conotativo', 'denotativo', 'conotação', 'denotação'],
    'discurso': ['discurso direto', 'discurso indireto', 'transposição'],
    'intertextualidade': ['intertextualidade', 'paráfrase', 'paródia', 'citação'],
    'figuras': ['figura de linguagem', 'metáfora', 'metonímia', 'ironia', 'antítese', 'eufemismo', 'paradoxo']
}

for k, kw_list in keywords.items():
    matches = []
    for q in questoes:
        text = (q['enunciado'] + ' ' + ' '.join(q['alternativas'].values())).lower()
        if any(w in text for w in kw_list):
            matches.append(q)
    fcc_cnt = sum(1 for m in matches if m['banca'] == 'FCC')
    fgv_cnt = sum(1 for m in matches if m['banca'] == 'FGV')
    print(f"{k}: {len(matches)} encontradas (FCC: {fcc_cnt}, FGV: {fgv_cnt})")

