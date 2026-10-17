import os, re

FILE_1 = r"fontes_de_estudo/conhecimentos_gerais/01_lingua_portuguesa/01_compreensao_e_interpretacao_de_texto.md"

# Questões para o Arquivo 01:
# Questão 06: Gêneros Textuais (Seção 2)
# Questão 07: Tipologias Textuais (Seção 3)
# Questão 08: Argumentação e Tese (Seção 4.2)
# Questão 09: Pressupostos e Operadores Argumentativos (Seção 4.4)
# Questão 10: Intertextualidade (Seção 8)
# Questão 11: Figuras de Linguagem Sintáticas e Sonoras (Seção 9.4)

q06_text = """
### Questão 06
**(FCC – DPE-RS – Analista – Processual)**  
Considere o seguinte trecho:  
*"A recente decisão governamental de rever a concessão de incentivos fiscais para determinados setores produtivos não deve ser encarada sob a ótica simplista do confronto ideológico. Trata-se, em verdade, de imperativo inadiável de responsabilidade fiscal e transparência republicana. Não é concebível que renúncias bilionárias continuem sendo renovadas sem a devida comprovação de contrapartidas sociais e geração efetiva de empregos. A sociedade tem o direito de saber o retorno exato de cada centavo que deixa de ingressar nos cofres públicos."*  
(Adaptado de publicação institucional de órgão de imprensa)

Quanto ao gênero textual e ao contexto discursivo, é correto afirmar que o texto:

* **A)** Classifica-se como crônica lírica, por valer-se de fatos da vida diária para provocar comoção e despertar nostalgia no leitor.
* **B)** Configura um editorial, na medida em que expressa a posição institucional do veículo sobre tema de interesse público coletivo, empregando tom sóbrio e sem marcas de subjetividade pessoalizada.
* **C)** Estrutura-se como notícia estritamente factual, limitando-se a relatar cronologicamente os atos normativos recém-editados pelo Poder Executivo.
* **D)** Corresponde a um ensaio filosófico subjetivo, centrado na discussão metafísica dos conceitos abstratos de justiça e virtude individual.
* **E)** Caracteriza-se como texto injuntivo-instrucional, voltado a fornecer um passo a passo para que os cidadãos impugnem incentivos fiscais.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A crônica lírica parte de fatos cotidianos simples para evocar poesia, humor ou sentimentos subjetivos íntimos. O texto em análise aborda finanças públicas, orçamento e responsabilidade fiscal com vocabulário técnico-argumentativo.
> - **B)** Correta. O texto analisa criticamente uma política pública, sustenta uma tese ("imperativo inadiável de responsabilidade fiscal"), não possui assinatura individual, evita pronomes de primeira pessoa do singular e expressa a opinião abalizada e institucional do veículo sobre tema de relevante interesse coletivo.
> - **C)** Incorreta. A notícia tem caráter meramente informativo e expositivo (relata quem, o quê, quando, onde e como). O excerto acima é declaradamente opinativo e argumentativo ("não deve ser encarada", "Trata-se, em verdade", "Não é concebível").
> - **D)** Incorreta. O texto é prático, político-econômico e jurídico-administrativo, e não uma reflexão teórica ou especulativa desvinculada de conjuntura concreta.
> - **E)** Incorreta. Textos injuntivos ou instrucionais orientam ações com verbos no imperativo (receitas, editais, manuais). Não há instruções ou comandos procedimentais no excerto.
>
> **Gabarito: B**
"""

q07_text = """
### Questão 07
**(FCC – TRT-23 – Analista Judiciário)**  
Considere o seguinte excerto:  
*"O relator ajeitou os óculos sobre o nariz, respirou fundo e abriu a pasta de capa azul que continha o processo de licitação sob suspeita. O silêncio na sala de sessões era denso, quebrado apenas pelo sussurro intermitente do aparelho de ar-condicionado. Naquelas quatrocentas páginas, repousavam indícios materiais de sobrepreço que desviavam recursos destinados ao transporte escolar. A negligência fiscalizatória da administração pública não é mera desatenção burocrática: traduz-se no abandono de crianças sem acesso às salas de aula e corrói a própria legitimidade das instituições democráticas."*

Sobre a tipologia textual do excerto, constata-se que:

* **A)** Há predomínio absoluto da tipologia narrativa de ficção, inexistindo qualquer juízo opinativo ou argumento dissertativo.
* **B)** Trata-se de texto exclusivamente descritivo, cujo objetivo único é enumerar os traços físicos do relator e o mobiliário do tribunal.
* **C)** Apresenta sequência híbrida em que elementos narrativos e descritivos funcionam como introdução contextualizadora para sustentar uma tese dissertativo-argumentativa sobre os efeitos sociais da corrupção.
* **D)** Constitui texto tipicamente injuntivo, pois determina expressamente a condenação imediata dos gestores responsáveis pela licitação.
* **E)** Classifica-se como dissertação puramente expositiva, isenta de qualquer posicionamento ético ou juízo de valor do emissor.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Embora o excerto comece narrando ações no tempo ("ajeitou", "respirou", "abriu"), a oração final introduz julgamento moral e político contundente ("não é mera desatenção... corrói a própria legitimidade"), afastando o caráter exclusivamente ficcional.
> - **B)** Incorreta. A descrição é apenas um recurso ambiental de ambientação ("pasta de capa azul", "silêncio na sala de sessões era denso"), não constituindo a tipologia estruturante do parágrafo.
> - **C)** Correta. Na tradição da FCC, é recorrente o uso de uma pequena cena narrativa/descritiva que serve de argumento por ilustração (ou exemplificação) para desembocar na tese central dissertativo-argumentativa formulada no desfecho.
> - **D)** Incorreta. O texto não contém ordens, prescrições regulamentares nem verbos no modo imperativo.
> - **E)** Incorreta. Há carga valorativa expressa em "negligência fiscalizatória", "abandono de crianças" e "corrói a própria legitimidade", o que caracteriza argumentação e refuta a pura neutralidade expositiva.
>
> **Gabarito: C**
"""

q08_text = """
### Questão 08
**(FCC – TCE-PI – Auditor de Controle Externo)**  
Considere o seguinte trecho argumentativo:  
*"Costuma-se argumentar que a imposição de regras rígidas de controle prévio nas contratações públicas paralisa a máquina administrativa e asfixia o dinamismo dos investimentos estatais. No entanto, estudos empíricos desenvolvidos pela OCDE e por centros de pesquisa econômica demonstram que cada real investido em fiscalização tempestiva economiza até quatro vezes mais em custos de reparação de danos e sobrepreços contratuais. Portanto, o controle não constitui entrave burocrático, mas sim salvaguarda indispensável à sustentabilidade fiscal do Estado."*

Na organização dos argumentos do excerto, o autor:

* **A)** Apoia sua conclusão exclusivamente no senso comum e no apelo emocional dos leitores em relação aos gastos públicos.
* **B)** Utiliza uma estrutura concessivo-adversativa, antecipando uma objeção frequente para refutá-la mediante dados e argumento de autoridade técnica antes de enunciar a tese conclusiva.
* **C)** Defende que o controle prévio deve ser abolido para assegurar a rapidez nas contratações públicas emergenciais.
* **D)** Conclui que as exigências de controle externo são responsáveis pela lentidão dos investimentos em infraestrutura.
* **E)** Evita o emprego de conectivos de oposição, optando por justapor argumentos que sustentam uma mesma direção ideológica.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O autor cita expressamente "estudos empíricos desenvolvidos pela OCDE e por centros de pesquisa econômica" (provas concretas e autoridade institucional reconhecida), e não mero senso comum ou apelo emotivo.
> - **B)** Correta. O autor adota a consagrada arquitetura argumentativa da FCC: inicia apresentando a tese contrária com fórmula de distanciamento ("Costuma-se argumentar que..."), contrapõe-na por meio do operador adversativo *"No entanto"*, respalda sua refutação com dados técnicos e remata com a conclusão balizada pelo operador *"Portanto"*.
> - **C)** Incorreta. Erro de contradição direta com o texto: o autor sustenta que o controle prévio é "salvaguarda indispensável", e não que deve ser abolido.
> - **D)** Incorreta. A tese do autor afirma exatamente o inverso: que o controle externo é proteção financeira e não entrave à eficiência pública.
> - **E)** Incorreta. O operador adversativo *"No entanto"* cumpre papel axial na guinada argumentativa do parágrafo.
>
> **Gabarito: B**
"""

q09_text = """
### Questão 09
**(FCC – TRT-14 – Analista Judiciário)**  
Considere a frase a seguir:  
*"Após a auditoria operacional, o órgão previdenciário **voltou a** publicar mensalmente as planilhas de desembolso financeiro, e os novos gestores **ainda** mantêm os relatórios acessíveis à consulta pública."*

A análise dos operadores argumentativos e dos implícitos linguísticos da frase indica que:

* **A)** A locução *"voltou a"* gera o pressuposto de que o órgão nunca havia publicado tais planilhas em momento algum de sua história.
* **B)** O advérbio *"ainda"* introduz a certeza de que a transparência dos relatórios será interrompida obrigatoriamente no próximo exercício financeiro.
* **C)** A expressão *"voltou a"* veicula o pressuposto de que as planilhas já eram publicadas no passado e haviam sido suspensas, ao passo que *"ainda"* pressupõe a continuidade no presente de um estado de coisas inaugurado anteriormente.
* **D)** A transparência pública é tratada como mera possibilidade remota, evidenciada pela flexão condicional dos verbos principais.
* **E)** A locução *"após a auditoria"* pressupõe que as auditorias de controle externo são inócuas para modificar condutas administrativas.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Dizer que o órgão *"voltou a"* publicar pressupõe necessariamente que ele já publicava antes e havia interrompido essa prática. Se nunca tivesse publicado, o verbo seria "passou a" ou "iniciou".
> - **B)** Incorreta. O advérbio *"ainda"* marca a persistência temporal de uma ação iniciada no passado até o momento da fala, sem antecipar ou determinar com certeza seu encerramento compulsório.
> - **C)** Correta. Trata-se da clássica distinção de pressupostos linguísticos da FCC: o verbo que indica reiteração (*voltar a*) carrega o pressuposto inegável de prática anterior descontinuada; o advérbio de aspecto continuativo (*ainda*) pressupõe que a ação já vinha ocorrendo e se estende até o presente.
> - **D)** Incorreta. Os verbos estão no modo indicativo afirmativo (*voltou*, *mantêm*), indicando certeza categórica de fatos concretos.
> - **E)** Incorreta. A relação temporal estabelecida indica exatamente o contrário: a auditoria funcionou como marco gerador de aprimoramento da transparência.
>
> **Gabarito: C**
"""

q10_text = """
### Questão 10
**(FCC – TCE-GO – Analista de Controle Externo)**  
Considere os dois textos abaixo:  

**Texto I** (Gonçalves Dias, *Canção do Exílio*):  
*"Minha terra tem palmeiras, / Onde canta o Sabiá; / As aves, que aqui gorjeiam, / Não gorjeiam como lá."*  

**Texto II** (Murilo Mendes, *Canção do Exílio*):  
*"Minha terra tem macieiras da Califórnia / onde cantam gaturamos de Veneza. / Os poetas da minha terra / são pretos que vivem em torres de ametista..."*  

Comparando os Textos I e II sob a perspectiva das relações intertextuais, verifica-se que o Texto II:

* **A)** Constitui uma paráfrase estrita do Texto I, mantendo fidelidade semântica ao ufanismo romântico e à exaltação da natureza nativa brasileira.
* **B)** Apresenta uma paródia, valendo-se da estrutura rítmica e de versos-chave do texto romântico de partida para desconstruir ironicamente a idealização patriótica.
* **C)** Configura um caso de plágio desprovido de qualquer autonomia artística ou intenção crítica.
* **D)** Utiliza uma epígrafe formal que se limita a homenagear Gonçalves Dias sem interagir com os conceitos da obra referenciada.
* **E)** Isola-se de qualquer diálogo com o cânone literário, não permitindo estabelecer paralelo intertextual com o poema de 1843.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A paráfrase reafirma as mesmas ideias do texto-fonte com vocabulário alternativo (relação de adesão). O Texto II altera drasticamente o significado e o tom lírico do original.
> - **B)** Correta. A paródia é o recurso intertextual de ruptura em que a forma, a métrica ou o refrão de um texto consagrado são reaproveitados com conteúdo irônico, crítico ou dissonante, rompendo deliberadamente com a atmosfera original (aqui, o nacionalismo ufanista romântico dá lugar ao estranhamento vanguardista moderno).
> - **C)** Incorreta. Não se trata de apropriação indevida ou fraude autoral, mas de intertextualidade manifesta e reconhecida como recurso estético legítimo.
> - **D)** Incorreta. O Texto II é um poema autônomo completo, e não uma epígrafe (que seria apenas uma citação introdutória no cabeçalho de outra obra).
> - **E)** Incorreta. O título homônimo e a repetição estilizada do primeiro verso estabelecem inegável diálogo com o Texto I.
>
> **Gabarito: B**
"""

q11_text = """
### Questão 11
**(FCC – TRT – Analista Judiciário)**  
Considere o seguinte período:  
*"O procurador examinava minuciosamente os autos da representação; o auditor, as planilhas financeiras das empreiteiras contratadas."*

No trecho acima, a vírgula empregada após a palavra *"auditor"* assinala a ocorrência da seguinte figura de linguagem sintática:

* **A)** Anacoluto, caracterizado pela quebra repentina e assistemática da coesão frasal.
* **B)** Zeugma, consistente na omissão de um termo verbal já expresso na oração anterior.
* **C)** Pleonasmo vicioso, consistente na repetição desnecessária de um complemento oracional.
* **D)** Hipérbato, que consiste na inversão drástica da ordem direta dos elementos sintáticos.
* **E)** Polissíndeto, decorrente da multiplicação expressiva de conjunções coordenativas.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Não há quebra gramatical nem sujeito sem predicado no período. A construção é perfeitamente harmônica e canônica.
> - **B)** Correta. O zeugma é uma modalidade especial de elipse em que se omite termo que **já foi explicitamente mencionado** antes no período. No caso, a vírgula elíptica substitui a forma verbal *"examinava"* ("o auditor [examinava] as planilhas financeiras"), evitando repetição cansativa.
> - **C)** Incorreta. Não há redundância ou repetição enfática/viciosa de ideias na oração.
> - **D)** Incorreta. A ordem direta dos termos foi mantida em ambas as orações (Sujeito + Verbo + Objeto Direto), não havendo transposição ou inversão abrupta.
> - **E)** Incorreta. Não há reiteração de conjunções; o período articula-se por meio de ponto e vírgula e vírgula zeugmática.
>
> **Gabarito: B**
"""

def enrich_file_1():
    with open(FILE_1, "r", encoding="utf-8") as f:
        text = f.read()

    # Inserção da Questão 06: no fim da Seção 2 (antes de "## 3. Tipologias Textuais")
    sec3_marker = "## 3. Tipologias Textuais"
    insert_q06 = q06_text + "\n---\n\n"
    idx3 = text.find(sec3_marker)
    # Procurar a linha "---" antes da sec 3
    dash_idx = text.rfind("---", 0, idx3)
    text = text[:dash_idx] + insert_q06 + text[dash_idx:]

    # Inserção da Questão 07: no fim da Seção 3 (antes de "## 4. Argumentação na Tipologia Dissertativa")
    sec4_marker = "## 4. Argumentação na Tipologia Dissertativa"
    insert_q07 = q07_text + "\n---\n\n"
    idx4 = text.find(sec4_marker)
    dash_idx = text.rfind("---", 0, idx4)
    text = text[:dash_idx] + insert_q07 + text[dash_idx:]

    # Inserção da Questão 08 e 09:
    # Questão 08 após Seção 4.3 (antes de "### 4.4 Pressupostos e Subentendidos")
    sec44_marker = "### 4.4 Pressupostos e Subentendidos"
    insert_q08 = "\n---\n" + q08_text + "\n---\n\n"
    idx44 = text.find(sec44_marker)
    text = text[:idx44] + insert_q08 + text[idx44:]

    # Questão 09 após Seção 4.4 (antes de "## 5. Níveis de Linguagem e Denotação e Conotação")
    sec5_marker = "## 5. Níveis de Linguagem e Denotação e Conotação"
    insert_q09 = q09_text + "\n---\n\n"
    idx5 = text.find(sec5_marker)
    dash_idx = text.rfind("---", 0, idx5)
    text = text[:dash_idx] + insert_q09 + text[dash_idx:]

    # Inserção da Questão 10: no fim da Seção 8 (antes de "## 9. Figuras de Linguagem")
    sec9_marker = "## 9. Figuras de Linguagem"
    insert_q10 = q010_text = q10_text + "\n---\n\n"
    idx9 = text.find(sec9_marker)
    dash_idx = text.rfind("---", 0, idx9)
    text = text[:dash_idx] + insert_q10 + text[dash_idx:]

    # Inserção da Questão 11: no fim da Seção 9 (antes de "## 🌐 Fontes Oficiais e Referências Bibliográficas")
    sec_fontes_marker = "## 🌐 Fontes Oficiais e Referências Bibliográficas"
    insert_q11 = q11_text + "\n---\n\n"
    idxf = text.find(sec_fontes_marker)
    dash_idx = text.rfind("---", 0, idxf)
    text = text[:dash_idx] + insert_q11 + text[dash_idx:]

    with open(FILE_1, "w", encoding="utf-8") as f:
        f.write(text)

    print("Arquivo 01 enriquecido com sucesso.")

enrich_file_1()
