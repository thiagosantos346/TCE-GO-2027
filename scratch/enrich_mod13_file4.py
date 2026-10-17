import os

file_path = "fontes_de_estudo/conhecimentos_especificos_b02_ti/13_legislacao_aplicada_a_ti/04_lei_complementar_estadual_205_2025.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

q06 = """
---

### Questão 06 (FCC – Inédita – Padrão TCE-GO - Auditor Estadual de Controle Externo / TI)
**Enunciado:** A Lei Complementar Estadual nº 205, de 19 de maio de 2025, instituiu a Política Estadual de Inteligência Artificial no Estado de Goiás. A respeito dos objetivos centrais e do escopo regulatório estabelecido por esse diploma legal para a administração pública goiana, assinale a afirmativa correta:  

* **A)** A lei visa fomentar exclusivamente a substituição integral de todos os auditores fiscais e juízes por sistemas autônomos de tomada de decisão não auditáveis.
* **B)** A norma tem como escopo conciliar o fomento à inovação tecnológica, ao desenvolvimento socioeconômico e à governança digital com a salvaguarda inegociável de direitos fundamentais, transparência algorítmica e proteção de dados pessoais.
* **C)** A política estadual veda terminantemente que universidades e centros de pesquisa estaduais desenvolvam modelos de inteligência artificial em cooperação com o setor produtivo.
* **D)** A LC nº 205/2025 autoriza os órgãos públicos do Estado a utilizarem dados pessoais para fins discriminatórios sempre que houver potencial de aumento da arrecadação tributária.
* **E)** O escopo da lei restringe-se exclusivamente a empresas privadas do setor financeiro, não vinculando os órgãos da administração pública direta ou indireta de Goiás.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A lei expressamente estabelece a centralidade na pessoa humana (*Human-Centric AI*) e a exigência de supervisão humana, repudiando a substituição irresponsável de agentes públicos por algoritmos opacos.
> - **B)** **Correta.** O objetivo estruturante da LC nº 205/2025 é o equilíbrio estratégico: impulsionar a inovação digital, a competitividade e a eficiência governamental, ao mesmo tempo em que institui barreiras éticas e legais rígidas contra vieses discriminatórios, abusos e violações à privacidade.
> - **C)** Incorreta. A cooperação entre poder público, universidades, ICTs e setor privado (modelo da hélice tríplice) é um dos eixos mais incentivados pela política de inovação estadual.
> - **D)** Incorreta. A não discriminação e a equidade algorítmica são princípios cogentes e absolutos na legislação de IA goiana.
> - **E)** Incorreta. A norma vincula expressamente os órgãos e entidades da administração pública direta, autárquica e fundacional do Estado de Goiás.
> 
> **Gabarito: B**
"""

q07 = """
---

### Questão 07 (FCC – Inédita – Padrão TCE-GO - Analista de Sistemas / Ciência de Dados)
**Enunciado:** Um dos princípios mais relevantes da LC nº 205/2025 é a **Transparência Algorítmica e a Explicabilidade** (*Explainable AI - XAI*). Ao fiscalizar a utilização de modelos complexos de aprendizado de máquina (como redes neurais profundas e gradient boosting) empregados por secretarias de estado na concessão de benefícios assistenciais, o auditor do TCE-GO deve verificar se:  

* **A)** A Administração Pública esconde a documentação técnica sob segredo comercial irrestrito, impedindo o cidadão de conhecer os critérios da decisão.
* **B)** São adotadas metodologias e ferramentas técnicas de interpretabilidade e explicabilidade (como valores SHAP, LIME ou modelos substitutos interpretáveis) que permitam justificar de forma inteligível ao cidadão e aos órgãos de controle as variáveis determinantes do ato administrativo automatizado.
* **C)** O modelo foi construído utilizando parâmetros aleatórios que dispensam qualquer comprovação lógica ou estatística.
* **D)** A explicabilidade é tratada como opcional quando o custo de processamento computacional da inferência for superior a um centavo de real.
* **E)** Apenas especialistas com pós-doutorado em física quântica consigam compreender as razões da decisão estatal proferida.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A administração pública rege-se pelos princípios constitucionais da publicidade e motivação dos atos administrativos; o segredo comercial não pode ser invocado pelo Estado para blindar decisões públicas automatizadas.
> - **B)** **Correta.** A diretriz de explicabilidade algorítmica (*XAI*) exige que o poder público disponha de meios técnicos (como SHAP - *SHapley Additive exPlanations* e LIME - *Local Interpretable Model-agnostic Explanations*) para auditar e fundamentar as decisões, tornando transparentes os fatores e pesos que levaram o sistema ao resultado.
> - **C)** Incorreta. Atos administrativos baseados em algoritmos devem observar a motivação, legalidade e robustez metodológica.
> - **D)** Incorreta. A transparência algorítmica é um dever legal inderrogável imposto pela LC 205/2025 e pela Constituição.
> - **E)** Incorreta. A explicabilidade deve viabilizar a compreensão em linguagem acessível e clara tanto para os órgãos de controle quanto para os cidadãos impactados.
> 
> **Gabarito: B**
"""

q08 = """
---

### Questão 08 (FCC – Inédita – Padrão TCE-GO - Técnico de Controle Externo / TI)
**Enunciado:** O *Sandbox Estadual Permanente de Inteligência Artificial*, regulamentado pela LC nº 205/2025 de Goiás, foi concebido como um ambiente pioneiro no Brasil. A respeito das condições e salvaguardas mandatórias para que uma empresa ou consórcio participe desse ambiente experimental de inovação, assinale a afirmativa correta:  

* **A)** A admissão no sandbox dispensa a empresa de cumprir as regras da Lei Geral de Proteção de Dados Pessoais (LGPD).
* **B)** A participação no sandbox exige prévia aprovação em processo público de seleção e a apresentação de matriz de gerenciamento de riscos, garantida a preservação da responsabilidade civil por eventuais danos causados a terceiros.
* **C)** O sandbox permite testes clandestinos em dados sensíveis de pacientes sem qualquer controle ou monitoramento por parte dos órgãos estaduais competentes.
* **D)** Apenas empresas multinacionais com sede fora do Brasil têm autorização para submeter projetos ao sandbox goiano.
* **E)** As autorizações concedidas no sandbox têm prazo de vigência perpétuo e irrevogável pelo Estado.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A conformidade com a LGPD e os direitos fundamentais constitui requisito inegociável e mandatório durante toda a estada no sandbox.
> - **B)** **Correta.** Conforme a LC nº 205/2025, o ingresso no sandbox ocorre mediante edital de chamada pública e exige plano detalhado de mitigação e gestão de riscos. A flexibilização regulatória temporária não isenta os participantes da responsabilidade civil perante terceiros.
> - **C)** Incorreta. Testes clandestinos são ilícitos; todo o ciclo é monitorado e supervisionado pelas autoridades estaduais designadas.
> - **D)** Incorreta. O programa é aberto a startups locais, empresas de base tecnológica, ICTs e universidades, estimulando fortemente o ecossistema regional goiano.
> - **E)** Incorreta. As licenças e autorizações experimentais são essencialmente temporárias e condicionadas a relatórios periódicos de conformidade.
> 
> **Gabarito: B**
"""

q09 = """
---

### Questão 09 (FCC – Inédita – Padrão TCE-GO - Analista de Controle Externo / Governança de TI)
**Enunciado:** A diretriz de **Inteligência Artificial Aberta (*Open Source AI*)**, positivada no marco legal da LC nº 205/2025, estabelece que os órgãos e entidades do Estado de Goiás deem preferência a modelos e ferramentas de código aberto. Sob a ótica do controle externo e da auditoria de TI do TCE-GO, essa diretriz fundamenta-se tecnicamente em:  

* **A)** Reduzir o nível de segurança dos servidores públicos, permitindo que qualquer invasor externo delete os bancos de dados estaduais sem ser identificado.
* **B)** Garantir a auditabilidade profunda e independente de códigos-fonte, arquitetura e pesos dos modelos (eliminando o problema da "caixa-preta"), além de preservar a soberania de dados do Estado e mitigar o risco de dependência de fornecedor (*vendor lock-in*).
* **C)** Proibir que o Estado celebre convênios com a Universidade Federal de Goiás (UFG) ou com a Fapeg.
* **D)** Obrigar o pagamento de royalties abusivos a monopólios internacionais de computação em nuvem proprietária.
* **E)** Impedir a realização de testes de validação estatística em pipelines de aprendizado de máquina.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O uso de software livre e modelos abertos permite auditoria pública e correção mais célere de falhas, não significando relaxamento de segurança.
> - **B)** **Correta.** A preferência por IA Aberta (*Open Source AI*) é um marco estratégico da LC nº 205/2025: possibilita que os auditores de controle externo examinem os algoritmos e pesos sem entraves de segredo comercial proprietário (*caixa-preta*), viabiliza a execução *on-premises* sem vazamento de dados fiscais goianos para datacenters no exterior e previne o aprisionamento tecnológico (*vendor lock-in*).
> - **C)** Incorreta. A diretriz de IA aberta incentiva exatamente a cooperação com universidades e centros de pesquisa estaduais.
> - **D)** Incorreta. A redução drástica de custos de licenciamento e royalties em moeda estrangeira é uma das principais vantagens econômicas da diretriz.
> - **E)** Incorreta. A auditabilidade de modelos abertos facilita e aprofunda os testes de validação estatística e MLOps.
> 
> **Gabarito: B**
"""

q10 = """
---

### Questão 10 (FCC – Inédita – Padrão TCE-GO - Auditor Estadual de Controle Externo / TI)
**Enunciado:** Na realização de auditorias operacionais e de conformidade sobre soluções governamentais que utilizam sistemas de inteligência artificial em Goiás, o corpo técnico de fiscalização de TIC do TCE-GO estrutura seus trabalhos em três dimensões avaliativas essenciais. Assinale a afirmativa que descreve corretamente a **Auditoria de Dados de Treinamento (*Data-Centric AI Audit*)**:  

* **A)** Consiste exclusivamente em verificar a marca dos gabinetes dos computadores onde os dados foram digitados por estagiários.
* **B)** Avalia a licitude da coleta e tratamento das bases de treino perante a LGPD, a representatividade estatística das amostras, a qualidade do processo de rotulagem e a higidez histórica para prevenir a perpetuação ou indução de vieses algorítmicos discriminatórios.
* **C)** Avalia unicamente se o contrato foi assinado em cartório físico de notas no interior do Estado.
* **D)** Visa impedir que os órgãos públicos realizem limpeza e pré-processamento nos dados brutos antes de treinar os algoritmos.
* **E)** Restringe-se a checar se os dados de treino foram comprados em fóruns ilegais da dark web para garantir maior variedade de informações.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Auditoria em dados de treino foca na camada lógica, estatística, ética e regulatória dos dados, não na carcaça metálica dos servidores.
> - **B)** **Correta.** Na abordagem *Data-Centric AI Audit*, o Tribunal de Contas audita a "matéria-prima" do modelo: conformidade das bases com a LGPD, pertinência, completude, qualidade das anotações e ausência de vieses estruturais que possam contaminar as decisões automatizadas de políticas públicas.
> - **C)** Incorreta. Processos formais de licitação pertencem à auditoria de conformidade tradicional, enquanto a auditoria de dados é técnica e analítica.
> - **D)** Incorreta. Limpeza, tratamento de outliers e normalização são requisitos fundamentais de engenharia de dados.
> - **E)** Incorreta. A aquisição de dados ilícitos constituiria infração gravíssima e nulidade insanável.
> 
> **Gabarito: B**
"""

# Insertions:
# 1. After Section 1.1 bullet 2 (line ~44)
p1 = "2. **Salvaguardas de Direitos Fundamentais e Ética Algorítmica:** Assegurar que os sistemas de IA empregados na administração pública estadual respeitem os direitos dos cidadãos, a legalidade, a transparência, a não discriminação e a privacidade de dados pessoais (LGPD).\n"
assert p1 in content, "Pattern 1 not found"
content = content.replace(p1, p1 + q06 + "\n")

# 2. After Section 1.2 alert box (line ~80)
p2 = "> A FCC adora cobrar a regra da **Supervisão Humana (*Human-in-the-Loop*)**. É vedada no Estado de Goiás a tomada de decisão administrativa puramente automatizada e irrecorrível por IA que restrinja direitos de cidadãos ou empresas (como cancelamento de benefício ou sanção fiscal). O cidadão tem o direito de requerer a revisão humana da decisão!\n"
assert p2 in content, "Pattern 2 not found"
content = content.replace(p2, p2 + q07 + "\n")

# 3. After Section 2.1 bullet 4 (line ~119)
p3 = "    - Limitação temporal de permanência no ambiente experimental.\n"
assert p3 in content, "Pattern 3 not found"
content = content.replace(p3, p3 + q08 + "\n")

# 4. After Section 2.3 bullet 4 (line ~200)
p4 = "- **Customização Local:** Facilita o ajuste fino (*fine-tuning*) dos modelos para atender particularidades regionais, jurídicas e econômicas de Goiás.\n"
assert p4 in content, "Pattern 4 not found"
content = content.replace(p4, p4 + q09 + "\n")

# 5. After Section 3.1 item 3 (line ~265)
p5 = "    - Trilhas de auditoria registrando inputs, scores de confiança e identificação do servidor responsável pela homologação final do ato.\n"
assert p5 in content, "Pattern 5 not found"
content = content.replace(p5, p5 + q10 + "\n")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("File 13_04 successfully updated!")
