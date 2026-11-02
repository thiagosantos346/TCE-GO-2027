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
**(FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo - Administração)**
A figura a seguir mostra 5 círculos cuja união é formada por 10 regiões disjuntas. Cada região possui um número e a figura mostra os números de três regiões vizinhas. Sabe-se que: • a soma dos três números contidos em cada círculo é 20; • os números das outras sete regiões são: 3, 4, 5, 6, 8, 9, 11, sendo um número em cada região. O número 𝑥 da figura acima é

* **A)** 2.
* **B)** 3.
* **C)** 4.
* **D)** 6.
* **E)** 11.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "2". De acordo com a teoria estudada em *1.1 Conceito de Razão e Grandezas Comensuráveis*, razão: Dados dois números reais $a$ e $b$ (com $b \neq 0$), a razão entre $a$ e $b$ (nesta ordem) é o quociente indicado pela divisão.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "3". De acordo com a teoria estudada em *1.3 Propriedade da Soma dos Termos e Constante de Proporcionalidade*, em uma série de razões iguais, a soma dos antecedentes dividida pela soma dos consequentes é igual a qualquer uma das razões primitivas, correspondendo à constante de proporcionalidade $k$.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "4". De acordo com a teoria estudada em *1.3 Propriedade da Soma dos Termos e Constante de Proporcionalidade*, $$\frac{a}{b} = \frac{c}{d} = \frac{e}{f} = k \implies \frac{a + c + e}{b + d + f} = k$$.
> - **D)** **Correta.** Conforme fundamentado na seção *3.2 Grandezas Inversamente Proporcionais e Multiplicação em Linha Reta* deste guia, o erro mais comum do candidato afobado em regra de três simples é multiplicar todas as matrizes em cruz de forma mecânica! Antes de efetuar qualquer conta, teste mentalmente: *"Se eu aumentar o número de técnicos, vou precisar de mais ou de menos dias para fazer o mesmo trabalho?"*. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "6".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "11". De acordo com a teoria estudada em *1.3 Propriedade da Soma dos Termos e Constante de Proporcionalidade*, essa propriedade é a base algébrica definitiva para solucionar repartições orçamentárias e partilhas de bens em auditoria sem necessidade de recorrer a sistemas lineares extensos.
>
> **Gabarito: D**

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
**(FGV – TRT 16ª – 2022 – Analista Judiciário (Área Administrativa - Tecnologia da Informação))**
Um terreno de 1280 m2 foi dividido em 3 partes, proporcionais aos números: 2, 5/2 e 7/2. A área da maior parte, em m2, é

* **A)** 400.
* **B)** 440.
* **C)** 480.
* **D)** 520.
* **E)** 560.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "400". De acordo com a teoria estudada em *2.1 Divisão Diretamente Proporcional com a Constante k*, repartir um total $V$ em partes $x, y, z$ diretamente proporcionais aos pesos $a, b, c$.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "440". De acordo com a teoria estudada em *2.2 Divisão Inversamente Proporcional e o Método do MMC*, repartir um montante $V$ em partes $x, y, z$ inversamente proporcionais aos coeficientes $a, b, c$ significa repartir diretamente aos seus inversos $\frac{1}{a}, \frac{1}{b}, \frac{1}{c}$.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "480". De acordo com a teoria estudada em *2.1 Divisão Diretamente Proporcional com a Constante k*, cada parte individual é calculada multiplicando $k$ pelo peso do beneficiário.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "520". De acordo com a teoria estudada em *O Método Rápido do MMC:*, se a partilha for inversamente proporcional a apenas dois números $a$ e $b$, basta inverter diretamente as posições dos pesos: $x = b \cdot k$ e $y = a \cdot k$. Dividir inversamente a 2 e 3 equivale a dividir diretamente a 3 e 2.
> - **E)** **Correta.** Conforme fundamentado na seção *2. Divisão em Partes Proporcionais* deste guia, a partilha proporcional consiste em distribuir uma quantia total $V$ entre vários beneficiários ou centros de custo em conformidade com critérios predeterminados de mérito, produtividade ou penalidade. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT 16ª/2022) ao estabelecer que "560".
>
> **Gabarito: E**

---

### Teste 084
**(FCC – TRT 1ª – 2014 – Analista Judiciário - Tecnologia da Informação)**
Em relação a dispositivos de memória e armazenamento presentes em um computador típico, dispositivos caracterizados como memória principal são, APENAS,

* **A)** consomem mais energia do que os HDs.
* **B)** possuem custo inferior ao dos HDs.
* **C)** não possuem partes mecânicas como os HDs.
* **D)** possuem tempo de acesso equivalente ao tempo de acesso dos HDs.
* **E)** utilizam memória RAM.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "consomem mais energia do que os HDs". De acordo com a teoria estudada em *1.2 Proporções e a Propriedade Fundamental*, uma proporção é formalmente definida como a igualdade matemática entre duas ou mais razões equivalentes.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "possuem custo inferior ao dos HDs". De acordo com a teoria estudada em *2. Divisão em Partes Proporcionais*, a partilha proporcional consiste em distribuir uma quantia total $V$ entre vários beneficiários ou centros de custo em conformidade com critérios predeterminados de mérito, produtividade ou penalidade.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "não possuem partes mecânicas como os HDs". De acordo com a teoria estudada em *1.1 Conceito de Razão e Grandezas Comensuráveis*, quando as grandezas possuem a mesma unidade de medida (ex.: metros por metros, reais por reais), a razão é uma grandeza adimensional pura.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "possuem tempo de acesso equivalente ao tempo de acesso dos HDs". De acordo com a teoria estudada em *2.3 Divisão Proporcional Composta ou Mista*, ocorre quando a partilha obedece simultaneamente a critérios diretos (como tempo de casa, horas trabalhadas) e inversos (como número de faltas, processos pendentes, dias de atraso).
> - **E)** **Correta.** Conforme fundamentado na seção *O Método Rápido do MMC:* deste guia, despreza-se o denominador comum e utilizam-se os novos numeradores inteiros como os pesos diretos para a constante $k$. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 1ª/2014) ao estabelecer que "utilizam memória RAM".
>
> **Gabarito: E**

---

### Teste 085
**(FGV – TRT da 24º Região – 2025 – Analista Judiciário - Área Administrativa - Contabilidade)**
Em 31/12/2022, uma sociedade empresária apresentava os seguintes saldos em seu balanço patrimonial:  Disponibilidades: R$100.000,00.  Patrimônio Líquido: R$100.000,00. Em 01/01/2023, essa sociedade empresária pagou, antecipadamente, o aluguel de três anos de seu escritório. A sociedade empresária utilizava, internamente, o regime de caixa. Em 2024, ela decidiu utilizar o regime de competência, apenas. Ao reapresentar o balanço patrimonial corrigido de 31/12/2023, assinale a opção que indica um impacto que pode ser observado pela mudança de regime.

* **A)** Aumento do ativo e do passivo.
* **B)** Diminuição do ativo e do passivo.
* **C)** Aumento do ativo e do patrimônio líquido.
* **D)** Diminuição do passivo e aumento no patrimônio líquido.
* **E)** Aumento do passivo e diminuição no patrimônio líquido.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Aumento do ativo e do passivo". De acordo com a teoria estudada em *4.1 Conceito e Fatores de Aumento e Desconto*, $$F = 1 + i \qquad \text{Exemplo: aumento de } 15\% \implies F = 1 + 0{,}15 = 1{,}15$$.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Diminuição do ativo e do passivo". De acordo com a teoria estudada em *4.1 Conceito e Fatores de Aumento e Desconto*, $$V_{\text{final}} = V_0 \times 1{,}15$$.
> - **C)** **Correta.** Conforme fundamentado na seção *4.1 Conceito e Fatores de Aumento e Desconto* deste guia, qualquer acréscimo ou dedução percentual pode ser calculado de modo instantâneo multiplicando o valor primitivo ($V_0$) pelo seu respectivo Fator Multiplicador ($F$). Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT da 24º Região/2025) ao estabelecer que "Aumento do ativo e do patrimônio líquido".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Diminuição do passivo e aumento no patrimônio líquido". De acordo com a teoria estudada em *4.1 Conceito e Fatores de Aumento e Desconto*, $$F = 1 - i \qquad \text{Exemplo: desconto de } 10\% \implies F = 1 - 0{,}10 = 0{,}90$$.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Aumento do passivo e diminuição no patrimônio líquido". De acordo com a teoria estudada em *4.1 Conceito e Fatores de Aumento e Desconto*, $$V_{\text{final}} = V_0 \times 0{,}90$$.
>
> **Gabarito: C**

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
**(FCC – TRT 24ª – 2017 – Analista Judiciário - Tecnologia da Informação)**
Uma sequência pode ser criada com a seguinte regra: escolhe-se um número natural maior que 100, para ser o primeiro termo dessa sequência. Se o termo da sequência é um número natural PAR, o termo seguinte deverá ser a metade desse número PAR; se o termo da sequência for um número natural ÍMPAR, deve-se somar 13 a esse número ÍMPAR e em seguida calcular a metade dessa soma para obter o termo seguinte. Segue um exemplo: se um termo da sequência é o número 137, que é ÍMPAR, o termo seguinte será 75, que é a metade da soma entre 137 e 13. O 8o termo de uma sequência, criada com essa regra e com termo inicial igual a 4855, é

* **A)** 49
* **B)** 93
* **C)** 35
* **D)** 75
* **E)** 118

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "49". De acordo com a teoria estudada em *3.2 Grandezas Inversamente Proporcionais e Multiplicação em Linha Reta*, o erro mais comum do candidato afobado em regra de três simples é multiplicar todas as matrizes em cruz de forma mecânica! Antes de efetuar qualquer conta, teste mentalmente: *"Se eu aumentar o número de técnicos, vou precisar de mais ou de menos dias para fazer o mesmo trabalho?"*.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "93". De acordo com a teoria estudada em *1.1 Conceito de Razão e Grandezas Comensuráveis*, o primeiro termo $a$ denomina-se antecedente e o segundo termo $b$ é o consequente.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "35". De acordo com a teoria estudada em *4.1 Conceito e Fatores de Aumento e Desconto*, qualquer acréscimo ou dedução percentual pode ser calculado de modo instantâneo multiplicando o valor primitivo ($V_0$) pelo seu respectivo Fator Multiplicador ($F$).
> - **D)** **Correta.** Conforme fundamentado na seção *3.2 Grandezas Inversamente Proporcionais e Multiplicação em Linha Reta* deste guia, como serão necessários menos dias, a relação é inversamente proporcional e a multiplicação deve ser feita obrigatoriamente em linha reta ($6 \times 8 = 8 \times D \implies D = 6$). Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 24ª/2017) ao estabelecer que "75".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "118". De acordo com a teoria estudada em *4. Porcentagem, Fatores Multiplicadores e Variações*, a porcentagem (ou percentagem) é uma razão cujo consequente (denominador) é igual a 100.
>
> **Gabarito: D**

---

### Teste 087
**(FGV – TRT/DA – 2025 – Analista Judiciario Area Apoio Especializado Tecnologia Da Informacao)**
O analista Raimundo sabe que a indução de árvores de decisão é uma das formas mais simples, e ainda assim mais bem sucedidas, de aprendizagem de máquina. No entanto, ao aplicá-la em alguns problemas da empresa em que atua, o algoritmo de aprendizagem-em-árvore-de-decisão gera uma grande árvore quando realmente não há padrão a ser encontrado nos dados. O nome do problema encontrado por Raimundo é

* **A)** suposição de estacionaridade.
* **B)** poda de árvore de decisão.
* **C)** superadaptação.
* **D)** hipótese nula.
* **E)** hiperárvore.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "suposição de estacionaridade". De acordo com a teoria estudada em *3. Classificação de Grandezas e Regra de Três Simples*, a regra de três simples é o método algébrico que permite descobrir um quarto valor desconhecido a partir de três valores conhecidos de duas grandezas proporcionais.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "poda de árvore de decisão". De acordo com a teoria estudada em *3.2 Grandezas Inversamente Proporcionais e Multiplicação em Linha Reta*, como serão necessários menos dias, a relação é inversamente proporcional e a multiplicação deve ser feita obrigatoriamente em linha reta ($6 \times 8 = 8 \times D \implies D = 6$).
> - **C)** **Correta.** Conforme fundamentado na seção *3.2 Grandezas Inversamente Proporcionais e Multiplicação em Linha Reta* deste guia, o erro mais comum do candidato afobado em regra de três simples é multiplicar todas as matrizes em cruz de forma mecânica! Antes de efetuar qualquer conta, teste mentalmente: *"Se eu aumentar o número de técnicos, vou precisar de mais ou de menos dias para fazer o mesmo trabalho?"*. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT/DA/2025) ao estabelecer que "superadaptação".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "hipótese nula". De acordo com a teoria estudada em *1.1 Conceito de Razão e Grandezas Comensuráveis*, razão: Dados dois números reais $a$ e $b$ (com $b \neq 0$), a razão entre $a$ e $b$ (nesta ordem) é o quociente indicado pela divisão.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "hiperárvore". De acordo com a teoria estudada em *1.2 Proporções e a Propriedade Fundamental*, $$\frac{a}{b} = \frac{c}{d} \quad \text{lê-se: 'a está para b assim como c está para d'}$$.
>
> **Gabarito: C**

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
**(FGV – TJ/BA – 2015 – Analista Judiciario Tecnologia Da Informacao)**
No texto 1, a palavra “bem-intencionada” aparece grafada com hífen; o Novo Acordo Ortográfico diz que “Nas palavras em que o primeiro elemento é bem-, a regra geral é o emprego do hífen, não importando se o segundo elemento começa por vogal ou consoante”. Sobre esse caso, a afirmação correta é:

* **A)** a palavra foi mal grafada, pois deve ser escrita sem hífen;
* **B)** a palavra foi bem grafada já que se trata da junção de um advérbio de modo + adjetivo;
* **C)** a palavra foi bem grafada, pois se trata de um adjetivo composto com um elemento de valor prefixal;
* **D)** a palavra foi mal grafada, visto que não se trata de um vocábulo, mas de dois;
* **E)** a palavra foi bem grafada, pois houve mudanças nesse emprego, com as novas regras. Texto 2 - “A saga do rapto de Helena e a subsequente Guerra de Troia continuam sendo um dos melhores exemplos dos perigos da luxúria. No todo, a história sugere quão imprudente é para um hóspede na casa de um homem levar consigo, ao partir, a esposa do anfitrião. Acrescentamos a esse erro crasso a dupla idiotice da raiva e da inveja, agravadas quando o marido abandonado, Menelau, insistiu nos direitos de um velho tratado e arrastou todo o seu reino e os dos vizinhos em missão de vingança. Muitos deles demoraram quase vinte anos na guerra e no retorno, para não falar na maioria que morreu, deixando os lares e as famílias no desamparo e na ruína – mal sobrevivendo, sugerem os registros, a assédios diversos e a desastres naturais.” (Menelau e a esposa perdida, Stephen Weir)

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "a palavra foi mal grafada, pois deve ser escrita sem hífen". De acordo com a teoria estudada em *3.2 Grandezas Inversamente Proporcionais e Multiplicação em Linha Reta*, como serão necessários menos dias, a relação é inversamente proporcional e a multiplicação deve ser feita obrigatoriamente em linha reta ($6 \times 8 = 8 \times D \implies D = 6$).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "a palavra foi bem grafada já que se trata da junção de um advérbio de modo + adjetivo". De acordo com a teoria estudada em *4.1 Conceito e Fatores de Aumento e Desconto*, qualquer acréscimo ou dedução percentual pode ser calculado de modo instantâneo multiplicando o valor primitivo ($V_0$) pelo seu respectivo Fator Multiplicador ($F$).
> - **C)** **Correta.** Conforme fundamentado na seção *4.2 Aumentos e Descontos Sucessivos Cumulativos* deste guia, em geral, um aumento de $i$ seguido de desconto de $i$ gera sempre uma perda real acumulada de $i^2$ (pois $(1+i)(1-i) = 1 - i^2$). Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/BA/2015) ao estabelecer que "a palavra foi bem grafada, pois se trata de um adjetivo composto com um elemento de valor prefixal".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "a palavra foi mal grafada, visto que não se trata de um vocábulo, mas de dois". De acordo com a teoria estudada em *3. Classificação de Grandezas e Regra de Três Simples*, a regra de três simples é o método algébrico que permite descobrir um quarto valor desconhecido a partir de três valores conhecidos de duas grandezas proporcionais.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "a palavra foi bem grafada, pois houve mudanças nesse emprego, com as novas regras. Texto 2 - “A saga do rapto de...". De acordo com a teoria estudada em *3.2 Grandezas Inversamente Proporcionais e Multiplicação em Linha Reta*, o erro mais comum do candidato afobado em regra de três simples é multiplicar todas as matrizes em cruz de forma mecânica! Antes de efetuar qualquer conta, teste mentalmente: *"Se eu aumentar o número de técnicos, vou precisar de mais ou de menos dias para fazer o mesmo trabalho?"*.
>
> **Gabarito: C**

---

### Teste 089
**(FCC – TRT 4ª – 2015 – Analista Judiciário - Tecnologia Da Informação)**
A quantidade de cartuchos de impressora distribuídos mensalmente para os três escritórios (P, Q e R) de uma empresa é diretamente proporcional ao número de impressoras de cada escritório. Sabe-se que P possui três impressoras a mais do que o dobro das impressoras de Q; e que R possui o dobro das impressoras de P. Nessas condições, a quantidade total mensal de cartuchos distribuídos para os três escritórios juntos é um número que, na divisão por 7, deixa resto igual a

* **A)** 4.
* **B)** 6.
* **C)** 5.
* **D)** 2.
* **E)** 3.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "4". De acordo com a teoria estudada em *2.1 Divisão Diretamente Proporcional com a Constante k*, repartir um total $V$ em partes $x, y, z$ diretamente proporcionais aos pesos $a, b, c$.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "6". De acordo com a teoria estudada em *3.1 Grandezas Diretamente Proporcionais e Multiplicação Cruzada*, exemplos: Número de auditores e quantidade de processos analisados (mesmo tempo); horas trabalhadas e páginas digitalizadas; consumo de combustível e distância percorrida.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "5". De acordo com a teoria estudada em *2. Divisão em Partes Proporcionais*, a partilha proporcional consiste em distribuir uma quantia total $V$ entre vários beneficiários ou centros de custo em conformidade com critérios predeterminados de mérito, produtividade ou penalidade.
> - **D)** **Correta.** Conforme fundamentado na seção *3.2 Grandezas Inversamente Proporcionais e Multiplicação em Linha Reta* deste guia, o erro mais comum do candidato afobado em regra de três simples é multiplicar todas as matrizes em cruz de forma mecânica! Antes de efetuar qualquer conta, teste mentalmente: *"Se eu aumentar o número de técnicos, vou precisar de mais ou de menos dias para fazer o mesmo trabalho?"*. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 4ª/2015) ao estabelecer que "2".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "3". De acordo com a teoria estudada em *2.3 Divisão Proporcional Composta ou Mista*, ocorre quando a partilha obedece simultaneamente a critérios diretos (como tempo de casa, horas trabalhadas) e inversos (como número de faltas, processos pendentes, dias de atraso).
>
> **Gabarito: D**

---

### Teste 090
**(CEBRASPE – TJ/DFT – 2015 – Analista Judiciario Suporte Em Tecnologia Da Informacao)**
As partes A e B compartilham a mesma chave criptográfica, também denominada chave secreta.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Correta.** O item está **Certo**. Conforme fundamentado na seção *1.1 Conceito de Razão e Grandezas Comensuráveis* deste guia, quando as grandezas possuem a mesma unidade de medida (ex.: metros por metros, reais por reais), a razão é uma grandeza adimensional pura. Dessa forma, está plenamente correta a proposição da banca (CEBRASPE – TJ/DFT/2015) ao afirmar que "As partes A e B compartilham a mesma chave criptográfica, também denominada chave secreta".
> - **E)** **Incorreta.** A marcação como **Errado** não procede, visto que a assertiva guarda integral conformidade com a teoria estudada em *3.1 Grandezas Diretamente Proporcionais e Multiplicação Cruzada*, segundo a qual duas grandezas são Diretamente Proporcionais (DP) quando a variação de uma acarreta a variação da outra na mesma razão e sentido: duplicando-se uma, a outra dobra; reduzindo-se à metade, a outra também se reduz à metade.
>
> **Gabarito: C**

---

### Teste 091
**(FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo - Direito)**
João da Silva ajuizou ação em face do Instituto Nacional do Seguro Social (INSS), autarquia federal vinculada à União, postulando a concessão de benefício de aposentadoria por incapacidade permanente, com pagamento das prestações em atraso desde a data do requerimento administrativo indeferido. A sentença julgou o pedido procedente, fixando como termo inicial o mês do requerimento administrativo, estabelecendo a renda mensal inicial do benefício com base no salário de benefício já apurado pelo INSS e determinando a incidência de correção monetária e juros de mora conforme os índices legalmente previstos. A condenação em parcelas atrasadas, apurável mediante simples cálculos aritméticos com base nos parâmetros da sentença, estimava-se em aproximadamente 380 salários-mínimos, não havendo necessidade de liquidação autônoma ou atividade cognitiva complementar para sua quantificação. O INSS, em sede de impugnação ao cumprimento de sentença promovido por João da Silva, sustentou que a sentença deveria ter sido submetida ao duplo grau obrigatório de jurisdição por força da remessa necessária. Considerando o disposto na legislação processual civil e o entendimento fixado pelo Superior Tribunal de Justiça sob o regime dos recursos repetitivos, é correto afirmar que a sentença em referência

* **A)** não está sujeita à remessa necessária, pois a condenação imposta ao INSS não ultrapassa 500 salários-mínimos, limite a partir do qual a remessa necessária é exigível nas demandas que envolvam autarquias federais, nos termos do art. 496, § 3º, I, do CPC/2015.
* **B)** está sujeita à remessa necessária, uma vez que o valor da condenação supera 100 salários-mínimos, limite a partir do qual a remessa necessária é exigível nas demandas que envolvam autarquias federais, nos termos do art. 496, § 3º, I, do CPC/2015.
* **C)** está sujeita à remessa necessária, pois as condenações impostas ao INSS em demandas previdenciárias são, por sua própria natureza, materialmente ilíquidas, pois dependem da aferição de competências, salários de contribuição e índices de atualização variáveis, razão pela qual se submetem invariavelmente à remessa necessária.
* **D)** não está sujeita à remessa necessária, pois, havendo parâmetros suficientes fixados no decisum que permitam a apuração imediata da condenação por simples cálculos aritméticos, e sendo possível estimar que o valor não excederá o limite de 1.000 salários-mínimos previsto no art. 496, § 3º, I, do CPC/2015, resta afastado o duplo grau obrigatório de jurisdição.
* **E)** não está sujeita à remessa necessária, pelo fato de o valor da condenação ser inferior ao limite estabelecido no art. 496, § 3º, I, do CPC/2015, sendo irrelevante, para esse fim, a análise da complexidade exigida na fase de liquidação ou a existência de parâmetros suficientes na sentença para a apuração do quantum debeatur.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "não está sujeita à remessa necessária, pois a condenação imposta ao INSS não ultrapassa 500 salários-mínimos...". De acordo com a teoria estudada em *4.3 Inversão da Base de Referência Percentual*, a base de referência percentual corresponde ao valor que ocupa o denominador da razão comparativa ($\text{Base} = 100\%$). Ao inverter o ponto de vista da comparação, a base numérica altera-se, mudando compulsoriamente a taxa percentual.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "está sujeita à remessa necessária, uma vez que o valor da condenação supera 100 salários-mínimos, limite a partir...". De acordo com a teoria estudada em *4.3 Inversão da Base de Referência Percentual*, $$\text{Taxa de Redução} = \frac{\text{Diferença}}{\text{Nova Base}} = \frac{125 - 100}{125} = \frac{25}{125} = \frac{1}{5} = 0{,}20 = \mathbf{20\%}$$.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "está sujeita à remessa necessária, pois as condenações impostas ao INSS em demandas previdenciárias são, por sua...". De acordo com a teoria estudada em *4.4 Diferença entre Pontos Percentuais e Variação Percentual*, pontos Percentuais (p.p.): É a diferença aritmética simples entre duas taxas percentuais (ex.: uma taxa que sobe de $10\%$ para $12\%$ aumentou $2$ pontos percentuais).
> - **D)** **Correta.** Conforme fundamentado na seção *3. Classificação de Grandezas e Regra de Três Simples* deste guia, a regra de três simples é o método algébrico que permite descobrir um quarto valor desconhecido a partir de três valores conhecidos de duas grandezas proporcionais. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "não está sujeita à remessa necessária, pois, havendo parâmetros suficientes fixados no decisum que permitam a...".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "não está sujeita à remessa necessária, pelo fato de o valor da condenação ser inferior ao limite estabelecido no...". De acordo com a teoria estudada em *4.1 Conceito e Fatores de Aumento e Desconto*, qualquer acréscimo ou dedução percentual pode ser calculado de modo instantâneo multiplicando o valor primitivo ($V_0$) pelo seu respectivo Fator Multiplicador ($F$).
>
> **Gabarito: D**

---

## 🌐 Fontes Oficiais e Referências Bibliográficas

* [Khan Academy Brasil - Pré-Álgebra: Razões, Proporções e Porcentagens](https://pt.khanacademy.org/math/pre-algebra) - Conceito formal de razões, proporções, grandezas direta e inversamente proporcionais e taxas percentuais.
* [Khan Academy Brasil - Aritmética: Problemas com Proporções e Porcentagem](https://pt.khanacademy.org/math/arithmetic) - Cálculo prático de porcentagens, acréscimos, descontos sucessivos e regra de três simples.
* [OBMEP / IMPA - Apostila 2 do PIC: Métodos de Contagem e Razões](https://www.obmep.org.br/docs/apostila2.pdf) - Raciocínio proporcional aplicado a problemas combinatórios e variações relativas (Prof. Paulo Cezar Pinto Carvalho).
* [Portal da Matemática OBMEP / IMPA - Módulo de Proporcionalidade e Porcentagem](https://portaldaobmep.impa.br/index.php/modulo/ver?modulo=77) - Videoaulas e material teórico oficial sobre grandezas proporcionais e regra de três composta.
* MORGADO, Augusto César; WAGNER, Eduardo; CARVALHO, Paulo Cezar Pinto. **Matemática do Ensino Médio, Volume 1**. 11. ed. Rio de Janeiro: SBM, 2012. (Cap. 4 - Proporcionalidade e Funções Lineares).
* IEZZI, Gelson; HAZZAN, Samuel; DEGENSZAJN, David. **Fundamentos de Matemática Elementar, Volume 11: Matemática Comercial e Financeira**. 2. ed. São Paulo: Atual, 2013. (Cap. 1 a 3 - Razões, Proporções e Porcentagens).
* D'AMBRÓSIO, Ubiratan. **Etnomatemática: Elo entre as Tradições e a Modernidade**. Belo Horizonte: Autêntica, 2001. (Cap. 2 - Aritmética Prática e Proporções).
