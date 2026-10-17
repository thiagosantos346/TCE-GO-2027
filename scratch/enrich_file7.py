import os, re

FILE_7 = r"fontes_de_estudo/conhecimentos_gerais/01_lingua_portuguesa/07_redacao_oficial.md"

q06_text = """
### Questão 06
**(FCC – TCE-GO – Analista de Controle Externo)**  
Segundo as diretrizes consagradas pelo Manual de Redação da Presidência da República (3ª edição) e pelo ordenamento constitucional vigente (art. 37 da CF/88):

* **A)** A redação oficial admite a inserção de impressões pessoais e juízos subjetivos do redator, desde que justificados pelo interesse público primário.
* **B)** A impessoalidade da redação oficial desdobra-se em tríplice dimensão: impessoalidade do emissor (é o serviço público quem se manifesta, e não o servidor individualmente), impessoalidade do destinatário (o texto destina-se ao cidadão ou a outro órgão com tratamento uniforme e isonômico) e impessoalidade do assunto (trata-se estritamente do interesse público, sem paixões político-partidárias).
* **C)** O Decreto Federal nº 9.758/2019 instituiu o uso obrigatório dos pronomes *Vossa Excelência* e *Ilustríssimo* em toda e qualquer comunicação direta com os cidadãos comuns.
* **D)** A publicidade dos atos administrativos autoriza a utilização de gírias e jargões regionais nos expedientes oficiais visando aproximar o Estado das massas populares.
* **E)** O princípio da eficiência desobriga os órgãos de controle externo de observar o padrão culto da língua portuguesa na elaboração de seus relatórios.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A redação oficial é rigorosamente impessoal e técnica; impressões ou opiniões subjetivas de foro íntimo do servidor são terminantemente vedadas pelo MRPR.
> - **B)** Correta. O MRPR (3ª Ed., Cap. 1) explicita com precisão lapidar a tríplice acepção do princípio da impessoalidade na comunicação oficial: 1) Da posição de quem emite a comunicação (o Estado/Administração); 2) Do destinatário que a recebe (isonomia e uniformidade republicana); 3) Do assunto tratado (estrito interesse público, exposto de modo objetivo e isento).
> - **C)** Incorreta. O Decreto nº 9.758/2019 extinguiu expressamente o uso de fórmulas laudatórias (*Digníssimo*, *Ilustríssimo*) e padronizou o tratamento geral no âmbito federal como *senhor* ou *senhora*.
> - **D) e E)** Incorretas. O padrão culto da língua e a formalidade são atributos inegociáveis impostos pela Constituição e pelo MRPR para garantir a inteligibilidade e solenidade dos atos estatais.
>
> **Gabarito: B**
"""

q07_text = """
### Questão 07
**(FCC – TRT-23 – Analista Judiciário)**  
Quanto à diagramação, tipografia e padrão gráfico dos expedientes oficiais prescritos na 3ª edição do Manual de Redação da Presidência da República:

* **A)** É livre o emprego de qualquer fonte tipográfica decorativa no corpo do ofício, a critério discricionário do redator do documento.
* **B)** O MRPR padronizou o uso obrigatório das fontes tipográficas *Calibri* ou *Carlito*, corpo 12 pontos no texto principal, com espaçamento simples entre linhas e parágrafos numerados sequencialmente a partir do segundo parágrafo.
* **C)** O recuo de parágrafo deve ser de 5 centímetros a partir da margem esquerda da página.
* **D)** A datação do expediente deve constar de forma centralizada e sem a indicação do local de emissão.
* **E)** As margens do documento oficial são livres, permitindo-se a impressão rente às bordas da folha de papel.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O MRPR veda fontes decorativas ou estilizadas para preservar a padronização e a sobriedade dos atos públicos.
> - **B)** Correta. A 3ª Edição do MRPR (Item 2.2) padronizou expressamente as famílias tipográficas *Calibri* ou *Carlito* (software livre equivalente): corpo 12 pt no texto em geral, 10 pt em citações longas e notas de rodapé, espaçamento entrelinhas simples e parágrafos numerados em algarismos arábicos a partir do segundo parágrafo (o 1º e o fecho não se numeram).
> - **C)** Incorreta. O recuo padrão de início de parágrafo na margem esquerda é de **2,5 cm** (e não 5 cm).
> - **D)** Incorreta. A datação é alinhada à direita e inicia-se obrigatoriamente pelo local de expedição seguido de vírgula (*Goiânia, 15 de março de 2026*).
> - **E)** Incorreta. As margens são estritamente padronizadas: esquerda e superior de 3 cm; direita e inferior de 1,5 cm.
>
> **Gabarito: B**
"""

q08_text = """
### Questão 08
**(FCC – DPE-RS – Analista Processual)**  
Considere as seguintes afirmações sobre a assinatura e os fechos nos expedientes oficiais segundo o Manual de Redação da Presidência da República:  

I. *O MRPR estabelece um sistema binário de fechos: "Respeitosamente", para autoridades de hierarquia superior à do signatário (inclusive o Presidente da República); e "Atenciosamente", para autoridades de mesma hierarquia, de hierarquia inferior ou para particulares.*  
II. *A identificação do signatário deve ser precedida de um traço ou linha horizontal de assinatura de 5 centímetros para orientar a firma.*  
III. *Na identificação do signatário, constam centralizados o nome do signatário em letras maiúsculas e, na linha imediatamente inferior, o cargo que ocupa, sem linha de assinatura.*  

Está correto o que se afirma em:

* **A)** I, apenas.
* **B)** I e III, apenas.
* **C)** II, apenas.
* **D)** II e III, apenas.
* **E)** I, II e III.

> **Comentário Detalhado:**
>
> - **Item I:** Correto. A 3ª Edição do MRPR consagrou expressamente a simplificação binária dos fechos regulamentares: apenas dois fechos são admitidos em toda a correspondência oficial da administração pública:  
>   - **Respeitosamente:** para autoridades superiores à do remetente (inclusive chefes de Poder);  
>   - **Atenciosamente:** para autoridades de mesma hierarquia, hierarquia inferior ou para o público em geral.
> - **Item II:** Incorreto. O MRPR veda expressamente o antigo uso de traço ou linha sublinhada sobre o qual se assinava (*"não deve haver linha de assinatura"*).
> - **Item III:** Correto. Abaixo do fecho, reserva-se espaço para a assinatura (manual ou digital certificada) e, logo abaixo, sem qualquer traço, constam o nome da autoridade signatária (em maiúsculas) e o cargo em caixa-baixa.
> - **Conclusão:** Estão corretos os itens I e III.
>
> **Gabarito: B**
"""

q09_text = """
### Questão 09
**(FCC – TRT-14 – Analista Judiciário)**  
Acerca do correio eletrônico institucional (*e-mail*) no âmbito da administração pública, de acordo com o Manual de Redação da Presidência da República:

* **A)** Por constituir comunicação informal e dinâmica, dispensa o cumprimento do padrão culto da língua e dos parâmetros de clareza e impessoalidade.
* **B)** O campo "Assunto" deve ser preenchido de modo pontual e claro, permitindo ao destinatário identificar de imediato o tema e o teor da comunicação sem necessidade de abrir a mensagem.
* **C)** O envio de mensagens eletrônicas institucionais com cópia oculta (Cco) para superiores hierárquicos é prática recomendada pelo MRPR para fiscalização sigilosa.
* **D)** O e-mail público não possui validade legal ou administrativa para fins de instrução processual ou transmissão de documentos públicos.
* **E)** Recomenda-se a inserção de imagens emotivas, frases religiosas ou pensamentos filosóficos pessoais na assinatura institucional automática de e-mail do servidor.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O e-mail institucional é um documento oficial público e deve observar rigorosamente a norma culta, a impessoalidade e a formalidade.
> - **B)** Correta. O MRPR (Item 3.2) instrui que o campo "Assunto" (*Subject*) deve ser redigido com clareza e precisão para orientar o destinatário sobre o exato conteúdo da demanda antes mesmo da abertura do corpo do texto.
> - **C)** Incorreta. O uso de cópia oculta (*blind carbon copy*) em comunicações oficiais rotineiras é desestimulado por atentar contra o princípio da transparência e da lealdade administrativa.
> - **D)** Incorreta. O correio eletrônico institucional tem pleno valor documental e probatório, inclusive respaldado pelas normas de processo eletrônico.
> - **E)** Incorreta. Mensagens religiosas, frases de efeito e imagens particulares violam o princípio da laicidade, da sobriedade e da impessoalidade da comunicação pública.
>
> **Gabarito: B**
"""

q10_text = """
### Questão 10
**(FCC – TCE-PI – Auditor de Controle Externo)**  
Considere as seguintes definições sobre espécies documentais da administração pública:  

1. *Documento formal emitido pelos Tribunais de Contas com caráter terminativo ou resolutivo, consubstanciando a decisão colegiada definitiva sobre a regularidade ou irregularidade das contas de um gestor.*  
2. *Documento expedido por ministros de Estado ou secretários com o objetivo de submeter ao chefe do Poder Executivo a proposta de um ato normativo ou projeto de lei.*  
3. *Instrumento de comunicação formal utilizado entre os chefes dos Poderes da República, como no envio de mensagens de prestação de contas governamentais ao Poder Legislativo.*  

As espécies documentais descritas em 1, 2 e 3 correspondem, respectivamente, a:

* **A)** Parecer Técnico – Ofício Circular – Despacho Governamental
* **B)** Acórdão – Exposição de Motivos – Mensagem
* **C)** Resolução – Relatório de Auditoria – Edital
* **D)** Acórdão – Parecer Jurídico – Memorando
* **E)** Nota Técnica – Exposição de Motivos – Decreto

> **Comentário Detalhado:**
>
> - **Item 1:** A decisão colegiada deliberativa de um Tribunal de Contas reunido em Plenário ou em Câmara que julga em definitivo processos de controle externo e prestação de contas denomina-se **Acórdão** (art. 71 da CF/88 e leis orgânicas dos TCs).
> - **Item 2:** O expediente privativo de autoridades de alto escalão (ministros ou secretários) dirigido ao chefe do Poder Executivo propondo edição de normas, projetos ou decretos é a **Exposição de Motivos (EM)**.
> - **Item 3:** O instrumento de comunicação oficial exclusivo entre os chefes de Poder (Presidente/Governador para Congresso/Assembleia) denomina-se **Mensagem**.
> - **Conclusão:** A sequência exata é *Acórdão – Exposição de Motivos – Mensagem* (Alternativa B).
>
> **Gabarito: B**
"""

def enrich_file_7():
    with open(FILE_7, "r", encoding="utf-8") as f:
        text = f.read()

    # Inserção da Questão 06: no fim da Seção 1 (antes de "## 2. Atributos Fundamentais da Redação Oficial")
    sec2_marker = "## 2. Atributos Fundamentais da Redação Oficial"
    insert_q06 = q06_text + "\n---\n\n"
    idx2 = text.find(sec2_marker)
    dash_idx = text.rfind("---", 0, idx2)
    text = text[:dash_idx] + insert_q06 + text[dash_idx:]

    # Inserção da Questão 07: no fim da Seção 2 (antes de "## 3. Pronomes de Tratamento")
    sec3_marker = "## 3. Pronomes de Tratamento, Vocativos e Endereçamento"
    insert_q07 = q07_text + "\n---\n\n"
    idx3 = text.find(sec3_marker)
    dash_idx = text.rfind("---", 0, idx3)
    text = text[:dash_idx] + insert_q07 + text[dash_idx:]

    # Inserção da Questão 08: no fim da Seção 4 (antes de "## 5. Espécies Documentais e Comunicação Digital")
    sec5_marker = "## 5. Espécies Documentais e Comunicação Digital"
    insert_q08 = q08_text + "\n---\n\n"
    idx5 = text.find(sec5_marker)
    dash_idx = text.rfind("---", 0, idx5)
    text = text[:dash_idx] + insert_q08 + text[dash_idx:]

    # Inserção da Questão 09: na Seção 5.2 (antes de "### 5.3 A Exposição de Motivos (EM)")
    sec53_marker = "### 5.3 A Exposição de Motivos (EM)"
    insert_q09 = "\n---\n" + q09_text + "\n---\n\n"
    idx53 = text.find(sec53_marker)
    text = text[:idx53] + insert_q09 + text[idx53:]

    # Inserção da Questão 10: no fim da Seção 5 (antes de "## 🌐 Fontes Oficiais e Referências Bibliográficas")
    sec_fontes = "## 🌐 Fontes Oficiais e Referências Bibliográficas"
    insert_q10 = q10_text + "\n---\n\n"
    idxf = text.find(sec_fontes)
    dash_idx = text.rfind("---", 0, idxf)
    text = text[:dash_idx] + insert_q10 + text[dash_idx:]

    with open(FILE_7, "w", encoding="utf-8") as f:
        f.write(text)

    print("Arquivo 07 enriquecido com sucesso.")

enrich_file_7()
