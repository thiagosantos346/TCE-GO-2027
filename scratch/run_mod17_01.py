# -*- coding: utf-8 -*-
import os
import re

BASE_DIR = "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/17_nocoes_de_direito_constitucional"

# ==============================================================================
# FILE 01: 01_aplicabilidade_das_normas_e_principios_fundamentais.md
# ==============================================================================
f01_path = f"{BASE_DIR}/01_aplicabilidade_das_normas_e_principios_fundamentais.md"
with open(f01_path, "r", encoding="utf-8") as f:
    t01 = f.read()

assert "### Questão 01" in t01
assert "### Questão 02" in t01
assert "### Questão 03" in t01
assert "### Questão 04" in t01
assert "### Questão 05" in t01

q06_01 = """### Questão 06 (FCC - Analista Judiciário - Área Judiciária)
De acordo com a clássica classificação das normas constitucionais quanto à sua eficácia e aplicabilidade proposta por José Afonso da Silva, assinale a afirmativa correta.

* **A)** As normas de eficácia contida dependem obrigatoriamente de lei infraconstitucional regulamentadora para produzirem qualquer efeito prático desde a promulgação da Constituição.
* **B)** As normas de eficácia plena produzem ou têm possibilidade de produzir todos os seus efeitos essenciais imediatamente com a entrada em vigor da Constituição, independentemente de qualquer normação infraconstitucional integrativa.
* **C)** As normas de eficácia limitada são destituídas de qualquer juridicidade ou eficácia, não servindo sequer como parâmetro para o controle de constitucionalidade de leis futuras.
* **D)** A norma constitucional que assegura que 'é livre o exercício de qualquer trabalho, ofício ou profissão, atendidas as qualificações profissionais que a lei estabelecer' (art. 5º, XIII) é de eficácia limitada.
* **E)** As normas programáticas não vinculam o legislador nem os órgãos executivos, consistindo em meras exortações morais desprovidas de força normativa.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. As normas de **eficácia contida** têm aplicabilidade direta, imediata e integral desde a promulgação, mas podem ter seu alcance restringido ou contido por lei posterior.
> - **B)** Correta. As normas de **eficácia plena** têm aplicabilidade direta, imediata e integral: desde o momento em que a Constituição é promulgada, estão aptas a produzir a plenitude de seus efeitos jurídicos sem necessidade de intermediação legislativa infraconstitucional.
> - **C)** Incorreta. Toda norma constitucional possui eficácia jurídica mínima: as normas de eficácia limitada revogam a legislação anterior em sentido contrário (eficácia negativa/derrogatória) e vinculam o legislador futuro, servindo plenamente como paradigma no controle de constitucionalidade.
> - **D)** Incorreta. O art. 5º, XIII, é o exemplo clássico de norma de **eficácia contida**: a liberdade profissional é imediata; a lei superveniente pode apenas impor qualificações restritivas quando a atividade exigir.
> - **E)** Incorreta. As normas programáticas possuem força normativa vinculante (doutrina de Konrad Hesse); direcionam a atuação do Estado e fundamentam políticas públicas e controle de omissões inconstitucionais.
>
> **Gabarito: B**"""

q07_01 = """### Questão 07 (FGV - Auditor Fiscal da Receita Estadual)
Determinada norma da Constituição Federal estabelece que 'a lei disporá sobre a criação e extinção de ministérios e órgãos da administração pública'.

Quanto à aplicabilidade e eficácia das normas constitucionais, esse preceito classifica-se como norma de eficácia:

* **A)** Plena, pois independe de qualquer atuação do legislador infraconstitucional para que seus preceitos gerem efeitos no mundo fenomênico.
* **B)** Contida, pois o Presidente da República pode criar ministérios discricionariamente por meio de portaria interna enquanto não for editada a lei.
* **C)** Limitada de princípio institutivo, porquanto depende de lei formal para organizar e estruturar entidades e órgãos do Poder Executivo.
* **D)** Limitada de princípio programático, por versar exclusivamente sobre programas sociais dirigidos aos cidadãos.
* **E)** Exaurida, em virtude de ter esgotado sua eficácia jurídica no momento da promulgação da Carta de 1988.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A norma expressamente delega à lei futura a incumbência de dispor sobre a criação e extinção de órgãos e ministérios.
> - **B)** Incorreta. Não se trata de norma contida; o art. 84, VI, 'a', veda inclusive decreto autônomo para criação ou extinção de órgãos públicos (exige lei formal, art. 48, XI).
> - **C)** Correta. As normas de eficácia limitada subdividem-se em: (1) **normas definidoras de princípios institutivos ou organizativos**, que dependem de lei para estruturar órgãos, entidades ou procedimentos do Estado; e (2) normas definidoras de princípios programáticos. O preceito em análise é típico princípio institutivo.
> - **D)** Incorreta. Normas programáticas veiculam fins sociais e econômicos do Estado (ex.: saúde, erradicação da pobreza), e não a estruturação orgânica do aparelho administrativo.
> - **E)** Incorreta. Normas de eficácia exaurida são as do ADCT que já produziram efeitos transitórios pretéritos definitivos.
>
> **Gabarito: C**"""

q08_01 = """### Questão 08 (FCC - Técnico de Controle Externo / TCE-GO)
O Título I da Constituição Federal de 1988 consagra os Princípios Fundamentais do Estado brasileiro. Sobre os fundamentos da República Federativa do Brasil expressos no art. 1º da CF/88, assinale a afirmativa correta.

* **A)** A prevalência dos direitos humanos e a concessão de asilo político constituem fundamentos da República Federativa do Brasil.
* **B)** A soberania, a cidadania, a dignidade da pessoa humana, os valores sociais do trabalho e da livre iniciativa e o pluralismo político constituem os fundamentos expressos da República Federativa do Brasil (mnemônico SO-CI-DI-VA-PLU).
* **C)** A erradicação da pobreza e a redução das desigualdades sociais e regionais constituem fundamentos originários da República.
* **D)** A autodeterminação dos povos e a não intervenção são fundamentos republicanos internos.
* **E)** O pluralismo político confunde-se exclusivamente com o pluripartidarismo partidário, vedando manifestações filosóficas ou religiosas diversas.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A prevalência dos direitos humanos e o asilo político são princípios que regem o Brasil nas suas **relações internacionais** (art. 4º, II e X, da CF/88).
> - **B)** Correta. O art. 1º da CF/88 elenca como **fundamentos** da República Federativa do Brasil: I - a **so**berania; II - a **ci**dadania; III - a **di**gnidade da pessoa humana; IV - os **va**lores sociais do trabalho e da livre iniciativa; V - o **plu**ralismo político (mnemônico clássico da FCC: SO-CI-DI-VA-PLU).
> - **C)** Incorreta. Erradicar a pobreza e reduzir as desigualdades são **objetivos fundamentais** (art. 3º, III).
> - **D)** Incorreta. Autodeterminação e não intervenção são princípios das **relações internacionais** (art. 4º, I e IV).
> - **E)** Incorreta. O pluralismo político é gênero amplo que abrange a liberdade de ideias, de crença, correntes de pensamento e visões de mundo; o pluripartidarismo é mera espécie eleitoral.
>
> **Gabarito: B**"""

q09_01 = """### Questão 09 (FGV - Analista de Controle Externo / TCE-GO)
A Constituição da República Federativa do Brasil de 1988 estabelece em seu art. 3º os objetivos fundamentais da República.

Dentre as alternativas a seguir, assinale aquela que apresenta com exatidão um objetivo fundamental constitucional:

* **A)** Defesa da paz e solução pacífica dos conflitos.
* **B)** Construir uma sociedade livre, justa e solidária; garantir o desenvolvimento nacional; erradicar a pobreza e a marginalização e reduzir as desigualdades sociais e regionais; e promover o bem de todos, sem preconceitos de origem, raça, sexo, cor, idade e quaisquer outras formas de discriminação.
* **C)** Independência nacional e cooperação entre os povos para o progresso da humanidade.
* **D)** Garantia do direito de propriedade privada sem qualquer condicionamento social.
* **E)** Igualdade entre os Estados e repúdio categórico ao asilo político.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Princípios de relações internacionais (art. 4º, VI e VII).
> - **B)** Correta. Os **objetivos fundamentais** (art. 3º da CF/88) exprimem metas de ação com verbos no infinitivo (mnemônico: CON-GA-ER-PRO): I - **construir** uma sociedade livre, justa e solidária; II - **garantir** o desenvolvimento nacional; III - **erradicar** a pobreza e a marginalização e **reduzir** as desigualdades sociais e regionais; IV - **promover** o bem de todos, sem preconceitos de origem, raça, sexo, cor, idade e quaisquer outras formas de discriminação.
> - **C)** Incorreta. Princípios de relações internacionais (art. 4º, I e IX).
> - **D)** Incorreta. A propriedade privada submete-se indelevelmente à sua função social (art. 5º, XXIII, e art. 170, III).
> - **E)** Incorreta. O Brasil concede asilo político como princípio internacional expresso (art. 4º, X).
>
> **Gabarito: B**"""

q10_01 = """### Questão 10 (FCC - Procurador do Estado / Adaptada)
Nas suas relações internacionais, a República Federativa do Brasil rege-se pelos princípios positivados no art. 4º da Constituição Federal de 1988.

Sobre o regramento e a interpretação desses princípios, assinale a afirmativa correta.

* **A)** A concessão de asilo político constitui obrigação internacional cogente que retira do Presidente da República o juízo de conveniência soberana sobre o acolhimento do estrangeiro.
* **B)** A República Federativa do Brasil buscará a integração econômica, política, social e cultural dos povos da América Latina, visando à formação de uma comunidade latino-americana de nações.
* **C)** O princípio da não intervenção impede o Brasil de participar de missões de paz organizadas pela Organização das Nações Unidas (ONU).
* **D)** O repúdio ao terrorismo e ao racismo é princípio constitucional de aplicabilidade restrita ao território nacional.
* **E)** O Brasil subordina sua soberania interna às decisões unilaterais tomadas por tribunais estrangeiros não reconhecidos pelo Estado brasileiro.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A concessão de asilo político (art. 4º, X) é ato de soberania estatal do Presidente da República, que dispõe de margem de discricionariedade política internacional.
> - **B)** Correta. O parágrafo único do art. 4º da CF/88 consagra categoricamente que *"A República Federativa do Brasil buscará a integração econômica, política, social e cultural dos povos da América Latina, visando à formação de uma comunidade latino-americana de nações"*.
> - **C)** Incorreta. O princípio da não intervenção convive com a cooperação internacional e a defesa da paz sob a égide do direito internacional humanitário.
> - **D)** Incorreta. O repúdio ao terrorismo e ao racismo é diretriz de política externa e universal (art. 4º, VIII).
> - **E)** Incorreta. O art. 4º, I, coloca a independência nacional e a soberania como vetores inegociáveis do Estado brasileiro.
>
> **Gabarito: B**"""

q11_01 = """### Questão 11 (FGV - Analista de Controle Externo / Auditoria)
O art. 2º da Constituição Federal de 1988 consagra que 'são Poderes da União, independentes e harmônicos entre si, o Legislativo, o Executivo e o Judiciário'.

A respeito do princípio da Separação de Poderes e do sistema de freios e contrapesos (checks and balances), assinale a afirmativa correta.

* **A)** A separação de poderes é absoluta, sendo terminantemente vedado a qualquer Poder exercer atribuições de natureza atípica.
* **B)** O controle de constitucionalidade de leis exercido pelo Poder Judiciário, a aprovação de autoridades pelo Senado Federal e o veto do Presidente da República a projetos de lei constituem manifestações legítimas do sistema constitucional de freios e contrapesos.
* **C)** O Tribunal de Contas constitui órgão subordinado ao Poder Judiciário para fins de fiscalização contábil do Estado.
* **D)** A edição de medidas provisórias pelo Chefe do Poder Executivo decorre do exercício de sua função executiva típica originária.
* **E)** O princípio da separação dos poderes impede que o Poder Legislativo fiscalize a gestão financeira e orçamentária dos órgãos do Poder Executivo.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A separação de poderes não é estanque nem absoluta. Cada Poder exerce uma função típica preponderante e, de forma atípica, funções inerentes aos outros Poderes (ex.: o Judiciário administra seus serviços e legisla em regimentos internos; o Legislativo julga o Presidente por crime de responsabilidade).
> - **B)** Correta. O sistema de freios e contrapesos assegura que nenhum Poder se torne hegemônico ou tirânico, permitindo que um Poder controle e limite o outro nos estritos termos traçados pela Constituição (veto presidencial, controle judicial de constitucionalidade, sabatina de autoridades pelo Senado).
> - **C)** Incorreta. Os Tribunais de Contas são órgãos autônomos e independentes com assento constitucional que auxiliam o Poder Legislativo no controle externo.
> - **D)** Incorreta. Editar medida provisória com força de lei é exercício atípico de função legislativa pelo Chefe do Poder Executivo.
> - **E)** Incorreta. O controle externo financeiro pelo Legislativo é a essência do postulado republicano (arts. 70 e 71 da CF/88).
>
> **Gabarito: B**"""

# Inserções no arquivo 01 de trás para frente
pos_q05 = t01.find("### Questão 05")
assert pos_q05 != -1
pos_fontes = t01.find("## 3. Fontes", pos_q05)
if pos_fontes == -1:
    pos_fontes = t01.find("## ", pos_q05 + 10)
if pos_fontes == -1:
    pos_fontes = len(t01)

t01 = t01[:pos_fontes] + "\n\n" + q11_01.strip() + "\n\n---\n\n" + t01[pos_fontes:]
t01 = t01[:pos_q05] + "\n\n" + q10_01.strip() + "\n\n---\n\n" + t01[pos_q05:]

pos_q04 = t01.find("### Questão 04")
assert pos_q04 != -1
t01 = t01[:pos_q04] + "\n\n" + q09_01.strip() + "\n\n---\n\n" + t01[pos_q04:]

pos_q03 = t01.find("### Questão 03")
assert pos_q03 != -1
t01 = t01[:pos_q03] + "\n\n" + q08_01.strip() + "\n\n---\n\n" + t01[pos_q03:]

pos_q02 = t01.find("### Questão 02")
assert pos_q02 != -1
pos_end_q02 = t01.find("\n\n---\n\n", pos_q02)
assert pos_end_q02 != -1
t01 = t01[:pos_end_q02 + 7] + "\n\n" + q07_01.strip() + "\n\n---\n\n" + t01[pos_end_q02 + 7:]

pos_q01 = t01.find("### Questão 01")
assert pos_q01 != -1
t01 = t01[:pos_q01] + "\n\n" + q06_01.strip() + "\n\n---\n\n" + t01[pos_q01:]

qs_01 = re.findall(r"### Questão (\d+)", t01)
print("Questões no arquivo 01 do Módulo 17:", qs_01)
assert len(qs_01) == 11
assert sorted(qs_01) == ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']

with open(f01_path, "w", encoding="utf-8") as f:
    f.write(t01)

print("Arquivo 01 do Módulo 17 gravado com sucesso! Total: 11 questões.")
