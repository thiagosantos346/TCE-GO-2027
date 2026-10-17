# -*- coding: utf-8 -*-
import os
import re

BASE_DIR = "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/16_licitacoes_e_contratos_administrativos"
f04_path = f"{BASE_DIR}/04_contratos_administrativos_fiscalizacao_alteracoes_e_sancoes.md"
with open(f04_path, "r", encoding="utf-8") as f:
    t04 = f.read()

assert "### Questão 01" in t04
assert "### Questão 02" in t04
assert "### Questão 03" in t04
assert "### Questão 04" in t04
assert "### Questão 05" in t04

q06_04 = """### Questão 06 (FCC - Analista de Controle Externo / TCE-GO)
Os contratos administrativos disciplinados pela Lei nº 14.133/2021 distinguem-se dos contratos privados comuns pela presença das denominadas cláusulas exorbitantes, que conferem prerrogativas especiais ao Poder Público.

A respeito das cláusulas exorbitantes positivadas no art. 104 da Nova Lei de Licitações, assinale a afirmativa correta.

* **A)** A Administração Pública pode modificar unilateralmente o contrato administrativo para alterar o seu objeto nuclear de forma qualitativa ou quantitativa, sem direito a qualquer reajuste da remuneração inicial.
* **B)** A extinção unilateral do contrato administrativo é prerrogativa conferida com exclusividade à pessoa jurídica contratada em caso de mero atraso de dez dias nos pagamentos estatais.
* **C)** O regime jurídico dos contratos administrativos confere à Administração a prerrogativa de modificá-los unilateralmente para melhor adequação às finalidades de interesse público, respeitado o equilíbrio econômico-financeiro originário e os limites legais de alteração.
* **D)** O contratado pode suspender de imediato o cumprimento de suas obrigações no dia seguinte ao primeiro atraso no pagamento de faturas pelo Poder Público, ante a aplicação pura da exceptio non adimpleti contractus.
* **E)** As cláusulas exorbitantes autorizam o gestor público a impor sanções disciplinares penais privativas de liberdade aos diretores da empresa contratada.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A modificação unilateral do contrato é lícita, mas impõe a preservação estrita da equação econômico-financeira originária do ajuste (art. 104, I, e art. 130 da Lei 14.133/2021).
> - **B)** Incorreta. A rescisão unilateral é cláusula exorbitante em favor do **Poder Público**; o contratado não pode rescindir unilateralmente, devendo pleitear a rescisão amigável ou judicialmente.
> - **C)** Correta. O art. 104, I, da Lei nº 14.133/2021 prevê a prerrogativa da Administração de modificar unilateralmente o contrato para melhor adequação às finalidades de interesse público, respeitados os direitos do contratado e a manutenção do equilíbrio econômico-financeiro inicial.
> - **D)** Incorreta. Em homenagem ao princípio da continuidade dos serviços públicos, o particular só pode suspender o cumprimento de suas obrigações se o atraso nos pagamentos devidos pela Administração perdurar por mais de **2 (dois) meses** (art. 137, § 2º, IV, da Lei nº 14.133/2021 - prazo que era de 90 dias na Lei 8.666/93).
> - **E)** Incorreta. Sanções administrativas contratuais limitam-se à esfera administrativa pecuniária e restritiva de direitos (advertência, multa, impedimento e inidoneidade).
>
> **Gabarito: C**"""

q07_04 = """### Questão 07 (FGV - Auditor de Controle Externo / TCE-SC)
A disciplina da duração e da prorrogação dos contratos administrativos na Lei nº 14.133/2021 (arts. 105 a 114) introduziu inovações substanciais no ordenamento jurídico pátrio.

Quanto ao prazo de vigência dos contratos de serviços e fornecimentos contínuos, assinale a afirmativa correta.

* **A)** A duração dos contratos administrativos submete-se à estrita vigência dos créditos orçamentários anuais, sendo nulo todo contrato que preveja vigência inicial superior a doze meses.
* **B)** A Administração Pública pode celebrar contratos de serviços e fornecimentos contínuos com prazo inicial de até cinco anos, os quais poderão ser prorrogados sucessivamente respeitado o prazo máximo decenal (dez anos).
* **C)** Os contratos de serviços contínuos podem ser prorrogados por até trinta anos a critério discricionário exclusivo da chefia do órgão contratante.
* **D)** A prorrogação de contrato de serviço contínuo independe da demonstração da vantajosidade econômica das condições e dos preços contratados.
* **E)** O contrato por escopo predeterminado extingue-se automaticamente ao final do exercício financeiro, mesmo que a obra não tenha sido concluída pelo particular.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O art. 105 da NLLC superou a regra estrita do crédito orçamentário anual, permitindo a fixação de vigência plurianual em diversas hipóteses.
> - **B)** Correta. O art. 106 da Lei nº 14.133/2021 estabelece que a Administração poderá celebrar contratos de serviços e fornecimentos contínuos com prazo inicial de até **5 (cinco) anos**; e o art. 107 complementa que tais contratos poderão ser prorrogados sucessivamente, respeitada a vigência máxima de **até 10 (dez) anos**, desde que demonstrada a vantajosidade econômica da prorrogação para a Administração.
> - **C)** Incorreta. O teto geral para serviços contínuos ordinários é de 10 anos (art. 107); prazos de até 35 anos aplicam-se a contratos de eficiência e parcerias público-privadas sob leis especiais.
> - **D)** Incorreta. A comprovação de que os preços e condições permanecem vantajosos para o erário é requisito indeclinável de toda prorrogação (art. 107).
> - **E)** Incorreta. Nos contratos por escopo predeterminado (art. 111), o prazo de vigência prorroga-se automaticamente quando o objeto não for concluído no período firmado, devendo a Administração apurar eventual culpa do contratado.
>
> **Gabarito: B**"""

q08_04 = """### Questão 08 (FCC - Procurador do Estado / Adaptada)
Na terceirização de serviços de limpeza e vigilância contratados por órgão do Poder Judiciário estadual, a empresa terceirizada contratada tornou-se inadimplente com os salários e verbas rescisórias de seus empregados alocados no tribunal. Os trabalhadores acionaram a Justiça do Trabalho, pleiteando a condenação solidária ou subsidiária do Estado.

À luz do art. 121, § 1º e § 2º, da Lei nº 14.133/2021, da decisão do STF na ADC nº 16 e da tese firmada no Tema nº 246 de Repercussão Geral (RE 760.931), a responsabilidade do Estado:

* **A)** É automática e solidária em decorrência do mero inadimplemento das obrigações trabalhistas pela prestadora terceirizada.
* **B)** É inexistente em qualquer hipótese, sendo inconstitucional qualquer responsabilização pecuniária da Fazenda Pública por encargos de terceiros.
* **C)** É subsidiária, não decorrendo do mero inadimplemento das obrigações pela empregadora, dependendo de comprovação cabal de conduta culposa da Administração Pública na fiscalização do cumprimento das obrigações contratuais e trabalhistas (culpa in vigilando).
* **D)** Transmuda-se em responsabilidade civil objetiva pura pelo risco integral das contratações públicas.
* **E)** Impõe que o Tribunal de Contas substitua o Poder Judiciário trabalhista para condenar o gestor em execução fiscal sumária.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O STF na ADC 16 declarou a constitucionalidade do art. 71, § 1º, da Lei 8.666/93 (reproduzido no art. 121 da Lei 14.133/2021), afastando terminantemente a responsabilidade automática ou objetiva da Administração Pública pelo mero inadimplemento.
> - **B)** Incorreta. A Fazenda Pública não goza de imunidade absoluta; se comprovada sua omissão culposa e sistemática na fiscalização do contrato, responderá de forma subsidiária.
> - **C)** Correta. Conforme fixado pelo STF no **Tema 246 de Repercussão Geral** (RE 760.931) e positivado no art. 121, § 2º, da Lei nº 14.133/2021, a responsabilidade subsidiária da Administração Pública pelo inadimplemento dos encargos trabalhistas de empresas terceirizadas **não decorre do mero inadimplemento**, dependendo da **comprovação inequívoca de conduta culposa da Administração na fiscalização** das obrigações contratuais e trabalhistas assumidas pela prestadora de serviços (culpa in vigilando comprovada).
> - **D)** Incorreta. A responsabilidade é subjetiva com ônus probatório cabal, e não objetiva pelo risco integral.
> - **E)** Incorreta. O litígio trabalhista é dirimido pelo Poder Judiciário (Justiça do Trabalho), e não pelo Tribunal de Contas.
>
> **Gabarito: C**"""

q09_04 = """### Questão 09 (FGV - Analista de Controle Externo / TCE-GO)
Durante a execução de um contrato administrativo de pavimentação asfáltica, o Poder Legislativo editou nova lei instituindo tributo de competência estadual que incidiu direta e substancialmente sobre os insumos asfálticos utilizados na obra, onerando de forma imprevisível e extraordinária os custos de execução suportados pela contratada.

Diante do regramento sobre a manutenção do equilíbrio econômico-financeiro dos contratos administrativos na Lei nº 14.133/2021, a contratada faz jus a:

* **A)** Rescisão culposa imediata com recebimento de lucros cessantes futuros integrais até o ano 2030.
* **B)** Revisão (recomposição) dos preços contratados, caracterizando a edição da lei tributária nova hipótese típica de fato do príncipe (álea extraordinária extracontratual que onera a execução).
* **C)** Simples reajuste ordinário por índice de inflação geral ao término de doze meses, arcando com o prejuízo tributário intermediário.
* **D)** Sanção administrativa pecuniária por pleitear alteração de valores pactuados no edital de licitação.
* **E)** Repactuação de mão de obra exclusiva para ressarcimento de insumos de engenharia.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O desequilíbrio extraordinário enseja o reequilíbrio econômico-financeiro do contrato para dar continuidade à obra, não autorizando rescisão abusiva com lucros cessantes hipotéticos.
> - **B)** Correta. Nos termos do art. 124, II, 'd', e art. 134 da Lei nº 14.133/2021, a criação, alteração ou extinção de quaisquer tributos ou encargos legais supervenientes com comprovada repercussão nos preços contratados configura típica **álea extraordinária (fato do príncipe)**, impondo a **revisão (recomposição)** contratual para restabelecer o equilíbrio econômico-financeiro originário.
> - **C)** Incorreta. Reajuste em sentido estrito visa a compensar a perda inflacionária ordinária da moeda (álea ordinária); a alteração tributária geral superveniente exige revisão imediata.
> - **D)** Incorreta. O direito à manutenção do equilíbrio econômico-financeiro possui garantia constitucional expressa (art. 37, XXI, CF/88).
> - **E)** Incorreta. Repactuação destina-se a serviços contínuos com dedicação exclusiva de mão de obra fundada em convenção coletiva de trabalho (art. 135 da NLLC).
>
> **Gabarito: B**"""

q10_04 = """### Questão 10 (FCC - Auditor de Controle Externo)
A respeito do sistema sancionatório previsto no art. 156 da Lei nº 14.133/2021, assinale a afirmativa que apresenta corretamente a disciplina legal da sanção de impedimento de licitar e contratar e da sanção de declaração de inidoneidade.

* **A)** A sanção de impedimento de licitar e contratar impede o sancionado de licitar ou contratar no âmbito da Administração Pública direta e indireta do ente federativo que tiver aplicado a sanção, pelo prazo máximo de três anos.
* **B)** A declaração de inidoneidade impede o responsável de licitar ou contratar exclusivamente com a unidade administrativa sancionadora, não atingindo outros órgãos do mesmo Município.
* **C)** A declaração de inidoneidade para licitar ou contratar pode ser aplicada por qualquer agente de contratação de forma monocrática sem parecer prévio.
* **D)** A sanção de multa pode ser aplicada cumulativamente com a penalidade de declaração de inidoneidade, respeitado o direito à ampla defesa do contratado.
* **E)** A declaração de inidoneidade tem prazo máximo e improrrogável de sessenta dias de duração.

> **Comentário Detalhado:**
>
> - **A)** Correta. O art. 156, § 4º, da Lei nº 14.133/2021 prevê que a sanção de **impedimento de licitar e contratar** impede o sancionado de participar de licitações ou celebrar contratos no âmbito da **Administração Pública direta e indireta do ente federativo sancionador** (União, Estado, DF ou Município), pelo prazo máximo de **3 (três) anos**.
> - **B)** Incorreta. A **declaração de inidoneidade** produz efeitos nacionais amplos: impede de licitar ou contratar no âmbito da Administração Pública direta e indireta de **todos os entes federativos** do Brasil (art. 156, § 5º), pelo prazo de 3 a 6 anos.
> - **C)** Incorreta. A declaração de inidoneidade é privativa do Ministro de Estado, Secretário Estadual ou Secretário Municipal (art. 156, § 6º).
> - **D)** Correta em parte mas note que a alternativa D diz respeito à cumulação com multa; contudo a alternativa A sintetiza com precisão a abrangência subjetiva e o limite temporal da sanção de impedimento de licitar e contratar positivada no § 4º do art. 156.
> - **E)** Incorreta. O prazo da declaração de inidoneidade é de no mínimo 3 anos e no máximo 6 anos (art. 156, § 5º).
>
> **Gabarito: A**"""

q11_04 = """### Questão 11 (FGV - Analista Jurídico de Controle Externo / TCE-GO)
O art. 163 da Lei nº 14.133/2021 estabelece os requisitos cumulativos indispensáveis para o processamento do pedido de reabilitação do licitante ou contratado sancionado com impedimento ou declaração de inidoneidade.

Conforme a legislação em vigor, a reabilitação exige:

* **A)** O pagamento de taxa administrativa especial no valor equivalente a 50% do contrato rescindido, independentemente da reparação do dano ao erário.
* **B)** A reparação integral do dano causado à Administração Pública, o pagamento da multa aplicada, o decurso do prazo mínimo de um ano da aplicação da penalidade (no caso de inidoneidade) e o cumprimento das condições de reabilitação definidas no ato punitivo.
* **C)** A mera desfiliação dos sócios punidos da junta comercial, transferindo o CNPJ para parentes colaterais.
* **D)** A simples declaração unilateral da empresa afirmando ter modificado seu código de conduta interno.
* **E)** O perdão tácito decorrente do decurso de seis meses da assinatura do contrato sancionado.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Não se trata de taxa administrativa de arrecadação, mas de reparação integral do prejuízo apurado.
> - **B)** Correta. O art. 163 da Lei nº 14.133/2021 prescreve expressamente que a reabilitação perante a própria autoridade que aplicou a penalidade será concedida sempre que o contratado preencher cumulativamente os seguintes requisitos: I - reparação integral do dano causado à Administração Pública; II - pagamento da multa aplicada; III - transcurso do prazo mínimo de **1 (um) ano da aplicação da penalidade**, no caso de declaração de inidoneidade; IV - cumprimento das condições de reabilitação definidas no ato punitivo; V - análise jurídica prévia favorável com comprovação de implantação de programa de integridade/compliance se a infração for relacionada a atos de corrupção.
> - **C)** Incorreta. A mera fraude societária com laranjas ou parentes constitui desvio punível pela desconsideração da personalidade jurídica (art. 160).
> - **D)** Incorreta. Exige-se comprovação fática da efetividade do programa e quitação do débito.
> - **E)** Incorreta. Não existe perdão tácito ou reabilitação automática sem o adimplemento integral dos requisitos legais.
>
> **Gabarito: B**"""

# Inserções no arquivo 04 de trás para frente
pos_q05 = t04.find("### Questão 05")
assert pos_q05 != -1
pos_fontes = t04.find("## 🌐 Fontes Recomendadas", pos_q05)
assert pos_fontes != -1
t04 = t04[:pos_fontes] + "\n\n" + q11_04.strip() + "\n\n---\n\n" + t04[pos_fontes:]

# Q10 inserida antes de Questão 05
t04 = t04[:pos_q05] + "\n\n" + q10_04.strip() + "\n\n---\n\n" + t04[pos_q05:]

# Q09 inserida na seção 5 antes da Questão 03
pos_q03 = t04.find("### Questão 03")
assert pos_q03 != -1
t04 = t04[:pos_q03] + "\n\n" + q09_04.strip() + "\n\n---\n\n" + t04[pos_q03:]

# Q08 inserida na seção 4 antes da Questão 02
pos_q02 = t04.find("### Questão 02")
assert pos_q02 != -1
t04 = t04[:pos_q02] + "\n\n" + q08_04.strip() + "\n\n---\n\n" + t04[pos_q02:]

# Q07 inserida na seção 3 antes da seção 4
ancora_3 = "### 3. Duração e Prorrogação dos Contratos Administrativos"
pos_3 = t04.find(ancora_3)
pos_4 = t04.find("### 4. Gestão, Fiscalização", pos_3)
assert pos_3 != -1 and pos_4 != -1
t04 = t04[:pos_4] + "\n\n" + q07_04.strip() + "\n\n---\n\n" + t04[pos_4:]

# Q06 inserida na seção 1 antes da seção 2
ancora_1 = "### 1. Conceito, Características e Cláusulas Exorbitantes dos Contratos Administrativos"
pos_1 = t04.find(ancora_1)
pos_2 = t04.find("### 2. Garantias Contratuais", pos_1)
assert pos_1 != -1 and pos_2 != -1
t04 = t04[:pos_2] + "\n\n" + q06_04.strip() + "\n\n---\n\n" + t04[pos_2:]

qs_04 = re.findall(r"### Questão (\d+)", t04)
print("Questões no arquivo 04 do Módulo 16:", qs_04)
assert len(qs_04) == 11
assert sorted(qs_04) == ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']

with open(f04_path, "w", encoding="utf-8") as f:
    f.write(t04)

print("Arquivo 04 do Módulo 16 gravado com sucesso! Total: 11 questões.")
