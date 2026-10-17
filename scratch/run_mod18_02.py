# -*- coding: utf-8 -*-
import os
import re

BASE_DIR = "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/18_nocoes_de_controle_externo"
f02_path = f"{BASE_DIR}/02_instrumentos_e_tipos_de_auditoria_governamental_nbasp.md"
with open(f02_path, "r", encoding="utf-8") as f:
    t02 = f.read()

assert "### Questão 01" in t02
assert "### Questão 02" in t02
assert "### Questão 03" in t02
assert "### Questão 04" in t02
assert "### Questão 05" in t02

q06_02 = """### Questão 06 (FCC - Auditor de Controle Externo / TCE-GO)
Os regimentos internos dos Tribunais de Contas e as normas de fiscalização tipificam diferentes instrumentos de fiscalização para a consecução do controle externo: auditoria, levantamento, acompanhamento, monitoramento e inspeção.

A respeito das finalidades específicas do 'monitoramento' e do 'levantamento', assinale a afirmativa correta.

* **A)** O monitoramento é o instrumento utilizado privativamente para apurar denúncias anônimas de fraudes graves que demandem busca e apreensão.
* **B)** O monitoramento é o instrumento de fiscalização utilizado para verificar o cumprimento das deliberações do Tribunal de Contas (determinações e recomendações) e os resultados delas decorrentes.
* **C)** O levantamento destina-se a aplicar multas diárias imediatas aos gestores faltosos sem oportunizar o contraditório.
* **D)** A inspeção substitui a tomada de contas especial nos casos de desfalque comprovado de recursos financeiros.
* **E)** O acompanhamento destina-se exclusivamente a fiscalizar contratos já liquidados e pagos há mais de dez anos.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O instrumento adequado para apurar denúncias pontuais com urgência in loco é a **inspeção**.
> - **B)** Correta. Conceito regimental e normativo canônico dos Tribunais de Contas (RI/TCU e RI/TCE-GO): o **monitoramento** é o instrumento de controle externo utilizado para averiguar o cumprimento das deliberações do Tribunal (acórdãos, recomendações e determinações) e avaliar o impacto positivo das medidas corretivas adotadas pela entidade auditada. O **levantamento** visa a conhecer a organização e o funcionamento das instituições para identificar objetos e viabilidade de futuras auditorias.
> - **C)** Incorreta. O levantamento é instrumento de diagnóstico de sistemas e planejamento, não possuindo viés punitivo direto.
> - **D)** Incorreta. A tomada de contas especial é processo específico de ressarcimento de dano que não se confunde com inspeção.
> - **E)** Incorreta. O acompanhamento fiscaliza a gestão em tempo real (concomitantemente), e não fatos de uma década atrás.
>
> **Gabarito: B**"""

q07_02 = """### Questão 07 (FGV - Auditor de Controle Externo / TCE-SC)
A NBASP 300 (Norma Brasileira de Auditoria do Setor Público equivalente à ISSAI 300) estabelece os princípios e as diretrizes fundamentais da auditoria operacional (ou de desempenho).

Sobre os objetivos e as dimensões avaliadas na auditoria operacional (princípios dos 4 Es), assinale a afirmativa correta.

* **A)** A auditoria operacional limita-se a conferir a fidedignidade contábil dos balanços patrimoniais e a regularidade fiscal das notas de empenho.
* **B)** A auditoria operacional examina a gestão pública sob os critérios de economicidade (minimização dos custos dos recursos sem comprometer a qualidade), eficiência (obtenção do máximo rendimento dos recursos empregados) e eficácia (grau de alcance dos objetivos e metas estabelecidos).
* **C)** Na auditoria operacional, o auditor emite uma opinião formal com certificação padronizada sobre as demonstrações financeiras nos moldes de parecer de auditoria contábil independente.
* **D)** A dimensão da efetividade na auditoria operacional preocupa-se exclusivamente com a rapidez na assinatura dos contratos administrativos de compras públicas.
* **E)** A auditoria operacional é terminantemente proibida de emitir recomendações aos gestores públicos sobre melhorias procedimentais.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A conferência contábil de balanços é objeto precípuo da **auditoria financeira**; a conformidade de empenhos é da **auditoria de conformidade**.
> - **B)** Correta. A teor da NBASP 300 e da doutrina consolidada, a **auditoria operacional** avalia o desempenho dos programas, órgãos e políticas públicas com foco na **economicidade** (relação insumo/custo), **eficiência** (relação insumo/produto), **eficácia** (relação produto/meta) e **efetividade** (impacto social real na população).
> - **C)** Incorreta. A emissão de parecer/opinião sobre demonstrações financeiras é privativa da **auditoria financeira**. A auditoria operacional conclui com relatório analítico de achados e recomendações de aperfeiçoamento gerencial.
> - **D)** Incorreta. A efetividade avalia o alcance dos resultados e os impactos sociais de longo prazo da política pública (ex.: redução da mortalidade infantil, e não simples celeridade na compra de remédios).
> - **E)** Incorreta. As recomendações propositivas constituem o principal produto e valor agregado da auditoria de desempenho.
>
> **Gabarito: B**"""

q08_02 = """### Questão 08 (FCC - Analista de Controle Externo / TCE-GO)
De acordo com a estrutura normativa da NBASP / INTOSAI, a auditoria do setor público divide-se em três tipos principais: auditoria financeira, auditoria de conformidade e auditoria operacional.

Assinale a afirmativa que apresenta a correta caracterização da 'auditoria financeira':

* **A)** Foca no exame da moralidade subjetiva dos agentes públicos para avaliar desvios de conduta privada.
* **B)** Concentra-se em determinar se as informações financeiras de uma entidade são apresentadas, em todos os aspectos relevantes, em conformidade com a estrutura de relatório financeiro e o arcabouço contábil aplicável, emitindo o auditor uma opinião sobre a fidedignidade dessas demonstrações (NBASP 200).
* **C)** Destina-se com exclusividade a punir disciplinarmente os chefes de tesouraria de municípios com menos de dez mil habitantes.
* **D)** Tem como objeto unicamente a legalidade dos processos licitatórios de obras rodoviárias.
* **E)** Prescinde do conceito de materialidade e relevância, exigindo a checagem individualizada de 100% dos lançamentos contábeis do órgão.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A auditoria financeira examina dados e demonstrações contábeis e orçamentárias, não vida privada de agentes.
> - **B)** Correta. A NBASP 200 / ISSAI 200 define que a **auditoria financeira** visa a obter segurança razoável de que as demonstrações financeiras tomadas em conjunto estão livres de distorções relevantes, decorrentes de fraude ou erro, permitindo ao auditor expressar uma opinião técnica fundamentada sobre se as demonstrações refletem adequadamente a situação patrimonial e orçamentária do ente.
> - **C)** Incorreta. Aplica-se a todos os entes públicos jurisdicionados e não visa a aplicar penas disciplinares funcionais.
> - **D)** Incorreta. O exame de licitações é objeto clássico da auditoria de **conformidade**.
> - **E)** Incorreta. O conceito de **materialidade** (relevância econômica e qualitativa) é pilar estruturante da auditoria financeira.
>
> **Gabarito: B**"""

q09_02 = """### Questão 09 (FGV - Auditor de Controle Externo / TCE-SC)
A NBASP 100 (Princípios Fundamentais de Auditoria do Setor Público) estabelece que uma auditoria do setor público envolve tipicamente três partes distintas que se relacionam no processo fiscalizatório.

Essas três partes são:

* **A)** O Poder Executivo, o Poder Legislativo e o Poder Judiciário.
* **B)** O auditor (representado pela equipe do Tribunal de Contas), a parte responsável (os gestores públicos responsáveis pela gestão dos recursos e pela informação objeto do controle) e os usuários previstos (os órgãos legislativos, os órgãos de controle e a sociedade/cidadãos).
* **C)** O autor da representação, o réu e a testemunha de acusação.
* **D)** A empresa contratada, o banco financiador e o engenheiro fiscal de obras.
* **E)** O Ministério Público de Contas, a Controladoria-Geral da União e a Polícia Federal.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Trata-se da divisão constitucional clássica dos Poderes estatais.
> - **B)** Correta. Conforme a NBASP 100 (item 25), a auditoria do setor público estrutura-se na relação entre **três partes fundamentais**: (1) **O Auditor**: a pessoa ou equipe que conduz a auditoria vinculada à Entidade Fiscalizadora Superior (Tribunal de Contas); (2) **A Parte Responsável**: os indivíduos ou órgãos responsáveis pelo objeto da auditoria (gestores públicos executores); (3) **Os Usuários Previstos**: aqueles para quem o auditor prepara o relatório de auditoria (o Parlamento, órgãos reguladores e o público em geral/sociedade).
> - **C)** Incorreta. Relação processual penal/civil, e não estrutura conceitual de auditoria pública.
> - **D)** Incorreta. Partes de relação contratual de engenharia.
> - **E)** Incorreta. Órgãos autônomos de fiscalização e persecução.
>
> **Gabarito: B**"""

q10_02 = """### Questão 10 (FCC - Técnico de Controle Externo / TCE-GO)
De acordo com os princípios da NBASP 100 e do Código de Ética das Entidades Fiscalizadoras Superiores (NBASP 30), o auditor do Tribunal de Contas deve pautar sua conduta profissional pelo ceticismo profissional e pelo julgamento profissional.

Sobre esses atributos, assinale a afirmativa correta.

* **A)** O ceticismo profissional impõe que o auditor assuma previamente que todo gestor público é culpado por dolo de corrupção, cabendo ao auditado provar sua inocência moral.
* **B)** O ceticismo profissional implica manter uma postura que inclui uma mente questionadora e alerta a condições que possam indicar possíveis distorções decorrentes de erro ou fraude, com avaliação crítica das evidências obtidas ao longo de todo o trabalho de auditoria.
* **C)** O julgamento profissional autoriza o auditor a ignorar normas técnicas e determinar sanções com base em impressões subjetivas pessoais.
* **D)** A independência do auditor é irrelevante quando a auditoria envolver órgãos de seu próprio círculo de amizade íntima.
* **E)** O auditor do Tribunal de Contas fica desobrigado de manter sigilo profissional sobre informações reservadas obtidas durante os trabalhos de campo.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O ceticismo profissional não se confunde com presunção preconceituosa de má-fé ou perseguição pessoal; é postura técnica imparcial e prudente.
> - **B)** Correta. A NBASP 100 define o **ceticismo profissional** como a atitude que inclui uma mente questionadora, alerta a condições que possam indicar distorções em decorrência de erro ou fraude, e uma avaliação crítica das evidências de auditoria. O auditor não presume que a administração seja desonesta nem assume sua honestidade inquestionável sem evidências corroborativas.
> - **C)** Incorreta. O julgamento profissional é a aplicação de conhecimento e experiência técnica às circunstâncias concretas para tomar decisões fundamentadas nos limites das normas de auditoria.
> - **D)** Incorreta. A independência e a imparcialidade são os pilares éticos máximos do auditor (NBASP 30); amizade íntima é causa expressa de suspeição/impedimento.
> - **E)** Incorreta. O sigilo profissional e a confidencialidade são deveres funcionais indeclináveis.
>
> **Gabarito: B**"""

q11_02 = """### Questão 11 (FGV - Analista Jurídico de Controle Externo / TCE-GO)
A Declaração de Lima, adotada no IX Congresso da Organização Internacional das Entidades Fiscalizadoras Superiores (INTOSAI) em 1977, é reconhecida mundialmente como a 'Carta Magna da Auditoria Governamental'.

A respeito dos postulados consagrados pela Declaração de Lima, assinale a afirmativa correta.

* **A)** As Entidades Fiscalizadoras Superiores (Tribunais de Contas) devem ser subordinadas hierarquicamente ao Ministério da Fazenda para assegurar o equilíbrio fiscal.
* **B)** A independência das Entidades Fiscalizadoras Superiores e de seus membros em relação às instituições auditadas, garantida pela Constituição e pelas leis, constitui condição indispensável para a credibilidade e a eficácia do controle externo das finanças públicas.
* **C)** O controle financeiro externo deve ser exclusivamente a posteriori, sendo vedado qualquer exame prévio ou concomitante de operações públicas.
* **D)** A fiscalização do uso dos recursos públicos deve ser sigilosa e inacessível aos cidadãos, para não constranger os gestores governamentais.
* **E)** As decisões dos órgãos de controle externo submetem-se à homologação prévia da chefia do Poder Executivo.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A Declaração de Lima veda veementemente a subordinação das Cortes de Contas a qualquer órgão do Poder Executivo.
> - **B)** Correta. A Declaração de Lima estatui no seu artigo 1º que o controle das finanças públicas é indispensável e que *"as Entidades Fiscalizadoras Superiores só poderão desempenhar suas funções com eficácia se forem **independentes da instituição auditada e protegidas contra influências externas**"*. Essa independência deve estar expressamente ancorada na Constituição e nas leis, abrangendo independência funcional, orgânica e financeira.
> - **C)** Incorreta. A Declaração de Lima reconhece a coexistência e legitimidade do controle prévio, concomitante e a posteriori.
> - **D)** Incorreta. A prestação de contas pública e a transparência perante a sociedade são preceitos centrais da Declaração.
> - **E)** Incorreta. O controle externo não depende de chancela ou homologação do Executivo.
>
> **Gabarito: B**"""

# Inserções no arquivo 02 de trás para frente
pos_q05 = t02.find("### Questão 05")
assert pos_q05 != -1
pos_fontes = t02.find("## 🌐 Fontes", pos_q05)
assert pos_fontes != -1
t02 = t02[:pos_fontes] + "\n\n" + q11_02.strip() + "\n\n---\n\n" + t02[pos_fontes:]

pos_q04 = t02.find("### Questão 04")
assert pos_q04 != -1
pos_end_q04 = t02.find("\n\n---\n\n", pos_q04)
assert pos_end_q04 != -1
t02 = t02[:pos_end_q04 + 7] + "\n\n" + q10_02.strip() + "\n\n---\n\n" + t02[pos_end_q04 + 7:]

ancora_3 = "### 3. Estrutura Normativa NBASP / INTOSAI e as Três Partes da Auditoria"
pos_3 = t02.find(ancora_3)
pos_4 = t02.find("### 4. Postura e Conduta Profissional", pos_3)
assert pos_3 != -1 and pos_4 != -1
t02 = t02[:pos_4] + "\n\n" + q09_02.strip() + "\n\n---\n\n" + t02[pos_4:]

pos_q03 = t02.find("### Questão 03")
assert pos_q03 != -1
pos_end_q03 = t02.find("\n\n---\n\n", pos_q03)
assert pos_end_q03 != -1
t02 = t02[:pos_end_q03 + 7] + "\n\n" + q08_02.strip() + "\n\n---\n\n" + t02[pos_end_q03 + 7:]

pos_q02 = t02.find("### Questão 02")
assert pos_q02 != -1
t02 = t02[:pos_q02] + "\n\n" + q07_02.strip() + "\n\n---\n\n" + t02[pos_q02:]

pos_q01 = t02.find("### Questão 01")
assert pos_q01 != -1
t02 = t02[:pos_q01] + "\n\n" + q06_02.strip() + "\n\n---\n\n" + t02[pos_q01:]

qs_02 = re.findall(r"### Questão (\d+)", t02)
print("Questões no arquivo 02 do Módulo 18:", qs_02)
assert len(qs_02) == 11
assert sorted(qs_02) == ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']

with open(f02_path, "w", encoding="utf-8") as f:
    f.write(t02)

print("Arquivo 02 do Módulo 18 gravado com sucesso! Total: 11 questões.")
