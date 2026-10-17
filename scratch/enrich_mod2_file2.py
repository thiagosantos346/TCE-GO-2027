import os, re

FILE = r"fontes_de_estudo/conhecimentos_gerais/02_matematica_e_raciocinio_logico/02_proporcoes_regra_de_tres_e_porcentagem.md"

q06_text = """
### Questão 06
**(FCC – TRT – Analista Judiciário)**  
Em um tribunal, a razão entre o número de processos físicos e o número de processos eletrônicos que aguardavam triagem era de $3$ para $7$. Se o número total de processos aguardando triagem era de $250$, quantos processos eletrônicos havia a mais do que processos físicos?

* **A)** $80$
* **B)** $100$
* **C)** $120$
* **D)** $140$
* **E)** $175$

> **Comentário Detalhado:**
>
> - **Método da Constante de Proporcionalidade ($k$):**  
>   - Seja $F$ o número de processos físicos e $E$ o número de processos eletrônicos.  
>   - A razão é dada por $\\frac{F}{E} = \\frac{3}{7} \\implies F = 3k \\text{ e } E = 7k$.  
> - **Equação do total:**  
>   $$F + E = 250 \\implies 3k + 7k = 250 \\implies 10k = 250 \\implies k = 25$$  
> - **Cálculo das quantidades:**  
>   - Processos físicos: $F = 3 \\times 25 = 75$.  
>   - Processos eletrônicos: $E = 7 \\times 25 = 175$.  
> - **Diferença solicitada no enunciado:**  
>   $$E - F = 175 - 75 = 100$$  
>   (Ou diretamente pela diferença em partes: $(7 - 3)k = 4k = 4 \\times 25 = 100$).  
> - **Conclusão:** Havia 100 processos eletrônicos a mais do que físicos (Alternativa B).
>
> **Gabarito: B**
"""

q07_text = """
### Questão 07
**(FCC – TCE-GO – Analista de Controle Externo)**  
Uma gratificação extraordinária no valor de R$ 18.000,00 foi dividida entre três auditores de controle externo em partes diretamente proporcionais aos seus respectivos tempos de atuação no órgão: $2$ anos, $3$ anos e $5$ anos. O auditor com maior tempo de serviço recebeu:

* **A)** R$ 3.600,00
* **B)** R$ 5.400,00
* **C)** R$ 9.000,00
* **D)** R$ 10.000,00
* **E)** R$ 12.000,00

> **Comentário Detalhado:**
>
> - **Divisão Diretamente Proporcional:**  
>   - Sejam $A_1$, $A_2$ e $A_3$ os valores recebidos pelos auditores com 2, 3 e 5 anos de atuação, respectivamente.  
>   - $A_1 = 2k$, $A_2 = 3k$, $A_3 = 5k$.  
> - **Soma das quotas:**  
>   $$A_1 + A_2 + A_3 = 18.000 \\implies (2 + 3 + 5)k = 18.000 \\implies 10k = 18.000 \\implies k = 1.800$$  
> - **Valor do auditor com maior tempo de serviço (5 anos):**  
>   $$A_3 = 5 \\times 1.800 = 9.000,00$$  
> - **Conferência:** $A_1 = 3.600$, $A_2 = 5.400$, $A_3 = 9.000$. Soma: $3.600 + 5.400 + 9.000 = 18.000,00$.  
> - **Conclusão:** O auditor recebeu R$ 9.000,00 (Alternativa C).
>
> **Gabarito: C**
"""

q08_text = """
### Questão 08
**(FCC – TCE-PI – Auditor de Controle Externo)**  
Em uma unidade técnica de auditoria, $6$ auditores de mesmo rendimento funcional analisam $180$ prestações de contas trabalhando $8$ horas por dia durante $10$ dias. Se a equipe for reforçada por mais $2$ auditores de igual produtividade, quantas prestações de contas eles conseguirão analisar trabalhando $6$ horas por dia durante $15$ dias?

* **A)** $225$
* **B)** $240$
* **C)** $270$
* **D)** $300$
* **E)** $320$

> **Comentário Detalhado:**
>
> - **Método do Processo $\\times$ Produto (Regra de Três Composta):**  
>   - Na engenharia de problemas da FCC, separam-se as grandezas em dois grupos:  
>     - **Processo (Agentes que realizam a tarefa):** número de auditores ($A$), horas por dia ($H$) e número de dias ($D$).  
>     - **Produto (Resultado produzido):** prestações de contas ($P$).  
>   - Relação fundamental de proporcionalidade:  
>     $$\\frac{\\text{Processo}_1}{\\text{Produto}_1} = \\frac{\\text{Processo}_2}{\\text{Produto}_2} \\implies \\frac{A_1 \\times H_1 \\times D_1}{P_1} = \\frac{A_2 \\times H_2 \\times D_2}{P_2}$$  
> - **Dados da situação 1:** $A_1 = 6$, $H_1 = 8$, $D_1 = 10$, $P_1 = 180$.  
> - **Dados da situação 2:** $A_2 = 6 + 2 = 8$, $H_2 = 6$, $D_2 = 15$, $P_2 = x$.  
> - **Montagem da equação:**  
>   $$\\frac{6 \\times 8 \\times 10}{180} = \\frac{8 \\times 6 \\times 15}{x}$$  
>   $$\\frac{480}{180} = \\frac{720}{x} \\implies \\frac{8}{3} = \\frac{720}{x} \\implies 8x = 3 \\times 720 = 2.160 \\implies x = \\frac{2.160}{8} = 270$$  
> - **Conclusão:** Eles conseguirão analisar exatamente 270 prestações de contas (Alternativa C).
>
> **Gabarito: C**
"""

q09_text = """
### Questão 09
**(FCC – DPE-RS – Analista)**  
O valor de determinada taxa de emolumentos cartorários sofreu um reajuste de $20\\%$ no início do primeiro semestre e, ao final do ano, sofreu um novo aumento sucessivo de $15\\%$. Em relação ao valor inicial antes dos dois reajustes, o aumento real total acumulado foi de:

* **A)** $35{,}0\\%$
* **B)** $37{,}5\\%$
* **C)** $38{,}0\\%$
* **D)** $40{,}0\\%$
* **E)** $42{,}5\\%$

> **Comentário Detalhado:**
>
> - **Método dos Fatores Multiplicadores Cumulativos:**  
>   - Um aumento de $20\\%$ equivale a multiplicar pelo fator $F_1 = 1 + 0{,}20 = 1{,}20$.  
>   - Um aumento de $15\\%$ equivale a multiplicar pelo fator $F_2 = 1 + 0{,}15 = 1{,}15$.  
> - **Fator Acumulado Total ($F_{total}$):**  
>   $$F_{total} = F_1 \\times F_2 = 1{,}20 \\times 1{,}15$$  
>   Efetuando o produto:  
>   $$1{,}20 \\times 1{,}15 = 1{,}380$$  
> - **Taxa de Aumento Equivalente ($i_{total}$):**  
>   $$i_{total} = F_{total} - 1 = 1{,}380 - 1 = 0{,}380 = 38\\%$$  
> - **Alerta de Pegadinha FCC:** A banca induz o candidato apressado a simplesmente somar as porcentagens ($20\\% + 15\\% = 35\\%$, alternativa A). Em aumentos sucessivos, a segunda taxa incide sobre o montante já inflacionado, gerando juros sobre juros ($20\\% + 15\\% + (20\\% \\times 15\\%) = 35\\% + 3\\% = 38\\%$).
>
> **Gabarito: C**
"""

q10_text = """
### Questão 10
**(FCC – TRT-14 – Analista Judiciário)**  
Em determinado município goiano, a alíquota do Imposto Sobre Serviços (ISS) incidente sobre serviços de informática passou de $2\\%$ para $3\\%$ da receita bruta. Comparando a alíquota final com a inicial, verifica-se que houve um acréscimo de:

* **A)** $1$ ponto percentual e uma variação percentual relativa de $50\\%$.
* **B)** $1\\%$ absoluto e uma variação percentual relativa de $33{,}3\\%$.
* **C)** $50$ pontos percentuais e uma variação percentual relativa de $1\\%$.
* **D)** $1$ ponto percentual e uma variação percentual relativa de $100\\%$.
* **E)** $1{,}5$ ponto percentual e uma variação percentual relativa de $25\\%$.

> **Comentário Detalhado:**
>
> - **Distinção Técnica entre Pontos Percentuais e Variação Relativa:**  
>   - **Pontos Percentuais (Diferença Aritmética Absoluta):**  
>     $$\\Delta = 3\\% - 2\\% = 1 \\text{ ponto percentual (p.p.)}$$  
>   - **Variação Percentual Relativa (Aumento em relação à base original de $2\\%$):**  
>     $$V = \\frac{\\text{Valor Final} - \\text{Valor Inicial}}{\\text{Valor Inicial}} = \\frac{3 - 2}{2} = \\frac{1}{2} = 0{,}50 = 50\\%$$  
> - **Conclusão:** O aumento foi de 1 ponto percentual e representou uma variação percentual relativa de $50\\%$ sobre a alíquota anterior (Alternativa A).
>
> **Gabarito: A**
"""

def enrich_mod2_file2():
    with open(FILE, "r", encoding="utf-8") as f:
        text = f.read()

    # Inserção da Questão 06: no fim da Seção 1 (antes de "## 2. Divisão em Partes Proporcionais")
    sec2 = "## 2. Divisão em Partes Proporcionais"
    idx2 = text.find(sec2)
    dash_idx = text.rfind("---", 0, idx2)
    text = text[:dash_idx] + q06_text + "\n---\n\n" + text[dash_idx:]

    # Inserção da Questão 07: na Seção 2.1 (antes de "### 2.2 Divisão Inversamente Proporcional")
    sec22 = "### 2.2 Divisão Inversamente Proporcional e o Método do MMC"
    idx22 = text.find(sec22)
    text = text[:idx22] + "\n---\n" + q07_text + "\n---\n\n" + text[idx22:]

    # Inserção da Questão 08: na Seção 3.3 (antes de "## 4. Porcentagem, Fatores Multiplicadores e Variações")
    sec4 = "## 4. Porcentagem, Fatores Multiplicadores e Variações"
    idx4 = text.find(sec4)
    dash_idx = text.rfind("---", 0, idx4)
    text = text[:dash_idx] + q08_text + "\n---\n\n" + text[dash_idx:]

    # Inserção da Questão 09: na Seção 4.2 (antes de "### 4.3 Inversão da Base de Referência Percentual")
    sec43 = "### 4.3 Inversão da Base de Referência Percentual"
    idx43 = text.find(sec43)
    dash_idx = text.rfind("---", 0, idx43)
    text = text[:dash_idx] + q09_text + "\n---\n\n" + text[dash_idx:]

    # Inserção da Questão 10: no fim da Seção 4 (antes de "## 🌐 Fontes Oficiais e Referências Bibliográficas")
    sec_fontes = "## 🌐 Fontes Oficiais e Referências Bibliográficas"
    idxf = text.find(sec_fontes)
    dash_idx = text.rfind("---", 0, idxf)
    text = text[:dash_idx] + q10_text + "\n---\n\n" + text[dash_idx:]

    with open(FILE, "w", encoding="utf-8") as f:
        f.write(text)

    print("Module 02 File 02 enriquecido com sucesso.")

enrich_mod2_file2()
