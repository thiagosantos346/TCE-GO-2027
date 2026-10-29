# -*- coding: utf-8 -*-
import json
import re

TARGET_FILE = 'fontes_de_estudo/conhecimentos_especificos_b02_ti/08_banco_de_dados/01_modelagem_de_dados_mer_e_normalizacao.md'
DB_FILE = 'banco_questoes_extraidas.json'

with open(DB_FILE, 'r', encoding='utf-8') as f:
    db = json.load(f)

questoes_dict = {q['id']: q for q in db['questoes']}

# Mapeamento para o arquivo 01 de Banco de Dados
# Teste 236 já é real (preservar)
replacements = [
    {
        "test_num": "234",
        "qid": "TRT6-2012-FCC-Q43",
        "header": "**(FCC – TRT-6 – Analista Judiciário (TI) – 2012)**",
        "comments": {
            "A": "Correta. No modelo entidade-relacionamento (MER), entidades fortes possuem chave primária própria e existência independente, enquanto entidades fracas dependem existencialmente de uma entidade proprietária para sua identificação.",
            "B": "Incorreta. Atributos multivalorados não podem ser representados diretamente como chave estrangeira atômica sem normalização.",
            "C": "Incorreta. A cardinalidade mínima (0 ou 1) indica a participação opcional ou obrigatória da entidade no relacionamento, e não a cardinalidade máxima.",
            "D": "Incorreta. Um relacionamento não pode existir isoladamente sem a vinculação das entidades participantes.",
            "E": "Incorreta. O modelo lógico relacional não admite atributos compostos sem prévia decomposição em atributos simples."
        }
    },
    {
        "test_num": "235",
        "qid": "TRT23-2016-FCC-Q29",
        "header": "**(FCC – TRT-23 – Analista Judiciário (TI) – 2016)**",
        "comments": {
            "A": "Incorreta. A generalização/especialização total exige que toda instância da superclasse pertença obrigatoriamente a uma subclasse.",
            "B": "Incorreta. A modelagem lógica não dispensa a definição de chaves primárias e estrangeiras.",
            "C": "Correta. Na perspectiva lógica do modelo entidade-relacionamento, atributos derivados ou calculados não devem ser persistidos fisicamente na tabela para evitar redundância e inconsistência de dados, sendo obtidos por consultas ou visões dinâmicas.",
            "D": "Incorreta. Relacionamentos recursivos (auto-relacionamentos) são perfeitamente admitidos na modelagem lógica.",
            "E": "Incorreta. Entidades fracas não possuem identificador primário próprio sem a composição com a chave da entidade dominante."
        }
    },
    {
        "test_num": "237",
        "qid": "TRT1-2014-FCC-Q31",
        "header": "**(FCC – TRT-1 – Analista Judiciário (TI) – 2014)**",
        "comments": {
            "A": "Incorreta. O relacionamento muitos para muitos não exige que a associação seja compulsória a 'mais de uma' em todos os casos.",
            "B": "Correta. A cardinalidade muitos para muitos (N:M) entre dois conjuntos de entidades A e B define que uma entidade de A pode estar associada a várias (zero, uma ou muitas) entidades de B, e reciprocamente cada entidade de B pode estar associada a várias entidades de A.",
            "C": "Incorreta. O número de atributos de cada entidade é completamente independente da cardinalidade do relacionamento.",
            "D": "Incorreta. A cardinalidade não determina a nulidade de atributos.",
            "E": "Incorreta. A definição apresentada na alternativa corresponde a um relacionamento de um para muitos (1:N), e não muitos para muitos (N:M)."
        }
    },
    {
        "test_num": "238",
        "qid": "TJBA-2015-FGV-Q40",
        "header": "**(FGV – TJ-BA – Analista Judiciário (TI) – 2015)**",
        "comments": {
            "A": "Incorreta. A relação atinge a 1ª Forma Normal, mas viola formas normais superiores pelas dependências funcionais parciais.",
            "B": "Incorreta. Há dependências funcionais transitivas que impedem o alcance da 3ª Forma Normal.",
            "C": "Incorreta. O esquema viola os critérios da Forma Normal de Boyce-Codd (BCNF).",
            "D": "Correta. A análise das dependências funcionais determina que a chave candidata é composta e que os atributos não-chave dependem totalmente dela, cumprindo os requisitos de integridade da normalização.",
            "E": "Incorreta. O conjunto de dependências não caracteriza a 4ª Forma Normal por envolver dependências multivaloradas não tratadas."
        }
    },
    {
        "test_num": "244",
        "qid": "TRT23-2016-FCC-Q34",
        "header": "**(FCC – TRT-23 – Analista Judiciário (TI) – 2016)**",
        "comments": {
            "A": "Incorreta. A tabela fato contém predominantemente chaves estrangeiras que apontam para as dimensões e medidas numéricas aditivas.",
            "B": "Incorreta. As dimensões no modelo Star Schema são mantidas desnormalizadas propositalmente para otimizar consultas.",
            "C": "Incorreta. A tabela fato não é menor em número de linhas que as tabelas de dimensão; ao contrário, possui volume muito superior.",
            "D": "Incorreta. O modelo Star Schema não normaliza as tabelas de dimensão (o modelo Snowflake é que realiza essa normalização).",
            "E": "Correta. No esquema estrela (Star Schema), os fatos representam eventos quantitativos do negócio com atributos numéricos (medidas) associados a um conjunto de chaves estrangeiras que referenciam as dimensões circundantes."
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
    formatted_enunciado = '\n\n'.join(lines) if any(l.startswith('I.') or l.startswith('II.') or l.startswith('(') for l in lines) else ' '.join(lines)
    
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

print("\nProcessamento de 01_modelagem_de_dados_mer_e_normalizacao.md concluído com sucesso!")

