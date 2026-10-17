# -*- coding: utf-8 -*-
import os
import re

BASE_DIR = "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/17_nocoes_de_direito_constitucional"
f05_path = f"{BASE_DIR}/05_poder_executivo_poder_judiciario_e_funcoes_essenciais.md"
with open(f05_path, "r", encoding="utf-8") as f:
    t05 = f.read()

assert "### Questão 01" in t05
assert "### Questão 02" in t05
assert "### Questão 03" in t05
assert "### Questão 04" in t05
assert "### Questão 05" in t05

q06_05 = """### Questão 06 (FCC - Analista de Controle Externo / TCE-GO)
O art. 84, VI, da Constituição Federal, com a redação dada pela Emenda Constitucional nº 32/2001, introduziu no direito constitucional brasileiro a figura do decreto autônomo presidencial.

Conforme a disciplina constitucional vigente, o Chefe do Poder Executivo pode dispor mediante decreto sobre:

* **A)** Criação e extinção de ministérios e órgãos públicos da administração direta e indireta.
* **B)** Organização e funcionamento da administração federal, quando não implicar aumento de despesa nem criação ou extinção de órgãos públicos; e extinção de funções ou cargos públicos, quando vagos.
* **C)** Definição de novos crimes e cominação de penas disciplinares privativas de liberdade.
* **D)** Concessão de anistia e indulto para infrações funcionais apuradas em processos de contas pelo Tribunal de Contas.
* **E)** Instituição e majoração discricionária de tributos sem autorização legislativa formal.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A criação e extinção de órgãos públicos e ministérios exige **obrigatoriamente lei formal** de iniciativa privativa do Presidente (art. 48, XI e art. 84, VI, 'a', parte final).
> - **B)** Correta. O art. 84, VI, da CF/88 consagra categoricamente as duas únicas hipóteses constitucionais admitidas de **decreto autônomo**: 'a' - organização e funcionamento da administração federal, quando não implicar aumento de despesa nem criação ou extinção de órgãos públicos; 'b' - extinção de funções ou cargos públicos, **quando vagos**.
> - **C)** Incorreta. Matéria penal e criação de penas submetem-se ao princípio da reserva legal absoluta (art. 5º, XXXIX).
> - **D)** Incorreta. O indulto presidencial (art. 84, XII) destina-se a condenações penais comuns, e não a sanções de ressarcimento impostas por Cortes de Contas.
> - **E)** Incorreta. Instituição de tributos exige estrita legalidade tributária (art. 150, I).
>
> **Gabarito: B**"""

q07_05 = """### Questão 07 (FGV - Auditor de Controle Externo / TCE-SC)
A responsabilidade do Presidente da República é disciplinada nos arts. 85 e 86 da Constituição Federal de 1988, diferenciando os crimes comuns dos crimes de responsabilidade.

Sobre o rito constitucional de responsabilização do Chefe do Poder Executivo, assinale a afirmativa correta.

* **A)** O Presidente da República somente pode ser submetido a julgamento por crime comum ou de responsabilidade após a admissão da acusação por dois terços dos membros da Câmara dos Deputados.
* **B)** Admitida a acusação por crime comum, o Presidente da República será processado e julgado perante o Senado Federal.
* **C)** No julgamento por crime de responsabilidade, a condenação pelo Senado Federal exige voto da maioria simples dos senadores presentes à sessão.
* **D)** O Presidente da República, na vigência de seu mandato, pode ser responsabilizado por atos estranhos ao exercício de suas funções na esfera criminal.
* **E)** A admissão da acusação pela Câmara dos Deputados suspende o Presidente da República de suas funções imediatamente, antes mesmo da instauração formal do processo pelo órgão julgador competente.

> **Comentário Detalhado:**
>
> - **A)** Correta. O art. 86, caput, da CF/88 estabelece o juízo político prévio de admissibilidade: *"Se admitida a acusação contra o Presidente da República, por **dois terços da Câmara dos Deputados**, será ele submetido a julgamento perante o Supremo Tribunal Federal, nas infrações penais comuns, ou perante o Senado Federal, nos crimes de responsabilidade"*.
> - **B)** Incorreta. Por crimes penais comuns o julgamento realiza-se perante o **Supremo Tribunal Federal** (art. 86 e art. 102, I, 'b').
> - **C)** Incorreta. A condenação no Senado por crime de responsabilidade exige quórum qualificado de **dois terços dos votos** (art. 52, parágrafo único), operando a perda do cargo e a inabilitação por oito anos.
> - **D)** Incorreta. O art. 86, § 4º, consagra a imunidade penal temporária relativa: *"O Presidente da República, na vigência de seu mandato, não pode ser responsabilizado por atos estranhos ao exercício de suas funções"*.
> - **E)** Incorreta. A suspensão de funções opera-se apenas após a instauração formal do processo pelo STF (crime comum) ou após a instauração pelo Senado Federal (crime de responsabilidade), e não pela mera votação na Câmara (art. 86, § 1º).
>
> **Gabarito: A**"""

q08_05 = """### Questão 08 (FCC - Analista Judiciário - Área Judiciária)
A Constituição Federal de 1988 assegura garantias institucionais e funcionais indispensáveis à independência dos membros do Poder Judiciário (art. 95).

A respeito das garantias dos magistrados, assinale a afirmativa correta.

* **A)** A vitaliciedade é adquirida pelo juiz concursado imediatamente após a cerimônia de posse no cargo.
* **B)** A vitaliciedade, no primeiro grau de jurisdição, só será adquirida após dois anos de efetivo exercício, dependendo a perda do cargo, nesse período, de deliberação do tribunal a que o juiz estiver vinculado, e, após o biênio, exclusivamente de sentença judicial transitada em julgado.
* **C)** A inamovibilidade dos magistrados é absoluta, sendo vedada a remoção compulsória por motivo de interesse público fundamentado.
* **D)** Os magistrados podem exercer livremente a atividade político-partidária e a advocacia privada durante as férias e licenças funcionais.
* **E)** A irredutibilidade de subsídio autoriza o magistrado a receber remuneração superior ao teto constitucional dos Ministros do STF.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. No primeiro grau, a vitaliciedade exige o estágio probatório bienal (2 anos).
> - **B)** Correta. O art. 95, I, da CF/88 estatui categoricamente: a vitaliciedade *"no primeiro grau, só será adquirida após **dois anos de exercício**, dependendo a perda do cargo, nesse período, de deliberação do tribunal a que o juiz estiver vinculado, e, após o biênio, **somente por sentença judicial transitada em julgado**"*. (Observação: para os que ingressam pelo quinto constitucional nos tribunais, a vitaliciedade é imediata com a posse).
> - **C)** Incorreta. A inamovibilidade admite exceção por motivo de interesse público, fundada em decisão por voto da maioria absoluta do respectivo tribunal ou do CNJ, com ampla defesa (art. 95, II c/c art. 93, VIII).
> - **D)** Incorreta. A CF veda aos juízes expressamente a dedicação a atividade político-partidária (art. 95, parágrafo único, III) e a advocacia.
> - **E)** Incorreta. A irredutibilidade submete-se estritamente ao teto constitucional do art. 37, XI.
>
> **Gabarito: B**"""

q09_05 = """### Questão 09 (FGV - Analista Jurídico de Controle Externo / TCE-GO)
O art. 103-A da Constituição Federal, inserido pela Emenda Constitucional nº 45/2004, autoriza o Supremo Tribunal Federal a editar súmulas vinculantes.

Sobre os requisitos de aprovação, objeto e efeitos da Súmula Vinculante, assinale a afirmativa correta.

* **A)** A Súmula Vinculante pode ser aprovada por maioria simples dos Ministros do Supremo Tribunal Federal, vinculando o Congresso Nacional em sua função típica legislativa.
* **B)** O STF poderá, de ofício ou por provocação, mediante decisão de dois terços dos seus membros, após reiteradas decisões sobre matéria constitucional, aprovar súmula que terá efeito vinculante em relação aos demais órgãos do Poder Judiciário e à administração pública direta e indireta, nas esferas federal, estadual e municipal.
* **C)** A Súmula Vinculante vincula o próprio Supremo Tribunal Federal, impedindo que a Corte altere ou cancele seus enunciados em julgamentos futuros.
* **D)** Do ato administrativo ou decisão judicial que contrariar a súmula vinculante aplicável caberá recurso ordinário ao Tribunal de Justiça local.
* **E)** É dispensada a existência de reiteradas decisões anteriores para a edição de enunciado de súmula vinculante.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Exige-se quórum qualificado de **dois terços (8 Ministros)**. Ademais, a súmula vinculante **não vincula o Poder Legislativo** em sua atividade típica de legislar (para evitar o indesejado 'fóssil normativo' ou 'engessamento do legislador').
> - **B)** Correta. O art. 103-A da CF/88 estabelece que o STF poderá, de ofício ou por provocação, mediante decisão de **2/3 dos seus membros**, após reiteradas decisões sobre matéria constitucional, editar súmula com efeito vinculante em relação aos demais órgãos do Poder Judiciário e a toda a **administração pública direta e indireta**, nas esferas federal, estadual e municipal.
> - **C)** Incorreta. O STF pode, pelo mesmo quórum qualificado, revisar ou cancelar enunciados de súmula vinculante (art. 103-A, caput).
> - **D)** Incorreta. O instrumento constitucional cabível contra ato administrativo ou decisão que afronte súmula vinculante é a **Reclamação Constitucional** perante o próprio STF (art. 103-A, § 3º).
> - **E)** Incorreta. É pressuposto constitucional obrigatório a existência de controvérsia atual e reiteradas decisões colegiadas sobre a matéria.
>
> **Gabarito: B**"""

q10_05 = """### Questão 10 (FCC - Procurador do Estado / Adaptada)
O Ministério Público é instituição permanente, essencial à função jurisdicional do Estado, incumbindo-lhe a defesa da ordem jurídica, do regime democrático e dos interesses sociais e individuais indisponíveis (art. 127, caput, da CF/88).

São princípios institucionais expressos do Ministério Público positivados no art. 127, § 1º, da Constituição Federal:

* **A)** A unidade, a indivisibilidade e a independência funcional.
* **B)** A hierarquia funcional rígida, a publicidade restrita e a descentralização decisória.
* **C)** A subordinação administrativa ao Ministério da Justiça e a solidariedade orçamentária.
* **D)** A presunção de legalidade, a tipicidade e a subsidiariedade penal.
* **E)** A intranscendência, a colegialidade estrita e a rotatividade partidária.

> **Comentário Detalhado:**
>
> - **A)** Correta. O art. 127, § 1º, da Constituição Federal consagra categoricamente a tríade de princípios institucionais do Ministério Público: a **unidade** (os membros integram um só corpo sob a mesma direção institucional), a **indivisibilidade** (um membro pode substituir outro no mesmo processo sem quebra de continuidade funcional) e a **independência funcional** (cada membro atua com autonomia de convicção jurídica respaldada na lei e na Constituição, não se submetendo a ordens de mérito de chefias).
> - **B)** Incorreta. No âmbito funcional não há hierarquia sobre a convicção jurídica dos membros do MP; existe apenas chefia na esfera administrativa.
> - **C)** Incorreta. O MP goza de **autonomia funcional, administrativa e financeira**, não sendo subordinado ao Poder Executivo ou ao Ministério da Justiça (art. 127, § 2º).
> - **D)** Incorreta. São atributos do ato administrativo ou princípios do direito processual penal.
> - **E)** Incorreta. Princípios alheios à estrutura do parquet.
>
> **Gabarito: A**"""

q11_05 = """### Questão 11 (FGV - Analista de Controle Externo / Auditoria)
A respeito das Funções Essenciais à Justiça disciplinadas nos arts. 131 a 135 da Constituição Federal, compare as atribuições e o regime constitucional da Advocacia Pública e da Defensoria Pública.

Assinale a afirmativa correta.

* **A)** A Advocacia-Geral da União (AGU) e as Procuradorias dos Estados (PGEs) têm como missão institucional prestar assistência jurídica integral e gratuita aos cidadãos comprovadamente hipossuficientes.
* **B)** A Defensoria Pública é instituição permanente, essencial à função jurisdicional do Estado, incumbindo-lhe, como expressão e instrumento do regime democrático, fundamentalmente, a orientação jurídica, a promoção dos direitos humanos e a defesa, em todos os graus, judicial e extrajudicial, dos direitos individuais e coletivos, de forma integral e gratuita, aos necessitados.
* **C)** Os Procuradores do Estado e os Defensores Públicos podem ser nomeados pelo Chefe do Poder Executivo em comissão, sem necessidade de concurso público de provas e títulos.
* **D)** A Advocacia Pública não possui competência para exercer atividades de consultoria e assessoramento jurídico ao Poder Executivo, limitando-se à representação em juízo.
* **E)** A Defensoria Pública é administrativamente subordinada à Secretaria Estadual de Segurança Pública.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A assistência jurídica aos necessitados/hipossuficientes é missão privativa da **Defensoria Pública** (art. 134 da CF/88). A Advocacia Pública (AGU e PGEs) exerce a representação judicial e a consultoria jurídica das respectivas unidades federadas (pessoas jurídicas de direito público).
> - **B)** Correta. Trata-se da definição literal do art. 134, caput, da Constituição Federal de 1988 (com a redação dada pela EC nº 80/2014), que consagra a estatura e missão fundamental da **Defensoria Pública** como defensora dos vulneráveis e promotora dos direitos humanos.
> - **C)** Incorreta. O ingresso nas carreiras da Advocacia Pública (art. 131, § 2º e art. 132) e da Defensoria Pública (art. 134, § 1º) depende obrigatoriamente de **concurso público de provas e títulos**, com a participação da OAB.
> - **D)** Incorreta. A Advocacia Pública exerce expressamente as atividades de **consultoria e assessoramento jurídico** do Poder Executivo (art. 131).
> - **E)** Incorreta. Às Defensorias Públicas Estaduais são asseguradas expressamente **autonomia funcional e administrativa** e a iniciativa para elaboração de sua proposta orçamentária (art. 134, § 2º, EC 45/04).
>
> **Gabarito: B**"""

# Inserções no arquivo 05 de trás para frente
pos_q05 = t05.find("### Questão 05")
assert pos_q05 != -1
pos_fontes = t05.find("## 🌐 Fontes", pos_q05)
assert pos_fontes != -1
t05 = t05[:pos_fontes] + "\n\n" + q11_05.strip() + "\n\n---\n\n" + t05[pos_fontes:]
t05 = t05[:pos_q05] + "\n\n" + q10_05.strip() + "\n\n---\n\n" + t05[pos_q05:]

pos_q04 = t05.find("### Questão 04")
assert pos_q04 != -1
pos_end_q04 = t05.find("\n\n---\n\n", pos_q04)
assert pos_end_q04 != -1
t05 = t05[:pos_end_q04 + 7] + "\n\n" + q09_05.strip() + "\n\n---\n\n" + t05[pos_end_q04 + 7:]

pos_q03 = t05.find("### Questão 03")
assert pos_q03 != -1
t05 = t05[:pos_q03] + "\n\n" + q08_05.strip() + "\n\n---\n\n" + t05[pos_q03:]

pos_q02 = t05.find("### Questão 02")
assert pos_q02 != -1
pos_end_q02 = t05.find("\n\n---\n\n", pos_q02)
assert pos_end_q02 != -1
t05 = t05[:pos_end_q02 + 7] + "\n\n" + q07_05.strip() + "\n\n---\n\n" + t05[pos_end_q02 + 7:]

pos_q01 = t05.find("### Questão 01")
assert pos_q01 != -1
t05 = t05[:pos_q01] + "\n\n" + q06_05.strip() + "\n\n---\n\n" + t05[pos_q01:]

qs_05 = re.findall(r"### Questão (\d+)", t05)
print("Questões no arquivo 05 do Módulo 17:", qs_05)
assert len(qs_05) == 11
assert sorted(qs_05) == ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']

with open(f05_path, "w", encoding="utf-8") as f:
    f.write(t05)

print("Arquivo 05 do Módulo 17 gravado com sucesso! Total: 11 questões.")
