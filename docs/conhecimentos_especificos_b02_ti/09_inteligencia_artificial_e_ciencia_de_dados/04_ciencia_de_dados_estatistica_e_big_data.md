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

## 🌐 Fontes Oficiais e Referências Bibliográficas

* [Scikit-Learn Official User Guide - Model Evaluation and Metrics](https://scikit-learn.org/stable/modules/model_evaluation.html) - Matriz de confusão, acurácia, precisão, recall, F1-score, curva ROC e AUC.
* [Apache Spark Official Documentation - Spark SQL and DataFrames](https://spark.apache.org/docs/latest/sql-programming-guide.html) - Processamento distribuído massivo de dados em memória, arquitetura Master-Worker e RDDs.
* [Pandas Official Documentation - 10 Minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html) - Manipulação, agregação, limpeza de dados tabulares e estatísticas descritivas.
* [Scikit-Learn Official User Guide - Preprocessing Data](https://scikit-learn.org/stable/modules/preprocessing.html) - Padronização (StandardScaler), normalização (MinMaxScaler) e tratamento de valores ausentes.
* PROVOST, Foster; FAWCETT, Tom. **Data Science para Negócios: O que Você Precisa Saber Sobre Mineração de Dados e Pensamento Analítico de Dados**. Rio de Janeiro: Alta Books, 2016. (Cap. 7 e 8 - Avaliação de Desempenho e Curvas ROC).
* HASTIE, Trevor; TIBSHIRANI, Robert; FRIEDMAN, Jerome. **The Elements of Statistical Learning: Data Mining, Inference, and Prediction**. 2. ed. Nova York: Springer, 2009. (Cap. 2 e 7 - Visão Geral do Aprendizado Supervisionado e Validação Cruzada).
* BUSSAB, Wilton de Oliveira; MORETTIN, Pedro Alberto. **Estatística Básica**. 9. ed. São Paulo: Saraiva, 2017. (Cap. 3 a 5 - Medidas de Posição, Dispersão e Probabilidades).
