# -*- coding: utf-8 -*-
import os
import re

BASE_DIR = "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/17_nocoes_de_direito_constitucional"
f03_path = f"{BASE_DIR}/03_organizacao_do_estado_e_reparticao_de_competencias.md"
with open(f03_path, "r", encoding="utf-8") as f:
    t03 = f.read()

assert "### Questão 01" in t03
assert "### Questão 02" in t03
assert "### Questão 03" in t03
assert "### Questão 04" in t03
assert "### Questão 05" in t03

q06_03 = """### Questão 06 (FCC - Analista Judiciário - Área Administrativa)
A República Federativa do Brasil, formada pela união indissolúvel dos Estados e Municípios e do Distrito Federal, constitui-se em Estado Democrático de Direito (art. 1º, caput, da CF/88).

A respeito da forma de Estado federativa e da organização político-administrativa brasileira, assinale a afirmativa correta.

* **A)** Os Estados-membros da Federação brasileira possuem direito de secessão, sendo-lhes lícito desmembrarem-se unilateralmente da União mediante plebiscito local.
* **B)** A autonomia dos entes federados (União, Estados, Distrito Federal e Municípios) compreende as capacidades de auto-organização, autogoverno, autolegislação e autoadministração, nos estritos limites delineados pela Constituição Federal.
* **C)** Os Territórios Federais integram a Federação brasileira como entes autônomos dotados de representação própria no Senado Federal.
* **D)** A criação de um novo Município prescinde de consulta plebiscitária às populações dos Municípios envolvidos, dependendo apenas de parecer prévio do Tribunal de Contas do Estado.
* **E)** A soberania é atributo partilhado de forma idêntica entre a União e os Municípios brasileiros.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O princípio republicano federativo brasileiro assenta-se no dogma da **indissolubilidade do vínculo federativo**, sendo terminantemente vedado o direito de secessão (passível de intervenção federal, art. 34, I).
> - **B)** Correta. A federação brasileira é dotada de entes autônomos que possuem a chamada quádrupla capacidade: auto-organização (elaboração de Constituições Estaduais e Leis Orgânicas), autogoverno (eleição de seus próprios mandatários), autolegislação (edição de leis locais) e autoadministração (prestação de serviços e gestão tributária), tudo sob a supremacia da CF/88.
> - **C)** Incorreta. Os Territórios Federais não são entes federados autônomos; integram a União como meras descentralizações administrativas territoriais (art. 18, § 2º).
> - **D)** Incorreta. A criação de municípios exige: lei complementar federal de período, Estudos de Viabilidade Municipal, plebiscito obrigatório e lei ordinária estadual (art. 18, § 4º).
> - **E)** Incorreta. A **soberania** pertence exclusivamente à República Federativa do Brasil (o Estado brasileiro no plano internacional); os entes federados internos gozam apenas de **autonomia**.
>
> **Gabarito: B**"""

q07_03 = """### Questão 07 (FGV - Auditor de Controle Externo / TCE-GO)
O art. 24 da Constituição Federal estabelece que compete à União, aos Estados e ao Distrito Federal legislar concorrentemente sobre direito tributário, financeiro, penitenciário, econômico e urbanístico.

A respeito da dinâmica da competência legislativa concorrente, assinale a afirmativa correta.

* **A)** No âmbito da legislação concorrente, a competência da União limita-se a estabelecer normas gerais, cabendo aos Estados e ao DF a competência suplementar.
* **B)** A inexistência de lei federal sobre normas gerais impede os Estados de exercerem qualquer competência legislativa sobre a matéria até a manifestação do Congresso Nacional.
* **C)** A superveniência de lei federal sobre normas gerais revoga integralmente a lei estadual anterior que dispôs sobre a mesma matéria.
* **D)** A competência legislativa concorrente estende-se expressamente aos Municípios para fixação de normas gerais nacionais de direito econômico.
* **E)** Os Estados possuem competência privativa para editar normas gerais sobre direito financeiro e orçamentos públicos.

> **Comentário Detalhado:**
>
> - **A)** Correta. O art. 24, § 1º e § 2º, da CF/88 determina que, no âmbito da legislação concorrente, a competência da União limitar-se-á a estabelecer **normas gerais**, não excluindo a competência suplementar dos Estados para preencher as lacunas e particularidades regionais.
> - **B)** Incorreta. Inexistindo lei federal sobre normas gerais, os Estados exercerão a **competência legislativa plena**, para atender a suas peculiaridades (art. 24, § 3º).
> - **C)** Incorreta. Conforme o art. 24, § 4º, a superveniência de lei federal sobre normas gerais **suspende a eficácia** (e não revoga) da lei estadual, no que lhe for contrário.
> - **D)** Incorreta. O art. 24 não inclui os Municípios na competência concorrente; a competência municipal é suplementar no que couber (art. 30, II).
> - **E)** Incorreta. Normas gerais financeiras competem à União (art. 24, I c/c art. 163).
>
> **Gabarito: A**"""

q08_03 = """### Questão 08 (FCC - Procurador do Estado / Adaptada)
A Câmara Municipal de determinado Município aprovou lei local disciplinando o horário de funcionamento de estabelecimentos bancários situados em seu território, bem como exigindo a instalação de portas de segurança eletrônicas e banheiros para os clientes nas agências.

À luz da jurisprudência consolidada do Supremo Tribunal Federal e do Superior Tribunal de Justiça, a referida lei municipal é:

* **A)** Integralmente inconstitucional, uma vez que o sistema financeiro nacional é de competência legislativa privativa da União (art. 22, VI e VII, CF/88).
* **B)** Constitucional quanto aos itens de conforto, segurança e tempo de atendimento ao consumidor (como banheiros e portas eletrônicas), mas inconstitucional quanto à fixação do horário de funcionamento bancário, cuja competência é privativa da União (Súmula Vinculante nº 38 do STF).
* **C)** Válida em sua integralidade, inclusive para fixar o horário de compensação nacional de cheques.
* **D)** Nula de pleno direito por violar a competência concorrente dos Estados-membros em matéria de direito comercial.
* **E)** Inconstitucional exclusivamente quanto à exigência de portas de segurança, por configurar matéria de segurança nacional do Exército Brasileiro.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O STF distingue o funcionamento do sistema financeiro (privativo da União) das regras de atendimento, conforto e segurança local do consumidor (competência municipal de interesse local, art. 30, I).
> - **B)** Correta. Jurisprudência pacificada nas súmulas dos Tribunais Superiores: (1) **Súmula Vinculante nº 38 do STF**: *"É inconstitucional a lei municipal que fixa o horário de funcionamento de estabelecimento bancário"* (competência da União, Súmula 19/STJ); e (2) **Súmula 469 do STJ / Tema 145 do STF**: O Município tem competência para legislar sobre segurança, instalação de sanitários, bebedouros e tempo razoável de espera em filas nas agências bancárias, por se tratar de matéria de interesse local e proteção ao consumidor.
> - **C)** Incorreta. Fixar horário de abertura e fechamento das agências bancárias é matéria privativa da União.
> - **D)** Incorreta. Matéria consumerista local insere-se no interesse local municipal.
> - **E)** Incorreta. Segurança física das agências e porta giratória são temas de competência municipal válidos.
>
> **Gabarito: B**"""

q09_03 = """### Questão 09 (FGV - Analista de Controle Externo / TCE-GO)
A intervenção federal nos Estados e no Distrito Federal (art. 34 da CF/88) configura medida excepcional de supressão temporária da autonomia política do ente federado.

A respeito dos pressupostos materiais e procedimentais da intervenção federal, assinale a afirmativa correta.

* **A)** O Presidente da República pode decretar a intervenção federal em qualquer Estado sem controle político do Congresso Nacional se o Governador for filiado a partido de oposição.
* **B)** A intervenção federal para assegurar a observância dos princípios constitucionais sensíveis (como a forma republicana, o sistema representativo, os direitos humanos e a prestação de contas da administração pública) depende de provimento pelo Supremo Tribunal Federal de representação interventiva ajuizada pelo Procurador-Geral da República (ADI interventiva).
* **C)** O Tribunal de Contas da União pode decretar diretamente a intervenção em Estado que atrasar o repasse de verbas do SUS aos municípios.
* **D)** O decreto de intervenção federal dispensa a indicação da amplitude, do prazo e das condições de execução, cabendo ao interventor poderes soberanos ilimitados.
* **E)** Cessados os motivos da intervenção, as autoridades estaduais afastadas de seus cargos não poderão reassumi-los, devendo ser convocadas novas eleições gerais imediatas.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A intervenção é estritamente vinculada às hipóteses taxativas do art. 34 da CF/88 e submete-se ao controle político obrigatório do Congresso Nacional em até 24 horas (art. 36, § 1º).
> - **B)** Correta. Nos termos do art. 36, III, da CF/88, no caso de desrespeito aos chamados **princípios constitucionais sensíveis** (art. 34, VII: forma republicana, direitos da pessoa humana, prestação de contas, aplicação dos mínimos em saúde/educação), a intervenção federal depende de **provimento pelo STF de representação interventiva ajuizada privativamente pelo Procurador-Geral da República (PGR)**.
> - **C)** Incorreta. Decretar intervenção é competência privativa e indelegável do Presidente da República (art. 84, X).
> - **D)** Incorreta. O art. 36, § 1º, exige que o decreto de intervenção especifique a amplitude, o prazo, as condições de execução e a nomeação do interventor.
> - **E)** Incorreta. O art. 36, § 4º, estabelece que, cessados os motivos da intervenção, as autoridades afastadas reassumirão seus cargos, salvo impedimento legal.
>
> **Gabarito: B**"""

q10_03 = """### Questão 10 (FCC - Técnico de Controle Externo / Administrativa)
No âmbito do regime constitucional da Administração Pública e de seus servidores (arts. 37 a 41 da CF/88), a remuneração e o subsídio dos ocupantes de cargos, funções e empregos públicos submetem-se ao teto remuneratório constitucional.

A esse respeito, assinale a afirmativa correta.

* **A)** O teto remuneratório no âmbito do Poder Executivo dos Estados e do Distrito Federal tem como limite o subsídio mensal dos Desembargadores do Tribunal de Justiça.
* **B)** O teto remuneratório constitucional no âmbito dos Estados e do DF corresponde: no Poder Executivo, ao subsídio mensal do Governador; no Poder Legislativo, ao subsídio dos Deputados Estaduais; e no Poder Judiciário, ao subsídio dos Desembargadores do Tribunal de Justiça, limitado a 90,25% do subsídio dos Ministros do STF.
* **C)** As verbas de caráter indenizatório expressamente previstas em lei submetem-se integralmente ao teto remuneratório constitucional.
* **D)** A acumulação lícita de dois cargos públicos de médico autoriza a Administração a somar os vencimentos para aplicação do teto de forma global unificada.
* **E)** Servidores públicos ocupantes exclusivamente de cargos em comissão estão imunes ao teto remuneratório constitucional.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. No Poder Executivo estadual o teto é o subsídio do **Governador do Estado** (art. 37, XI da CF/88).
> - **B)** Correta. O art. 37, XI, da CF/88 estabelece o sistema de tetos remuneratórios no plano estadual: (1) no **Poder Executivo**, o subsídio do Governador; (2) no **Poder Legislativo**, o subsídio dos Deputados Estaduais; (3) no **Poder Judiciário**, o subsídio dos Desembargadores do Tribunal de Justiça (limitado a 90,25% do subsídio dos Ministros do STF), limite este aplicável aos membros do Ministério Público, aos Procuradores e aos Defensores Públicos.
> - **C)** Incorreta. O art. 37, § 11, da CF/88 exclui expressamente do cômputo do teto as **parcelas de caráter indenizatório** previstas em lei (ex.: diárias, ajuda de custo).
> - **D)** Incorreta. Tese fixada pelo STF no Tema 377 e Tema 384: nos casos de acumulação lícita de cargos (como dois cargos de saúde), o teto remuneratório constitucional deve incidir **isoladamente sobre a remuneração de cada um dos cargos**, e não sobre o somatório de ambos.
> - **E)** Incorreta. O teto atinge a todos os agentes públicos, efetivos ou comissionados.
>
> **Gabarito: B**"""

q11_03 = """### Questão 11 (FGV - Analista de Controle Externo / Auditoria)
A estabilidade no serviço público é direito constitucional assegurado aos servidores nomeados para cargo de provimento efetivo em virtude de concurso público, nos termos do art. 41 da Constituição Federal de 1988.

Sobre as condições e regras da estabilidade funcional, assinale a afirmativa correta.

* **A)** São estáveis após dois anos de efetivo exercício os servidores nomeados para cargo efetivo, independentemente de avaliação especial de desempenho.
* **B)** Como condição obrigatória para a aquisição da estabilidade, é indispensável a aprovação do servidor em avaliação especial de desempenho por comissão instituída para essa finalidade, após três anos de efetivo exercício.
* **C)** O servidor público estável não pode perder o cargo em hipótese alguma, gozando de garantia absoluta de permanência no serviço público.
* **D)** Invalidada por sentença judicial a demissão do servidor estável, ele será reintegrado, e o eventual ocupante da vaga, se estável, será compulsoriamente demitido sem direito a indenização.
* **E)** Em caso de extinção do cargo ou declaração de sua desnecessidade, o servidor público estável será imediatamente exonerado sem remuneração.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A EC nº 19/1998 ampliou o prazo do estágio probatório para **3 (três) anos** de efetivo exercício e tornou obrigatória a avaliação especial de desempenho.
> - **B)** Correta. O art. 41, caput e § 4º, da Constituição Federal prescreve que são estáveis após 3 (três) anos de efetivo exercício os servidores concursados, sendo condição obrigatória para aquisição da estabilidade a prévia aprovação em **avaliação especial de desempenho** por comissão constituída para essa finalidade.
> - **C)** Incorreta. O servidor estável pode perder o cargo em 4 hipóteses constitucionais (art. 41, § 1º c/c art. 169, § 4º): (1) sentença judicial transitada em julgado; (2) processo administrativo com ampla defesa; (3) avaliação periódica de desempenho (lei complementar); (4) excesso de despesas com pessoal.
> - **D)** Incorreta. O eventual ocupante da vaga reconduzido ao cargo de origem, aproveitado em outro cargo ou posto em disponibilidade com remuneração proporcional, **jamais demitido sem indenização** (art. 41, § 2º).
> - **E)** Incorreta. Extinto o cargo, o servidor estável ficará em **disponibilidade**, com remuneração proporcional ao tempo de contribuição, até seu adequado aproveitamento em outro cargo (art. 41, § 3º).
>
> **Gabarito: B**"""

# Inserções no arquivo 03 de trás para frente
pos_q05 = t03.find("### Questão 05")
assert pos_q05 != -1
pos_fontes = t03.find("## 🌐 Fontes", pos_q05)
assert pos_fontes != -1
t03 = t03[:pos_fontes] + "\n\n" + q11_03.strip() + "\n\n---\n\n" + t03[pos_fontes:]

pos_q03 = t03.find("### Questão 03")
assert pos_q03 != -1
t03 = t03[:pos_q03] + "\n\n" + q10_03.strip() + "\n\n---\n\n" + t03[pos_q03:]

ancora_3 = "### 3. Mecanismos Excepcionais de Equilíbrio: Intervenção Federal e Estadual"
pos_3 = t03.find(ancora_3)
pos_4 = t03.find("### 4. Regime Constitucional", pos_3)
assert pos_3 != -1 and pos_4 != -1
t03 = t03[:pos_4] + "\n\n" + q09_03.strip() + "\n\n---\n\n" + t03[pos_4:]

pos_q02 = t03.find("### Questão 02")
assert pos_q02 != -1
pos_end_q02 = t03.find("\n\n---\n\n", pos_q02)
assert pos_end_q02 != -1
t03 = t03[:pos_end_q02 + 7] + "\n\n" + q08_03.strip() + "\n\n---\n\n" + t03[pos_end_q02 + 7:]

pos_q01 = t03.find("### Questão 01")
assert pos_q01 != -1
t03 = t03[:pos_q01] + "\n\n" + q07_03.strip() + "\n\n---\n\n" + t03[pos_q01:]

ancora_1 = "### 1. Forma Federativa e Organização Político-Administrativa"
pos_1 = t03.find(ancora_1)
pos_2 = t03.find("### 2. O Modelo Constitucional", pos_1)
assert pos_1 != -1 and pos_2 != -1
t03 = t03[:pos_2] + "\n\n" + q06_03.strip() + "\n\n---\n\n" + t03[pos_2:]

qs_03 = re.findall(r"### Questão (\d+)", t03)
print("Questões no arquivo 03 do Módulo 17:", qs_03)
assert len(qs_03) == 11
assert sorted(qs_03) == ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']

with open(f03_path, "w", encoding="utf-8") as f:
    f.write(t03)

print("Arquivo 03 do Módulo 17 gravado com sucesso! Total: 11 questões.")
