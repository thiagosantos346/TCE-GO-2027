# -*- coding: utf-8 -*-
"""
Enriquecedor Módulo 19 - Noções de Administração Financeira e Orçamentária
Adiciona de 5 a 6 questões por arquivo (Questões 06 a 10/11) no padrão rigoroso FCC / Anti-spoiler.
"""

import os
import re

BASE_DIR = "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/19_nocoes_de_administracao_financeira_e_orcamentaria"

# ==========================================
# ARQUIVO 01: 01_orcamento_publico_principios_e_ciclo_ppa_ldo_loa.md
# ==========================================
def enrich_file_01():
    filepath = os.path.join(BASE_DIR, "01_orcamento_publico_principios_e_ciclo_ppa_ldo_loa.md")
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    # Se já foi enriquecido, pula
    if "### Questão 06" in text:
        print("File 01 already enriched.")
        return

    # Q06: Após 1.2 Modelos Orçamentários e Comparativo Evolutivo (antes de ### 2.)
    q06 = """### Questão 06 (FCC - Adaptada / Analista de Planejamento e Orçamento)
No processo evolutivo da gestão pública e das finanças governamentais, diferentes técnicas orçamentárias foram desenvolvidas para responder às demandas do Estado. Sobre os modelos e técnicas orçamentárias, assinale a afirmativa INCORRETA:

* **A)** O Orçamento Tradicional ou Clássico caracteriza-se pela ênfase primordial no objeto do gasto e no controle contábil das despesas, prescindindo de um planejamento estruturado de objetivos finalísticos.
* **B)** O Orçamento de Desempenho (ou por Realizações) representou um estágio intermediário em que a ênfase deslocou-se para as coisas que o governo faz, embora ainda dissociado de um planejamento global articulado de longo prazo.
* **C)** O Orçamento Base-Zero (OBZ) adota como premissa a análise e a justificação individualizada de todos os programas a cada ciclo orçamentário, não havendo direitos adquiridos a dotações fixadas no exercício pretérito.
* **D)** O Orçamento-Programa vincula as dotações orçamentárias diretamente a objetivos e metas preestabelecidas, utilizando indicadores sistemáticos para aferição da eficácia e da efetividade das políticas públicas.
* **E)** O Orçamento Incremental fundamenta-se na revisão integral da base orçamentária existente, recusando terminantemente a aplicação de índices marginais ou percentuais de reajuste automático sobre os gastos anteriores.

> **Comentário Detalhado:**
>
> - **A)** Correta. O orçamento tradicional/clássico priorizava estritamente o objeto do gasto (insumos/compras) e o controle contábil-legalista.
> - **B)** Correta. O orçamento de desempenho focava no que a administração realizava, mas carecia de conexão integrada com o planejamento governamental global.
> - **C)** Correta. No OBZ (criado por Peter Pyhrr), inexiste direito a dotações passadas; cada pacote de decisão é reavaliado a partir da estaca zero.
> - **D)** Correta. O orçamento-programa é o instrumento contemporâneo que articula planejamento, programas de trabalho e mensuração de resultados.
> - **E)** Incorreta. O orçamento incremental baseia-se justamente na preservação da base de gastos anterior e aplicação de ajustes marginais (na margem), sem rever criticamente as ações continuadas.
> 
> **Gabarito: E**

---

"""

    # Q07: Após 2.7 Princípios do Equilíbrio, Legalidade, Clareza e Publicidade (antes de ### 3.)
    q07 = """### Questão 07 (FCC - Adaptada / TCE-SC - Auditor de Controle Externo)
A respeito dos princípios orçamentários consagrados na legislação de finanças públicas brasileira (Lei nº 4.320/1964 e CF/88), analise as proposições a seguir:

I. O princípio da universalidade preceitua que a Lei Orçamentária Anual deve conter todas as receitas e todas as despesas de todos os Poderes, órgãos, entidades, fundos e fundações instituídas e mantidas pelo Poder Público.  
II. O princípio do orçamento bruto veda a inclusão no orçamento de deduções de despesas de arrecadação das receitas, devendo estas figurar pelas importâncias globais arrecadadas.  
III. O princípio da unidade ou totalidade admite a existência formal de três leis orçamentárias autônomas e independentes em cada exercício financeiro: o orçamento fiscal, o orçamento da seguridade social e o orçamento de investimentos.

Está correto o que se afirma em:

* **A)** I, apenas.
* **B)** I e II, apenas.
* **C)** II e III, apenas.
* **D)** I e III, apenas.
* **E)** I, II e III.

> **Comentário Detalhado:**
>
> - **I. Correto.** O art. 2º da Lei nº 4.320/1964 e o art. 165, § 5º da CF/88 consagram a universalidade: a LOA abrange a totalidade das receitas e despesas de todos os Poderes e esferas orçamentárias.
> - **II. Correto.** O art. 6º da Lei nº 4.320/1964 estabelece o princípio do orçamento bruto: vedada qualquer dedução preliminar sobre receitas e despesas.
> - **III. Incorreto.** O princípio da unidade/totalidade exige que o orçamento seja uno para cada esfera governamental. O orçamento fiscal, da seguridade social e de investimentos compõem **uma única lei anual** (LOA), dividida em três peças orçamentárias integradas, e não três leis autônomas.
> 
> **Gabarito: B**

---

"""

    # Q08: Após 3.3 Lei Orçamentária Anual (antes de ### 4.)
    q08 = """### Questão 08 (FCC - Adaptada / Analista de Gestão Pública)
A Lei de Diretrizes Orçamentárias (LDO), concebida pela Carta Magna de 1988 e substancialmente fortalecida pela Lei de Responsabilidade Fiscal (LC nº 101/2000), desempenha papel fundamental no equilíbrio fiscal da Administração Pública. Sobre os anexos obrigatórios que integram o projeto da LDO, é correto afirmar:

* **A)** O Anexo de Metas Fiscais define metas anuais para receitas, despesas, montante da dívida pública, resultado nominal e resultado primário para o exercício a que se referir e para os dois seguintes.
* **B)** O Anexo de Riscos Fiscais é elaborado exclusivamente pela União, sendo os Estados, DF e Municípios dispensados de demonstrar passivos contingentes e riscos orçamentários.
* **C)** As metas fiscais fixadas na LDO possuem caráter meramente enunciativo e acadêmico, não vinculando as dotações a serem consignadas no projeto de LOA.
* **D)** A reserva de contingência constante da LOA deve ser fixada em percentual livremente escolhido pelo ordenador de despesas, sem parâmetros definidos na LDO.
* **E)** O Anexo de Metas Fiscais contempla unicamente o demonstrativo das despesas com pessoal ativo e inativo de todos os Poderes.

> **Comentário Detalhado:**
>
> - **A)** Correta. O art. 4º, § 1º da LRF estabelece expressamente que integrará o projeto de LDO o Anexo de Metas Fiscais, no qual serão fixadas metas anuais de receitas, despesas, resultados nominal e primário e montante da dívida para o exercício e os dois seguintes (triênio).
> - **B)** Incorreta. O Anexo de Riscos Fiscais é de elaboração compulsória para todos os entes da Federação (União, Estados, DF e Municípios).
> - **C)** Incorreta. As metas fiscais são vinculantes e orientam a elaboração e execução da LOA, servindo de base para eventual limitação de empenho e movimentação financeira.
> - **D)** Incorreta. A destinação e a forma de utilização da reserva de contingência são estipuladas na LDO (art. 5º, III da LRF).
> - **E)** Incorreta. O AMF contempla metas de receita, despesa, resultado nominal, primário e dívida consolidada, com memória e metodologia de cálculo, e não apenas gastos com pessoal.
> 
> **Gabarito: A**

---

"""

    # Q09: Após 4.3 Prazos Constitucionais de Envio e Devolução (antes de ### 5.)
    q09 = """### Questão 09 (FCC - Adaptada / Auditor de Controle Externo)
Acerca do ciclo orçamentário e das competências constitucionais dos Poderes na tramitação da Lei Orçamentária Anual (LOA), assinale a afirmativa correta:

* **A)** O Poder Executivo possui a prerrogativa privativa de iniciativa dos projetos do PPA, da LDO e da LOA, cabendo ao Poder Legislativo a deliberação, apreciação e eventual aprovação ou rejeição de emendas.
* **B)** Caso a proposta da LOA não seja aprovada pelo Congresso Nacional até o encerramento da sessão legislativa, a sessão deve ser suspensa imediatamente e o orçamento anterior é prorrogado tacitamente por mais um exercício completo.
* **C)** É admitida a aprovação de emendas parlamentares individuais ao projeto de LOA que acarretem aumento de despesa global sem indicação dos recursos compensatórios mediante anulação de dotações.
* **D)** As emendas parlamentares impositivas individuais destinadas à saúde podem ser executadas discricionariamente pelo Executivo quando houver superávit primário.
* **E)** A Comissão Mista Permanente de Senadores e Deputados (CMO) examina e emite parecer unicamente sobre o PPA, não tendo competência formal sobre a LOA nem sobre os créditos adicionais.

> **Comentário Detalhado:**
>
> - **A)** Correta. A iniciativa legislativa dos projetos orçamentários (PPA, LDO e LOA) é competência privativa do Chefe do Poder Executivo (art. 165 da CF/88), cabendo ao Legislativo o exame, debate, emendamento e votação.
> - **B)** Incorreta. A não votação da LDO impede a interrupção da sessão legislativa (recesso parlamentar). A não aprovação da LOA autoriza a execução provisória mensal de despesas correntes inadiáveis conforme regras da LDO, jamais a prorrogação tácita do orçamento anterior.
> - **C)** Incorreta. Conforme o art. 166, § 3º da CF/88, as emendas ao projeto de lei orçamentária somente podem ser aprovadas caso indiquem os recursos necessários, admitidos apenas os provenientes de anulação de despesas (excluídas dotações de pessoal, serviço da dívida e transferências tributárias constitucionais).
> - **D)** Incorreta. As emendas individuais têm execução obrigatória (orçamento impositivo), sujeitando-se apenas a contingenciamento proporcional ou impedimentos técnicos formalizados.
> - **E)** Incorreta. A CMO possui competência constitucional expressa para examinar e emitir parecer sobre todos os projetos de PPA, LDO, LOA, créditos adicionais e contas de governo (art. 166, § 1º da CF/88).
> 
> **Gabarito: A**

---

"""

    # Q10 e Q11: Após 5.4 antes de ## 🌐 Fontes Oficiais & Normativas Recomendadas
    q10_11 = """### Questão 10 (FCC - Adaptada / TCE-GO - Analista de Controle Externo)
A respeito do regime constitucional das emendas parlamentares impositivas instituído pelas Emendas Constitucionais nº 86/2015, nº 100/2019 e nº 105/2019, considere a seguinte hipótese fática:

Determinada Assembleia Legislativa estadual aprovou a Lei Orçamentária Anual consignando emendas parlamentares individuais no patamar correspondente a 2% da receita corrente líquida apurada no exercício anterior. Dos recursos destinados por um dos parlamentares mediante a modalidade de Transferência Especial ("Emenda PIX") ao Município Gama, o Chefe do Poder Executivo municipal determinou a aplicação de 40% para pagamento da folha salarial dos servidores da saúde e 60% para aquisição de ambulâncias e pavimentação urbana.

À luz do art. 166-A da CF/88 e das normas de finanças públicas, a destinação dos recursos pelo Prefeito Municipal:

* **A)** É inteiramente regular, pois nas transferências especiais os recursos passam a pertencer ao Município a título de doação livre, podendo ser alocados em qualquer necessidade pública local.
* **B)** É flagrantemente inconstitucional e irregular quanto aos 40% aplicados na folha de pessoal, uma vez que a Constituição veda expressamente o uso de transferências especiais em despesas com pessoal e amortização de dívidas.
* **C)** É irregular no tocante às despesas de capital (ambulâncias e pavimentação), visto que a Constituição exige a aplicação de 100% dos recursos em despesas de custeio corrente.
* **D)** É válida, desde que o Tribunal de Contas do Estado autorize previamente a utilização da transferência especial para fins salariais em regime de urgência.
* **E)** Depende obrigatoriamente de prévia celebração de convênio com o Estado para que a transferência especial possa ser executada validamente pelo Município.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Embora a transferência especial independa de convênio, ela sofre limitações constitucionais materiais rígidas.
> - **B)** Correta. O art. 166-A, § 1º da CF/88 veda terminantemente a destinação de transferências especiais para despesas com pessoal e encargos sociais, bem como encargos do serviço da dívida. Ademais, pelo menos 70% devem ser alocados em despesas de capital.
> - **C)** Incorreta. Pelo menos 70% das transferências especiais devem ser aplicadas em despesas de capital (investimentos/obras), exatamente como a compra de ambulâncias e obras de pavimentação.
> - **D)** Incorreta. O Tribunal de Contas fiscaliza a conformidade da execução e não tem atribuição legal de dispensar vedação constitucional expressa.
> - **E)** Incorreta. A marca distintiva da transferência especial ("PIX") é a dispensa de convênio ou contrato de repasse.
> 
> **Gabarito: B**

---

### Questão 11 (FCC - Adaptada / Analista de Planejamento e Orçamento)
Considere que, na elaboração do projeto de Lei Orçamentária Anual para o exercício subsequente, verificou-se a necessidade de inclusão de ações para atendimento de despesas decorrentes de um programa continuado de fomento regional com duração estimada de 3 (três) anos.

De acordo com o art. 167, § 1º da Constituição Federal de 1988:

* **A)** Nenhum investimento cuja execução ultrapasse um exercício financeiro poderá ser iniciado sem prévia inclusão no Plano Plurianual, ou sem lei que autorize a inclusão, sob pena de crime de responsabilidade.
* **B)** Qualquer investimento plurianual pode ser iniciado desde que autorizado expressamente pela Lei de Diretrizes Orçamentárias, sendo dispensada a menção no PPA.
* **C)** O início de projetos plurianuais independe de autorização em lei, bastando a existência de dotação suficiente na LOA para a primeira parcela.
* **D)** Os investimentos plurianuais subordinam-se unicamente ao limite da capacidade de endividamento da Lei de Responsabilidade Fiscal, sendo prescindível a programação orçamentária.
* **E)** Apenas as obras públicas financiadas por empréstimos externos exigem compatibilidade obrigatória com o Plano Plurianual.

> **Comentário Detalhado:**
>
> - **A)** Correta. É a dicção literal do art. 167, § 1º da CF/88: "Nenhum investimento cuja execução ultrapasse um exercício financeiro poderá ser iniciado sem prévia inclusão no plano plurianual, ou sem lei que autorize a inclusão, sob pena de crime de responsabilidade".
> - **B)** Incorreta. A exigência é de inclusão no PPA (ou lei específica de alteração do PPA), não bastando a LDO.
> - **C)** Incorreta. A CF/88 veda taxativamente o início do investimento plurianual sem previsão no PPA, configurando crime de responsabilidade.
> - **D)** Incorreta. A compatibilidade com o PPA é imperativo constitucional formal inegociável.
> - **E)** Incorreta. Aplica-se a todo e qualquer investimento cuja execução ultrapasse um exercício financeiro, independentemente da fonte de recursos.
> 
> **Gabarito: A**

---

"""

    # Inserções
    anchor_2 = "### 2. Princípios Orçamentários: O Núcleo Normativo e Doutrinário"
    anchor_3 = "### 3. O Sistema Orçamentário Constitucional: PPA, LDO e LOA"
    anchor_4 = "### 4. Ciclo Orçamentário e Processo Legislativo Orçamentário"
    anchor_5 = "### 5. Emendas Parlamentares e o Regime do Orçamento Impositivo"
    anchor_fontes = "## 🌐 Fontes Oficiais & Normativas Recomendadas"

    text = text.replace(anchor_2, q06 + "\n" + anchor_2)
    text = text.replace(anchor_3, q07 + "\n" + anchor_3)
    text = text.replace(anchor_4, q08 + "\n" + anchor_4)
    text = text.replace(anchor_5, q09 + "\n" + anchor_5)
    text = text.replace(anchor_fontes, q10_11 + "\n" + anchor_fontes)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
    print("Enriched File 01 successfully! Total: 11 questions.")


# ==========================================
# ARQUIVO 02: 02_receita_publica_estagios_fontes_e_classificacoes.md
# ==========================================
def enrich_file_02():
    filepath = os.path.join(BASE_DIR, "02_receita_publica_estagios_fontes_e_classificacoes.md")
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    if "### Questão 06" in text:
        print("File 02 already enriched.")
        return

    # Q06: Após 2.3 O Princípio da Unidade de Caixa (antes de ### 3.)
    q06 = """### Questão 06 (FCC - Adaptada / Analista de Planejamento e Orçamento)
No tocante ao estágio da arrecadação e ao princípio da unidade de caixa na execução orçamentária das receitas públicas (art. 56 da Lei nº 4.320/1964), assinale a afirmativa correta:

* **A)** O recolhimento de todas as receitas far-se-á em estrita observância ao princípio de unidade de tesouraria, vedando-se a fragmentação de disponibilidades governamentais em contas bancárias descentralizadas sem autorização legal.
* **B)** A arrecadação confunde-se juridicamente com o recolhimento, ocorrendo ambos simultaneamente quando o contribuinte entrega o valor à instituição bancária credenciada.
* **C)** É facultado às autarquias manterem receitas públicas sob a guarda de cofres particulares, dispensando-se a transferência para a Conta Única do Tesouro.
* **D)** As receitas vinculadas a fundos especiais não se sujeitam à unidade de caixa, devendo seus recursos permanecerem fora do sistema bancário oficial.
* **E)** O recolhimento consiste no ato pelo qual os agentes arrecadadores entregam os recursos aos agentes fiscais para conferência manual antes do depósito no Tesouro.

> **Comentário Detalhado:**
>
> - **A)** Correta. O art. 56 da Lei nº 4.320/1964 consagra o princípio da unidade de tesouraria (unidade de caixa): todas as receitas devem ser recolhidas à conta única do Tesouro, vedada a dispersão não autorizada por lei.
> - **B)** Incorreta. Arrecadação é a entrega dos valores pelo contribuinte aos agentes arrecadadores (bancos); recolhimento é a transferência desses valores arrecadados para a Conta Única do Tesouro.
> - **C)** Incorreta. É absolutamente vedada a custódia particular de dinheiros públicos.
> - **D)** Incorreta. Os recursos de fundos especiais sujeitam-se à unidade de caixa, sendo geridos em subcontas vinculadas dentro da Conta Única.
> - **E)** Incorreta. O recolhimento é a efetiva transferência bancária dos valores arrecadados para a Conta Única do Tesouro.
> 
> **Gabarito: A**

---

"""

    # Q07: Após 3.4 Classificação por Natureza da Receita (antes de ### 4.)
    q07 = """### Questão 07 (FCC - Adaptada / TCE-PI - Auditor de Controle Externo)
Segundo a classificação por categoria econômica estabelecida pela Lei Federal nº 4.320/1964 e pelo Manual de Contabilidade Aplicada ao Setor Público (MCASP), constituem, respectivamente, Receita Corrente e Receita de Capital:

* **A)** Receita Patrimonial decorrente de aluguéis de imóveis públicos e Receita decorrente de Alienação de Bens Imóveis.
* **B)** Amortização de Empréstimos concedidos e Receita Tributária proveniente de impostos sobre patrimônio.
* **C)** Operações de Crédito de longo prazo e Receita de Serviços prestados pelo ente estatal.
* **D)** Alienação de Bens Móveis inservíveis e Receita de Contribuições Sociais.
* **E)** Transferências de Capital recebidas para obras e Receita Agropecuária decorrente de produção própria.

> **Comentário Detalhado:**
>
> - **A)** Correta. A Receita Patrimonial (aluguéis, dividendos, juros recebidos) é Receita Corrente (art. 11, § 1º); a Alienação de Bens Imóveis/Móveis é típica Receita de Capital (art. 11, § 2º da Lei nº 4.320/1964).
> - **B)** Invertido. Amortização de empréstimos concedidos é Capital; receita tributária é Corrente.
> - **C)** Invertido. Operações de crédito são Capital; serviços são Correntes.
> - **D)** Invertido. Alienação de bens é Capital; contribuições são Correntes.
> - **E)** Invertido. Transferências de capital são Capital; agropecuária é Corrente.
> 
> **Gabarito: A**

---

"""

    # Q08: Após 3.4 (Segunda questão sobre classificação)
    q08 = """### Questão 08 (FCC - Adaptada / TCE-RS - Auditor de Controle Externo)
A classificação por natureza da receita orçamentária é estruturada em 8 (oito) dígitos decimais padronizados nacionalmente pela SOF e STN. Considere o código de natureza de receita `1.3.2.1.01.1.1`:

O primeiro dígito "1" e o segundo dígito "3" identificam, na estrutura oficial, respectivamente:

* **A)** Categoria Econômica (Receitas Correntes) e Origem da Receita (Receita Patrimonial).
* **B)** Origem da Receita (Receitas Tributárias) e Espécie da Receita (Taxas).
* **C)** Subdivisão de Recursos e Vinculação Constitucional de Impostos.
* **D)** Categoria Econômica (Receitas de Capital) e Tipo de Receita (Principal).
* **E)** Esfera Orçamentária e Identificador de Uso (IDUSO).

> **Comentário Detalhado:**
>
> - **A)** Correta. Na estrutura da natureza da receita (`C.O.E.S.DD.T.P`): o 1º dígito (1) é a **Categoria Econômica** (1 = Receita Corrente; 2 = Receita de Capital); o 2º dígito (3) é a **Origem** (no caso de Correntes: 1-Impostos/Taxas, 2-Contribuições, 3-Patrimonial, 4-Agropecuária, 5-Industrial, 6-Serviços, 7-Transferências Correntes, 9-Outras Receitas Correntes).
> - **B)** Incorreta. O primeiro nível é a categoria econômica, não origem.
> - **C)** Incorreta. Misturou com a classificação por fonte de recursos.
> - **D)** Incorreta. O dígito 1 representa receitas correntes, e não de capital.
> - **E)** Incorreta. Esfera orçamentária e IDUSO não compõem a codificação de natureza da receita.
> 
> **Gabarito: A**

---

"""

    # Q09 e Q10: Após 4.2 antes de ## 🌐 Fontes Oficiais & Manuais Técnicos Recomendados
    q09_10 = """### Questão 09 (FCC - Adaptada / Analista Jurídico de Controle)
O art. 14 da Lei de Responsabilidade Fiscal (LC nº 101/2000) impõe condicionantes rigorosas para a concessão ou ampliação de incentivo ou benefício de natureza tributária da qual resulte renúncia de receita. Sobre o tema, é INCORRETO afirmar:

* **A)** A renúncia compreende anistia, remissão, subsídio, crédito presumido, isenção em caráter não geral, alteração de alíquota ou modificação de base de cálculo que implique redução discriminada de tributos ou contribuições.
* **B)** A concessão do benefício deve estar acompanhada de estimativa do impacto orçamentário-financeiro no exercício em que deva iniciar sua vigência e nos dois seguintes.
* **C)** O proponente deve demonstrar que a renúncia foi considerada na estimativa de receita da lei orçamentária e que não afetará as metas de resultados fiscais previstas no anexo próprio da LDO.
* **D)** É vedada a concessão de renúncia de receita mesmo quando acompanhada de medidas de compensação fiscal mediante elevação de alíquotas ou criação de outro tributo.
* **E)** Se o ato de concessão de renúncia de receita for condicionado a medidas de compensação, o benefício só entrará em vigor quando implementadas as referidas medidas de compensação.

> **Comentário Detalhado:**
>
> - **A)** Correta. Definição expressa constante do art. 14, § 1º da LRF.
> - **B)** Correta. Exigência do caput do art. 14: estimativa trienal do impacto orçamentário-financeiro.
> - **C)** Correta. É uma das alternativas do art. 14, I da LRF (ter sido prevista na LOA e compatível com as metas fiscais).
> - **D)** Incorreta. O art. 14, II admite expressamente a concessão de renúncia se acompanhada de medidas de compensação, no exercício e nos dois seguintes, por meio do aumento de receita proveniente da elevação de alíquotas, ampliação da base de cálculo, majoração ou criação de tributo.
> - **E)** Correta. O art. 14, § 2º da LRF prevê que o benefício só entra em vigor após a efetiva implementação das medidas compensatórias.
> 
> **Gabarito: D**

---

### Questão 10 (FCC - Adaptada / TCE-GO - Auditor de Controle Externo)
Determinado Município goiano realizou a alienação de diversos imóveis públicos de seu patrimônio disponível, arrecadando R$ 10.000.000,00. Visando equilibrar o caixa municipal no final do mandato, o Prefeito enviou projeto de lei autorizando a utilização de 50% desses recursos para pagamento da folha salarial atrasada dos servidores públicos municipais e 50% para obras de pavimentação asfáltica.

À luz do art. 44 da Lei Complementar nº 101/2000 (LRF):

* **A)** A destinação proposta pelo Prefeito é plenamente lícita, pois os recursos provenientes da venda de bens móveis ou imóveis integram a receita livre do ente e podem ser aplicados em qualquer despesa pública.
* **B)** A destinação para pagamento de folha de salários é expressamente vedada pela LRF, configurando nulidade do ato e infração fiscal, sendo a aplicação em pavimentação asfáltica perfeitamente regular por se tratar de despesa de capital.
* **C)** Ambos os gastos propostos são ilícitos, pois a receita de alienação de ativos só pode ser utilizada para aplicação exclusiva no mercado de ações e títulos públicos.
* **D)** É permitido o pagamento de pessoal com receitas de alienação de bens desde que haja autorização prévia por decreto do Governador do Estado.
* **E)** O Município pode utilizar o produto da alienação para despesa de pessoal, desde que o montante não ultrapasse o limite prudencial de gastos da LRF.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O art. 44 da LRF proíbe expressamente a aplicação de receita de capital derivada da alienação de bens no financiamento de despesa corrente.
> - **B)** Correta. O art. 44 da LRF veda terminantemente a aplicação da receita de alienação de ativos em despesas correntes (custeio e pessoal), ressalvadas exclusivamente as destinadas por lei aos regimes de previdência social. As obras de pavimentação constituem investimentos (despesas de capital), destinação perfeitamente legítima.
> - **C)** Incorreta. As despesas de capital (investimentos) são a destinação natural da receita de capital de alienação de ativos.
> - **D)** Incorreta. A vedação é legal e absoluta, não podendo ser suplantada por decreto estadual.
> - **E)** Incorreta. O limite do art. 44 é categórico e independe dos percentuais globais de gasto com pessoal.
> 
> **Gabarito: B**

---

"""

    anchor_3 = "### 3. Classificações da Receita Orçamentária (Lei nº 4.320/1964 e MCASP)"
    anchor_4 = "### 4. Regras Fiscais Restritivas da Receita e a LRF"
    anchor_fontes = "## 🌐 Fontes Oficiais & Manuais Técnicos Recomendados"

    text = text.replace(anchor_3, q06 + "\n" + anchor_3)
    text = text.replace(anchor_4, q07 + "\n" + q08 + "\n" + anchor_4)
    text = text.replace(anchor_fontes, q09_10 + "\n" + anchor_fontes)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
    print("Enriched File 02 successfully! Total: 10 questions.")


# ==========================================
# ARQUIVO 03: 03_despesa_publica_estagios_restos_a_pagar_e_suprimento.md
# ==========================================
def enrich_file_03():
    filepath = os.path.join(BASE_DIR, "03_despesa_publica_estagios_restos_a_pagar_e_suprimento.md")
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    if "### Questão 06" in text:
        print("File 03 already enriched.")
        return

    # Q06: Após 1.2 Os Quatro Estágios da Despesa Pública (antes de 1.3)
    q06 = """### Questão 06 (FCC - Adaptada / Analista de Planejamento e Orçamento)
No tocante ao estágio da liquidação da despesa pública disciplinado nos arts. 62 e 63 da Lei Federal nº 4.320/1964, é correto afirmar:

* **A)** A liquidação consiste na verificação do direito adquirido pelo credor, tendo por base os títulos e documentos comprobatórios do respectivo crédito, com o objetivo de apurar a origem e o objeto do que se deve pagar, a importância exata a pagar e a quem se deve pagar.
* **B)** A emissão da ordem de pagamento precede a liquidação da despesa, servindo de autorização para o recebimento definitivo dos bens adquiridos.
* **C)** É lícito efetuar o pagamento da despesa antes da regular liquidação, desde que haja termo de garantia prestado pelo fornecedor contratado.
* **D)** A nota de empenho substitui integralmente a fase de liquidação quando se tratar de contratação de serviços contínuos com dedicação exclusiva de mão de obra.
* **E)** A liquidação é ato discricionário do ordenador de despesas, que pode dispensá-la quando o fornecedor for órgão integrante da Administração Pública direta.

> **Comentário Detalhado:**
>
> - **A)** Correta. É a literalidade do art. 63 da Lei nº 4.320/1964: "A liquidação da despesa consiste na verificação do direito adquirido pelo credor tendo por base os títulos e documentos comprobatórios do respectivo crédito". Apura: I - a origem e o objeto do que se deve pagar; II - a importância exata a pagar; III - a quem se deve pagar.
> - **B)** Incorreta. A ordem de pagamento é posterior à liquidação (art. 64).
> - **C)** Incorreta. O art. 62 estabelece que a ordem de pagamento só pode ser exarada após regular liquidação da despesa.
> - **D)** Incorreta. O empenho cria a obrigação orçamentária, mas jamais dispensa a liquidação para atestar o fornecimento.
> - **E)** Incorreta. A liquidação é ato vinculado e indispensável na execução da despesa pública.
> 
> **Gabarito: A**

---

"""

    # Q07: Após 2.4 A Distinção Crítica FCC: Investimentos vs Inversões Financeiras (antes de ### 3.)
    q07 = """### Questão 07 (FCC - Adaptada / TCE-PI - Auditor de Controle Externo)
Na classificação da despesa orçamentária por natureza, as despesas de capital dividem-se em três Grupos de Natureza da Despesa (GND): Investimentos (GND 4), Inversões Financeiras (GND 5) e Amortização da Dívida (GND 6).

Constituem, respectivamente, Investimento (GND 4) e Inversão Financeira (GND 5):

* **A)** A construção de um novo edifício para abrigar a sede do Tribunal de Contas e a aquisição de um imóvel já construído para funcionamento de uma escola pública.
* **B)** A aquisição de títulos da dívida pública de outros entes e a pavimentação de uma rodovia estadual.
* **C)** O pagamento do principal da dívida contratual externa e a aquisição de computadores novos para a secretaria de fazenda.
* **D)** A concessão de empréstimos habitacionais e a realização de obras de reforma que ampliem a vida útil de hospital estadual.
* **E)** A aquisição de instalações hospitalares novas e a contratação de serviços de consultoria contábil continuada.

> **Comentário Detalhado:**
>
> - **A)** Correta. Conforme os arts. 12 e 13 da Lei nº 4.320/1964: **Investimentos (GND 4)** englobam obras públicas e aquisições que criam novos bens de capital (aumento líquido do patrimônio público, ex.: construção de novo edifício); **Inversões Financeiras (GND 5)** englobam a aquisição de imóveis ou de bens de capital já em utilização (apenas transferem patrimônio entre agentes sem criar novo ativo na economia, ex.: compra de prédio já construído), além de aquisição de títulos e constituição/aumento de capital de empresas.
> - **B)** Invertido. Títulos da dívida são inversões financeiras; rodovia é investimento.
> - **C)** Amortização da dívida é GND 6; computadores novos são GND 4 (investimento).
> - **D)** Invertido. Empréstimos são GND 5; reforma ampliativa é GND 4.
> - **E)** Instalações novas são GND 4; serviços continuados são GND 3 (outras despesas correntes).
> 
> **Gabarito: A**

---

"""

    # Q08: Após 3.3 As Três Hipóteses Legais de DEA (antes de ### 4.)
    q08 = """### Questão 08 (FCC - Adaptada / TCE-SC - Auditor de Controle Externo)
A respeito do reconhecimento e pagamento de Despesas de Exercícios Anteriores (DEA), disciplinadas pelo art. 37 da Lei Federal nº 4.320/1964 e normas correlatas, analise as hipóteses a seguir:

I. Despesas de exercícios encerrados para os quais o orçamento respectivo consignava crédito próprio, com saldo suficiente para atendê-las, que não se tenham processado na época própria.  
II. Restos a Pagar com prescrição interrompida, a respeito dos quais o credor tenha mantido tempestivamente o direito de cobrança.  
III. Compromissos decorrentes de obrigação de pagamento criada em virtude de lei e pela mesma promulgada, que não tenham sido previstos no orçamento anterior.

À luz da legislação de finanças públicas, podem ser pagas à conta de dotação orçamentária específica para Despesas de Exercícios Anteriores (DEA):

* **A)** I, apenas.
* **B)** I e II, apenas.
* **C)** II e III, apenas.
* **D)** I e III, apenas.
* **E)** I, II e III.

> **Comentário Detalhado:**
>
> - **I. Correto.** É a primeira hipótese do art. 37 da Lei nº 4.320/1964: despesas que tinham dotação orçamentária e saldo suficiente, mas não foram empenhadas na época própria.
> - **II. Correto.** É a segunda hipótese do art. 37: Restos a Pagar cancelados cuja prescrição tenha sido regularmente interrompida pelo credor.
> - **III. Correto.** É a terceira hipótese do art. 37: compromissos decorrentes de obrigação legal promulgada após o encerramento do orçamento respectivo.
> 
> **Gabarito: E**

---

"""

    # Q09 e Q10: Após 4.2 antes de ## 🌐 Fontes Oficiais & Manuais Técnicos Recomendados
    q09_10 = """### Questão 09 (FCC - Adaptada / Analista Jurídico de Controle)
O regime de adiantamento ou suprimento de fundos é uma exceção ao princípio geral de que o pagamento de despesas públicas deve ser precedido de regular empenho e liquidação pelo rito ordinário.

A respeito do suprimento de fundos, de acordo com o art. 68 da Lei nº 4.320/1964 e normas gerais de administração financeira, é correto afirmar:

* **A)** O suprimento de fundos dispensa a realização de empenho prévio, formalizando-se diretamente pelo saque financeiro na conta do órgão.
* **B)** É lícito conceder suprimento de fundos a servidor público que seja responsável por dois adiantamentos anteriores já prestados e aprovados pelo Tribunal de Contas.
* **C)** O suprimento de fundos é cabível unicamente para despesas eventuais de pronto pagamento, que exijam pronta prestação de serviço ou aquisições miúdas que não possam subordinar-se ao processo normal de aplicação.
* **D)** O suprido tem prazo indeterminado para prestar contas dos recursos sacados, sujeitando-se apenas ao prazo prescricional decadencial de dez anos.
* **E)** É permitido efetuar adiantamento de suprimento de fundos a servidor em alcance ou que tenha deixado de prestar contas de suprimento anterior no prazo legal.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O suprimento de fundos **exige prévio empenho** na dotação própria da despesa (art. 60 da Lei nº 4.320/1964).
> - **B)** Incorreta. O Decreto nº 93.872/1986 veda expressamente a concessão de novo adiantamento a quem já seja responsável por mais de dois suprimentos de fundos pendentes de aplicação ou a servidor em atraso na prestação de contas.
> - **C)** Correta. O art. 68 da Lei nº 4.320/1964 restringe o regime de suprimento de fundos aos casos excepcionais: despesas miúdas de pronto pagamento, despesas extraordinárias ou urgentes e despesas que exijam sigilo.
> - **D)** Incorreta. O suprido deve prestar contas em prazo estrito (geralmente até 30 dias após o encerramento do período de aplicação), sob pena de imediata instauração de Tomada de Contas Especial.
> - **E)** Incorreta. É vedado expressamente conceder suprimento a servidor em alcance (aquele que não prestou contas no prazo legal ou teve contas desaprovadas).
> 
> **Gabarito: C**

---

### Questão 10 (FCC - Adaptada / TCE-GO - Analista de Controle Externo)
Em relação aos Restos a Pagar (RAP), sua classificação e regras de controle fiscal, considere a seguinte situação fática:

Determinado órgão do Estado empenhou, no exercício de 2024, despesa referente à aquisição de equipamentos de tecnologia. Os equipamentos foram formalmente entregues, atestados pela comissão de recebimento e liquidados pela unidade orçamentária em 20 de dezembro de 2024, mas a ordem bancária de pagamento não pôde ser emitida até 31 de dezembro por razões operacionais de fechamento do sistema bancário.

No encerramento do exercício financeiro de 2024, tal despesa deverá ser inscrita como:

* **A)** Restos a Pagar Processados (RPP), pois a despesa foi devidamente liquidada no exercício financeiro de origem, gerando direito creditório líquido e certo para o contratado.
* **B)** Restos a Pagar Não Processados (RPNP), haja vista que não ocorreu o efetivo desembolso financeiro da quantia devida ao credor.
* **C)** Despesas de Exercícios Anteriores (DEA), extinguindo-se a nota de empenho emitida e exigindo-se nova dotação no exercício seguinte.
* **D)** Dívida Flutuante Insubsistente, devendo ser cancelada sumariamente em atendimento ao princípio da anualidade orçamentária.
* **E)** Encargos Financeiros da Dívida Fundada, visto que sua exigibilidade ultrapassará o término do exercício financeiro.

> **Comentário Detalhado:**
>
> - **A)** Correta. Os **Restos a Pagar Processados (RPP)** são aqueles cuja despesa cumpriu o estágio da liquidação (o credor entregou o bem ou prestou o serviço, tendo seu direito reconhecido e atestado pela Administração), restando unicamente o pagamento.
> - **B)** Incorreta. Os RPNP são aqueles que foram apenas empenhados, mas ainda pendentes de liquidação ao término do exercício.
> - **C)** Incorreta. DEA aplica-se quando não houve empenho ou restos a pagar válidos no exercício respectivo.
> - **D)** Incorreta. A despesa liquidada não pode ser sumariamente cancelada, sob pena de enriquecimento sem causa do Estado.
> - **E)** Incorreta. Restos a Pagar integram a dívida flutuante (curto prazo), e não a dívida fundada/consolidada.
> 
> **Gabarito: A**

---

"""

    anchor_13 = "#### 1.3 Modalidades de Empenho: Ordinário, Estimativo e Global"
    anchor_3 = "### 3. Restos a Pagar (RAP) e Despesas de Exercícios Anteriores (DEA)"
    anchor_4 = "### 4. Regime Excepcional de Suprimento de Fundos (Adiantamento)"
    anchor_fontes = "## 🌐 Fontes Oficiais & Manuais Técnicos Recomendados"

    text = text.replace(anchor_13, q06 + "\n" + anchor_13)
    text = text.replace(anchor_3, q07 + "\n" + anchor_3)
    text = text.replace(anchor_4, q08 + "\n" + anchor_4)
    text = text.replace(anchor_fontes, q09_10 + "\n" + anchor_fontes)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
    print("Enriched File 03 successfully! Total: 10 questions.")


# ==========================================
# ARQUIVO 04: 04_creditos_adicionais_e_divida_publica.md
# ==========================================
def enrich_file_04():
    filepath = os.path.join(BASE_DIR, "04_creditos_adicionais_e_divida_publica.md")
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    if "### Questão 06" in text:
        print("File 04 already enriched.")
        return

    # Q06: Após 1.3 Quadro Comparativo dos Ritos e Vigência (antes de ### 2.)
    q06 = """### Questão 06 (FCC - Adaptada / Analista de Planejamento e Orçamento)
No tocante às três modalidades de créditos adicionais previstas no art. 41 da Lei Federal nº 4.320/1964, considere as seguintes assertivas:

I. Os créditos suplementares destinam-se a reforço de dotação orçamentária já existente na Lei Orçamentária Anual.  
II. Os créditos especiais destinam-se a despesas para as quais não haja dotação orçamentária específica na LOA, criando nova programação de trabalho.  
III. Os créditos extraordinários destinam-se a despesas imprevisíveis e urgentes, em caso de guerra, comoção intestina ou calamidade pública, abertos por medida provisória na União ou decreto do Executivo onde não houver previsão de MP.

Está correto o que se afirma em:

* **A)** I, apenas.
* **B)** I e II, apenas.
* **C)** II e III, apenas.
* **D)** I e III, apenas.
* **E)** I, II e III.

> **Comentário Detalhado:**
>
> - **I. Correto.** Art. 41, I da Lei nº 4.320/1964: suplementares são os destinados a reforço de dotação orçamentária existente.
> - **II. Correto.** Art. 41, II da Lei nº 4.320/1964: especiais são os destinados a despesas para as quais não haja dotação orçamentária específica.
> - **III. Correto.** Art. 41, III da Lei nº 4.320/1964 e art. 167, § 3º da CF/88: extraordinários destinam-se a despesas urgentes e imprevisíveis (guerra, comoção interna ou calamidade pública).
> 
> **Gabarito: E**

---

"""

    # Q07: Após 3.4 Reserva de Contingência e Recursos Decorrentes de Veto (antes de ### 4.)
    q07 = """### Questão 07 (FCC - Adaptada / TCE-RS - Auditor de Controle Externo)
O art. 43 da Lei Federal nº 4.320/1964 disciplina as fontes de recursos disponíveis que podem ser utilizadas pelo Poder Público para a abertura de créditos suplementares e especiais.

Considera-se **superávit financeiro**, para fins de abertura de créditos adicionais:

* **A)** A diferença positiva entre o ativo financeiro e o passivo financeiro, conjugando-se, ainda, os saldos dos créditos adicionais transferidos e as operações de crédito a eles vinculadas, apurados no Balanço Patrimonial do exercício anterior.
* **B)** O excesso de arrecadação acumulado mês a mês no exercício financeiro corrente, sem dedução das parcelas já comprometidas com créditos suplementares.
* **C)** A economia de despesa decorrente de compras públicas adjudicadas por valores inferiores ao preço de referência do edital licitatório.
* **D)** O saldo positivo apurado na Demonstração das Variações Patrimoniais (DVP) decorrente de doações de bens imóveis recebidos pelo Estado.
* **E)** O total das disponibilidades de caixa existentes na Conta Única do Tesouro no último dia útil de cada quadrimestre fiscal.

> **Comentário Detalhado:**
>
> - **A)** Correta. Nos precisos termos do art. 43, § 2º da Lei nº 4.320/1964: "Entende-se por superávit financeiro a diferença positiva entre o ativo financeiro e o passivo financeiro, conjugando-se, ainda, os saldos dos créditos adicionais transferidos e as operações de crédito a eles vinculadas". É apurado no Balanço Patrimonial do exercício encerrado.
> - **B)** Incorreta. Conceito referente a excesso de arrecadação (art. 43, § 3º), e não superávit financeiro.
> - **C)** Incorreta. Economia de despesa em compras não constitui fonte de créditos adicionais na Lei nº 4.320/1964.
> - **D)** Incorreta. Variação patrimonial aumentativa em bens imóveis afeta o patrimônio permanente, não gerando liquidez financeira no ativo financeiro.
> - **E)** Incorreta. O superávit financeiro é uma grandeza de balanço patrimonial anual, deduzindo passivos financeiros e saldos de créditos reabertos.
> 
> **Gabarito: A**

---

"""

    # Q08: Segunda questão sobre fontes de créditos
    q08 = """### Questão 08 (FCC - Adaptada / TCE-PI - Auditor de Controle Externo)
Na apuração da fonte **excesso de arrecadação** para a abertura de créditos suplementares e especiais (art. 43, § 3º da Lei Federal nº 4.320/1964), a Administração Pública deve obrigatoriamente:

* **A)** Computar a diferença positiva entre a receita arrecadada e a estimada na LOA, considerando a tendência do exercício, deduzindo-se a importância dos créditos extraordinários já abertos no exercício.
* **B)** Desconsiderar qualquer tendência estatística dos meses vincendos e utilizar apenas a arrecadação histórica do exercício financeiro anterior.
* **C)** Deduzir do excesso apurado o valor das dotações orçamentárias anuladas na LOA durante a tramitação parlamentar.
* **D)** Utilizar os recursos exclusivamente se houver prévia autorização judicial proferida em ação direta de inconstitucionalidade.
* **E)** Reabrir compulsoriamente os saldos de créditos suplementares não utilizados no ano anterior antes de apurar novo excesso.

> **Comentário Detalhado:**
>
> - **A)** Correta. Conforme o art. 43, § 3º da Lei nº 4.320/1964: "Entende-se por excesso de arrecadação, para os fins deste artigo, o saldo positivo das diferenças acumuladas mês a mês entre a arrecadação prevista e a realizada, considerando-se, ainda, a tendência do exercício". E o § 4º complementa que do montante devem ser deduzidas as importâncias dos créditos extraordinários abertos no exercício.
> - **B)** Incorreta. A lei exige expressamente considerar a tendência do exercício.
> - **C)** Incorreta. Anulação de dotação é outra fonte autônoma (art. 43, § 1º, III).
> - **D)** Incorreta. Trata-se de procedimento estritamente administrativo-orçamentário.
> - **E)** Incorreta. Créditos suplementares não são passíveis de reabertura no exercício seguinte (apenas especiais e extraordinários com ato nos últimos 4 meses).
> 
> **Gabarito: A**

---

"""

    # Q09 e Q10: Após 4.2 antes de ## 🌐 Fontes Oficiais & Manuais Técnicos Recomendados
    q09_10 = """### Questão 09 (FCC - Adaptada / Analista Jurídico de Controle)
No que tange à disciplina jurídica da Dívida Pública e à distinção entre Dívida Flutuante e Dívida Fundada (Consolidada), assinale a opção correta:

* **A)** A dívida fundada compreende os compromissos de exigibilidade a longo prazo, cujo prazo de amortização seja superior a doze meses, contraídos mediante emissão de títulos ou contratos de mútuo.
* **B)** A dívida flutuante é constituída pelas operações de crédito autorizadas na LOA para financiamento de grandes obras de infraestrutura com amortização em dez anos.
* **C)** Os Restos a Pagar processados e não processados integram a dívida consolidada de longo prazo do ente governamental.
* **D)** As operações de crédito por antecipação de receita orçamentária (ARO) compõem a dívida fundada e podem ser quitadas em até quatro anos.
* **E)** Os depósitos judiciais e cauções sob custódia temporária do Estado são classificados como patrimônio líquido governamental, e não como dívida flutuante.

> **Comentário Detalhado:**
>
> - **A)** Correta. A dívida fundada ou consolidada (art. 29 da LRF e art. 98 da Lei nº 4.320/1964) consiste nas obrigações financeiras assumidas para amortização em prazo superior a 12 meses.
> - **B)** Incorreta. Empréstimos para obras de longo prazo integram a dívida fundada (consolidada), não a flutuante.
> - **C)** Incorreta. Os Restos a Pagar integram formalmente a **Dívida Flutuante** (curto prazo - art. 92 da Lei nº 4.320/1964).
> - **D)** Incorreta. ARO é débito de tesouraria de curto prazo integrante da dívida flutuante, devendo ser liquidada até 10 de dezembro do mesmo exercício.
> - **E)** Incorreta. Depósitos de terceiros e cauções constituem passivos exigíveis de curto prazo e integram a dívida flutuante.
> 
> **Gabarito: A**

---

### Questão 10 (FCC - Adaptada / TCE-GO - Auditor de Controle Externo)
A respeito da vigência e da reabertura de créditos adicionais, a Constituição Federal de 1988 estabelece regra excepcional ao princípio da anualidade orçamentária (art. 167, § 2º).

Considere que, em 20 de outubro de determinado exercício financeiro, o Governador do Estado Alfa abriu um crédito extraordinário por ato próprio, no valor de R$ 50.000.000,00, para atendimento a vítimas de grave calamidade pública. Em 31 de dezembro, verificou-se que apenas R$ 35.000.000,00 haviam sido liquidados e pagos, remanescendo saldo orçamentário não utilizado de R$ 15.000.000,00.

À luz da Carta Magna, no exercício financeiro imediatamente subsequente, o saldo remanescente de R$ 15.000.000,00:

* **A)** Não poderá ser aproveitado sob nenhuma hipótese, extinguindo-se definitivamente com o término do ano civil em estrita observância à anualidade.
* **B)** Poderá ser reaberto, até o limite de seu saldo, mediante decreto do Poder Executivo, sendo incorporado ao orçamento do exercício subsequente e vigendo até o término deste novo exercício.
* **C)** Será convertido automaticamente em Restos a Pagar Processados, independentemente de ter havido empenho ou liquidação.
* **D)** Poderá ser reaberto exclusivamente se a Assembleia Legislativa aprovar novo projeto de PPA que contemple a mesma obra de socorro.
* **E)** Exigirá que o ente estatal contraia operação de crédito por ARO para financiar o montante residual reaberto.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O art. 167, § 2º da CF/88 prevê exceção expressa para créditos especiais e extraordinários abertos nos últimos quatro meses do exercício.
> - **B)** Correta. Conforme o art. 167, § 2º da CF/88, os créditos especiais e extraordinários terão vigência no exercício financeiro em que forem autorizados, salvo se o ato de autorização for promulgado nos **últimos quatro meses do exercício** (setembro a dezembro), caso em que, reabertos nos limites dos seus saldos, serão incorporados ao orçamento do exercício financeiro subsequente.
> - **C)** Incorreta. Restos a Pagar pressupõem empenho prévio da despesa. O saldo não utilizado da dotação orçamentária é reaberto como crédito orçamentário vigente no novo ano.
> - **D)** Incorreta. A reabertura decorre de ato do Poder Executivo, respeitado o saldo remanescente, sem necessidade de novo PPA.
> - **E)** Incorreta. O recurso de cobertura do saldo reaberto decorre do próprio superávit financeiro/disponibilidade do crédito extraordinário de origem.
> 
> **Gabarito: B**

---

"""

    anchor_2 = "### 2. A Regra Constitucional de Reabertura de Saldos (Art. 167, § 2º da CF/88)"
    anchor_4 = "### 4. Regime Jurídico da Dívida Pública: Flutuante vs. Fundada (Consolidada)"
    anchor_fontes = "## 🌐 Fontes Oficiais & Manuais Técnicos Recomendados"

    text = text.replace(anchor_2, q06 + "\n" + anchor_2)
    text = text.replace(anchor_4, q07 + "\n" + q08 + "\n" + anchor_4)
    text = text.replace(anchor_fontes, q09_10 + "\n" + anchor_fontes)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
    print("Enriched File 04 successfully! Total: 10 questions.")


# ==========================================
# ARQUIVO 05: 05_lei_de_responsabilidade_fiscal_lrf_e_despesa_com_pessoal.md
# ==========================================
def enrich_file_05():
    filepath = os.path.join(BASE_DIR, "05_lei_de_responsabilidade_fiscal_lrf_e_despesa_com_pessoal.md")
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    if "### Questão 06" in text:
        print("File 05 already enriched.")
        return

    # Q06: Após 1.2 Os Relatórios Fiscais Obrigatórios: RREO e RGF (antes de ### 2.)
    q06 = """### Questão 06 (FCC - Adaptada / Analista de Planejamento e Orçamento)
A Lei Complementar nº 101/2000 (LRF) estabelece dois instrumentos essenciais de transparência da gestão fiscal: o Relatório Resumido da Execução Orçamentária (RREO) e o Relatório de Gestão Fiscal (RGF).

Sobre a periodicidade de publicação e o alcance desses relatórios, assinale a afirmativa correta:

* **A)** O RREO é publicado bimestralmente pelo Poder Executivo (abrangendo todos os Poderes), enquanto o RGF é emitido quadrimestralmente por cada um dos Poderes e órgãos autônomos (Executivo, Legislativo, Judiciário e Ministério Público).
* **B)** O RGF é divulgado mensalmente apenas pela União, sendo os Estados e Municípios dispensados de sua elaboração quando tiverem população inferior a 500 mil habitantes.
* **C)** O RREO e o RGF são publicados anualmente em conjunto, exclusivamente como anexo integrante da prestação de contas do Governador ao Tribunal de Contas.
* **D)** O RGF abrange unicamente o demonstrativo das despesas com propaganda institucional e diárias de viagem.
* **E)** O descumprimento dos prazos de publicação do RREO não gera qualquer sanção institucional ao ente federado, possuindo natureza meramente orientativa.

> **Comentário Detalhado:**
>
> - **A)** Correta. O art. 52 da LRF determina a publicação do RREO até 30 dias após o encerramento de cada **bimestre** pelo Executivo (englobando todos os Poderes). O RGF (arts. 54 e 55 da LRF) é emitido ao final de cada **quadrimestre** por cada titular de Poder e órgão autônomo (com faculdade semestral para municípios com menos de 50 mil habitantes).
> - **B)** Incorreta. O RGF é obrigatório para todos os entes federados (União, Estados, DF e Municípios).
> - **C)** Incorreta. Os relatórios possuem periodicidades próprias infra-anuais (bimestral para RREO e quadrimestral para RGF).
> - **D)** Incorreta. O RGF demonstra despesa com pessoal, dívida consolidada, concessão de garantias, operações de crédito e restos a pagar.
> - **E)** Incorreta. O atraso na publicação do RREO e do RGF sujeita o ente ao impedimento de receber transferências voluntárias e contratar operações de crédito (art. 51, § 2º da LRF).
> 
> **Gabarito: A**

---

"""

    # Q07: Após 3.4 Regras de Recondução e Medidas Constitucionais Sucessivas de Corte (antes de ### 4.)
    q07 = """### Questão 07 (FCC - Adaptada / TCE-PI - Auditor de Controle Externo)
Na hipótese de a Despesa Total com Pessoal (DTP) de determinado Poder ou órgão autônomo estadual ultrapassar o limite máximo fixado na LRF, a Constituição Federal de 1988 (art. 169, §§ 3º e 4º) e a própria LRF impõem medidas sucessivas e escalonadas para o retorno aos limites.

A ordem constitucional obrigatória das medidas de corte é:

* **A)** 1º - Redução de pelo menos 20% das despesas com cargos em comissão e funções de confiança; 2º - Exoneração de servidores não estáveis; 3º - Se as medidas anteriores não forem suficientes, perda do cargo pelo servidor público estável.
* **B)** 1º - Demissão sumária de servidores públicos estáveis; 2º - Redução proporcional de salários dos magistrados; 3º - Extinção de fundos constitucionais.
* **C)** 1º - Suspensão do pagamento de proventos a aposentados; 2º - Extinção de órgãos públicos; 3º - Corte de despesas de capital em saúde e educação.
* **D)** 1º - Exoneração imediata de servidores aprovados em concurso recente; 2º - Demissão de ocupantes de cargos comissionados; 3º - Aumento compulsório da alíquota do ICMS.
* **E)** 1º - Devolução voluntária de subsídios pelos Chefes de Poder; 2º - Congelamento da inflação; 3º - Limitação exclusiva das despesas de investimento.

> **Comentário Detalhado:**
>
> - **A)** Correta. O art. 169, §§ 3º e 4º da CF/88 estabelece a ordem cronológica estrita de providências: 1) redução em pelo menos 20% das despesas com comissionados e funções de confiança; 2) se não bastar, exoneração dos servidores não estáveis; 3) se ainda assim não alcançar o equilíbrio, o servidor estável poderá perder o cargo mediante processo administrativo em que lhe seja assegurada ampla defesa, fazendo jus a indenização de 1 mês por ano de serviço.
> - **B)** Incorreta. Atingir servidor estável é medida extrema e residual (última etapa), jamais primeira.
> - **C)** Incorreta. Proventos de aposentadoria gozam de garantia constitucional irredutível.
> - **D)** Incorreta. A primeira etapa atinge cargos em comissão e funções de confiança, não servidores concursados.
> - **E)** Incorreta. Não existe previsão constitucional de tais medidas nessa ordem.
> 
> **Gabarito: A**

---

"""

    # Q08: Segunda questão sobre limites de pessoal da LRF
    q08 = """### Questão 08 (FCC - Adaptada / TCE-SC - Auditor de Controle Externo)
Em determinado Estado da Federação, apurou-se que a Despesa Total com Pessoal do Poder Executivo atingiu 96% do limite máximo legalmente admitido pela Lei de Responsabilidade Fiscal (limite prudencial ultrapassado).

Diante dessa situação fática, o Poder Executivo estadual está expressamente VEDADO de:

* **A)** Conceder vantagem, aumento, reajuste ou adequação de remuneração a qualquer título, salvo os derivados de sentença judicial ou de determinação legal ou contratual anterior, bem como criar cargo, emprego ou função.
* **B)** Pagar a folha normal de salários e os proventos regulares de aposentadoria e pensão dos servidores já existentes.
* **C)** Efetuar qualquer tipo de empenho orçamentário destinado à manutenção de escolas e hospitais estaduais.
* **D)** Arrecadar tributos estaduais inscritos em dívida ativa e ajuizar execuções fiscais.
* **E)** Publicar o Relatório Resumido da Execução Orçamentária e as prestações de contas constitucionais.

> **Comentário Detalhado:**
>
> - **A)** Correta. O art. 22, parágrafo único da LRF estabelece que, ao ultrapassar o limite prudencial (95% do limite máximo), aplicam-se proibições imediatas ao órgão: vedada concessão de vantagens/aumentos/reajustes (salvo decisão judicial ou lei anterior), criação de cargos, alteração de estruturas de carreira que impliquem aumento de despesa, provimento de cargo público (ressalvada reposição em saúde, educação e segurança por aposentadoria/falecimento) e contratação de hora extra.
> - **B)** Incorreta. O pagamento da folha regular existente permanece obrigatório.
> - **C)** Incorreta. As despesas de custeio e funcionamento de serviços essenciais continuam normais.
> - **D)** Incorreta. A atividade arrecadatória é dever funcional vinculado do Estado.
> - **E)** Incorreta. A transparência fiscal é mantida e reforçada nesse cenário.
> 
> **Gabarito: A**

---

"""

    # Q09 e Q10: Após 4.3 antes de ## 🌐 Fontes Oficiais & Normativas Recomendadas
    q09_10 = """### Questão 09 (FCC - Adaptada / Analista Jurídico de Controle)
O art. 167, inciso III da Constituição Federal de 1988 estabelece o princípio conhecido pela doutrina e jurisprudência como a **"Regra de Ouro"** das finanças públicas brasileiras.

Segundo a Regra de Ouro constitucional:

* **A)** É vedada a realização de operações de créditos que excedam o montante das despesas de capital, ressalvadas as autorizadas mediante créditos suplementares ou especiais com finalidade precisa, aprovados pelo Poder Legislativo por maioria absoluta.
* **B)** As receitas tributárias correntes devem superar em pelo menos 50% todas as despesas com juros e encargos da dívida pública consolidada.
* **C)** É obrigatória a destinação de 10% da receita de impostos para a constituição de reserva monetária em ouro no Banco Central do Brasil.
* **D)** Nenhuma dívida pública fundada poderá ultrapassar o prazo de amortização de dez anos sem autorização unânime do Senado Federal.
* **E)** Os precatórios judiciais alimentares gozam de preferência absoluta de saque em relação a qualquer outro dispêndio estatal.

> **Comentário Detalhado:**
>
> - **A)** Correta. É o teor literal do art. 167, III da CF/88. A finalidade da Regra de Ouro é impedir que o Estado financie despesas correntes de custeio diário com endividamento público (empréstimos), exigindo que o crédito obtido financie despesas de capital (investimentos), ressalvada autorização legislativa especial por maioria absoluta.
> - **B)** Incorreta. Trata-se de formulação sem respaldo constitucional.
> - **C)** Incorreta. Não existe exigência de lastro em metal ouro na gestão orçamentária hodierna.
> - **D)** Incorreta. Os limites da dívida consolidada são fixados por resolução do Senado Federal com base no art. 52 da CF/88.
> - **E)** Incorreta. Embora precatórios tenham preferência no art. 100 da CF/88, não é essa a definição da Regra de Ouro.
> 
> **Gabarito: A**

---

### Questão 10 (FCC - Adaptada / TCE-GO - Analista de Controle Externo)
Nos termos do art. 42 da Lei de Responsabilidade Fiscal (LC nº 101/2000), aplicável aos governantes dos Poderes Executivo, Legislativo e Judiciário em fim de mandato:

* **A)** É vedado ao titular de Poder ou órgão contrair obrigação de despesa que não possa ser cumprida integralmente dentro dos últimos dois quadrimestres do seu mandato, ou que tenha parcelas a serem pagas no exercício seguinte sem que haja suficiente disponibilidade de caixa para este efeito.
* **B)** É permitida a contratação de quaisquer despesas continuadas, desde que os empenhos sejam cancelados no primeiro dia útil do mandato do sucessor.
* **C)** Os contratos administrativos firmados nos últimos oito meses do mandato ficam automaticamente rescindidos sem direito a indenização.
* **D)** As restrições de final de mandato atingem exclusivamente o Presidente da República e os Governadores de Estado, não se aplicando aos Prefeitos Municipais.
* **E)** O descumprimento do art. 42 da LRF constitui mera irregularidade formal de gestão, sem repercussão na esfera penal do ordenador de despesas.

> **Comentário Detalhado:**
>
> - **A)** Correta. É a redação expressa do art. 42 da LRF: veda contrair despesa nos últimos dois quadrimestres (8 meses) do mandato sem suficiente disponibilidade de caixa para saldá-la ou cobrir parcelas no exercício subsequente.
> - **B)** Incorreta. A vedação visa justamente evitar o cancelamento abusivo de restos a pagar e a transmissão de déficits ao sucessor.
> - **C)** Incorreta. Contratos regulares não são rescindidos automaticamente; o que se proíbe é contrair obrigações sem lastro de caixa.
> - **D)** Incorreta. Aplica-se a todos os titulares de Poder e órgão de todas as esferas federativas.
> - **E)** Incorreta. O descumprimento do art. 42 da LRF configura o crime tipificado no art. 359-C do Código Penal (pena de reclusão de 1 a 4 anos).
> 
> **Gabarito: A**

---

"""

    anchor_2 = "### 2. Despesa Obrigatória de Caráter Continuado (DOCC - Art. 17)"
    anchor_4 = "### 4. Endividamento, Regra de Ouro, ARO e Vedações de Fim de Mandato"
    anchor_fontes = "## 🌐 Fontes Oficiais & Normativas Recomendadas"

    text = text.replace(anchor_2, q06 + "\n" + anchor_2)
    text = text.replace(anchor_4, q07 + "\n" + q08 + "\n" + anchor_4)
    text = text.replace(anchor_fontes, q09_10 + "\n" + anchor_fontes)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
    print("Enriched File 05 successfully! Total: 10 questions.")


if __name__ == "__main__":
    enrich_file_01()
    enrich_file_02()
    enrich_file_03()
    enrich_file_04()
    enrich_file_05()
    print("Module 19 fully processed!")
