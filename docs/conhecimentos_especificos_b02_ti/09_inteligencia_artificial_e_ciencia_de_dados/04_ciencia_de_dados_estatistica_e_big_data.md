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
**(FGV – TCE-PA – Auditor de Controle Externo Administrativa Ciencia de Dados – 2024)**
Ao se utilizar bancos de dados reais no treinamento de métodos de aprendizado de máquina é normal se deparar com entradas que possuem um ou mais parâmetros (campos) ausentes. Com relação às estratégias para lidar com dados ausentes, analise as afirmativas a seguir. I. Só é possível realizar imputation quando o atributo (feature) ausente é numérico. II. Ao utilizar o k-nearest neighbors (KNN) para fazer o imputation é uma boa estratégia primeiro fazer a normalização ou padronização dos dados. III. Ao se trabalhar com bancos de dados com poucas amostras (itens), uma estratégia usualmente utilizada para lidar com as amostras) que possuem valores ausentes é a remoção. Está correto o que se afirma em

* **A)** I, apenas.
* **B)** II, apenas.
* **C)** III, apenas.
* **D)** I e II apenas.
* **E)** I, II e III.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I, apenas". De acordo com a teoria estudada em *1.1 As Seis Fases do Framework CRISP-DM*, modeling (Modelagem): Escolha de técnicas algorítmicas de aprendizado de máquina (árvores de decisão, regressões, redes neurais), divisão em partições de treino e calibração de hiperparâmetros.
> - **B)** **Correta.** Conforme fundamentado na seção *1.2 Tratamento de Valores Ausentes e Outliers (Critério IQR)* deste guia, *Imputação Avançada:* KNN Imputer (imputa pelo valor ponderado dos \$k\$ vizinhos mais próximos no espaço vetorial) e MICE (*Multivariate Imputation by Chained Equations*). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE-PA/2024) ao estabelecer que "II, apenas".
> - **C)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "III, apenas". De acordo com a teoria estudada em *1.2 Tratamento de Valores Ausentes e Outliers (Critério IQR)*, *Remoção:* Exclusão de linhas (*listwise*) ou colunas. Inviável quando reduz excessivamente o poder estatístico da amostra.
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e II apenas". De acordo com a teoria estudada em *1.2 Tratamento de Valores Ausentes e Outliers (Critério IQR)*, mAR (*Missing at Random*): A probabilidade de o dado faltar relaciona-se sistematicamente com outras variáveis conhecidas da base (ex.: declarações de renda faltam mais frequentemente para determinados perfis etários observados).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "I, II e III". De acordo com a teoria estudada em *1.2 Tratamento de Valores Ausentes e Outliers (Critério IQR)*, o critério do Escore Z (*Z-Score*) (\$Z = \frac{x - \mu}{\sigma}\$) sinaliza anomalias quando \$|Z| > 3\$, pressupondo distribuição aproximadamente normal.
>
> **Gabarito: B**

---

### Teste 334
**(FGV – TCE-PA – Auditor de Controle Externo Administrativa Administracao – 2024)**
A administração de materiais e estoques é uma função crítica na gestão de uma organização, focada na supervisão eficiente e eficaz de materiais e suprimentos necessários para a produção e operações diárias. A tabela seguinte é utilizada pela empresa XYZ para controlar seus estoques: Mês Estoque Inicial Entradas Saídas Estoque Final Jan 150 350 200 300 Fev 300 50 250 100 Mar 100 200 250 50 Abril 50 400 150 300 Maio 300 150 300 150 Junho 150 50 100 200 Assinale a opção que apresenta o número aproximado de vezes que o estoque girou de janeiro a maio.

* **A)** 3,4 vezes.
* **B)** 4,7 vezes.
* **C)** 5,2 vezes.
* **D)** 6,4 vezes.
* **E)** 7,1 vezes.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "3,4 vezes". De acordo com a teoria estudada em *1.1 As Seis Fases do Framework CRISP-DM*, deployment (Implantação): Disponibilização do modelo em ambiente de produção (APIs de auditoria em tempo real, rotinas de escoragem em lote ou dashboards de fiscalização), estabelecendo governança contínua contra degradação temporal do modelo (*model drift* e *concept drift*).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "4,7 vezes". De acordo com a teoria estudada em *1.2 Tratamento de Valores Ausentes e Outliers (Critério IQR)*, mAR (*Missing at Random*): A probabilidade de o dado faltar relaciona-se sistematicamente com outras variáveis conhecidas da base (ex.: declarações de renda faltam mais frequentemente para determinados perfis etários observados).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "5,2 vezes". De acordo com a teoria estudada em *2.2 Distribuições de Probabilidade: Normal, Binomial e Poisson*, modela o número de sucessos \$k\$ em \$n\$ ensaios de Bernoulli independentes com probabilidade de sucesso \$p\$.
> - **D)** **Correta.** Conforme fundamentado na seção *1.1 As Seis Fases do Framework CRISP-DM* deste guia, data Understanding (Compreensão dos Dados): Coleta dos dados brutos preliminares, exploração de tipos de variáveis, inspeção inicial de integridade e formulação das primeiras hipóteses estatísticas. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE-PA/2024) ao estabelecer que "6,4 vezes".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "7,1 vezes". De acordo com a teoria estudada em *4.2 Paradigma MapReduce e suas Limitações de I/O em Disco*, fase Reduce: Agrega e sintetiza os valores associados a cada chave, emitindo o resultado final.
>
> **Gabarito: D**

---

### Teste 335
**(FGV – TJ-AP – Analista Judiciario Apoio Especializado Tecnologia da Informacao Banco de Dados – 2023)**
Uma das primeiras etapas da modelagem multidimensional de dados, para o desenvolvimento de um ambiente de Data Warehouse (DW), é a definição do nível de detalhamento dos dados que serão carregados na tabela fato. Quanto mais detalhado ou atômico, maior será o volume de dados armazenados e maior serão as possibilidades de agregação. O nível de detalhamento dos dados de um DW é definido pelo(a):

* **A)** surrogate key;
* **B)** granularidade;
* **C)** conformed facts;
* **D)** barramento de dados;
* **E)** aditividade das métricas.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "surrogate key". De acordo com a teoria estudada em *1.1 As Seis Fases do Framework CRISP-DM*, data Preparation (Preparação dos Dados): Fase que tradicionalmente consome a maior parcela do esforço do projeto (70% a 80%).
> - **B)** **Correta.** Conforme fundamentado na seção *1.1 As Seis Fases do Framework CRISP-DM* deste guia, data Understanding (Compreensão dos Dados): Coleta dos dados brutos preliminares, exploração de tipos de variáveis, inspeção inicial de integridade e formulação das primeiras hipóteses estatísticas. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ-AP/2023) ao estabelecer que "granularidade".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "conformed facts". De acordo com a teoria estudada em *1.1 As Seis Fases do Framework CRISP-DM*, o CRISP-DM (*Cross-Industry Standard Process for Data Mining*) é o padrão internacional mais adotado para estruturar ciclos analíticos de dados em fases iterativas e interdependentes.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "barramento de dados". De acordo com a teoria estudada em *4.1 Os Vs do Big Data e a Arquitetura HDFS/YARN do Hadoop*, dataNodes: Servidores de trabalho que armazenam os blocos de dados físicos em seus discos rígidos locais.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "aditividade das métricas". De acordo com a teoria estudada em *3.2 Matriz de Confusão e Métricas para Classes Desbalanceadas*, em dados desbalanceados, a acurácia é totalmente inútil, exigindo-se Precisão, Recall e F1-Score.
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
**(CEBRASPE – TJ-RJ – Analista Judiciario Grupo Tecnologia da Informacao Analista de Gestao de Tic – 2021)**
Considere que, em um estudo para avaliar a satisfação dos serviços de comunicação de dados oferecidos por uma operadora, no qual foram utilizadas duas variáveis, X e Y, observou-se que X = 6Y + 24 e que o valor da variância de Y foi igual a 1. Nesse caso, o valor da variância de X é

* **A)** 30.
* **B)** 60.
* **C)** 6.
* **D)** 24.
* **E)** 36.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "30". De acordo com a teoria estudada em *4.2 Paradigma MapReduce e suas Limitações de I/O em Disco*, o MapReduce opera o processamento em lote (*batch*) em duas etapas estruturadas.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "60". De acordo com a teoria estudada em *3.1 O Trade-off Viés vs. Variância (Bias-Variance Tradeoff)*, overfitting (Sobreajuste / Alta Variância): O modelo é hipercomplexo (ex.: árvore de decisão profunda sem limites) e decora as particularidades e ruídos estocásticos do treino, apresentando erro mínimo no treino e erro elevado nos dados inéditos de teste.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "6". De acordo com a teoria estudada em *3.1 O Trade-off Viés vs. Variância (Bias-Variance Tradeoff)*, validação Cruzada k-Fold Estratificada (*Stratified k-Fold*): Divide os dados em \$k\$ partições preservando a mesma proporção percentual das classes em cada dobra, técnica mandatória em problemas desbalanceados.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "24". De acordo com a teoria estudada em *2.1 Medidas de Tendência Central, Dispersão e Assimetria*, variância Amostral (\$s^2\$): \$\frac{1}{n-1}\sum (x_i - \bar{x})^2\$ (utiliza o divisor de Bessel \$n-1\$ para estimador não enviesado).
> - **E)** **Correta.** Conforme fundamentado na seção *1.3 Escalonamento e Codificação de Variáveis Categóricas* deste guia, padronização (StandardScaler / Z-Score): Reescalona a distribuição para apresentar média zero (\$\mu = 0\$) e variância unitária (\$\sigma = 1\$). Dessa forma, está plenamente correta a assertiva da banca (CEBRASPE – TJ-RJ/2021) ao estabelecer que "36".
>
> **Gabarito: E**

---

### Teste 337
**(FGV – TCE-SC – Auditor Fiscal de Controle Externo Administracao – 2026)**
Um Auditor deseja comparar se a média de gastos per capita com educação, nos Municípios da região Oeste de Santa Catarina, é significativamente diferente da média da região Serrana. Ele sabe que a suposição de que tais gastos seguem uma distribuição normal é válida. O método estatístico mais adequado, para comparar as médias dessas duas amostras independentes, é o

* **A)** teste t de Student.
* **B)** teste qui-quadrado.
* **C)** do coeficiente de correlação de Pearson.
* **D)** da regressão logística.
* **E)** da distribuição de Poisson.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "teste t de Student". De acordo com a teoria estudada em *2.3 Testes de Hipóteses, Erros Tipo I e II e Critério do p-Valor*, o \$p\$-valor indica a probabilidade de obter uma estatística de teste tão ou mais extrema que a observada, assumindo \$H_0\$ como verdadeira.
> - **B)** **Correta.** Conforme fundamentado na seção *2.3 Testes de Hipóteses, Erros Tipo I e II e Critério do p-Valor* deste guia, erro Tipo II (\$\beta\$): Não rejeitar \$H_0\$ quando \$H_0\$ é falsa (Falso Negativo estatístico). O complemento \$1 - \beta\$ define o Poder do Teste. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE-SC/2026) ao estabelecer que "teste qui-quadrado".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "do coeficiente de correlação de Pearson". De acordo com a teoria estudada em *2.1 Medidas de Tendência Central, Dispersão e Assimetria*, coeficiente de Variação (CV): \$\text{CV} = \frac{s}{\bar{x}} \times 100\%\$. Medida relativa adimensional que viabiliza a comparação direta da variabilidade entre variáveis de escalas ou grandezas distintas.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "da regressão logística". De acordo com a teoria estudada em *3.3 Curva ROC, AUC-ROC e Métricas de Regressão (MAE, MSE, RMSE, R²)*, mSE (Mean Squared Error): \$\frac{1}{n}\sum (y - \hat{y})^2\$. Penaliza exponencialmente erros grandes ao elevá-los ao quadrado.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "da distribuição de Poisson". De acordo com a teoria estudada em *2.1 Medidas de Tendência Central, Dispersão e Assimetria*, média Aritmética (\$\bar{x}\$): Centro de massa da distribuição (\$\bar{x} = \frac{1}{n}\sum x_i\$). Extremamente vulnerável a distorções por valores discrepantes.
>
> **Gabarito: B**

---

### Teste 338
**(CEBRASPE – TJ-RJ – Analista Judiciario Grupo Tecnologia da Informacao Analista de Gestao de Tic – 2021)**
Considere que um levantamento sobre o número diário de vezes (N) que um usuário observa códigos de erros em determinada página de Internet produziu a tabela de frequências a seguir. N frequência (%) 0 20 1 60 2 10 4 10 total 100 Nesse caso, a diferença entre a média e a mediana da variável N é igual a

* **A)** 0.
* **B)** 0,2.
* **C)** 1.
* **D)** 0,25.
* **E)** 0,75.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "0". De acordo com a teoria estudada em *2.1 Medidas de Tendência Central, Dispersão e Assimetria*, assimetria Positiva (à Direita / Cauda Longa Superior): Típica de dados salariais e contratações públicas onde poucos valores gigantescos puxam a média: \$\text{Moda} < \text{Mediana} < \text{Média}\$.
> - **B)** **Correta.** Conforme fundamentado na seção *2.3 Testes de Hipóteses, Erros Tipo I e II e Critério do p-Valor* deste guia, hipótese Nula (\$H_0\$): Premissa básica de ausência de diferença, conformidade ou efeito padrão. Dessa forma, está plenamente correta a assertiva da banca (CEBRASPE – TJ-RJ/2021) ao estabelecer que "0,2".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "1". De acordo com a teoria estudada em *2.1 Medidas de Tendência Central, Dispersão e Assimetria*, assimetria Negativa (à Esquerda / Cauda Longa Inferior): \$\text{Média} < \text{Mediana} < \text{Moda}\$.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "0,25". De acordo com a teoria estudada em *2.1 Medidas de Tendência Central, Dispersão e Assimetria*, distribuição Simétrica: \$\text{Média} = \text{Mediana} = \text{Moda}\$.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "0,75". De acordo com a teoria estudada em *2.1 Medidas de Tendência Central, Dispersão e Assimetria*, moda (\$Mo\$): O valor que ocorre com a maior frequência estatística observada.
>
> **Gabarito: B**

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
**(CEBRASPE – TRT-8 – Analista Judiciario Area Apoio Especializado Tecnologia da Informacao – 2022)**
Quanto à avaliação de modelos preditivos, assinale a opção correta.

* **A)** A taxa de acerto da métrica de classificação é o complemento da taxa de erro; valores próximos de 0 são considerados melhores.
* **B)** O gráfico ROC é tridimensional, plotado em um espaço chamado de espaço ROC, com eixos X, Y e Z.
* **C)** As duas medidas de erro mais comumente utilizadas na métrica de regressão são o potencial erro definido e a distância média, sempre utilizando números negativos.
* **D)** Nas métricas de classificação, a taxa de erro varia entre 0 e 1, sendo os valores próximos ao extremo 0 melhores.
* **E)** Uma forma de avaliar classificadores em problemas complexos, ou seja, que possuem mais de duas classes, é com o uso das curvas ROC (Receiving Operating Characteristics).

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A taxa de acerto da métrica de classificação é o complemento da taxa de erro; valores próximos de 0 são...". De acordo com a teoria estudada em *3.2 Matriz de Confusão e Métricas para Classes Desbalanceadas*, é a média harmônica entre Precisão e Recall, penalizando severamente modelos desequilibrados que sacrificam uma métrica em favor da outra.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O gráfico ROC é tridimensional, plotado em um espaço chamado de espaço ROC, com eixos X, Y e Z". De acordo com a teoria estudada em *3.3 Curva ROC, AUC-ROC e Métricas de Regressão (MAE, MSE, RMSE, R²)*, mAE (Mean Absolute Error): \$\frac{1}{n}\sum |y - \hat{y}|\$. Erro linear simples, altamente robusto a outliers.
> - **C)** **Incorreta.** A opção promove generalização excessiva que desconsidera as condições técnicas e normativas ao afirmar que "As duas medidas de erro mais comumente utilizadas na métrica de regressão são o potencial erro definido e a...". De acordo com a teoria estudada em *4.3 Apache Spark: Processamento em Memória, Lazy Evaluation e RDDs*, o Apache Spark superou as limitações de I/O do Hadoop executando a computação massiva diretamente na memória RAM, sendo até \$100\times\$ mais rápido para algoritmos iterativos.
> - **D)** **Correta.** Conforme fundamentado na seção *1.2 Tratamento de Valores Ausentes e Outliers (Critério IQR)* deste guia, *Imputação Avançada:* KNN Imputer (imputa pelo valor ponderado dos \$k\$ vizinhos mais próximos no espaço vetorial) e MICE (*Multivariate Imputation by Chained Equations*). Dessa forma, está plenamente correta a assertiva da banca (CEBRASPE – TRT-8/2022) ao estabelecer que "Nas métricas de classificação, a taxa de erro varia entre 0 e 1, sendo os valores próximos ao extremo 0 melhores".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Uma forma de avaliar classificadores em problemas complexos, ou seja, que possuem mais de duas classes, é com o...". De acordo com a teoria estudada em *3.1 O Trade-off Viés vs. Variância (Bias-Variance Tradeoff)*, validação Cruzada k-Fold Estratificada (*Stratified k-Fold*): Divide os dados em \$k\$ partições preservando a mesma proporção percentual das classes em cada dobra, técnica mandatória em problemas desbalanceados.
>
> **Gabarito: D**

---

### Teste 340
**(FGV – TJ-RR – Analista Judiciario Gestao e Governanca de Tecnologia da Informacao – 2024)**
Dados são importantes elementos de apoio à tomada de decisão, sendo que algumas aplicações geram quantidade massiva e heterogênea de dados, com alta velocidade. Para lidar com esse cenário, foi desenvolvido o seguinte modelo de programação que consiste em dividir, processar e combinar os dados em paralelo, de forma a acelerar o processamento e garantir a confiabilidade dos resultados:

* **A)** Data Warehousing.
* **B)** Elastic Search.
* **C)** Hadoop.
* **D)** MapReduce.
* **E)** NoSQL.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Data Warehousing". De acordo com a teoria estudada em *4.1 Os Vs do Big Data e a Arquitetura HDFS/YARN do Hadoop*, os cinco pilares conceituais do Big Data compreendem: Volume (escala de terabytes/petabytes), Velocidade (taxa contínua de ingestão e processamento), Variedade (estruturados, semiestruturados e não estruturados), Veracidade (qualidade e confiabilidade da fonte) e Valor (impacto no negócio).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Elastic Search". De acordo com a teoria estudada em *4.2 Paradigma MapReduce e suas Limitações de I/O em Disco*, *Gargalo Crítico:* O MapReduce grava compulsoriamente os resultados intermediários em disco rígido (*spill to disk*) ao término de cada fase, impondo severos gargalos de I/O mecânico em pipelines analíticos de múltiplos estágios.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Hadoop". De acordo com a teoria estudada em *4.3 Apache Spark: Processamento em Memória, Lazy Evaluation e RDDs*, o Apache Spark superou as limitações de I/O do Hadoop executando a computação massiva diretamente na memória RAM, sendo até \$100\times\$ mais rápido para algoritmos iterativos.
> - **D)** **Correta.** Conforme fundamentado na seção *3.1 O Trade-off Viés vs. Variância (Bias-Variance Tradeoff)* deste guia, overfitting (Sobreajuste / Alta Variância): O modelo é hipercomplexo (ex.: árvore de decisão profunda sem limites) e decora as particularidades e ruídos estocásticos do treino, apresentando erro mínimo no treino e erro elevado nos dados inéditos de teste. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ-RR/2024) ao estabelecer que "MapReduce".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "NoSQL". De acordo com a teoria estudada em *4.2 Paradigma MapReduce e suas Limitações de I/O em Disco*, o MapReduce opera o processamento em lote (*batch*) em duas etapas estruturadas.
>
> **Gabarito: D**

---

### Teste 341
**(FGV – TCE-SC – Auditor Fiscal de Controle Externo Ciencias da Computacao Sistemas de Informacao – 2026)**
Um modelo de classificação foi treinado para identificar transações bancárias fraudulentas. Como as fraudes são eventos muito raros (1 em cada 10.000), o auditor nota que a métrica de Acurácia é enganosa, pois o modelo poderia simplesmente classificar tudo como não fraude, e ainda assim ter 99,99% de acerto. A seguinte métrica seria a mais adequada para avaliar a performance do modelo, nesse cenário de dados altamente desbalanceados, focando na capacidade de detectar o máximo de fraudes reais:

* **A)** acurácia global.
* **B)** recall.
* **C)** precision.
* **D)** erro quadrático médio.
* **E)** coeficiente de correlação r².

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "acurácia global". De acordo com a teoria estudada em *3.2 Matriz de Confusão e Métricas para Classes Desbalanceadas*, a FCC explora exaustivamente a falácia da Acurácia em classes desbalanceadas! Se um tribunal possui uma base com 99% de processos regulares e 1% com fraudes, um modelo tolo que declare "regular" para 100% dos casos terá uma fantástica acurácia de 99%, mas terá detectado zero fraudes (\$0\%\$ de sensibilidade).
> - **B)** **Correta.** Conforme fundamentado na seção *3.2 Matriz de Confusão e Métricas para Classes Desbalanceadas* deste guia, em dados desbalanceados, a acurácia é totalmente inútil, exigindo-se Precisão, Recall e F1-Score. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE-SC/2026) ao estabelecer que "recall".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "precision". De acordo com a teoria estudada em *3.2 Matriz de Confusão e Métricas para Classes Desbalanceadas*, precisão (Precision / Confiabilidade Preditiva).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "erro quadrático médio". De acordo com a teoria estudada em *3.2 Matriz de Confusão e Métricas para Classes Desbalanceadas*, é a média harmônica entre Precisão e Recall, penalizando severamente modelos desequilibrados que sacrificam uma métrica em favor da outra.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "coeficiente de correlação r²". De acordo com a teoria estudada em *3.3 Curva ROC, AUC-ROC e Métricas de Regressão (MAE, MSE, RMSE, R²)*, \$R^2\$ (Coeficiente de Determinação): \$1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}\$, quantificando a proporção da variância explicada pelo modelo.
>
> **Gabarito: B**

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
**(FGV – TCE-SC – Auditor Fiscal de Controle Externo Ciencias da Computacao Sistemas de Informacao – 2026)**
Para processar terabytes de logs de notas fiscais eletrônicas, o TCE-SC utiliza um cluster Apache Spark. O Auditor nota que o processamento está lento devido ao excesso de movimentação de dados entre os nós da rede durante operações de agrupamento. A operação do Spark conhecida por causar esse fenômeno de Shuffle e que deve ser utilizada com cautela em grandes datasets é:

* **A)** map()
* **B)** filter()
* **C)** groupByKey()
* **D)** broadcast()
* **E)** first()

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *4.3 Apache Spark: Processamento em Memória, Lazy Evaluation e RDDs* deste guia, *Narrow (Estreita):* Cada partição de entrada é consumida por no máximo uma partição de saída, sem transferência de dados entre máquinas pela rede (*sem shuffle*, ex.: `map()`, `filter()`). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE-SC/2026) ao estabelecer que "map()".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "filter()". De acordo com a teoria estudada em *4.3 Apache Spark: Processamento em Memória, Lazy Evaluation e RDDs*, transformações (*Transformations*): Preguiçosas (*Lazy Evaluation*). — `filter()`, `map()`, `select()`, `groupBy()`, `join()` — Não executam o processamento físico de imediato. Apenas constroem e encadeiam as etapas no Grafo Acíclico Direcionado (DAG).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "groupByKey()". De acordo com a teoria estudada em *4.3 Apache Spark: Processamento em Memória, Lazy Evaluation e RDDs*, *Wide (Ampla):* A partição de saída depende de dados espalhados em múltiplos nós, exigindo redistribuição massiva de partições pela rede (*com shuffle*, ex.: `groupByKey()`, `join()`).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "broadcast()". De acordo com a teoria estudada em *4.3 Apache Spark: Processamento em Memória, Lazy Evaluation e RDDs*, categoria: Comportamento de Execução — Exemplos de Operações — Papel no Pipeline.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "first()". De acordo com a teoria estudada em *4.2 Paradigma MapReduce e suas Limitações de I/O em Disco*, fase Map: Lê os blocos distribuídos e emite pares intermediários no formato \$(chave, valor)\$.
>
> **Gabarito: A**

---

### Teste 343
**(FGV – TCE-PA – Auditor de Controle Externo Administrativa Ciencia de Dados – 2024)**
Analise o trecho a seguir: É um padrão de transformação de dados em lote que foi introduzido como uma alternativa para lidar com grandes volumes de dados. Consiste em tarefas de mapa que leem blocos de dados individuais espalhados pelos nós, seguidas por uma etapa de shuffle que redistribui os dados de resultado e uma etapa de redução que agrega os dados em cada nó. Seu paradigma foi construído em torno da ideia de que a capacidade e largura de banda do disco magnético eram tão baratas que fazia sentido simplesmente usar uma enorme quantidade de disco para realizar consultas ultrarrápidas. A tecnologia em questão é:

* **A)** Apache Spark.
* **B)** Hadoop MapReduce.
* **C)** Business Warehouse.
* **D)** ETL (Extract, Transform, Load).
* **E)** GIS (Geographic Information System).

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Apache Spark". De acordo com a teoria estudada em *4.3 Apache Spark: Processamento em Memória, Lazy Evaluation e RDDs*, *Wide (Ampla):* A partição de saída depende de dados espalhados em múltiplos nós, exigindo redistribuição massiva de partições pela rede (*com shuffle*, ex.: `groupByKey()`, `join()`).
> - **B)** **Correta.** Conforme fundamentado na seção *4.2 Paradigma MapReduce e suas Limitações de I/O em Disco* deste guia, fase Reduce: Agrega e sintetiza os valores associados a cada chave, emitindo o resultado final. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE-PA/2024) ao estabelecer que "Hadoop MapReduce".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Business Warehouse". De acordo com a teoria estudada em *4.2 Paradigma MapReduce e suas Limitações de I/O em Disco*, o MapReduce opera o processamento em lote (*batch*) em duas etapas estruturadas.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "ETL (Extract, Transform, Load)". De acordo com a teoria estudada em *4.2 Paradigma MapReduce e suas Limitações de I/O em Disco*, fase Shuffle and Sort: Agrupa e ordena via rede todos os registros intermediários que compartilham a mesma chave.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "GIS (Geographic Information System)". De acordo com a teoria estudada em *4.2 Paradigma MapReduce e suas Limitações de I/O em Disco*, fase Map: Lê os blocos distribuídos e emite pares intermediários no formato \$(chave, valor)\$.
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
