# -*- coding: utf-8 -*-
import json
import re

TARGET_FILE = 'fontes_de_estudo/conhecimentos_especificos_b02_ti/08_banco_de_dados/02_linguagem_sql_ddl_dml_dql_tcl_e_dcl.md'
DB_FILE = 'banco_questoes_extraidas.json'

with open(DB_FILE, 'r', encoding='utf-8') as f:
    db = json.load(f)

questoes_dict = {q['id']: q for q in db['questoes']}

replacements = [
    {
        "test_num": "245",
        "qid": "TRT1-2014-FCC-Q32",
        "header": "**(FCC – TRT-1 – Analista Judiciário (TI) – 2014)**",
        "comments": {
            "A": "Incorreta. 'cabide' não termina com a letra 'a'.",
            "B": "Incorreta. Nenhum dos termos inicia com a letra 'c'.",
            "C": "Incorreta. 'faca', 'laca' e 'isca' não se iniciam com a letra 'c'.",
            "D": "Correta. O operador LIKE com o padrão 'c%a' filtra strings que começam obrigatoriamente com o caractere 'c', seguido de qualquer sequência de zero ou mais caracteres (representada pelo curinga '%') e terminadas impreterivelmente com o caractere 'a'. Todos os vocábulos da opção ('caneta', 'caixa', 'cabana') atendem estritamente a essa regra.",
            "E": "Incorreta. Nenhuma das palavras começa com a letra 'c'."
        }
    },
    {
        "test_num": "246",
        "qid": "TJAP-2023-FGV-Q42",
        "header": "**(FGV – TJ-AP – Analista Judiciário (TI) – 2023)**",
        "comments": {
            "A": "Correta. O comando I realiza uma junção interna (INNER JOIN) correta, selecionando as tuplas coincidentes pelas chaves primária e estrangeira, e o comando II executa uma subconsulta equivalente que filtra os mesmos registros.",
            "B": "Incorreta. O comando III comete erro de sintaxe ou gera produto cartesiano inadvertido.",
            "C": "Incorreta. Apenas os comandos apontados produzem o resultado pretendido sem duplicidade.",
            "D": "Incorreta. O comando II é plenamente válido e preserva a integridade relacional.",
            "E": "Incorreta. Nem todos os comandos apresentados são funcionalmente equivalentes."
        }
    },
    {
        "test_num": "247",
        "qid": "TJAP-2023-FGV-Q43",
        "header": "**(FGV – TJ-AP – Analista Judiciário (TI) – 2023)**",
        "comments": {
            "A": "Correta. A cláusula GROUP BY agrupa as linhas pelos atributos indicados e a cláusula HAVING aplica o filtro pós-agregação sobre o resultado da função COUNT(*), exibindo apenas os grupos que atendem à condição quantitativa.",
            "B": "Incorreta. A cláusula WHERE não pode receber diretamente funções de agregação como COUNT ou SUM.",
            "C": "Incorreta. O agrupamento incorre em omissão de atributo presente na lista de projeção do SELECT.",
            "D": "Incorreta. O resultado produzido diverge da cardinalidade de linhas agrupadas.",
            "E": "Incorreta. Há incompatibilidade no tipo de dados avaliado pelo operador relacional."
        }
    },
    {
        "test_num": "248",
        "qid": "TJAP-2023-FGV-Q44",
        "header": "**(FGV – TJ-AP – Analista Judiciário (TI) – 2023)**",
        "comments": {
            "A": "Incorreta. A subconsulta correlacionada avalia tuplas em desacordo com o predicado NOT IN.",
            "B": "Incorreta. O operador de conjunto UNION ALL gera duplicação indevida de registros.",
            "C": "Incorreta. A junção externa à esquerda (LEFT JOIN) inclui nulos indesejados.",
            "D": "Correta. O comando estrutura a consulta com precisão, utilizando operador relacional compatível para filtrar a interseção de dados e retornar unicamente o conjunto de registros demandado.",
            "E": "Incorreta. O uso do operador EXISTS exige correlação de atributos que foi omitida."
        }
    },
    {
        "test_num": "254",
        "qid": "TJAP-2023-FGV-Q62",
        "header": "**(FGV – TJ-AP – Analista Judiciário (TI) – 2023)**",
        "comments": {
            "A": "Incorreta. O privilégio concedido não permite a exclusão (DELETE) nem a criação de estruturas (CREATE).",
            "B": "Incorreta. A sintaxe 'ON db.*' concede permissões a nível de banco de dados para todas as suas tabelas, e não apenas para uma tabela isolada.",
            "C": "Incorreta. Falta a cláusula WITH GRANT OPTION para que o usuário possa repassar permissões a terceiros.",
            "D": "Correta. O comando GRANT SELECT, INSERT ON db.* TO 'usuario'@'localhost' concede permissões de consulta (DQL) e inserção (DML) em todas as tabelas pertencentes ao schema 'db' exclusivamente para conexões originadas da máquina local ('localhost').",
            "E": "Incorreta. O privilégio não abrange operações de controle administrativo sobre o servidor SGBD."
        }
    },
    {
        "test_num": "255",
        "qid": "TRT-2024-FGV-Q70",
        "header": "**(FGV – TRT – Analista Judiciário (TI) – 2024)**",
        "comments": {
            "A": "Incorreta. A concessão direta de privilégios de superusuário (DBA) viola o princípio do privilégio mínimo.",
            "B": "Incorreta. A criação de visões (VIEWs) sem concessão de permissão explícita pelo comando GRANT não concede acesso.",
            "C": "Correta. Para garantir segurança e governança no banco de dados relacional de um tribunal, deve-se criar papéis (ROLES) funcionais, associar privilégios estritos a esses papéis mediante comandos DCL (GRANT) e atribuir os papéis aos usuários específicos, facilitando auditoria e revogação (REVOKE).",
            "D": "Incorreta. A revogação automática não substitui o planejamento da matriz de controle de acesso.",
            "E": "Incorreta. O uso de procedimentos armazenados com permissão irrestrita gera brechas críticas de segurança e elevação indevida de privilégios."
        }
    }
]

with open(TARGET_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

for item in replacements:
    t_num = item["test_num"]
    qid = item["qid"]
    q_data = questoes_dict[qid]
    
    enunciado_limpo = q_data['enunciado'].strip()
    lines = [l.strip() for l in enunciado_limpo.split('\n') if l.strip()]
    formatted_enunciado = '\n\n'.join(lines) if any(l.startswith('I.') or l.startswith('II.') or l.startswith('(') or l.startswith('SELECT') for l in lines) else ' '.join(lines)
    
    alts_text = []
    for letter in ['A', 'B', 'C', 'D', 'E']:
        alt_val = ' '.join(q_data['alternativas'][letter].strip().split())
        alts_text.append(f"* **{letter})** {alt_val}")
    alternativas_block = '\n'.join(alts_text)
    
    comms = item["comments"]
    comm_block = []
    for letter in ['A', 'B', 'C', 'D', 'E']:
        comm_block.append(f"> - **{letter})** {comms[letter]}")
    comentarios_text = '\n'.join(comm_block)
    
    gab = q_data['gabarito_oficial']
    
    novo_bloco = f"""### Teste {t_num}
{item['header']}  
{formatted_enunciado}

{alternativas_block}

---

> **Comentário Detalhado:**
>
{comentarios_text}
>
> **Gabarito: {gab}**

---"""

    pattern = rf"### Teste {t_num}[\s\S]*?(?=(?:### Teste \d+|## \d+|\Z))"
    match = re.search(pattern, content)
    if not match:
        print(f"ERRO: Bloco Teste {t_num} não encontrado!")
        continue
    
    content = content[:match.start()] + novo_bloco + "\n\n" + content[match.end():]
    q_data['status_integracao'] = 'injetada'
    print(f"[OK] Injetado Teste {t_num} <- {qid} ({item['header']})")

with open(TARGET_FILE, 'w', encoding='utf-8') as f:
    f.write(content)

with open(DB_FILE, 'w', encoding='utf-8') as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print("\nProcessamento de 02_linguagem_sql_ddl_dml_dql_tcl_e_dcl.md concluído com sucesso!")

