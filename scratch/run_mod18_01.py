# -*- coding: utf-8 -*-
import os
import re

BASE_DIR = "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/18_nocoes_de_controle_externo"

# ==============================================================================
# FILE 01: 01_sistema_constitucional_e_jurisdicao_dos_tcs.md
# ==============================================================================
f01_path = f"{BASE_DIR}/01_sistema_constitucional_e_jurisdicao_dos_tcs.md"
with open(f01_path, "r", encoding="utf-8") as f:
    t01 = f.read()

assert "### Questão 01" in t01
assert "### Questão 02" in t01
assert "### Questão 03" in t01
assert "### Questão 04" in t01
assert "### Questão 05" in t01

q06_01 = """### Questão 06 (FGV - Auditor de Controle Externo / TCE-GO)
O art. 70 da Constituição Federal de 1988 estabelece que a fiscalização contábil, financeira, orçamentária, operacional e patrimonial da União e das entidades da administração direta e indireta será exercida pelo Congresso Nacional, mediante controle externo, e pelo sistema de controle interno de cada Poder.

A respeito dos aspectos fiscalizados pelo controle externo (cinco dimensões do controle), assinale a afirmativa correta.

* **A)** A fiscalização limita-se ao estrito exame da legalidade formal dos atos administrativos, sendo vedado ao Tribunal de Contas perquirir a economicidade ou a legitimidade das despesas públicas.
* **B)** A fiscalização contábil, financeira, orçamentária, operacional e patrimonial abrange a legalidade, a legitimidade, a economicidade, a aplicação das subvenções e a renúncia de receitas.
* **C)** O controle patrimonial exercido pelo Tribunal de Contas restringe-se a bens imóveis de valor superior a dez milhões de reais.
* **D)** A renúncia de receitas fiscais promovida pelo Chefe do Poder Executivo fica imune ao controle externo dos Tribunais de Contas.
* **E)** As empresas públicas exploradoras de atividade econômica não se sujeitam à fiscalização operacional ou financeira das Cortes de Contas.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O controle externo moderno no Brasil superou a visão reducionista da mera legalidade estrita; avalia a **legitimidade, a economicidade, a eficiência e a eficácia** dos gastos públicos.
> - **B)** Correta. O art. 70, caput, da CF/88 consagra categoricamente o alcance amplo da auditoria governamental: fiscalização contábil, financeira, orçamentária, operacional e patrimonial, abrangendo expressamente a legalidade, a legitimidade, a **economicidade**, a aplicação das subvenções e a renúncia de receitas públicas.
> - **C)** Incorreta. A fiscalização patrimonial alcança a universalidade dos bens públicos (móveis, imóveis e intangíveis) pertencentes ao ente federado.
> - **D)** Incorreta. A fiscalização da renúncia de receitas (isenções, anistias e incentivos fiscais) é competência constitucional expressa do Tribunal de Contas (art. 70, caput).
> - **E)** Incorreta. Todas as empresas estatais da Administração Indireta sujeitam-se ao controle externo (art. 70, caput c/c art. 71, II).
>
> **Gabarito: B**"""

q07_01 = """### Questão 07 (FCC - Analista de Controle Externo / TCE-GO)
No modelo de controle externo desenhado pela Constituição da República de 1988, a competência para julgar as contas públicas divide-se com base na natureza das funções exercidas pelo responsável.

Sobre a distinção entre o julgamento das contas dos administradores públicos e a apreciação das contas prestadas pelo Chefe do Poder Executivo, assinale a afirmativa correta.

* **A)** As contas de gestão prestadas pelos administradores e demais responsáveis por dinheiros, bens e valores públicos são julgadas em definitivo pelo próprio Tribunal de Contas (art. 71, II, CF/88).
* **B)** As contas anuais prestadas pelo Presidente da República, pelos Governadores e pelos Prefeitos são julgadas em caráter final pelo Tribunal de Contas por decisão colegiada de seu Plenário.
* **C)** O parecer prévio emitido pelo Tribunal de Contas sobre as contas do Governador do Estado vincula compulsoriamente a Assembleia Legislativa.
* **D)** O Poder Legislativo julga definitivamente as contas de gestão de todos os secretários de Estado e diretores de autarquias estaduais.
* **E)** O Tribunal de Contas não pode emitir parecer desfavorável à aprovação das contas do Chefe do Executivo sem autorização prévia da mesa diretora do parlamento.

> **Comentário Detalhado:**
>
> - **A)** Correta. O art. 71, II, da CF/88 estabelece que compete privativamente ao Tribunal de Contas: *"julgar as contas dos administradores e demais responsáveis por dinheiros, bens e valores públicos da administração direta e indireta [...] e as contas daqueles que derem causa a perda, extravio ou outra irregularidade de que resulte prejuízo ao erário público"*. Trata-se de julgamento técnico de contas de gestão emitido com força definitiva na esfera administrativa.
> - **B)** Incorreta. As contas anuais dos Chefes do Poder Executivo (contas de governo) são **apreciadas** pelo Tribunal de Contas mediante **parecer prévio** técnico-opinativo (art. 71, I), cabendo o **julgamento político exclusivo ao respectivo Poder Legislativo** (Congresso Nacional, Assembleia Legislativa ou Câmara Municipal).
> - **C)** Incorreta. O parecer prévio não vincula a Assembleia Legislativa; constitui subsídio técnico para a deliberação política dos deputados estaduais.
> - **D)** Incorreta. Contas de secretários e dirigentes autárquicos (contas de gestão) são julgadas diretamente pelo Tribunal de Contas, e não pelo Legislativo.
> - **E)** Incorreta. O Tribunal de Contas atua com plena independência técnico-institucional na emissão de seus pareceres prévios.
>
> **Gabarito: A**"""

q08_01 = """### Questão 08 (FGV - Auditor de Controle Externo / TCE-SC)
O Tribunal de Contas, no exercício de sua competência para apreciar, para fins de registro, a legalidade dos atos de concessão inicial de aposentadoria de servidor público estadual (art. 71, III, c/c art. 75 da CF/88), recebeu o processo administrativo encaminhado pelo órgão de origem.

Considerando a tese fixada pelo Supremo Tribunal Federal no Tema nº 445 de Repercussão Geral (RE 636.553), o Tribunal de Contas:

* **A)** Tem o prazo improrrogável de dois anos, contado da data do pedido de aposentadoria protocolado pelo servidor no órgão de origem, para negar o registro.
* **B)** Dispõe do prazo de cinco anos, a contar da chegada do processo à Corte de Contas, para apreciar a legalidade do ato de concessão de aposentadoria, reforma ou pensão; decorrido esse prazo sem manifestação, opera-se a estabilização da situação do beneficiário e o registro tácito do ato concessivo.
* **C)** Fica impedido de recusar o registro caso a concessão de aposentadoria tenha sido respaldada em certidão por tempo de contribuição fraudulenta.
* **D)** Deve assegurar o contraditório e a ampla defesa ao servidor nos primeiros cinco anos da tramitação do processo dentro do Tribunal de Contas (Súmula Vinculante nº 3).
* **E)** Pode anular a aposentadoria a qualquer tempo, mesmo após trinta anos da concessão, ante a imprescritibilidade absoluta dos atos administrativos nulos.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O termo a quo não é o protocolo originário no órgão de origem, mas sim a **chegada formal do processo ao Tribunal de Contas**, e o prazo é de 5 anos.
> - **B)** Correta. Tese de repercussão geral fixada pelo STF no **Tema 445** (RE 636.553): *"Em atenção aos princípios da segurança jurídica e da confiança legítima, os Tribunais de Contas estão sujeitos ao prazo de 5 anos para o julgamento da legalidade do ato de concessão inicial de aposentadoria, reforma ou pensão, a contar da chegada do processo à respectiva Corte de Contas, em atenção ao art. 1º do Decreto 20.910/1932. Passado esse prazo sem finalização do processo, o ato considerar-se-á definitivamente registrado"*.
> - **C)** Incorreta. Hipóteses de comprovada má-fé afastam a estabilização decadencial.
> - **D)** Incorreta. Nos termos da Súmula Vinculante nº 3 do STF, no exame de registro inicial de aposentadoria, pensão e reforma, **não é obrigatório o contraditório prévio** perante o TC nos primeiros 5 anos, por se tratar de ato complexo em formação.
> - **E)** Incorreta. O STF baniu a tese da anulação perpétua de aposentadorias por violar frontalmente a segurança jurídica e a dignidade humana.
>
> **Gabarito: B**"""

q09_01 = """### Questão 09 (FCC - Procurador do Estado / Adaptada)
Durante auditoria em procedimento licitatório de grande vulto deflagrado por empresa pública estadual para a construção de uma usina termoelétrica, a equipe técnica do Tribunal de Contas constatou indícios veementes de direcionamento do certame e risco iminente de dano de difícil reparação ao erário.

Diante desse cenário e com fulcro no poder cautelar implícito reconhecido pelo Supremo Tribunal Federal, o Tribunal de Contas pode:

* **A)** Decretar diretamente e de ofício a prisão temporária de todos os membros da comissão de licitação.
* **B)** Determinar cautelarmente a suspensão do procedimento licitatório até a deliberação final sobre o mérito das irregularidades apontadas.
* **C)** Expropriar compulsoriamente o patrimônio das empresas licitantes participantes da disputa.
* **D)** Anular unilateralmente contratos já assinados sem prévia notificação da autoridade administrativa.
* **E)** Substituir o edital de licitação pelo seu próprio modelo regulamentar e declarar vencedora a segunda colocada.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O Tribunal de Contas não tem competência jurisdicional penal nem poderes para decretar prisão preventiva ou temporária.
> - **B)** Correta. Jurisprudência consolidada do STF (MS 24.510, Rel. Min. Ellen Gracie): a outorga constitucional de competência fiscalizatória e decisória aos Tribunais de Contas importa no deferimento implícito dos meios necessários à sua efetivação (**Teoria dos Poderes Implícitos**), incluindo a prerrogativa de **expedir medidas cautelares** para suspender procedimentos licitatórios irregulares que ameacem o erário público antes da assinatura de contratos lesivos.
> - **C)** Incorreta. Desapropriação ou expropriação é competência privativa do Poder Executivo (art. 5º, XXIV da CF/88).
> - **D)** Incorreta. Nos termos do art. 71, § 1º, da CF/88, em caso de contrato, o ato de sustação é adotado diretamente pelo Congresso Nacional/Assembleia Legislativa e, se este não deliberar em noventa dias, pelo próprio Tribunal.
> - **E)** Incorreta. O Tribunal de Contas exerce controle de legalidade e legitimidade; não atua como administrador ativo para gerir licitações ou substituir editais.
>
> **Gabarito: B**"""

q10_01 = """### Questão 10 (FGV - Analista de Controle Externo / TCE-GO)
O art. 71, § 3º, da Constituição Federal estabelece que as decisões do Tribunal de Contas de que resulte imputação de débito ou multa terão eficácia de título executivo.

Sobre a prescrição da pretensão de ressarcimento ao erário fundada em decisões de Tribunal de Contas, consoante tese fixada pelo Supremo Tribunal Federal no Tema nº 899 de Repercussão Geral (RE 636.886), assinale a afirmativa correta.

* **A)** A pretensão de ressarcimento ao erário fundada em acórdão condenatório de Tribunal de Contas é absolutamente imprescritível, em virtude do art. 37, § 5º, da Constituição Federal.
* **B)** É prescritível a pretensão de ressarcimento ao erário fundada em decisão de Tribunal de Contas, aplicando-se o prazo prescricional quinquenal (cinco anos) previsto na Lei nº 6.830/1980 (Lei de Execução Fiscal).
* **C)** O prazo prescricional para execução da decisão do Tribunal de Contas é de dez anos, regulado pelas regras gerais do Código Civil.
* **D)** A prescrição da cobrança do débito impede a emissão de certidão de débitos pelo Tribunal de Contas.
* **E)** A execução fiscal do título emitido pelo Tribunal de Contas deve ser proposta perante o Tribunal de Justiça em competência originária.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A imprescritibilidade do art. 37, § 5º, da CF/88 restringe-se às ações de ressarcimento decorrentes de **atos dolosos de improbidade administrativa julgados judicialmente** (Tema 897/STF). Não se aplica às decisões de Tribunais de Contas.
> - **B)** Correta. O STF fixou a seguinte tese vinculante no **Tema 899 de Repercussão Geral** (RE 636.886): *"É prescritível a pretensão de ressarcimento ao erário fundada em decisão de Tribunal de Contas"*. O prazo aplicável à execução fiscal da dívida ativa é de **5 (cinco) anos**, em consonância com a Lei de Execução Fiscal e o Decreto nº 20.910/1932.
> - **C)** Incorreta. O prazo do Código Civil não se aplica às execuções de dívidas públicas fazendárias.
> - **D)** Incorreta. O foco do julgamento foi a pretensão executória patrimonial da Fazenda Pública.
> - **E)** Incorreta. A execução fiscal tramita na primeira instância da Justiça Comum perante as Varas da Fazenda Pública.
>
> **Gabarito: B**"""

q11_01 = """### Questão 11 (FCC - Auditor Governamental / Controle Externo)
A respeito da independência das instâncias e da jurisdição ampla dos Tribunais de Contas, considere que determinado gestor público foi absolvido em ação penal instaurada perante a Justiça Estadual pela suposta prática de peculato, sob o fundamento de insuficiência de provas para a condenação (art. 386, VII, do CPP).

Nessa hipótese, a decisão penal absolutória por falta de provas:

* **A)** Impede compulsoriamente o Tribunal de Contas de condenar o gestor em tomada de contas especial, operando coisa julgada material vinculante para a Corte de Contas.
* **B)** Não vincula o Tribunal de Contas nem impede a condenação do gestor ao ressarcimento do dano e à aplicação de multa pelo Tribunal de Contas, tendo em vista o princípio da independência e autonomia das instâncias administrativa e penal.
* **C)** Obriga o Tribunal de Contas a anular todos os acórdãos condenatórios já proferidos sobre o mesmo fato.
* **D)** Transfere a competência decisória sobre o processo de controle externo para o juízo da vara criminal estadual.
* **E)** Só permitirá a cobrança do débito se a absolvição penal for reformada pelo Supremo Tribunal Federal em grau de recurso extraordinário.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. No ordenamento brasileiro vigora o postulado da **independência das instâncias**. A sentença absolutória criminal por falta ou insuficiência de provas (art. 386, VII, CPP) não faz coisa julgada na esfera civil ou administrativa, não vinculando o Tribunal de Contas.
> - **B)** Correta. As únicas hipóteses em que a sentença penal absolutória vincula as esferas administrativa e controladora dos Tribunais de Contas são: (1) a declaração inequívoca da **inexistência material do fato** (art. 386, I, CPP); e (2) a comprovação cabal de **negativa de autoria** (art. 386, IV, CPP). A absolvição por falta de provas ou atipicidade penal não impede que o Tribunal de Contas apure a ilicitude financeira, impute débito e aplique sanções administrativas.
> - **C)** Incorreta. O acórdão do TC mantém plena validade e higidez jurídica.
> - **D)** Incorreta. O juízo criminal não absorve a competência fiscalizatória das Cortes de Contas.
> - **E)** Incorreta. A execução do título do TC prossegue de forma autônoma.
>
> **Gabarito: B**"""

# Inserções no arquivo 01 de trás para frente
pos_q05 = t01.find("### Questão 05")
assert pos_q05 != -1
pos_fontes = t01.find("## 🌐 Fontes", pos_q05)
assert pos_fontes != -1
t01 = t01[:pos_fontes] + "\n\n" + q11_01.strip() + "\n\n---\n\n" + t01[pos_fontes:]

pos_q04 = t01.find("### Questão 04")
assert pos_q04 != -1
pos_end_q04 = t01.find("\n\n---\n\n", pos_q04)
assert pos_end_q04 != -1
t01 = t01[:pos_end_q04 + 7] + "\n\n" + q10_01.strip() + "\n\n---\n\n" + t01[pos_end_q04 + 7:]

pos_q03 = t01.find("### Questão 03")
assert pos_q03 != -1
pos_end_q03 = t01.find("\n\n---\n\n", pos_q03)
assert pos_end_q03 != -1
t01 = t01[:pos_end_q03 + 7] + "\n\n" + q09_01.strip() + "\n\n---\n\n" + t01[pos_end_q03 + 7:]

pos_q02 = t01.find("### Questão 02")
assert pos_q02 != -1
pos_end_q02 = t01.find("\n\n---\n\n", pos_q02)
assert pos_end_q02 != -1
t01 = t01[:pos_end_q02 + 7] + "\n\n" + q08_01.strip() + "\n\n---\n\n" + t01[pos_end_q02 + 7:]

ancora_3 = "### 3. Competências Constitucionais: Julgamento Técnico versus Parecer Prévio"
pos_3 = t01.find(ancora_3)
pos_4 = t01.find("### 4. Registro de Atos de Admissão", pos_3)
assert pos_3 != -1 and pos_4 != -1
t01 = t01[:pos_4] + "\n\n" + q07_01.strip() + "\n\n---\n\n" + t01[pos_4:]

pos_q01 = t01.find("### Questão 01")
assert pos_q01 != -1
t01 = t01[:pos_q01] + "\n\n" + q06_01.strip() + "\n\n---\n\n" + t01[pos_q01:]

qs_01 = re.findall(r"### Questão (\d+)", t01)
print("Questões no arquivo 01 do Módulo 18:", qs_01)
assert len(qs_01) == 11
assert sorted(qs_01) == ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']

with open(f01_path, "w", encoding="utf-8") as f:
    f.write(t01)

print("Arquivo 01 do Módulo 18 gravado com sucesso! Total: 11 questões.")
