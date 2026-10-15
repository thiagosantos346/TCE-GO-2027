# Módulo 09: Inteligência Artificial e Ciência de Dados
## 01. Fundamentos de IA, Machine Learning e Deep Learning

**Última Atualização:** 2026-03-31  
**Banca Foco:** FCC (Fundação Carlos Chagas)  
**Cargo:** Auditor de Controle Externo - Tecnologia da Informação  
**Status do Mapeamento:** 100% aderente ao edital TCE-GO

---

### 📌 Ementa / Itens do Edital
1. **Fundamentos e Histórico da Inteligência Artificial:** Definições clássicas de Russell & Norvig; Teste de Turing, Quarto Chinês de Searle; IA Estreita (*Narrow AI*) vs. IA Geral (*AGI*) vs. Superinteligência (*ASI*); Paradigma Simbólico (*Sistemas Especialistas*) vs. Paradigma Conexionista (*Subsimbólico/Estatístico*); Conceito formal de Agente Racional.
2. **Aprendizado de Máquina (Machine Learning):**
   - **Aprendizado Supervisionado:** Tarefas de Classificação (Regressão Logística, Árvores de Decisão com Entropia/Gini, SVM com hiperplano de margem máxima e kernel trick, Naive Bayes com suposição de independência condicional, k-NN com cálculo de distâncias) e Tarefas de Regressão (Regressão Linear via OLS, Regularização Ridge com norma $L_2$ e Lasso com norma $L_1$ para seleção de atributos, Elastic Net).
   - **Métodos de Ensemble:** Bagging (*Random Forest* com amostragem bootstrap e subespaço aleatório de features para redução de variância) vs. Boosting (*AdaBoost*, *Gradient Boosting*, *XGBoost* e *LightGBM* com treinamento sequencial focado em resíduos para redução de viés).
   - **Aprendizado Não Supervisionado:** Agrupamento/Clustering (K-Means com inércia e método do cotovelo, DBSCAN com densidade, pontos núcleo/borda/ruído para detecção de anomalias, Agrupamento Hierárquico com dendrogramas e abordagens aglomerativa/divisiva) e Redução de Dimensionalidade (PCA com autovalores/autovetores e máxima variância, t-SNE e UMAP).
   - **Aprendizado por Reforço:** Agente, Ambiente, Estado, Ação, Recompensa, Processos de Decisão de Markov (MDP), Equação de Bellman, Dilema *Exploration vs. Exploitation* e Q-Learning.
3. **Redes Neurais Artificiais e Deep Learning:**
   - **Arquitetura e Fundamentos:** Perceptron de Rosenblatt (pesos, bias, soma ponderada), limitação linear e problema do XOR (Minsky & Papert); Perceptron Multicamadas (MLP) e Teorema da Aproximação Universal.
   - **Funções de Ativação Não Lineares:** Sigmoide (desvanecimento do gradiente), Tangente Hiperbólica ($\tanh$ centrada em zero), ReLU (padrão em camadas ocultas e patologia do *Dying ReLU*) e Softmax (restrita à camada de saída multiclasse).
   - **Treinamento e Otimização:** Funções de Perda (MSE, Entropia Cruzada Binária e Categórica), Retropropagação (*Backpropagation* via Regra da Cadeia), Gradiente Descendente e Otimizadores (SGD, Momentum, RMSprop e Adam), Regularização (Dropout, Batch Normalization e Early Stopping).
   - **Arquiteturas Especializadas:** Redes Convolucionais (CNNs: filtros convolucionais, compartilhamento de pesos, pooling e invariância translacional para visão computacional); Redes Recorrentes (RNNs, LSTM com portas de esquecimento/entrada/saída e GRU); e Arquitetura Transformer (mecanismo de autoatenção pura).

---

### 🧭 Sumário
- [1. Fundamentos e Paradigmas da Inteligência Artificial](#1-fundamentos-e-paradigmas-da-inteligência-artificial)
  - [1.1 Dimensões de Russell & Norvig e o Conceito de Agente Racional](#11-dimensões-de-russell--norvig-e-o-conceito-de-agente-racional)
  - [1.2 Níveis de IA: Narrow AI vs. AGI vs. Superinteligência](#12-níveis-de-ia-narrow-ai-vs-agi-vs-superinteligência)
  - [1.3 Paradigma Simbólico vs. Paradigma Conexionista](#13-paradigma-simbólico-vs-paradigma-conexionista)
- [2. Aprendizado de Máquina Supervisionado](#2-aprendizado-de-máquina-supervisionado)
  - [2.1 Modelos e Algoritmos de Classificação](#21-modelos-e-algoritmos-de-classificação)
  - [2.2 Comitês de Modelos (Ensemble): Bagging vs. Boosting](#22-comitês-de-modelos-ensemble-bagging-vs-boosting)
  - [2.3 Modelos de Regressão e Técnicas de Regularização (Ridge, Lasso e Elastic Net)](#23-modelos-de-regressão-e-técnicas-de-regularização-ridge-lasso-e-elastic-net)
- [3. Aprendizado Não Supervisionado e por Reforço](#3-aprendizado-não-supervisionado-e-por-reforço)
  - [3.1 Algoritmos de Agrupamento (Clustering: K-Means, DBSCAN e Hierárquico)](#31-algoritmos-de-agrupamento-clustering-k-means-dbscan-e-hierárquico)
  - [3.2 Redução de Dimensionalidade (PCA, t-SNE e UMAP)](#32-redução-de-dimensionalidade-pca-t-sne-e-umap)
  - [3.3 Aprendizado por Reforço (Reinforcement Learning)](#33-aprendizado-por-reforço-reinforcement-learning)
- [4. Redes Neurais Artificiais e Deep Learning](#4-redes-neurais-artificiais-e-deep-learning)
  - [4.1 Perceptron, Limitações Lineares e Redes Multicamadas (MLP)](#41-perceptron-limitações-lineares-e-redes-multicamadas-mlp)
  - [4.2 Funções de Ativação Não Lineares e suas Patologias](#42-funções-de-ativação-não-lineares-e-suas-patologias)
  - [4.3 Treinamento: Backpropagation, Gradiente Descendente e Otimizadores](#43-treinamento-backpropagation-gradiente-descendente-e-otimizadores)
  - [4.4 Arquiteturas Profundas: CNNs, RNNs/LSTM e Transformers](#44-arquiteturas-profundas-cnns-rnnslstm-e-transformers)
- [5. Questões Comentadas (FCC)](#5-questões-comentadas-fcc)

---

## 1. Fundamentos e Paradigmas da Inteligência Artificial

A Inteligência Artificial (IA) estuda e projeta entidades computacionais capazes de realizar tarefas cognitivas historicamente associadas à inteligência biológica humana, tais como percepção visual, tomada de decisão sob incerteza, raciocínio lógico dedutivo e aprendizado contínuo.

### 1.1 Dimensões de Russell & Norvig e o Conceito de Agente Racional

A taxonomia formal estabelecida por Stuart Russell e Peter Norvig estrutura as abordagens de IA em uma matriz quadrante baseada em duas dimensões fundamentais:

```
                          FIDELIDADE AO HUMANO          FIDELIDADE À RACIONALIDADE
                   ┌──────────────────────────────┬──────────────────────────────┐
  FOCO NO PROCESSO │    PENSAR COMO HUMANOS       │      PENSAR RACIONALMENTE    │
    DE PENSAMENTO  │ (Ciência Cognitiva, Modelagem│ (Lógica Formal, Silogismos   │
                   │  Empírica do Cérebro Humano) │  Aristotélicos, Leis da Mente│
                   ├──────────────────────────────┼──────────────────────────────┤
  FOCO NO COMPOR-  │      AGIR COMO HUMANOS       │       AGIR RACIONALMENTE     │
      TAMENTO      │ (Teste de Turing de 1950,    │ (Agente Racional, Maximização│
   (AÇÃO VISÍVEL)  │  Processamento de Linguagem) │  da Utilidade/Desempenho)    │
                   └──────────────────────────────┴──────────────────────────────┘
```

1. **Agir como Humanos:** Medido operacionalmente pelo célebre **Teste de Turing (1950)**. Se um avaliador humano interagindo via terminal de texto não for capaz de distinguir confiavelmente se as respostas procedem de um operador humano ou de um computador, o sistema é considerado aprovado no teste comportamental. O filósofo John Searle contra-argumentou com o experimento mental do **Quarto Chinês (*Chinese Room*)**, afirmando que a mera manipulação sintática de regras e símbolos não confere compreensão semântica ou consciência real à máquina.
2. **Pensar como Humanos:** Procura reproduzir fielmente os processos mentais e psicológicos dos seres humanos por meio da intersecção entre modelos computacionais de IA e técnicas experimentais da psicologia e neurociência cognitiva.
3. **Pensar Racionalmente:** Baseia-se em sistemas de lógica formal dedutiva (silogismos e cálculo proposicional). Limitação prática: incapacidade de lidar eficientemente com incertezas, dados probabilísticos e o conhecimento informal difuso do mundo real.
4. **Agir Racionalmente (Abordagem de Agentes Racionais):** Paradigma predominante na ciência da computação contemporânea. Um **Agente Racional** é definido formalmente como uma entidade autônoma que:
   - Percebe seu ambiente operacional por meio de **Sensores**;
   - Processa computacionalmente esse fluxo perceptivo através de uma **Função de Agente** interna;
   - Executa intervenções físicas ou virtuais no ambiente através de **Atuadores** com o objetivo explícito de **maximizar a sua medida de desempenho esperada**.

> ⚠️ **Alerta de Prova (FCC):**
> A banca FCC costuma cobrar com frequência a definição canônica de **Agente Racional**. Fixe bem: a racionalidade não significa perfeição, onisciência ou clarividência humana. A racionalidade computacional busca maximizar o resultado esperado em face do conhecimento histórico acumulado pelo agente e das percepções recebidas pelos seus sensores no momento da decisão.

### 1.2 Níveis de IA: Narrow AI vs. AGI vs. Superinteligência

* **IA Estreita / Fraca (*Narrow AI* ou *Weak AI*):**
  - Sistemas computacionais altamente especializados, construídos e treinados para solucionar **uma tarefa restrita e delimitada**.
  - Exemplos: Classificação de transações fraudulentas pelo TCE-GO, sistemas de reconhecimento facial, motores de recomendação de comércio eletrônico, grandes modelos de linguagem (LLMs) e motores de xadrez/Go. **Toda a inteligência artificial desenvolvida e operacional no mundo atual pertence exclusivamente à categoria Narrow AI**.
* **IA Geral / Forte (*Artificial General Intelligence - AGI*):**
  - Sistema hipotético dotado de plasticidade e capacidade cognitiva comparáveis ou equivalentes às de um ser humano adulto. Uma AGI deve ser capaz de aprender, raciocinar, transferir aprendizado entre domínios totalmente distintos e solucionar desafios inéditos sem a necessidade de reconfiguração algorítmica ou retreinamento supervisionado por humanos.
* **Superinteligência Artificial (*Artificial Superintelligence - ASI*):**
  - Estágio teórico em que a capacidade cognitiva de uma entidade de silício ultrapassa exponencialmente a capacidade intelectual combinada de todos os cérebros humanos da Terra em todas as disciplinas criativas, científicas, estratégicas e sociais.

### 1.3 Paradigma Simbólico vs. Paradigma Conexionista

A trajetória histórica da IA subdivide-se em duas correntes metodológicas centrais:
- **Paradigma Simbólico (IA Clássica / GOFAI - *Good Old-Fashioned AI*):**
  - Abordagem *top-down* orientada à manipulação lógica de símbolos, árvores de inferência dedutiva e bases de regras determinísticas do tipo `SE <condição> ENTÃO <ação>`.
  - Seu apogeu deu-se nas décadas de 1970 e 1980 com os **Sistemas Especialistas** (*Expert Systems*).
  - *Vantagem:* Total interpretabilidade, transparência explicativa e facilidade de auditoria (*white box*).
  - *Gargalo Histórico:* Dificuldade extrema de codificar regras manuais para conhecimento implícito complexo (*knowledge acquisition bottleneck*) e total fragilidade perante ruídos em dados não estruturados (áudio, vídeo, imagens).
- **Paradigma Conexionista / Subsimbólico:**
  - Abordagem *bottom-up* inspirada na neurobiologia humana e modelada em redes matemáticas densas de nós processadores interconectados por pesos sinápticos numéricos ajustáveis (Redes Neurais Artificiais e modelos estatísticos).
  - O conhecimento não reside em regras textuais explícitas, mas sim distribuído nos pesos numéricos aprendidos por otimização estatística direta sobre grandes massas de dados.
  - *Vantagem:* Robustez incomparável a ruídos estatísticos e capacidade superior de extrair padrões latentes de alta dimensionalidade (processamento de linguagem natural e visão computacional).
  - *Desvantagem:* Natureza de "caixa-preta" (*black box*), opacidade decisória e altíssimo custo de processamento computacional em GPUs/TPUs.

---

## 2. Aprendizado de Máquina Supervisionado

O Aprendizado Supervisionado opera sobre conjuntos de dados históricos previamente rotulados, formalizados pelo conjunto de treino $\{(x_1, y_1), (x_2, y_2), \dots, (x_n, y_n)\}$, onde $x_i$ representa o vetor de características (*features*) e $y_i$ representa o rótulo verdadeiro (*ground truth*). O objetivo do algoritmo é estimar uma função $f(x) \approx y$ com alta capacidade de generalização para amostras inéditas.

### 2.1 Modelos e Algoritmos de Classificação

Quando a variável dependente $y$ é de natureza discreta/categórica (ex.: `0` para contratação idônea e `1` para superfaturada), o problema enquadra-se como **Classificação**:

1. **Regressão Logística:**
   - Apesar do termo "regressão", é um algoritmo de **classificação linear**. Estima a probabilidade a posteriori de uma classe binária através da função logística sigmoide:
     $$P(y=1|\mathbf{x}) = \sigma(\mathbf{w}^T \mathbf{x} + b) = \frac{1}{1 + e^{-(\mathbf{w}^T \mathbf{x} + b)}}$$
   - A fronteira de separação entre as classes é estritamente linear ($\mathbf{w}^T \mathbf{x} + b = 0$). O treinamento minimiza a função de perda de Entropia Cruzada Binária (*Log-Loss*).

2. **Árvores de Decisão (*Decision Trees*):**
   - Modelos hierárquicos não paramétricos compostos por nós de decisão, ramos e folhas que dividem recursivamente o espaço de atributos.
   - **Critérios de Divisão de Nós:**
     - *Entropia e Ganho de Informação (Algoritmos ID3 e C4.5):* A Entropia mede o grau de desordem ou incerteza dos dados:
       $$\text{Entropia}(S) = - \sum_{i=1}^{c} p_i \log_2(p_i)$$
       O algoritmo escolhe a divisão que maximiza a redução de entropia (Ganho de Informação).
     - *Índice de Impureza Gini (Algoritmo CART):* Mede a probabilidade de um elemento aleatório ser incorretamente classificado:
       $$\text{Gini}(S) = 1 - \sum_{i=1}^{c} p_i^2$$
   - Árvores de decisão profundas e sem limites de crescimento sofrem gravemente de **sobreajuste (*overfitting*)** (alta variância). Para mitigar essa patologia, aplicam-se técnicas de poda prévia (*pre-pruning*, limitando a profundidade máxima `max_depth` ou número mínimo de amostras por nó) e poda posterior (*post-pruning* via complexidade de custo).

3. **Support Vector Machines (SVM):**
   - Constrói o **hiperplano de separação ótimo** que maximiza a distância geométrica perpendicular (**margem de separação**) até as instâncias mais próximas de cada classe.
   - **Vetores de Suporte:** São unicamente as instâncias críticas situadas sobre as fronteiras da margem que determinam a posição matemática e inclinação do hiperplano; todos os outros pontos podem ser adicionados ou removidos sem afetar a solução ótima.
   - **Hiperparâmetro $C$ (Margem Suave):** Controla o compromisso entre a largura da margem e a tolerância a erros de classificação: um $C$ elevado penaliza violações severamente (margem estreita, risco de sobreajuste); um $C$ baixo admite mais violações em troca de margens mais amplas (maior viés e melhor generalização).
   - **Truque do Kernel (*Kernel Trick*):** Permite resolver problemas não linearmente separáveis sem a necessidade de calcular explicitamente as coordenadas em um espaço de dimensão infinita ou muito alta, substituindo o produto escalar por uma função de kernel: Linear, Polinomial ou Gaussiano RBF (*Radial Basis Function*).

4. **Naive Bayes:**
   - Classificador probabilístico alicerçado diretamente no Teorema de Bayes:
     $$P(y|\mathbf{X}) = \frac{P(\mathbf{X}|y) P(y)}{P(\mathbf{X})}$$
   - **Suposição "Ingênua" (*Naive*):** Assume categoricamente que todos os atributos preditores $x_1, x_2, \dots, x_d$ são **mutuamente independentes entre si, dado o rótulo de classe $y$**:
     $$P(\mathbf{X}|y) = \prod_{j=1}^{d} P(x_j|y)$$
   - Apesar dessa premissa ser quase sempre violada no mundo real, apresenta eficácia e velocidade ímpares na filtragem de spam, análise de sentimento e classificação de textos jurídicos.

5. **k-Nearest Neighbors (k-NN):**
   - Algoritmo não-paramétrico **baseado em instâncias** (*instance-based*) e classificado como **aprendizado preguiçoso (*lazy learning*)**, pois não possui uma fase de treinamento explícita que gere coeficientes ou modelos matemáticos: ele simplesmente memoriza todos os dados de treino na memória.
   - Durante a inferência, calcula a distância (Euclidiana, Manhattan ou Minkowski) entre a nova amostra e todos os pontos históricos da base, atribuindo a classe majoritária entre os $k$ vizinhos mais próximos. Sofre severamente com a **maldição da dimensionalidade** (*curse of dimensionality*).

### 2.2 Comitês de Modelos (Ensemble): Bagging vs. Boosting

A combinação coordenada de múltiplos estimadores fracos (*weak learners*) permite construir comitês com capacidade preditiva muito superior à de qualquer modelo individual isolado:

```
[BAGGING - Random Forest]
 Amostra Bootstrap 1 ──► [Árvore Profunda 1] ──┐
 Amostra Bootstrap 2 ──► [Árvore Profunda 2] ──┼──► Votação Majoritária (Média)
 Amostra Bootstrap N ──► [Árvore Profunda N] ──┘    Reduz a VARIÂNCIA (Overfitting)
 (Treinamento em PARALELO e INDEPENDENTE)

[BOOSTING - XGBoost / AdaBoost]
 Dataset ──► [Modelo Fraco 1] ──(Resíduos/Erros)──► [Modelo Fraco 2] ──(Resíduos)──► ...
 (Treinamento SEQUENCIAL / ADAPTATIVO)               Reduz o VIÉS (Underfitting)
```

| Critério Comparativo | Bagging (Bootstrap Aggregating) | Boosting |
| :--- | :--- | :--- |
| **Arquitetura de Treinamento** | **Paralela** e estritamente independente. | **Sequencial**, cumulativa e adaptativa. |
| **Tratamento dos Dados** | Reamostragem com reposição (*Bootstrap*) aleatória uniforme. | Reamostragem ponderada: instâncias mal classificadas recebem maior peso no próximo ciclo. |
| **Foco Matemático no Erro** | **Reduzir a Variância** (combater a tendência ao *overfitting* de modelos complexos). | **Reduzir o Viés** (combater o *underfitting* transformando modelos simples em preditores fortes). |
| **Estimadores de Base Típicos** | Modelos complexos e profundos com baixo viés e alta variância (ex.: árvores de decisão não podadas). | Estimadores fracos e rasos intencionalmente simples (ex.: árvores de profundidade 1 a 3, chamadas *decision stumps*). |
| **Agregação Final** | Média aritmética simples (em regressão) ou voto da maioria (em classificação). | Combinação linear ponderada pela performance de cada modelo fraco no histórico. |
| **Algoritmos Canônicos** | **Random Forest**, Extra Trees. | **AdaBoost, Gradient Boosting, XGBoost, LightGBM, CatBoost**. |

> ⚠️ **Alerta de Prova (FCC):**
> A FCC adora inverter os papéis do Bagging e do Boosting em questões de TI e Ciência de Dados:
> 1. No **Random Forest (Bagging)**, as árvores são geradas em **paralelo**. Além do bootstrap nas linhas, o algoritmo sorteia aleatoriamente um subconjunto de variáveis (*feature subsampling*, comumente $\sqrt{p}$) na divisão de cada nó. Isso descorrelaciona as árvores e derruba a **variância**.
> 2. No **Boosting**, as árvores são geradas em **série sequencial**, onde cada árvore aprende a prever os **resíduos/erros** gerados pelo somatório das anteriores, reduzindo drasticamente o **viés**.

### 2.3 Modelos de Regressão e Técnicas de Regularização (Ridge, Lasso e Elastic Net)

Quando a variável de saída $y$ é contínua (ex.: estimativa do valor de sobrepreço em obras públicas), emprega-se a **Regressão**.
O método clássico dos **Mínimos Quadrados Ordinários (OLS - *Ordinary Least Squares*)** minimiza o Erro Quadrático Médio ($\text{MSE}$). Em bases com dezenas ou centenas de variáveis multicolineares, o OLS produz coeficientes com variância gigante e sobreajuste.

Para estabilizar o modelo, adiciona-se uma penalidade matemática $\lambda \cdot \Omega(\mathbf{w})$ à função de perda:

```
[Geometria das Restrições de Regularização]
     Penalidade L2 (Ridge)                      Penalidade L1 (Lasso)
             w2                                         w2
             ▲                                          ▲
          ┌──┴──┐                                       /\
         /   │   \                                     /  \
        │────┼────│ w1                                /────┼────\ w1
         \   │   /                                     \  /
          └──┬──┘                                       \/
             ▼                                          ▼
   (Esfera lisa: encolhe coeficientes         (Losango pontiagudo nos eixos:
    sem zerar rigorosamente nenhum)             zera coeficientes irrelevantes)
```

1. **Regressão Ridge (Penalidade com Norma $L_2$):**
   - Adiciona a soma dos quadrados dos coeficientes:
     $$\mathcal{L}_{\text{Ridge}} = \text{MSE} + \lambda \sum_{j=1}^{p} w_j^2$$
   - Por ser suave e esférica, a penalidade $L_2$ **encolhe (*shrinks*) continuamente a magnitude dos coeficientes** em direção a zero à medida que $\lambda$ cresce, **mas nunca força nenhum coeficiente a se tornar rigorosamente zero**. Excelente para mitigar multicolinearidade severa.
2. **Regressão Lasso (*Least Absolute Shrinkage and Selection Operator* - Norma $L_1$):**
   - Adiciona a soma dos valores absolutos dos coeficientes:
     $$\mathcal{L}_{\text{Lasso}} = \text{MSE} + \lambda \sum_{j=1}^{p} |w_j|$$
   - Devido aos vértices pontiagudos nos eixos da geometria em losango da norma $L_1$, a solução de custo mínimo toca os eixos cartesianos, **forçando coeficientes irrelevantes a se tornarem EXATAMENTE ZERO**.
   - O Lasso executa simultaneamente contração e **seleção automática de atributos (*feature selection*)**, produzindo modelos parcimoniosos e esparsos.
3. **Elastic Net:**
   - Combinação convexa das penalidades $L_1$ e $L_2$:
     $$\mathcal{L}_{\text{ElasticNet}} = \text{MSE} + \lambda \left[ \alpha \sum_{j=1}^{p} |w_j| + \frac{1-\alpha}{2} \sum_{j=1}^{p} w_j^2 \right]$$
   - Une a capacidade de gerar modelos esparsos do Lasso com a capacidade do Ridge de manter grupos inteiros de variáveis correlacionadas dentro do modelo.

---

## 3. Aprendizado Não Supervisionado e por Reforço

### 3.1 Algoritmos de Agrupamento (Clustering: K-Means, DBSCAN e Hierárquico)

O agrupamento descobre partições ou morfologias naturais em dados não rotulados:

1. **K-Means (Agrupamento Particional por Centroides):**
   - O algoritmo requer a especificação prévia do número de clusters ($k$).
   - Minimiza a variação intra-cluster somando as distâncias euclidianas quadráticas dos pontos até o centroide correspondente (**Inércia** ou WCSS):
     $$\text{WCSS} = \sum_{k=1}^{K} \sum_{\mathbf{x}_i \in C_k} \|\mathbf{x}_i - \boldsymbol{\mu}_k\|^2$$
   - O número ideal $k$ é avaliado visualmente pelo **Método do Cotovelo (*Elbow Method*)** ou pelo **Coeficiente de Silhueta** (que oscila entre $-1$ e $+1$).
   - *Limitações Clássicas:* Assume que todos os clusters são convexos e esféricos com variâncias semelhantes. Falha completamente na identificação de formatos orgânicos alongados e atribui compulsoriamente todo ponto a algum cluster, sendo muito sensível a *outliers*.

2. **DBSCAN (*Density-Based Spatial Clustering of Applications with Noise*):**
   - Agrupa os dados com base na **densidade espacial local**, orientando-se por dois parâmetros: raio de vizinhança ($\varepsilon$) e número mínimo de pontos (*min_samples*).
   - Tipologia dos pontos:
     - *Ponto Núcleo (Core Point):* Possui pelo menos *min_samples* pontos em seu raio $\varepsilon$.
     - *Ponto de Borda (Border Point):* Não é núcleo, mas situa-se no raio $\varepsilon$ de um núcleo.
     - *Ruído / Outlier (Noise):* Não é núcleo nem borda (cai em regiões de baixa densidade).
   - *Vantagens Essenciais:* **Não requer a definição prévia da quantidade de grupos ($k$)**, detecta agrupamentos de **formatos geométricos arbitrários e não convexos** e **isola explicitamente ruídos e anomalias**, constituindo o algoritmo perfeito para detecção de fraudes em auditorias de controle externo.

3. **Agrupamento Hierárquico (*Hierarchical Clustering*):**
   - Gera uma representação em árvore taxonômica denominada **Dendrograma**.
   - Abordagem **Aglomerativa (*Bottom-up*)**: Cada ponto inicia como seu próprio cluster e pares mais próximos são progressivamente fundidos.
   - Métodos de Ligação (*Linkage*): *Single* (distância mínima entre membros, suscetível ao efeito de encadeamento /*chaining*), *Complete* (distância máxima), *Average* (distância média) e *Ward* (minimiza o incremento da variância total interna).

### 3.2 Redução de Dimensionalidade (PCA, t-SNE e UMAP)

Reduz a quantidade de preditores de um dataset volumoso preservando a maior quantidade possível de variância estatística ou vizinhança:
- **PCA (*Principal Component Analysis*):**
  - Técnica estatística **linear e não supervisionada** que transforma as variáveis originais em um novo conjunto de variáveis não correlacionadas denominadas **Componentes Principais (PCs)**.
  - O primeiro componente principal captura a direção de **máxima variância** dos dados; o segundo componente captura a segunda maior variância sob a restrição de ser rigorosamente **ortogonal** ao primeiro, e assim por diante.
  - Obtido computacionalmente através da **decomposição espectral (autovalores e autovetores)** da matriz de covariância dos dados padronizados ou por decomposição em valores singulares (SVD).
- **t-SNE e UMAP:**
  - Métodos **não lineares** dedicados prioritariamente à projeção de espaços de centenas de dimensões em espaços de 2D ou 3D para inspeção visual humana, preservando topologias de vizinhança local.

### 3.3 Aprendizado por Reforço (Reinforcement Learning)

Um **Agente** aprende a tomar decisões sequenciais ideais através de tentativa e erro, interagindo iterativamente com um **Ambiente** dinâmico:
- Formalizado matematicamente por um **Processo de Decisão de Markov (MDP)**, representado pela 5-tupla $(S, A, P, R, \gamma)$.
- A cada instante $t$, o agente observa o estado $S_t$, executa uma ação $A_t$ orientada por sua política $\pi(a|s)$, recebe uma recompensa escalar imediata $R_{t+1}$ e transiciona para o novo estado $S_{t+1}$.
- O objetivo é aprender uma política ótima que maximize o retorno cumulativo descontado no longo prazo ($G_t = \sum_{k=0}^{\infty} \gamma^k R_{t+k+1}$), governado pela **Equação de Bellman**.
- **Dilema Exploração vs. Explotação (*Exploration vs. Exploitation*):** O agente deve arbitrar entre descobrir ações inéditas (*exploration*) para colher melhores recompensas futuras e executar as ações que já provaram ser eficazes (*exploitation*).
- **Q-Learning:** Algoritmo clássico de aprendizado por diferença temporal, classificado como *model-free* e *off-policy*, que atualiza recursivamente os valores $Q(s, a)$ da função de valor ação-estado.

---

## 4. Redes Neurais Artificiais e Deep Learning

O Aprendizado Profundo (*Deep Learning*) fundamenta-se em arquiteturas com múltiplas camadas ocultas empilhadas capazes de extrair representações hierárquicas e abstratas de dados não estruturados de ponta a ponta (*end-to-end*).

### 4.1 Perceptron, Limitações Lineares e Redes Multicamadas (MLP)

* **O Neurônio Artificial (Perceptron de Rosenblatt - 1958):**
  Calcula a soma ponderada de suas entradas multiplicadas pelos pesos sinápticos, soma um coeficiente linear de ajuste (**bias** $b$) e submete o resultado a uma função de ativação:
  $$z = \sum_{i=1}^{m} w_i x_i + b = \mathbf{w}^T \mathbf{x} + b, \quad \hat{y} = f(z)$$
  Em 1969, Marvin Minsky e Seymour Papert demonstraram matematicamente que o Perceptron de camada única só é capaz de resolver funções linearmente separáveis, sendo **completamente incapaz de resolver o problema do OU-Exclusivo (XOR)**.
* **Perceptron Multicamadas (MLP - *Multilayer Perceptron*):**
  A introdução de uma ou mais **camadas ocultas (*hidden layers*)** com **funções de ativação não lineares** resolveu essa limitação histórica. Segundo o **Teorema da Aproximação Universal** (Cybenko, 1989 / Hornik, 1991), uma rede MLP feedforward com uma única camada oculta contendo uma quantidade finita de neurônios não lineares é capaz de aproximar qualquer função contínua arbitrária com precisão pré-estabelecida.

### 4.2 Funções de Ativação Não Lineares e suas Patologias

As funções de ativação inserem a não linearidade necessária para que o empilhamento de camadas neurais não colapse matematicamente em uma única transformação afim linear:

| Função de Ativação | Fórmula Matemática | Faixa de Saída (*Range*) | Características Operacionais | Patologia Crítica / Cuidados de Projeto |
| :--- | :--- | :--- | :--- | :--- |
| **Sigmoide** | $\sigma(z) = \frac{1}{1 + e^{-z}}$ | $(0, 1)$ | Saída probabilística interpretável; curva em formato de "S". | Sofre com a **Saturação e Desvanecimento do Gradiente (*Vanishing Gradient*)**: quando $|z|$ é grande, sua derivada tende a zero, anulando a atualização das camadas iniciais. Saída não é centrada em zero. |
| **Tangente Hiperbólica (tanh)** | $\tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}$ | $(-1, 1)$ | Saída **centrada em zero**, o que acelera a convergência dos gradientes em comparação à sigmoide. | Também satura nas caudas e sofre de desvanecimento de gradientes em redes profundas. |
| **ReLU (*Rectified Linear Unit*)** | $f(z) = \max(0, z)$ | $[0, +\infty)$ | **Padrão da indústria para camadas ocultas**. Não satura para valores positivos ($z > 0$, onde a derivada é $1$), permitindo treinar redes profundas rapidamente sem vanishing gradient. | **Problema do Neurônio Morto (*Dying ReLU*)**: se uma entrada $z \le 0$, tanto a saída quanto a derivada tornam-se zero. Um neurônio empurrado para essa região inerte pode nunca mais atualizar seus pesos. |
| **Softmax** | $\sigma(\mathbf{z})_i = \frac{e^{z_i}}{\sum_{j=1}^{K} e^{z_j}}$ | $(0, 1)$, $\sum \sigma_i = 1$ | Converte o vetor de valores reais brutos (*logits*) em uma **distribuição de probabilidades normalizada**. | **Exclusiva da camada de saída** em problemas de classificação multiclasse mutualmente exclusivos. **Nunca deve ser usada em camadas ocultas intermediárias**. |

### 4.3 Treinamento: Backpropagation, Gradiente Descendente e Otimizadores

O ciclo de aprendizado de redes profundas articula quatro etapas fundamentais:
1. **Propagação Direta (*Forward Pass*):** Os dados avançam pelas camadas da rede até produzir uma saída predita $\hat{y}$, que é comparada ao rótulo real $y$ através de uma **Função de Perda** ($\mathcal{L}$).
   - Regressão: $\text{MSE} = \frac{1}{n} \sum (y - \hat{y})^2$.
   - Classificação Binária: Entropia Cruzada Binária ($\text{Log-Loss}$).
   - Classificação Multiclasse: Entropia Cruzada Categórica ($-\sum y_i \log \hat{y}_i$).
2. **Retropropagação (*Backpropagation*):** Algoritmo que calcula analiticamente o vetor de derivadas parciais da perda em relação a cada peso de cada camada ($\frac{\partial \mathcal{L}}{\partial w}$), partindo da camada final em direção à camada inicial através da aplicação estrita da **Regra da Cadeia (*Chain Rule*)** do cálculo multivariável.
3. **Otimizadores de Atualização de Pesos:**
   - *Gradiente Descendente Estocástico (SGD):* Atualiza pesos por amostra ou minilote (*mini-batch*): $w \leftarrow w - \eta \nabla \mathcal{L}$.
   - *Momentum:* Adiciona uma fração inercial da velocidade anterior, amortecendo oscilações e acelerando o escape de platôs e mínimos locais rasos.
   - *RMSprop:* Ajusta a taxa de aprendizado dinamicamente com base na raiz da média móvel quadrática dos gradientes recentes.
   - *Adam (*Adaptive Moment Estimation*):* Combina os benefícios do **Momentum** (primeiro momento dos gradientes) e do **RMSprop** (segundo momento não-centrado dos gradientes). É o otimizador padrão mais utilizado no estado da arte.
4. **Técnicas de Regularização em Deep Learning:**
   - *Dropout:* Desativa aleatoriamente uma porcentagem fixada de neurônios (ex.: 20% a 50%) a cada iteração do treinamento, impedindo a coadaptação espúria entre nós vizinhos.
   - *Batch Normalization:* Normaliza as ativações de cada minilote para média zero e variância unitária, estabilizando e acelerando a convergência.
   - *Early Stopping:* Interrompe o treinamento quando o erro no conjunto de validação começa a subir consecutivamente, evitando o *overfitting*.

### 4.4 Arquiteturas Profundas: CNNs, RNNs/LSTM e Transformers

* **Redes Neurais Convolucionais (CNNs):**
  - Projetadas especificamente para processar dados estruturados em grades bidimensionais ou tridimensionais (visão computacional, imagens de satélite para fiscalização de obras pelo TCE-GO).
  - *Convoluções e Kernels:* Filtros matemáticos deslizantes que operam com **compartilhamento de pesos (*weight sharing*)**, capturando características invariantes à translação espacial e reduzindo drasticamente o número total de parâmetros livres.
  - *Pooling:* Camadas de subamostragem (*Max Pooling* e *Average Pooling*) que reduzem a resolução espacial dos mapas de características, conferindo tolerância a pequenas rotações e deformações geométricas.
* **Redes Neurais Recorrentes (RNNs) e Células LSTM / GRU:**
  - Concebidas para dados sequenciais e temporais (textos e séries temporais). Possuem conexões de realimentação que mantêm um estado oculto de memória.
  - Como as RNNs simples sofrem de desvanecimento de gradientes em dependências longas, utilizam-se células **LSTM (*Long Short-Term Memory*)**, que utilizam portas lógicas governadas por ativações sigmoides:
    - *Forget Gate:* Seleciona o que descartar da memória antiga.
    - *Input Gate:* Seleciona quais informações inéditas gravar na célula de estado.
    - *Output Gate:* Decide qual porção do estado da célula comporá a saída visível.
* **Arquitetura Transformer (Vaswani et al., 2017):**
  - Revolucionou o processamento de linguagem natural ao abandonar totalmente a recorrência sequencial em favor de mecanismos de **Autoatenção (*Self-Attention*) e Atenção Multi-Cabeça (*Multi-Head Attention*)**.
  - Permite o processamento massivamente paralelo de sequências textuais inteiras e modela dependências contextuais de longuíssimo alcance sem sofrer degradação informacional.

---

## 5. Questões Comentadas (FCC)

### Questão 01
**(FCC - SEFAZ-PE - Auditoria de Tecnologia da Informação)**
Uma equipe de auditores de dados está implementando modelos de aprendizado de máquina para classificar notas fiscais e declarações fiscais de contribuintes estaduais em duas classes: "Conforme" ou "Potencialmente Fraudulenta". Durante o desenvolvimento, debateu-se a utilização de algoritmos baseados em Comitês de Modelos (*Ensemble Learning*), especificamente comparando o *Random Forest* (baseado em *Bagging*) com o *XGBoost* e *LightGBM* (baseados em *Boosting*).
Sobre os fundamentos teóricos desses métodos de ensemble, é correto afirmar:
A) O *Random Forest* treina seus estimadores base de maneira estritamente sequencial, focando cada árvore sucessiva na redução do viés do modelo anterior.
B) O método de *Bagging* treina múltiplos estimadores em paralelo a partir de amostras geradas com reposição (*bootstrap*), tendo como foco matemático primordial a redução da variância do ensemble final sem aumentar substancialmente o seu viés.
C) Os algoritmos de *Boosting* constroem árvores de decisão profundas e complexas de maneira totalmente independente, utilizando a votação por maioria simples para reduzir a variância.
D) No *Random Forest*, o processo de amostragem aleatória restringe-se exclusivamente às linhas do dataset, sendo vedada a seleção aleatória de subconjuntos de atributos (*features*) na divisão dos nós.
E) O *AdaBoost* mantém pesos uniformes e imutáveis para todas as instâncias de treino ao longo de todas as iterações, independentemente de os estimadores anteriores terem classificado o registro corretamente ou não.

> **Comentário Detalhado:**
> - **A)** Incorreta. Quem treina árvores em sequência focando na redução de viés é o **Boosting** (como o AdaBoost ou Gradient Boosting). O *Random Forest* utiliza **Bagging** com treinamento paralelo e independente.
> - **B)** **Correta.** O **Bagging (*Bootstrap Aggregating*)** gera réplicas de conjuntos de dados via amostragem com reposição (*bootstrap*), ajustando estimadores base em **paralelo**. A agregação das predições de múltiplos modelos descorrelacionados reduz drasticamente a **variância** global do comitê, combatendo o sobreajuste (*overfitting*).
> - **C)** Incorreta. O *Boosting* opera em **série sequencial** e utiliza estimadores fracos intencionalmente simples (*weak learners / stumps*), atuando precipuamente na redução do **viés**.
> - **D)** Incorreta. O diferencial determinante do *Random Forest* é a amostragem aleatória de atributos (*feature subsampling*): ao avaliar cada divisão de nó, sorteia-se um subconjunto aleatório de features (tipicamente $\sqrt{p}$), descorrelacionando as árvores.
> - **E)** Incorreta. O núcleo do *AdaBoost* reside no reponderamento adaptativo: instâncias classificadas com erro na iteração atual recebem **pesos significativamente maiores** no ciclo seguinte.
> 
> **Gabarito: B**

---

### Questão 02
**(FCC - TCE-RS - Auditor Público Externo - Tecnologia da Informação)**
Em uma auditoria de contratos de obras públicas, um auditor necessita aplicar técnicas de Aprendizado Não Supervisionado (*Clustering*) para segmentar os pagamentos emitidos e detectar desvios operacionais atípicos. O conjunto de dados apresenta geometrias arbitrárias com densidades heterogêneas e a auditoria não possui uma estimativa prévia de quantos grupos naturais existem na base.
Nesse contexto, o algoritmo mais apropriado para a tarefa e sua fundamentação técnica é o:
A) K-Means, pois particiona os dados descobrindo clusters de qualquer geometria arbitrária não-esférica sem exigir o valor de $k$ a priori.
B) PCA, pois é um algoritmo de particionamento estocástico que divide a base em grupos convexos através dos autovetores da matriz de confusão.
C) DBSCAN, pois identifica agrupamentos baseando-se na densidade local de pontos delimitada por raio e vizinhos mínimos, não exige o fornecimento prévio da quantidade de clusters e classifica dados em regiões rarefeitas explicitamente como ruído (*outliers*).
D) Regressão Logística, pois dispensa rótulos de classe para traçar a fronteira linear que separa automaticamente anomalias de observações regulares.
E) Agrupamento Hierárquico Divisivo com ligação simples (*Single Linkage*), pois exige a parametrização de centroides esféricos pré-fixados para evitar o efeito de encadeamento (*chaining*).

> **Comentário Detalhado:**
> - **A)** Incorreta. O *K-Means* exige a parametrização prévia e obrigatória do número de clusters ($k$) e assume que os grupos são esféricos e de variâncias semelhantes, falhando em formatos arbitrários.
> - **B)** Incorreta. O PCA é uma técnica de **redução de dimensionalidade linear**, e não um algoritmo de agrupamento.
> - **C)** **Correta.** O **DBSCAN (*Density-Based Spatial Clustering of Applications with Noise*)** é sob medida para o problema: utiliza os parâmetros $\varepsilon$ e *min_samples*; **dispensa a definição prévia de $k$**; detecta formas geométricas não convexas e complexas; e isola dados em áreas de baixa densidade classificando-os formalmente como **ruído (*noise/outliers*)**, perfeito para auditoria e detecção de anomalias.
> - **D)** Incorreta. A Regressão Logística é um modelo de aprendizado **supervisionado** que exige rótulos históricos de classe para treino.
> - **E)** Incorreta. O método de ligação simples no agrupamento hierárquico é notório justamente por sofrer severamente do efeito de encadeamento (*chaining*), não resolvendo anomalias por centroides esféricos.
> 
> **Gabarito: C**

---

### Questão 03
**(FCC - TRT-15ª Região - Analista Judiciário - Tecnologia da Informação)**
Em arquiteturas de Redes Neurais Artificiais profundas (*Deep Learning*), as funções de ativação não lineares são elementos indispensáveis para viabilizar o aprendizado de fronteiras complexas. A respeito do comportamento dessas funções de ativação e de suas características computacionais, assinale a alternativa correta:
A) A função de ativação ReLU (*Rectified Linear Unit*), definida por $f(z) = \max(0, z)$, resolve o desvanecimento do gradiente para valores positivos ($z > 0$), porém pode apresentar a patologia do "neurônio morto" (*Dying ReLU*) quando as entradas $z$ são negativas, caso em que o neurônio emite saída e gradiente nulos.
B) A função Sigmoide é a escolha recomendada para todas as camadas ocultas intermediárias de redes profundas com centenas de camadas, pois suas derivadas nunca se aproximam de zero.
C) A função de ativação *Softmax* pode ser aplicada indistintamente em qualquer camada oculta intermediária de redes convolucionais para acelerar o cálculo de tensores.
D) A função Tangente Hiperbólica ($\tanh$) gera valores de saída estritamente limitados ao intervalo de $0$ a $+1$, comportando-se de forma equivalente à função logística sigmoide.
E) A retropropagação (*Backpropagation*) dispensa a regra da cadeia e utiliza apenas a média aritmética simples dos erros da camada final para atualizar os pesos de todas as camadas.

> **Comentário Detalhado:**
> - **A)** **Correta.** A função **ReLU** ($f(z) = \max(0, z)$) possui derivada constante igual a $1$ para $z > 0$, prevenindo o desvanecimento de gradiente na região positiva. No entanto, para entradas menores ou iguais a zero ($z \le 0$), sua saída e derivada tornam-se zero. Se um neurônio for levado por gradientes desfavoráveis a um estado de ativação negativo para quase todo o dataset, ele não mais atualizará seus pesos, tornando-se inerte (*Dying ReLU*).
> - **B)** Incorreta. A Sigmoide satura nas caudas ($|z| \gg 0$) gerando derivadas próximas a zero. Ao encadear dezenas de camadas, o produto sucessivo dessas derivadas zera o gradiente (**vanishing gradient**), inviabilizando o treino das camadas iniciais.
> - **C)** Incorreta. A função **Softmax** converte saídas em probabilidades categóricas cuja soma resulta em $1$, pertencendo estrita e quase exclusivamente à **camada de saída** de problemas de classificação multiclasse.
> - **D)** Incorreta. A Tangente Hiperbólica mapeia as entradas para o intervalo **$(-1, +1)$**, sendo centrada em zero, diferentemente da Sigmoide que mapeia para $(0, 1)$.
> - **E)** Incorreta. O algoritmo de *Backpropagation* fundamenta-se compulsoriamente na **Regra da Cadeia** do cálculo diferencial multivariável.
> 
> **Gabarito: A**

---

### Questão 04
**(FCC - SEFAZ-PE - Auditor Fiscal do Tesouro Estadual)**
Um cientista de dados está desenvolvendo um modelo preditivo de regressão para projetar a arrecadação tributária estadual a partir de duzentas variáveis macroeconômicas. Sabendo que muitas dessas variáveis apresentam alta correlação entre si e que diversas delas não contribuem relevantemente para o poder explicativo do modelo, o analista deseja aplicar uma técnica de regularização que execute **seleção automática de atributos**, forçando expressamente a zero os coeficientes das variáveis irrelevantes para gerar um modelo final esparso e parcimonioso.
A técnica de modelagem que atende estritamente ao requisito de zerar coeficientes e sua correspondente penalização matemática é:
A) Regressão Ridge, que utiliza uma penalidade baseada na norma $L_2$ (soma dos quadrados dos coeficientes).
B) Mínimos Quadrados Ordinários (OLS), que utiliza restrições de posto pleno para anular colinearidades.
C) Regressão Lasso (*Least Absolute Shrinkage and Selection Operator*), que utiliza uma penalidade baseada na norma $L_1$ (soma dos valores absolutos dos coeficientes).
D) Regressão Logística com regularização nula, que elimina preditores irrelevantes pelo determinante da matriz Hessiana.
E) Análise Discriminante Linear, que zera coeficientes descartando autovalores inferiores à unidade.

> **Comentário Detalhado:**
> - **A)** Incorreta. A Regressão **Ridge** utiliza a norma $L_2$ ($\sum w_j^2$). A geometria esférica suave encolhe os coeficientes em direção a zero, mas **nunca zera nenhum estritamente**, não realizando seleção de atributos.
> - **B)** Incorreta. O método OLS clássico não possui termo de regularização, sofrendo com alta variância e coeficientes instáveis sob multicolinearidade.
> - **C)** **Correta.** A Regressão **Lasso** adiciona a penalidade com base na norma $L_1$ ($\lambda \sum |w_j|$). Devido aos vértices pontiagudos nos eixos cartesianos da restrição em losango da norma $L_1$, a solução atinge pontos onde os coeficientes tornam-se **rigorosamente iguais a zero**, realizando simultaneamente contração e **seleção automática de variáveis**.
> - **D)** Incorreta. Modelos sem regularização não eliminam nem zeram coeficientes.
> - **E)** Incorreta. A Análise Discriminante Linear é um método de classificação/redução dimensional, não um estimador de regressão com penalidade esparsa.
> 
> **Gabarito: C**

---

### Questão 05
**(FCC - TRF-3ª Região - Analista Judiciário - Informática)**
No ecossistema de arquiteturas especializadas de Aprendizado Profundo (*Deep Learning*), diversas redes foram desenvolvidas para processar eficientemente imagens, fluxos de áudio e dados textuais sequenciais.
Sobre as características estruturais dessas arquiteturas, assinale a alternativa correta:
A) As Redes Neurais Convolucionais (CNNs) utilizam filtros deslizantes com compartilhamento de pesos nas camadas convolucionais, proporcionando invariância à translação espacial e reduzindo substancialmente a quantidade de parâmetros em comparação com redes totalmente conectadas.
B) As camadas de *Max Pooling* em uma rede convolucional aumentam a resolução espacial das matrizes de características para expandir o número de parâmetros ajustáveis na retropropagação.
C) As Redes Neurais Recorrentes (RNNs) simples conseguem manter dependências contextuais de longuíssimo prazo sem sofrer atenuação de gradientes, tornando as células LSTM obsoletas.
D) A arquitetura *Transformer* baseia-se exclusivamente em convoluções bidimensionais causais e descarta inteiramente mecanismos de atenção entre tokens.
E) As células LSTM (*Long Short-Term Memory*) descartam qualquer tipo de porta reguladora, substituindo todo o fluxo interno por uma única camada Perceptron sem função de ativação.

> **Comentário Detalhado:**
> - **A)** **Correta.** As **CNNs** empregam filtros convolucionais deslizantes (*kernels*) que compartilham pesos ao longo de todo o mapa espacial. Isso confere a propriedade fundamental de **invariância à translação espacial** (um padrão como uma assinatura ou trinca em asfalto é reconhecido independentemente de sua posição na imagem) e derruba drasticamente a quantidade de parâmetros livres frente a redes densas (MLP).
> - **B)** Incorreta. O propósito das camadas de pooling (*Max Pooling* ou *Average Pooling*) é realizar o **downsampling (subamostragem)**, ou seja, **reduzir** a resolução espacial das matrizes para diminuir o custo de processamento e conferir robustez a pequenas deformações.
> - **C)** Incorreta. As RNNs simples sofrem severamente do problema de **desvanecimento do gradiente** (*vanishing gradient*) em sequências longas. Por esse motivo, as células **LSTM** e **GRU** foram desenvolvidas com portas seletivas para reter dependências contextuais distantes.
> - **D)** Incorreta. O *Transformer* (Vaswani et al., 2017) fundamenta-se precipuamente no mecanismo de **Autoatenção (*Self-Attention*)**, dispensando tanto convoluções quanto recorrências sequenciais.
> - **E)** Incorreta. A LSTM baseia-se exatamente em **portas reguladoras não lineares** (*forget gate*, *input gate* e *output gate*), que governam matematicamente a retenção e descarte de dados no fluxo de memória.
> 
> **Gabarito: A**
