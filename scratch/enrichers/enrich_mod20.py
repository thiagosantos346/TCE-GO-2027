# -*- coding: utf-8 -*-
"""
Enriquecedor Módulo 20 - Contabilidade Aplicada ao Setor Público (CASP)
Arquivos: 01, 02, 03, 04
Adiciona de 5 a 6 questões por arquivo (Questões 06 a 10/11) no padrão rigoroso FCC / Anti-spoiler.
"""

import os

BASE_DIR = "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/20_contabilidade_aplicada_ao_setor_publico"

# ==========================================
# ARQUIVO 01: 01_nbc_tsp_estrutura_conceitual_e_normas_gerais.md
# ==========================================
def enrich_file_01():
    filepath = os.path.join(BASE_DIR, "01_nbc_tsp_estrutura_conceitual_e_normas_gerais.md")
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    if "### Questão 06" in text:
        print("File 01 already enriched.")
        return

    # Q06: Após 1.3 Usuários Primários e Objetivos Centrais dos RCPGs (antes de ### 2.)
    q06 = """### Questão 06 (FCC - Adaptada / Analista Contábil)
De acordo com a NBC TSP Estrutura Conceitual, a informação contábil no setor público destina-se primordialmente a suprir as necessidades de informação dos usuários primários dos Relatórios Contábeis de Propósito Geral das Entidades do Setor Público (RCPGs).

São considerados usuários primários dos RCPGs:

* **A)** Os usuários dos serviços públicos e seus representantes (cidadãos, membros do Poder Legislativo) e os provedores de recursos (contribuintes, doadores, credores por empréstimos).
* **B)** Exclusivamente os auditores de controle externo dos Tribunais de Contas e os contadores públicos responsáveis pelo fechamento do balanço.
* **C)** Unicamente as agências internacionais de classificação de risco de crédito soberano (ratings).
* **D)** Apenas os secretários de fazenda e os dirigentes máximos das entidades do Poder Executivo.
* **E)** As sociedades empresárias privadas concorrentes que participam de processos licitatórios governamentais.

> **Comentário Detalhado:**
>
> - **A)** Correta. A NBC TSP Estrutura Conceitual define expressamente como **usuários primários dos RCPGs**: (1) os usuários de serviços e seus representantes (cidadãos e parlamentares); e (2) os provedores de recursos e seus representantes (contribuintes, doadores, financiadores e credores).
> - **B)** Incorreta. Auditores e contadores são usuários institucionais e reguladores, mas os usuários primários são os cidadãos e provedores de recursos para fins de prestação de contas (*accountability*) e tomada de decisão.
> - **C)** Incorreta. Agências de rating são usuários secundários ou específicos.
> - **D)** Incorreta. Gestores públicos utilizam relatórios de gestão gerencial interna; os RCPGs destinam-se a usuários externos que não têm poder para exigir relatórios customizados.
> - **E)** Incorreta. Licitantes não figuram no rol dos usuários primários conceituais dos RCPGs.
> 
> **Gabarito: A**

---

"""

    # Q07: Após 2.2 Restrições Inerentes: Custo-Benefício e Materialidade (antes de ### 3.)
    q07 = """### Questão 07 (FCC - Adaptada / TCE-SC - Auditor de Controle Externo)
Na NBC TSP Estrutura Conceitual, as características qualitativas são atributos que tornam a informação contida nos RCPGs útil para os usuários. Considere as seguintes características:

I. **Relevância:** A informação é relevante se for capaz de influenciar as decisões dos usuários, tendo valor confirmatório, preditivo ou ambos.  
II. **Representação Fidedigna:** Para ser fidedigna, a informação deve ser completa, neutra e livre de erro material, retratando fielmente a substância econômica da transação e não apenas sua forma jurídica.  
III. **Compreensibilidade:** Pressupõe que os relatórios contábeis públicos sejam simplificados a ponto de dispensar qualquer conhecimento prévio dos usuários sobre economia e finanças governamentais.

Está correto o que se afirma em:

* **A)** I, apenas.
* **B)** I e II, apenas.
* **C)** II e III, apenas.
* **D)** I e III, apenas.
* **E)** I, II e III.

> **Comentário Detalhado:**
>
> - **I. Correto.** A relevância é característica qualitativa fundamental caracterizada pelo valor confirmatório e/ou preditivo.
> - **II. Correto.** A representação fidedigna exige que a informação seja completa, neutra e isenta de erro material, com primazia da substância sobre a forma.
> - **III. Incorreto.** A compreensibilidade permite que a informação seja facilmente compreendida por usuários que tenham conhecimento razoável das atividades do setor público e do ambiente econômico, e que se disponham a estudar a informação com razoável diligência. Não se eliminam informações complexas e relevantes apenas sob o argumento de que seriam difíceis de compreender por leigos absolutos.
> 
> **Gabarito: B**

---

"""

    # Q08: Após 3.2 Bases de Mensuração para Ativos e Passivos (antes de ### 4.)
    q08 = """### Questão 08 (FCC - Adaptada / Analista de Planejamento e Orçamento)
No que concerne às bases de mensuração para ativos e passivos segundo a NBC TSP Estrutura Conceitual, assinale a opção correta:

* **A)** O custo histórico é uma base de mensuração a valor de saída que reflete o preço que seria recebido pela venda de um ativo no mercado aberto.
* **B)** O custo de reposição ou substituição é uma base de mensuração a valor de entrada que reflete o custo mais econômico exigido para a entidade substituir o potencial de serviços de um ativo na data das demonstrações contábeis.
* **C)** O valor justo é uma medida específica da entidade que independe das condições de transação entre participantes do mercado.
* **D)** O valor em uso de um ativo reflete o valor presente dos fluxos de caixa futuros descontados, aplicável exclusivamente a ativos geradores de caixa do setor público.
* **E)** Todos os passivos públicos devem ser obrigatoriamente mensurados pelo custo histórico original, sendo vedada qualquer avaliação pelo preço de liquidação.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O custo histórico é uma base de mensuração a valor de **entrada** (reflete a transação original passada).
> - **B)** Correta. O **custo de reposição/substituição** (*depreciated replacement cost*) é uma base de mensuração a valor de entrada amplamente utilizada no setor público para ativos não geradores de caixa, correspondendo ao custo mais econômico para substituir o potencial de serviços do ativo.
> - **C)** Incorreta. O valor justo é mensuração baseada no mercado (preço de saída), e não medida específica da entidade.
> - **D)** Incorreta. No setor público, o valor em uso também se aplica a ativos não geradores de caixa através da mensuração do valor presente do potencial de serviços remanescente do ativo.
> - **E)** Incorreta. Passivos podem ser mensurados pelo custo histórico, custo de cumprimento da obrigação (*fulfillment cost*) ou valor de mercado/liquidação.
> 
> **Gabarito: B**

---

"""

    # Q09 e Q10: Após 4.3 Ativo Imobilizado e Depreciação Sistemática (antes de ## 🌐 Fontes Oficiais & Normativas Recomendadas)
    q09_10 = """### Questão 09 (FCC - Adaptada / TCE-PI - Auditor de Controle Externo)
A respeito da NBC TSP 07 (Ativo Imobilizado) e do reconhecimento contábil dos elementos patrimoniais, analise a seguinte hipótese:

Determinado Tribunal de Contas realizou despesas no valor de R$ 300.000,00 com obras de reforma e adaptação predial em seu auditório principal. A reforma resultou no aumento comprovado da vida útil do imóvel em 10 anos e na ampliação da capacidade de recepção de público, com instalação de novos sistemas centrais de ar-condicionado.

À luz da NBC TSP 07 e das normas contábeis aplicadas ao setor público, o dispêndio realizado:

* **A)** Deve ser capitalizado ao valor contábil do ativo imobilizado (incorporado ao custo do edifício), pois aumentou a vida útil e o potencial de serviços do bem público.
* **B)** Deve ser reconhecido integralmente como Variação Patrimonial Diminutiva (VPD) no resultado do exercício, por se tratar de despesa de manutenção rotineira.
* **C)** Não pode ser registrado no subsistema patrimonial, limitando-se ao subsistema de compensação de atos potenciais.
* **D)** Deve ser registrado como ativo intangível pelo período em que perdurarem as garantias da construtora.
* **E)** Constitui inversão financeira na classificação por natureza da despesa, devendo ser baixado imediatamente do patrimônio líquido.

> **Comentário Detalhado:**
>
> - **A)** Correta. A NBC TSP 07 e o MCASP determinam que os gastos posteriores com ativos imobilizados que aumentem a vida útil econômica, melhorem o potencial de serviços ou ampliem a capacidade produtiva do bem devem ser **capitalizados** (incorporados ao valor contábil do ativo).
> - **B)** Incorreta. Apenas reparos de conservação e manutenção periódica que visem manter o bem em operação normal sem ampliação de vida útil são reconhecidos diretamente como VPD (despesa de manutenção).
> - **C)** Incorreta. O fato afeta o patrimônio permanente e é registrado no subsistema patrimonial.
> - **D)** Incorreta. Auditórios e instalações físicas são ativos tangíveis (imobilizado), não intangíveis.
> - **E)** Incorreta. Obras de ampliação física constituem investimentos (GND 4) e aumentam o ativo não circulante.
> 
> **Gabarito: A**

---

### Questão 10 (FCC - Adaptada / TCE-GO - Analista de Controle Externo)
Segundo a NBC TSP 03 (Provisões, Passivos Contingentes e Ativos Contingentes), assinale a opção que apresenta o correto tratamento contábil para uma ação judicial movida contra um Estado da Federação cuja perda seja avaliada pela Procuradoria-Geral do Estado como **provável** e cujo valor possa ser estimado com confiabilidade:

* **A)** Deve ser reconhecida uma provisão no passivo exigível, com contrapartida em Variação Patrimonial Diminutiva (VPD) no resultado do exercício.
* **B)** Não deve ser efetuado nenhum registro no passivo, bastando a divulgação em nota explicativa como passivo contingente.
* **C)** Deve ser registrada apenas no subsistema de controle (atos potenciais passivos), sendo vedado o lançamento contábil no passivo patrimonial.
* **D)** O registro contábil fica condicionado ao trânsito em julgado da decisão judicial irrecorrível perante os Tribunais Superiores.
* **E)** Deve ser contabilizado um ativo contingente garantidor em contrapartida ao patrimônio líquido.

> **Comentário Detalhado:**
>
> - **A)** Correta. Conforme a NBC TSP 03: quando uma obrigação presente resultante de evento passado tiver saída de recursos avaliada como **provável** e puder ser mensurada com confiabilidade, **deve ser reconhecida uma provisão no passivo**, afetando o resultado (VPD).
> - **B)** Incorreta. Essa conduta aplica-se a passivos contingentes com probabilidade de perda apenas **possível**.
> - **C)** Incorreta. O fato de ser provável e mensurável exige contabilização patrimonial efetiva no Passivo Circulante ou Não Circulante.
> - **D)** Incorreta. A provisão existe exatamente para antecipar obrigações prováveis antes da liquidação jurídica definitiva (trânsito em julgado).
> - **E)** Incorreta. Ativos contingentes não são reconhecidos no balanço patrimonial.
> 
> **Gabarito: A**

---

"""

    anchor_2 = "### 2. Características Qualitativas da Informação Contábil Útil (NBC TSP EC)"
    anchor_3 = "### 3. Elementos das Demonstrações Contábeis e Bases de Mensuração"
    anchor_4 = "### 4. Normas Específicas Fundamentais no Padrão FCC"
    anchor_fontes = "## 🌐 Fontes Oficiais & Normativas Recomendadas"

    text = text.replace(anchor_2, q06 + "\n" + anchor_2)
    text = text.replace(anchor_3, q07 + "\n" + anchor_3)
    text = text.replace(anchor_4, q08 + "\n" + anchor_4)
    text = text.replace(anchor_fontes, q09_10 + "\n" + anchor_fontes)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
    print("Enriched File 20/01 successfully! Total: 10 questions.")


# ==========================================
# ARQUIVO 02: 02_mcasp_procedimentos_orcamentarios_e_patrimoniais.md
# ==========================================
def enrich_file_02():
    filepath = os.path.join(BASE_DIR, "02_mcasp_procedimentos_orcamentarios_e_patrimoniais.md")
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    if "### Questão 06" in text:
        print("File 02 already enriched.")
        return

    # Q06: Após 1.3 Quadro Sinótico de Confronto e Fatos Contábeis (antes de ### 2.)
    q06 = """### Questão 06 (FCC - Adaptada / Analista Contábil)
No âmbito da Contabilidade Aplicada ao Setor Público (CASP), a coexistência dos regimes orçamentário e patrimonial decorre da aplicação simultânea da Lei Federal nº 4.320/1964 e das normas internacionais de contabilidade (NBC TSP / MCASP).

A respeito da aplicação dos regimes contábeis, assinale a afirmativa correta:

* **A)** A despesa pública sob o enfoque patrimonial é reconhecida segundo o princípio da competência (pela ocorrência do fato gerador), independentemente do estágio da execução orçamentária (empenho ou liquidação).
* **B)** A receita orçamentária é reconhecida pelo regime de competência no momento do lançamento tributário da dívida ativa.
* **C)** O regime orçamentário adota a competência integral para as receitas públicas e a caixa estrita para as despesas públicas.
* **D)** O reconhecimento patrimonial de uma obrigação pública subordina-se à emissão prévia de autorização de saque pelo Tesouro Estadual.
* **E)** O fato gerador da despesa coincide obrigatoriamente com o ato administrativo da fixação orçamentária anual constante da LOA.

> **Comentário Detalhado:**
>
> - **A)** Correta. Sob o enfoque **patrimonial**, aplica-se o regime de competência tanto para receitas (VPA) quanto para despesas (VPD): a VPD deve ser reconhecida no momento em que ocorre o fato gerador (ex.: consumo de material, prestação do serviço ou fruição do trabalho), independentemente do estágio orçamentário.
> - **B)** Incorreta. Sob o enfoque orçamentário (art. 35, I da Lei nº 4.320/1964), a receita orçamentária é reconhecida no momento da arrecadação (regime de caixa orçamentário).
> - **C)** Incorreta. O art. 35 da Lei nº 4.320/1964 prevê regime de caixa para as receitas e competência para as despesas no orçamento (regime misto orçamentário).
> - **D)** Incorreta. As obrigações patrimoniais surgem com o fato gerador, independentemente de saques financeiros.
> - **E)** Incorreta. A fixação apenas autoriza o limite de gasto; não gera fato patrimonial.
> 
> **Gabarito: A**

---

"""

    # Q07: Após 2.2 Variações Resultantes vs Independentes da Execução Orçamentária (antes de ### 3.)
    q07 = """### Questão 07 (FCC - Adaptada / TCE-PI - Auditor de Controle Externo)
Na Contabilidade Pública, as Variações Patrimoniais classificam-se quanto ao impacto sobre a situação líquida (qualitativas vs. quantitativas) e quanto à vinculação ao orçamento (resultantes vs. independentes da execução orçamentária).

Constitui uma Variação Patrimonial Diminutiva (VPD) **independente da execução orçamentária**:

* **A)** O reconhecimento mensal do encargo de depreciação do ativo imobilizado e a baixa de bens públicos em razão de sinistro/inutilização.
* **B)** O pagamento de salários e vencimentos aos servidores públicos estaduais mediante empenho ordinário.
* **C)** A aquisição de veículos novos mediante licitação e pagamento com recursos correntes.
* **D)** A contratação de serviços de consultoria técnica especializada com nota de empenho global.
* **E)** A amortização do principal da dívida pública contratual de longo prazo.

> **Comentário Detalhado:**
>
> - **A)** Correta. A depreciação, amortização, exaustão, perecimento de bens, sinistros e perdas por redução ao valor recuperável (*impairment*) constituem VPDs que afetam negativamente a situação patrimonial líquida **sem envolver execução de dotação orçamentária**, sendo, portanto, VPDs independentes da execução orçamentária.
> - **B)** Incorreta. Despesa com pessoal afeta o patrimônio, mas é resultante da execução orçamentária.
> - **C)** Incorreta. Aquisição de veículos é variação qualitativa (troca de caixa por imobilizado).
> - **D)** Incorreta. Serviços prestados são VPDs resultantes da execução do orçamento.
> - **E)** Incorreta. Amortização é fato permutativo (baixa de passivo com baixa de caixa).
> 
> **Gabarito: A**

---

"""

    # Q08: Após 3.3 Ativos que NÃO Sofrem Depreciação Periódica (antes de ### 4.)
    q08 = """### Questão 08 (FCC - Adaptada / TCE-SC - Auditor de Controle Externo)
Segundo as disposições do MCASP e da NBC TSP 07 (Ativo Imobilizado), a depreciação de um bem público:

* **A)** Deve iniciar-se no momento em que o ativo estiver disponível para uso, no local e nas condições necessárias para operar da forma pretendida pela administração, e não cessa quando o ativo se torna ocioso.
* **B)** Inicia-se unicamente após a quitação total da última fatura emitida pelo fornecedor da obra ou equipamento.
* **C)** É calculada sobre o valor original total do bem, sendo expressamente proibida a dedução de qualquer valor residual na fórmula de cálculo.
* **D)** Aplica-se compulsoriamente a todos os terrenos e obras de arte de acervos públicos históricos.
* **E)** Interrompe-se temporariamente sempre que o órgão público entrar em recesso administrativo parlamentar ou judiciário.

> **Comentário Detalhado:**
>
> - **A)** Correta. A depreciação de um ativo inicia-se quando ele está disponível para uso (instalado e pronto para operar). A depreciação não cessa quando o ativo se torna ocioso ou é retirado temporariamente de uso, a menos que o ativo esteja totalmente depreciado.
> - **B)** Incorreta. A depreciação vincula-se à disponibilidade operacional do ativo, e não a liquidações financeiras.
> - **C)** Incorreta. A base depreciável é exatamente o valor contábil deduzido do **valor residual** estimado.
> - **D)** Incorreta. Terrenos têm vida útil indefinida e obras de arte/acervos históricos raramente depreciam, estando dispensados de depreciação.
> - **E)** Incorreta. Recessos administrativos não paralisam a perda temporal de valor do ativo.
> 
> **Gabarito: A**

---

"""

    # Q09 e Q10: Após 4.2 Reconhecimento Contábil da Perda e Reversões (antes de ## 🌐 Fontes Oficiais & Manuais Técnicos Recomendados)
    q09_10 = """### Questão 09 (FCC - Adaptada / SEFAZ-PE - Auditor Fiscal do Tesouro Estadual)
Em relação ao Teste de Redução ao Valor Recuperável (*Impairment Test*), disciplinado pela NBC TSP 09 (Ativos Não Geradores de Caixa) e NBC TSP 10 (Ativos Geradores de Caixa), é correto afirmar:

* **A)** Se o valor recuperável de um ativo for inferior ao seu valor contábil líquido, o valor contábil do ativo deve ser reduzido ao seu valor recuperável, reconhecendo-se essa redução imediatamente como Variação Patrimonial Diminutiva (VPD).
* **B)** O teste de recuperabilidade é aplicável exclusivamente a empresas estatais dependentes, sendo os órgãos da Administração Direta dispensados de aferir perdas patrimoniais.
* **C)** Uma perda por redução ao valor recuperável reconhecida em períodos anteriores para um ativo jamais poderá ser revertida em exercícios futuros.
* **D)** O valor recuperável de um ativo não gerador de caixa corresponde unicamente ao valor líquido de venda no mercado de leilões públicos.
* **E)** A constatação de obsolescência tecnológica relevante de um equipamento de TI não constitui indício para realização do teste de redução ao valor recuperável.

> **Comentário Detalhado:**
>
> - **A)** Correta. A regra matriz do *impairment* estabelece: constatado que o valor recuperável (maior entre valor justo líquido de despesas de venda e valor em uso) é inferior ao valor contábil líquido, a entidade deve reconhecer perda por desvalorização (VPD) e conta retificadora do ativo.
> - **B)** Incorreta. Aplica-se a todas as entidades do setor público abrangidas pelas NBC TSP.
> - **C)** Incorreta. As normas preveem a reversão de perdas por *impairment* caso as estimativas que fundamentaram a redução tenham se alterado favoravelmente em períodos posteriores.
> - **D)** Incorreta. O valor recuperável é o maior entre o valor justo menos custos de venda e o valor em uso (potencial de serviços remanescente).
> - **E)** Incorreta. A obsolescência tecnológica ou física é indício explícito para a aplicação obrigatória do teste.
> 
> **Gabarito: A**

---

### Questão 10 (FCC - Adaptada / TCE-GO - Analista de Controle Externo)
Determinado órgão público estadual efetuou a aquisição de um imóvel no valor de R$ 5.000.000,00 mediante regular processo licitatório, efetuando o pagamento à vista através de ordem bancária vinculada a dotação de despesa de capital (GND 4 - Investimentos).

Sob o enfoque estritamente patrimonial da Contabilidade Pública, essa transação corresponde a:

* **A)** Uma variação patrimonial qualitativa (ou permutativa), que não acarreta alteração no montante do patrimônio líquido do órgão, ocorrendo apenas permuta entre elementos do ativo (redução de caixa e aumento do ativo imobilizado).
* **B)** Uma variação patrimonial diminutiva quantitativa, reduzindo imediatamente o patrimônio líquido da entidade em R$ 5.000.000,00.
* **C)** Uma variação patrimonial aumentativa orçamentária pura, que eleva o superávit financeiro do exercício.
* **D)** Um fato contábil misto aumentativo, pois os imóveis públicos não se desvalorizam economicamente.
* **E)** Um ato potencial ativo a ser escriturado apenas nas classes 7 e 8 do PCASP.

> **Comentário Detalhado:**
>
> - **A)** Correta. A aquisição de bens do ativo imobilizado (bens de capital) com recursos do ativo circulante (disponibilidades) constitui **fato contábil permutativo (variação qualitativa)**: altera a composição qualitativa do patrimônio (sai dinheiro do banco e entra imóvel no imobilizado), mantendo inalterado o valor do Patrimônio Líquido.
> - **B)** Incorreta. Não há redução do Patrimônio Líquido, pois o Estado recebeu um ativo de valor equivalente.
> - **C)** Incorreta. Não gerou aumento de PL nem receita patrimonial.
> - **D)** Incorreta. Não se trata de fato misto, mas permutativo puro no momento da aquisição.
> - **E)** Incorreta. É fato contábil patrimonial efetivo, registrado nas classes 1 (Ativo).
> 
> **Gabarito: A**

---

"""

    anchor_2 = "### 2. Variações Patrimoniais: Classificações e Origens"
    anchor_3 = "### 3. Procedimentos Patrimoniais Aplicados ao Ativo Imobilizado"
    anchor_4 = "### 4. Teste de Redução ao Valor Recuperável de Ativos (*Impairment Test*)"
    anchor_fontes = "## 🌐 Fontes Oficiais & Manuais Técnicos Recomendados"

    text = text.replace(anchor_2, q06 + "\n" + anchor_2)
    text = text.replace(anchor_3, q07 + "\n" + anchor_3)
    text = text.replace(anchor_4, q08 + "\n" + anchor_4)
    text = text.replace(anchor_fontes, q09_10 + "\n" + anchor_fontes)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
    print("Enriched File 20/02 successfully! Total: 10 questions.")


# ==========================================
# ARQUIVO 03: 03_pcasp_estrutura_e_lancamentos_contabeis.md
# ==========================================
def enrich_file_03():
    filepath = os.path.join(BASE_DIR, "03_pcasp_estrutura_e_lancamentos_contabeis.md")
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    if "### Questão 06" in text:
        print("File 03 already enriched.")
        return

    # Q06: Após 1.2 Os Atributos P/F das Contas Contábeis (antes de ### 2.)
    q06 = """### Questão 06 (FCC - Adaptada / Analista Contábil)
No Plano de Contas Aplicado ao Setor Público (PCASP), as contas contábeis do ativo e do passivo recebem atributos que identificam sua natureza e vinculação orçamentária e financeira, destacando-se o atributo **F/P** (Financeiro / Permanente).

A esse respeito, é correto afirmar:

* **A)** O atributo Financeiro (F) indica que a conta compreende créditos e obrigações cuja arrecadação ou pagamento independe de autorização orçamentária, servindo de base para a apuração do superávit financeiro da Lei nº 4.320/1964.
* **B)** O atributo Permanente (P) é atribuído exclusivamente às contas bancárias que integram a Conta Única do Tesouro Nacional.
* **C)** Todas as contas do patrimônio líquido recebem o atributo financeiro para possibilitar a imediata liquidação de passivos contingentes.
* **D)** O atributo financeiro e permanente foi totalmente extinto pelas normas internacionais de contabilidade (IPSAS), sendo vedada sua utilização pelo PCASP.
* **E)** As disponibilidades de caixa possuem atributo permanente por estarem vinculadas às leis orçamentárias futuras.

> **Comentário Detalhado:**
>
> - **A)** Correta. O art. 105 da Lei nº 4.320/1964 e o PCASP definem: o **Atributo Financeiro (F)** identifica as contas do Ativo e Passivo Financeiro cujas entradas ou saídas financeiras independem de autorização orçamentária ou decorrem de saldos orçamentários já autorizados (ex.: caixa, bancos, restos a pagar, depósitos de terceiros). Essas contas alimentam a apuração do superávit financeiro do art. 43, § 2º. O **Atributo Permanente (P)** identifica bens, créditos e obrigações que dependem de autorização orçamentária para alienação ou quitação de longo prazo.
> - **B)** Incorreta. Contas bancárias e disponibilidades recebem atributo Financeiro (F).
> - **C)** Incorreta. O atributo F/P aplica-se ao Ativo (Classe 1) e Passivo (Classe 2), não ao Patrimônio Líquido.
> - **D)** Incorreta. O PCASP manteve obrigatoriamente os atributos F/P para compatibilizar o balanço patrimonial com a Lei nº 4.320/1964.
> - **E)** Incorreta. Caixa e bancos são a expressão máxima do atributo financeiro.
> 
> **Gabarito: A**

---

"""

    # Q07: Após 2.2 Detalhamento Federativo vs Especificidades do Ente (antes de ### 3.)
    q07 = """### Questão 07 (FCC - Adaptada / TCE-PI - Auditor de Controle Externo)
A estrutura codificada das contas contábeis no PCASP é padronizada nacionalmente pela Secretaria do Tesouro Nacional (STN) em níveis de desdobramento.

Sobre a estrutura padronizada das contas no PCASP, assinale a opção correta:

* **A)** Os primeiros níveis da codificação (Classe, Grupo, Subgrupo e Título) são de padronização nacional e de adoção obrigatória por todos os entes da Federação (União, Estados, DF e Municípios).
* **B)** Cada Estado e Município é livre para alterar a numeração das Classes de contas, podendo designar a Classe 1 para Despesas e a Classe 2 para Receitas.
* **C)** O PCASP é facultativo para os Tribunais de Contas e órgãos do Poder Judiciário, que podem utilizar planos de contas próprios do direito privado.
* **D)** O código da conta no PCASP possui 3 dígitos decimais no padrão internacional das normas IFRS.
* **E)** Os níveis de Subtítulo e Item de detalhamento não admitem nenhuma adaptação ou criação de contas pelas entidades federadas.

> **Comentário Detalhado:**
>
> - **A)** Correta. A estrutura federativa do PCASP padroniza obrigatoriamente os níveis superiores (Classe, Grupo, Subgrupo, Título e Subtítulo) para assegurar a comparabilidade nacional e a consolidação das contas públicas (BSN e SICONFI).
> - **B)** Incorreta. As Classes 1 a 8 são rígidas e imutáveis em todo o território nacional.
> - **C)** Incorreta. O PCASP é de adoção compulsória por todos os Poderes e órgãos de todas as esferas federativas.
> - **D)** Incorreta. O código estruturado do PCASP é composto por 7 níveis padronizados (`X.X.X.X.X.XX.XX`).
> - **E)** Incorreta. Os níveis inferiores mais analíticos podem ser detalhados pelos entes conforme suas peculiaridades de controle.
> 
> **Gabarito: A**

---

"""

    # Q08: Após 3.4 Regra da Autonomia e Fechamento das Partidas Dobradas (antes de ### 4.)
    q08 = """### Questão 08 (FCC - Adaptada / TCE-RS - Auditor de Controle Externo)
O PCASP estrutura as contas em três grandes subsistemas contábeis autônomos de informação: **Patrimonial**, **Orçamentário** e **de Controle**.

A respeito do princípio da autonomia dos subsistemas no PCASP, é correto afirmar:

* **A)** O método das partidas dobradas deve ser respeitado internamente em cada um dos subsistemas contábeis, de tal forma que um lançamento a débito em conta de subsistema orçamentário deve ter sua contrapartida a crédito em outra conta do mesmo subsistema orçamentário.
* **B)** É lícito efetuar um débito no subsistema orçamentário (Classe 6) tendo como contrapartida direta um crédito no subsistema patrimonial (Classe 1).
* **C)** O subsistema de controle destina-se unicamente ao registro dos saldos bancários e do ativo disponível.
* **D)** O subsistema patrimonial engloba as Classes 5 e 6 do PCASP para registrar a previsão da receita e fixação da despesa.
* **E)** As contas de compensação do subsistema de controle foram abolidas e substituídas pelo balanço financeiro.

> **Comentário Detalhado:**
>
> - **A)** Correta. A **Regra da Autonomia dos Subsistemas** estabelece que o fechamento das partidas dobradas ocorre dentro de cada subsistema: débitos no subsistema patrimonial fecham com créditos no subsistema patrimonial; débitos no orçamentário fecham com créditos no orçamentário; e débitos no controle fecham com créditos no controle. Jamais se cruza débito de uma classe orçamentária com crédito de classe patrimonial.
> - **B)** Incorreta. Viola frontalmente a regra de autonomia e isolamento dos subsistemas no PCASP.
> - **C)** Incorreta. O subsistema de controle (classes 7 e 8) registra atos potenciais (contratos, garantias, convênios) e controles específicos.
> - **D)** Incorreta. O subsistema patrimonial engloba as Classes 1, 2, 3 e 4. Classes 5 e 6 pertencem ao subsistema orçamentário.
> - **E)** Incorreta. O subsistema de controle (Classes 7 e 8) é amplamente ativo e estruturante no PCASP.
> 
> **Gabarito: A**

---

"""

    # Q09 e Q10: Após 5.4 Escrituração dos Atos Potenciais (antes de ## 🌐 Fontes Oficiais & Manuais Técnicos Recomendados)
    q09_10 = """### Questão 09 (FCC - Adaptada / SEFAZ-SC - Auditor Fiscal da Receita Estadual)
No PCASP, a assinatura de um contrato administrativo formal de obras públicas no valor de R$ 20.000.000,00, antes do início da execução física e financeira, acarreta:

* **A)** Registro obrigatório no subsistema de controle (Classes 7 - Controles Devedores e 8 - Controles Credores), por se tratar de ato potencial passivo que poderá vir a afetar o patrimônio estatal no futuro.
* **B)** Reconhecimento imediato de uma Variação Patrimonial Diminutiva (VPD) no subsistema patrimonial (Classe 3).
* **C)** Lançamento de despesa liquidada a pagar no subsistema orçamentário (Classe 6).
* **D)** Baixa das disponibilidades bancárias na Conta Única do Tesouro Estadual (Classe 1).
* **E)** Nenhum lançamento no sistema contábil, devendo a informação ser arquivada exclusivamente nos autos do processo licitatório.

> **Comentário Detalhado:**
>
> - **A)** Correta. A celebração de contratos administrativos representa **ato potencial** (fato que não afeta o patrimônio de imediato, mas pode gerar direitos ou obrigações futuras). Os atos potenciais são registrados obrigatoriamente no **Subsistema de Controle** (Classes 7 e 8 do PCASP).
> - **B)** Incorreta. A assinatura do contrato ainda não é fato gerador de VPD; o serviço ou obra ainda não foi executado.
> - **C)** Incorreta. Despesa liquidada exige atesto do fornecimento físico do objeto contratado.
> - **D)** Incorreta. Não houve desembolso financeiro no momento da assinatura.
> - **E)** Incorreta. O registro dos contratos em vigor é obrigatório no subsistema de controle do PCASP.
> 
> **Gabarito: A**

---

### Questão 10 (FCC - Adaptada / TCE-GO - Analista de Controle Externo)
Na liquidação da despesa orçamentária decorrente da entrega definitiva de material de consumo recebido e atestado no almoxarifado central, ocorrem lançamentos simultâneos nos seguintes subsistemas do PCASP:

* **A)** No subsistema orçamentário (debita-se despesa empenhada a liquidar e credita-se despesa liquidada a pagar) e no subsistema patrimonial (debita-se estoques no ativo circulante e credita-se fornecedores a pagar no passivo circulante).
* **B)** Apenas no subsistema orçamentário, sendo vedado qualquer lançamento patrimonial antes do pagamento bancário.
* **C)** Exclusivamente no subsistema patrimonial com débito em bancos e crédito em capital social.
* **D)** No subsistema de controle mediante cancelamento da conta única do Tesouro.
* **E)** No subsistema de custos governamentais mediante estorno de provisões fiscais.

> **Comentário Detalhado:**
>
> - **A)** Correta. No estágio da **liquidação**: (1) No *Subsistema Orçamentário* (Classes 5 e 6), a despesa transita de "empenhada a liquidar" para "despesa liquidada a pagar"; (2) No *Subsistema Patrimonial* (Classes 1 e 2), reconhece-se o direito/ativo recebido no almoxarifado (Débito em Estoques / Material de Consumo na Classe 1) em contrapartida da obrigação constituída perante o terceiro (Crédito em Fornecedores a Pagar na Classe 2).
> - **B)** Incorreta. O enfoque patrimonial moderno impõe o reconhecimento imediato do ativo e da obrigação na liquidação.
> - **C)** Incorreta. O pagamento bancário ocorrerá apenas no estágio subsequente do pagamento.
> - **D)** Incorreta. A liquidação não cancela contas do subsistema de controle.
> - **E)** Incorreta. Não se trata de estorno, mas de apropriação regular de ativos de consumo.
> 
> **Gabarito: A**

---

"""

    anchor_2 = "### 2. Estrutura Codificada do PCASP (Sete Níveis de Detalhamento)"
    anchor_3 = "### 3. Os Três Subsistemas de Informação Contábil e Regra da Autonomia"
    anchor_4 = "### 4. As Oito Classes de Contas e a Natureza dos Saldos"
    anchor_fontes = "## 🌐 Fontes Oficiais & Manuais Técnicos Recomendados"

    text = text.replace(anchor_2, q06 + "\n" + anchor_2)
    text = text.replace(anchor_3, q07 + "\n" + anchor_3)
    text = text.replace(anchor_4, q08 + "\n" + anchor_4)
    text = text.replace(anchor_fontes, q09_10 + "\n" + anchor_fontes)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
    print("Enriched File 20/03 successfully! Total: 10 questions.")


# ==========================================
# ARQUIVO 04: 04_demonstracoes_contabeis_mcasp_e_prestacao_de_contas.md
# ==========================================
def enrich_file_04():
    filepath = os.path.join(BASE_DIR, "04_demonstracoes_contabeis_mcasp_e_prestacao_de_contas.md")
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    if "### Questão 06" in text:
        print("File 04 already enriched.")
        return

    # Q06: Após 1.2 Apuração do Resultado Orçamentário (antes de ### 2.)
    q06 = """### Questão 06 (FCC - Adaptada / Analista Contábil)
No Balanço Orçamentário elaborado segundo os ditames da Lei Federal nº 4.320/1964 e as diretrizes do MCASP, o confronto entre as receitas arrecadadas e as despesas empenhadas determina o resultado:

* **A)** Orçamentário do exercício (superávit orçamentário se a receita arrecadada superar a despesa empenhada; déficit orçamentário na hipótese inversa).
* **B)** Financeiro bruto, dispensando-se a consideração das disponibilidades de caixa líquidas do exercício anterior.
* **C)** Patrimonial do exercício, apurado obrigatoriamente pela diferença entre variações ativas e passivas.
* **D)** Nominal primário ajustado pelas metas fiscais da Lei de Diretrizes Orçamentárias.
* **E)** De caixa econômico, desconsiderando-se a existência de créditos suplementares abertos.

> **Comentário Detalhado:**
>
> - **A)** Correta. O **Resultado Orçamentário** no Balanço Orçamentário (art. 102 da Lei nº 4.320/1964) decorre do confronto estrito entre a Receita Realizada (arrecadada) e a Despesa Executada (empenhada). Havendo excesso de receitas arrecadadas sobre as despesas empenhadas, constata-se **Superávit Orçamentário**; caso contrário, **Déficit Orçamentário**.
> - **B)** Incorreta. O resultado financeiro é apurado no Balanço Financeiro ou no confronto do ativo/passivo financeiro do Balanço Patrimonial.
> - **C)** Incorreta. O resultado patrimonial é apurado na DVP (Demonstração das Variações Patrimoniais).
> - **D)** Incorreta. Resultados primário e nominal são indicadores fiscais da LRF demonstrados no RREO e no AMF da LDO.
> - **E)** Incorreta. Créditos orçamentários integram a coluna de dotação autorizada no Balanço Orçamentário.
> 
> **Gabarito: A**

---

"""

    # Q07: Após 2.2 O Fechamento Contábil Obrigatório e a Inscrição de Restos a Pagar (antes de ### 3.)
    q07 = """### Questão 07 (FCC - Adaptada / TCE-PI - Auditor de Controle Externo)
O Balanço Financeiro estruturado pelo art. 103 da Lei Federal nº 4.320/1964 demonstra a receita e a despesa orçamentárias, bem como os recebimentos e pagamentos de natureza extraorçamentária, conjugados com os saldos em espécie provenientes do exercício anterior e os que se transferem para o exercício seguinte.

No Balanço Financeiro, a inscrição de despesas em **Restos a Pagar** do exercício figura como:

* **A)** Ingresso extraorçamentário, para compensar a despesa orçamentária total computada no quadro dos dispêndios e viabilizar o equilíbrio formal das disponibilidades financeiras.
* **B)** Pagamento orçamentário definitivo com redução do saldo de disponibilidades que se transferem para o exercício seguinte.
* **C)** Receita de capital derivada de operações de crédito por antecipação de receita.
* **D)** Variação patrimonial aumentativa independente da execução orçamentária no subsistema patrimonial.
* **E)** Dedução obrigatória das receitas tributárias correntes arrecadadas no exercício.

> **Comentário Detalhado:**
>
> - **A)** Correta. No Balanço Financeiro (art. 103), a despesa orçamentária é computada pelo valor empenhado no lado dos dispêndios. Como nem toda despesa empenhada foi efetivamente desembolsada (paga), o montante empenhado e não pago é inscrito em **Restos a Pagar** e registrado no lado dos **Ingressos Extraorçamentários**; dessa forma, anula-se o efeito contábil do gasto não desembolsado e mantém-se a exatidão matemática do saldo final de caixa.
> - **B)** Incorreta. A inscrição em restos a pagar representa exatamente a ausência do pagamento financeiro no exercício.
> - **C)** Incorreta. Restos a Pagar não são operações de crédito.
> - **D)** Incorreta. Trata-se de fluxo financeiro/orçamentário e não de VPA patrimonial.
> - **E)** Incorreta. Não constitui dedução de tributos.
> 
> **Gabarito: A**

---

"""

    # Q08: Após 4.3 Demonstração das Mutações do Patrimônio Líquido e Notas Explicativas (antes de ### 5.)
    q08 = """### Questão 08 (FCC - Adaptada / TCE-SC - Auditor de Controle Externo)
Na Demonstração dos Fluxos de Caixa (DFC) elaborada pelas entidades do setor público de acordo com a NBC TSP 12 e o MCASP:

* **A)** Os fluxos de caixa devem ser obrigatoriamente segregados em três grandes categorias de atividades: Operacionais, de Investimento e de Financiamento.
* **B)** O método indireto é de uso compulsório no setor público brasileiro, vedando-se a utilização do método direto para apresentação das atividades operacionais.
* **C)** As receitas provenientes de alienação de bens do ativo imobilizado são classificadas no fluxo das atividades de financiamento.
* **D)** O pagamento de juros da dívida pública deve ser classificado compulsoriamente como atividade de investimento.
* **E)** As transferências correntes recebidas da União integram o fluxo de caixa das atividades de financiamento internacional.

> **Comentário Detalhado:**
>
> - **A)** Correta. A NBC TSP 12 e o MCASP padronizam a DFC em três fluxos estruturais: (1) **Atividades Operacionais** (atividades cotidianas de arrecadação de tributos, prestação de serviços e pagamento de pessoal/custeio); (2) **Atividades de Investimento** (aquisição e venda de ativos imobilizados e intangíveis); (3) **Atividades de Financiamento** (obtenção e amortização de empréstimos e financiamentos de longo prazo).
> - **B)** Incorreta. No setor público brasileiro, o MCASP exige a apresentação dos fluxos operacionais pelo **método direto**.
> - **C)** Incorreta. Venda de ativos imobilizados compõe o fluxo das atividades de **investimento**.
> - **D)** Incorreta. Juros e encargos da dívida são classificados nas atividades operacionais (ou financiamento em notas, mas não investimento).
> - **E)** Incorreta. Transferências correntes compõem os fluxos das atividades operacionais.
> 
> **Gabarito: A**

---

"""

    # Q09 e Q10: Após 5.2 Composição Documental Obrigatória (antes de ## 🌐 Fontes Oficiais & Manuais Técnicos Recomendados)
    q09_10 = """### Questão 09 (FCC - Adaptada / TCE-GO - Analista de Controle Externo)
No tocante ao controle externo exercido pelo Tribunal de Contas do Estado de Goiás (TCE-GO) sobre a prestação de contas dos Chefes dos Poderes e gestores públicos, assinale a opção que distingue corretamente Contas de Governo e Contas de Gestão:

* **A)** As Contas de Governo expressam a atuação política e a gestão fiscal macroeconômica do Chefe do Poder Executivo em todo o exercício, sobre as quais o Tribunal de Contas emite Parecer Prévio consultivo para julgamento pelo Poder Legislativo; já as Contas de Gestão referem-se à administração dos recursos pelos ordenadores de despesas e administradores públicos, sendo julgadas técnica e definitivamente pelo próprio Tribunal de Contas.
* **B)** As Contas de Gestão são julgadas pela Assembleia Legislativa estadual, cabendo ao Tribunal de Contas julgar as Contas de Governo do Governador do Estado.
* **C)** O parecer prévio emitido pelo Tribunal de Contas sobre as Contas de Governo vincula categoricamente a Assembleia Legislativa, que não pode rejeitá-lo em nenhuma hipótese.
* **D)** Os ordenadores de despesa de autarquias e fundações estaduais prestam contas diretamente ao Governador do Estado, não se sujeitando à jurisdição do TCE-GO.
* **E)** As Contas de Governo e de Gestão foram unificadas pela Constituição de 1988, devendo todas ser julgadas exclusivamente pelo Tribunal de Justiça do Estado.

> **Comentário Detalhado:**
>
> - **A)** Correta. A distinção clássica do direito financeiro e controle externo (CF/88, art. 71, I e II, e CE-GO): **Contas de Governo** (do Governador/Prefeito): o Tribunal de Contas atua como órgão auxiliar e emite **Parecer Prévio**, cabendo o julgamento político à Casa Legislativa (Assembleia ou Câmara); **Contas de Gestão** (ordenadores de despesa, secretários, dirigentes): o Tribunal de Contas possui jurisdição constitucional própria e emite **julgamento técnico definitivo** (contas regulares, regulares com ressalva ou irregulares), com poder de aplicar multas e imputar débito com eficácia de título executivo.
> - **B)** Invertido. Contas de governo são julgadas pelo Legislativo; contas de gestão pelo Tribunal de Contas.
> - **C)** Incorreta. O parecer prévio do TCE sobre o Governador tem natureza opinativa-técnica, podendo ser acatado ou rejeitado pelo Legislativo.
> - **D)** Incorreta. Todos os ordenadores de despesas da administração indireta sujeitam-se à jurisdição direta do TCE-GO.
> - **E)** Incorreta. A dualidade permanece viva e estruturante no controle externo brasileiro.
> 
> **Gabarito: A**

---

### Questão 10 (FCC - Adaptada / Auditor de Controle Externo)
Na Demonstração das Variações Patrimoniais (DVP) elaborada de acordo com as normas da CASP (NBC TSP e MCASP), o resultado patrimonial do exercício é considerado **deficitário** quando:

* **A)** O total das Variações Patrimoniais Diminutivas (VPD) for superior ao total das Variações Patrimoniais Aumentativas (VPA), reduzindo o patrimônio líquido da entidade.
* **B)** O montante das despesas orçamentárias pagas superar as receitas orçamentárias arrecadadas na Conta Única.
* **C)** O saldo do passivo financeiro for maior do que o ativo financeiro apurado no Balanço Patrimonial.
* **D)** A despesa fixada na Lei Orçamentária Anual não for integralmente liquidada pelos órgãos setoriais.
* **E)** O superávit financeiro do exercício anterior for totalmente consumido pela abertura de créditos adicionais suplementares.

> **Comentário Detalhado:**
>
> - **A)** Correta. A DVP evidencia o resultado econômico do exercício pelo regime de competência. O resultado patrimonial decorre do confronto direto entre Variações Patrimoniais Aumentativas (VPA) e Variações Patrimoniais Diminutivas (VPD). Quando as **VPD superam as VPA**, o resultado é deficitário, reduzindo o Patrimônio Líquido governamental.
> - **B)** Incorreta. Essa comparação traduz resultado financeiro de caixa, não resultado patrimonial de competência.
> - **C)** Incorreta. Esse confronto expressa déficit financeiro apurado no Balanço Patrimonial (art. 43, § 2º da Lei nº 4.320/1964).
> - **D)** Incorreta. A economia de dotações não caracteriza déficit patrimonial na DVP.
> - **E)** Incorreta. Refere-se à utilização de fontes orçamentárias de créditos adicionais.
> 
> **Gabarito: A**

---

"""

    anchor_2 = "### 2. Balanço Financeiro (BF - Art. 103 da Lei nº 4.320/1964)"
    anchor_3 = "### 3. Balanço Patrimonial (BP - Art. 105 da Lei nº 4.320/1964 e NBC TSP 11)"
    anchor_5 = "### 5. Prestação de Contas ao Tribunal de Contas (TCE-GO)"
    anchor_fontes = "## 🌐 Fontes Oficiais & Manuais Técnicos Recomendados"

    text = text.replace(anchor_2, q06 + "\n" + anchor_2)
    text = text.replace(anchor_3, q07 + "\n" + anchor_3)
    text = text.replace(anchor_5, q08 + "\n" + anchor_5)
    text = text.replace(anchor_fontes, q09_10 + "\n" + anchor_fontes)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
    print("Enriched File 20/04 successfully! Total: 10 questions.")


if __name__ == "__main__":
    enrich_file_01()
    enrich_file_02()
    enrich_file_03()
    enrich_file_04()
    print("Module 20 fully processed!")
