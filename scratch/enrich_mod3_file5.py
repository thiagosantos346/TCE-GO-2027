import os, re

FILE = r"fontes_de_estudo/conhecimentos_gerais/03_legislacao_institucional/05_codigo_de_etica_servidores_tce_go.md"

q06_text = """
### Questão 06
**(FCC – Inédita – Padrão TCE-GO)**  
O Código de Ética dos Servidores do TCE-GO orienta-se pelos padrões éticos internacionais consolidados na norma ISSAI 130 da Organização Internacional das Instituições Superiores de Controle (INTOSAI). Entre os valores axiais que norteiam a integridade do auditor governamental, destaca-se:

* **A)** A flexibilidade moral nas auditorias operacionais, autorizando o auditor a transigir com irregularidades formais em favor de interesses corporativos.
* **B)** A independência profissional e a objetividade, que impõem ao auditor manter-se livre de quaisquer influências políticas, econômicas ou pessoais capazes de comprometer a imparcialidade técnica de seus relatórios e pareceres.
* **C)** O dever de subordinação hierárquica cega, segundo o qual o auditor deve omitir achados de fiscalização se assim for verbalmente orientado pela chefia imediata.
* **D)** A faculdade de prestar consultoria remunerada aos órgãos jurisdicionados com a finalidade de aumentar a eficiência fiscalizatória do Estado.
* **E)** O privilégio de divulgar privativamente conclusões de relatórios sigilosos a agentes do mercado financeiro antes da deliberação colegiada.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A conduta ética do auditor é pautada pela intransigência ética com a legalidade e moralidade republicana, sem concessões a conveniências corporativas.
> - **B)** Correta. A ISSAI 130 e o Código de Ética do TCE-GO elegem a **independência, integridade e objetividade** como pilares fundantes da fiscalização pública: o auditor deve agir com neutralidade axiológica absoluta, sem se deixar influenciar por pressões de partidos, gestores fiscalizados, laços familiares ou vantagens pessoais.
> - **C)** Incorreta. A hierarquia administrativa não convalida ordens manifestamente ilegais ou antiéticas; o dever de integridade profissional impõe a fidedignidade nos relatórios técnicos.
> - **D)** Incorreta. O exercício de consultoria ou assessoria a órgãos e entidades sujeitas à jurisdição do TCE-GO constitui conflito de interesses e infração ética gravíssima expressamente vedada.
> - **E)** Incorreta. O vazamento de informações sigilosas ou privilegiadas atenta frontalmente contra a deontologia e constitui ilícito administrativo e penal.
>
> **Gabarito: B**
"""

q07_text = """
### Questão 07
**(FCC – Inédita – Padrão TCE-GO)**  
Nos termos do Código de Ética dos Servidores do TCE-GO, quanto aos deveres funcionais e à postura profissional do servidor:

* **A)** É facultado ao auditor tratar com rispidez cidadãos e gestores fiscalizados para assegurar a autoridade do cargo e a imposição da fiscalização.
* **B)** O servidor deve desempenhar suas funções com zelo, celeridade e assiduidade, pautando suas relações interpessoais pela urbanidade, respeito e consideração mútua tanto perante os jurisdicionados quanto perante seus colegas de trabalho.
* **C)** A produtividade técnica do servidor isenta-o de observar a pontualidade e o decoro no ambiente físico e virtual de trabalho.
* **D)** O servidor pode priorizar a instrução de processos de interesse de conhecidos ou amigos íntimos, desde que não receba remuneração extra.
* **E)** É lícito ao servidor negar atendimento ao público externo fora dos dias designados para sessões plenárias.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A urbanidade e o respeito à dignidade humana dos fiscalizados e do cidadão são deveres éticos inafastáveis. O rigor técnico não se confunde com grosseria ou truculência.
> - **B)** Correta. O Código de Ética estatui como deveres primordiais do servidor a assiduidade, presteza, zelo técnico e a urbanidade exemplar nas relações de serviço e no trato com o público e colegas de trabalho.
> - **C)** Incorreta. A conduta ética exige a observância integral dos deveres funcionais, inclusive pontualidade e decoro profissional.
> - **D)** Incorreta. Quebra manifesta da impessoalidade e isonomia processual (favorecimento antiético).
> - **E)** Incorreta. A prestação de serviços e a presteza ao público são contínuas no horário de funcionamento regulamentar da Corte.
>
> **Gabarito: B**
"""

q08_text = """
### Questão 08
**(FCC – Inédita – Padrão TCE-GO)**  
Sobre o dever de sigilo profissional e a custódia de dados confidenciais regulados no Código de Ética do TCE-GO:

* **A)** O servidor está autorizado a repassar dados de auditorias em andamento a familiares próximos, desde que advertidos sobre a reserva do assunto.
* **B)** O dever de sigilo cessa imediatamente após o término do vínculo funcional do servidor com o Tribunal de Contas, desobrigando servidores aposentados ou exonerados.
* **C)** O servidor do TCE-GO tem o dever incondicional de guardar reserva e absoluto sigilo sobre dados, fatos e informações obtidos em razão do exercício de suas atribuições que não sejam de domínio público, sendo terminantemente vedado o uso de informação privilegiada para obter vantagem indevida para si ou para outrem.
* **D)** A divulgação de minutas de acórdãos em redes sociais é permitida quando o objetivo for testar a repercussão pública das propostas de voto.
* **E)** O sigilo de auditoria não se aplica a contratos de obras públicas de grande vulto financeiro.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O sigilo vincula o servidor em face de qualquer terceiro estranho à equipe de fiscalização formal, inclusive familiares.
> - **B)** Incorreta. O dever de sigilo e discrição sobre dados confidenciais obtidos no exercício do cargo **subsiste mesmo após a cessação do vínculo** efetivo ou comissionado (aposentadoria, exoneração ou término de mandato).
> - **C)** Correta. Trata-se do comando deontológico de salvaguarda das informações sigilosas e privilegiadas: o servidor é guardião da confidencialidade dos dados que acessa no cumprimento do dever legal, sendo rigorosamente proibido explorá-los em benefício próprio ou de terceiros (o que configura infração ética e crime funcional).
> - **D)** Incorreta. Minutas de decisão e relatórios em elaboração são peças internas sigilosas; sua exposição pública atenta contra a ética pública e o devido processo legal.
> - **E)** Incorreta. O dever de reserva processual abrange todos os processos e auditorias até a sua regular publicidade institucional deliberativa.
>
> **Gabarito: C**
"""

q09_text = """
### Questão 09
**(FCC – Inédita – Padrão TCE-GO)**  
No que concerne às proibições éticas e conduta pública do servidor do TCE-GO nas redes sociais e no ambiente profissional:

* **A)** É expressamente vedado ao servidor manifestar-se publicamente em redes sociais como porta-voz do Tribunal sem a devida autorização institucional, bem como emitir juízos depreciativos sobre processos e fiscalizações que estejam pendentes de deliberação pela Corte.
* **B)** O servidor pode utilizar livremente os canais oficiais do Tribunal para defender interesses político-partidários pessoais e promover candidaturas eleitorais de parentes.
* **C)** É lícito ao servidor atuar como procurador ou consultor de empresa que dispute licitação fiscalizada pela sua própria unidade técnica.
* **D)** O Código de Ética autoriza que o auditor receba presentes de alto valor de dirigentes de empreiteiras auditadas, desde que divididos com os colegas de equipe.
* **E)** As vedações éticas sobre conflito de interesses aplicam-se unicamente no horário de expediente presencial nas dependências físicas do Tribunal.

> **Comentário Detalhado:**
>
> - **A)** Correta. O Código de Ética do TCE-GO veda expressamente o uso das redes sociais particulares para emissão de manifestações com aparente chancela institucional sem prévia autorização, bem como comentários públicos que antecipem juízos de valor ou depreciem processos e partes sujeitas à fiscalização da Corte de Contas antes de sua formal conclusão pelo colegiado.
> - **B)** Incorreta. O uso de bens, recursos ou canais públicos para propaganda político-partidária atenta contra o art. 37 da CF/88 e constitui infração ética gravíssima e improbidade administrativa.
> - **C)** Incorreta. A advocacia ou consultoria perante o Tribunal ou em favor de fiscalizados é vedada de forma absoluta.
> - **D)** Incorreta. A política institucional proíbe terminantemente o recebimento de presentes e vantagens de pessoas físicas ou jurídicas fiscalizadas ou interessadas em decisões da Corte (apenas brindes sem valor comercial e com logotipo institucional de praxe são admitidos).
> - **E)** Incorreta. Os padrões de integridade e a vedação ao conflito de interesses estendem-se a toda a conduta pública do agente, dentro e fora do horário de expediente.
>
> **Gabarito: A**
"""

q10_text = """
### Questão 10
**(FCC – Inédita – Padrão TCE-GO)**  
Sobre as competências da Comissão de Ética do Tribunal de Contas do Estado de Goiás e o rito do processo ético:

* **A)** A Comissão de Ética pode aplicar diretamente aos servidores as penalidades estatutárias de demissão e cassação de aposentadoria.
* **B)** A única sanção de competência sancionatória direta da Comissão de Ética é a pena de **Censura Ética**, devendo a Comissão, quando constatar indícios de falta disciplinar de maior gravidade, remeter cópia integral dos autos à Corregedoria-Geral para instauração de processo disciplinar competente.
* **C)** O processo perante a Comissão de Ética não admite a apresentação de defesa prévia pelo investigado, vigendo a presunção absoluta de veracidade da denúncia.
* **D)** A Comissão de Ética é composta exclusivamente por magistrados de carreira requisitados do Poder Judiciário.
* **E)** As deliberações da Comissão de Ética têm natureza puramente punitiva e repressiva, sendo vedada qualquer atuação preventiva ou pedagógica.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. As penas de demissão e cassação de aposentadoria são privativas da autoridade competente (Presidente do Tribunal) após regular Processo Administrativo Disciplinar (PAD) instaurado sob a égide da Lei nº 20.756/2020.
> - **B)** Correta. A sanção máxima e privativa prevista no âmbito deontológico da Comissão de Ética do TCE-GO é a **Censura Ética** (fundada na reprovação moral e funcional). Quando a infração ultrapassar o plano meramente deontológico e caracterizar potencial infração estatutária punível com advertência, suspensão ou demissão, a Comissão remete o processo à Corregedoria-Geral para as providências disciplinares e apuração em PAD.
> - **C)** Incorreta. O processo ético assegura rigorosamente o contraditório e a ampla defesa, facultando-se manifestação prévia e juntada de documentos pelo denunciado.
> - **D)** Incorreta. A Comissão de Ética é integrada por membros e servidores do próprio quadro do TCE-GO, designados pelo Presidente.
> - **E)** Incorreta. A Comissão tem papel preponderantemente preventivo, consultivo e pedagógico na disseminação da cultura de integridade pública.
>
> **Gabarito: B**
"""

def enrich_mod3_file5():
    with open(FILE, "r", encoding="utf-8") as f:
        text = f.read()

    # Inserção da Questão 06: no fim da Seção 1 (antes de "## 2. Deveres Éticos e Postura Funcional do Servidor do TCE-GO")
    sec2 = "## 2. Deveres Éticos e Postura Funcional do Servidor do TCE-GO"
    idx2 = text.find(sec2)
    dash_idx = text.rfind("---", 0, idx2)
    text = text[:dash_idx] + q06_text + "\n---\n\n" + text[dash_idx:]

    # Inserção da Questão 07: na Seção 2.2 (antes de "### 2.3 Dever Incondicional de Sigilo")
    sec23 = "### 2.3 Dever Incondicional de Sigilo, Custódia de Dados e Vedação a Informações Privilegiadas"
    idx23 = text.find(sec23)
    dash_idx = text.rfind("---", 0, idx23)
    text = text[:dash_idx] + q07_text + "\n---\n\n" + text[dash_idx:]

    # Inserção da Questão 08: no fim da Seção 2 (antes de "## 3. Proibições Éticas, Vedações e Conflito de Interesses")
    sec3 = "## 3. Proibições Éticas, Vedações e Conflito de Interesses"
    idx3 = text.find(sec3)
    dash_idx = text.rfind("---", 0, idx3)
    text = text[:dash_idx] + q08_text + "\n---\n\n" + text[dash_idx:]

    # Inserção da Questão 09: no fim da Seção 3 (antes de "## 4. A Comissão de Ética do TCE-GO e o Processo Ético")
    # Nota: Seção 3 já contém Questão 01, 02 e 03. Vamos inserir Questão 09 no fim da Seção 3
    sec4 = "## 4. A Comissão de Ética do TCE-GO e o Processo Ético"
    idx4 = text.find(sec4)
    dash_idx = text.rfind("---", 0, idx4)
    text = text[:dash_idx] + q09_text + "\n---\n\n" + text[dash_idx:]

    # Inserção da Questão 10: no fim da Seção 4 (antes de "## 5. Fontes Oficiais e Referências Bibliográficas")
    sec_fontes = "## 5. Fontes Oficiais e Referências Bibliográficas"
    idxf = text.find(sec_fontes)
    dash_idx = text.rfind("---", 0, idxf)
    text = text[:dash_idx] + q10_text + "\n---\n\n" + text[dash_idx:]

    with open(FILE, "w", encoding="utf-8") as f:
        f.write(text)

    print("Module 03 File 05 enriquecido com sucesso.")

enrich_mod3_file5()
