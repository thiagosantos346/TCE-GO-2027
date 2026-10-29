# -*- coding: utf-8 -*-
import json
import re

TARGET_FILE = 'fontes_de_estudo/conhecimentos_especificos_b02_ti/04_engenharia_de_software/05_qualidade_testes_refatoracao_e_divida_tecnica.md'
DB_FILE = 'banco_questoes_extraidas.json'

with open(DB_FILE, 'r', encoding='utf-8') as f:
    db = json.load(f)

questoes_dict = {q['id']: q for q in db['questoes']}

replacements = [
    {
        "test_num": "043",
        "qid": "TRT1-2014-FCC-Q36",
        "header": "**(FCC – TRT-1 – Analista Judiciário (TI) – 2014)**",
        "comments": {
            "A": "Incorreta. A portabilidade refere-se à facilidade com que o software pode ser transferido de um ambiente computacional para outro.",
            "B": "Correta. Segundo as normas de qualidade de produto de software (ISO/IEC 9126 e ISO/IEC 25010 SQuaRE), a confiabilidade (reliability) avalia a capacidade do software de manter seu nível de desempenho sob condições estabelecidas durante um período determinado, abrangendo maturidade, tolerância a falhas e capacidade de recuperação.",
            "C": "Incorreta. A manutenibilidade mede o esforço necessário para modificar o software (corretiva, adaptativa ou evolutivamente).",
            "D": "Incorreta. A usabilidade diz respeito à facilidade de aprendizado e operação pelo usuário.",
            "E": "Incorreta. A eficiência avalia o tempo de resposta e o consumo adequado de recursos do sistema."
        }
    },
    {
        "test_num": "044",
        "qid": "TRT1-2014-FCC-Q37",
        "header": "**(FCC – TRT-1 – Analista Judiciário (TI) – 2014)**",
        "comments": {
            "A": "Incorreta. Testar a comunicação entre subsistemas e módulos integrados caracteriza os testes de integração.",
            "B": "Incorreta. Avaliar o sistema completo em conformidade com as regras de negócio finais é o objetivo do teste de aceitação.",
            "C": "Correta. O teste de unidade (ou unitário) consiste em testar a menor parte testável de uma aplicação de software (como funções, métodos, classes ou módulos isolados), verificando se o componente individual se comporta rigorosamente conforme o especificado, tipicamente isolando dependências externas com o uso de stubs e mocks.",
            "D": "Incorreta. Testar o comportamento sob alta carga de acessos concorrentes define os testes de estresse/desempenho.",
            "E": "Incorreta. A verificação do sistema contra ataques externos refere-se aos testes de segurança e vulnerabilidade."
        }
    },
    {
        "test_num": "045",
        "qid": "TRT14-2016-FCC-Q40",
        "header": "**(FCC – TRT-14 – Analista Judiciário (TI) – 2016)**",
        "comments": {
            "A": "Correta. No framework de testes JUnit para Java, o método asserção assertEquals(esperado, obtido) verifica se o valor retornado pelo método sob teste coincide exatamente com o valor esperado, provocando a falha do teste caso haja discrepância.",
            "B": "Incorreta. O método assertTrue avalia condições estritamente booleanas, e não igualdade de valores numéricos complexos.",
            "C": "Incorreta. A anotação @Test identifica os métodos executáveis de teste, não servindo como método de verificação de resultado.",
            "D": "Incorreta. O método fail() força explicitamente a reprovação do teste sem comparar resultados.",
            "E": "Incorreta. assertSame verifica a identidade de referência em memória (==), e não a igualdade de valores de objetos."
        }
    },
    {
        "test_num": "046",
        "qid": "TRT14-2016-FCC-Q41",
        "header": "**(FCC – TRT-14 – Analista Judiciário (TI) – 2016)**",
        "comments": {
            "A": "Incorreta. A espera estática rígida (Thread.sleep) é uma má prática que torna os testes lentos e instáveis.",
            "B": "Incorreta. O polling contínuo sem timeout pode gerar loops infinitos na suíte de testes automatizados.",
            "C": "Incorreta. A espera implícita global afeta todos os elementos indiscriminadamente, não tratando condições específicas de eventos assíncronos.",
            "D": "Correta. Na automação de testes funcionais (como no Selenium WebDriver), a Espera Explícita (Explicit Wait / WebDriverWait) configura o controle ideal para aguardar dinamicamente até que uma condição esperada (ExpectedCondition) específica se concretize antes de prosseguir com a interação, evitando quebras por assincronismo sem desperdício de tempo.",
            "E": "Incorreta. O tratamento genérico de exceções mascara defeitos reais na interface gráfica da aplicação."
        }
    },
    {
        "test_num": "047",
        "qid": "TRT-2024-FCC-Q57",
        "header": "**(FCC – TRT – Analista Judiciário (TI) – 2024)**",
        "comments": {
            "A": "Correta. Nas práticas modernas de DevOps e Integração Contínua (CI/CD), a execução automatizada de testes integrados e regressivos no pipeline de entrega assegura a detecção precoce de incompatibilidades entre microsserviços e bibliotecas antes da promoção de artefatos para o ambiente de produção.",
            "B": "Incorreta. O item II nega a utilidade dos testes de regressão automatizados, contrariando as premissas centrais do DevOps.",
            "C": "Incorreta. O isolamento manual de ambientes sem automação eleva o risco de falhas operacionais em produção.",
            "D": "Incorreta. O teste de fumaça (smoke test) não substitui os testes funcionais de cobertura completa.",
            "E": "Incorreta. A ausência de monitoramento pós-deploy contraria a cultura de observabilidade do DevOps."
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

print("\nProcessamento de 05_qualidade_testes_refatoracao_e_divida_tecnica.md concluído com sucesso!")

