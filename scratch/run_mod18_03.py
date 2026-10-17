# -*- coding: utf-8 -*-
import os
import re

BASE_DIR = "fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo/18_nocoes_de_controle_externo"
f03_path = f"{BASE_DIR}/03_planejamento_amostragem_procedimentos_e_achados.md"
with open(f03_path, "r", encoding="utf-8") as f:
    t03 = f.read()

assert "### Questão 01" in t03
assert "### Questão 02" in t03
assert "### Questão 03" in t03
assert "### Questão 04" in t03
assert "### Questão 05" in t03

q06_03 = """### Questão 06 (FCC - Auditor de Controle Externo / TCE-GO)
No planejamento de uma auditoria governamental, a avaliação do risco de auditoria é fundamental para dimensionar a extensão, a oportunidade e a natureza dos procedimentos a serem aplicados.

Sobre os componentes do risco de auditoria (risco inerente, risco de controle e risco de detecção), assinale a afirmativa correta.

* **A)** O risco de detecção decorre da suscetibilidade de uma afirmação a uma distorção relevante antes da consideração de quaisquer controles internos compensatórios.
* **B)** O risco inerente e o risco de controle existem independentemente da auditoria e são próprios da entidade auditada e de seus processos internos de governança.
* **C)** O risco de controle é o risco de que os procedimentos executados pelo auditor não detectem uma distorção relevante existente no órgão fiscalizado.
* **D)** O auditor do Tribunal de Contas pode controlar e modificar diretamente o nível de risco inerente existente na secretaria auditada.
* **E)** Se o auditor avaliar o risco de controle interno como muito alto, ele deve reduzir o volume de testes substantivos de auditoria para economizar recursos.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A suscetibilidade intrínseca a distorções antes de considerar os controles é o **risco inerente** (NBASP 200).
> - **B)** Correta. A doutrina e as normas de auditoria internacional (NBASP 100/200) estabelecem que o **risco inerente** (inerente à complexidade ou volatilidade da atividade pública) e o **risco de controle** (risco de o sistema de controle interno do órgão falhar em prevenir ou detectar tempestivamente uma distorção) são riscos próprios da entidade auditada, existindo independentemente da realização de auditoria externa.
> - **C)** Incorreta. O risco de que os procedimentos do auditor falhem em detectar o erro é o **risco de detecção**, que é o único componente diretamente controlado pela equipe de auditoria (por meio do tamanho da amostra e profundidade dos testes).
> - **D)** Incorreta. O risco inerente independe da atuação do auditor; o auditor apenas o avalia.
> - **E)** Incorreta. Quanto mais alto o risco de controle, **maior** deve ser a quantidade de testes substantivos e procedimentos de detecção do auditor para mitigar o risco global de auditoria.
>
> **Gabarito: B**"""

q07_03 = """### Questão 07 (FGV - Analista de Controle Externo / TCE-GO)
Os papéis de trabalho (documentação de auditoria) constituem o registro físico ou eletrônico de todo o planejamento, dos procedimentos técnicos aplicados, das evidências obtidas e das conclusões alcançadas pela equipe de fiscalização do Tribunal de Contas.

A respeito dos papéis de trabalho na auditoria do setor público (NBASP 100 e NBASP 230), assinale a afirmativa correta.

* **A)** Os papéis de trabalho são de propriedade exclusiva do gestor público auditado, devendo ser devolvidos ao órgão no encerramento da inspeção in loco.
* **B)** A documentação de auditoria deve ser suficientemente completa e detalhada para permitir que um auditor experiente, sem nenhum contato prévio com a auditoria, compreenda a natureza, a época, a extensão dos procedimentos executados, as evidências obtidas e as conclusões alcançadas.
* **C)** É dispensável registrar nos papéis de trabalho a metodologia empregada na seleção de amostras estatísticas.
* **D)** O auditor pode destruir de ofício papéis de trabalho que contenham evidências divergentes das conclusões emitidas no relatório final.
* **E)** Os papéis de trabalho elaborados em fiscalizações de controle externo não possuem valor probatório para fins de instauração de tomada de contas especial.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Os papéis de trabalho são de **propriedade da Entidade Fiscalizadora Superior (Tribunal de Contas)** e ficam sob sua custódia e responsabilidade permanente.
> - **B)** Correta. A NBASP 230 (Documentação de Auditoria) estabelece a chamada regra do **auditor experiente**: a documentação deve ser preparada em nível de detalhamento e clareza suficiente para que um auditor experiente, que não tenha participado anteriormente do trabalho, compreenda os objetivos, a metodologia, os testes realizados, as evidências que suportam os achados e a fundamentação técnica das conclusões e recomendações emitidas.
> - **C)** Incorreta. Toda a memória de cálculo e os parâmetros amostrais devem constar obrigatoriamente nos papéis de trabalho.
> - **D)** Incorreta. A destruição ou sonegação de evidências é infração gravíssima; evidências contraditórias devem ser registradas e tratadas tecnicamente.
> - **E)** Incorreta. Os papéis de trabalho formam a base probatória idônea e documental indispensável que lastreia os achados e os processos de responsabilização no Tribunal de Contas.
>
> **Gabarito: B**"""

q08_03 = """### Questão 08 (FCC - Analista Judiciário - Área Administrativa)
No planejamento da execução de auditoria contábil e de conformidade em uma secretaria estadual com milhares de processos de pagamento anuais, a equipe de auditoria optou pelo emprego de amostragem em auditoria.

Sobre as técnicas e modalidades de amostragem em auditoria governamental, assinale a afirmativa correta.

* **A)** A amostragem não estatística (por julgamento) permite ao auditor mensurar matematicamente o risco de amostragem e extrapolar com precisão probabilística os resultados para toda a população.
* **B)** Na amostragem estatística, a seleção dos itens da amostra ocorre de forma aleatória ou sistemática fundamentada no cálculo de probabilidades, permitindo que todos os itens da população tenham chance conhecida de serem selecionados, viabilizando a mensuração do risco de amostragem.
* **C)** O risco de amostragem é o risco de o auditor aplicar testes inadequados ou interpretar incorretamente os documentos fiscais analisados.
* **D)** A amostragem é obrigatória em 100% das fiscalizações de controle externo, sendo proibido aos auditores o exame integral (censo) de qualquer contrato.
* **E)** O tamanho da amostra estatística independe do nível de confiança e da taxa de desvio tolerável definidos no plano de auditoria.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A amostragem não estatística (baseada exclusivamente no tirocínio ou julgamento do auditor) não permite calcular matematicamente o risco de amostragem nem extrapolar os resultados com rigor probabilístico.
> - **B)** Correta. Na **amostragem estatística**, os itens são selecionados aleatoriamente com apoio no cálculo de probabilidades, conferindo a todos os elementos do universo a mesma probabilidade matemática de seleção e permitindo quantificar objetivamente o **risco de amostragem** e o nível de precisão dos testes.
> - **C)** Incorreta. Falhas humanas na interpretação ou seleção de procedimentos inadequados configuram o **risco não amostral**. O risco de amostragem é a possibilidade de a conclusão baseada na amostra ser diferente daquela que seria obtida se toda a população fosse examinada.
> - **D)** Incorreta. O auditor pode optar pelo exame integral (100% da população) quando o universo for pequeno ou quando os itens tiverem valor econômico extremamente elevado ou risco crítico.
> - **E)** Incorreta. O tamanho da amostra é calculado em função direta do nível de confiança desejado, da margem de erro e da taxa de desvio tolerável.
>
> **Gabarito: B**"""

q09_03 = """### Questão 09 (FGV - Auditor de Controle Externo / TCE-SC)
Durante auditoria de conformidade em contrato de fornecimento de merenda escolar, a equipe técnica do Tribunal de Contas necessitou confirmar os saldos financeiros e as entregas efetivas de mercadorias declaradas pela empresa contratada em notas fiscais suspeitas.

Para tanto, os auditores enviaram correspondência formal direta aos fornecedores atacadistas primários da empresa, solicitando a confirmação formal e por escrito das quantidades e dos valores das notas emitidas contra a contratada.

O procedimento de auditoria adotado denomina-se:

* **A)** Inspeção física, que consiste no exame in loco das características visuais de um canteiro de obras.
* **B)** Confirmação externa (circularização), caracterizada pela obtenção direta de uma declaração por escrito de um terceiro independente sobre determinadas informações fiscais, bancárias ou operacionais.
* **C)** Procedimento analítico preliminar, baseado unicamente em gráficos e estatísticas orçamentárias gerais.
* **D)** Reexecução, consubstanciada na repetição independente pelo auditor de cálculos aritméticos efetuados pela contabilidade.
* **E)** Observação direta passiva de uma rotina burocrática de almoxarifado.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Inspeção física é a verificação material presencial da existência de bens ou obras.
> - **B)** Correta. A **confirmação externa (ou circularização)**, disciplinada pela NBASP 505 / NBC TA 505, é a evidência obtida pelo auditor como uma resposta direta, por escrito e emitida por um terceiro independente (a parte que confirma) ao auditor, seja em formato de papel, eletrônico ou outro meio. É considerada uma das evidências de maior confiabilidade em auditoria governamental.
> - **C)** Incorreta. Procedimentos analíticos envolvem avaliações de informações financeiras por meio de análise de relações plausíveis entre dados financeiros e não financeiros (análise de tendências e índices).
> - **D)** Incorreta. A conferência matemática de somas e produtos denomina-se **recálculo**; **reexecução** é a realização independente de processos ou controles.
> - **E)** Incorreta. Observação consiste em acompanhar presencialmente a realização de um procedimento executado por terceiros.
>
> **Gabarito: B**"""

q10_03 = """### Questão 10 (FCC - Procurador do Estado / Adaptada)
A validade e a força persuasiva de um relatório de auditoria emitido pelo Tribunal de Contas dependem diretamente da qualidade das evidências coligidas pela equipe técnica durante os trabalhos de fiscalização.

Nos termos da NBASP 100, para que sustentem adequadamente um achado de auditoria, as evidências devem ser:

* **A)** Secretas e mantidas fora do alcance do contraditório do gestor responsável até a publicação do acórdão condenatório.
* **B)** Suficientes (em quantidade adequada para convencer uma pessoa razoável) e apropriadas (relevantes, válidas e confiáveis em relação ao critério e ao objeto da auditoria).
* **C)** Obtidas exclusivamente mediante confissão expressa do servidor público em termo de oitiva formal.
* **D)** Subjetivas e fundamentadas em ilações conjecturais da imprensa local.
* **E)** Restritas a cópias reprográficas autenticadas em cartório por tabelião de notas.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. As evidências devem ser disponibilizadas ao auditado para assegurar o contraditório e a ampla defesa.
> - **B)** Correta. A NBASP 100 estatui categoricamente que o auditor deve obter **evidência de auditoria suficiente e apropriada** para fundamentar suas conclusões e recomendações: (1) **Suficiência** é a medida da *quantidade* de evidência necessária; (2) **Apropriação** é a medida da *qualidade* da evidência (sua relevância em relação ao critério e sua confiabilidade na representação da realidade).
> - **C)** Incorreta. Em auditoria governamental a evidência documental, física e analítica prevalece sobre o mero testemunho verbal.
> - **D)** Incorreta. Achados não podem ser embasados em meras suposições, boatos ou conjecturas; exigem substrato probatório fático e documental idôneo.
> - **E)** Incorreta. O princípio da verdade material e o art. 37 da CF dispensam a autenticação cartorária de documentos oficiais da administração pública.
>
> **Gabarito: B**"""

q11_03 = """### Questão 11 (FGV - Analista Jurídico de Controle Externo / TCE-GO)
Ao finalizar os trabalhos de fiscalização, a equipe de auditoria do Tribunal de Contas estruturou a matriz de achados, identificando deficiências materiais na execução de um programa estadual de incentivo à agricultura familiar.

A respeito dos elementos constitutivos de um achado de auditoria e das deliberações propositivas emitidas pelo Tribunal de Contas, assinale a afirmativa correta.

* **A)** A condição é o padrão ideal que deveria existir conforme estabelecido na lei ou nas melhores práticas de gestão.
* **B)** O achado de auditoria estrutura-se em quatro elementos fundamentais: a condição (a situação encontrada na prática), o critério (o que deveria ser segundo a lei ou padrão), a causa (a razão pela qual a condição ocorreu) e o efeito (a consequência prática ou impacto do desvio).
* **C)** A recomendação constitui mandamento cogente e impositivo que obriga o gestor a cumprir ordem específica sob pena de prisão imediata.
* **D)** A determinação é mera sugestão de melhoria operacional desprovida de qualquer força coercitiva.
* **E)** O efeito de um achado de auditoria limita-se unicamente ao valor monetário do prejuízo contábil imediato.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O padrão normativo que deveria existir denomina-se **critério**. A situação fática real encontrada no órgão é a **condição**.
> - **B)** Correta. Dogmática clássica de auditoria governamental (NBASP 300 e Manual de Auditoria Operacional do TCU/TCEs): todo **achado de auditoria** compõe-se de quatro elementos indissociáveis: (1) **Condição**: o que é (a realidade fática constatada); (2) **Critério**: o que deveria ser (a norma legal, técnica ou boa prática); (3) **Causa**: por que ocorreu (a falha estrutural, omissão ou deficiência); (4) **Efeito**: qual a consequência (o dano patrimonial, social ou ineficiência gerada).
> - **C)** Incorreta. A recomendação tem caráter propositivo e orientativo para aperfeiçoar a gestão; não é ordem coativa punível com prisão.
> - **D)** Incorreta. A **determinação** tem caráter cogente e impositivo, determinando a correção de ilegalidade sob pena de multa e responsabilização funcional do gestor.
> - **E)** Incorreta. O efeito abrange tanto impactos financeiros quanto sociais, qualitativos, ambientais e institucionais.
>
> **Gabarito: B**"""

# Inserções no arquivo 03 de trás para frente
pos_q05 = t03.find("### Questão 05")
assert pos_q05 != -1
pos_fontes = t03.find("## 🌐 Fontes", pos_q05)
assert pos_fontes != -1
t03 = t03[:pos_fontes] + "\n\n" + q11_03.strip() + "\n\n---\n\n" + t03[pos_fontes:]

ancora_4 = "### 4. Evidências de Auditoria: Os Três Pilares da Validade"
pos_4 = t03.find(ancora_4)
pos_5 = t03.find("### 5. A Estrutura Anatômica do Achado de Auditoria", pos_4)
assert pos_4 != -1 and pos_5 != -1
t03 = t03[:pos_5] + "\n\n" + q10_03.strip() + "\n\n---\n\n" + t03[pos_5:]

pos_q03 = t03.find("### Questão 03")
assert pos_q03 != -1
pos_end_q03 = t03.find("\n\n---\n\n", pos_q03)
assert pos_end_q03 != -1
t03 = t03[:pos_end_q03 + 7] + "\n\n" + q09_03.strip() + "\n\n---\n\n" + t03[pos_end_q03 + 7:]
t03 = t03[:pos_q03] + "\n\n" + q08_03.strip() + "\n\n---\n\n" + t03[pos_q03:]

pos_q02 = t03.find("### Questão 02")
assert pos_q02 != -1
pos_end_q02 = t03.find("\n\n---\n\n", pos_q02)
assert pos_end_q02 != -1
t03 = t03[:pos_end_q02 + 7] + "\n\n" + q07_03.strip() + "\n\n---\n\n" + t03[pos_end_q02 + 7:]

pos_q01 = t03.find("### Questão 01")
assert pos_q01 != -1
t03 = t03[:pos_q01] + "\n\n" + q06_03.strip() + "\n\n---\n\n" + t03[pos_q01:]

qs_03 = re.findall(r"### Questão (\d+)", t03)
print("Questões no arquivo 03 do Módulo 18:", qs_03)
assert len(qs_03) == 11
assert sorted(qs_03) == ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']

with open(f03_path, "w", encoding="utf-8") as f:
    f.write(t03)

print("Arquivo 03 do Módulo 18 gravado com sucesso! Total: 11 questões.")
