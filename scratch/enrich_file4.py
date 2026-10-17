import os, re

FILE_4 = r"fontes_de_estudo/conhecimentos_gerais/01_lingua_portuguesa/04_sintaxe_coordenacao_subordinacao_conectivos_pontuacao.md"

q06_text = """
### Questão 06
**(FCC – DPE-RS – Analista Jurídico)**  
Considere o período:  
*"O plenário não acolheu as preliminares da defesa, nem os auditores encontraram atenuantes nos documentos acostados aos autos."*

Em relação à estrutura sintática do período acima, é correto afirmar que:

* **A)** É composto por subordinação, sendo a segunda oração classificada como subordinada substantiva completiva nominal.
* **B)** É composto por coordenação, sendo a segunda oração uma coordenada sindética aditiva introduzida pela conjunção *"nem"*.
* **C)** A oração introduzida por *"nem"* expressa circunstância de consequência em relação ao fato expresso na primeira oração.
* **D)** A conjunção *"nem"* equivale semanticamente ao conectivo conclusivo *"por conseguinte"*.
* **E)** As orações guardam relação de dependência sintática estrita, exercendo uma a função de sujeito da outra.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O período é composto por coordenação, pois as orações são sintaticamente independentes entre si (não exercem função de termo oracional de outra oração).
> - **B)** Correta. A conjunção coordenativa aditiva *"nem"* equivale a *"e não"*, ligando duas orações coordenadas que expressam soma de ideias negativas: *"O plenário não acolheu as preliminares (...) e os auditores não encontraram atenuantes..."*. Trata-se de oração coordenada sindética aditiva.
> - **C)** Incorreta. Não há nexo causal-consecutivo entre as orações, mas simples adição de fatos constatados.
> - **D)** Incorreta. *"Nem"* é aditivo, ao passo que *"por conseguinte"* é conclusivo.
> - **E)** Incorreta. A dependência sintática é própria da subordinação. Na coordenação, cada oração possui estrutura sintática completa e autônoma.
>
> **Gabarito: B**
"""

q07_text = """
### Questão 07
**(FCC – TCE-GO – Analista de Controle Externo)**  
Considere as duas orações destacadas a seguir:  

1. *"É fundamental **que os gestores apresentem as notas fiscais originais**."*  
2. *"A equipe técnica constatou **que os pagamentos foram efetuados sem prévio empenho**."*  

Quanto à função sintática exercida pelas orações destacadas, assinale a alternativa correta:

* **A)** Em 1, a oração é subordinada substantiva objetiva direta; em 2, é subordinada substantiva subjetiva.
* **B)** Em 1, a oração exerce a função de sujeito do verbo *ser* (subordinada substantiva subjetiva); em 2, funciona como objeto direto da forma verbal *constatou* (subordinada substantiva objetiva direta).
* **C)** Ambas as orações exercem a função de aposto explicativo do termo antecedente.
* **D)** Em 1 e 2, as orações classificam-se como subordinadas adjetivas explicativas introduzidas por pronome relativo.
* **E)** Em 1, a oração é completiva nominal dependente do predicativo *fundamental*; em 2, é adverbial causal.

> **Comentário Detalhado:**
>
> - **Oração 1:** *"É fundamental [que os gestores apresentem as notas fiscais originais]"*. Aplicando o método da substituição pelo pronome substantivo **ISSO**: *"É fundamental ISSO"* $\rightarrow$ *"ISSO é fundamental"*. O termo *"ISSO"* funciona como sujeito da oração principal (que possui verbo de ligação *é* + predicativo do sujeito *fundamental*). Logo, a oração é **subordinada substantiva subjetiva**.
> - **Oração 2:** *"A equipe técnica constatou [que os pagamentos foram efetuados sem prévio empenho]"*. Substituindo: *"A equipe técnica constatou ISSO"*. O verbo *constatar* é transitivo direto (quem constata, constata algo). Logo, o termo *"ISSO"* desempenha a função de objeto direto da oração principal, classificando a oração como **subordinada substantiva objetiva direta**.
> - **Conclusão:** A alternativa **B** traduz com exatidão essas duas funções sintáticas primordiais da FCC.
>
> **Gabarito: B**
"""

q08_text = """
### Questão 08
**(FCC – TRT – Analista Judiciário)**  
Considere o período:  
*"À medida que as investigações avançavam, novos indícios de irregularidades vinham à tona, de modo que a comissão decidiu prorrogar os trabalhos por mais trinta dias."*

Os conectivos destacados expressam, correta e respectivamente, as noções circunstanciais de:

* **A)** tempo e causa.
* **B)** proporção e consequência.
* **C)** concessão e finalidade.
* **D)** condição e conformidade.
* **E)** proporção e explicação.

> **Comentário Detalhado:**
>
> - **1ª locução:** *"À medida que"* é a locução conjuntiva subordinativa por excelência de valor **proporcional** (indica um fenômeno que varia em relação direta e concomitante com outro). Atenção: não confundir com a locução causal "na medida em que".
> - **2ª locução:** *"de modo que"* introduz fato que decorre do que foi afirmado anteriormente (efeito produzido pelo acúmulo de novos indícios), configurando nexo subordinativo adverbial **consecutivo** (consequência).
> - **Análise das alternativas:** A alternativa **B** traz exatamente a dupla relação: proporção e consequência.
>
> **Gabarito: B**
"""

q09_text = """
### Questão 09
**(FCC – TCE-PI – Auditor de Controle Externo)**  
Considere a pontuação no período abaixo:  
*"A Lei de Responsabilidade Fiscal impõe limites severos para os gastos com pessoal; os municípios combalidos financeiramente, no entanto, frequentemente ultrapassam esses tetos prudenciais."*

Sobre o emprego dos sinais de pontuação no trecho, assinale a alternativa correta:

* **A)** O ponto e vírgula separa orações coordenadas de certa extensão que guardam contraste semântico, estando a segunda oração marcada por conectivo adversativo deslocado.
* **B)** O ponto e vírgula foi empregado incorretamente, devendo ser compulsoriamente substituído por dois-pontos para introduzir uma citação.
* **C)** As vírgulas que isolam *"no entanto"* são de emprego facultativo, podendo ser suprimidas sem nenhum prejuízo às normas gramaticais.
* **D)** O ponto e vírgula deveria ser substituído por ponto de exclamação para realçar a indignação do autor.
* **E)** É obrigatória a aposição de vírgula imediatamente após o termo *"combalidos financeiramente"*, sob pena de quebra da regência verbal.

> **Comentário Detalhado:**
>
> - **A)** Correta. O ponto e vírgula é o sinal de pontuação ideal na sintaxe culta da FCC para separar orações coordenadas extensas que se contrapõem em sentido, especialmente quando uma delas já possui vírgulas internas isolando adjuntos ou conjunções adversativas deslocadas (como *"no entanto"* entre vírgulas).
> - **B)** Incorreta. Não se trata de enumeração explicativa nem citação literal, razão pela qual o ponto e vírgula é plenamente legítimo e elegante.
> - **C)** Incorreta. Estando a conjunção adversativa (*no entanto*) deslocada para o meio da oração (após o sujeito *"os municípios..."*), o isolamento por vírgulas é **rigorosamente obrigatório**.
> - **D)** Incorreta. O texto é técnico-dissertativo e descarta pontuação enfática de teor emotivo.
> - **E)** Incorreta. *"combalidos financeiramente"* é adjunto adnominal restritivo de *municípios*; colocar vírgula após ele separaria o sujeito do seu verbo (*ultrapassam*), violando a regra de ouro SVC.
>
> **Gabarito: A**
"""

q10_text = """
### Questão 10
**(FCC – TRT-23 – Técnico Judiciário)**  
Considere as seguintes frases:  

I. *"Os auditores que concluíram a capacitação técnica elaboraram pareceres impecáveis."*  
II. *"Os auditores, que concluíram a capacitação técnica, elaboraram pareceres impecáveis."*  

Comparando-se as frases I e II quanto aos efeitos semânticos e sintáticos decorrentes da pontuação, conclui-se que:

* **A)** Em I e II, o sentido é estritamente idêntico, sendo o uso das vírgulas mero capricho de estilo do redator.
* **B)** Em I, a oração sem vírgulas restringe o sentido de *auditores*, indicando que apenas um grupo específico deles concluiu o curso; em II, a oração entre vírgulas é explicativa, atribuindo a conclusão da capacitação à totalidade dos auditores referidos.
* **C)** Em II, a oração entre vírgulas restringe o universo dos auditores, ao passo que em I generaliza para toda a categoria profissional.
* **D)** A frase I contém erro gramatical grave por não pontuar oração adjetiva introduzida por pronome relativo.
* **E)** A frase II apresenta pontuação incorreta porque nunca se deve isolar orações adjetivas por vírgulas.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A presença ou ausência de vírgulas nas orações subordinadas adjetivas altera radicalmente o escopo semântico da frase (restrição vs. generalização explicativa).
> - **B)** Correta. Trata-se da clássica distinção entre orações subordinadas adjetivas cobrada à exaustão pela FCC:  
>   - **Sem vírgulas (Restritiva - Frase I):** Limita o antecedente. Apenas aqueles auditores que concluíram a capacitação elaboraram pareceres impecáveis (os que não concluíram não o fizeram).  
>   - **Com vírgulas (Explicativa - Frase II):** Generaliza e qualifica o antecedente como um todo. Todos os auditores em questão concluíram a capacitação técnica e elaboraram pareceres impecáveis.
> - **C)** Incorreta. Inverteu os conceitos (afirmou que a pontuada restringe, o que é falso).
> - **D) e E)** Incorretas. Ambas as frases são gramaticalmente impecáveis e plenamente válidas, cada qual veiculando um sentido próprio e distinto.
>
> **Gabarito: B**
"""

def enrich_file_4():
    with open(FILE_4, "r", encoding="utf-8") as f:
        text = f.read()

    # Inserção da Questão 06: no fim da Seção 1 (antes de "## 2. Orações Coordenadas e Conectivos Coordenativos")
    sec2_marker = "## 2. Orações Coordenadas e Conectivos Coordenativos"
    insert_q06 = q06_text + "\n---\n\n"
    idx2 = text.find(sec2_marker)
    dash_idx = text.rfind("---", 0, idx2)
    text = text[:dash_idx] + insert_q06 + text[dash_idx:]

    # Inserção da Questão 07: na Seção 3.2 (antes de "### 3.3 Orações Subordinadas Adjetivas")
    sec33_marker = "### 3.3 Orações Subordinadas Adjetivas: Explicativas vs. Restritivas"
    insert_q07 = "\n---\n" + q07_text + "\n---\n\n"
    idx33 = text.find(sec33_marker)
    text = text[:idx33] + insert_q07 + text[idx33:]

    # Inserção da Questão 08: na Seção 4.1 (antes de "### 4.2 Adversativas vs. Concessivas")
    sec42_marker = "### 4.2 Adversativas vs. Concessivas: Conflito Sintático, Semântico e Modal"
    insert_q08 = "\n---\n" + q08_text + "\n---\n\n"
    idx42 = text.find(sec42_marker)
    text = text[:idx42] + insert_q08 + text[idx42:]

    # Inserção da Questão 09: na Seção 5.4 (antes de "### 5.5 Alterações de Sentido Provocadas pela Supressão")
    sec55_marker = "### 5.5 Alterações de Sentido Provocadas pela Supressão ou Deslocamento de Pontuação"
    insert_q09 = "\n---\n" + q09_text + "\n---\n\n"
    idx55 = text.find(sec55_marker)
    text = text[:idx55] + insert_q09 + text[idx55:]

    # Inserção da Questão 10: no fim da Seção 5 (antes de "## 🌐 Fontes Oficiais e Referências Bibliográficas")
    sec_fontes = "## 🌐 Fontes Oficiais e Referências Bibliográficas"
    insert_q10 = q10_text + "\n---\n\n"
    idxf = text.find(sec_fontes)
    dash_idx = text.rfind("---", 0, idxf)
    text = text[:dash_idx] + insert_q10 + text[dash_idx:]

    with open(FILE_4, "w", encoding="utf-8") as f:
        f.write(text)

    print("Arquivo 04 enriquecido com sucesso.")

enrich_file_4()
