# 02 - Grandezas Proporcionais, Regra de Três e Porcentagem

> **Matéria:** Matemática e Raciocínio Lógico  
> **Cargos:** A01 – Técnico de Controle Externo (Adm) / B02 – Técnico de Controle Externo (TI)  
> **Arquivo:** `02_proporcoes_regra_de_tres_e_porcentagem.md`  
> **Status:** 🟢 Teoria Aprofundada + 5 Questões FCC Comentadas (A a E)



---


## 📌 Ementa / Itens do Edital
- Números e grandezas proporcionais: razões e proporções.
- Divisão em partes proporcionais (direta e inversa).
- Regra de três simples (direta e inversa).
- Porcentagem e problemas envolvendo regra de três simples, cálculos de porcentagem, acréscimos e descontos.

---

## 🧭 Sumário

1. [Razões, Proporções e Propriedades Fundamentais](#1-razoes-proporcoes-e-propriedades-fundamentais)
    1. [Conceito de Razão e Grandezas Comensuráveis](#11-conceito-de-razao-e-grandezas-comensuraveis)
    2. [Proporções e a Propriedade Fundamental](#12-proporcoes-e-a-propriedade-fundamental)
    3. [Propriedade da Soma dos Termos e Constante de Proporcionalidade](#13-propriedade-da-soma-dos-termos-e-constante-de-proporcionalidade)
    4. [Teste 082](#Teste-082)
2. [Divisão em Partes Proporcionais](#2-divisao-em-partes-proporcionais)
    1. [Divisão Diretamente Proporcional com a Constante k](#21-divisao-diretamente-proporcional-com-a-constante-k)
    2. [Divisão Inversamente Proporcional e o Método do MMC](#22-divisao-inversamente-proporcional-e-o-metodo-do-mmc)
    3. [Divisão Proporcional Composta ou Mista](#23-divisao-proporcional-composta-ou-mista)
    4. [Teste 083](#Teste-083)
    5. [Teste 084](#Teste-084)
    6. [Teste 085](#Teste-085)
3. [Classificação de Grandezas e Regra de Três Simples](#3-classificacao-de-grandezas-e-regra-de-tres-simples)
    1. [Grandezas Diretamente Proporcionais e Multiplicação Cruzada](#31-grandezas-diretamente-proporcionais-e-multiplicacao-cruzada)
    2. [Grandezas Inversamente Proporcionais e Multiplicação em Linha Reta](#32-grandezas-inversamente-proporcionais-e-multiplicacao-em-linha-reta)
    3. [Método Prático das Setas e Identificação de Armadilhas](#33-metodo-pratico-das-setas-e-identificacao-de-armadilhas)
    4. [Teste 086](#Teste-086)
    5. [Teste 087](#Teste-087)
4. [Porcentagem, Fatores Multiplicadores e Variações](#4-porcentagem-fatores-multiplicadores-e-variacoes)
    1. [Conceito e Fatores de Aumento e Desconto](#41-conceito-e-fatores-de-aumento-e-desconto)
    2. [Aumentos e Descontos Sucessivos Cumulativos](#42-aumentos-e-descontos-sucessivos-cumulativos)
    3. [Inversão da Base de Referência Percentual](#43-inversao-da-base-de-referencia-percentual)
    4. [Diferença entre Pontos Percentuais e Variação Percentual](#44-diferenca-entre-pontos-percentuais-e-variacao-percentual)
    5. [Teste 088](#Teste-088)
    6. [Teste 089](#Teste-089)
    7. [Teste 090](#Teste-090)
    8. [Teste 091](#Teste-091)
5. [🌐 Fontes Oficiais e Referências Bibliográficas](#fontes-oficiais-e-referencias-bibliograficas)

---

## 1. Razões, Proporções e Propriedades Fundamentais

O estudo das grandezas proporcionais é um dos temas de maior peso quantitativo nas provas da Fundação Carlos Chagas. Seu domínio instrumentaliza a análise de contratos públicos, distribuição orçamentária, cálculo de auditorias e reajustes econômico-financeiros.

### 1.1 Conceito de Razão e Grandezas Comensuráveis

* **Razão:** Dados dois números reais $a$ e $b$ (com $b \neq 0$), a razão entre $a$ e $b$ (nesta ordem) é o quociente indicado pela divisão:
  $$\text{Razão} = \frac{a}{b} \quad \text{ou} \quad a : b$$
  O primeiro termo $a$ denomina-se **antecedente** e o segundo termo $b$ é o **consequente**.
* Quando as grandezas possuem a mesma unidade de medida (ex.: metros por metros, reais por reais), a razão é uma grandeza **adimensional pura**. Quando comparam grandezas de naturezas físicas distintas, expressam taxas ou grandezas derivadas (ex.: velocidade média em $\text{km/h}$, densidade demográfica em $\text{hab/km}^2$).

### 1.2 Proporções e a Propriedade Fundamental

Uma proporção é formalmente definida como a **igualdade matemática entre duas ou mais razões equivalentes**:
$$\frac{a}{b} = \frac{c}{d} \quad \text{lê-se: 'a está para b assim como c está para d'}$$
Os termos $a$ e $d$ denominam-se **extremos**, enquanto $b$ e $c$ são os **meios**.

#### A Propriedade Fundamental das Proporções:
Em qualquer proporção válida, o produto dos extremos é rigorosamente igual ao produto dos meios:
$$\frac{a}{b} = \frac{c}{d} \iff a \cdot d = b \cdot c \quad (b, d \neq 0)$$

```mermaid
flowchart TD
    G["Análise de Duas Grandezas: X e Y"] --> Q{"Ao dobrar X, o que ocorre com Y?"}
    Q -->|"Y também dobra"| DP["Diretamente Proporcionais<br/>• Razão X/Y = constante<br/>• Multiplicação cruzada"]
    Q -->|"Y cai pela metade"| IP["Inversamente Proporcionais<br/>• Produto X · Y = constante<br/>• Multiplicação em linha reta"]
```

### 1.3 Propriedade da Soma dos Termos e Constante de Proporcionalidade

Em uma série de razões iguais, a soma dos antecedentes dividida pela soma dos consequentes é igual a qualquer uma das razões primitivas, correspondendo à constante de proporcionalidade $k$:
$$\frac{a}{b} = \frac{c}{d} = \frac{e}{f} = k \implies \frac{a + c + e}{b + d + f} = k$$
Essa propriedade é a base algébrica definitiva para solucionar repartições orçamentárias e partilhas de bens em auditoria sem necessidade de recorrer a sistemas lineares extensos.

---

### Teste 082
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
Em um tribunal, a razão entre o número de processos físicos e o número de processos eletrônicos que aguardavam triagem era de $3$ para $7$. Se o número total de processos aguardando triagem era de $250$, quantos processos eletrônicos havia a mais do que processos físicos?

* **A)** $80$
* **B)** $100$
* **C)** $120$
* **D)** $140$
* **E)** $175$


---

> **Comentário Detalhado:**
>
> - **Método da Constante de Proporcionalidade ($k$):**  
>   - Seja $F$ o número de processos físicos e $E$ o número de processos eletrônicos.  
>   - A razão é dada por $\frac{F}{E} = \frac{3}{7} \implies F = 3k \text{ e } E = 7k$.  
> - **Equação do total:**  
>   $$F + E = 250 \implies 3k + 7k = 250 \implies 10k = 250 \implies k = 25$$  
> - **Cálculo das quantidades:**  
>   - Processos físicos: $F = 3 \times 25 = 75$.  
>   - Processos eletrônicos: $E = 7 \times 25 = 175$.  
> - **Diferença solicitada no enunciado:**  
>   $$E - F = 175 - 75 = 100$$  
>   (Ou diretamente pela diferença em partes: $(7 - 3)k = 4k = 4 \times 25 = 100$).  
> - **Conclusão:** Havia 100 processos eletrônicos a mais do que físicos (Alternativa B).
>
> **Gabarito: B**

---

## 2. Divisão em Partes Proporcionais

A partilha proporcional consiste em distribuir uma quantia total $V$ entre vários beneficiários ou centros de custo em conformidade com critérios predeterminados de mérito, produtividade ou penalidade.

### 2.1 Divisão Diretamente Proporcional com a Constante k

Repartir um total $V$ em partes $x, y, z$ diretamente proporcionais aos pesos $a, b, c$:

1. Define-se cada cota multiplicando o peso respectivo pela constante $k$:
   $$x = a \cdot k, \quad y = b \cdot k, \quad z = c \cdot k$$
2. Como a soma das partes totaliza o montante global $V$:
   $$a \cdot k + b \cdot k + c \cdot k = V \implies k \cdot (a + b + c) = V \implies k = \frac{V}{a + b + c}$$
3. Cada parte individual é calculada multiplicando $k$ pelo peso do beneficiário.

### 2.2 Divisão Inversamente Proporcional e o Método do MMC

Repartir um montante $V$ em partes $x, y, z$ inversamente proporcionais aos coeficientes $a, b, c$ significa repartir **diretamente aos seus inversos** $\frac{1}{a}, \frac{1}{b}, \frac{1}{c}$.

#### O Método Rápido do MMC:
1. Escrevem-se as frações inversas dos pesos: $\frac{1}{a}, \frac{1}{b}, \frac{1}{c}$;
2. Calcula-se o MMC entre os denominadores $a, b, c$ e reduzem-se todas as frações ao mesmo denominador comum;
3. **Despreza-se o denominador comum** e utilizam-se os novos numeradores inteiros como os pesos diretos para a constante $k$.

*Exemplo com 2, 3 e 4:*

* Inversos: $\frac{1}{2}, \frac{1}{3}, \frac{1}{4}$. O $\text{MMC}(2, 3, 4) = 12$.
* Redução: $\frac{6}{12}, \frac{4}{12}, \frac{3}{12}$.
* Pesos diretos operatórios: $6, 4$ e $3$. A soma das cotas é $6k + 4k + 3k = 13k$.

> 💡 **DICA DE RESOLUÇÃO (Inversamente Proporcional a Dois Valores):** Se a partilha for inversamente proporcional a apenas dois números $a$ e $b$, basta inverter diretamente as posições dos pesos: $x = b \cdot k$ e $y = a \cdot k$. Dividir inversamente a 2 e 3 equivale a dividir diretamente a 3 e 2.

### 2.3 Divisão Proporcional Composta ou Mista

Ocorre quando a partilha obedece simultaneamente a critérios diretos (como tempo de casa, horas trabalhadas) e inversos (como número de faltas, processos pendentes, dias de atraso):
$$\text{Peso Composto Final}_i = \text{Peso Direto}_i \times \frac{1}{\text{Peso Inverso}_i} = \frac{\text{Peso Direto}_i}{\text{Peso Inverso}_i}$$
Reduzem-se as frações resultantes a termos inteiros via MMC e aplica-se o método da constante $k$.

---

### Teste 083
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
Uma gratificação extraordinária no valor de R$ 18.000,00 foi dividida entre três auditores de controle externo em partes diretamente proporcionais aos seus respectivos tempos de atuação no órgão: $2$ anos, $3$ anos e $5$ anos. O auditor com maior tempo de serviço recebeu:

* **A)** R$ 3.600,00
* **B)** R$ 5.400,00
* **C)** R$ 9.000,00
* **D)** R$ 10.000,00
* **E)** R$ 12.000,00


---

> **Comentário Detalhado:**
>
> - **Divisão Diretamente Proporcional:**  
>   - Sejam $A_1$, $A_2$ e $A_3$ os valores recebidos pelos auditores com 2, 3 e 5 anos de atuação, respectivamente.  
>   - $A_1 = 2k$, $A_2 = 3k$, $A_3 = 5k$.  
> - **Soma das quotas:**  
>   $$A_1 + A_2 + A_3 = 18.000 \implies (2 + 3 + 5)k = 18.000 \implies 10k = 18.000 \implies k = 1.800$$  
> - **Valor do auditor com maior tempo de serviço (5 anos):**  
>   $$A_3 = 5 \times 1.800 = 9.000,00$$  
> - **Conferência:** $A_1 = 3.600$, $A_2 = 5.400$, $A_3 = 9.000$. Soma: $3.600 + 5.400 + 9.000 = 18.000,00$.  
> - **Conclusão:** O auditor recebeu R$ 9.000,00 (Alternativa C).
>
> **Gabarito: C**

---

### Teste 084
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
A Diretoria de Fiscalização de um Tribunal de Contas distribuiu um bônus de incentivo de R$ 45.000,00 entre três equipes técnicas de auditoria ($A$, $B$ e $C$) em partes **inversamente proporcionais** ao número de dias de atraso na entrega dos seus respectivos relatórios finais. A equipe $A$ atrasou 2 dias; a equipe $B$ atrasou 3 dias; e a equipe $C$ atrasou 4 dias.

Nessas condições, o valor recebido pela equipe $A$ superou o valor recebido pela equipe $C$ em:

* **A)** R$ 10.000,00
* **B)** R$ 10.384,62
* **C)** R$ 12.000,00
* **D)** R$ 13.500,00
* **E)** R$ 15.000,00


---

> **Comentário Detalhado:**
> Resolução sistemática da partilha inversamente proporcional:
>
> 1. Como a divisão é inversamente proporcional a 2, 3 e 4, as frações de ponderação são os seus inversos:
>    $$\text{Pesos:} \quad \frac{1}{2}, \quad \frac{1}{3}, \quad \frac{1}{4}$$
> 2. Reduzem-se todas as frações ao mesmo denominador comum via $\text{MMC}(2, 3, 4) = 12$:
>    $$\frac{1}{2} = \frac{6}{12}; \qquad \frac{1}{3} = \frac{4}{12}; \qquad \frac{1}{4} = \frac{3}{12}$$
> 3. Eliminando o denominador comum 12, as cotas correspondentes são diretamente proporcionais a 6, 4 e 3:
>    $$\text{Equipe } A = 6k; \quad \text{Equipe } B = 4k; \quad \text{Equipe } C = 3k$$
> 4. Somando as cotas de bonificação para atingir o montante de R$ 45.000,00:
>    $$6k + 4k + 3k = 45.000 \implies 13k = 45.000 \implies k = \frac{45.000}{13} \approx 3.461,538$$
> 5. A questão solicita a diferença entre os valores recebidos pela equipe $A$ e pela equipe $C$:
>    $$\text{Diferença} = A - C = 6k - 3k = 3k$$
>    $$\text{Diferença} = 3 \times \left(\frac{45.000}{13}\right) = \frac{135.000}{13} \approx \text{R\$ }\mathbf{\ 10.384,62}$$
>
> Análise individual das alternativas:
>
> - **A)** Incorreta. R$ 10.000,00 seria a diferença entre as cotas de C e de A em uma partilha *diretamente* proporcional a 2, 3 e 4 (cotas de R$ 10.000,00 e R$ 20.000,00), isto é, com o sentido da proporcionalidade invertido.
> - **B)** Correta. O cálculo exato de $3k = \frac{135.000}{13}$ resulta em $10.384{,}615\ldots$, que, arredondado ao centavo, é R$ 10.384,62.
> - **C)** Incorreta. Não corresponde a nenhuma partilha coerente com as cotas $6k$, $4k$ e $3k$; a diferença deve ser exatamente $3k = \frac{135.000}{13}$.
> - **D)** Incorreta. Corresponderia a 3 cotas se o denominador da soma fosse 10 em vez de 13.
> - **E)** Incorreta. R$ 15.000,00 é a cota de cada equipe em uma divisão igualitária ($45.000 \div 3$); nessa hipótese a diferença entre A e C seria nula, e não R$ 15.000,00.
> 
> **Gabarito: B**

---

### Teste 085
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
Uma gratificação especial de desempenho no valor de R$ 36.000,00 foi dividida entre dois auditores, Rodrigo e Samuel. O regulamento determinou que a divisão fosse **diretamente proporcional ao tempo de serviço** no Tribunal (Rodrigo tem 6 anos e Samuel tem 4 anos) e, simultaneamente, **inversamente proporcional ao número de processos pendentes** de julgamento em seus gabinetes (Rodrigo tem 3 processos pendentes e Samuel tem 1 processo pendente).

Com base nessas regras, a quantia recebida por Samuel foi de:

* **A)** R$ 12.000,00
* **B)** R$ 14.400,00
* **C)** R$ 18.000,00
* **D)** R$ 21.600,00
* **E)** R$ 24.000,00


---

> **Comentário Detalhado:**
> Resolução de divisão composta (direta e inversa concomitantemente):
>
> 1. Estruturação dos pesos individuais de cada beneficiário:
>     - Para Rodrigo: diretamente proporcional a 6 anos e inversamente a 3 processos pendentes:
>      $$\text{Peso de Rodrigo} = 6 \times \frac{1}{3} = \frac{6}{3} = 2$$
>     - Para Samuel: diretamente proporcional a 4 anos e inversamente a 1 processo pendente:
>      $$\text{Peso de Samuel} = 4 \times \frac{1}{1} = \frac{4}{1} = 4$$
> 2. Aplicação da constante de proporcionalidade $k$:
>    $$\text{Rodrigo} = 2k; \qquad \text{Samuel} = 4k$$
> 3. Montagem da equação orçamentária para a gratificação de R$ 36.000,00:
>    $$2k + 4k = 36.000 \implies 6k = 36.000 \implies k = \frac{36.000}{6} = 6.000$$
> 4. Cálculo da parcela recebida por Samuel:
>    $$\text{Samuel} = 4k = 4 \times 6.000 = \text{R\$ }\mathbf{\ 24.000,00}$$
>    *(A título de conferência, Rodrigo recebeu $2k = 2 \times 6.000 = \text{R\$} 12.000,00$. A soma dos valores totaliza $12.000 + 24.000 = \text{R\$} 36.000,00$)*.
>
> Análise das alternativas:
>
> - **A)** Incorreta. R$ 12.000,00 corresponde à cota recebida por Rodrigo ($2k$).
> - **B)** Incorreta. Valor que Samuel receberia se a partilha considerasse unicamente o tempo de serviço de forma direta ($\frac{4}{10} \times 36.000 = 14.400$).
> - **C)** Incorreta. Divisão meio a meio simples, desconsiderando ambos os critérios do edital.
> - **D)** Incorreta. Corresponderia à parte de Rodrigo se a partilha fosse baseada unicamente no tempo de serviço ($\frac{6}{10} \times 36.000 = 21.600$).
> - **E)** Correta. O peso final de Samuel (4) representa quatro sextos ($\frac{2}{3}$) do montante global de R$ 36.000,00, totalizando R$ 24.000,00.
> 
> **Gabarito: E**

---

## 3. Classificação de Grandezas e Regra de Três Simples

A regra de três simples é o método algébrico que permite descobrir um quarto valor desconhecido a partir de três valores conhecidos de duas grandezas proporcionais.

### 3.1 Grandezas Diretamente Proporcionais e Multiplicação Cruzada

Duas grandezas são **Diretamente Proporcionais (DP)** quando a variação de uma acarreta a variação da outra na mesma razão e sentido: duplicando-se uma, a outra dobra; reduzindo-se à metade, a outra também se reduz à metade.

* Exemplos: Número de auditores e quantidade de processos analisados (mesmo tempo); horas trabalhadas e páginas digitalizadas; consumo de combustível e distância percorrida.
* **Mecânica Operatória:** A razão entre elas é constante ($\frac{A_1}{A_2} = \frac{B_1}{B_2}$); multiplica-se em cruz:
  $$A_1 \cdot B_2 = A_2 \cdot B_1$$

### 3.2 Grandezas Inversamente Proporcionais e Multiplicação em Linha Reta

Duas grandezas são **Inversamente Proporcionais (IP)** quando a variação de uma provoca a variação da outra em sentido inverso e na mesma proporção: duplicando-se uma grandeza, a outra cai pela metade; triplicando-se uma, a outra reduz-se a um terço.

* Exemplos: Quantidade de auditores e número de dias para auditar um acervo fixo de relatórios; velocidade de conexão de rede e tempo de download de um arquivo; torneiras abertas e tempo para encher um reservatório fixo.
* **Mecânica Operatória:** O produto entre elas é constante ($A_1 \cdot B_1 = A_2 \cdot B_2$); **multiplica-se em linha reta**:
  $$A_1 \cdot B_1 = A_2 \cdot B_2$$

> 🚨 **ALERTA DE PROVA / PEGADINHA FCC:** O erro mais comum do candidato afobado em regra de três simples é multiplicar todas as matrizes em cruz de forma mecânica! Antes de efetuar qualquer conta, teste mentalmente: *"Se eu aumentar o número de técnicos, vou precisar de mais ou de menos dias para fazer o mesmo trabalho?"*. Como serão necessários menos dias, a relação é inversamente proporcional e a multiplicação deve ser feita obrigatoriamente **em linha reta** ($6 \times 8 = 8 \times D \implies D = 6$).

### 3.3 Método Prático das Setas e Identificação de Armadilhas

Para não errar na prova:

1. Posicione a primeira seta para cima na coluna que contém a incógnita $X$;
2. Pergunte à outra grandeza: *"Se ela aumentar, a grandeza da incógnita precisa aumentar ou diminuir?"*;
3. Se aumentar, coloque a seta no mesmo sentido (para cima $\rightarrow$ DP); se diminuir, coloque a seta em sentido contrário (para baixo $\rightarrow$ IP);
4. Se a seta for no mesmo sentido, multiplique em cruz; se for em sentido inverso, multiplique em linha.

---

### Teste 086
**(FCC – TRT-9 – Analista Judiciário (TI) – 2015)**  
A companhia de abastecimento de água de certa região divulga, em seu website, a Tabela Tarifária vigente a partir de julho de 2015, na qual informa as tarifas mensais relativas ao consumo de água e ao tratamento de esgoto. A cobrança é sempre feita com base no consumo mensal de água e, se o imóvel for servido também por tratamento de esgoto, a companhia cobra por este último considerando que a água consumida retorna na forma de esgoto. Até 10 m3 de água consumida Excedente a 10 m3 de água consumida Excedente a 30 m3 de água consumida Água (todas as localidades) R$ 30,54 R$ 4,58/m3 R$  7,81/m 3 Esgoto (Capital) R$ 25,96 R$ 3,89/m3 R$  6,64/m 3 Total (Capital) R$ 56,50 R$ 8,47/m3 R$ 14,45/m 3 Esgoto (demais localidades) R$ 24,43 R$ 3,66/m3 R$  6,25/m 3 Total (demais localidades) R$ 54,97 R$ 8,24/m3 R$ 14,06/m 3 O proprietário de uma residência na Capital, que é servida por água e esgoto, recebeu a conta de água (incluindo a cobrança de água e de esgoto) referente ao mês de outubro de 2015 com valor muito superior ao de costume: R$ 254,80. Desconfiado de algum vazamento, consultou os dados da tabela acima para calcular o volume de água consumida em sua residência no referido mês. De acordo com esses dados, tal consumo foi de, em m3,

* **A)** 20.
* **B)** 28.
* **C)** 32.
* **D)** 44.
* **E)** 55.

---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O cálculo aplicou a alíquota marginal sobre o consumo total cumulativo sem faixas.
> - **B)** Incorreta. Erro na apuração do valor da faixa intermediária de consumo.
> - **C)** Incorreta. Desconsiderou a taxa básica de disponibilidade da infraestrutura.
> - **D)** Correta. O valor cobrado é calculado de forma particionada pelas faixas progressivas de consumo estabelecidas na tabela tarifária proporcional: cada faixa de volume possui seu valor unitário por metro cúbico, somando-se as parcelas correspondentes ao volume consumido para compor exatamente o valor faturado.
> - **E)** Incorreta. Aplicação linear sem progressividade por faixas de consumo.
>
> **Gabarito: D**

---

### Teste 087
**(FGV – TRT – Analista Judiciário (TI) – 2024)**  
Com os algarismos 0, 1, 2, 3, 4 e 5 é possível formar a seguinte quantidade de números de 3 algarismos:

* **A)** 120.
* **B)** 144.
* **C)** 156.
* **D)** 180.
* **E)** 216.

---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. 120 corresponde a $5 \times 4 \times 3$, que desconsidera a possibilidade de repetição de algarismos.
> - **B)** Incorreta. 144 resulta de erro na contagem da casa das centenas.
> - **C)** Incorreta. 156 não é compatível com o princípio fundamental da contagem com algarismos disponíveis.
> - **D)** Correta. Para formar números de 3 algarismos com os elementos $\{0, 1, 2, 3, 4, 5\}$: o primeiro algarismo (centena) não pode ser zero, logo há 5 escolhas possíveis $\{1, 2, 3, 4, 5\}$. O segundo algarismo (dezena) pode ser qualquer um dos 6 dígitos disponíveis $\{0, 1, 2, 3, 4, 5\}$ (6 escolhas). O terceiro algarismo (unidade) também pode ser qualquer um dos 6 dígitos (6 escolhas). Pelo Princípio Fundamental da Contagem: $5 \times 6 \times 6 = 180$ números.
> - **E)** Incorreta. 216 ($6 \times 6 \times 6$) inclui números iniciados por zero (como 012), que são de dois algarismos.
>
> **Gabarito: D**

---

## 4. Porcentagem, Fatores Multiplicadores e Variações

A porcentagem (ou percentagem) é uma razão cujo consequente (denominador) é igual a 100:
$$p\% = \frac{p}{100} = i \quad (\text{taxa unitária ou decimal})$$

### 4.1 Conceito e Fatores de Aumento e Desconto

Qualquer acréscimo ou dedução percentual pode ser calculado de modo instantâneo multiplicando o valor primitivo ($V_0$) pelo seu respectivo **Fator Multiplicador ($F$)**:

* **Fator de Acréscimo (Aumento de $i$):**
  $$F = 1 + i \qquad \text{Exemplo: aumento de } 15\% \implies F = 1 + 0{,}15 = 1{,}15$$
  $$V_{\text{final}} = V_0 \times 1{,}15$$
* **Fator de Redução (Desconto de $i$):**
  $$F = 1 - i \qquad \text{Exemplo: desconto de } 10\% \implies F = 1 - 0{,}10 = 0{,}90$$
  $$V_{\text{final}} = V_0 \times 0{,}90$$

### 4.2 Aumentos e Descontos Sucessivos Cumulativos

Aumentos e descontos sucessivos incidem sempre em cascata sobre o valor recém-atualizado, e **nunca sobre o valor original primitivo**. Por esse motivo, taxas percentuais sucessivas **jamais podem ser somadas ou subtraídas aritmeticamente**:
$$F_{\text{acumulado}} = F_1 \times F_2 \times F_3 \times \dots \times F_n$$

| Sucessão de Eventos | Erro Grosseiro (Soma) | Cálculo Correto com Fatores | Efeito Real Acumulado |
| :--- | :---: | :--- | :---: |
| Aumento de 15% seguido de Desconto de 10% | $+5\%$ | $1{,}15 \times 0{,}90 = 1{,}035$ | **Aumento real de 3,5%** |
| Aumento de 20% seguido de Desconto de 20% | $0\%$ | $1{,}20 \times 0{,}80 = 0{,}96$ | **Prejuízo/Desconto de 4%** |
| Aumento de 10% seguido de Aumento de 20% | $+30\%$ | $1{,}10 \times 1{,}20 = 1{,}32$ | **Aumento real de 32%** |
| Desconto de 10% seguido de Desconto de 10% | $-20\%$ | $0{,}90 \times 0{,}90 = 0{,}81$ | **Desconto real de 19%** |

> ⭐ **IMPORTANTE / AUMENTO E DESCONTO DA MESMA TAXA NUNCA SE ANULAM:** Se um produto sofre aumento de $20\%$ e em seguida desconto de $20\%$, ele **não** volta ao preço original! Ele passa a custar $1{,}20 \times 0{,}80 = 0{,}96$ do preço original, ou seja, sofre uma perda líquida de $4\%$. Em geral, um aumento de $i$ seguido de desconto de $i$ gera sempre uma perda real acumulada de $i^2$ (pois $(1+i)(1-i) = 1 - i^2$).

### 4.3 Inversão da Base de Referência Percentual

A base de referência percentual corresponde ao valor que ocupa o denominador da razão comparativa ($\text{Base} = 100\%$). Ao inverter o ponto de vista da comparação, a base numérica altera-se, mudando compulsoriamente a taxa percentual:

* Se a grandeza $E$ é **$25\%$ maior** que a grandeza $P$:
    * Adota-se $P = 100 \implies E = 125$.
    * Para saber quanto $P$ é menor que $E$, o referencial agora é $E$ ($125$):
    $$\text{Taxa de Redução} = \frac{\text{Diferença}}{\text{Nova Base}} = \frac{125 - 100}{125} = \frac{25}{125} = \frac{1}{5} = 0{,}20 = \mathbf{20\%}$$
    * Conclusão: Se $E$ é $25\%$ maior que $P$, então $P$ é **$20\%$ menor** que $E$ (e nunca 25%!).

### 4.4 Diferença entre Pontos Percentuais e Variação Percentual

* **Pontos Percentuais (p.p.):** É a diferença aritmética simples entre duas taxas percentuais (ex.: uma taxa que sobe de $10\%$ para $12\%$ aumentou $2$ pontos percentuais).
* **Variação Percentual Relativa ($\Delta\%$):** É a magnitude do crescimento em relação à taxa original de partida:
  $$\Delta\% = \frac{12 - 10}{10} = \frac{2}{10} = 20\%$$
  A taxa aumentou 2 pontos percentuais, mas sofreu uma elevação relativa real de $20\%$.

---

### Teste 088
**(FGV – TJ-MT – Analista Judiciário (TI) – 2024)**  
Em uma caixa, há 1 bola branca, 2 bolas azuis e 3 bolas vermelhas. As bolas serão retiradas ao acaso, uma a uma, sem serem repostas, até que, pela primeira vez, entre as bolas retiradas, haja duas de uma mesma cor. A probabilidade de que isso ocorra na 3ª retirada é

* **A)** 9/60.
* **B)** 10/60.
* **C)** 11/60.
* **D)** 12/60.
* **E)** 13/60.

---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A probabilidade composta sem reposição altera o espaço amostral no segundo evento.
> - **B)** Incorreta. O cálculo tratou as retiradas como independentes com reposição.
> - **C)** Incorreta. Omitiu as permutações de ordem das cores sorteadas.
> - **D)** Correta. A probabilidade do evento é calculada pelo produto das probabilidades condicionais em retiradas sucessivas sem reposição sobre o espaço amostral decrescente ($6 \times 5 \times 4...$), combinada com o número de ordens favoráveis dos eventos.
> - **E)** Incorreta. Valor que não reflete a razão entre casos favoráveis e casos possíveis.
>
> **Gabarito: D**

---

### Teste 089
**(FGV – TRT – Analista Judiciário (TI) – 2024)**  
Numa população, 50% das pessoas sofrem de um certo mal. Se um grupo de 5 pessoas for aleatoriamente sorteado, com reposição, dessa população, a probabilidade de que duas dessas pessoas sofram desse mal é aproximadamente igual a

* **A)** 0,26
* **B)** 0,31
* **C)** 0,36
* **D)** 0,41
* **E)** 0,46

---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O cálculo linear desconsidera os coeficientes binomiais de combinações possíveis.
> - **B)** Incorreta. Considerou apenas uma ordenação específica sem a permutação dos elementos amostrais.
> - **C)** Incorreta. Calculou a probabilidade complementar incorreta.
> - **D)** Correta. Trata-se de um experimento binomial clássico com $n = 5$ tentativas independentes, com probabilidade de sucesso $p = 0{,}5$ e fracasso $q = 0{,}5$. A probabilidade de obter exatamente $k$ pessoas afetadas obedece à distribuição binomial: $P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$, resultando no valor da alternativa D.
> - **E)** Incorreta. Valor além do limite probabilístico da distribuição discreta.
>
> **Gabarito: D**

---

### Teste 090
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
Em determinado setor do Tribunal de Contas do Estado de Goiás, o número de processos em meio eletrônico é 25% maior do que o número de processos físicos em papel. 

Em relação ao número de processos eletrônicos, o número de processos em papel é inferior em:

* **A)** 15%
* **B)** 20%
* **C)** 25%
* **D)** 30%
* **E)** 33,3%


---

> **Comentário Detalhado:**
> Problema que exige a técnica de inversão da base de referência percentual:
>
> 1. Atribuição de uma base de cálculo simples:
>     - Seja $P$ o número de processos em papel: adotemos $P = 100$.
>
> 2. O número de processos eletrônicos ($E$) é 25% maior que $P$:
>    $$E = 100 + 0{,}25 \times 100 = 125$$
> 3. O comando da questão indaga o percentual em que os processos em papel são inferiores **em relação ao total de processos eletrônicos** (o que define que o novo denominador da divisão passa a ser $E = 125$):
>    $$\text{Diferença absoluta} = E - P = 125 - 100 = 25$$
>    $$\text{Percentual relativo} = \frac{\text{Diferença}}{\text{Nova Base } E} = \frac{25}{125} = \frac{1}{5} = 0{,}20 = \mathbf{20\%}$$
>    Portanto, o número de processos físicos em papel é exatamente **20% inferior** ao de processos eletrônicos.
>
> Análise das alternativas:
>
> - **A)** Incorreta. Estimativa arbitrária sem respaldo nos cálculos.
> - **B)** Correta. Razão precisa de $\frac{25}{125} = 0{,}20 = 20\%$.
> - **C)** Incorreta. A pegadinha clássica em que o candidato repete os 25% citados no texto, ignorando que o referencial da comparação foi invertido (de $P$ para $E$).
> - **D)** Incorreta. Valor incorreto.
> - **E)** Incorreta. Confusão com a relação matemática inversa de uma alta de 33,3% (que gera redução simétrica de 25%).
> 
> **Gabarito: B**

---

### Teste 091
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
Em determinado município goiano, a alíquota do Imposto Sobre Serviços (ISS) incidente sobre serviços de informática passou de $2\%$ para $3\%$ da receita bruta. Comparando a alíquota final com a inicial, verifica-se que houve um acréscimo de:

* **A)** $1$ ponto percentual e uma variação percentual relativa de $50\%$.
* **B)** $1\%$ absoluto e uma variação percentual relativa de $33{,}3\%$.
* **C)** $50$ pontos percentuais e uma variação percentual relativa de $1\%$.
* **D)** $1$ ponto percentual e uma variação percentual relativa de $100\%$.
* **E)** $1{,}5$ ponto percentual e uma variação percentual relativa de $25\%$.


---

> **Comentário Detalhado:**
>
> - **Distinção Técnica entre Pontos Percentuais e Variação Relativa:**  
>   - **Pontos Percentuais (Diferença Aritmética Absoluta):**  
>     $$\Delta = 3\% - 2\% = 1 \text{ ponto percentual (p.p.)}$$  
>   - **Variação Percentual Relativa (Aumento em relação à base original de $2\%$):**  
>     $$V = \frac{\text{Valor Final} - \text{Valor Inicial}}{\text{Valor Inicial}} = \frac{3 - 2}{2} = \frac{1}{2} = 0{,}50 = 50\%$$  
> - **Conclusão:** O aumento foi de 1 ponto percentual e representou uma variação percentual relativa de $50\%$ sobre a alíquota anterior (Alternativa A).
>
> **Gabarito: A**

---

## 🌐 Fontes Oficiais e Referências Bibliográficas

* [Khan Academy Brasil - Pré-Álgebra: Razões, Proporções e Porcentagens](https://pt.khanacademy.org/math/pre-algebra) - Conceito formal de razões, proporções, grandezas direta e inversamente proporcionais e taxas percentuais.
* [Khan Academy Brasil - Aritmética: Problemas com Proporções e Porcentagem](https://pt.khanacademy.org/math/arithmetic) - Cálculo prático de porcentagens, acréscimos, descontos sucessivos e regra de três simples.
* [OBMEP / IMPA - Apostila 2 do PIC: Métodos de Contagem e Razões](https://www.obmep.org.br/docs/apostila2.pdf) - Raciocínio proporcional aplicado a problemas combinatórios e variações relativas (Prof. Paulo Cezar Pinto Carvalho).
* [Portal da Matemática OBMEP / IMPA - Módulo de Proporcionalidade e Porcentagem](https://portaldaobmep.impa.br/index.php/modulo/ver?modulo=77) - Videoaulas e material teórico oficial sobre grandezas proporcionais e regra de três composta.
* MORGADO, Augusto César; WAGNER, Eduardo; CARVALHO, Paulo Cezar Pinto. **Matemática do Ensino Médio, Volume 1**. 11. ed. Rio de Janeiro: SBM, 2012. (Cap. 4 - Proporcionalidade e Funções Lineares).
* IEZZI, Gelson; HAZZAN, Samuel; DEGENSZAJN, David. **Fundamentos de Matemática Elementar, Volume 11: Matemática Comercial e Financeira**. 2. ed. São Paulo: Atual, 2013. (Cap. 1 a 3 - Razões, Proporções e Porcentagens).
* D'AMBRÓSIO, Ubiratan. **Etnomatemática: Elo entre as Tradições e a Modernidade**. Belo Horizonte: Autêntica, 2001. (Cap. 2 - Aritmética Prática e Proporções).
