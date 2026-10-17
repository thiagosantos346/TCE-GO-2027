# -*- coding: utf-8 -*-
import os
import re

BASE_DIR = "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/17_nocoes_de_direito_constitucional"
f04_path = f"{BASE_DIR}/04_poder_legislativo_processo_legislativo_e_fiscalizacao_tce.md"
with open(f04_path, "r", encoding="utf-8") as f:
    t04 = f.read()

assert "### Questão 01" in t04
assert "### Questão 02" in t04
assert "### Questão 03" in t04
assert "### Questão 04" in t04
assert "### Questão 05" in t04

q06_04 = """### Questão 06 (FCC - Analista Legislativo - Área Processo Legislativo)
As Comissões Parlamentares de Inquérito (CPIs), previstas no art. 58, § 3º, da Constituição Federal, são dotadas de poderes de investigação próprios das autoridades judiciais, além de outros previstos nos regimentos das respectivas Casas.

A respeito dos limites constitucionais e jurisprudenciais dos poderes de uma CPI, assinale a afirmativa correta.

* **A)** Uma CPI pode determinar diretamente a quebra do sigilo fiscal, bancário e telefônico (dados cadastrais e registros de ligações) do investigado, desde que mediante decisão fundamentada aprovada pela maioria de seus membros.
* **B)** A CPI tem competência constitucional para decretar a interceptação telefônica (escuta em tempo real de comunicações) e a busca e apreensão domiciliar noturna sem mandado judicial.
* **C)** A criação de uma CPI submete-se ao juízo discricionário da maioria parlamentar, podendo o Plenário da Casa rejeitar o requerimento de minoria subscrito por um terço dos membros.
* **D)** A CPI pode decretar a prisão preventiva de indiciado que se recuse a colaborar com os trabalhos investigativos da comissão.
* **E)** As conclusões e relatórios finais de uma CPI possuem eficácia de sentença condenatória criminal irrecorrível.

> **Comentário Detalhado:**
>
> - **A)** Correta. Conforme pacífica jurisprudência do STF (MS 23.452 e MS 23.851), as CPIs dispõem de poderes instrutórios próprios de autoridade judicial para determinar a **quebra de sigilo bancário, fiscal e telefônico (registros pretéritos de chamadas e extratos de dados)**, exigindo-se fundamentação concreta e deliberação colegiada.
> - **B)** Incorreta. Medidas submetidas à estrita **reserva constitucional de jurisdição** (interceptação telefônica em tempo real, busca e apreensão domiciliar, decretação de prisão preventiva) **não podem** ser determinadas por CPIs, exigindo autorização judicial prévia.
> - **C)** Incorreta. A criação de CPI é direito subjetivo das minorias parlamentares (art. 58, § 3º: 1/3 dos membros, fato determinado e prazo certo), não dependendo de votação ou aprovação discricionária do Plenário (MS 24.831/STF).
> - **D)** Incorreta. A CPI não pode decretar prisão preventiva; sua atuação restringe-se a prender em flagrante delito, como qualquer cidadão.
> - **E)** Incorreta. O relatório final da CPI não condena; é encaminhado ao Ministério Público para promoção da responsabilidade civil ou criminal dos infratores (art. 58, § 3º).
>
> **Gabarito: A**"""

q07_04 = """### Questão 07 (FGV - Auditor de Controle Externo / TCE-GO)
O art. 53 da Constituição Federal de 1988 estabelece que os Deputados e Senadores são invioláveis, civil e penalmente, por quaisquer de suas opiniões, palavras e votos (imunidade material ou substantiva).

Sobre as imunidades parlamentares formais ou adjetivas (processuais), assinale a afirmativa correta.

* **A)** Desde a expedição do diploma, os membros do Congresso Nacional não poderão ser presos, salvo em flagrante de crime inafiançável, caso em que os autos serão remetidos dentro de vinte e quatro horas à Casa respectiva, para que, pelo voto da maioria de seus membros, resolva sobre a prisão.
* **B)** A imunidade material protege o parlamentar por declarações emitidas em redes sociais mesmo que absolutamente desvinculadas do exercício do mandato legislativo.
* **C)** Os Deputados Estaduais não gozam das imunidades materiais e formais conferidas pela CF aos parlamentares federais.
* **D)** A instauração de ação penal contra Deputado Federal perante o STF depende de prévia e indispensável licença política da Câmara dos Deputados.
* **E)** A perda do mandato de parlamentar condenado criminalmente com trânsito em julgado opera-se automaticamente pela simples certidão do juízo eleitoral.

> **Comentário Detalhado:**
>
> - **A)** Correta. O art. 53, § 2º, da Constituição Federal consagra literalmente que: *"Desde a expedição do diploma, os membros do Congresso Nacional não poderão ser presos, salvo em flagrante de crime inafiançável. Nesse caso, os autos serão remetidos dentro de vinte e quatro horas à Casa respectiva, para que, pelo voto da maioria de seus membros, resolva sobre a prisão"*.
> - **B)** Incorreta. O STF pacificou que manifestações proferidas fora do recinto parlamentar só estão cobertas pela imunidade material se guardarem **nexo funcional direto** com o exercício do mandato parlamentar (Inq 3.814 e Inq 3.932).
> - **C)** Incorreta. O art. 27, § 1º, da CF/88 estende expressamente aos Deputados Estaduais as mesmas regras sobre imunidades materiais e formais aplicáveis aos Deputados Federais (princípio da simetria).
> - **D)** Incorreta. A EC nº 35/2001 extinguiu a necessidade de licença prévia para instauração da ação penal; a Casa respectiva pode sustar o andamento da ação penal mediante requerimento de partido político e voto da maioria de seus membros (art. 53, § 3º).
> - **E)** Incorreta. Dependendo da hipótese (art. 55, VI), a perda é decidida pela respectiva Casa Legislativa por maioria absoluta.
>
> **Gabarito: A**"""

q08_04 = """### Questão 08 (FCC - Procurador do Estado / Adaptada)
A respeito dos limites ao poder constituinte derivado reformador positivados no art. 60 da Constituição Federal de 1988, analise as seguintes afirmativas sobre as propostas de emenda à Constituição (PECs):

I. A Constituição não poderá ser emendada na vigência de intervenção federal, de estado de defesa ou de estado de sítio (limitações circunstanciais).  
II. Não será objeto de deliberação a proposta de emenda tendente a abolir a forma federativa de Estado, o voto direto, secreto, universal e periódico, a separação dos Poderes e os direitos e garantias individuais (cláusulas pétreas / limitações materiais).  
III. A emenda à Constituição será promulgada pelas Mesas da Câmara dos Deputados e do Senado Federal, com o respectivo número de ordem, inexistindo sanção ou veto do Presidente da República.

Está correto o que se afirma em:

* **A)** I, apenas.
* **B)** I e II, apenas.
* **C)** II e III, apenas.
* **D)** I e III, apenas.
* **E)** I, II e III.

> **Comentário Detalhado:**
>
> - **I. Correta:** O art. 60, § 1º, da CF/88 estabelece as limitações circunstanciais ao poder de reforma, impedindo emendas durante grave anomalia institucional (intervenção federal, estado de defesa e estado de sítio).
> - **II. Correta:** O art. 60, § 4º, elenca as chamadas **cláusulas pétreas** (limitações materiais explícitas): I - a forma federativa de Estado; II - o voto direto, secreto, universal e periódico; III - a separação dos Poderes; IV - os direitos e garantias individuais. Propostas tendentes a aboli-las sequer podem ser objeto de deliberação legislativa.
> - **III. Correta:** O art. 60, § 3º, da CF/88 dispõe que a emenda promulgada diretamente pelas **Mesas da Câmara dos Deputados e do Senado Federal**. O Presidente da República não participa do processo de promulgação, não possuindo poder de veto sobre emendas constitucionais.
>
> Todas as afirmativas encontram-se rigorosamente corretas.
>
> **Gabarito: E**"""

q09_04 = """### Questão 09 (FGV - Analista de Controle Externo / TCE-GO)
O art. 62 da Constituição da República de 1988 autoriza o Presidente da República a adotar medidas provisórias, com força de lei, em caso de relevância e urgência.

Sobre as limitações materiais e temporais expressas aplicáveis às medidas provisórias, assinale a afirmativa correta.

* **A)** É permitida a edição de medida provisória sobre matéria relativa a direito penal, direito processual penal e direito processual civil.
* **B)** As medidas provisórias terão prazo de vigência de sessenta dias, prorrogável uma vez por igual período se não tiver a sua votação encerrada nas duas Casas do Congresso Nacional.
* **C)** O Presidente da República pode editar medida provisória que disponha sobre planos plurianuais, diretrizes orçamentárias e orçamento anual.
* **D)** É lícita a edição de medida provisória que vise à detenção ou sequestro de bens, de poupança popular ou de qualquer outro ativo financeiro dos cidadãos.
* **E)** Se a medida provisória não for apreciada em até quarenta e cinco dias de sua publicação, ela perde sumariamente sua eficácia retroativa.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O art. 62, § 1º, I, 'b', da CF/88 veda terminantemente medida provisória sobre direito penal, processual penal e processual civil.
> - **B)** Correta. O art. 62, § 3º e § 7º, da CF/88 estabelece que as medidas provisórias terão eficácia por **60 (sessenta) dias**, prorrogáveis automaticamente **uma única vez por igual período (60 dias)** se não tiverem sua votação concluída em ambas as Casas Legislativas.
> - **C)** Incorreta. O art. 62, § 1º, I, 'd', veda medida provisória sobre planos plurianuais, diretrizes orçamentárias, orçamento e créditos adicionais (ressalvados créditos extraordinários do art. 167, § 3º).
> - **D)** Incorreta. A EC nº 32/2001 vedou expressamente medida provisória que vise à retenção de poupança ou sequestro de ativos financeiros (art. 62, § 1º, II).
> - **E)** Incorreta. Ultrapassados 45 dias sem votação, a MP entra em **regime de urgência**, sobrestando as demais deliberações legislativas da Casa (trancamento de pauta, art. 62, § 6º), mas continua válida até o prazo final de 120 dias.
>
> **Gabarito: B**"""

q10_04 = """### Questão 10 (FCC - Técnico de Controle Externo / Adaptada TCE-GO)
A Constituição Federal de 1988, ao disciplinar a composição do Tribunal de Contas da União (art. 73) e estabelecer o princípio da simetria para os Tribunais de Contas dos Estados (art. 75), definiu o modelo constitucional de preenchimento dos cargos de Conselheiro.

No Tribunal de Contas do Estado de Goiás (TCE-GO), composto por sete Conselheiros, as vagas são preenchidas de acordo com a seguinte proporção constitucional:

* **A)** Sete Conselheiros nomeados exclusivamente pelo Governador do Estado com aprovação do Poder Judiciário.
* **B)** Quatro Conselheiros escolhidos pela Assembleia Legislativa; e três Conselheiros escolhidos pelo Governador do Estado, com aprovação da Assembleia Legislativa, sendo um de sua livre escolha e dois alternadamente entre auditores substitutos de conselheiro e membros do Ministério Público junto ao Tribunal de Contas, indicados em lista tríplice pelo Tribunal.
* **C)** Três Conselheiros pela Assembleia Legislativa e quatro Conselheiros pelo Governador do Estado.
* **D)** Seis Conselheiros eleitos por voto direto dos cidadãos goianos e um indicado pela Ordem dos Advogados do Brasil.
* **E)** Cinco Conselheiros indicados pelo Poder Judiciário e dois indicados pela Controladoria-Geral do Estado.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A Assembleia Legislativa indica a maioria dos membros do Tribunal de Contas.
> - **B)** Correta. O art. 73, § 2º, c/c art. 75 da CF/88 e a Constituição do Estado de Goiás consagram o modelo simétrico obrigatório de composição dos Tribunais de Contas Estaduais (compostos por 7 membros): (1) **quatro Conselheiros** escolhidos privativamente pelo Poder Legislativo (Assembleia Legislativa); e (2) **três Conselheiros** indicados pelo Governador do Estado, com aprovação da Assembleia, sendo um de livre escolha do Chefe do Executivo e dois necessariamente técnicos (um Auditor/Conselheiro-Substituto de carreira e um Procurador de Contas do MPC, ambos indicados em lista tríplice de antiguidade e merecimento pelo próprio Tribunal).
> - **C)** Incorreta. Inverte a proporção; o Legislativo indica quatro e o Executivo indica três.
> - **D)** Incorreta. A escolha dos Conselheiros é indireta e institucionalizada nos moldes do art. 73 e 75.
> - **E)** Incorreta. O Judiciário não possui vaga na composição originária dos Tribunais de Contas.
>
> **Gabarito: B**"""

q11_04 = """### Questão 11 (FGV - Analista Jurídico de Controle Externo / TCE-GO)
A fiscalização dos municípios é exercida pelo Poder Legislativo municipal, mediante controle externo, e pelos sistemas de controle interno do Poder Executivo municipal, com o auxílio dos Tribunais de Contas (art. 31 da CF/88).

A respeito da eficácia do parecer prévio emitido pelo Tribunal de Contas e do julgamento das contas do Prefeito Municipal, em consonância com a jurisprudência fixada pelo STF (Temas 835 e 157 de Repercussão Geral), assinale a afirmativa correta.

* **A)** O parecer prévio emitido pelo Tribunal de Contas sobre as contas anuais prestadas pelo Prefeito vincula compulsoriamente a Câmara Municipal, operando a rejeição automática das contas sem necessidade de votação parlamentar.
* **B)** Para os fins da inelegibilidade da Lei da Ficha Limpa (art. 1º, I, 'g', da LC nº 64/1990), a competência para julgar tanto as contas de governo quanto as contas de gestão do Prefeito Municipal é exclusiva da Câmara Municipal, cabendo ao Tribunal de Contas a emissão de parecer prévio, que só deixará de prevalecer por decisão de dois terços dos vereadores.
* **C)** O Tribunal de Contas tem competência constitucional originária para julgar de forma definitiva as contas de gestão de prefeitos que atuem como ordenadores de despesa, dispensando pronunciamento da Câmara.
* **D)** O parecer prévio do Tribunal de Contas sobre as contas do Prefeito só pode ser rejeitado pela Câmara Municipal por unanimidade absoluta de votos.
* **E)** A criação de novos Tribunais, Conselhos ou órgãos de Contas Municipais é expressamente autorizada pelos arts. 31 e 75 da CF/88 aos municípios com mais de um milhão de habitantes.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O parecer prévio é peça técnico-opinativa que subsidia o julgamento político da Câmara de Vereadores.
> - **B)** Correta. O STF pacificou nos **Temas 835 e 157 de Repercussão Geral** (RE 848.826 e RE 729.744) que: a competência para julgar as contas de Prefeito (sejam contas de governo, sejam contas de gestão na qualidade de ordenador de despesas) para fins de inelegibilidade eleitoral é **exclusiva da Câmara Municipal**, cabendo ao Tribunal de Contas atuar como órgão técnico auxiliar mediante a emissão de parecer prévio. E o art. 31, § 2º, da CF/88 determina que *"O parecer prévio, emitido pelo órgão competente sobre as contas que o Prefeito deve anualmente prestar, só deixará de prevalecer por decisão de dois terços dos membros da Câmara Municipal"*.
> - **C)** Incorreta. O STF afastou o julgamento direto pelo Tribunal de Contas para fins de inelegibilidade do Prefeito ordenador de despesa, exigindo a decisão da Câmara.
> - **D)** Incorreta. O quórum qualificado exigido pela CF para rejeitar o parecer prévio é de **2/3 (dois terços)** dos membros da Câmara, e não unanimidade.
> - **E)** Incorreta. O art. 31, § 4º, da CF/88 veda peremptoriamente a criação de novos Tribunais, Conselhos ou órgãos de Contas municipais.
>
> **Gabarito: B**"""

# Inserções no arquivo 04 de trás para frente
pos_q05 = t04.find("### Questão 05")
assert pos_q05 != -1
pos_fontes = t04.find("## 🌐 Fontes", pos_q05)
assert pos_fontes != -1
t04 = t04[:pos_fontes] + "\n\n" + q11_04.strip() + "\n\n---\n\n" + t04[pos_fontes:]

pos_q03 = t04.find("### Questão 03")
assert pos_q03 != -1
t04 = t04[:pos_q03] + "\n\n" + q10_04.strip() + "\n\n---\n\n" + t04[pos_q03:]

pos_q02 = t04.find("### Questão 02")
assert pos_q02 != -1
pos_end_q02 = t04.find("\n\n---\n\n", pos_q02)
assert pos_end_q02 != -1
t04 = t04[:pos_end_q02 + 7] + "\n\n" + q09_04.strip() + "\n\n---\n\n" + t04[pos_end_q02 + 7:]
t04 = t04[:pos_q02] + "\n\n" + q08_04.strip() + "\n\n---\n\n" + t04[pos_q02:]

pos_q01 = t04.find("### Questão 01")
assert pos_q01 != -1
pos_end_q01 = t04.find("\n\n---\n\n", pos_q01)
assert pos_end_q01 != -1
t04 = t04[:pos_end_q01 + 7] + "\n\n" + q07_04.strip() + "\n\n---\n\n" + t04[pos_end_q01 + 7:]
t04 = t04[:pos_q01] + "\n\n" + q06_04.strip() + "\n\n---\n\n" + t04[pos_q01:]

qs_04 = re.findall(r"### Questão (\d+)", t04)
print("Questões no arquivo 04 do Módulo 17:", qs_04)
assert len(qs_04) == 11
assert sorted(qs_04) == ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']

with open(f04_path, "w", encoding="utf-8") as f:
    f.write(t04)

print("Arquivo 04 do Módulo 17 gravado com sucesso! Total: 11 questões.")
