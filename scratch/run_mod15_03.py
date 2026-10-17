# -*- coding: utf-8 -*-
import os
import re

BASE_DIR = "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/15_nocoes_de_direito_administrativo"
f03_path = f"{BASE_DIR}/03_atos_administrativos_e_processo_estadual.md"

with open(f03_path, "r", encoding="utf-8") as f:
    text = f.read()

assert "### Questão 01" in text
assert "### Questão 02" in text
assert "### Questão 03" in text
assert "### Questão 04" in text
assert "### Questão 05" in text

q06_03 = """### Questão 06 (FCC - Analista Judiciário - Área Judiciária)
No estudo da Teoria Geral do Ato Administrativo, os planos da existência (perfeição), da validade e da eficácia devem ser compreendidos como conceitos analiticamente distintos e autônomos.

A esse respeito, assinale a afirmativa correta.

* **A)** O ato administrativo perfeito é necessariamente válido e eficaz, inexistindo no ordenamento a figura de ato perfeito porém inválido.
* **B)** Um ato administrativo pode ser perfeito, válido e ineficaz, como na hipótese em que seus efeitos jurídicos ficam condicionados à ocorrência de um termo inicial ou de uma condição suspensiva.
* **C)** A eficácia do ato administrativo decorre de sua conformidade com a ordem jurídica, sendo nulo todo ato que temporariamente não produza efeitos práticos.
* **D)** A perfeição do ato administrativo diz respeito à sua adequação às normas constitucionais e legais em vigor, de modo que a ausência de motivo gera a imperfeição do ato.
* **E)** Todo ato administrativo perfeito adquire imediatamente eficácia retroativa plena (ex tunc), independentemente de publicação oficial prévia.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A perfeição refere-se à conclusão do ciclo de formação do ato (existência). Um ato pode ser perfeito (concluiu suas etapas formativas), mas ser inválido (por violar a lei) ou ineficaz (por depender de termo ou condição).
> - **B)** Correta. A tridimensionalidade do ato administrativo consagra que: (1) perfeição = ato concluído e existente; (2) validade = ato conforme ao ordenamento jurídico; (3) eficácia = idoneidade atual para produzir seus efeitos. Um ato pode estar concluído (perfeito) e em perfeita consonância com a lei (válido), mas com efeitos suspensos aguardando um termo (data futura) ou condição suspensiva (evento futuro e incerto), configurando ato ineficaz.
> - **C)** Incorreta. A conformidade com a ordem jurídica traduz a **validade** do ato. A ineficácia temporária não implica nulidade; o ato pode ser válido e simplesmente aguardar publicação ou condição.
> - **D)** Incorreta. A adequação à lei e à Constituição concerne ao plano da **validade**. A perfeição exige apenas que o ato tenha completado todos os passos formais de sua edição.
> - **E)** Incorreta. Os atos administrativos operam em regra para o futuro (efeitos ex nunc), dependendo de publicação na imprensa oficial ou notificação para produzirem efeitos externos.
>
> **Gabarito: B**"""

q07_03 = """### Questão 07 (FGV - Auditor de Controle Externo / TCE-PA)
A autoridade competente de determinada autarquia estadual instaurou processo administrativo de desapropriação e expediu decreto expropriatório sobre imóvel pertencente a particular, sob o fundamento formal de interesse público na construção de um posto de saúde comunitário. Restou cabalmente demonstrado, todavia, que o verdadeiro intuito da autoridade era retaliar o proprietário por desafeto político de campanha eleitoral, tendo a autarquia abandonado o projeto sanitário logo após a imissão na posse.

Nessa situação, o ato expropriatório praticado padece de vício de:

* **A)** Incompetência absoluta, uma vez que autarquias estaduais não possuem competência legal para executar desapropriações.
* **B)** Desvio de finalidade (desvio de poder), caracterizado pela utilização de competência legalmente conferida para alcançar finalidade alheia ao interesse público primário, acarretando a nulidade insanável do ato.
* **C)** Forma, sendo plenamente convalidável pela autoridade superior mediante simples ratificação em termo aditivo.
* **D)** Objeto ilícito, sujeitando-se unicamente à anulação parcial com aproveitamento dos atos expropriatórios pretéritos.
* **E)** Mera irregularidade formal sanável, bastando a aplicação de multa disciplinar leve ao gestor.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. As autarquias têm legitimidade para promover desapropriações quando expressamente autorizadas por lei ou decreto delegatório (Decreto-Lei nº 3.365/1941, art. 3º). O vício reside na finalidade da conduta.
> - **B)** Correta. O desvio de finalidade (desvio de poder) ocorre quando o agente pratica o ato visando a fim diverso daquele previsto, explícita ou implicitamente, na lei ou alheio ao interesse público (art. 2º, parágrafo único, 'e', da Lei nº 4.717/1965). No caso concreto, o uso da desapropriação como instrumento de vingança pessoal contra desafeto político fere o elemento finalidade e os princípios da impessoalidade e moralidade, gerando nulidade insanável.
> - **C)** Incorreta. O vício de finalidade é insanável, sendo vedada a sua convalidação pela Administração Pública ou por autoridade superior.
> - **D)** Incorreta. A desapropriação para utilidade pública tem objeto material lícito em tese; o vício está na finalidade subjetiva e desvio de poder que contamina todo o ato, gerando nulidade integral ex tunc.
> - **E)** Incorreta. O desvio de poder é vício de legalidade gravíssimo que atinge a validade do ato e configura ato de improbidade administrativa.
>
> **Gabarito: B**"""

q08_03 = """### Questão 08 (FCC - Procurador do Estado)
No que tange aos elementos e requisitos de validade do ato administrativo, analise as afirmativas a seguir sobre o objeto (conteúdo) e a delimitação do mérito administrativo:

I. O objeto é a alteração no mundo jurídico que o ato se propõe a operar de forma imediata (criação, modificação, resguardo ou extinção de direitos e deveres).  
II. O mérito do ato administrativo reside no núcleo discricionário conferido pela lei ao administrador, integrando com exclusividade os elementos motivo e objeto (juízo de oportunidade e conveniência).  
III. Os elementos competência, finalidade e forma são, em regra, estritamente vinculados no ordenamento jurídico pátrio.

Está correto o que se afirma em:

* **A)** I, apenas.
* **B)** I e II, apenas.
* **C)** II e III, apenas.
* **D)** I, II e III.
* **E)** III, apenas.

> **Comentário Detalhado:**
>
> - **I. Correta:** O objeto (conteúdo) é a transformação prática e jurídica pretendida pelo ato (ex.: a concessão da licença, a aplicação da demissão, a autorização de uso). Deve ser lícito, possível, determinado ou determinável.
> - **II. Correta:** O mérito administrativo (conveniência e oportunidade) situa-se única e exclusivamente na margem de liberdade conferida ao administrador para valorar o **motivo** (circunstâncias determinantes) e escolher o **objeto** (conteúdo da providência mais adequada).
> - **III. Correta:** A doutrina clássica e consolidada da FCC estabelece que os elementos **Competência, Finalidade e Forma** são sempre vinculados pela lei (salvo raríssimas hipóteses de forma não solene), enquanto o **Motivo** e o **Objeto** podem ser vinculados ou discricionários.
>
> Logo, todas as afirmativas estão corretas.
>
> **Gabarito: D**"""

q09_03 = """### Questão 09 (FGV - Analista Judiciário - Área Judiciária)
Determinada fiscalização de vigilância sanitária estadual constatou que um restaurante comercializava grande quantidade de carnes bovinas em avançado estado de putrefação, expondo a risco iminente a saúde pública coletiva. De imediato, sem necessidade de prévia autorização judicial, os fiscais apreenderam as mercadorias impróprias e interditaram cautelarmente o estabelecimento.

A atuação administrativa descrita fundamenta-se precipuamente no atributo do ato administrativo denominado:

* **A)** Tipicidade, que autoriza a Administração a criar sanções inominadas sem previsão em lei.
* **B)** Autoexecutoriedade, que confere ao Poder Público a prerrogativa de executar direta e materialmente seus atos e medidas de polícia administrativa sem a intervenção prévia do Poder Judiciário em situações de urgência ou previsão em lei.
* **C)** Imperatividade pura, a qual dispensa a observância do contraditório e da ampla defesa até mesmo na fase recursal ulterior.
* **D)** Presunção de veracidade relativa, que inibe qualquer controle judicial a posteriori sobre a validade da apreensão.
* **E)** Irrevogabilidade, por se tratar de ato administrativo de polícia de conteúdo definitivo.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A tipicidade assegura que a Administração só pratique atos previamente previstos em figuras jurídicas delimitadas pelo legislador, impedindo atos arbitrários ou sanções inominadas.
> - **B)** Correta. A **autoexecutoriedade** desdobra-se em exigibilidade (obrigação de cumprimento) e executoriedade material (coação direta da Administração sem ordem judicial prévia). É admitida quando expressamente autorizada por lei ou em situações de urgência que ponham em risco bens jurídicos essenciais (como a saúde coletiva).
> - **C)** Incorreta. A autoexecutoriedade e a imperatividade não anulam o devido processo legal; o contraditório e a ampla defesa são diferidos (postecipados), cabendo processo administrativo posterior e eventual recurso.
> - **D)** Incorreta. A presunção de legitimidade e veracidade é júris tantum (relativa); jamais impede que o particular lesado acione o Poder Judiciário ou demonstre vício na conduta estatal.
> - **E)** Incorreta. A interdição cautelar e a apreensão são atos materiais e administrativos plenamente sindicáveis.
>
> **Gabarito: B**"""

q10_03 = """### Questão 10 (FCC - Auditor de Controle Externo)
Na classificação dos atos administrativos quanto à formação da vontade, a doutrina divide os atos em simples, complexos e compostos. Sobre essa tipologia, assinale a afirmativa correta.

* **A)** O ato complexo decorre da manifestação de vontade de um único órgão, que consulta previamente outro órgão apenas para fins de aconselhamento opinativo facultativo.
* **B)** O ato composto resulta da conjugação e fusão das vontades de dois ou mais órgãos distintos e independentes, cuja integração é condição indispensável para a própria existência do ato único.
* **C)** A nomeação de Ministro do Supremo Tribunal Federal (escolha do Presidente da República com prévia aprovação do Senado Federal) e a concessão de aposentadoria sujeita a registro pelo Tribunal de Contas constituem exemplos clássicos de atos complexos.
* **D)** No ato composto, a vontade de um órgão principal depende da confirmação por órgão subordinado, não gerando efeitos a aprovação ou homologação da autoridade superior.
* **E)** O ato simples colegiado (editado por órgão com colegiado numeroso, como o Pleno do Tribunal de Contas) transmuda-se automaticamente em ato complexo.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A consulta opinativa não gera ato complexo. O ato complexo exige a união de duas ou mais vontades estatais autônomas e indispensáveis que se fundem para formar um único ato administrativo.
> - **B)** Incorreta. A definição apresentada corresponde ao **ato complexo** ("órgãos distintos cujas vontades se fundem"). O ato composto é formado pela manifestação de vontade de um órgão principal (ato principal) que depende da aprovação, homologação ou visto de outro órgão (ato acessório/instrumental).
> - **C)** Correta. Na nomeação de Ministro do STF (art. 84, XIV c/c art. 52, III, 'a', CF/88) há manifestação do Executivo e do Legislativo (Senado) formando um único ato complexo. Da mesma forma, segundo pacífica e consolidada jurisprudência do STF (Súmula Vinculante nº 3 e Tema 445), o ato de concessão de aposentadoria de servidor público é ato complexo, que somente se aperfeiçoa com o registro perante a Corte de Contas competente.
> - **D)** Incorreta. No ato composto, o ato instrumental é comumente praticado por órgão superior controlador (como uma homologação de licitação ou visto ministerial).
> - **E)** Incorreta. O ato deliberado por órgão colegiado (como o Pleno do TCE) é **ato simples colegiado**; a pluralidade de membros não altera a singularidade do órgão emissor.
>
> **Gabarito: C**"""

q11_03 = """### Questão 11 (FGV - Analista Judiciário de Controle Externo / TCE-GO)
De acordo com o regime jurídico do processo administrativo no âmbito da Administração Pública do Estado de Goiás, disciplinado pela Lei Estadual nº 13.800/2001, considere as seguintes afirmativas:

I. O direito da Administração de anular os atos administrativos de que decorram efeitos favoráveis para os destinatários decai em cinco anos, contados da data em que foram praticados, salvo comprovada má-fé.  
II. É impedido de atuar em processo administrativo o servidor ou autoridade que tenha interesse direto ou indireto na matéria, ou que tenha participado como perito, testemunha ou representante no mesmo feito.  
III. Das decisões administrativas cabe recurso, em face de razões de legalidade e de mérito, tramitando o recurso no máximo por três instâncias administrativas, salvo disposição legal em contrário.

Está correto o que se afirma em:

* **A)** I, apenas.
* **B)** I e II, apenas.
* **C)** II e III, apenas.
* **D)** I e III, apenas.
* **E)** I, II e III.

> **Comentário Detalhado:**
>
> - **I. Correta:** O art. 54 da Lei Estadual nº 13.800/2001 (reproduzindo idêntico regramento da Lei Federal nº 9.784/1999) consagra o prazo decadencial de 5 (cinco) anos para que a Administração Pública anule atos favoráveis aos administrados, ressalvada a hipótese de comprovada má-fé do beneficiário (caso em que a anulação é admitida a qualquer tempo).
> - **II. Correta:** O art. 18 da Lei Estadual nº 13.800/2001 estipula os casos expressos de impedimento do servidor ou autoridade (interesse direto ou indireto, atuação como perito/testemunha/representante ou parentesco até o terceiro grau).
> - **III. Correta:** O art. 56 e art. 57 da Lei Estadual nº 13.800/2001 determinam que o recurso administrativo independe de caução, abrange legalidade e mérito e tramitará por no máximo três instâncias administrativas, salvo expressa previsão legal diversa.
>
> Todas as afirmativas encontram-se rigorosamente corretas conforme a Lei Estadual nº 13.800/2001.
>
> **Gabarito: E**"""

# Inserções no arquivo 03 de trás para frente
ancora_63 = "### 6.3 Impedimentos e Suspeição de Agentes e Julgadores"
pos_63 = text.find(ancora_63)
pos_64 = text.find("### 6.4 Motivação das Decisões", pos_63)
assert pos_63 != -1 and pos_64 != -1
text = text[:pos_64] + "\n\n" + q11_03.strip() + "\n\n---\n\n" + text[pos_64:]

ancora_41 = "### 4.1 Atos Simples, Complexos e Compostos"
pos_41 = text.find(ancora_41)
pos_42 = text.find("### 4.2 O Registro de Aposentadoria", pos_41)
assert pos_41 != -1 and pos_42 != -1
text = text[:pos_42] + "\n\n" + q10_03.strip() + "\n\n---\n\n" + text[pos_42:]

ancora_32 = "### 3.2 Autoexecutoriedade e seus Limites"
pos_32 = text.find(ancora_32)
pos_33 = text.find("### 3.3 Tipicidade Administrativa", pos_32)
assert pos_32 != -1 and pos_33 != -1
text = text[:pos_33] + "\n\n" + q09_03.strip() + "\n\n---\n\n" + text[pos_33:]

ancora_25 = "### 2.5 Objeto (Conteúdo) e a Delimitação do Mérito Administrativo"
pos_25 = text.find(ancora_25)
pos_30 = text.find("## 3. Atributos do Ato", pos_25)
assert pos_25 != -1 and pos_30 != -1
text = text[:pos_30] + "\n\n" + q08_03.strip() + "\n\n---\n\n" + text[pos_30:]

ancora_22 = "### 2.2 Finalidade e o Desvio de Poder"
pos_22 = text.find(ancora_22)
pos_23 = text.find("### 2.3 Forma e Princípio", pos_22)
assert pos_22 != -1 and pos_23 != -1
text = text[:pos_23] + "\n\n" + q07_03.strip() + "\n\n---\n\n" + text[pos_23:]

ancora_12 = "### 1.2 Perfeição, Validade e Eficácia do Ato"
pos_12 = text.find(ancora_12)
pos_20 = text.find("## 2. Elementos e Requisitos", pos_12)
assert pos_12 != -1 and pos_20 != -1
text = text[:pos_20] + "\n\n" + q06_03.strip() + "\n\n---\n\n" + text[pos_20:]

final_qs = re.findall(r"### Questão (\d+)", text)
print("Questões no arquivo 03:", final_qs)
assert len(final_qs) == 11
assert sorted(final_qs) == ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']

with open(f03_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Arquivo 03 gravado com sucesso! Total: 11 questões.")
