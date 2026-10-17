import os, re

FILE = r"fontes_de_estudo/conhecimentos_gerais/03_legislacao_institucional/02_lei_organica_tce_go_lei_16168_2007.md"

q06_text = """
### Questão 06
**(FCC – Inédita – Padrão TCE-GO)**  
De acordo com as disposições da Lei Orgânica do Tribunal de Contas do Estado de Goiás (Lei Estadual nº 16.168/2007, arts. 1º a 4º), estão sujeitos à jurisdição do TCE-GO:

* **A)** Exclusivamente os chefes dos Poderes Executivo, Legislativo e Judiciário, excluindo-se servidores subordinados e dirigentes de entidades privadas.
* **B)** Qualquer pessoa física ou jurídica, pública ou privada, que utilize, arrecade, guarde, gerencie ou administre dinheiros, bens e valores públicos estaduais ou pelos quais o Estado responda, bem como aqueles que derem causa a perda, extravio ou outra irregularidade de que resulte dano ao erário.
* **C)** Apenas os agentes que praticarem atos com dolo comprovado, ficando as condutas culposas isentas da jurisdição fiscalizatória da Corte de Contas.
* **D)** As empresas públicas e sociedades de economia mista apenas no que tange às suas atividades-meio de contratação de pessoal temporário.
* **E)** Exclusivamente os órgãos da administração direta estadual, excluídas as fundações e autarquias dotadas de personalidade jurídica própria.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A jurisdição do TCE-GO alcança todos os ordenadores de despesas e administradores públicos em qualquer nível funcional, além de particulares que causem dano aos cofres públicos.
> - **B)** Correta. Reproduz com precisão o comando do art. 2º da Lei Orgânica do TCE-GO (Lei nº 16.168/2007), que espelha o art. 70, parágrafo único, da CF/88 e art. 26 da CE/GO: a sujeição à jurisdição da Corte abrange todas as pessoas físicas e jurídicas (públicas ou privadas) gestoras de recursos estaduais ou que causem prejuízo patrimonial ao Estado de Goiás.
> - **C)** Incorreta. A responsabilidade perante o Tribunal de Contas alcança atos omissivos ou comissivos praticados tanto com dolo quanto com culpa estrita (negligência, imprudência ou imperícia).
> - **D) e E)** Incorretas. Toda a administração indireta estadual (autarquias, fundações, empresas públicas e sociedades de economia mista) submete-se integralmente à fiscalização contábil, financeira, orçamentária, operacional e patrimonial do TCE-GO.
>
> **Gabarito: B**
"""

q07_text = """
### Questão 07
**(FCC – Inédita – Padrão TCE-GO)**  
A Lei Orgânica do TCE-GO (Lei nº 16.168/2007, arts. 5º a 10) tipifica os instrumentos operacionais de fiscalização a serem utilizados pelo Tribunal. Considere as seguintes definições:  

1. *Instrumento destinado a verificar a legalidade e a legitimidade dos atos e fatos administrativos em andamento ou já praticados, bem como coligir dados preliminares ou esclarecer dúvidas decorrentes de denúncia ou representação.*  
2. *Instrumento utilizado para verificar a eficácia, eficiência e economicidade da gestão, mediante exame aprofundado dos sistemas de gestão e das operações financeiras e patrimoniais do órgão.*  
3. *Instrumento voltado a verificar o cumprimento de deliberações do Tribunal e os resultados das recomendações e determinações expedidas em processos anteriores.*  

Os instrumentos operacionais descritos em 1, 2 e 3 correspondem, respectivamente, a:

* **A)** Levantamento – Auditoria – Acompanhamento
* **B)** Inspeção – Auditoria – Monitoramento
* **C)** Auditoria – Levantamento – Monitoramento
* **D)** Inspeção – Levantamento – Acompanhamento
* **E)** Monitoramento – Inspeção – Auditoria

> **Comentário Detalhado:**
>
> - **Item 1:** A **Inspeção** é o instrumento de fiscalização pontual e emergencial utilizado pelo TCE-GO para suprir omissões, esclarecer fatos duvidosos, apurar denúncias/representações ou periciar atos e contratos específicos (art. 7º da Lei 16.168/2007).
> - **Item 2:** A **Auditoria** é o instrumento estruturado e programado de controle pelo qual o Tribunal avalia a conformidade, economicidade, eficiência e efetividade de órgãos e programas governamentais (art. 8º da Lei 16.168/2007).
> - **Item 3:** O **Monitoramento** é o instrumento fiscalizatório destinado especificamente a verificar o cumprimento de determinações, acórdãos e recomendações emanados pelo TCE-GO e avaliar seus impactos práticos (art. 10 da Lei 16.168/2007).
> - **Conclusão:** A sequência exata é *Inspeção – Auditoria – Monitoramento* (Alternativa B).
>
> **Gabarito: B**
"""

q08_text = """
### Questão 08
**(FCC – Inédita – Padrão TCE-GO)**  
Quanto ao poder cautelar e sancionatório do Tribunal de Contas do Estado de Goiás previsto na Lei Estadual nº 16.168/2007 (arts. 41 a 47):

* **A)** O TCE-GO não possui competência para adotar medidas cautelares sem prévia autorização judicial expedida pelo Tribunal de Justiça do Estado de Goiás.
* **B)** Havendo fundado receio de dano irreparável ou de grave lesão ao erário, o Tribunal ou o Relator pode, cautelarmente, determinar o afastamento temporário do responsável e a indisponibilidade de seus bens por prazo determinado.
* **C)** A declaração de inidoneidade para participar de licitações com a administração pública estadual não pode ser aplicada pelo TCE-GO, sendo ato privativo do Governador do Estado.
* **D)** As multas pecuniárias aplicadas pelo TCE-GO têm natureza meramente administrativa e dependem de processo judicial de conhecimento prévio para adquirirem força de cobrança.
* **E)** A inabilitação para o exercício de cargo em comissão ou função de confiança no âmbito da administração estadual pode ser decretada pelo prazo perpétuo nos casos de dolo comprovado.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O poder geral de cautela dos Tribunais de Contas decorre diretamente de sua competência constitucional implícita e de autorização legal expressa (art. 41 da Lei 16.168/2007 e jurisprudência vinculante do STF - MS 24.510).
> - **B)** Correta. De acordo com o art. 41 e 42 da Lei Orgânica do TCE-GO, verificada a presença do *fumus boni iuris* e do *periculum in mora*, o Tribunal ou o Relator poderá decretar medidas cautelares, inclusive a suspensão de atos/contratos, o afastamento preventivo de gestor que esteja embaraçando a fiscalização e a indisponibilidade cautelar de bens do responsável suficientes para garantir o ressarcimento do erário.
> - **C)** Incorreta. O art. 45 da Lei Orgânica confere ao TCE-GO competência expressa para declarar a inidoneidade de licitante fraudador por prazo de até 5 anos.
> - **D)** Incorreta. Conforme o art. 71, § 3º, da CF/88 e art. 46 da Lei 16.168/2007, o acórdão condenatório que imputa débito ou multa tem **eficácia de título executivo extrajudicial**.
> - **E)** Incorreta. A inabilitação para cargo em comissão tem prazo máximo de até 5 a 8 anos (conforme o caso na lei), sendo vedada a pena de caráter perpétuo pela Constituição Federal (art. 5º, XLVII, "b").
>
> **Gabarito: B**
"""

q09_text = """
### Questão 09
**(FCC – Inédita – Padrão TCE-GO)**  
Sobre o sistema recursal disciplinado nos artigos 54 a 65 da Lei Orgânica do TCE-GO (Lei nº 16.168/2007), assinale a afirmativa correta:

* **A)** O Pedido de Reconsideração é cabível em face de qualquer acórdão proferido pelo Tribunal Pleno em grau originário de recurso.
* **B)** O Recurso de Reexame é a modalidade recursal cabível contra decisões definitivas ou terminativas proferidas em processos de prestação ou tomada de contas, possuindo efeito suspensivo.
* **C)** Os Embargos de Declaração podem ser opostos no prazo improrrogável de 30 dias contados da publicação do acórdão impugnado.
* **D)** O Pedido de Rescisão (ou Revisão) constitui recurso ordinário com efeito suspensivo automático que impede a execução da decisão condenatória.
* **E)** Das decisões proferidas pelo Tribunal Pleno não cabe qualquer espécie de recurso, operando-se preclusão imediata.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O Pedido de Reconsideração destina-se a impugnar decisões terminativas ou definitivas de processos de fiscalização (não de contas ordinárias), e não cabe contra decisões que já apreciaram recurso anterior.
> - **B)** Correta. Conforme os arts. 55 e 56 da Lei Orgânica do TCE-GO, o **Recurso de Reexame** é o instrumento recursal próprio para atacar decisões proferidas em processos de tomada ou prestação de contas, dotado de efeito devolutivo e suspensivo, admitindo reexame integral da matéria fática e de direito pelo Tribunal Pleno.
> - **C)** Incorreta. O prazo regimental para a oposição de Embargos de Declaração no TCE-GO é de **5 dias** (art. 60 da Lei Orgânica), e não 30 dias.
> - **D)** Incorreta. O Pedido de Revisão é uma ação de impugnação autônoma (análoga à ação rescisória civil), fundada em fatos novos ou documentos falsos supervenientes, e não possui efeito suspensivo automático.
> - **E)** Incorreta. Das decisões originárias do Pleno cabem recursos expressamente previstos em lei, tais como embargos de declaração, recurso de reexame e pedido de revisão.
>
> **Gabarito: B**
"""

q10_text = """
### Questão 10
**(FCC – Inédita – Padrão TCE-GO)**  
Em conformidade com a jurisprudência do Supremo Tribunal Federal (Tema 899 de Repercussão Geral - RE 636.886) e as normas de controle externo do TCE-GO acerca da prescrição:

* **A)** As ações de ressarcimento ao erário fundadas em decisões dos Tribunais de Contas são imprescritíveis em qualquer hipótese, nos termos literais do artigo 37, § 5º, da CF/88.
* **B)** É prescritível a pretensão de ressarcimento ao erário fundada em decisão de Tribunal de Contas, aplicando-se o prazo prescricional de 5 anos para a cobrança judicial do título executivo, sem prejuízo da incidência da prescrição intercorrente no curso do processo administrativo de controle externo.
* **C)** A prescrição da pretensão punitiva do Tribunal de Contas ocorre no prazo decadencial de 20 anos previsto no Código Civil.
* **D)** A citação válida do responsável no processo de tomada de contas especial não interrompe o curso do prazo prescricional.
* **E)** O TCE-GO não pode reconhecer a prescrição de ofício, dependendo sempre de provocação expressa da defesa técnica do gestor.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A tese fixada pelo STF no Tema 899 é categórica: *"É prescritível a pretensão de ressarcimento ao erário fundada em decisão de Tribunal de Contas"*. A imprescritibilidade do art. 37, § 5º, restringe-se às ações de improbidade com dolo comprovado ajuizadas perante o Poder Judiciário (Tema 897).
> - **B)** Correta. As pretensões punitiva (multas) e ressarcitória (débitos) no âmbito do Tribunal de Contas submetem-se ao prazo prescricional geral de **5 anos** (Lei 9.873/1999 e regulamentação do TCE-GO), além da prescrição intercorrente de **3 anos** caso o processo permaneça paralisado injustificadamente em instrução.
> - **C)** Incorreta. Não se aplica o prazo vintenário do Código Civil, mas a disciplina de direito público quinquenal (5 anos).
> - **D)** Incorreta. A citação válida ou notificação inicial do responsável é causa clássica de interrupção do prazo prescricional.
> - **E)** Incorreta. Tratando-se de matéria de ordem pública, a prescrição pode e deve ser reconhecida de ofício pelo relator ou pelo colegiado deliberativo da Corte.
>
> **Gabarito: B**
"""

def enrich_mod3_file2():
    with open(FILE, "r", encoding="utf-8") as f:
        text = f.read()

    # Inserção da Questão 06: no fim da Seção 1 (antes de "## 2. Instrumentos de Fiscalização Externa")
    sec2 = "## 2. Instrumentos de Fiscalização Externa (Arts. 5º a 10)"
    idx2 = text.find(sec2)
    dash_idx = text.rfind("---", 0, idx2)
    text = text[:dash_idx] + q06_text + "\n---\n\n" + text[dash_idx:]

    # Inserção da Questão 07: no fim da Seção 2 (antes de "## 3. Julgamento de Contas e Tomada de Contas Especial")
    sec3 = "## 3. Julgamento de Contas e Tomada de Contas Especial (Arts. 11 a 28)"
    idx3 = text.find(sec3)
    dash_idx = text.rfind("---", 0, idx3)
    text = text[:dash_idx] + q07_text + "\n---\n\n" + text[dash_idx:]

    # Inserção da Questão 08: no fim da Seção 4 (antes de "## 5. Processo, Prazos e Sistema Recursal")
    sec5 = "## 5. Processo, Prazos e Sistema Recursal da Lei Orgânica (Arts. 50 a 65)"
    idx5 = text.find(sec5)
    dash_idx = text.rfind("---", 0, idx5)
    text = text[:dash_idx] + q08_text + "\n---\n\n" + text[dash_idx:]

    # Inserção da Questão 09: na Seção 5.2 (antes de "### 5.3 Regime da Prescrição Punitiva e Ressarcitória")
    # Nota: Seção 5 já tem Questão 04 e Questão 05. Vamos inserir Questão 09 antes da Seção 5.3
    sec53 = "### 5.3 Regime da Prescrição Punitiva e Ressarcitória no TCE-GO"
    idx53 = text.find(sec53)
    dash_idx = text.rfind("---", 0, idx53)
    text = text[:dash_idx] + q09_text + "\n---\n\n" + text[dash_idx:]

    # Inserção da Questão 10: no fim da Seção 5 (antes de "## 6. Fontes Oficiais e Referências Bibliográficas")
    sec_fontes = "## 6. Fontes Oficiais e Referências Bibliográficas"
    idxf = text.find(sec_fontes)
    dash_idx = text.rfind("---", 0, idxf)
    text = text[:dash_idx] + q10_text + "\n---\n\n" + text[dash_idx:]

    with open(FILE, "w", encoding="utf-8") as f:
        f.write(text)

    print("Module 03 File 02 enriquecido com sucesso.")

enrich_mod3_file2()
