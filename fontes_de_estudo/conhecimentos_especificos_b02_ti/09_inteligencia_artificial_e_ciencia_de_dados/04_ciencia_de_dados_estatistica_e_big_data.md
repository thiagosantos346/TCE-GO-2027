# 04 - Ciência de Dados, Estatística Aplicada e Big Data
**Última Atualização:** 2026-03-31  
**Banca Foco:** FCC (Fundação Carlos Chagas)  
**Cargo:** Auditor de Controle Externo - Tecnologia da Informação  
**Status do Mapeamento:** 100% aderente ao edital TCE-GO



---


## 📌 Ementa / Itens do Edital
1. **Fundamentos de Ciência de Dados e Metodologia CRISP-DM:** As seis fases iterativas do CRISP-DM (*Business Understanding*, *Data Understanding*, *Data Preparation*, *Modeling*, *Evaluation*, *Deployment*).
2. **Pipeline de Dados e Engenharia de Features:** Tratamento de valores ausentes (*Missing Values*: MCAR, MAR, MNAR, deleção e métodos de imputação simples e avançada com KNN Imputer); Detecção de outliers (critério do IQR de Tukey e escore Z); Transformações de escala (Normalização Min-Max vs. Padronização/StandardScaler); Codificação categórica (One-Hot Encoding e armadilha dummy vs. Ordinal/Label Encoding); e Análise Exploratória de Dados (EDA).
3. **Estatística Aplicada e Probabilidade:** Medidas de tendência central (Média, Mediana e Moda) e assimetria de distribuições (simétrica, assimetria positiva à direita e assimetria negativa à esquerda); Medidas de dispersão (Variância, Desvio Padrão e Coeficiente de Variação); Distribuições canônicas (Normal/Gaussiana com regra empírica 68-95-99.7%, Binomial e Poisson); Inferência estatística e Testes de Hipóteses ($H_0$, $H_1$, Erro Tipo I $\alpha$, Erro Tipo II $\beta$, nível de significância e regra de decisão pelo $p$-valor).
4. **Métricas e Avaliação de Modelos Preditivos:** Trade-off Viés vs. Variância (*Underfitting* vs. *Overfitting*); Técnicas de validação (Hold-out e Validação Cruzada k-Fold estratificada); Métricas de Classificação sobre Matriz de Confusão (Acurácia e suas armadilhas em dados desbalanceados, Precisão, Sensibilidade/Recall, F1-Score como média harmônica, Curva ROC e AUC-ROC); e Métricas de Regressão (MAE, MSE, RMSE e $R^2$).
5. **Fundamentos de Big Data e Processamento Distribuído:** As dimensões dos Vs do Big Data (Volume, Velocidade, Variedade, Veracidade e Valor); Ecossistema Apache Hadoop (arquitetura HDFS com NameNode em RAM e DataNodes em disco, blocos de 128 MB, replicação $3\times$ com rack awareness, YARN e paradigma MapReduce com etapas de Map, Shuffle & Sort e Reduce); e Apache Spark (computação em memória RAM, RDDs com Grafo de Linhagem, DataFrames com otimizador Catalyst, Avaliação Preguiçosa/*Lazy Evaluation* de Transformações vs. Ações imediatas, e operações Narrow vs. Wide com shuffle).

---

## 🧭 Sumário

1. [Metodologia CRISP-DM e Pipeline de Engenharia de Dados](#1-metodologia-crisp-dm-e-pipeline-de-engenharia-de-dados)
    1. [As Seis Fases do Framework CRISP-DM](#11-as-seis-fases-do-framework-crisp-dm)
    2. [Tratamento de Valores Ausentes e Outliers (Critério IQR)](#12-tratamento-de-valores-ausentes-e-outliers-criterio-iqr)
    3. [Escalonamento e Codificação de Variáveis Categóricas](#13-escalonamento-e-codificacao-de-variaveis-categoricas)
    4. [Teste 333](#Teste-333)
    5. [Teste 334](#Teste-334)
    6. [Teste 335](#Teste-335)
2. [Estatística Aplicada, Probabilidades e Testes de Hipóteses](#2-estatistica-aplicada-probabilidades-e-testes-de-hipoteses)
    1. [Medidas de Tendência Central, Dispersão e Assimetria](#21-medidas-de-tendencia-central-dispersao-e-assimetria)
    2. [Distribuições de Probabilidade: Normal, Binomial e Poisson](#22-distribuicoes-de-probabilidade-normal-binomial-e-poisson)
    3. [Testes de Hipóteses, Erros Tipo I e II e Critério do p-Valor](#23-testes-de-hipoteses-erros-tipo-i-e-ii-e-criterio-do-p-valor)
    4. [Teste 336](#Teste-336)
    5. [Teste 337](#Teste-337)
    6. [Teste 338](#Teste-338)
3. [Avaliação de Modelos Preditivos (Classificação e Regressão)](#3-avaliacao-de-modelos-preditivos-classificacao-e-regressao)
    1. [O Trade-off Viés vs. Variância (Bias-Variance Tradeoff)](#31-o-trade-off-vies-vs-variancia-bias-variance-tradeoff)
    2. [Matriz de Confusão e Métricas para Classes Desbalanceadas](#32-matriz-de-confusao-e-metricas-para-classes-desbalanceadas)
    3. [Curva ROC, AUC-ROC e Métricas de Regressão (MAE, MSE, RMSE, R²)](#33-curva-roc-auc-roc-e-metricas-de-regressao-mae-mse-rmse-r2)
    4. [Teste 339](#Teste-339)
    5. [Teste 340](#Teste-340)
    6. [Teste 341](#Teste-341)
4. [Ecossistema Big Data: Hadoop e Apache Spark](#4-ecossistema-big-data-hadoop-e-apache-spark)
    1. [Os Vs do Big Data e a Arquitetura HDFS/YARN do Hadoop](#41-os-vs-do-big-data-e-a-arquitetura-hdfsyarn-do-hadoop)
    2. [Paradigma MapReduce e suas Limitações de I/O em Disco](#42-paradigma-mapreduce-e-suas-limitacoes-de-io-em-disco)
    3. [Apache Spark: Processamento em Memória, Lazy Evaluation e RDDs](#43-apache-spark-processamento-em-memoria-lazy-evaluation-e-rdds)
    4. [Teste 342](#Teste-342)
    5. [Teste 343](#Teste-343)
5. [🌐 Fontes Oficiais e Referências Bibliográficas](#fontes-oficiais-e-referencias-bibliograficas)

---

## 1. Metodologia CRISP-DM e Pipeline de Engenharia de Dados

A Ciência de Dados constitui a intersecção analítica entre Estatística, Ciência da Computação e Conhecimento do Negócio (Auditoria e Controle Externo), operando transformações metodológicas para converter dados brutos não estruturados em conhecimento aplicável.

### 1.1 As Seis Fases do Framework CRISP-DM

O **CRISP-DM (*Cross-Industry Standard Process for Data Mining*)** é o padrão internacional mais adotado para estruturar ciclos analíticos de dados em fases iterativas e interdependentes:

```
[1. Business Understanding] ◄───────────────┐
           │                                 │
           ▼                                 │
[2. Data Understanding]                      │
           │                                 │
           ▼                                 │
[3. Data Preparation] ◄──┐                   │ (Retorno cíclico se
           │             │ (Iteração mútua)  │  avaliação reprovar)
           ▼             │                   │
[4. Modeling] ───────────┘                   │
           │                                 │
           ▼                                 │
[5. Evaluation] ─────────────────────────────┘
           │
           ▼
[6. Deployment] ──► Monitoramento Contínuo (Data Drift / Model Drift)
```

1. **Business Understanding (Compreensão do Negócio):** Fase inaugural que define os objetivos institucionais, metas de negócio e restrições regulatórias do tribunal, convertendo-os em problemas formais de mineração de dados e planejamento técnico.
2. **Data Understanding (Compreensão dos Dados):** Coleta dos dados brutos preliminares, exploração de tipos de variáveis, inspeção inicial de integridade e formulação das primeiras hipóteses estatísticas.
3. **Data Preparation (Preparação dos Dados):** Fase que tradicionalmente **consome a maior parcela do esforço do projeto (70% a 80%)**. Envolve seleção de registros e colunas, limpeza, higienização, tratamento de nulos, enriquecimento de bases, transformação de escalas e codificação categórica.
4. **Modeling (Modelagem):** Escolha de técnicas algorítmicas de aprendizado de máquina (árvores de decisão, regressões, redes neurais), divisão em partições de treino e calibração de hiperparâmetros. A seta bidirecional com a fase de Preparação reflete que a modelagem frequentemente exige novas transformações de variáveis.
5. **Evaluation (Avaliação):** Julgamento minucioso do modelo frente aos critérios de sucesso e metas institucionais formulados na fase 1 (*Business Understanding*). Se o modelo não atingir os patamares de negócio exigidos, retorna-se à primeira fase para redefinições de escopo.
6. **Deployment (Implantação):** Disponibilização do modelo em ambiente de produção (APIs de auditoria em tempo real, rotinas de escoragem em lote ou dashboards de fiscalização), estabelecendo governança contínua contra degradação temporal do modelo (*model drift* e *concept drift*).

### 1.2 Tratamento de Valores Ausentes e Outliers (Critério IQR)

* **Tratamento de Valores Ausentes (*Missing Values*):**
    - *Mecanismos Teóricos de Perda:*
    - **MCAR (*Missing Completely at Random*):** A falta do dado ocorre de forma estritamente aleatória, não guardando correlação com nenhuma variável observada ou não observada na base.
    - **MAR (*Missing at Random*):** A probabilidade de o dado faltar relaciona-se sistematicamente com outras variáveis conhecidas da base (ex.: declarações de renda faltam mais frequentemente para determinados perfis etários observados).
    - **MNAR (*Missing Not at Random*):** O motivo da ausência relaciona-se diretamente com o próprio valor não registrado (ex.: contribuintes que praticaram desvios milionários recusam-se a preencher o campo de patrimônio).
    - *Abordagens de Tratamento:*
    - *Remoção:* Exclusão de linhas (*listwise*) ou colunas. Inviável quando reduz excessivamente o poder estatístico da amostra.
    - *Imputação Simples:* Substituição pela Média (distribuições normais e simétricas), pela Mediana (distribuições assimétricas ou com presença de outliers) ou pela Moda (dados categóricos nominais).
    - *Imputação Avançada:* **KNN Imputer** (imputa pelo valor ponderado dos $k$ vizinhos mais próximos no espaço vetorial) e **MICE** (*Multivariate Imputation by Chained Equations*).

* **Detecção de Valores Discrepantes (*Outliers*) pelo Critério do IQR:**
    - O método de John Tukey baseia-se no **Intervalo Interquartil (IQR - *Interquartile Range*)**:
    $$\text{IQR} = Q_3 - Q_1$$
    $$\text{Limite Inferior (LI)} = Q_1 - 1{,}5 \cdot \text{IQR}$$
    $$\text{Limite Superior (LS)} = Q_3 + 1{,}5 \cdot \text{IQR}$$
    - Qualquer observação que satisfaça $x < \text{LI}$ ou $x > \text{LS}$ é categorizada como **outlier moderado**. Se o fator multiplicador for $3{,}0$, classifica-se como **outlier extremo**.
    - O critério do **Escore Z (*Z-Score*)** ($Z = \frac{x - \mu}{\sigma}$) sinaliza anomalias quando $|Z| > 3$, pressupondo distribuição aproximadamente normal.

### 1.3 Escalonamento e Codificação de Variáveis Categóricas

1. **Transformações de Escala Numérica:**
    - **Normalização Min-Max:** Projeta os valores no intervalo fechado $[0, 1]$:
     $$X_{\text{norm}} = \frac{X - X_{\min}}{X_{\max} - X_{\min}}$$
     *Atenção:* É altamente suscetível a distorções causadas por outliers que comprimem a massa dos dados normais.
    - **Padronização (StandardScaler / Z-Score):** Reescalona a distribuição para apresentar média zero ($\mu = 0$) e variância unitária ($\sigma = 1$):
     $$X_{\text{pad}} = \frac{X - \mu}{\sigma}$$
     *Vantagem:* Não delimita limites artificiais e é a escolha prioritária para algoritmos baseados em descida de gradiente e cálculo de distâncias euclidianas (SVM, Redes Neurais, K-Means e PCA).

2. **Codificação de Variáveis Categóricas:**
    - **One-Hot Encoding:** Cria uma coluna binária indicadora ($0$ ou $1$) para cada uma das $K$ categorias existentes. Indicado para variáveis nominais sem relação de hierarquia (ex.: Unidades Federativas). Em regressões lineares clássicas, descarta-se uma coluna ($K-1$) para evitar a **armadilha das variáveis dummy** (colinearidade perfeita).
    - **Ordinal / Label Encoding:** Mapeia categorias em números inteiros sequenciais ($0, 1, 2, \dots$). Aplicável estritamente a variáveis que guardam ordem ou gradação natural (ex.: Risco Fiscal: Baixo $=0$, Médio $=1$, Alto $=2$).

---

### Teste 333
**(FCC - TCE-RS - Auditor Público Externo - Tecnologia da Informação)**
No desenvolvimento de um projeto de ciência de dados estruturado sob a metodologia CRISP-DM para análise de superfaturamento em contratos de obras públicas, os analistas estão executando a etapa de *Data Preparation*. Durante a identificação de valores discrepantes no custo unitário do metro quadrado de asfalto, a equipe optou pela técnica do Intervalo Interquartil (IQR).
A base de dados indicou que o primeiro quartil ($Q_1$) foi apurado em R$ 200,00 e o terceiro quartil ($Q_3$) foi apurado em R$ 350,00.
A respeito da metodologia CRISP-DM e dos critérios de pré-processamento de outliers, assinale a afirmativa correta:

* **A)** O Intervalo Interquartil (IQR) é de R$ 550,00, e qualquer valor acima de R$ 900,00 será classificado como valor regular.
* **B)** O IQR é de R$ 150,00 ($350 - 200$), o Limite Inferior é de R$ -25,00 ($200 - 1{,}5 \times 150$) e o Limite Superior é de R$ 575,00 ($350 + 1{,}5 \times 150$), configurando como outlier qualquer custo unitário superior a R$ 575,00.
* **C)** Na metodologia CRISP-DM, a fase de *Business Understanding* sucede a fase de *Deployment*, visto que o entendimento dos objetivos de negócio só pode ocorrer após a solução estar em produção no âmbito da administração pública direta e indireta.
* **D)** A técnica de Padronização (*Z-Score*) deve ser evitada em modelos baseados em gradiente descendente, sendo imperativo o uso exclusivo do One-Hot Encoding para variáveis puramente numéricas.
* **E)** A metodologia CRISP-DM proíbe expressamente qualquer retorno ou iteração entre a fase de Modelagem (*Modeling*) e a fase de Preparação de Dados (*Data Preparation*).


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O IQR é a diferença entre os quartis ($Q_3 - Q_1 = 350 - 200 = 150$), e não a soma.
> - **B)** **Correta.** Aplicando o critério formal de Tukey:
>     - $\text{IQR} = 350 - 200 = 150$
>     - $\text{Limite Superior} = Q_3 + 1{,}5 \cdot \text{IQR} = 350 + 1{,}5 \cdot 150 = 350 + 225 = 575$
>     - $\text{Limite Inferior} = Q_1 - 1{,}5 \cdot \text{IQR} = 200 - 1{,}5 \cdot 150 = 200 - 225 = -25$
>   Portanto, qualquer custo unitário por $m^2$ superior a R$ 575,00 é formalmente rotulado como outlier.
> - **C)** Incorreta. *Business Understanding* é a **primeira** fase do CRISP-DM, enquanto o *Deployment* é a última.
> - **D)** Incorreta. A padronização é altamente indicada para algoritmos com descida de gradiente, e o *One-Hot Encoding* é uma técnica exclusiva para atributos categóricos.
> - **E)** Incorreta. O ciclo CRISP-DM é intrinsecamente iterativo, com retorno contínuo entre modelagem e preparação de dados.
> 
> **Gabarito: B**

---

### Teste 334
**(FGV - TJ-RR / Analista Judiciário - TI - Tratamento de Outliers e Critério IQR)**
Em um projeto de ciência de dados para auditoria de contratos emergenciais de saúde, a equipe técnica precisa identificar desvios grosseiros e valores atípicos (*outliers*) nos preços unitários de medicamentos, utilizando um método estatístico não paramétrico e robusto à presença de distribuições assimétricas.

O método amplamente recomendado pela literatura é o do **Intervalo Interquartil** (*Interquartile Range - IQR*). Considerando o Primeiro Quartil ($Q_1$) e o Terceiro Quartil ($Q_3$) de uma série ordenada de preços, assinale a opção que apresenta os limites inferior e superior que definem formalmente um *outlier* pelo critério de Tukey:

* **A)** Limite Inferior: $Q_1 - 1,5 \cdot IQR$; Limite Superior: $Q_3 + 1,5 \cdot IQR$, onde $IQR = Q_3 - Q_1$.
* **B)** Limite Inferior: $\mu - 2 \cdot \sigma$; Limite Superior: $\mu + 2 \cdot \sigma$, sendo $\mu$ a média e $\sigma$ a variância.
* **C)** Limite Inferior: $0$; Limite Superior: $Q_3 \times 100$.
* **D)** Limite Inferior: $\text{Mediana} / 2$; Limite Superior: $\text{Mediana} \times 2$.
* **E)** Limite Inferior: $Q_1 + Q_3$; Limite Superior: $Q_1 - Q_3$.


---

> **Comentário Detalhado:**
>
> - **A)** **CORRETA.** A regra dos passos de John Tukey (*Boxplot rule*) define o **Intervalo Interquartil (IQR)** como a dispersão da metade central dos dados:
>   $$IQR = Q_3 - Q_1$$
>   As "cercas" (*fences*) clássicas para classificação de pontos atípicos (*outliers*) são calculadas por:
>   - **Limite Inferior:** $LI = Q_1 - 1,5 \cdot IQR$ (qualquer valor abaixo de $LI$ é considerado atípico inferior).
>   - **Limite Superior:** $LS = Q_3 + 1,5 \cdot IQR$ (qualquer valor acima de $LS$ é considerado atípico superior).
>   - Para *outliers extremos*, o fator multiplicador sobe para $3,0 \cdot IQR$. Trata-se de uma métrica altamente robusta porque não é influenciada por valores extremos como ocorre com a média e o desvio padrão.
> - **B)** Incorreta. Essa regra assume distribuição normal estrita e usa desvio padrão ($\sigma$), além de confundir variância com desvio padrão.
> - **C)** Incorreta. Fórmulas fictícias sem fundamentação estatística.
> - **D)** Incorreta. A mediana por si só não expressa a dispersão dos quartis intermediários.
> - **E)** Incorreta. Fórmulas sem sentido algébrico.
> 
> **Gabarito: A**

---

### Teste 335
**(FGV - TRT / Analista Judiciário - TI - Escalonamento de Recursos e Prevenção de Data Leakage)**
Na etapa de pré-processamento de um modelo de Machine Learning preditor de probabilidade de insolvência de fornecedores públicos, o cientista de dados depara-se com variáveis numéricas em escalas de grandezas muito distintas (ex.: `faturamento_anual` na ordem de milhões de reais e `tempo_empresa_anos` variando de 0 a 30).

A respeito das técnicas de escalonamento e dos cuidados mandatórios no fluxo de validação cruzada, assinale a afirmativa correta:

* **A)** Algoritmos baseados em distâncias euclidianas (como KNN e SVM) ou gradiente descendente são imunes à escala dos atributos, dispensando qualquer técnica de escalonamento.
* **B)** A padronização (*StandardScaler*) transforma a variável de modo que ela passe a ter média igual a zero e desvio padrão unitário ($Z = \frac{X - \mu}{\sigma}$).
* **C)** O ajuste dos parâmetros de escalonamento (como média e desvio padrão) deve ser calculado simultaneamente sobre toda a base unificada (treino + teste) antes da divisão em folds para acelerar o processamento no âmbito da administração pública direta e indireta.
* **D)** O escalonamento de variáveis deve ser aplicado obrigatoriamente também na variável alvo categórica de classificação binária.
* **E)** Árvores de decisão puras (Decision Trees) e Random Forests sofrem severa perda de acurácia se as variáveis numéricas não forem escalonadas entre 0 e 1.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Algoritmos geométricos baseados em distância (KNN, SVM, K-Means) e métodos baseados em gradiente são **extremamente sensíveis à escala**; sem escalonamento, o atributo com maior valor numérico absoluto domina completamente a métrica de distância.
> - **B)** **CORRETA.** Fundamentos das duas técnicas de escalonamento mais comuns:
>   - **StandardScaler (Padronização / Z-Score):** $z = \frac{x - \mu}{\sigma}$. Centraliza os dados na média 0 e escala pela variância unitária. Não possui limites fixos superiores/inferiores e lida muito melhor com dados que contêm outliers.
>   - **MinMaxScaler (Normalização Min-Max):** $x_{norm} = \frac{x - x_{min}}{x_{max} - x_{min}}$. Comprime os valores no intervalo fechado $[0, 1]$. É vulnerável a outliers, pois um valor extremo espreme todas as instâncias normais em uma faixa minúscula.
> - **C)** Incorreta. Calcular métricas em toda a base antes da separação de treino e teste configura **vazamento de dados (Data Leakage)**, resultando em métricas de validação enganosamente otimistas. O escalonador deve ser ajustado (`fit`) exclusivamente nos dados de treino e apenas aplicado (`transform`) no conjunto de teste.
> - **D)** Incorreta. O alvo categórico (rótulo 0 ou 1) não deve ser submetido a *StandardScaler*.
> - **E)** Incorreta. Modelos baseados em árvores de decisão particionam variáveis independentemente de escalas monotônicas, sendo invariantes ao escalonamento de atributos.
> 
> **Gabarito: B**

---

## 2. Estatística Aplicada, Probabilidades e Testes de Hipóteses

### 2.1 Medidas de Tendência Central, Dispersão e Assimetria

* **Medidas de Posição:**
    - **Média Aritmética ($\bar{x}$):** Centro de massa da distribuição ($\bar{x} = \frac{1}{n}\sum x_i$). Extremamente vulnerável a distorções por valores discrepantes.
    - **Mediana ($Md$):** O elemento central ordenado que divide a amostra exatamente ao meio (percentil 50). Trata-se de uma medida **robusta e resistente a outliers**.
    - **Moda ($Mo$):** O valor que ocorre com a maior frequência estatística observada.
* **Comportamento das Medidas sob Assimetria de Distribuições:**

```
   Assimetria Positiva (à Direita)            Distribuição Simétrica           Assimetria Negativa (à Esquerda)
          Densidade                                 Densidade                                Densidade
             /\                                        /\                                       /\
            /  \                                      /  \                                     /  \
           /    \                                    /    \                                   /    \
     _____/      \________                     _____/      \_____                       _____/      \_____
         Mo < Md < Média                          Média = Md = Mo                          Média < Md < Mo
   (Cauda longa puxa a Média)               (Curva Normal Gaussiana)             (Cauda longa puxa a Média)
```

> ⚠️ **Alerta de Prova (FCC):**
> A banca FCC cobra recorrentemente a relação de ordem sob assimetria:
>
> - **Assimetria Positiva (à Direita / Cauda Longa Superior):** Típica de dados salariais e contratações públicas onde poucos valores gigantescos puxam a média: **$\text{Moda} < \text{Mediana} < \text{Média}$**.
> - **Assimetria Negativa (à Esquerda / Cauda Longa Inferior):** **$\text{Média} < \text{Mediana} < \text{Moda}$**.
> - **Distribuição Simétrica:** **$\text{Média} = \text{Mediana} = \text{Moda}$**.

* **Medidas de Dispersão:**
    - **Variância Amostral ($s^2$):** $\frac{1}{n-1}\sum (x_i - \bar{x})^2$ (utiliza o divisor de Bessel $n-1$ para estimador não enviesado).
    - **Desvio Padrão ($s$):** $\sqrt{s^2}$, expresso na mesma unidade de medida da variável original.
    - **Coeficiente de Variação (CV):** $\text{CV} = \frac{s}{\bar{x}} \times 100\%$. Medida relativa adimensional que viabiliza a comparação direta da variabilidade entre variáveis de escalas ou grandezas distintas.

### 2.2 Distribuições de Probabilidade: Normal, Binomial e Poisson

1. **Distribuição Normal (Gaussiana):**
    - Curva simétrica em formato de sino governada pela média $\mu$ e desvio padrão $\sigma$.
    - **Regra Empírica (68-95-99.7%):**
    - $68{,}27\%$ dos dados encontram-se no intervalo $[\mu - 1\sigma, \mu + 1\sigma]$.
    - $95{,}45\%$ dos dados situam-se no intervalo $[\mu - 2\sigma, \mu + 2\sigma]$.
    - $99{,}73\%$ dos dados situam-se no intervalo $[\mu - 3\sigma, \mu + 3\sigma]$.

2. **Distribuição Binomial:**
    - Modela o número de sucessos $k$ em $n$ ensaios de Bernoulli independentes com probabilidade de sucesso $p$:
     $$P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad E[X] = np, \quad \text{Var}(X) = np(1-p)$$
3. **Distribuição de Poisson:**
    - Modela a contagem de ocorrências de eventos raros que acontecem a uma taxa média constante $\lambda$ em um intervalo fixado contínuo de tempo ou espaço.
    - Propriedade elementar cobrada em prova: **$\text{Média} = \text{Variância} = \lambda$**.

### 2.3 Testes de Hipóteses, Erros Tipo I e II e Critério do p-Valor

Estrutura formal de tomada de decisão estatística sob incerteza:

- **Hipótese Nula ($H_0$):** Premissa básica de ausência de diferença, conformidade ou efeito padrão.
- **Hipótese Alternativa ($H_1$):** Afirmação de presença de efeito, anomalia ou fraude que se pretende demonstrar.
- **Tipologia dos Erros de Decisão:**
    - **Erro Tipo I ($\alpha$):** Rejeitar $H_0$ quando $H_0$ é **verdadeira** (Falso Positivo estatístico). O limite tolerado de ocorrência desse erro define o **Nível de Significância** ($\alpha$, tipicamente fixado em 5%).
    - **Erro Tipo II ($\beta$):** Não rejeitar $H_0$ quando $H_0$ é **falsa** (Falso Negativo estatístico). O complemento $1 - \beta$ define o **Poder do Teste**.
- **Regra de Decisão pelo $p$-valor:**
    - O $p$-valor indica a probabilidade de obter uma estatística de teste tão ou mais extrema que a observada, assumindo $H_0$ como verdadeira.
    - **Critério de Rejeição:** Se **$p\text{-valor} \le \alpha$**, rejeita-se a hipótese nula $H_0$ com significância estatística; se $p\text{-valor} > \alpha$, não há evidência amostral suficiente para rejeitar $H_0$.

---

### Teste 336
**(FCC - TRF-3ª Região - Analista Judiciário - Estatística Aplicada)**
Na análise estatística dos salários praticados por fornecedores contratados pelo setor público, observou-se que a distribuição de rendimentos apresenta uma acentuada **Assimetria Positiva (à direita)**, decorrente da existência de uma minoria de executivos com salários desproporcionalmente vultosos em comparação com o grande contingente de operários.
Considerando o comportamento das medidas de tendência central e os conceitos de inferência estatística, assinale a alternativa correta:

* **A)** Em uma distribuição contínua unimodal com assimetria positiva, a relação de ordem observada entre as medidas de posição é: $\text{Moda} < \text{Mediana} < \text{Média}$.
* **B)** Em uma distribuição perfeitamente simétrica gaussiana, a Média é estritamente superior à Mediana, e a Moda assume obrigatoriamente valor nulo.
* **C)** O Erro Tipo I em um teste de hipóteses ocorre quando o auditor decide não rejeitar a hipótese nula $H_0$, mesmo sendo ela flagrantemente falsa.
* **D)** Um $p$-valor de $0{,}001$ obtido em um teste estatístico indica que se deve aceitar a hipótese nula $H_0$ sob o nível de significância padrão de $\alpha = 0{,}05$ no âmbito da administração pública direta e indireta.
* **E)** O desvio padrão amostral de uma variável não se altera quando todos os valores observados na amostra são multiplicados por uma constante real não nula.


---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Na distribuição com **assimetria positiva (à direita)**, a cauda alongada superior puxa a **Média** para cima. A **Moda** permanece no ponto de maior frequência e a **Mediana** posiciona-se no centro ordinal, resultando na ordem: $\text{Moda} < \text{Mediana} < \text{Média}$.
> - **B)** Incorreta. Em distribuições simétricas, as três medidas coincidem no mesmo ponto: $\text{Média} = \text{Mediana} = \text{Moda}$.
> - **C)** Incorreta. O Erro Tipo I ($\alpha$) é **rejeitar** $H_0$ quando $H_0$ é verdadeira. Não rejeitar $H_0$ falsa é o Erro Tipo II ($\beta$).
> - **D)** Incorreta. A regra de decisão estatística determina: se $p\text{-valor} \le \alpha$, a hipótese $H_0$ deve ser **rejeitada**. Com $p = 0{,}001$ e $\alpha = 0{,}05$, rejeita-se $H_0$.
> - **E)** Incorreta. Se multiplicarmos todos os valores por uma constante $c$, o desvio padrão é multiplicado por $|c|$.
> 
> **Gabarito: A**

---

### Teste 337
**(FGV - TRT / Analista Judiciário - TI - Distribuição Normal e Teorema Central do Limite)**
A Distribuição Normal (Gaussiana) é o modelo probabilístico mais importante da inferência estatística e da ciência de dados, formalmente expressa por sua densidade de probabilidade $X \sim \mathcal{N}(\mu, \sigma^2)$.

A respeito das propriedades geométricas e teóricas da Distribuição Normal, assinale a afirmativa correta:

* **A)** A curva da distribuição normal é assimétrica e bimodal, onde a moda diverge significativamente da média e da mediana.
* **B)** Na distribuição normal, a média, a mediana e a moda coincidem no centro exato da curva; além disso, pela regra empírica (regra 68-95-99.7), aproximadamente 68,26% das observações situam-se no intervalo de $\mu \pm 1\sigma$, aproximadamente 95,44% em $\mu \pm 2\sigma$ e cerca de 99,73% em $\mu \pm 3\sigma$.
* **C)** O Teorema Central do Limite estabelece que a soma ou média de variáveis aleatórias independentes e identicamente distribuídas converge para uma distribuição exponencial quando o tamanho da amostra tende ao infinito considerando os requisitos operacionais de segurança, escalabilidade, auditoria e desempenho corporativo.
* **D)** A área total sob a curva de densidade de probabilidade de uma Gaussiana é igual a 100,0.
* **E)** O desvio padrão ($\sigma$) desloca a curva horizontalmente para a direita ou esquerda sem afetar o seu achatamento ou dispersão.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A distribuição normal é estritamente **simétrica** e **unimodal** em torno de sua média central.
> - **B)** **CORRETA.** Propriedades geométricas e probabilísticas basilares da Normal:
>   1. **Coincidência dos Parâmetros Centrais:** $\text{Média} = \text{Mediana} = \text{Moda} = \mu$.
>   2. **Simetria Perfeita:** Coeficiente de assimetria (*skewness*) igual a 0 e curtose normal de referência (kurtosis excess igual a 0).
>   3. **Regra Empírica dos Desvios:** 
>      - $P(\mu - 1\sigma \le X \le \mu + 1\sigma) \approx 68,27\%$
>      - $P(\mu - 2\sigma \le X \le \mu + 2\sigma) \approx 95,45\%$
>      - $P(\mu - 3\sigma \le X \le \mu + 3\sigma) \approx 99,73\%$
> - **C)** Incorreta. O **Teorema Central do Limite (TCL)** garante a convergência para a **Distribuição Normal**, e não para a distribuição exponencial.
> - **D)** Incorreta. A integral total sob qualquer função densidade de probabilidade contínua é rigorosamente igual a $1$ (representando 100% da probabilidade total).
> - **E)** Incorreta. Quem desloca a curva horizontalmente é a média ($\mu$); o desvio padrão ($\sigma$) controla a dispersão (largura e achatamento).
> 
> **Gabarito: B**

---

### Teste 338
**(FGV - TRT / Analista Judiciário - TI - Testes de Hipóteses, Erros Tipo I e II e p-Valor)**
Na auditoria estatística de folha de pagamento, os auditores formulam um teste de hipóteses para avaliar se a média de horas extras de determinado departamento ($H_1$) é estatisticamente superior ao limite legal regulamentado ($H_0$).

A respeito dos conceitos de hipótese nula, erros de decisão e interpretação do $p$-valor, assinale a afirmativa correta:

* **A)** O Erro Tipo I ($lpha$) ocorre quando o teste rejeita a hipótese nula ($H_0$) sendo ela verdadeira (Falso Positivo); ao passo que o Erro Tipo II ($eta$) ocorre quando o teste não rejeita a hipótese nula sendo ela falsa (Falso Negativo).
* **B)** O nível de significância $\alpha$ deve ser fixado em 99% para garantir que não haja erros de tipo I.
* **C)** Um $p$-valor menor que o nível de significância estipulado (ex.: $p < 0,05$) indica que a hipótese nula ($H_0$) deve ser aceita e confirmada como verdadeira com certeza absoluta em estrita conformidade com as normas legais e regulamentares aplicáveis.
* **D)** O Poder do Teste estatístico é dado algebricamente por $1 - \alpha$.
* **E)** A hipótese alternativa ($H_1$) representa o estado inicial de conformidade ou ausência de efeito a ser mantido caso faltem evidências probatórias.


---

> **Comentário Detalhado:**
>
> - **A)** **CORRETA.** Matriz clássica de decisões em inferência estatística:
>   - **Erro Tipo I (Nível de Significância $\alpha$):** Rejeitar a hipótese nula ($H_0$) quando ela é, na realidade, verdadeira. Na auditoria: apontar uma fraude ou ilegalidade indevidamente (Falso Positivo).
>   - **Erro Tipo II ($eta$):** Não rejeitar a hipótese nula quando ela é falsa. Na auditoria: deixar passar uma fraude real e concluir que o processo está em conformidade (Falso Negativo).
>   - **Poder do Teste ($1 - \beta$):** A probabilidade de rejeitar corretamente uma hipótese nula falsa.
> - **B)** Incorreta. O nível de significância $lpha$ é uma probabilidade de erro (tipicamente fixado em 5% ou 1%, ou seja, 0,05 ou 0,01), e não 99%.
> - **C)** Incorreta. A regra universal de decisão é: **se $p < \alpha$, rejeita-se $H_0$** em favor da hipótese alternativa ($H_1$). O $p$-valor mede a probabilidade de observar dados tão ou mais extremos sob a premissa de que $H_0$ fosse verdadeira.
> - **D)** Incorreta. O Poder do Teste é $1 - \beta$ (complementar ao erro tipo II), e não $1 - \alpha$ (que é o nível de confiança).
> - **E)** Incorreta. Quem representa o status quo ou ausência de diferença/efeito é a **hipótese nula ($H_0$)**.
> 
> **Gabarito: A**

---

## 3. Avaliação de Modelos Preditivos (Classificação e Regressão)

### 3.1 O Trade-off Viés vs. Variância (Bias-Variance Tradeoff)

O erro de generalização de qualquer algoritmo decomponde-se em três termos matemáticos:
$$\text{Erro de Teste} = \text{Viés}^2 + \text{Variância} + \sigma_{\text{ruído irredutível}}^2$$

- **Underfitting (Subajuste / Alto Viés):** O modelo é excessivamente simples (ex.: impor uma reta sobre um fenômeno curvo) e falha em capturar os padrões subjacentes, apresentando alto erro tanto na base de treino quanto no teste.
- **Overfitting (Sobreajuste / Alta Variância):** O modelo é hipercomplexo (ex.: árvore de decisão profunda sem limites) e decora as particularidades e ruídos estocásticos do treino, apresentando erro mínimo no treino e erro elevado nos dados inéditos de teste.
- **Validação Cruzada k-Fold Estratificada (*Stratified k-Fold*):** Divide os dados em $k$ partições preservando a mesma proporção percentual das classes em cada dobra, técnica mandatória em problemas desbalanceados.

### 3.2 Matriz de Confusão e Métricas para Classes Desbalanceadas

```
                             REALIDADE (GROUND TRUTH)
                        Positivo (Fraude = 1)   Negativo (Regular = 0)
                      ┌───────────────────────┬───────────────────────┐
  PREDIÇÃO   Positivo │  VERDADEIRO POSITIVO  │    FALSO POSITIVO     │
     DO      (Previsto│         (VP)          │   (FP - Erro Tipo I)  │
   MODELO      = 1)   ├───────────────────────┼───────────────────────┤
             Negativo │    FALSO NEGATIVO     │  VERDADEIRO NEGATIVO  │
             (Previsto│  (FN - Erro Tipo II)  │         (VN)          │
               = 0)   └───────────────────────┴───────────────────────┘
```

1. **Acurácia (Accuracy):**
   $$\text{Acurácia} = \frac{\text{VP} + \text{VN}}{\text{VP} + \text{VN} + \text{FP} + \text{FN}}$$
   > ⚠️ **Alerta de Prova (FCC):**
   > A FCC explora exaustivamente a **falácia da Acurácia em classes desbalanceadas**! Se um tribunal possui uma base com 99% de processos regulares e 1% com fraudes, um modelo tolo que declare "regular" para 100% dos casos terá uma fantástica acurácia de 99%, mas terá detectado zero fraudes ($0\%$ de sensibilidade). Em dados desbalanceados, a acurácia é totalmente inútil, exigindo-se Precisão, Recall e F1-Score.

2. **Precisão (Precision / Confiabilidade Preditiva):**
   $$\text{Precisão} = \frac{\text{VP}}{\text{VP} + \text{FP}}$$
   Mede a proporção de predições positivas corretas. Priorizada quando o custo operacional de um Falso Positivo é inaceitável.
3. **Sensibilidade / Revocação / Recall (True Positive Rate - TPR):**
   $$\text{Recall} = \frac{\text{VP}}{\text{VP} + \text{FN}}$$
   Mede a proporção de casos positivos reais capturados pelo modelo. Priorizada quando o custo de um Falso Negativo é catastrófico (ex.: não detectar um esquema ilícito de desvio de verbas).
4. **F1-Score:**
   $$F_1 = 2 \cdot \frac{\text{Precisão} \times \text{Recall}}{\text{Precisão} + \text{Recall}}$$
   É a **média harmônica** entre Precisão e Recall, penalizando severamente modelos desequilibrados que sacrificam uma métrica em favor da outra.

### 3.3 Curva ROC, AUC-ROC e Métricas de Regressão (MAE, MSE, RMSE, R²)

* **Curva ROC e Métrica AUC-ROC:**
    - A Curva ROC mapeia o $\text{Recall}$ (Sensibilidade, Eixo Y) contra o $\text{FPR} = \frac{\text{FP}}{\text{FP} + \text{VN}} = 1 - \text{Especificidade}$ (Eixo X) variando o limiar de probabilidade de $0$ a $1$.
    - A **AUC-ROC** mede a área sob a curva: uma $\text{AUC} = 0{,}5$ indica desempenho aleatório; uma $\text{AUC} = 1{,}0$ representa um separador perfeito.
* **Métricas de Regressão Numérica:**
    - **MAE (Mean Absolute Error):** $\frac{1}{n}\sum |y - \hat{y}|$. Erro linear simples, altamente robusto a outliers.
    - **MSE (Mean Squared Error):** $\frac{1}{n}\sum (y - \hat{y})^2$. Penaliza exponencialmente erros grandes ao elevá-los ao quadrado.
    - **RMSE (Root Mean Squared Error):** $\sqrt{\text{MSE}}$. Mantém a penalização sobre desvios extremos e preserva a unidade original da variável dependente.
    - **$R^2$ (Coeficiente de Determinação):** $1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}$, quantificando a proporção da variância explicada pelo modelo.

---

### Teste 339
**(FCC - TRT / Analista Judiciário - TI - O Dilema Viés vs. Variância em Modelos Preditivos)**
Na avaliação do erro de generalização de algoritmos de aprendizado supervisionado, o Erro Médio Quadrático Esperado de predição sobre dados não vistos pode ser decomposto matematicamente em três componentes fundamentais:

$$\mathbb{E}[Erro] = \text{Viés}^2 + \text{Variância} + \sigma_{\epsilon}^2$$

A respeito do comportamento dessas componentes e do fenômeno do **Bias-Variance Tradeoff**, assinale a afirmativa correta:

* **A)** Modelos com alto viés (*high bias*) tendem a superajustar-se aos ruídos aleatórios do conjunto de treinamento, resultando em acurácia de 100% no teste.
* **B)** O termo $\sigma_{\epsilon}^2$ representa o erro redutível, que pode ser reduzido a zero simplesmente escolhendo o algoritmo de inteligência artificial mais moderno do mercado considerando os requisitos operacionais de segurança, escalabilidade, auditoria e desempenho corporativo considerando os requisitos operacionais de segurança, escalabilidade, auditoria e desempenho corporativo.
* **C)** Modelos excessivamente simples e rígidos (como regressão linear em dados curvilíneos) sofrem de **alto viés e baixa variância**, caracterizando o fenômeno do **Subajuste (*Underfitting*)**; enquanto modelos hipercomplexos e flexíveis (como árvores de decisão profundas sem poda) sofrem de **baixo viés e alta variância**, decorando os ruídos do treino e caracterizando o **Sobreajuste (*Overfitting*)**.
* **D)** Aumentar a quantidade de variáveis irrelevantes e ruídos na base diminui a variância do modelo.
* **E)** Técnicas de regularização (como penalidades L1/L2) servem para aumentar a variância do modelo a níveis extremos.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Alto viés indica simplificação excessiva do modelo (*underfitting*), com desempenho fraco tanto no treino quanto no teste.
> - **B)** Incorreta. O termo $\sigma_{\epsilon}^2$ é o **erro irredutível** (ruído estocástico inerente aos dados do mundo real), impossível de ser eliminado por qualquer modelo matemático.
> - **C)** **CORRETA.** Teorema fundamental do aprendizado estatístico:
>   - **Alto Viés (Underfitting):** O modelo impõe pressupostos excessivamente rígidos sobre a relação funcional entre $X$ e $Y$. Ele erra bastante tanto nos dados de treinamento quanto no conjunto de validação.
>   - **Alta Variância (Overfitting):** O modelo é extremamente flexível e sensível a pequenas flutuações das amostras de treino. Ele atinge erro quase nulo no treino, mas falha dramaticamente ao generalizar para novos dados de teste.
>   - **Objetivo da Otimização:** Encontrar o equilíbrio ótimo (*sweet spot*) de complexidade do modelo que minimize a soma de Viés ao quadrado e Variância.
> - **D)** Incorreta. Variáveis irrelevantes aumentam a variância e estimulam sobreajuste.
> - **E)** Incorreta. Regularizações (Lasso, Ridge) introduzem uma leve penalidade (aumentam ligeiramente o viés) com o propósito benéfico de **reduzir drasticamente a variância**.
> 
> **Gabarito: C**

---

### Teste 340
**(FCC - DPE-RS - Analista de Tecnologia da Informação)**
Um Tribunal de Contas implantou um algoritmo de aprendizado de máquina para triagem de prestações de contas municipais. Em uma amostra de teste com 10.000 processos auditados, sabe-se que 200 processos continham irregularidades graves (positivos) e 9.800 eram processos estritamente regulares (negativos).
Após a execução do classificador, os resultados observados na matriz de confusão foram:

- Verdadeiros Positivos (VP) = 160
- Falsos Positivos (FP) = 40
- Falsos Negativos (FN) = 40
- Verdadeiros Negativos (VN) = 9.760

Avaliando o desempenho desse modelo para o controle externo, assinale a afirmativa correta:

* **A)** A Sensibilidade (Recall) do classificador é de 80%, a Precisão é de 80% e o F1-Score é exatamente 80%.
* **B)** A Acurácia simples é de 80%, comprovando que ela é a métrica mais apropriada para atestar a detecção de fraudes em ambientes com alta desproporção de classes.
* **C)** O classificador apresenta uma Sensibilidade de 99,2%, calculada pela divisão dos Verdadeiros Negativos pela soma dos casos regulares.
* **D)** Em problemas de detecção de fraudes em compras governamentais, deve-se buscar a redução do Recall e o aumento deliberado de Falsos Negativos para reduzir a carga de trabalho dos auditores.
* **E)** Um modelo fictício ingênuo que classificasse todas as 10.000 prestações de contas como regulares apresentaria uma Acurácia de 0%, revelando a sensibilidade dessa métrica ao desbalanceamento.


---

> **Comentário Detalhado:**
>
> - **A)** **Correta.**
>     - **Precisão:** $P = \frac{VP}{VP + FP} = \frac{160}{160 + 40} = \frac{160}{200} = 0{,}80$ ($80\%$).
>     - **Sensibilidade (Recall):** $R = \frac{VP}{VP + FN} = \frac{160}{160 + 40} = \frac{160}{200} = 0{,}80$ ($80\%$).
>     - **F1-Score:** $F_1 = 2 \cdot \frac{P \cdot R}{P + R} = 2 \cdot \frac{0{,}80 \cdot 0{,}80}{0{,}80 + 0{,}80} = 0{,}80$ ($80\%$).
> - **B)** Incorreta. A Acurácia simples é $\frac{160 + 9760}{10000} = 99{,}2\%$, e não 80%. Além disso, ela é sabidamente enganosa em dados desbalanceados.
> - **C)** Incorreta. 99,2% corresponde à Acurácia geral, e não à Sensibilidade (que é 80%).
> - **D)** Incorreta. Reduzir o recall geraria mais Falsos Negativos, deixando fraudes reais passarem impunes.
> - **E)** Incorreta. Um classificador cego que declarasse "regular" para tudo obteria uma acurácia de $98\%$, e não de 0%, demonstrando o perigo de utilizar acurácia isolada em classes raras.
> 
> **Gabarito: A**

---

### Teste 341
**(FCC - TRT / Analista Judiciário - TI - Avaliação de Modelos: Curva ROC, AUC e Métricas de Erro)**
Para mensurar a eficácia de um classificador probabilístico encarregado de apontar licitações suspeitas de fraude sob diferentes limiares de corte (*thresholds*), a área técnica utiliza a **Curva ROC** (*Receiver Operating Characteristic*) e sua respectiva área sob a curva (**AUC-ROC**).

A respeito dessas métricas de avaliação de desempenho, assinale a afirmativa correta:

* **A)** A Curva ROC plota graficamente a Taxa de Verdadeiros Positivos (Sensibilidade / *Recall*) no eixo $Y$ contra a Taxa de Falsos Positivos ($1 - \text{Especificidade}$) no eixo $X$, para todos os limiares de classificação possíveis.
* **B)** Um classificador perfeitamente aleatório, equivalente ao lançamento de uma moeda honesta, apresenta um valor de AUC-ROC igual a 1,0.
* **C)** A métrica MAE (*Mean Absolute Error*) penaliza os grandes erros individuais com mais severidade do que o RMSE (*Root Mean Squared Error*), pois eleva os resíduos ao quadrado em estrita conformidade com as normas legais e regulamentares aplicáveis.
* **D)** O valor máximo teórico atingível pela métrica AUC-ROC é de 0,5.
* **E)** A Curva ROC só pode ser construída se a base de dados tiver exatamente 50% de instâncias de cada classe, sendo inoperante em problemas com classes desbalanceadas.


---

> **Comentário Detalhado:**
>
> - **A)** **CORRETA.** Propriedades fundamentais da **Curva ROC / AUC**:
>   - **Eixo Y:** Taxa de Verdadeiros Positivos ($TPR = \frac{TP}{TP + FN}$), também denominada Sensibilidade ou *Recall*.
>   - **Eixo X:** Taxa de Falsos Positivos ($FPR = \frac{FP}{FP + TN} = 1 - \text{Especificidade}$).
>   - Conforme o limiar de decisão ($	au$) varia de 1 a 0, traça-se a curva de desempenho do modelo.
>   - **AUC-ROC:** Representa a probabilidade de o modelo atribuir uma pontuação mais alta a uma instância positiva selecionada aleatoriamente do que a uma instância negativa.
>   - Classificador perfeito: $AUC = 1,0$.
>   - Classificador puramente aleatório (linha diagonal diagonal): $AUC = 0,5$.
> - **B)** Incorreta. Um classificador aleatório tem $AUC = 0,5$; quem tem $AUC = 1,0$ é o modelo ideal perfeito.
> - **C)** Incorreta. Quem eleva os resíduos ao quadrado e penaliza severamente grandes desvios e outliers é o **MSE/RMSE**, e não o MAE (que calcula a média linear das magnitudes absolutas dos erros).
> - **D)** Incorreta. O valor máximo da AUC-ROC é 1,0.
> - **E)** Incorreta. A Curva ROC é amplamente utilizada justamente por permitir avaliar o comportamento do modelo em diferentes cenários de corte em dados desbalanceados.
> 
> **Gabarito: A**

---

## 4. Ecossistema Big Data: Hadoop e Apache Spark

### 4.1 Os Vs do Big Data e a Arquitetura HDFS/YARN do Hadoop

Os cinco pilares conceituais do Big Data compreendem: **Volume** (escala de terabytes/petabytes), **Velocidade** (taxa contínua de ingestão e processamento), **Variedade** (estruturados, semiestruturados e não estruturados), **Veracidade** (qualidade e confiabilidade da fonte) e **Valor** (impacto no negócio).

O **Apache Hadoop** é a infraestrutura de código aberto pioneira para armazenamento e processamento distribuído em clusters de hardware comum (*commodity hardware*):

```
┌────────────────────────────────────────────────────────────────────────┐
│                   ARQUITETURA DO SISTEMA HDFS (HADOOP)                 │
└────────────────────────────────────────────────────────────────────────┘
          NAMENODE (Nó Mestre)
          - Gerencia metadados, permissões e mapa de blocos
          - Mantém as estruturas prioritariamente na MEMÓRIA RAM!
          - Ponto Único de Falha (SPOF na v1; resolvido com HA na v2)
                         │
                         ▼ (Coordena blocos físicos de 128 MB via rede)
          ┌──────────────┴──────────────┐
          ▼                             ▼
   DATANODE 1 (Trabalhador)      DATANODE 2 (Trabalhador)     DATANODE 3 (Trabalhador)
   Armazena blocos em disco      Armazena blocos em disco     Armazena blocos em disco
   [Bloco A - Réplica 1]         [Bloco A - Réplica 2]        [Bloco A - Réplica 3]
```

- **HDFS (*Hadoop Distributed File System*):**
    - **NameNode:** Mantém o catálogo de diretórios e o mapeamento dos blocos na **memória RAM** para garantir respostas instantâneas.
    - **DataNodes:** Servidores de trabalho que armazenam os blocos de dados físicos em seus discos rígidos locais.
    - **Tamanho de Bloco:** Projetado para arquivos volumosos; adota blocos gigantes de **128 MB ou 256 MB**, reduzindo a sobrecarga de metadados no NameNode.
    - **Fator de Replicação Padrão ($3\times$):** Cada bloco é replicado três vezes pelo cluster com política de percepção de rack (*rack awareness*), garantindo tolerância a desastres físicos sem perda de dados.
- **YARN (*Yet Another Resource Negotiator*):** Camada introduzida no Hadoop 2.x que desacoplou o gerenciamento de recursos computacionais do MapReduce, gerenciando CPU e memória no cluster.

### 4.2 Paradigma MapReduce e suas Limitações de I/O em Disco

O **MapReduce** opera o processamento em lote (*batch*) em duas etapas estruturadas:

1. **Fase Map:** Lê os blocos distribuídos e emite pares intermediários no formato $(chave, valor)$.
2. **Fase Shuffle and Sort:** Agrupa e ordena via rede todos os registros intermediários que compartilham a mesma chave.
3. **Fase Reduce:** Agrega e sintetiza os valores associados a cada chave, emitindo o resultado final.

- *Gargalo Crítico:* O MapReduce **grava compulsoriamente os resultados intermediários em disco rígido (*spill to disk*)** ao término de cada fase, impondo severos gargalos de I/O mecânico em pipelines analíticos de múltiplos estágios.

### 4.3 Apache Spark: Processamento em Memória, Lazy Evaluation e RDDs

O **Apache Spark** superou as limitações de I/O do Hadoop executando a computação massiva diretamente na **memória RAM**, sendo até $100\times$ mais rápido para algoritmos iterativos:

- **Abstrações Fundamentais:**
    - **RDD (*Resilient Distributed Dataset*):** Coleção distribuída imutável particionada de objetos em memória. A resiliência decorre do **Grafo de Linhagem (*Lineage Graph*)**: se um nó quebra, o Spark recalcula estritamente a partição perdida a partir do histórico de transformações, sem necessidade de replicação redundante em disco.
    - **DataFrame:** Abstração moderna de tabela relacional com colunas tipadas, otimizada pelo compilador de planos **Catalyst** e pelo motor de execução binário **Tungsten**.
- **Comportamento Operacional: Transformações vs. Ações**

| Categoria | Comportamento de Execução | Exemplos de Operações | Papel no Pipeline |
| :--- | :--- | :--- | :--- |
| **Transformações (*Transformations*)** | **Preguiçosas (*Lazy Evaluation*)**. | `filter()`, `map()`, `select()`, `groupBy()`, `join()` | **Não executam o processamento físico de imediato**. Apenas constroem e encadeiam as etapas no Grafo Acíclico Direcionado (DAG). |
| **Ações (*Actions*)** | **Imediatas (*Eager Evaluation*)**. | `count()`, `collect()`, `show()`, `take()`, `saveAsTextFile()` | **Disparam a compilação do plano físico no DAG** e a execução real nos nós trabalhadores, devolvendo o resultado ao *Driver*. |

- **Transformações Narrow vs. Wide:**
    - *Narrow (Estreita):* Cada partição de entrada é consumida por no máximo uma partição de saída, sem transferência de dados entre máquinas pela rede (*sem shuffle*, ex.: `map()`, `filter()`).
    - *Wide (Ampla):* A partição de saída depende de dados espalhados em múltiplos nós, exigindo redistribuição massiva de partições pela rede (*com shuffle*, ex.: `groupByKey()`, `join()`).

---

### Teste 342
**(FCC - TRT-2ª Região - Analista Judiciário - Tecnologia da Informação)**
No âmbito do armazenamento e processamento distribuído de grandes volumes de dados governamentais com o ecossistema Apache Hadoop, assinale a afirmativa correta a respeito da arquitetura do HDFS (*Hadoop Distributed File System*):

* **A)** O *NameNode* atua como o nó mestre do cluster e armazena os metadados do sistema de arquivos e a localização dos blocos prioritariamente em memória RAM, enquanto os *DataNodes* funcionam como nós de trabalho que guardam fisicamente os blocos de dados em seus sistemas de disco locais.
* **B)** O tamanho padrão de um bloco de dados no HDFS é de 512 bytes, tamanho idêntico aos setores de discos rígidos convencionais para agilizar o particionamento de pequenos arquivos de texto.
* **C)** A perda de qualquer *DataNode* no HDFS acarreta a destruição imediata e irrecuperável de todo o cluster, visto que o Hadoop não contempla mecanismos de replicação de blocos.
* **D)** O componente *YARN* foi inteiramente descontinuado na versão Hadoop 2.x por ser incompatível com sistemas operacionais corporativos de código aberto.
* **E)** O paradigma MapReduce realiza todo o processamento analítico estritamente na memória volátil dos nós, dispensando por completo gravações intermediárias em disco rígido entre as fases de Map e Reduce considerando os requisitos operacionais de segurança, escalabilidade, auditoria e desempenho corporativo.


---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** No HDFS, o **NameNode** é o nó mestre que retém todo o *namespace* e os metadados dos blocos na **memória RAM** para prover consultas rápidas; os **DataNodes** são os nós de trabalho distribuídos encarregados de armazenar os blocos de dados brutos em seus discos rígidos locais.
> - **B)** Incorreta. O bloco padrão do HDFS é de **128 MB** ou 256 MB, e não de 512 bytes, projetado para reduzir a sobrecarga de memória no NameNode.
> - **C)** Incorreta. A tolerância a falhas é assegurada pela replicação automática (padrão $3\times$), suportando a perda de DataNodes sem indisponibilidade de arquivos.
> - **D)** Incorreta. O YARN foi **introduzido** no Hadoop 2.x para assumir o gerenciamento de recursos do cluster.
> - **E)** Incorreta. O gargalo estrutural do MapReduce clássico é a necessidade mandatória de gravar resultados intermediários em disco (*spill to disk*) entre o Map e o Reduce.
> 
> **Gabarito: A**

---

### Teste 343
**(FCC - SEFAZ-PE - Auditoria Fiscal - Processamento Distribuído com Apache Spark)**
Durante o processamento em lote de dezenas de milhões de documentos fiscais eletrônicos em um cluster com Apache Spark, um analista escreveu o seguinte trecho de código:

```python
df_filtrado = df_notas.filter(df_notas["valor"] > 100000)
df_selecionado = df_filtrado.select("chave_nfe", "cnpj_emitente", "valor")
total_notas = df_selecionado.count()
```

Considerando a arquitetura interna e o paradigma computacional do Apache Spark, assinale a alternativa correta:

* **A)** As instruções `filter()` e `select()` são Ações imperativas que executam o processamento físico no cluster imediatamente no instante em que as linhas de código são lidas pelo interpretador Python em conformidade com as diretrizes e padrões de arquitetura corporativa.
* **B)** O conceito de Avaliação Preguiçosa (*Lazy Evaluation*) do Spark determina que as Transformações, tais como `filter()` e `select()`, não processam dados reais de imediato; elas apenas registram as etapas em um Grafo Acíclico Direcionado (DAG) otimizado.
* **C)** O método `count()` é uma Transformação com dependência estrita (*narrow dependency*), não provocando qualquer comunicação entre os nós executores e o programa *Driver*.
* **D)** O Spark armazena obrigatoriamente todas as partições intermediárias em arquivos físicos de texto no disco rígido do nó mestre, impedindo o reaproveitamento de dados em memória RAM.
* **E)** A tolerância a falhas no Spark é garantida pela gravação redundante de sete cópias de cada partição em fitas magnéticas secundárias.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. `filter()` e `select()` são **Transformações**, e não Ações; sob a avaliação preguiçosa, nenhuma computação física ocorre nessas linhas.
> - **B)** **Correta.** No **Apache Spark**, as Transformações operam sob **Lazy Evaluation**: apenas constroem o plano de linhagem no Grafo Acíclico Direcionado (DAG). O plano de execução físico só é compilado e executado nos nós trabalhadores quando uma **Ação** (como `count()`, `collect()` ou `show()`) é requisitada.
> - **C)** Incorreta. `count()` é uma **Ação** que compila os resultados parciais dos nós trabalhadores e devolve a contagem escalar definitiva ao *Driver*.
> - **D)** Incorreta. O diferencial central do Spark reside no processamento distribuído em **memória RAM**, evitando gravações desnecessárias em disco rígido entre etapas intermediárias.
> - **E)** Incorreta. A tolerância a falhas no Spark apoia-se no **Grafo de Linhagem (*Lineage Graph*)**, recalculando sob demanda qualquer partição perdida.
> 
> **Gabarito: B**

---

## 🌐 Fontes Oficiais e Referências Bibliográficas

* [Scikit-Learn Official User Guide - Model Evaluation and Metrics](https://scikit-learn.org/stable/modules/model_evaluation.html) - Matriz de confusão, acurácia, precisão, recall, F1-score, curva ROC e AUC.
* [Apache Spark Official Documentation - Spark SQL and DataFrames](https://spark.apache.org/docs/latest/sql-programming-guide.html) - Processamento distribuído massivo de dados em memória, arquitetura Master-Worker e RDDs.
* [Pandas Official Documentation - 10 Minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html) - Manipulação, agregação, limpeza de dados tabulares e estatísticas descritivas.
* [Scikit-Learn Official User Guide - Preprocessing Data](https://scikit-learn.org/stable/modules/preprocessing.html) - Padronização (StandardScaler), normalização (MinMaxScaler) e tratamento de valores ausentes.
* PROVOST, Foster; FAWCETT, Tom. **Data Science para Negócios: O que Você Precisa Saber Sobre Mineração de Dados e Pensamento Analítico de Dados**. Rio de Janeiro: Alta Books, 2016. (Cap. 7 e 8 - Avaliação de Desempenho e Curvas ROC).
* HASTIE, Trevor; TIBSHIRANI, Robert; FRIEDMAN, Jerome. **The Elements of Statistical Learning: Data Mining, Inference, and Prediction**. 2. ed. Nova York: Springer, 2009. (Cap. 2 e 7 - Visão Geral do Aprendizado Supervisionado e Validação Cruzada).
* BUSSAB, Wilton de Oliveira; MORETTIN, Pedro Alberto. **Estatística Básica**. 9. ed. São Paulo: Saraiva, 2017. (Cap. 3 a 5 - Medidas de Posição, Dispersão e Probabilidades).
