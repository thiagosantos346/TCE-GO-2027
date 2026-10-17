# -*- coding: utf-8 -*-
import os
import re

BASE_DIR = "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/15_nocoes_de_direito_administrativo"
f05_path = f"{BASE_DIR}/05_controle_da_administracao_e_improbidade_administrativa.md"
with open(f05_path, "r", encoding="utf-8") as f:
    t05 = f.read()

assert "### Questão 01" in t05
assert "### Questão 02" in t05
assert "### Questão 03" in t05
assert "### Questão 04" in t05
assert "### Questão 05" in t05

q06_05 = """### Questão 06 (FCC - Analista de Controle Externo / TCE-GO)
A Constituição Federal de 1988 estabelece que os Poderes Legislativo, Executivo e Judiciário manterão, de forma integrada, sistema de controle interno (art. 74).

A respeito das finalidades constitucionais do controle interno e de sua articulação com o controle externo a cargo do Tribunal de Contas, assinale a afirmativa correta.

* **A)** Os responsáveis pelo controle interno que tomarem conhecimento de qualquer irregularidade ou ilegalidade têm a faculdade discricionária de decidir se comunicam ou não o fato ao Tribunal de Contas.
* **B)** O sistema de controle interno exerce papel meramente consultivo, sendo vedada sua atuação na avaliação do cumprimento das metas previstas no plano plurianual e na execução dos programas de governo.
* **C)** Os responsáveis pelo controle interno, ao tomarem conhecimento de qualquer irregularidade ou ilegalidade, dela darão ciência ao Tribunal de Contas competente, sob pena de responsabilidade solidária.
* **D)** O controle externo exercido pelo Tribunal de Contas absorve as funções do controle interno, tornando dispensável a manutenção de controladorias nos órgãos do Poder Executivo estadual.
* **E)** O controle interno tem competência para anular julgamentos técnicos definitivos emitidos pelo Tribunal de Contas sobre contas de prefeitos municipais.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Não se trata de faculdade ou juízo discricionário, mas de um **dever legal cogente e indeclinável** imposto expressamente pela Carta Magna.
> - **B)** Incorreta. O art. 74, I, da CF/88 estabelece expressamente como finalidade do controle interno "avaliar o cumprimento das metas previstas no plano plurianual, a execução dos programas de governo e dos orçamentos da União".
> - **C)** Correta. O art. 74, § 1º, da Constituição Federal dispõe literalmente que *"Os responsáveis pelo controle interno, ao tomarem conhecimento de qualquer irregularidade ou ilegalidade, dela darão ciência ao Tribunal de Contas da União [e congêneres estaduais], sob pena de responsabilidade solidária"*. O silêncio ou a omissão dolosa/culposa do controlador interno acarreta sua corresponsabilização direta pelo ilícito.
> - **D)** Incorreta. Controle interno e controle externo são instâncias constitucionais autônomas, harmônicas e complementares que atuam de forma integrada.
> - **E)** Incorreta. O controle interno jamais tem ascendência sobre as decisões colegiadas do Tribunal de Contas.
>
> **Gabarito: C**"""

q07_05 = """### Questão 07 (FGV - Auditor de Controle Externo / TCE)
No desenho institucional do controle externo brasileiro, o Tribunal de Contas desempenha competências multifacetadas delineadas no art. 71 da Constituição da República.

Sobre a competência das Cortes de Contas para apreciar a legalidade de atos de admissão de pessoal e concessão de benefícios previdenciários, assinale a afirmativa correta.

* **A)** O Tribunal de Contas aprecia a legalidade das admissões de pessoal a qualquer título, inclusive as nomeações para cargos de provimento em comissão.
* **B)** O ato de aposentadoria de servidor público é ato administrativo complexo que somente se aperfeiçoa com o registro no Tribunal de Contas, aplicando-se o prazo decadencial de cinco anos a contar da chegada do processo ao respectivo Tribunal de Contas (Tema 445 / STF).
* **C)** A concessão de aposentadoria consolida-se de imediato na esfera jurídica do servidor no momento da publicação do ato pelo órgão de origem, não podendo o Tribunal de Contas recusar seu registro.
* **D)** O Tribunal de Contas competente para julgar as contas de gestão prestadas por dirigentes de empresas estatais exploradoras de atividade econômica é o Poder Judiciário, ante o regime de direito privado dessas empresas.
* **E)** A recusa de registro de aposentadoria pelo Tribunal de Contas submete-se a recurso ordinário perante a Assembleia Legislativa.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O art. 71, III, da CF/88 estabelece que o Tribunal de Contas aprecia a legalidade dos atos de admissão de pessoal, na administração direta e indireta, incluídas as fundações instituídas e mantidas pelo Poder Público, **ressalvadas as nomeações para cargo em comissão**.
> - **B)** Correta. Conforme fixado pelo STF no **Tema 445 de Repercussão Geral** (RE 636.553), o ato de aposentadoria, reforma ou pensão ostenta natureza de ato complexo; assim, o prazo de 5 (cinco) anos para que a Corte de Contas analise a legalidade do ato com estrita observância do contraditório e da ampla defesa conta-se **a partir da chegada do respectivo processo ao Tribunal de Contas**. Passados os 5 anos sem manifestação, opera-se a estabilização/registro tácito.
> - **C)** Incorreta. A publicação originária tem eficácia precária e provisória até a manifestação integrativa do Tribunal de Contas.
> - **D)** Incorreta. O art. 71, II, da CF/88 submete à fiscalização do Tribunal de Contas qualquer pessoa que administre bens e valores públicos, inclusive dirigentes de empresas públicas e sociedades de economia mista.
> - **E)** Incorreta. A recusa de registro é deliberação técnica privativa do TC, impassível de recurso político para o Poder Legislativo.
>
> **Gabarito: B**"""

q08_05 = """### Questão 08 (FCC - Procurador do Estado)
Em processo de tomada de contas especial instaurado para apurar dano ao erário decorrente de superfaturamento em obras públicas estaduais, o Tribunal de Contas condenou o ex-gestor ao ressarcimento ao erário do valor desviado, bem como aplicou-lhe multa administrativa pecuniária individual.

À luz do art. 71, § 3º, da Constituição Federal e da jurisprudência consolidada, o acórdão proferido pelo Tribunal de Contas:

* **A)** Constitui título executivo extrajudicial, prescindindo de ação de conhecimento prévia para sua cobrança em juízo.
* **B)** Depende de homologação prévia por sentença judicial transitada em julgado para que possa ser executado perante a Vara da Fazenda Pública.
* **C)** Tem eficácia de título executivo judicial, devendo ser executado pelo próprio Tribunal de Contas por meio de seus auditores fiscais.
* **D)** Pode ter a cobrança executiva promovida diretamente pelo Ministério Público junto ao Tribunal de Contas em nome próprio.
* **E)** Prescreve na esfera patrimonial de cobrança no prazo de vinte anos, sendo inaplicável a Lei de Execução Fiscal.

> **Comentário Detalhado:**
>
> - **A)** Correta. O art. 71, § 3º, da CF/88 estatui categoricamente: *"As decisões do Tribunal de que resulte imputação de débito ou multa terão eficácia de título executivo"*. Trata-se de **título executivo extrajudicial**, apto a embasar direta e imediatamente ação de execução de título extrajudicial por quantia certa.
> - **B)** Incorreta. Não há qualquer necessidade de processo de conhecimento judicial prévio ou homologação judicial para conferir exequibilidade à decisão condenatória do TC.
> - **C)** Incorreta. É título **extrajudicial** e não judicial. Além disso, o Tribunal de Contas não tem personalidade jurídica nem capacidade postulatória para executar judicialmente suas próprias decisões condenatórias.
> - **D)** Incorreta. O STF pacificou no Tema 643 que a execução da decisão do Tribunal de Contas compete à **Procuradoria do respectivo ente federativo** (PGE ou PGM beneficiária do crédito), e não ao Ministério Público de Contas (MPC).
> - **E)** Incorreta. O STF definiu no Tema 899 (RE 636.886) que a pretensão de ressarcimento ao erário fundada em decisão de Tribunal de Contas prescreve em 5 (cinco) anos, regulada pela Lei de Execução Fiscal.
>
> **Gabarito: A**"""

q09_05 = """### Questão 09 (FGV - Analista de Controle Externo / TCE-GO)
A Lei nº 14.230/2021 promoveu profunda reformulação na Lei de Improbidade Administrativa (Lei nº 8.429/1992). Quanto aos sujeitos ativos e passivos dos atos de improbidade administrativa, assinale a afirmativa correta.

* **A)** O particular que não exerça função pública somente pode responder por ato de improbidade administrativa se for comprovado que induziu ou concorreu dolosamente para a prática do ato ímprobo, vedada a sua responsabilização isolada sem a presença de agente público no polo passivo.
* **B)** As pessoas jurídicas privadas não podem figurar no polo passivo de ações de improbidade administrativa, recaindo as sanções da LIA exclusivamente sobre as pessoas físicas dos administradores.
* **C)** Os agentes políticos estão integralmente imunes às sanções da Lei de Improbidade Administrativa, sujeitando-se exclusivamente a processo de crime de responsabilidade.
* **D)** O terceiro particular pode ser condenado por improbidade administrativa na modalidade culposa se restar demonstrada negligência profissional manifesta.
* **E)** Entidades que recebam subvenção ou benefício financeiro do poder público não são consideradas sujeitos passivos dos atos de improbidade administrativa.

> **Comentário Detalhado:**
>
> - **A)** Correta. O art. 3º da Lei nº 8.429/1992 (com redação da Lei nº 14.230/2021) prevê que as disposições da lei aplicam-se àquele que, mesmo não sendo agente público, induza ou concorra dolosamente para a prática do ato de improbidade. A jurisprudência consolidada do STJ e do STF pacificou que o particular jamais responde sozinho por improbidade administrativa; é indispensável a concorrência e a presença simultânea de um agente público no polo passivo ou na descrição da trama ímproba.
> - **B)** Incorreta. O art. 3º, § 1º, da LIA admite a responsabilização de pessoa jurídica por improbidade, desde que observada a subsidiariedade com a Lei Anticorrupção (Lei nº 12.846/2013).
> - **C)** Incorreta. Conforme jurisprudência do STF (Pet 3.240 e Rcl 2.138), prefeitos, secretários estaduais e governadores submetem-se ao regime da Lei de Improbidade Administrativa (a única exceção absoluta é o Presidente da República, sujeito exclusivamente à Lei nº 1.079/1950 por crimes de responsabilidade).
> - **D)** Incorreta. Com o advento da Lei nº 14.230/2021 e do Tema 1.199/STF, **toda e qualquer modalidade culposa foi revogada**; exige-se dolo específico em todos os tipos da LIA.
> - **E)** Incorreta. O art. 1º, § 6º e § 7º, da LIA prevê expressamente que as entidades privadas que recebam subvenção, benefício fiscal ou creditício do erário são sujeitos passivos protegidos pela lei.
>
> **Gabarito: A**"""

q10_05 = """### Questão 10 (FCC - Auditor de Controle Externo)
Constitui ato de improbidade administrativa que importa enriquecimento ilícito (art. 9º da Lei nº 8.429/1992, com as alterações da Lei nº 14.230/2021):

* **A)** Agir com negligência na celebração ou fiscalização de contrato administrativo de transporte escolar, provocando prejuízo financeiro ao erário público.
* **B)** Perceber vantagem econômica de qualquer natureza, direta ou indireta, para facilitar a aquisição de bem por preço superior ao de mercado.
* **C)** Deixar de prestar contas no prazo legal quando estejam disponíveis as condições técnicas para fazê-lo, com o escopo de ocultar irregularidades.
* **D)** Nomear parente consanguíneo de segundo grau para cargo de provimento em comissão em virtude de erro escusável na interpretação da Súmula Vinculante nº 13.
* **E)** Frustrar a licitude de procedimento licitatório sem auferimento de qualquer benefício patrimonial pessoal e sem perda financeira pelo erário.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Condutas negligentes (culpa) não caracterizam mais improbidade em hipótese alguma. Ademais, dano financeiro sem ganho patrimonial pessoal amolda-se ao art. 10 (prejuízo ao erário), e não ao art. 9º.
> - **B)** Correta. O art. 9º, III, da Lei nº 8.429/1992 tipifica expressamente como ato de improbidade que importa enriquecimento ilícito *"perceber vantagem econômica de qualquer natureza, direta ou indireta, para facilitar a aquisição, permuta ou locação de bem móvel ou imóvel, ou a contratação de serviços pelas entidades referidas no art. 1º desta lei, por preço superior ao valor de mercado"*. Exige vantagem patrimonial indevida auferida pelo agente público.
> - **C)** Incorreta. Deixar de prestar contas dolosamente atenta contra os princípios da administração pública (art. 11, VI, da LIA), não consubstanciando enriquecimento ilícito por si só.
> - **D)** Incorreta. A nomeação indevida de parente com dolo constitui ofensa a princípios (art. 11, XI - nepotismo); se fundada em erro escusável de hermenêutica ou sem dolo, é atípica na esfera da improbidade.
> - **E)** Incorreta. Frustrar a licitude de licitação gerando perda patrimonial é hipótese do art. 10, VIII da LIA; sem dolo e sem dano, não configura improbidade do art. 9º.
>
> **Gabarito: B**"""

q11_05 = """### Questão 11 (FGV - Analista Jurídico de Controle Externo / TCE-GO)
A Lei nº 14.230/2021 alterou profundamente o art. 11 da Lei nº 8.429/1992 (atos de improbidade que atentam contra os princípios da Administração Pública), bem como o regime prescricional do art. 23.

Sobre o regime atual dos atos de improbidade contra princípios e da prescrição na LIA, assinale a afirmativa correta.

* **A)** O rol de atos de improbidade administrativa previstos no art. 11 da Lei nº 8.429/1992 tornou-se taxativo (numerus clausus), exigindo a comprovação de dolo específico e da lesividade relevante ao bem jurídico tutelado.
* **B)** Qualquer violação aos princípios da legalidade e da moralidade autoriza a condenação por improbidade administrativa, subsistindo a natureza exemplificativa do caput do art. 11.
* **C)** O prazo prescricional para ajuizamento da ação de improbidade administrativa é de dez anos, contado da data do término do mandato do prefeito.
* **D)** A prescrição intercorrente na ação de improbidade administrativa ocorre no prazo de dois anos contados da publicação da sentença de primeiro grau.
* **E)** O ato de improbidade contra princípios previsto no art. 11 admite a sanção de perda dos direitos políticos por até vinte anos.

> **Comentário Detalhado:**
>
> - **A)** Correta. A Lei nº 14.230/2021 conferiu caráter **taxativo (exaustivo / numerus clausus)** aos incisos do art. 11 da LIA, conforme expressamente reconhecido pelo STF no Tema 1.199. Não mais se admite condenar o agente com base genérica em "ofensa a princípios" do caput; a conduta deve amoldar-se estritamente a um dos incisos positivados (ex.: frustrar concurso, nepotismo, revelar segredo), exigindo-se dolo específico e lesividade relevante.
> - **B)** Incorreta. Foi superada a tese do rol exemplificativo; o legislador vedou expressamente condenações genéricas sem enquadramento estrito nos incisos do art. 11.
> - **C)** Incorreta. O art. 23 da LIA fixa prazo prescricional unificado de **8 (oito) anos**, contado a partir da data de ocorrência do fato (ou, no caso de infrações permanentes, do dia em que cessou a permanência).
> - **D)** Incorreta. A prescrição intercorrente opera-se no prazo de **4 (quatro) anos** (art. 23, § 5º da LIA) entre os marcos interruptivos legais (ajuizamento, publicação da sentença condenatória, acórdão confirmatório etc.).
> - **E)** Incorreta. O art. 12, III, da LIA (com redação da Lei 14.230/2021) **revogou a sanção de suspensão dos direitos políticos** para os atos do art. 11; as sanções cabíveis são multa civil de até 24 vezes a remuneração e proibição de contratar/receber benefícios por até 4 anos.
>
> **Gabarito: A**"""

# Inserções no arquivo 05
ancora_53 = "### 5.3 Atentado aos Princípios da Administração (Art. 11 da LIA - Rol Taxativo)"
pos_53 = t05.find(ancora_53)
pos_54 = t05.find("### 5.4 Matriz Comparativa", pos_53)
assert pos_53 != -1 and pos_54 != -1
t05 = t05[:pos_54] + "\n\n" + q11_05.strip() + "\n\n---\n\n" + t05[pos_54:]

ancora_51 = "### 5.1 Enriquecimento Ilícito (Art. 9º da LIA)"
pos_51 = t05.find(ancora_51)
pos_52 = t05.find("### 5.2 Prejuízo ao Erário", pos_51)
assert pos_51 != -1 and pos_52 != -1
t05 = t05[:pos_52] + "\n\n" + q10_05.strip() + "\n\n---\n\n" + t05[pos_52:]

ancora_41 = "### 4.1 Sujeitos Ativos e Passivos da Improbidade Administrativa"
pos_41 = t05.find(ancora_41)
pos_42 = t05.find("### 4.2 O Elemento Subjetivo", pos_41)
assert pos_41 != -1 and pos_42 != -1
t05 = t05[:pos_42] + "\n\n" + q09_05.strip() + "\n\n---\n\n" + t05[pos_42:]

ancora_22 = "### 2.2 Natureza das Decisões e Título Executivo Extrajudicial"
pos_22 = t05.find(ancora_22)
pos_30 = t05.find("## 3. O Controle Judicial", pos_22)
assert pos_22 != -1 and pos_30 != -1
t05 = t05[:pos_30] + "\n\n" + q08_05.strip() + "\n\n---\n\n" + t05[pos_30:]

ancora_21 = "### 2.1 A Função Constitucional do Tribunal de Contas (CF/88, arts. 70 a 75)"
pos_21 = t05.find(ancora_21)
pos_22_new = t05.find("### 2.2 Natureza das Decisões", pos_21)
assert pos_21 != -1 and pos_22_new != -1
t05 = t05[:pos_22_new] + "\n\n" + q07_05.strip() + "\n\n---\n\n" + t05[pos_22_new:]

ancora_12 = "### 1.2 Classificação Quanto à Origem: Controle Interno vs. Controle Externo"
pos_12 = t05.find(ancora_12)
pos_13 = t05.find("### 1.3 Classificação Quanto ao Momento", pos_12)
assert pos_12 != -1 and pos_13 != -1
t05 = t05[:pos_13] + "\n\n" + q06_05.strip() + "\n\n---\n\n" + t05[pos_13:]

qs_05 = re.findall(r"### Questão (\d+)", t05)
print("Questões no arquivo 05:", qs_05)
assert len(qs_05) == 11
assert sorted(qs_05) == ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']

with open(f05_path, "w", encoding="utf-8") as f:
    f.write(t05)

print("Arquivo 05 gravado com sucesso! Total: 11 questões.")
