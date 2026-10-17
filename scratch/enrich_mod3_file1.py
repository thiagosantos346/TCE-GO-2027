import os, re

FILE = r"fontes_de_estudo/conhecimentos_gerais/03_legislacao_institucional/01_bases_constitucionais_cf88_e_ce_go.md"

q06_text = """
### Questão 06
**(FCC – TCE-GO – Analista de Controle Externo)**  
Nos termos do artigo 37, inciso XVI, e do artigo 38 da Constituição Federal de 1988, a respeito da acumulação remunerada de cargos públicos e do exercício de mandato eletivo por servidor público:

* **A)** É permitida a acumulação remunerada de três cargos de professor, desde que comprovada a compatibilidade de horários.
* **B)** É constitucional a acumulação remunerada de dois cargos privativos de profissionais de saúde, com profissões regulamentadas, havendo compatibilidade de horários, independentemente de teto remuneratório.
* **C)** O servidor público investido no mandato de Prefeito será afastado do cargo efetivo, sendo-lhe facultado optar pela sua remuneração de origem.
* **D)** O servidor público investido no mandato de Vereador deverá ser compulsoriamente afastado de seu cargo efetivo, sem direito a optar pelo subsídio do mandato legislativo.
* **E)** É vedada em qualquer hipótese a acumulação de um cargo de professor com outro técnico ou científico.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A regra do art. 37, XVI, "a", autoriza a acumulação de **dois** cargos de professor (e não três), desde que haja compatibilidade de horários.
> - **B)** Incorreta. Embora seja lícita a acumulação de dois cargos de profissionais de saúde (art. 37, XVI, "c"), a remuneração cumulada submete-se ao teto constitucional (STF, Temas 377 e 384: o teto incide isoladamente sobre cada vínculo, mas não há dispensa de teto).
> - **C)** Correta. De acordo com o art. 38, inciso II, da CF/88: *"investido no mandato de Prefeito, será afastado do cargo, emprego ou função, sendo-lhe facultado optar pela sua remuneração"*. O afastamento funcional é obrigatório, mas a opção remuneratória é prerrogativa expressa do servidor.
> - **D)** Incorreta. Para o mandato de Vereador (art. 38, III), havendo compatibilidade de horários, o servidor perceberá as vantagens de seu cargo cumulativamente com a remuneração do cargo eletivo. Se não houver compatibilidade, aplica-se a regra do prefeito.
> - **E)** Incorreta. A acumulação de um cargo de professor com outro técnico ou científico é expressamente autorizada pela CF/88 (art. 37, XVI, "b").
>
> **Gabarito: C**
"""

q07_text = """
### Questão 07
**(FCC – TCE-PI – Auditor de Controle Externo)**  
Em matéria de responsabilidade civil da Administração Pública (art. 37, § 6º, da CF/88) e atuação de agentes públicos:

* **A)** As pessoas jurídicas de direito público e as de direito privado prestadoras de serviços públicos responderão pelos danos que seus agentes causarem a terceiros com base na teoria da culpa administrativa subjetiva.
* **B)** A vítima de um dano causado por viatura oficial em trânsito pode ajuizar ação indenizatória diretamente e com exclusividade em face do servidor causador do acidente.
* **C)** A responsabilidade civil do Estado independe de culpa ou dolo da Administração (responsabilidade objetiva sob a teoria do risco administrativo), assegurado o direito de regresso contra o agente responsável nos casos de dolo ou culpa.
* **D)** O direito de regresso contra o agente público pode ser exercido mesmo que a Administração Pública não comprove dolo ou culpa do servidor.
* **E)** A teoria do risco integral é a regra geral no direito brasileiro, não admitindo excludentes como caso fortuito ou força maior.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A responsabilidade das pessoas de direito público e das prestadoras de serviço público é **objetiva** (teoria do risco administrativo), e não subjetiva.
> - **B)** Incorreta. Conforme jurisprudência vinculante do Supremo Tribunal Federal (Tema 940 de Repercussão Geral - RE 1.027.633): *"A teor do disposto no art. 37, § 6º, da Constituição Federal, a ação por danos causados por agente público deve ser ajuizada contra o Estado ou a pessoa jurídica de direito privado prestadora de serviço público, sendo parte ilegítima para a lide o autor do ato, assegurado o direito de regresso contra o responsável nos casos de dolo ou culpa"*.
> - **C)** Correta. Traduz fielmente a redação do art. 37, § 6º, da CF/88 e a doutrina do Direito Administrativo: a responsabilidade estatal é objetiva (basta conduta estatal, nexo causal e dano), cabendo ação regressiva contra o servidor unicamente se este tiver agido com dolo ou culpa.
> - **D)** Incorreta. Na ação de regresso em face do servidor, a responsabilidade é subjetiva, exigindo a demonstração inequívoca de dolo ou culpa.
> - **E)** Incorreta. A regra adotada é a do **risco administrativo**, que admite atenuantes e excludentes de responsabilidade (culpa exclusiva da vítima, caso fortuito e força maior).
>
> **Gabarito: C**
"""

q08_text = """
### Questão 08
**(FCC – TCE-GO – Analista de Controle Externo)**  
No tocante ao controle externo exercido pelo Tribunal de Contas sobre os atos de pessoal e concessão de benefícios previdenciários (art. 71, III, da CF/88):

* **A)** O registro de aposentadorias, reformas e pensões pelos Tribunais de Contas é ato meramente homologatório, não podendo a Corte de Contas recusar registro fundado em ilegalidade.
* **B)** O procedimento de registro inicial de aposentadoria no Tribunal de Contas prescinde do contraditório e da ampla defesa, desde que a análise seja concluída no prazo de 5 anos a contar da chegada do processo à Corte.
* **C)** A Súmula Vinculante nº 3 do STF estabelece que o contraditório e a ampla defesa são sempre obrigatórios na apreciação da legalidade do ato de concessão inicial de aposentadoria, independentemente do tempo decorrido.
* **D)** A nomeação para cargo em comissão de livre nomeação e exoneração está sujeita a registro prévio e obrigatório pelo Tribunal de Contas perante o qual atua o órgão.
* **E)** Decorrido o prazo de 10 anos sem manifestação do Tribunal de Contas, o ato de aposentadoria é sumariamente anulado por decurso de prazo.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O exame de legalidade para fins de registro é ato complexo e dotado de densidade fiscalizatória plena; se houver ilegalidade, o Tribunal de Contas nega o registro e determina a cessação dos pagamentos indevidos.
> - **B)** Correta. A Súmula Vinculante nº 3 do STF estabelece expressamente: *"Nos processos perante o Tribunal de Contas da União asseguram-se o contraditório e a ampla defesa quando da decisão puder resultar anulação ou revogação de ato administrativo que beneficie o interessado, **excetuada a apreciação da legalidade do ato de concessão inicial de aposentadoria, reforma e pensão**"*. Todavia, segundo tese de Repercussão Geral fixada pelo STF (Tema 445 - RE 636.553), ultrapassado o prazo de 5 anos a contar da chegada do processo ao TC sem decisão, o ato é tacitamente estabilizado, exigindo a partir de então prévio contraditório.
> - **C)** Incorreta. A SV 3 excetua expressamente a apreciação da concessão inicial.
> - **D)** Incorreta. O art. 71, III, da CF/88 ressalva taxativamente as nomeações para cargo de provimento em comissão da obrigatoriedade de registro no Tribunal de Contas.
> - **E)** Incorreta. Não há anulação sumária por decurso de prazo; ultrapassados 5 anos sem julgamento, opera-se o direito ao contraditório antes de eventual revisão.
>
> **Gabarito: B**
"""

q09_text = """
### Questão 09
**(FCC – TRT – Analista Judiciário)**  
Sobre o rito constitucional de fiscalização e sustação de atos e contratos administrativos disciplinado no artigo 71, incisos IX a XI e §§ 1º e 2º, da Constituição Federal:

* **A)** Tanto a sustação de ato administrativo quanto a de contrato administrativo são atos privativos de competência originária e direta do Tribunal de Contas.
* **B)** No caso de contrato administrativo com irregularidade grave, a competência para a sustação é primariamente do Congresso Nacional (ou Assembleia Legislativa), cabendo ao Tribunal de Contas decidir sobre a sustação caso o Poder Legislativo não se manifeste no prazo de 90 dias.
* **C)** O Tribunal de Contas pode sustar imediatamente um contrato administrativo sem necessidade de qualquer prévia comunicação ao Poder Legislativo ou ao Poder Executivo.
* **D)** A sustação de ato administrativo impugnado pelo Tribunal de Contas depende sempre de prévia autorização da Assembleia Legislativa.
* **E)** Se o Poder Legislativo sustar o contrato, o Tribunal de Contas deverá anular a decisão parlamentar no prazo de 30 dias.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O regime constitucional é diferenciado: o Tribunal de Contas susta diretamente os **atos** administrativos (art. 71, X); mas a sustação de **contratos** administrativos é prerrogativa primária do Poder Legislativo (art. 71, § 1º).
> - **B)** Correta. Trata-se da clássica pegadinha do art. 71, §§ 1º e 2º, da CF/88:  
>   - *§ 1º:* No caso de contrato, o ato de sustação será adotado diretamente pelo Congresso Nacional (ou Assembleia Legislativa), que solicitará, de imediato, ao Poder Executivo as medidas cabíveis.  
>   - *§ 2º:* Se o Congresso Nacional (ou o Poder Executivo) não efetivar as medidas no prazo de **90 dias**, o Tribunal de Contas decidirá a respeito da sustação do contrato.
> - **C)** Incorreta. O TC só assume a competência supletiva de sustar o contrato após a inércia parlamentar pelo prazo de 90 dias.
> - **D)** Incorreta. A sustação de ato administrativo é executada diretamente pelo Tribunal de Contas (art. 71, X).
> - **E)** Incorreta. O TC não anula decisões do Poder Legislativo sobre sustação de contratos; quem exerce o controle jurisdicional de constitucionalidade é o Poder Judiciário.
>
> **Gabarito: B**
"""

q10_text = """
### Questão 10
**(FCC – Inédita – Padrão TCE-GO)**  
De acordo com o artigo 30 da Constituição do Estado de Goiás e a jurisprudência sumulada do Supremo Tribunal Federal a respeito do Ministério Público de Contas (MPC):

* **A)** O Ministério Público de Contas compõe ramo autônomo do Ministério Público do Estado de Goiás (MPE-GO), sendo chefiado pelo Procurador-Geral de Justiça do Estado.
* **B)** O Ministério Público junto ao Tribunal de Contas do Estado de Goiás possui quadro próprio de membros, investidos por concurso público específico de provas e títulos, submetendo-se administrativamente à estrutura orgânica do Tribunal de Contas, sem personalidade jurídica própria.
* **C)** Os Procuradores do MPC de Goiás não gozam das garantias de vitaliciedade, inamovibilidade e irredutibilidade de subsídios conferidas aos membros do Ministério Público comum.
* **D)** Compete ao Ministério Público de Contas ajuizar ações civis públicas perante o Poder Judiciário para cobrança de títulos executivos emitidos pelo TCE-GO.
* **E)** O Procurador-Geral de Contas é livremente nomeado pelo Presidente do TCE-GO, sem participação do Governador do Estado.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O MPC não integra o MPE (Ministério Público comum estadual), sendo órgão especial que atua exclusivamente perante a Corte de Contas (Súmula 653 do STF: *"No Tribunal de Contas da União, o Ministério Público junto ao Tribunal tem sua organização regulada em lei federal, e não na Lei Orgânica do Ministério Público da União"*).
> - **B)** Correta. O MPC-GO é instituição dotada de autonomia funcional e prerrogativas ministeriais, mas administrativamente vinculada ao TCE-GO (art. 130 da CF/88 e art. 30 da CE/GO), sem personalidade jurídica independente. Seus membros ingressam por concurso público específico de provas e títulos.
> - **C)** Incorreta. O art. 130 da CF/88 estende expressamente aos membros do Ministério Público junto aos Tribunais de Contas as garantias, vedações e forma de investidura aplicáveis aos membros do Ministério Público da União e dos Estados (vitaliciedade, inamovibilidade e irredutibilidade).
> - **D)** Incorreta. Conforme jurisprudência vinculante do STF (Súmula 353 e Tema 642): a legitimidade para execução judicial de título condenatório de Tribunal de Contas é da Fazenda Pública beneficiária (PGE ou PGM), e não do MPC.
> - **E)** Incorreta. O Procurador-Geral de Contas é nomeado pelo Governador do Estado a partir de lista tríplice formada pelos membros do colegiado ministerial do MPC, conforme a Lei Orgânica do TCE-GO.
>
> **Gabarito: B**
"""

def enrich_mod3_file1():
    with open(FILE, "r", encoding="utf-8") as f:
        text = f.read()

    # Inserção da Questão 06: na Seção 1.5 (antes de "### 1.6 Estabilidade Constitucional")
    sec16 = "### 1.6 Estabilidade Constitucional e Hipóteses Taxativas de Perda do Cargo"
    idx16 = text.find(sec16)
    text = text[:idx16] + "\n---\n" + q06_text + "\n---\n\n" + text[idx16:]

    # Inserção da Questão 07: no fim da Seção 1 (antes de "## 2. Fiscalização e Controle na CF/88")
    sec2 = "## 2. Fiscalização e Controle na CF/88 (Arts. 70 a 75)"
    idx2 = text.find(sec2)
    dash_idx = text.rfind("---", 0, idx2)
    text = text[:dash_idx] + q07_text + "\n---\n\n" + text[dash_idx:]

    # Inserção da Questão 08: na Seção 2.3 (antes de "### 2.4 Rito Constitucional de Sustação de Atos e Contratos")
    sec24 = "### 2.4 Rito Constitucional de Sustação de Atos e Contratos Administrativos"
    idx24 = text.find(sec24)
    text = text[:idx24] + "\n---\n" + q08_text + "\n---\n\n" + text[idx24:]

    # Inserção da Questão 09: na Seção 2.5 (antes de "### 2.6 Sistema Integrado de Controle Interno")
    sec26 = "### 2.6 Sistema Integrado de Controle Interno e Responsabilidade Solidária (Art. 74)"
    idx26 = text.find(sec26)
    text = text[:idx26] + "\n---\n" + q09_text + "\n---\n\n" + text[idx26:]

    # Inserção da Questão 10: no fim da Seção 3 (antes de "## 4. Fontes Oficiais e Referências Bibliográficas")
    sec_fontes = "## 4. Fontes Oficiais e Referências Bibliográficas"
    idxf = text.find(sec_fontes)
    dash_idx = text.rfind("---", 0, idxf)
    text = text[:dash_idx] + q10_text + "\n---\n\n" + text[dash_idx:]

    with open(FILE, "w", encoding="utf-8") as f:
        f.write(text)

    print("Module 03 File 01 enriquecido com sucesso.")

enrich_mod3_file1()
