import os

file_path = "fontes_de_estudo/conhecimentos_especificos_b02_ti/12_governanca_de_ti/04_contratacoes_de_tic_lei_14133_2021.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

q06 = """
---

### Questão 06 (FCC - Tribunal de Contas - Auditor de Controle Externo / TI - Adaptada)
**Enunciado:** Em conformidade com a Lei nº 14.133/2021 e as boas práticas de governança de contratações públicas de TIC, os processos de compra de soluções tecnológicas devem observar estrito alinhamento ao planejamento prévio institucional. A respeito dos instrumentos de planejamento, assinale a afirmativa correta:  

* **A)** O Plano de Contratações Anual (PCA) substitui integralmente a necessidade de instauração de processos licitatórios individuais, autorizando a contratação verbal direta.
* **B)** A contratação de soluções de TIC prescinde de compatibilidade com o Plano Diretor de Tecnologia da Informação (PDTI), bastando o requerimento informal do presidente do órgão.
* **C)** O Plano Diretor de TIC (PDTI) é o instrumento plurianual de diagnóstico, planejamento e gestão estratégica de TI, ao qual devem estar alinhadas as contratações consolidadas no Plano de Contratações Anual (PCA).
* **D)** A elaboração do PCA é facultativa para órgãos que possuam menos de 10.000 servidores, devendo suas compras de tecnologia ser executadas exclusivamente por adiantamento de numerário.
* **E)** As soluções de TIC voltadas à modernização de auditorias fiscais podem ser adquiridas sem qualquer previsão no PDTI, desde que justificadas após o término do contrato.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O PCA consolida o planejamento anual das compras para fins orçamentários e de transparência, mas cada contratação segue seu devido processo administrativo licitatório ou de contratação direta.
> - **B)** Incorreta. O alinhamento com o PDTI e com o PEI (Planejamento Estratégico Institucional) é requisito mandatório de governança e economicidade.
> - **C)** **Correta.** O PDTI mapeia a visão estratégica plurianual de TIC, e o PCA operacionaliza o cronograma anual de contratações necessárias para viabilizar as metas institucionais.
> - **D)** Incorreta. A exigência de planejamento anual de contratações aplica-se aos órgãos e entidades no âmbito do sistema licitatório, sem isenção por número de servidores.
> - **E)** Incorreta. O planejamento é prévio (*ex ante*), sendo irregular a aquisição sem previsão ou fundamentação de compatibilidade tempestiva.
> 
> **Gabarito: C**
"""

q07 = """
---

### Questão 07 (FGV - TJ-AP - Analista Judiciário - Tecnologia da Informação - Adaptada)
**Enunciado:** Na fase preparatória de uma contratação de TIC sob a égide da Lei nº 14.133/2021 e normativos de contratação de soluções digitais, a equipe de planejamento da contratação é responsável por elaborar artefatos estruturantes. A respeito desses documentos, assinale a afirmativa correta:  

* **A)** O Documento de Oficialização da Demanda (DOD) é emitido pela empresa vencedora da licitação para comunicar à Administração o início da entrega de hardware.
* **B)** O Estudo Técnico Preliminar (ETP) tem como finalidade evidenciar o problema a ser resolvido e a melhor solução entre as alternativas de mercado, avaliando a viabilidade técnica e o Custo Total de Propriedade (TCO).
* **C)** O Termo de Referência é um documento preliminar e não vinculante, podendo a contratada alterar livremente os requisitos de software durante o desenvolvimento.
* **D)** A elaboração do Mapa de Riscos é dispensável em contratações de TIC, haja vista que os riscos cibernéticos são integralmente assumidos pelo fabricante de software.
* **E)** A equipe de planejamento da contratação de TIC deve ser composta por um único servidor sem conhecimento técnico em informática, visando garantir a imparcialidade do processo.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O DOD é um artefato interno emitido pela área requisitante (órgão público) para formalizar a necessidade institucional perante a área de TIC.
> - **B)** **Correta.** O ETP constitui a primeira etapa da fase preparatória e fundamenta a escolha da solução mediante estudo comparativo de alternativas e cálculo do TCO.
> - **C)** Incorreta. O TR é o documento definitivo e vinculante que integra o edital e define o objeto, requisitos, modelo de execução e IMR.
> - **D)** Incorreta. O gerenciamento de riscos ao longo de todo o ciclo de vida da contratação de TIC é obrigatório.
> - **E)** Incorreta. A equipe de planejamento deve observar a multidisciplinaridade e segregação de funções, contando com integrante técnico (TI), integrante requisitante e integrante administrativo.
> 
> **Gabarito: B**
"""

q08 = """
---

### Questão 08 (FCC - TRT-9 - Analista Judiciário - Tecnologia da Informação - Adaptada)
**Enunciado:** A Lei nº 14.133/2021 disciplina as hipóteses de contratação direta em seus artigos 74 (Inexigibilidade) e 75 (Dispensa). Em matéria de contratação de soluções de TIC na Administração Pública, assinale a opção que descreve uma hipótese legítima de Inexigibilidade de licitação:  

* **A)** Aquisição de computadores padrão para secretarias administrativas, com base unicamente na alegação de conveniência de prazo.
* **B)** Contratação de empresa para suporte técnico rotineiro e atendimento de help desk de primeiro nível em informática.
* **C)** Aquisição de materiais e cabos de rede de baixo valor financeiro que se enquadrem no limite de pequenos serviços.
* **D)** Contratação de serviços técnicos especializados de natureza predominantemente intelectual com profissionais ou empresas de notória especialização para perícia forense digital de altíssima complexidade e singularidade.
* **E)** Restabelecimento emergencial de infraestrutura de refrigeração do data center após incêndio acidental.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Computadores comuns são bens comuns de TIC e exigem licitação, preferencialmente na modalidade Pregão Eletrônico.
> - **B)** Incorreta. Suporte rotineiro de help desk é serviço comum contínuo, sem singularidade ou natureza predominantemente intelectual que justifique inexigibilidade.
> - **C)** Incorreta. Compras de pequeno valor constituem hipótese de Dispensa de Licitação em razão do valor (Art. 75, II).
> - **D)** **Correta.** Conforme o Art. 74, III, da Lei nº 14.133/2021, é inexigível a licitação para serviços técnicos especializados de natureza predominantemente intelectual prestados por profissional ou empresa de notória especialização, vedada a inexigibilidade para serviços de publicidade e divulgação.
> - **E)** Incorreta. Contratação decorrente de emergência ou calamidade pública constitui hipótese de Dispensa de Licitação (Art. 75, VIII).
> 
> **Gabarito: D**
"""

q09 = """
---

### Questão 09 (FCC - Auditor Estadual de Controle Externo / TI - Adaptada)
**Enunciado:** Em relação à gestão e fiscalização de contratos de prestação de serviços de Tecnologia da Informação na Lei nº 14.133/2021, a Administração deve designar servidores com papéis bem segregados. Assinale a alternativa que descreve com precisão a competência do Fiscal Técnico do contrato de TIC:  

* **A)** Conferir a regularidade trabalhista e o recolhimento das guias de FGTS e INSS dos empregados terceirizados alocados na empresa.
* **B)** Avaliar e atestar tecnicamente se os sistemas desenvolvidos ou serviços de infraestrutura atendem aos requisitos arquiteturais, padrões técnicos de codificação e níveis de serviço fixados no IMR.
* **C)** Formalizar administrativamente aditivos de prorrogação contratual e aplicar penalidades financeiras de impedimento de licitar.
* **D)** Assinar o contrato inicial em substituição ao Presidente do Tribunal de Contas.
* **E)** Realizar a mediação jurídica em litígios judiciais trabalhistas perante o Tribunal Regional do Trabalho.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A conferência de encargos sociais, trabalhistas e previdenciários compete ao Fiscal Administrativo.
> - **B)** **Correta.** O Fiscal Técnico de TIC é o responsável pela verificação da conformidade técnica do objeto entregue, analisando artefatos, arquitetura, testes e o cumprimento dos níveis acordados de serviço (IMR).
> - **C)** Incorreta. A coordenação administrativa, termos aditivos e proposição formal de sanções são atribuições do Gestor do Contrato e da autoridade competente.
> - **D)** Incorreta. A assinatura do contrato é atribuição da autoridade máxima do órgão contratante.
> - **E)** Incorreta. Representação judicial compete à Procuradoria Jurídica do órgão.
> 
> **Gabarito: B**
"""

q10 = """
---

### Questão 10 (FCC - Técnico de Controle Externo / TI - Adaptada)
**Enunciado:** No âmbito dos contratos de prestação de serviços e fornecimento de software e infraestrutura de TIC regidos pela Lei nº 14.133/2021, o processo de liquidação e pagamento depende dos atos formais de recebimento do objeto. Acerca do recebimento provisório e definitivo, assinale a afirmativa correta:  

* **A)** O recebimento provisório transfere a propriedade definitiva do código-fonte para a contratada e desonera a empresa de qualquer garantia técnica posterior.
* **B)** O recebimento provisório é realizado pelos fiscais do contrato para efeito de posterior verificação da conformidade dos serviços com as exigências contratuais, enquanto o recebimento definitivo é realizado pelo gestor do contrato ou comissão mediante termo detalhado que comprove o atendimento integral das exigências.
* **C)** Em contratos de soluções de TIC é vedada a emissão de recebimento provisório, ocorrendo a emissão imediata de nota fiscal e pagamento à vista antes da entrega do software.
* **D)** O recebimento definitivo pode ser firmado tacitamente pelo fornecedor caso a Administração não responda em 24 horas, vedada qualquer aplicação posterior de glosas contratuais.
* **E)** O recebimento definitivo dispensa a realização de testes de homologação de sistemas de auditoria digital.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O recebimento provisório apenas atesta a entrega física dos bens ou conclusão aparente do serviço para que se iniciem os testes de conformidade.
> - **B)** **Correta.** Conforme o Art. 140 da Lei nº 14.133/2021, o objeto é recebido provisoriamente pelo responsável por seu acompanhamento e fiscalização, e definitivamente por servidor ou comissão designada pela autoridade competente, mediante termo detalhado que comprove o atendimento das exigências contratuais.
> - **C)** Incorreta. O recebimento provisório é etapa obrigatória do procedimento de controle em serviços e compras de tecnologia.
> - **D)** Incorreta. Não há recebimento definitivo tácito por parte da empresa; o ato administrativo de atesto definitivo exige manifestação expressa e motivada da Administração.
> - **E)** Incorreta. O recebimento definitivo pressupõe justamente que os testes de homologação tenham sido integralmente realizados e aprovados.
> 
> **Gabarito: B**
"""

# Insertions:
# 1. After Section 1.1 bullet 3 (line ~61)
p1 = "- **Regra:** Toda contratação de solução de TIC deve estar expressamente prevista ou fundamentadamente compatível com o PDTI e com o PCA do exercício.\n"
assert p1 in content, "Pattern 1 not found"
content = content.replace(p1, p1 + q06 + "\n")

# 2. After Section 2.1 table row TR (line ~138)
p2 = "| **TR** (*Termo de Referência*) | Equipe de Planejamento | Documento definitivo que estabelece o objeto, requisitos funcionais e não funcionais, modelo de execução, critérios de habilitação e o **Instrumento de Medição de Resultado (IMR)**. |\n"
assert p2 in content, "Pattern 2 not found"
content = content.replace(p2, p2 + q07 + "\n")

# 3. After Section 3.2 alert box (line ~243)
p3 = "> A contratação de empresa por Notória Especialização com base em Inexigibilidade (Art. 74, III) **não pode** ser usada para suporte rotineiro de informática ou help-desk! Ela exige cumulativamente: 1) Natureza predominantemente intelectual; 2) Notória especialização do prestador; e 3) Singularidade do serviço.\n"
assert p3 in content, "Pattern 3 not found"
content = content.replace(p3, p3 + q08 + "\n")

# 4. After Section 4.1 bullet 4 (line ~271)
p4 = "- **Fiscal Administrativo:** Servidor que confere o pagamento de salários, FGTS, INSS e tributos dos empregados terceirizados, protegendo a Administração contra condenações subsidiárias na Justiça do Trabalho.\n"
assert p4 in content, "Pattern 4 not found"
content = content.replace(p4, p4 + q09 + "\n")

# 5. Before Section 6. Fontes
target = "## 6. Fontes Recomendadas na Internet"
assert target in content, "target not found"
idx = content.find(target)
content = content[:idx] + q10.strip() + "\n\n---\n\n" + content[idx:]

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("File 12_04 successfully updated!")
