import os
import re

file_path = "fontes_de_estudo/conhecimentos_especificos_b02_ti/12_governanca_de_ti/01_fundamentos_governanca_cobit_2019_e_iso_38500.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

q06 = """
---

### Questão 06 (FGV - TJ-MT - Analista Judiciário - Tecnologia da Informação - Adaptada)
**Enunciado:** A governança de TI é fundamental para alinhar os recursos e investimentos de tecnologia aos objetivos estratégicos organizacionais, assegurando a geração de valor público e a mitigação de riscos. A respeito das diferenças estruturais e operacionais entre governança e gestão de tecnologia da informação, assinale a alternativa correta:  

* **A)** A governança de TI concentra-se precipuamente na execução de atividades operacionais rotineiras, como configuração de switches de rede, homologação de código e atendimento diário de chamados de suporte de primeiro nível.
* **B)** A governança de TI é responsável por avaliar as necessidades estratégicas, direcionar as prioridades institucionais por meio de políticas e monitorar o desempenho e a conformidade, cabendo à gestão planejar, construir, executar e monitorar as atividades técnicas em consonância com as diretrizes estabelecidas.
* **C)** A gestão de TI possui horizonte temporal plurianual e é exercida com exclusividade pelos membros do Plenário e da alta administração, não se subordinando às diretrizes dos comitês estratégicos institucionais.
* **D)** A governança e a gestão de tecnologia constituem funções idênticas e intercambiáveis, de modo que os frameworks internacionais (como COBIT 2019 e ISO/IEC 38500) não estabelecem segregação de papéis ou responsabilidades entre os dois domínios.
* **E)** A responsabilidade final pela governança corporativa de TI deve ser compulsoriamente transferida e delegada às empresas contratadas que fornecem infraestrutura de data center ou sustentação de sistemas.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Configuração de ativos, codificação e atendimento de chamados operacionais de suporte são atribuições típicas de gestão de serviços de TI (nível operacional/tático), e não de governança.
> - **B)** **Correta.** A governança define o direcionamento estratégico segundo o modelo EDM (Avaliar, Dirigir e Monitorar), enquanto a gestão implementa e executa planos diários segundo o ciclo PBRM (Planejar, Construir, Executar e Monitorar).
> - **C)** Incorreta. A gestão foca no curto e médio prazo (sprints, rotinas operacionais). Quem possui visão de longo prazo e é exercida pela alta administração é a governança corporativa.
> - **D)** Incorreta. Há estrita segregação de funções (*separation of duties*). COBIT 2019 e ISO/IEC 38500 enfatizam que governança e gestão possuem propósitos, estruturas, responsabilidades e horizontes temporais distintos.
> - **E)** Incorreta. Pelo princípio da Responsabilidade, a prestação de contas (*accountability*) da governança é indelegável e não pode ser transferida para fornecedores ou prestadores externos.
> 
> **Gabarito: B**
"""

q07 = """
---

### Questão 07 (FCC - Tribunal de Contas - Auditor de TI - Adaptada)
**Enunciado:** A norma ABNT NBR ISO/IEC 38500:2024 define que a governança de Tecnologia da Informação pela alta administração é exercida por meio de um ciclo contínuo de três tarefas fundamentais (modelo EDM). Acerca desse modelo e dos papéis desempenhados pelo órgão de governança, assinale a alternativa correta:  

* **A)** Na tarefa de Dirigir (*Direct*), o órgão de governança assume diretamente a programação de scripts e o deploy contínuo de aplicações em ambientes de produção.
* **B)** Na tarefa de Avaliar (*Evaluate*), o órgão de governança examina e julga o uso presente e futuro da TI, considerando as estratégias institucionais, propostas de projetos e demandas das partes interessadas (*stakeholders*).
* **C)** O modelo EDM determina que a tarefa de Monitorar (*Monitor*) é dispensável caso a organização possua certificação ISO 9001 e auditoria interna constituída.
* **D)** A governança corporativa de TI conforme a ISO/IEC 38500 limita-se a organizações privadas com fins lucrativos, sendo vedada sua aplicação em tribunais de contas ou autarquias públicas.
* **E)** A tarefa de Dirigir (*Direct*) consiste exclusivamente na realização de auditorias fiscais pós-fato, sem competência para emitir políticas ou planos de investimento.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O papel de *Direct* consiste em definir políticas institucionais, prioridades e direcionamentos estratégicos, jamais na programação direta ou intervenção operacional diária de TI.
> - **B)** **Correta.** A avaliação (*Evaluate*) examina continuamente as circunstâncias presentes e futuras, considerando demandas dos stakeholders, tendências tecnológicas, requisitos legais e restrições financeiras.
> - **C)** Incorreta. O monitoramento contínuo de conformidade e desempenho é tarefa indispensável e mandatória da governança.
> - **D)** Incorreta. A norma ABNT NBR ISO/IEC 38500 aplica-se universalmente a qualquer organização pública ou privada, independente de porte ou finalidade lucrativa.
> - **E)** Incorreta. Dirigir é atribuir responsabilidades, definir estratégias e planos de TI de forma proativa.
> 
> **Gabarito: B**
"""

q08 = """
---

### Questão 08 (FGV - TRT-13 - Analista Judiciário - TI - Adaptada)
**Enunciado:** O COBIT 2019 estabelece que um sistema de governança requer fatores e recursos de diferentes naturezas trabalhando em conjunto, estruturados em 7 categorias de Componentes. A respeito desses componentes, assinale a alternativa correta:  

* **A)** O componente 'Processos' é o único obrigatório no COBIT 2019, sendo os demais 6 componentes considerados elementos puramente cosméticos e facultativos pela ISACA.
* **B)** As 'Estruturas Organizacionais' correspondem às entidades e comitês formais tomadores de decisão na organização, constituindo um dos 7 componentes do sistema de governança.
* **C)** O COBIT 2019 extinguiu o componente 'Pessoas, Habilidades e Competências', preconizando a automatização irrestrita de todas as práticas por inteligência artificial autônoma.
* **D)** O componente 'Cultura, Ética e Comportamento' aplica-se apenas a empresas privadas de capital aberto, não tendo relevância em órgãos públicos de controle externo.
* **E)** As ferramentas de software corporativo e data centers integram o componente de 'Estruturas Organizacionais' e não de 'Serviços, Infraestrutura e Aplicações'.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Todos os 7 componentes são essenciais e interdependentes para sustentar a eficácia do sistema de governança.
> - **B)** **Correta.** Estruturas organizacionais são os órgãos decisórios da governança e gestão (como o Plenário, comitês executivos de TI e a diretoria de tecnologia).
> - **C)** Incorreta. O capital humano (*People, Skills and Competencies*) continua sendo componente central do framework.
> - **D)** Incorreta. Cultura e ética corporativa são fundamentais em qualquer organização, sobretudo em tribunais de controle público.
> - **E)** Incorreta. Softwares e data centers integram a categoria 'Serviços, Infraestrutura e Aplicações'.
> 
> **Gabarito: B**
"""

q09 = """
---

### Questão 09 (FGV - TJ-RR - Analista Judiciário - Governança e Gestão de TI - Adaptada)
**Enunciado:** No COBIT 2019, o sistema de governança deve ser moldado sob medida para cada organização, recusando a premissa de 'tamanho único' (*one size fits all*). Para essa personalização e adaptação (*tailoring*), o framework utiliza os Fatores de Design (*Design Factors*). Sobre os Fatores de Design e as Áreas de Foco no COBIT 2019, assinale a alternativa correta:  

* **A)** Os 11 Fatores de Design incluem aspectos como Estratégia corporativa, Perfil de risco, Cenário de ameaças, Requisitos de conformidade e Modelo de fornecimento de TI.
* **B)** As Áreas de Foco são rigidamente limitadas a exatamente 5 domínios fixos e imutáveis, sendo vedada pela ISACA a publicação de novos guias de foco temático.
* **C)** O Fator de Design 'Papel da TI' reconhece apenas a TI como área de apoio secundário, proibindo a classificação de TI como motor estratégico do negócio.
* **D)** Os Fatores de Design são aplicados exclusivamente após a conclusão integral de todos os 40 processos de gestão, atuando como ferramentas de auditoria punitiva.
* **E)** O tamanho da organização (*Enterprise Size*) não é considerado fator de design pelo COBIT 2019, aplicando-se exatamente o mesmo modelo e volume documental a qualquer porte institucional.

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Os 11 fatores de design englobam estratégia institucional, objetivos, perfil de risco, problemas de I&T, cenário de ameaças, requisitos de conformidade, papel da TI, modelo de fornecimento, métodos de implementação, estratégia de adoção tecnológica e tamanho da organização.
> - **B)** Incorreta. Áreas de Foco podem ser ilimitadas e abertas, expandidas conforme o surgimento de novas demandas tecnológicas (ex.: Segurança, DevOps, Nuvem).
> - **C)** Incorreta. O papel da TI pode variar entre suporte, fábrica, transição e estratégico.
> - **D)** Incorreta. Fatores de design são utilizados no início, na concepção do sistema de governança (*design guide*), para selecionar e priorizar objetivos.
> - **E)** Incorreta. Tamanho da organização é expressamente o 11º Fator de Design.
> 
> **Gabarito: A**
"""

q10 = """
---

### Questão 10 (FCC - TRT-14 - Analista Judiciário - Tecnologia da Informação - Adaptada)
**Enunciado:** No modelo de Gestão de Desempenho do COBIT 2019 (CPM), para determinar o nível de capacidade de um processo, avalia-se o grau de alcance das práticas e atividades de governança e gestão por meio de uma escala percentual padrão dividida em quatro níveis (N, P, L e F). Assinale a alternativa que descreve corretamente essa escala:  

* **A)** Uma atividade com evidência de alcance entre maior que 15% e 50% é classificada como Parcialmente Atingida (*Partially Achieved* - P).
* **B)** Uma atividade com evidência de alcance de 0% a 15% é considerada Praticamente Atingida (*Largely Achieved* - L).
* **C)** Uma atividade é considerada Totalmente Atingida (*Fully Achieved* - F) apenas quando atinge 100% de conformidade formal sem qualquer margem de tolerância.
* **D)** A classificação 'Não Atingido' (*Not Achieved* - N) exige demonstração de fraude ou negligência dolosa comprovada por auditoria externa.
* **E)** A escala N-P-L-F foi descontinuada no COBIT 2019 e substituída exclusivamente pelo modelo binário de Sucesso ou Falha.

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme a régua oficial do CPM/CMMI: N (Não Atingido: 0% a 15%), P (Parcialmente Atingido: > 15% a 50%), L (Praticamente Atingido: > 50% a 85%) e F (Totalmente Atingido: > 85% a 100%).
> - **B)** Incorreta. De 0% a 15% a classificação é Não Atingido (*Not Achieved* - N). Praticamente Atingido (L) situa-se na faixa de > 50% a 85%.
> - **C)** Incorreta. Totalmente Atingido (F) abrange a faixa superior de > 85% até 100%.
> - **D)** Incorreta. A classificação N reflete ausência ou nível incipiente de evidências de execução (0% a 15%), sem relação com fraude ou dolo.
> - **E)** Incorreta. A escala N-P-L-F permanece a métrica de avaliação contínua de atividades e práticas do COBIT 2019.
> 
> **Gabarito: A**
"""

# Insertion 1: After 1.2
p1 = "A governança assegura a integração bidirecional contínua entre a estratégia institucional e a estratégia de TI, evitando que a área técnica formule objetivos isolados ou desconectados das reais prioridades de fiscalização e auditoria do Tribunal.\n"
assert p1 in content, "Pattern 1 not found"
content = content.replace(p1, p1 + q06 + "\n")

# Insertion 2: After 2.1 sequence diagram
p2 = "    GOV->>GOV: Monitorar (Monitor) indicadores e conformidade\n    GOV-->>SH: Prestação de contas e geração de valor público\n```\n"
assert p2 in content, "Pattern 2 not found"
content = content.replace(p2, p2 + q07 + "\n")

# Insertion 3: After 3.2
p3 = "7. **Serviços, Infraestrutura e Aplicações:** A infraestrutura tecnológica, redes, data centers, ferramentas de software e aplicações corporativas.\n"
assert p3 in content, "Pattern 3 not found"
content = content.replace(p3, p3 + q08 + "\n")

# Insertion 4: After 3.3
p4 = "As áreas de foco podem ser ilimitadas e são expandidas continuamente pela comunidade.\n"
assert p4 in content, "Pattern 4 not found"
content = content.replace(p4, p4 + q09 + "\n")

# Insertion 5: After 3.6 Escala de Avaliacao
p5 = "- **F (Totalmente Atingido / *Fully Achieved*):** Evidência de alcance de $> 85\%$ a $100\%$.\n"
assert p5 in content, "Pattern 5 not found"
content = content.replace(p5, p5 + q10 + "\n")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("File 12_01 successfully updated!")
