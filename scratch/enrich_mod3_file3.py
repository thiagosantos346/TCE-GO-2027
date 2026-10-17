import os, re

FILE = r"fontes_de_estudo/conhecimentos_gerais/03_legislacao_institucional/03_regimento_interno_tce_go_resolucao_22_2008.md"

q06_text = """
### Questão 06
**(FCC – Inédita – Padrão TCE-GO)**  
De acordo com o Regimento Interno do Tribunal de Contas do Estado de Goiás (Resolução nº 22/2008, arts. 1º a 35), quanto à competência e funcionamento dos órgãos colegiados:

* **A)** As Câmaras têm competência para emitir o parecer prévio sobre as contas anuais prestadas pelo Governador do Estado.
* **B)** O Tribunal Pleno funciona com a presença de, no mínimo, 4 Conselheiros, além do Presidente, e delibera sobre matérias regimentais, pedidos de rescisão e uniformização de jurisprudência.
* **C)** O Presidente do Tribunal participa do sorteio ordinário de distribuição de processos em ambas as Câmaras deliberativas.
* **D)** As Câmaras são presididas exclusivamente pelos Conselheiros Substitutos mais antigos em exercício.
* **E)** As deliberações em processos de consulta formulados por autoridades legitimadas são apreciadas originariamente pelas Câmaras.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A emissão de parecer prévio sobre as contas anuais do Governador do Estado é competência constitucional privativa e indelegável do **Tribunal Pleno** (art. 26 da CE/GO e arts. 14 e 15 do RITCE-GO).
> - **B)** Correta. O Plenário do TCE-GO é composto pelos 7 Conselheiros e exige o quórum mínimo de maioria absoluta de seus membros (4 Conselheiros além do Presidente) para funcionar e deliberar, sendo de sua alçada exclusiva a apreciação de incidentes de inconstitucionalidade, consultas, pedidos de rescisão e atos normativos.
> - **C)** Incorreta. O Presidente do Tribunal não integra Câmaras nem participa da distribuição ordinária de processos de controle externo, cabendo-lhe a direção administrativa e a presidência das sessões plenárias.
> - **D)** Incorreta. Cada Câmara é presidida pelo Conselheiro titular mais antigo que dela faça parte, em sistema de rodízio anual regimental.
> - **E)** Incorreta. O processo de Consulta é de apreciação obrigatória e originária do **Tribunal Pleno** (art. 15, IV, do RITCE-GO).
>
> **Gabarito: B**
"""

q07_text = """
### Questão 07
**(FCC – Inédita – Padrão TCE-GO)**  
No tocante às atribuições da Corregedoria-Geral e da Ouvidoria do TCE-GO, previstas no Regimento Interno (Resolução nº 22/2008):

* **A)** O Corregedor-Geral é eleito dentre os servidores de carreira do quadro de analistas de controle externo, por votação secreta da assembleia funcional.
* **B)** A Corregedoria-Geral tem por finalidade a fiscalização disciplinar dos membros e servidores do Tribunal, a realização de correições ordinárias e extraordinárias nas unidades técnicas e o controle dos prazos de instrução e julgamento processual.
* **C)** A Ouvidoria do TCE-GO pode acolher denúncias anônimas como peças processuais autônomas com capacidade probatória imediata, dispensando apuração preliminar.
* **D)** O Corregedor-Geral acumula automaticamente as funções jurisdicionais de relator nos processos de prestação de contas do Governador.
* **E)** As decisões disciplinares sancionatórias do Corregedor-Geral são irrecorríveis e não comportam revisão pelo Pleno.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O Corregedor-Geral é eleito pelo Tribunal Pleno **dentre os seus membros efetivos (Conselheiros)**, concomitantemente com o Presidente e o Vice-Presidente, para mandato de 2 anos (art. 38 do RITCE-GO).
> - **B)** Correta. Nos termos dos arts. 42 e 43 do Regimento Interno, a Corregedoria-Geral é órgão de direção superior encarregado da correição interna permanente, fiscalização da conduta ética/funcional de membros e servidores e monitoramento da tempestividade e regularidade processual.
> - **C)** Incorreta. A Ouvidoria recebe manifestações e representações de cidadãos, mas o Regimento veda o anonimato como fundamento único de processo formal de controle externo; manifestações anônimas podem, no máximo, inspirar averiguação sumária e reservada da Ouvidoria/Corregedoria.
> - **D)** Incorreta. O relator das contas de governo é sorteado entre os Conselheiros em sessão específica, não havendo vinculação automática com a Corregedoria.
> - **E)** Incorreta. De eventuais decisões da Corregedoria cabe recurso ao Tribunal Pleno.
>
> **Gabarito: B**
"""

q08_text = """
### Questão 08
**(FCC – Inédita – Padrão TCE-GO)**  
Acerca das regras regimentais de impedimento e suspeição de Conselheiros e da sistemática do Plenário Virtual no TCE-GO (Resolução nº 22/2008):

* **A)** O Conselheiro é considerado impedido de atuar em processo no qual tenha interesse puramente acadêmico ou científico sobre o tema jurídico debatido.
* **B)** Considera-se impedido de relatar ou votar no processo o Conselheiro que for cônjuge, companheiro ou parente em linha reta ou colateral até o terceiro grau de qualquer uma das partes ou de seus procuradores formalmente constituídos nos autos.
* **C)** A arguição de suspeição de Conselheiro pode ser apresentada oralmente por qualquer pessoa presente ao plenário, sem necessidade de fundamentação fática.
* **D)** No Plenário Virtual, a ausência de manifestação de voto pelo Conselheiro no prazo regimental computa-se como voto divergente da proposta do Relator.
* **E)** As sessões virtuais não admitem pedido de vista ou destaque para julgamento em sessão presencial.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Manifestação doutrinária genérica ou posicionamento acadêmico prévio não configura impedimento nem suspeição legal.
> - **B)** Correta. O RITCE-GO adota as hipóteses clássicas de impedimento da legislação processual (CPC e CPP): há impedimento de ordem objetiva e absoluta do julgador quando no feito atuar como parte, advogado ou interessado seu cônjuge, companheiro ou parente até o terceiro grau (consanguíneo ou afim).
> - **C)** Incorreta. A arguição de suspeição ou impedimento exige forma escrita fundamentada, acompanhada dos meios de prova materiais.
> - **D)** Incorreta. Na sistemática das sessões virtuais do TCE-GO, a ausência de manifestação do julgador no prazo assinalado presume adesão/concordância com o voto do Relator (voto convergente tácito).
> - **E)** Incorreta. Qualquer Conselheiro ou o Procurador-Geral de Contas pode solicitar destaque para julgamento em sessão presencial ou formular pedido de vista regimental.
>
> **Gabarito: B**
"""

q09_text = """
### Questão 09
**(FCC – Inédita – Padrão TCE-GO)**  
Em relação ao direito de sustentação oral e à disciplina do pedido de vista nas sessões de julgamento do TCE-GO, conforme o RITCE-GO (arts. 100 a 115):

* **A)** A sustentação oral da parte ou de seu advogado legalmente habilitado é realizada após a proclamação formal do resultado pelo Presidente da sessão.
* **B)** A sustentação oral é admitida pelo tempo improrrogável de até 15 minutos, devendo ser requerida previamente, sendo facultada a manifestação oral do Ministério Público de Contas por igual período.
* **C)** O pedido de vista formulado por Conselheiro em sessão confere prazo perpétuo e sem devolução obrigatória dos autos.
* **D)** Formulado pedido de vista, os demais julgadores ficam impedidos de antecipar seus votos na mesma sessão.
* **E)** A sustentação oral de advogados é privativa das sessões da 1ª Câmara, sendo expressamente vedada nas sessões plenárias.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A sustentação oral ocorre **antes** do início da votação do colegiado (imediatamente após a leitura do relatório e antes do voto do Relator), para que possa influenciar o julgamento dos membros da Corte.
> - **B)** Correta. De acordo com o art. 102 do Regimento Interno do TCE-GO, os procuradores das partes podem produzir sustentação oral pelo prazo regulamentar de **15 minutos**, estendendo-se igual prerrogativa ao representante do Ministério Público de Contas (art. 104).
> - **C)** Incorreta. O pedido de vista tem prazo regimentalmente determinado (geralmente até a 2ª sessão subsequente), sob pena de requisição compulsória dos autos pelo Presidente da sessão.
> - **D)** Incorreta. O regimento faculta expressamente aos julgadores que se sentirem habilitados a antecipar seus votos antes da remessa dos autos ao vistor.
> - **E)** Incorreta. A sustentação oral é plenamente cabível tanto nas Câmaras quanto no Plenário.
>
> **Gabarito: B**
"""

q10_text = """
### Questão 10
**(FCC – Inédita – Padrão TCE-GO)**  
Quanto ao processo de Representação perante o Tribunal de Contas do Estado de Goiás (arts. 135 a 140 do RITCE-GO):

* **A)** A Representação é privativa dos membros do Poder Legislativo, não podendo ser manejada por órgãos de controle interno ou equipes de auditoria.
* **B)** Têm legitimidade concorrente para formalizar representação ao TCE-GO: os Conselheiros e Conselheiros Substitutos, o Ministério Público de Contas, os titulares de órgãos de controle interno estadual, as autoridades públicas que tiverem ciência de irregularidades no exercício da função e as equipes técnicas de auditoria.
* **C)** A representação protocolada por equipe técnica de fiscalização pode ser arquivada monocraticamente pelo Presidente do Tribunal sem distribuição a relator.
* **D)** A representação prescreve no prazo improrrogável de 6 meses contados da ocorrência do fato sob apuração.
* **E)** Não cabe a aplicação de medidas cautelares no âmbito de processo instaurado por representação.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A legitimidade para representação é ampla e funcional, abrangendo órgãos ministeriais, equipes de inspeção/auditoria e dirigentes da administração pública (art. 135 do RITCE-GO).
> - **B)** Correta. O rol de legitimados para deflagrar processo de representação no TCE-GO abrange tanto os atores internos de fiscalização (Conselheiros, Auditores substitutos, MPC e analistas de controle externo) quanto autoridades públicas externas e chefes de controle interno vinculados ao dever legal de representar sob pena de solidariedade (art. 74, § 1º, da CF/88).
> - **C)** Incorreta. Uma vez preenchidos os requisitos de admissibilidade regimental, o processo é distribuído por sorteio ao Relator competente.
> - **D)** Incorreta. O prazo prescricional para o exercício da pretensão de controle externo é quinquenal (5 anos).
> - **E)** Incorreta. As medidas cautelares (art. 41 da Lei Orgânica) são plenamente cabíveis nos processos de representação e denúncia.
>
> **Gabarito: B**
"""

def enrich_mod3_file3():
    with open(FILE, "r", encoding="utf-8") as f:
        text = f.read()

    # Inserção da Questão 06: no fim da Seção 1 (antes de "## 2. Órgãos de Direção Superior")
    sec2 = "## 2. Órgãos de Direção Superior e Órgãos Vinculados (Arts. 36 a 70)"
    idx2 = text.find(sec2)
    dash_idx = text.rfind("---", 0, idx2)
    text = text[:dash_idx] + q06_text + "\n---\n\n" + text[dash_idx:]

    # Inserção da Questão 07: no fim da Seção 2 (antes de "## 3. Dinâmica Processual")
    sec3 = "## 3. Dinâmica Processual, Instrução e Sessões de Julgamento (Arts. 71 a 120)"
    idx3 = text.find(sec3)
    dash_idx = text.rfind("---", 0, idx3)
    text = text[:dash_idx] + q07_text + "\n---\n\n" + text[dash_idx:]

    # Inserção da Questão 08: na Seção 3.2 (antes de "### 3.3 Ordem das Deliberações")
    sec33 = "### 3.3 Ordem das Deliberações, Pedido de Vista e Sustentação Oral (15 Minutos)"
    idx33 = text.find(sec33)
    text = text[:idx33] + "\n---\n" + q08_text + "\n---\n\n" + text[idx33:]

    # Inserção da Questão 09: no fim da Seção 3 (antes de "## 4. Processos Especiais Disciplinados no RITCE-GO")
    sec4 = "## 4. Processos Especiais Disciplinados no RITCE-GO (Arts. 121 a 180)"
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

    print("Module 03 File 03 enriquecido com sucesso.")

enrich_mod3_file3()
