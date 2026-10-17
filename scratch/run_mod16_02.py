# -*- coding: utf-8 -*-
import os
import re

BASE_DIR = "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/16_licitacoes_e_contratos_administrativos"
f02_path = f"{BASE_DIR}/02_fases_modalidades_e_criterios_de_julgamento.md"
with open(f02_path, "r", encoding="utf-8") as f:
    t02 = f.read()

assert "### Questão 01" in t02
assert "### Questão 02" in t02
assert "### Questão 03" in t02
assert "### Questão 04" in t02
assert "### Questão 05" in t02

q06_02 = """### Questão 06 (FCC - Analista de Controle Externo / TCE-GO)
A Lei nº 14.133/2021 estruturou o processo de licitação em uma sequência de fases lógicas e sucessivas, positivada no caput do art. 17.

Assinale a opção que indica a ordem cronológica legal das fases da licitação, em sua regra geral:

* **A)** Habilitação, preparatória, divulgação do edital, apresentação de propostas, julgamento, homologação e recursal.
* **B)** Divulgação do edital, preparatória, habilitação, apresentação de propostas, julgamento, recursal e homologação.
* **C)** Preparatória, divulgação do edital de licitação, apresentação de propostas e lances, julgamento, habilitação, recursal e homologação.
* **D)** Preparatória, habilitação prévia de todos os concorrentes, divulgação do edital, julgamento, apresentação de lances, recursal e homologação.
* **E)** Divulgação do edital, julgamento, apresentação de propostas, habilitação, preparatória, recursal e homologação.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A habilitação não antecede a fase preparatória nem a divulgação do edital.
> - **B)** Incorreta. A fase preparatória (planejamento) é anterior à publicação do edital.
> - **C)** Correta. O art. 17 da Lei nº 14.133/2021 estabelece a seguinte sequência cronológica oficial das fases da licitação: I - preparatória; II - de divulgação do edital de licitação; III - de apresentação de propostas e lances, quando for o caso; IV - de julgamento; V - de habilitação; VI - recursal; VII - de homologação. Consagrou-se em definitivo como regra geral a análise de propostas (julgamento) antes da habilitação (inversão de fases legalizada).
> - **D)** Incorreta. A habilitação prévia era o modelo anacrônico da Lei nº 8.666/1993; na NLLC, a regra é julgar a proposta e habilitar apenas o licitante provisoriamente vencedor.
> - **E)** Incorreta. A fase preparatória é o ponto de partida indispensável de todo o certame.
>
> **Gabarito: C**"""

q07_02 = """### Questão 07 (FGV - Auditor de Controle Externo / TCE-PA)
A fase recursal na Nova Lei de Licitações e Contratos (art. 165 da Lei nº 14.133/2021) foi desenhada sob a lógica da concentração e celeridade procedimental.

Sobre as regras que disciplinam os recursos administrativos no processo licitatório, assinale a afirmativa correta.

* **A)** Cabe recurso administrativo autônomo com prazo de quinze dias úteis a cada decisão interlocutória do agente de contratação que rejeitar uma impugnação ao edital.
* **B)** A intenção de recorrer deve ser manifestada imediatamente, sob pena de preclusão, sendo o prazo para apresentação das razões recursais de três dias úteis, contados da data de intimação ou de lavratura da ata.
* **C)** Os recursos interpostos contra o julgamento de propostas têm efeito suspensivo automático e obrigatório sobre todas as fases subsequentes da licitação.
* **D)** O prazo para que os demais licitantes apresentem contrarrazões recursais é de dez dias úteis, independentemente do objeto licitado.
* **E)** O recurso administrativo independe de manifestação motivada prévia da intenção de recorrer em sessão pública.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O art. 165 unificou a fase recursal: os recursos contra o julgamento de propostas e a habilitação são concentrados em uma **única fase recursal** ao final do certame, vedando-se recursos fragmentados a cada ato intermediário.
> - **B)** Correta. O art. 165, § 1º, da Lei nº 14.133/2021 dispõe que a intenção de recorrer deverá ser manifestada **imediatamente, sob pena de preclusão**, e o prazo para apresentação das razões recursais será de **3 (três) dias úteis**, contado a partir da data de intimação ou de lavratura da ata de habilitação ou inabilitação.
> - **C)** Incorreta. O recurso contra julgamento e habilitação não tem efeito suspensivo automático; a concessão de efeito suspensivo é excepcional e depende de decisão justificada da autoridade (art. 168).
> - **D)** Incorreta. O prazo para apresentação de contrarrazões recursais é de **3 (três) dias úteis** (art. 165, § 1º), idêntico ao prazo das razões.
> - **E)** Incorreta. A ausência de manifestação imediata e motivada da intenção de recorrer em sessão implica a preclusão do direito de recurso.
>
> **Gabarito: B**"""

q08_02 = """### Questão 08 (FCC - Procurador do Estado)
Acerca da concorrência e do pregão na Lei nº 14.133/2021, considere que determinado órgão da Administração Pública estadual pretende contratar a construção de um complexo penitenciário de segurança máxima, classificado como obra de grande vulto e engenharia especial.

Para essa contratação, a Administração Pública:

* **A)** Pode optar discricionariamente pelo pregão presencial com critério de maior desconto sobre a taxa de administração.
* **B)** Deve adotar obrigatoriamente a modalidade concorrência, tendo em vista que o pregão é restrito a bens e serviços comuns, sendo vedado para obras e serviços especiais de engenharia.
* **C)** Pode utilizar a tomada de preços, desde que o valor total estimado da obra não ultrapasse o limite de trinta milhões de reais.
* **D)** Deve realizar convite internacional caso haja mais de cinco empresas especializadas cadastradas no Registro Cadastral Geral do Estado.
* **E)** Fica autorizada a dispensar a licitação em virtude de a obra envolver segurança penitenciária.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O art. 29 da Lei nº 14.133/2021 veda terminantemente a utilização do pregão para obras de engenharia e serviços especiais.
> - **B)** Correta. Nos termos do art. 6º, XXXVIII, e art. 28 da Lei nº 14.133/2021, a **concorrência** é a modalidade licitatória obrigatória para a contratação de bens e serviços especiais e de **obras de engenharia**. O pregão é exclusivo para bens e serviços comuns (art. 6º, XLI).
> - **C)** Incorreta. As modalidades Tomada de Preços e Convite foram **definitivamente extintas** pelo legislador na Lei nº 14.133/2021.
> - **D)** Incorreta. A modalidade convite não existe mais no ordenamento jurídico brasileiro.
> - **E)** Incorreta. Obras penitenciárias comuns ou especiais exigem licitação prévia; a dispensa do art. 75, VIII (emergência) ou IV (segurança nacional) restringe-se a situações fáticas de grave urgência comprovada.
>
> **Gabarito: B**"""

q09_02 = """### Questão 09 (FGV - Analista de Controle Externo / Auditoria)
A respeito da modalidade licitatória denominada concurso, disciplinada pelo art. 30 da Lei nº 14.133/2021, assinale a afirmativa correta.

* **A)** O concurso é a modalidade utilizada para a compra de bens comuns de prateleira com base no critério de julgamento de maior desconto.
* **B)** O concurso destina-se à escolha de trabalho técnico, científico ou artístico, cujo critério de julgamento será o de melhor técnica ou conteúdo artístico, e para concessão de prêmio ou remuneração ao vencedor.
* **C)** O prazo mínimo para apresentação dos trabalhos no concurso é de oito dias úteis, contados da data de publicação do edital.
* **D)** O julgamento dos trabalhos apresentados no concurso é realizado individualmente pelo pregoeiro do órgão, dispensada comissão técnica.
* **E)** O vencedor do concurso adquire o direito incondicional e automático de celebrar o contrato de execução da obra decorrente do projeto premiado.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A compra de bens comuns dá-se por pregão (art. 29), e não concurso.
> - **B)** Correta. O art. 30 da Lei nº 14.133/2021 prescreve que o **concurso** é a modalidade de licitação para escolha de trabalho técnico, científico ou artístico, mediante critério de julgamento de **melhor técnica ou conteúdo artístico**, e para concessão de prêmio ou remuneração ao vencedor.
> - **C)** Incorreta. O prazo mínimo para apresentação de propostas no concurso é de **no mínimo 45 (quarenta e cinco) dias úteis** (art. 55, I, 'c', da Lei nº 14.133/2021).
> - **D)** Incorreta. O julgamento do concurso deve ser efetuado por uma **comissão especial**, integrada por pessoas de ilibada reputação e reconhecido conhecimento na matéria (art. 30, § 1º).
> - **E)** Incorreta. O prêmio ou remuneração é a contraprestação do concurso; a eventual contratação do projeto executivo constitui etapa futura e condicionada às regras orçamentárias e legais.
>
> **Gabarito: B**"""

q10_02 = """### Questão 10 (FCC - Técnico de Controle Externo)
Na disciplina dos critérios de julgamento da Lei nº 14.133/2021 (art. 33), assinale a afirmativa que expressa corretamente a regra legal aplicável ao critério de julgamento por 'técnica e preço'.

* **A)** A pontuação atribuída à proposta de preço deve obrigatoriamente representar no mínimo 80% da valoração total do julgamento.
* **B)** O critério de técnica e preço é privativo da modalidade leilão, sendo vedado em concorrências.
* **C)** No critério de técnica e preço, a atribuição de fatores de ponderação distintos para a valoração técnica e de preço não pode resultar em peso da proposta técnica superior a 70% (setenta por cento).
* **D)** O julgamento por técnica e preço pode ser utilizado discricionariamente para a compra de qualquer material de consumo rotineiro e padronizado.
* **E)** A proposta técnica é julgada após a abertura da proposta de preços em sessão secreta.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Não existe exigência de mínimo de 80% para preço; o limitador legal foca no teto da técnica.
> - **B)** Incorreta. O leilão utiliza exclusivamente o critério de **maior lance** (art. 33, V); técnica e preço aplica-se à concorrência.
> - **C)** Correta. O art. 36, § 1º, da Lei nº 14.133/2021 estatui categoricamente: *"O desempenho do critério de julgamento de que trata o caput deste artigo dar-se-á por meio da valoração das propostas técnicas e de preço, em que a pontuação atribuída à proposta técnica não poderá ser superior a 70% (setenta por cento)"*.
> - **D)** Incorreta. Bens de consumo padronizados e comuns devem ser licitados por menor preço ou maior desconto (art. 34 e art. 29).
> - **E)** Incorreta. A proposta técnica é julgada antes da proposta de preço, em sessões públicas e transparentes.
>
> **Gabarito: C**"""

q11_02 = """### Questão 11 (FGV - Analista Jurídico de Controle Externo / TCE-GO)
Os modos de disputa na Lei nº 14.133/2021 podem ser abertos, fechados ou combinados, nos termos do art. 56.

A respeito da utilização dos modos de disputa e dos prazos mínimos de divulgação do edital (art. 55), assinale a afirmativa correta.

* **A)** É permitida a adoção isolada do modo de disputa fechado quando o critério de julgamento for o de menor preço ou maior desconto.
* **B)** É vedada a utilização isolada do modo de disputa fechado quando forem adotados os critérios de julgamento de menor preço ou de maior desconto.
* **C)** O modo de disputa aberto consiste na apresentação de propostas em envelopes lacrados, sem oportunidade de lances sucessivos pelos competidores.
* **D)** Para a contratação de obras de grande vulto pelo critério de melhor técnica, o prazo mínimo de divulgação do edital é de cinco dias úteis.
* **E)** No pregão, o modo de disputa fechado pode ser adotado isoladamente sempre que a autoridade competente julgar conveniente.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. É expressamente proibida a utilização isolada do modo fechado para menor preço ou maior desconto.
> - **B)** Correta. O art. 56, § 1º, da Lei nº 14.133/2021 estipula que *"A utilização do modo de disputa fechado será vedada quando adotados os critérios de julgamento de menor preço ou de maior desconto"*. Nesses casos, exige-se o modo aberto ou a combinação de aberto e fechado, permitindo lances públicos sucessivos para maximizar a economia estatal.
> - **C)** Incorreta. O modo aberto é aquele em que os licitantes apresentam lances públicos e sucessivos, crescentes ou decrescentes; apresentação sigilosa em envelope sem lances é o modo **fechado**.
> - **D)** Incorreta. Para obras e serviços sob melhor técnica ou técnica e preço, o prazo mínimo é substancialmente superior: **35 (trinta e cinco) dias úteis** ou até **60 (sessenta) dias úteis** se houver regime de contratação integrada (art. 55, II, 'b' e 'c').
> - **E)** Incorreta. No pregão, por utilizar menor preço ou maior desconto, é vedado o modo de disputa exclusivamente fechado.
>
> **Gabarito: B**"""

# Inserções no arquivo 02 de trás para frente
ancora_41 = "### 4.1 Modos de Disputa: Aberto, Fechado e Combinações (Art. 56)"
pos_41 = t02.find(ancora_41)
pos_42 = t02.find("### 4.2 Prazos Mínimos", pos_41)
assert pos_41 != -1 and pos_42 != -1
t02 = t02[:pos_42] + "\n\n" + q11_02.strip() + "\n\n---\n\n" + t02[pos_42:]

ancora_33 = "### 3.3 Técnica e Preço e o Limite de Ponderação"
pos_33 = t02.find(ancora_33)
pos_34 = t02.find("### 3.4 Maior Lance", pos_33)
assert pos_33 != -1 and pos_34 != -1
t02 = t02[:pos_34] + "\n\n" + q10_02.strip() + "\n\n---\n\n" + t02[pos_34:]

ancora_23 = "### 2.3 Concurso: Premiação de Trabalhos Técnicos e Artísticos"
pos_23 = t02.find(ancora_23)
pos_24 = t02.find("### 2.4 Leilão: A Nova Sistemática", pos_23)
assert pos_23 != -1 and pos_24 != -1
t02 = t02[:pos_24] + "\n\n" + q09_02.strip() + "\n\n---\n\n" + t02[pos_24:]

ancora_22 = "### 2.2 Concorrência: Bens e Serviços Especiais e Obras"
pos_22 = t02.find(ancora_22)
pos_23_new = t02.find("### 2.3 Concurso: Premiação", pos_22)
assert pos_22 != -1 and pos_23_new != -1
t02 = t02[:pos_23_new] + "\n\n" + q08_02.strip() + "\n\n---\n\n" + t02[pos_23_new:]

ancora_13 = "### 1.3 Fase Recursal Única e Concentrada (Art. 165)"
pos_13 = t02.find(ancora_13)
pos_20 = t02.find("## 2. As Cinco Modalidades", pos_13)
assert pos_13 != -1 and pos_20 != -1
t02 = t02[:pos_20] + "\n\n" + q07_02.strip() + "\n\n---\n\n" + t02[pos_20:]

ancora_11 = "### 1.1 Sequência Cronológica Canônica (Art. 17)"
pos_11 = t02.find(ancora_11)
pos_12 = t02.find("### 1.2 A Inversão de Fases", pos_11)
assert pos_11 != -1 and pos_12 != -1
t02 = t02[:pos_12] + "\n\n" + q06_02.strip() + "\n\n---\n\n" + t02[pos_12:]

qs_02 = re.findall(r"### Questão (\d+)", t02)
print("Questões no arquivo 02 do Módulo 16:", qs_02)
assert len(qs_02) == 11
assert sorted(qs_02) == ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']

with open(f02_path, "w", encoding="utf-8") as f:
    f.write(t02)

print("Arquivo 02 do Módulo 16 gravado com sucesso! Total: 11 questões.")
