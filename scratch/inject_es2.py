# -*- coding: utf-8 -*-
import json
import re

TARGET_FILE = 'fontes_de_estudo/conhecimentos_especificos_b02_ti/04_engenharia_de_software/02_requisitos_historias_de_usuario_uml_e_bpmn.md'
DB_FILE = 'banco_questoes_extraidas.json'

with open(DB_FILE, 'r', encoding='utf-8') as f:
    db = json.load(f)

q_uml_class = None
for q in db['questoes']:
    if 'Observe o seguinte Diagrama de Classes UML 2.5.1' in q['enunciado'] and len(q.get('alternativas', {})) == 5:
        q_uml_class = q
        break

questoes_dict = {q['id']: q for q in db['questoes']}

replacements = [
    {
        "test_num": "012",
        "qid": "TRT23-2016-FCC-Q39",
        "header": "**(FCC – TRT-23 – Analista Judiciário (TI) – 2016)**",
        "comments": {
            "A": "Incorreta. O item I refere-se ao atributo de 'completude' da especificação, e não à rastreabilidade.",
            "B": "Incorreta. A ausência de conflitos conceituais caracteriza a 'consistência', e não a verificabilidade.",
            "C": "Incorreta. As definições conceituais dos itens foram trocadas entre si.",
            "D": "Correta. Uma Especificação de Requisitos é Completa (I) quando reflete todas as decisões e não deixa cláusulas em aberto (TBD); é Consistente (II) quando nenhuma exigência entra em conflito lógico com outra; e é Não-ambígua (III) quando cada requisito admite apenas uma única interpretação sem duplicidade semântica.",
            "E": "Incorreta. O item III define a não-ambiguidade, e não a modificabilidade."
        }
    },
    {
        "test_num": "013",
        "qid": "TRT14-2016-FCC-Q39",
        "header": "**(FCC – TRT-14 – Analista Judiciário (TI) – 2016)**",
        "comments": {
            "A": "Incorreta. O dicionário de dados documenta a estrutura dos elementos de dados, não a origem dos requisitos.",
            "B": "Incorreta. O plano de gerenciamento de escopo define os processos gerais de escopo do projeto.",
            "C": "Incorreta. O backlog do produto é a lista priorizada de funcionalidades, não o artefato formal de mapeamento de dependências cruzadas.",
            "D": "Incorreta. A especificação técnica de casos de uso foca na interação ator-sistema.",
            "E": "Correta. A Matriz de Rastreabilidade de Requisitos (Requirements Traceability Matrix) é a tabela ou instrumento formal que vincula os requisitos às suas fontes de origem, objetivos de negócio, artefatos de arquitetura, código e casos de teste, garantindo o acompanhamento de ponta a ponta ao longo do ciclo de vida."
        }
    },
    {
        "test_num": "015",
        "qid": "TRT1-2014-FCC-Q34",
        "header": "**(FCC – TRT-1 – Analista Judiciário (TI) – 2014)**",
        "comments": {
            "A": "Correta. Em um Diagrama de Casos de Uso segundo a UML, atores representam papéis que entidades externas (usuários humanos, sistemas externos ou hardware) desempenham ao interagir diretamente com os casos de uso do sistema.",
            "B": "Incorreta. Atores não são elementos internos do software nem classes de controle.",
            "C": "Incorreta. O relacionamento de inclusão (<<include>>) indica dependência obrigatória e incondicional, e não comportamento opcional.",
            "D": "Incorreta. O relacionamento de extensão (<<extend>>) é que insere comportamento sob condições específicas e pontos de extensão definidos.",
            "E": "Incorreta. Casos de uso descrevem o comportamento funcional do sistema a partir da perspectiva do usuário, não fluxos de código procedural interno."
        }
    },
    {
        "test_num": "016",
        "q_obj": q_uml_class,
        "header": "**(FGV – TJ-AP – Analista Judiciário (TI) – 2023)**",
        "comments": {
            "A": "Correta. No Diagrama de Classes da UML, quando um relacionamento possui propriedades ou atributos próprios (como 'Gratificação' na vinculação entre Professor e Turma/Projeto), esse elemento é modelado como uma Classe de Associação (Association Class), ligada à linha de associação por meio de uma linha tracejada.",
            "B": "Incorreta. Não se trata de uma classe abstrata comum, pois depende da existência da associação primária entre duas classes.",
            "C": "Incorreta. A interface apenas especifica assinaturas de operações sem manter atributos de instância associativos.",
            "D": "Incorreta. Não é um estereótipo nem componente físico de implementação.",
            "E": "Incorreta. Pacotes na UML organizam logicamente elementos do modelo, não possuindo atributos ou relacionamentos diretos desse tipo."
        }
    },
    {
        "test_num": "017",
        "qid": "TRT9-2015-FCC-Q32",
        "header": "**(FCC – TRT-9 – Analista Judiciário (TI) – 2015)**",
        "comments": {
            "A": "Incorreta. O Diagrama de Sequência é comportamental/interativo, e não estrutural.",
            "B": "Correta. Na taxonomia oficial da UML, os modelos estruturais representam os elementos estáticos do sistema e seus relacionamentos (ex: Diagramas de Classes, Objetos, Componentes, Implantação e Pacotes), enquanto os modelos comportamentais retratam a dinâmica e o fluxo temporal das interações (ex: Diagramas de Atividades, Casos de Uso, Máquina de Estados, Sequência e Comunicação).",
            "C": "Incorreta. O Diagrama de Casos de Uso é classificado como comportamental.",
            "D": "Incorreta. Diagramas de Atividades mostram o fluxo procedimental dinâmico, sendo comportamentais.",
            "E": "Incorreta. O Diagrama de Máquina de Estados retrata a transição dinâmica de estados em resposta a eventos, integrando o grupo comportamental."
        }
    },
    {
        "test_num": "018",
        "qid": "TRT23-2016-FCC-Q35",
        "header": "**(FCC – TRT-23 – Analista Judiciário (TI) – 2016)**",
        "comments": {
            "A": "Correta. A UML 2.0 define um conjunto de 13 diagramas formais organizados nas categorias estrutural e comportamental, permitindo expressar tanto a arquitetura estática quanto o comportamento em tempo de execução dos componentes e processos do sistema.",
            "B": "Incorreta. A UML não prescreve metodologia de desenvolvimento específica nem obriga o uso de processos proprietários.",
            "C": "Incorreta. Não há obrigatoriedade de construir todos os diagramas em todos os projetos; a modelagem deve ser seletiva e aderente às necessidades arquiteturais.",
            "D": "Incorreta. O Diagrama de Classes não substitui a modelagem comportamental em tempo de execução.",
            "E": "Incorreta. A notação da UML 2.0 suporta perfeitamente sistemas concorrentes, assíncronos e distribuídos."
        }
    },
    {
        "test_num": "019",
        "qid": "TRT13-2014-FCC-Q33",
        "header": "**(FCC – TRT-13 – Analista Judiciário (TI) – 2014)**",
        "comments": {
            "A": "Incorreta. O Diagrama de Sequência enfatiza a troca de mensagens ordenada no tempo entre objetos, não o particionamento de processos paralelos em raias com bifurcações.",
            "B": "Correta. O Diagrama de Atividades da UML é o diagrama ideal para modelar fluxos procedimentais, processos de negócio e algoritmos complexos, oferecendo suporte nativo a fluxos paralelos e sincronização (barras de fork e join), pontos de decisão (losangos) e raias de partição (swimlanes) que explicitam os responsáveis por cada atividade.",
            "C": "Incorreta. O Diagrama de Comunicação foca na organização estrutural dos objetos que colaboram na troca de mensagens.",
            "D": "Incorreta. O Diagrama de Casos de Uso foca na interação de fronteira externa sem detalhar o fluxo sequencial e concorrente interno do negócio.",
            "E": "Incorreta. O Diagrama de Componentes modela a arquitetura física e de módulos executáveis do software."
        }
    },
    {
        "test_num": "020",
        "qid": "TRT6-2012-FCC-Q35",
        "header": "**(FCC – TRT-6 – Analista Judiciário (TI) – 2012)**",
        "comments": {
            "A": "Incorreta. A associação simples entre as classes não descreve a hierarquia de herança com sobreposição de métodos.",
            "B": "Incorreta. A seta de ponta aberta tracejada indica dependência temporal ou realização de interface, não agregação.",
            "C": "Incorreta. A composição exige diamante preenchido no lado do todo, vinculando o ciclo de vida da parte ao todo.",
            "D": "Incorreta. A representação de generalização/herança exige triângulo fechado apontando para a superclasse.",
            "E": "Correta. A representação gráfica proposta no diagrama expressa de modo válido as relações fundamentais entre os elementos da UML, atendendo à semântica das notações de associação e visibilidade entre classes."
        }
    }
]

with open(TARGET_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

for item in replacements:
    t_num = item["test_num"]
    q_data = item.get("q_obj") or questoes_dict[item["qid"]]
    
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
    print(f"[OK] Injetado Teste {t_num} <- {q_data['id']} ({item['header']})")

with open(TARGET_FILE, 'w', encoding='utf-8') as f:
    f.write(content)

with open(DB_FILE, 'w', encoding='utf-8') as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print("\nProcessamento de 02_requisitos_historias_de_usuario_uml_e_bpmn.md concluído com sucesso!")

