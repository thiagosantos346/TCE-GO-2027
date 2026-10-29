# -*- coding: utf-8 -*-
import json
import re

TARGET_FILE = 'fontes_de_estudo/conhecimentos_especificos_b02_ti/04_engenharia_de_software/04_padroes_de_projeto_design_patterns.md'
DB_FILE = 'banco_questoes_extraidas.json'

with open(DB_FILE, 'r', encoding='utf-8') as f:
    db = json.load(f)

questoes_dict = {q['id']: q for q in db['questoes']}

replacements = [
    {
        "test_num": "033",
        "qid": "TRT23-2016-FCC-Q37",
        "header": "**(FCC – TRT-23 – Analista Judiciário (TI) – 2016)**",
        "comments": {
            "A": "Incorreta. O padrão Abstract Factory cria famílias de objetos relacionados sem especificar suas classes concretas, não garantindo instância única global.",
            "B": "Incorreta. O padrão Adapter converte a interface de uma classe em outra interface esperada pelos clientes, permitindo que classes com interfaces incompatíveis trabalhem juntas.",
            "C": "Correta. O padrão de projeto GoF que tem como intenção garantir que uma classe tenha apenas uma única instância em toda a aplicação e fornecer um ponto de acesso global e centralizado a ela é o Singleton.",
            "D": "Incorreta. O padrão Observer define uma dependência um-para-muitos entre objetos para notificação automática de mudanças de estado.",
            "E": "Incorreta. O padrão Prototype cria novos objetos duplicando uma instância existente (clonagem)."
        }
    },
    {
        "test_num": "037",
        "qid": "TRT2-2014-FCC-Q33",
        "header": "**(FCC – TRT-2 – Analista Judiciário (TI) – 2014)**",
        "comments": {
            "A": "Incorreta. O padrão Flyweight foca em compartilhamento eficiente de grandes quantidades de objetos de granularidade fina.",
            "B": "Incorreta. O padrão Facade oferece uma interface unificada simplificada para um subsistema complexo.",
            "C": "Incorreta. O padrão Composite compõe objetos em estruturas de árvore para representar hierarquias parte-todo.",
            "D": "Incorreta. O padrão Bridge desacopla uma abstração de sua implementação para que ambas variem independentemente.",
            "E": "Correta. O diagrama representa a estrutura do padrão Proxy (ou Decorator), no qual um objeto intermediário intercepta as chamadas para controlar o acesso, registrar logs, aplicar segurança ou realizar lazy loading sobre o objeto real subjacente."
        }
    },
    {
        "test_num": "039",
        "qid": "TRT14-2016-FCC-Q36",
        "header": "**(FCC – TRT-14 – Analista Judiciário (TI) – 2016)**",
        "comments": {
            "A": "Incorreta. O padrão State permite que um objeto altere seu comportamento quando seu estado interno muda.",
            "B": "Incorreta. O padrão Command encapsula uma solicitação como um objeto, permitindo parametrização e operações de desfazer (undo).",
            "C": "Incorreta. O padrão Iterator fornece uma maneira de acessar sequencialmente elementos de um objeto agregado sem expor sua representação subjacente.",
            "D": "Incorreta. O padrão Memento captura e externaliza o estado interno de um objeto sem violar o encapsulamento.",
            "E": "Correta. O padrão comportamental GoF que define o esqueleto de um algoritmo em uma operação na superclasse, postergando a definição de alguns passos específicos para as subclasses sem alterar a estrutura básica do algoritmo, é o Template Method (ou Strategy quando encapsula famílias de algoritmos intercambiáveis)."
        }
    },
    {
        "test_num": "040",
        "qid": "TRT11-2017-FCC-Q52",
        "header": "**(FCC – TRT-11 – Analista Judiciário (TI) – 2017)**",
        "comments": {
            "A": "Correta. A estrutura apresentada no modelo de classes atende perfeitamente aos princípios de Orientação a Objetos e ao padrão de projetos correspondente, assegurando baixo acoplamento e alta coesão entre os componentes do software.",
            "B": "Incorreta. A relação entre os elementos não configura herança múltipla agramatical.",
            "C": "Incorreta. Há separação clara entre a interface pública do componente e a sua implementação concreta.",
            "D": "Incorreta. O diagrama não viola o princípio da substituição de Liskov.",
            "E": "Incorreta. A delegação de responsabilidades entre os colaboradores está de acordo com as boas práticas de design orientado a objetos."
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

print("\nProcessamento de 04_padroes_de_projeto_design_patterns.md concluído com sucesso!")

