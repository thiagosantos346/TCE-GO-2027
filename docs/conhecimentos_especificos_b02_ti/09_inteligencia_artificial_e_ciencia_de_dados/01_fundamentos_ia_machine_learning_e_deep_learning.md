# 01 - Fundamentos de IA, Machine Learning e Deep Learning
**Última Atualização:** 2026-03-31  
**Banca Foco:** FCC (Fundação Carlos Chagas)  
**Cargo:** Auditor de Controle Externo - Tecnologia da Informação  
**Status do Mapeamento:** 100% aderente ao edital TCE-GO

---

## 📌 Ementa / Itens do Edital
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

## 🧭 Sumário

1. [Fundamentos e Paradigmas da Inteligência Artificial](#1-fundamentos-e-paradigmas-da-inteligencia-artificial)
    1. [Dimensões de Russell & Norvig e o Conceito de Agente Racional](#11-dimensoes-de-russell-norvig-e-o-conceito-de-agente-racional)
    2. [Níveis de IA: Narrow AI vs. AGI vs. Superinteligência](#12-niveis-de-ia-narrow-ai-vs-agi-vs-superinteligencia)
    3. [Paradigma Simbólico vs. Paradigma Conexionista](#13-paradigma-simbolico-vs-paradigma-conexionista)
    4. [Teste 300](#Teste-300)
    5. [Teste 301](#Teste-301)
2. [Aprendizado de Máquina Supervisionado](#2-aprendizado-de-maquina-supervisionado)
    1. [Modelos e Algoritmos de Classificação](#21-modelos-e-algoritmos-de-classificacao)
    2. [Comitês de Modelos (Ensemble): Bagging vs. Boosting](#22-comites-de-modelos-ensemble-bagging-vs-boosting)
    3. [Modelos de Regressão e Técnicas de Regularização (Ridge, Lasso e Elastic Net)](#23-modelos-de-regressao-e-tecnicas-de-regularizacao-ridge-lasso-e-elastic-net)
    4. [Teste 302](#Teste-302)
    5. [Teste 303](#Teste-303)
    6. [Teste 304](#Teste-304)
3. [Aprendizado Não Supervisionado e por Reforço](#3-aprendizado-nao-supervisionado-e-por-reforco)
    1. [Algoritmos de Agrupamento (Clustering: K-Means, DBSCAN e Hierárquico)](#31-algoritmos-de-agrupamento-clustering-k-means-dbscan-e-hierarquico)
    2. [Redução de Dimensionalidade (PCA, t-SNE e UMAP)](#32-reducao-de-dimensionalidade-pca-t-sne-e-umap)
    3. [Aprendizado por Reforço (Reinforcement Learning)](#33-aprendizado-por-reforco-reinforcement-learning)
    4. [Teste 305](#Teste-305)
    5. [Teste 306](#Teste-306)
    6. [Teste 307](#Teste-307)
4. [Redes Neurais Artificiais e Deep Learning](#4-redes-neurais-artificiais-e-deep-learning)
    1. [Perceptron, Limitações Lineares e Redes Multicamadas (MLP)](#41-perceptron-limitacoes-lineares-e-redes-multicamadas-mlp)
    2. [Funções de Ativação Não Lineares e suas Patologias](#42-funcoes-de-ativacao-nao-lineares-e-suas-patologias)
    3. [Treinamento: Backpropagation, Gradiente Descendente e Otimizadores](#43-treinamento-backpropagation-gradiente-descendente-e-otimizadores)
    4. [Arquiteturas Profundas: CNNs, RNNs/LSTM e Transformers](#44-arquiteturas-profundas-cnns-rnnslstm-e-transformers)
    5. [Teste 308](#Teste-308)
    6. [Teste 309](#Teste-309)
    7. [Teste 310](#Teste-310)
5. [🌐 Fontes Oficiais e Referências Bibliográficas](#fontes-oficiais-e-referencias-bibliograficas)

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
 Dataset ──► [Modelo Fraco 1] ──(Resíduos/Erros)──► [Modelo Fraco 2] ──(Resíduos)──► ..
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
>
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

### Teste 001
**(FGV – TCE/GO – 2024 – Analista de Controle Externo - Engenharia)**
Um engenheiro elabora um laudo para avaliação de um imóvel urbano utilizando um modelo de regressão linear e, para tanto, dispõe de 20 dados de mercado que serão efetivamente utilizados no estudo. Sabendo que o engenheiro deseja que a aplicação do modelo atinja grau III de fundamentação no laudo, o número máximo de variáveis independentes que deverá ser utilizado nesse modelo de regressão linear é

* **A)** 1
* **B)** 2
* **C)** 3
* **D)** 4
* **E)** 5

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "1". De acordo com a teoria estudada em *2.2 Comitês de Modelos (Ensemble): Bagging vs. Boosting*, agregação Final: Média aritmética simples (em regressão) ou voto da maioria (em classificação). — Combinação linear ponderada pela performance de cada modelo fraco no histórico.
> - **B)** **Correta.** Conforme fundamentado na seção *2.3 Modelos de Regressão e Técnicas de Regularização (Ridge, Lasso e Elastic Net)* deste guia, une a capacidade de gerar modelos esparsos do Lasso com a capacidade do Ridge de manter grupos inteiros de variáveis correlacionadas dentro do modelo. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/GO/2024) ao estabelecer que "2".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "3". De acordo com a teoria estudada em *4.2 Funções de Ativação Não Lineares e suas Patologias*, reLU ( Rectified Linear Unit ): $f(z) = \max(0, z)$ — $[0, +\infty)$ — Padrão da indústria para camadas ocultas. Não satura para valores positivos ($z 0$, onde a derivada é $1$), permitindo treinar redes profundas rapidamente sem vanishing gradient. — Problema do Neurônio Morto ( Dying ReLU ): se uma entrada $z \le 0$, tanto a saída quanto a derivada tornam se zero. Um neurônio empurrado para essa região inerte pode nunca mais atualizar seus pesos.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "4". De acordo com a teoria estudada em *2.1 Modelos e Algoritmos de Classificação*, entropia e Ganho de Informação (Algoritmos ID3 e C4.5): A Entropia mede o grau de desordem ou incerteza dos dados.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "5". De acordo com a teoria estudada em *3.2 Redução de Dimensionalidade (PCA, t-SNE e UMAP)*, técnica estatística linear e não supervisionada que transforma as variáveis originais em um novo conjunto de variáveis não correlacionadas denominadas Componentes Principais (PCs).
>
> **Gabarito: B**

---

### Teste 002
**(FGV – TCE/GO – 2024 – Analista de Controle Externo - Tecnologia da Informação)**
Os modelos de aprendizado de máquina desempenham um papel fundamental na análise e interpretação de dados em uma variedade de domínios. Uma característica dos modelos de aprendizado de máquina supervisionados e não supervisionados é que modelos supervisionados

* **A)** exploram a detecção de outliers, enquanto modelos não supervisionados usam dados representados em formatos como XML ou JSON para treinamento..
* **B)** geralmente têm menos tendência ao overfitting do que modelos não supervisionados.
* **C)** requerem dados rotulados para treinamento, enquanto modelos não supervisionados podem funcionar com dados não rotulados.
* **D)** são mais adequados para tarefas de análise exploratória de dados, enquanto modelos não supervisionados são mais adequados para previsão de séries temporais.
* **E)** são usados apenas para classificação, enquanto modelos não supervisionados são usados apenas para agrupamento.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "exploram a detecção de outliers, enquanto modelos não supervisionados usam dados representados em formatos como...". De acordo com a teoria estudada em *3.1 Algoritmos de Agrupamento (Clustering: K-Means, DBSCAN e Hierárquico)*, limitações Clássicas: Assume que todos os clusters são convexos e esféricos com variâncias semelhantes. Falha completamente na identificação de formatos orgânicos alongados e atribui compulsoriamente todo ponto a algum cluster, sendo muito sensível a outliers.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "geralmente têm menos tendência ao overfitting do que modelos não supervisionados". De acordo com a teoria estudada em *2.2 Comitês de Modelos (Ensemble): Bagging vs. Boosting*, foco Matemático no Erro: Reduzir a Variância (combater a tendência ao overfitting de modelos complexos). — Reduzir o Viés (combater o underfitting transformando modelos simples em preditores fortes).
> - **C)** **Correta.** Conforme fundamentado na seção *2. Aprendizado de Máquina Supervisionado* deste guia, o Aprendizado Supervisionado opera sobre conjuntos de dados históricos previamente rotulados, formalizados pelo conjunto de treino $\{(x 1, y 1), (x 2, y 2), \dots, (x n, y n)\}$, onde $x i$ representa o vetor de características ( features ) e $y i$ representa o rótulo verdadeiro ( ground truth ). O objetivo do algoritmo é estimar uma função $f(x) \approx y$ com alta capacidade de generalização para amostras inéditas. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/GO/2024) ao estabelecer que "requerem dados rotulados para treinamento, enquanto modelos não supervisionados podem funcionar com dados não...".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "são mais adequados para tarefas de análise exploratória de dados, enquanto modelos não supervisionados são mais...". De acordo com a teoria estudada em *4.4 Arquiteturas Profundas: CNNs, RNNs/LSTM e Transformers*, concebidas para dados sequenciais e temporais (textos e séries temporais). Possuem conexões de realimentação que mantêm um estado oculto de memória.
> - **E)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "são usados apenas para classificação, enquanto modelos não supervisionados são usados apenas para agrupamento". De acordo com a teoria estudada em *3.1 Algoritmos de Agrupamento (Clustering: K-Means, DBSCAN e Hierárquico)*, o agrupamento descobre partições ou morfologias naturais em dados não rotulados.
>
> **Gabarito: C**

---

### Teste 003
**(CEBRASPE – STJ – 2024 – Analista Judiciário - Apoio Especializado - Suporte em Tecnologia da Informação)**
A regressão linear do aprendizado de máquina busca estabelecer uma relação entre as variáveis de entrada de

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Incorreta.** A proposição apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A regressão linear do aprendizado de máquina busca estabelecer uma relação entre as variáveis de entrada de". De acordo com a teoria em *4.2 Funções de Ativação Não Lineares e suas Patologias*, reLU ( Rectified Linear Unit ): $f(z) = \max(0, z)$ — $[0, +\infty)$ — Padrão da indústria para camadas ocultas. Não satura para valores positivos ($z 0$, onde a derivada é $1$), permitindo treinar redes profundas rapidamente sem vanishing gradient. — Problema do Neurônio Morto ( Dying ReLU ): se uma entrada $z \le 0$, tanto a saída quanto a derivada tornam se zero. Um neurônio empurrado para essa região inerte pode nunca mais atualizar seus pesos.
> - **E)** **Correta.** O item está **Errado** (gabarito oficial: **E**), pois contraria a disciplina teórica aplicável.
>
> **Gabarito: E**

---

### Teste 004
**(FGV – TRT 16ª – 2022 – Analista Judiciário (Área Administrativa - Tecnologia da Informação))**
Com relação aos conceitos de aprendizado de máquina, assinale V para a afirmativa verdadeira e F para a falsa. I. Os três principais paradigmas de aprendizado de máquina são os de aprendizado supervisionado, não supervisionado e por inteligência profunda. II. os algoritmos de classificação e clusterização estão correlacionados com paradigma de aprendizado supervisionado. III. os algoritmos de support vector machines e randon forest são paradigmas do aprendizado de inteligência profunda. As afirmativas são, respectivamente,

* **A)** V, V e V.
* **B)** V, V e F.
* **C)** V, F e V.
* **D)** F, V e V.
* **E)** F, F e F.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "V, V e V". De acordo com a teoria estudada em *2. Aprendizado de Máquina Supervisionado*, o Aprendizado Supervisionado opera sobre conjuntos de dados históricos previamente rotulados, formalizados pelo conjunto de treino $\{(x 1, y 1), (x 2, y 2), \dots, (x n, y n)\}$, onde $x i$ representa o vetor de características ( features ) e $y i$ representa o rótulo verdadeiro ( ground truth ). O objetivo do algoritmo é estimar uma função $f(x) \approx y$ com alta capacidade de generalização para amostras inéditas.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "V, V e F". De acordo com a teoria estudada em *1.2 Níveis de IA: Narrow AI vs. AGI vs. Superinteligência*, sistema hipotético dotado de plasticidade e capacidade cognitiva comparáveis ou equivalentes às de um ser humano adulto. Uma AGI deve ser capaz de aprender, raciocinar, transferir aprendizado entre domínios totalmente distintos e solucionar desafios inéditos sem a necessidade de reconfiguração algorítmica ou retreinamento supervisionado por humanos.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "V, F e V". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, rUSSELL, Stuart; NORVIG, Peter. Inteligência Artificial: Uma Abordagem Moderna. 4. ed. Rio de Janeiro: GEN LTC, 2022. (Cap. 18 e 19 Aprendizado a Partir de Exemplos e Redes Neurais).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "F, V e V". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, gÉRON, Aurélien. Mãos à Obra: Aprendizado de Máquina com Scikit Learn, Keras & TensorFlow. 3. ed. Rio de Janeiro: Alta Books, 2023. (Cap. 4 a 6 Modelos Lineares, SVMs e Árvores de Decisão).
> - **E)** **Correta.** Conforme fundamentado na seção *1. Fundamentos e Paradigmas da Inteligência Artificial* deste guia, a Inteligência Artificial (IA) estuda e projeta entidades computacionais capazes de realizar tarefas cognitivas historicamente associadas à inteligência biológica humana, tais como percepção visual, tomada de decisão sob incerteza, raciocínio lógico dedutivo e aprendizado contínuo. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT 16ª/2022) ao estabelecer que "F, F e F".
>
> **Gabarito: E**

---

### Teste 005
**(FGV – TJ/MT – 2024 – Analista Judiciario Tecnologia Da Informacao)**
A divisão dos dados por ocasião das tarefas de aprendizado de máquina deve ser feita com todo critério técnico para evitar problemas nos modelos gerados. No contexto dessa divisão dos dados, assinale a afirmativa correta acerca do processo de overfitting em aprendizado de máquina.

* **A)** O modelo generaliza bem para dados novos, apresentando baixa taxa de erro tanto em dados de treino quanto em dados de teste.
* **B)** O modelo se ajusta excessivamente aos dados de treino, mas apresenta baixo desempenho em dados de teste.
* **C)** O modelo apresenta alto desempenho em dados de teste, mas baixo desempenho em dados de treino.
* **D)** O modelo é incapaz de aprender padrões dos dados de treino, resultando em alto erro de treino e de teste.
* **E)** O modelo é robusto e apresenta desempenho constante independentemente do conjunto de dados analisado.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O modelo generaliza bem para dados novos, apresentando baixa taxa de erro tanto em dados de treino quanto em dados...". De acordo com a teoria estudada em *4.3 Treinamento: Backpropagation, Gradiente Descendente e Otimizadores*, rMSprop: Ajusta a taxa de aprendizado dinamicamente com base na raiz da média móvel quadrática dos gradientes recentes.
> - **B)** **Correta.** Conforme fundamentado na seção *2. Aprendizado de Máquina Supervisionado* deste guia, o Aprendizado Supervisionado opera sobre conjuntos de dados históricos previamente rotulados, formalizados pelo conjunto de treino $\{(x 1, y 1), (x 2, y 2), \dots, (x n, y n)\}$, onde $x i$ representa o vetor de características ( features ) e $y i$ representa o rótulo verdadeiro ( ground truth ). O objetivo do algoritmo é estimar uma função $f(x) \approx y$ com alta capacidade de generalização para amostras inéditas. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/MT/2024) ao estabelecer que "O modelo se ajusta excessivamente aos dados de treino, mas apresenta baixo desempenho em dados de teste".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O modelo apresenta alto desempenho em dados de teste, mas baixo desempenho em dados de treino". De acordo com a teoria estudada em *2.1 Modelos e Algoritmos de Classificação*, algoritmo não paramétrico baseado em instâncias ( instance based ) e classificado como aprendizado preguiçoso ( lazy learning ), pois não possui uma fase de treinamento explícita que gere coeficientes ou modelos matemáticos: ele simplesmente memoriza todos os dados de treino na memória.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O modelo é incapaz de aprender padrões dos dados de treino, resultando em alto erro de treino e de teste". De acordo com a teoria estudada em *2.1 Modelos e Algoritmos de Classificação*, apesar dessa premissa ser quase sempre violada no mundo real, apresenta eficácia e velocidade ímpares na filtragem de spam, análise de sentimento e classificação de textos jurídicos.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O modelo é robusto e apresenta desempenho constante independentemente do conjunto de dados analisado". De acordo com a teoria estudada em *1.1 Dimensões de Russell & Norvig e o Conceito de Agente Racional*, agir como Humanos: Medido operacionalmente pelo célebre Teste de Turing (1950). Se um avaliador humano interagindo via terminal de texto não for capaz de distinguir confiavelmente se as respostas procedem de um operador humano ou de um computador, o sistema é considerado aprovado no teste comportamental. O filósofo John Searle contra argumentou com o experimento mental do Quarto Chinês ( Chinese Room ), afirmando que a mera manipulação sintática de regras e símbolos não confere compreensão semântica ou consciência real à máquina.
>
> **Gabarito: B**

---

### Teste 006
**(FGV – TRT/13 – 2022 – Analista Judiciario Tecnologia Da Informacao)**
A classe da biblioteca scikit-learn, versão 1.1.2, utilizada em scripts python para a implementação de regressão linear baseada no método dos mínimos quadrados é

* **A)** scikit-learn.LinearRegression.
* **B)** sklearn.linear.ml.LinearRegression.
* **C)** sklearn.linear_model.LinearRegression.
* **D)** sklearn.model.ml.Linear_Regression.LstSquare.
* **E)** scikit-learn.linear_model.LinearRegression.LeastSquare.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "scikit learn.LinearRegression". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, scikit Learn Official User Guide Supervised Learning Classificação e regressão: Regressão Linear, Árvores de Decisão, SVM, Naive Bayes e Ensembles.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "sklearn.linear.ml.LinearRegression". De acordo com a teoria estudada em *2.1 Modelos e Algoritmos de Classificação*, apesar do termo "regressão", é um algoritmo de classificação linear. Estima a probabilidade a posteriori de uma classe binária através da função logística sigmoide.
> - **C)** **Correta.** Conforme fundamentado na seção *2.3 Modelos de Regressão e Técnicas de Regularização (Ridge, Lasso e Elastic Net)* deste guia, o método clássico dos Mínimos Quadrados Ordinários (OLS Ordinary Least Squares ) minimiza o Erro Quadrático Médio ($\text{MSE}$). Em bases com dezenas ou centenas de variáveis multicolineares, o OLS produz coeficientes com variância gigante e sobreajuste. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT/13/2022) ao estabelecer que "sklearn.linear model.LinearRegression".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "sklearn.model.ml.Linear Regression.LstSquare". De acordo com a teoria estudada em *3.3 Aprendizado por Reforço (Reinforcement Learning)*, q Learning: Algoritmo clássico de aprendizado por diferença temporal, classificado como model free e off policy , que atualiza recursivamente os valores $Q(s, a)$ da função de valor ação estado.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "scikit learn.linear model.LinearRegression.LeastSquare". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, scikit Learn Official User Guide Unsupervised Learning Algoritmos de agrupamento (K Means, DBSCAN) e redução de dimensionalidade (PCA).
>
> **Gabarito: C**

---

### Teste 007
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Administrativa - Ciência de Dados)**
Modelos de aprendizagem de máquina são, em geral, avaliados com métricas que indicam os quão poderosos e relevantes eles são. Entre exemplos de métricas de avaliação utilizadas para modelos de classificação binária, podemos citar: • Taxa de precisão (razão entre verdadeiros positivos e o total dos verdadeiros positivos e falsos positivos); • Taxa de sensibilidade (razão entre verdadeiros positivos e o total dos verdadeiros positivos e falsos negativos, também conhecida por recall); e • Escore F1 (F1-score, também chamado de F-measure), que relaciona as taxas de precisão e de sensibilidade. Suponha a existência de um modelo de classificação binária cuja taxa de precisão é de 90,00% e cuja taxa de sensibilidade é de 75,00%. Utilize aproximação de duas casas decimais. O escore F1 referente a esse modelo é

* **A)** 41,42%.
* **B)** 81,82%.
* **C)** 82,15%.
* **D)** 82,50%.
* **E)** 82,84%.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "41,42%". De acordo com a teoria estudada em *1.2 Níveis de IA: Narrow AI vs. AGI vs. Superinteligência*, exemplos: Classificação de transações fraudulentas pelo TCE GO, sistemas de reconhecimento facial, motores de recomendação de comércio eletrônico, grandes modelos de linguagem (LLMs) e motores de xadrez/Go. Toda a inteligência artificial desenvolvida e operacional no mundo atual pertence exclusivamente à categoria Narrow AI.
> - **B)** **Correta.** Conforme fundamentado na seção *4.1 Perceptron, Limitações Lineares e Redes Multicamadas (MLP)* deste guia, a introdução de uma ou mais camadas ocultas ( hidden layers ) com funções de ativação não lineares resolveu essa limitação histórica. Segundo o Teorema da Aproximação Universal (Cybenko, 1989 / Hornik, 1991), uma rede MLP feedforward com uma única camada oculta contendo uma quantidade finita de neurônios não lineares é capaz de aproximar qualquer função contínua arbitrária com precisão pré estabelecida. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "81,82%".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "82,15%". De acordo com a teoria estudada em *2.1 Modelos e Algoritmos de Classificação*, apesar do termo "regressão", é um algoritmo de classificação linear. Estima a probabilidade a posteriori de uma classe binária através da função logística sigmoide.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "82,50%". De acordo com a teoria estudada em *2.1 Modelos e Algoritmos de Classificação*, a fronteira de separação entre as classes é estritamente linear ($\mathbf{w}^T \mathbf{x} + b = 0$). O treinamento minimiza a função de perda de Entropia Cruzada Binária ( Log Loss ).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "82,84%". De acordo com a teoria estudada em *2.2 Comitês de Modelos (Ensemble): Bagging vs. Boosting*, agregação Final: Média aritmética simples (em regressão) ou voto da maioria (em classificação). — Combinação linear ponderada pela performance de cada modelo fraco no histórico.
>
> **Gabarito: B**

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

### Teste 008
**(CEBRASPE – TRF 6ª – 2025 – Analista Judiciário - Apoio Especializado - Governança e Gestão de Tecnologia da Informação)**
Em aprendizado supervisionado, o algoritmo random forest utiliza múltiplas árvores de decisão para melhorar a precisão das previsões e reduzir o risco de overfitting.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Correta.** O item está **Certo**. Conforme fundamentado na seção *2.2 Comitês de Modelos (Ensemble): Bagging vs. Boosting*, no Random Forest (Bagging), as árvores são geradas em paralelo. Além do bootstrap nas linhas, o algoritmo sorteia aleatoriamente um subconjunto de variáveis ( feature subsampling , comumente $\sqrt{p}$) na divisão de cada nó. Isso descorrelaciona as árvores e derruba a variância. Dessa forma, está plenamente correta a assertiva da banca (CEBRASPE – TRF 6ª/2025) ao afirmar que "Em aprendizado supervisionado, o algoritmo random forest utiliza múltiplas árvores de decisão para melhorar a...".
> - **E)** **Incorreta.** A assertiva não incorre em erro conceitual, guardando conformidade com a teoria estudada.
>
> **Gabarito: C**

---

### Teste 009
**(FGV – TJ/AP – 2023 – Analista Judiciario Apoio Especializado Tecnologia Da Informacao Banco De Dados)**
A Resolução CNJ nº 335, de 29 de setembro de 2020, que institui política pública para a governança e a gestão de processo judicial eletrônico, no seu Art. 4º, considera que a plataforma digital do Poder Judiciário Brasileiro (PDPJ-BR) adotará obrigatoriamente soluções que abranjam o(s) seguinte(s) conceito(s):

* **A)** utilização preferencial de tecnologias com código fechado;
* **B)** desenvolvimento que possibilite o compartilhamento em segmentos específicos e esferas do Poder Judiciário;
* **C)** ampla cobertura de testes, alto acoplamento, baixa coesão e modularização;
* **D)** processo eletrônico em plataforma privada;
* **E)** adaptável ao uso de ferramentas de aprendizado de máquina (machine learning) e de I.A. (Inteligência Artificial)

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "utilização preferencial de tecnologias com código fechado". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, rUSSELL, Stuart; NORVIG, Peter. Inteligência Artificial: Uma Abordagem Moderna. 4. ed. Rio de Janeiro: GEN LTC, 2022. (Cap. 18 e 19 Aprendizado a Partir de Exemplos e Redes Neurais).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "desenvolvimento que possibilite o compartilhamento em segmentos específicos e esferas do Poder Judiciário". De acordo com a teoria estudada em *1.2 Níveis de IA: Narrow AI vs. AGI vs. Superinteligência*, exemplos: Classificação de transações fraudulentas pelo TCE GO, sistemas de reconhecimento facial, motores de recomendação de comércio eletrônico, grandes modelos de linguagem (LLMs) e motores de xadrez/Go. Toda a inteligência artificial desenvolvida e operacional no mundo atual pertence exclusivamente à categoria Narrow AI.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "ampla cobertura de testes, alto acoplamento, baixa coesão e modularização". De acordo com a teoria estudada em *3.3 Aprendizado por Reforço (Reinforcement Learning)*, formalizado matematicamente por um Processo de Decisão de Markov (MDP), representado pela 5 tupla $(S, A, P, R, \gamma)$.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "processo eletrônico em plataforma privada". De acordo com a teoria estudada em *1.1 Dimensões de Russell & Norvig e o Conceito de Agente Racional*, fOCO NO PROCESSO │ PENSAR COMO HUMANOS │ PENSAR RACIONALMENTE │.
> - **E)** **Correta.** Conforme fundamentado na seção *1. Fundamentos e Paradigmas da Inteligência Artificial* deste guia, a Inteligência Artificial (IA) estuda e projeta entidades computacionais capazes de realizar tarefas cognitivas historicamente associadas à inteligência biológica humana, tais como percepção visual, tomada de decisão sob incerteza, raciocínio lógico dedutivo e aprendizado contínuo. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/AP/2023) ao estabelecer que "adaptável ao uso de ferramentas de aprendizado de máquina (machine learning) e de I.A. (Inteligência Artificial)".
>
> **Gabarito: E**

---

### Teste 010
**(FGV – TRT 16ª – 2022 – Analista Judiciário (Área Administrativa - Tecnologia da Informação))**
O Keras é uma API de aprendizado profundo escrita em Python e executada sobre a plataforma de aprendizado de máquina TensorFlow. As principais estruturas de dados do Keras são

* **A)** tensor e pipes.
* **B)** layers e model.
* **C)** neuron e arrays.
* **D)** sets, model e frames.
* **E)** sequential, layers e optimizers.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "tensor e pipes". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, gÉRON, Aurélien. Mãos à Obra: Aprendizado de Máquina com Scikit Learn, Keras & TensorFlow. 3. ed. Rio de Janeiro: Alta Books, 2023. (Cap. 4 a 6 Modelos Lineares, SVMs e Árvores de Decisão).
> - **B)** **Correta.** Conforme fundamentado na seção *3.3 Aprendizado por Reforço (Reinforcement Learning)* deste guia, q Learning: Algoritmo clássico de aprendizado por diferença temporal, classificado como model free e off policy , que atualiza recursivamente os valores $Q(s, a)$ da função de valor ação estado. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT 16ª/2022) ao estabelecer que "layers e model".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "neuron e arrays". De acordo com a teoria estudada em *4.1 Perceptron, Limitações Lineares e Redes Multicamadas (MLP)*, a introdução de uma ou mais camadas ocultas ( hidden layers ) com funções de ativação não lineares resolveu essa limitação histórica. Segundo o Teorema da Aproximação Universal (Cybenko, 1989 / Hornik, 1991), uma rede MLP feedforward com uma única camada oculta contendo uma quantidade finita de neurônios não lineares é capaz de aproximar qualquer função contínua arbitrária com precisão pré estabelecida.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "sets, model e frames". De acordo com a teoria estudada em *4. Redes Neurais Artificiais e Deep Learning*, o Aprendizado Profundo ( Deep Learning ) fundamenta se em arquiteturas com múltiplas camadas ocultas empilhadas capazes de extrair representações hierárquicas e abstratas de dados não estruturados de ponta a ponta ( end to end ).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "sequential, layers e optimizers". De acordo com a teoria estudada em *2. Aprendizado de Máquina Supervisionado*, o Aprendizado Supervisionado opera sobre conjuntos de dados históricos previamente rotulados, formalizados pelo conjunto de treino $\{(x 1, y 1), (x 2, y 2), \dots, (x n, y n)\}$, onde $x i$ representa o vetor de características ( features ) e $y i$ representa o rótulo verdadeiro ( ground truth ). O objetivo do algoritmo é estimar uma função $f(x) \approx y$ com alta capacidade de generalização para amostras inéditas.
>
> **Gabarito: B**

---

### Teste 011
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
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "suposição de estacionaridade". De acordo com a teoria estudada em *2.1 Modelos e Algoritmos de Classificação*, suposição "Ingênua" ( Naive ): Assume categoricamente que todos os atributos preditores $x 1, x 2, \dots, x d$ são mutuamente independentes entre si, dado o rótulo de classe $y$.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "poda de árvore de decisão". De acordo com a teoria estudada em *2.1 Modelos e Algoritmos de Classificação*, árvores de decisão profundas e sem limites de crescimento sofrem gravemente de sobreajuste ( overfitting ) (alta variância). Para mitigar essa patologia, aplicam se técnicas de poda prévia ( pre pruning , limitando a profundidade máxima max depth ou número mínimo de amostras por nó) e poda posterior ( post pruning via complexidade de custo).
> - **C)** **Correta.** Conforme fundamentado na seção *4.2 Funções de Ativação Não Lineares e suas Patologias* deste guia, reLU ( Rectified Linear Unit ): $f(z) = \max(0, z)$ — $[0, +\infty)$ — Padrão da indústria para camadas ocultas. Não satura para valores positivos ($z 0$, onde a derivada é $1$), permitindo treinar redes profundas rapidamente sem vanishing gradient. — Problema do Neurônio Morto ( Dying ReLU ): se uma entrada $z \le 0$, tanto a saída quanto a derivada tornam se zero. Um neurônio empurrado para essa região inerte pode nunca mais atualizar seus pesos. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT/DA/2025) ao estabelecer que "superadaptação".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "hipótese nula". De acordo com a teoria estudada em *3.2 Redução de Dimensionalidade (PCA, t-SNE e UMAP)*, o primeiro componente principal captura a direção de máxima variância dos dados; o segundo componente captura a segunda maior variância sob a restrição de ser rigorosamente ortogonal ao primeiro, e assim por diante.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "hiperárvore". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, gÉRON, Aurélien. Mãos à Obra: Aprendizado de Máquina com Scikit Learn, Keras & TensorFlow. 3. ed. Rio de Janeiro: Alta Books, 2023. (Cap. 4 a 6 Modelos Lineares, SVMs e Árvores de Decisão).
>
> **Gabarito: C**

---

### Teste 012
**(FGV – TJ/MT – 2024 – Analista Judiciario Tecnologia Da Informacao)**
O ciclo de vida de um processo de ciência de dados envolve uma série de etapas estruturadas que guiam o desenvolvimento de projetos de ciência de dados desde a definição do problema até a implementação e o monitoramento das soluções. No ciclo de vida de um processo de ciência de dados, na fase de preparação de dados

* **A)** são definidos os objetivos do projeto e formuladas as perguntas que o modelo deve responder.
* **B)** o modelo é treinado e avaliado usando algoritmos de aprendizado de máquina.
* **C)** são realizadas atividades como limpeza, transformação e formatação dos dados para garantir qualidade e adequação ao modelo.
* **D)** os resultados são comunicados aos stakeholders por meio de visualizações e relatórios.
* **E)** os dados são coletados diretamente dos usuários para garantir que o modelo esteja alinhado com as necessidades do público.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "são definidos os objetivos do projeto e formuladas as perguntas que o modelo deve responder". De acordo com a teoria estudada em *4.2 Funções de Ativação Não Lineares e suas Patologias*, as funções de ativação inserem a não linearidade necessária para que o empilhamento de camadas neurais não colapse matematicamente em uma única transformação afim linear.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "o modelo é treinado e avaliado usando algoritmos de aprendizado de máquina". De acordo com a teoria estudada em *2. Aprendizado de Máquina Supervisionado*, o Aprendizado Supervisionado opera sobre conjuntos de dados históricos previamente rotulados, formalizados pelo conjunto de treino $\{(x 1, y 1), (x 2, y 2), \dots, (x n, y n)\}$, onde $x i$ representa o vetor de características ( features ) e $y i$ representa o rótulo verdadeiro ( ground truth ). O objetivo do algoritmo é estimar uma função $f(x) \approx y$ com alta capacidade de generalização para amostras inéditas.
> - **C)** **Correta.** Conforme fundamentado na seção *2.1 Modelos e Algoritmos de Classificação* deste guia, algoritmo não paramétrico baseado em instâncias ( instance based ) e classificado como aprendizado preguiçoso ( lazy learning ), pois não possui uma fase de treinamento explícita que gere coeficientes ou modelos matemáticos: ele simplesmente memoriza todos os dados de treino na memória. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/MT/2024) ao estabelecer que "são realizadas atividades como limpeza, transformação e formatação dos dados para garantir qualidade e adequação...".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "os resultados são comunicados aos stakeholders por meio de visualizações e relatórios". De acordo com a teoria estudada em *2.2 Comitês de Modelos (Ensemble): Bagging vs. Boosting*, tratamento dos Dados: Reamostragem com reposição ( Bootstrap ) aleatória uniforme. — Reamostragem ponderada: instâncias mal classificadas recebem maior peso no próximo ciclo.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "os dados são coletados diretamente dos usuários para garantir que o modelo esteja alinhado com as necessidades do...". De acordo com a teoria estudada em *2.1 Modelos e Algoritmos de Classificação*, classificador probabilístico alicerçado diretamente no Teorema de Bayes.
>
> **Gabarito: C**

---

### Teste 013
**(FGV – TJ/MT – 2024 – Analista Judiciario Tecnologia Da Informacao)**
A linguagem de programação Python é uma linguagem de alto nível, de tipagem dinâmica e interpretada, conhecida pela sua simplicidade, legibilidade e versatilidade. Criada por Guido van Rossum e lançada pela primeira vez em 1991, Python tem se tornado uma das linguagens mais populares do mundo, devido à sua capacidade de ser usada em diversos tipos de projetos, como desenvolvimento web, automação, análise de dados, inteligência artificial, aprendizado de máquina, automação de tarefas, entre outros. Em Python, o operador //

* **A)** realiza a divisão entre dois números e retorna o resultado com a maior precisão possível.
* **B)** realiza a divisão entre dois números e sempre retorna um número com ponto decimal, mesmo que o resultado seja inteiro.
* **C)** eleva o primeiro número ao segundo número, funcionando como um operador de potência.
* **D)** realiza a divisão inteira entre dois números, retornando apenas a parte inteira do resultado e descartando o resto.
* **E)** realiza a divisão entre dois números e retorna o resto da divisão, semelhante ao operador %.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "realiza a divisão entre dois números e retorna o resultado com a maior precisão possível". De acordo com a teoria estudada em *3.2 Redução de Dimensionalidade (PCA, t-SNE e UMAP)*, reduz a quantidade de preditores de um dataset volumoso preservando a maior quantidade possível de variância estatística ou vizinhança.
> - **B)** **Incorreta.** A opção promove generalização excessiva que desconsidera as condições técnicas e normativas ao afirmar que "realiza a divisão entre dois números e sempre retorna um número com ponto decimal, mesmo que o resultado seja...". De acordo com a teoria estudada em *2.1 Modelos e Algoritmos de Classificação*, apesar dessa premissa ser quase sempre violada no mundo real, apresenta eficácia e velocidade ímpares na filtragem de spam, análise de sentimento e classificação de textos jurídicos.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "eleva o primeiro número ao segundo número, funcionando como um operador de potência". De acordo com a teoria estudada em *1.1 Dimensões de Russell & Norvig e o Conceito de Agente Racional*, agir como Humanos: Medido operacionalmente pelo célebre Teste de Turing (1950). Se um avaliador humano interagindo via terminal de texto não for capaz de distinguir confiavelmente se as respostas procedem de um operador humano ou de um computador, o sistema é considerado aprovado no teste comportamental. O filósofo John Searle contra argumentou com o experimento mental do Quarto Chinês ( Chinese Room ), afirmando que a mera manipulação sintática de regras e símbolos não confere compreensão semântica ou consciência real à máquina.
> - **D)** **Correta.** Conforme fundamentado na seção *3.1 Algoritmos de Agrupamento (Clustering: K-Means, DBSCAN e Hierárquico)* deste guia, agrupa os dados com base na densidade espacial local, orientando se por dois parâmetros: raio de vizinhança ($\varepsilon$) e número mínimo de pontos ( min samples ). Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/MT/2024) ao estabelecer que "realiza a divisão inteira entre dois números, retornando apenas a parte inteira do resultado e descartando o resto".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "realiza a divisão entre dois números e retorna o resto da divisão, semelhante ao operador %". De acordo com a teoria estudada em *1.2 Níveis de IA: Narrow AI vs. AGI vs. Superinteligência*, exemplos: Classificação de transações fraudulentas pelo TCE GO, sistemas de reconhecimento facial, motores de recomendação de comércio eletrônico, grandes modelos de linguagem (LLMs) e motores de xadrez/Go. Toda a inteligência artificial desenvolvida e operacional no mundo atual pertence exclusivamente à categoria Narrow AI.
>
> **Gabarito: D**

---

### Teste 014
**(FGV – TJ/MT – 2024 – Analista Judiciario Tecnologia Da Informacao)**
A Blockchain é uma tecnologia conhecida por sua segurança e transparência. Uma de suas principais características é a descentralização, que elimina a necessidade de uma autoridade central para validar as transações. Um conceito diretamente relacionado a essa característica da Blockchain é o de

* **A)** Contratos Inteligentes.
* **B)** Mineração de Dados.
* **C)** Machine Learning.
* **D)** Tokens de Utilidade.
* **E)** Livro-razão distribuído.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Contratos Inteligentes". De acordo com a teoria estudada em *1.2 Níveis de IA: Narrow AI vs. AGI vs. Superinteligência*, exemplos: Classificação de transações fraudulentas pelo TCE GO, sistemas de reconhecimento facial, motores de recomendação de comércio eletrônico, grandes modelos de linguagem (LLMs) e motores de xadrez/Go. Toda a inteligência artificial desenvolvida e operacional no mundo atual pertence exclusivamente à categoria Narrow AI.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Mineração de Dados". De acordo com a teoria estudada em *2. Aprendizado de Máquina Supervisionado*, o Aprendizado Supervisionado opera sobre conjuntos de dados históricos previamente rotulados, formalizados pelo conjunto de treino $\{(x 1, y 1), (x 2, y 2), \dots, (x n, y n)\}$, onde $x i$ representa o vetor de características ( features ) e $y i$ representa o rótulo verdadeiro ( ground truth ). O objetivo do algoritmo é estimar uma função $f(x) \approx y$ com alta capacidade de generalização para amostras inéditas.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Machine Learning". De acordo com a teoria estudada em *2.1 Modelos e Algoritmos de Classificação*, algoritmo não paramétrico baseado em instâncias ( instance based ) e classificado como aprendizado preguiçoso ( lazy learning ), pois não possui uma fase de treinamento explícita que gere coeficientes ou modelos matemáticos: ele simplesmente memoriza todos os dados de treino na memória.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Tokens de Utilidade". De acordo com a teoria estudada em *1.1 Dimensões de Russell & Norvig e o Conceito de Agente Racional*, (AÇÃO VISÍVEL) │ Processamento de Linguagem) │ da Utilidade/Desempenho) │.
> - **E)** **Correta.** Conforme fundamentado na seção *1.3 Paradigma Simbólico vs. Paradigma Conexionista* deste guia, o conhecimento não reside em regras textuais explícitas, mas sim distribuído nos pesos numéricos aprendidos por otimização estatística direta sobre grandes massas de dados. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/MT/2024) ao estabelecer que "Livro razão distribuído".
>
> **Gabarito: E**

---

### Teste 015
**(FGV – TRT/13 – 2022 – Analista Judiciario Tecnologia Da Informacao)**
O sckit-learn suporta o processamento de algoritmos de aprendizado de máquina do tipo supervisionado como, por exemplo,

* **A)** o SVM e a clusterização.
* **B)** o BIRCH e o vizinho mais próximo.
* **C)** o PCA e os gaussian mixture models.
* **D)** o naive bayes e as árvores de decisão.
* **E)** o modelo cúbico e a densidade estimada.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "o SVM e a clusterização". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, gÉRON, Aurélien. Mãos à Obra: Aprendizado de Máquina com Scikit Learn, Keras & TensorFlow. 3. ed. Rio de Janeiro: Alta Books, 2023. (Cap. 4 a 6 Modelos Lineares, SVMs e Árvores de Decisão).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "o BIRCH e o vizinho mais próximo". De acordo com a teoria estudada em *2.1 Modelos e Algoritmos de Classificação*, árvores de Decisão ( Decision Trees ).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "o PCA e os gaussian mixture models". De acordo com a teoria estudada em *2.1 Modelos e Algoritmos de Classificação*, árvores de decisão profundas e sem limites de crescimento sofrem gravemente de sobreajuste ( overfitting ) (alta variância). Para mitigar essa patologia, aplicam se técnicas de poda prévia ( pre pruning , limitando a profundidade máxima max depth ou número mínimo de amostras por nó) e poda posterior ( post pruning via complexidade de custo).
> - **D)** **Correta.** Conforme fundamentado na seção *🌐 Fontes Oficiais e Referências Bibliográficas* deste guia, scikit Learn Official User Guide Supervised Learning Classificação e regressão: Regressão Linear, Árvores de Decisão, SVM, Naive Bayes e Ensembles. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT/13/2022) ao estabelecer que "o naive bayes e as árvores de decisão".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "o modelo cúbico e a densidade estimada". De acordo com a teoria estudada em *2.2 Comitês de Modelos (Ensemble): Bagging vs. Boosting*, estimadores de Base Típicos: Modelos complexos e profundos com baixo viés e alta variância (ex.: árvores de decisão não podadas). — Estimadores fracos e rasos intencionalmente simples (ex.: árvores de profundidade 1 a 3, chamadas decision stumps ).
>
> **Gabarito: D**

---

### Teste 016
**(FCC – TRT 24ª – 2017 – Analista Judiciário - Tecnologia da Informação)**
Consider these statements. I. OpenSSL is an open source Project that provides a robust, commercial-grade, and full-featured toolkit for the Transport Layer Security (TLS) and Secure Sockets Layer (SSL) protocols. It is also a general-purpose cryptography library. II. OpenLDAP stands for Open Light Directory Access Protocol. It is a lightweight protocol for accessing directory services, specifically X.500-based directory services. LDAP runs only over TCP/IP services. The LDAP information model is based on entries. An entry is a collection of commands that has a globally-unique Distinguished Name (DN). The DN is used to refer to the entry ambiguously. In LDAP, directory entries are arranged in a non hierarchical tree-like structure. III. The Active Directory module for Windows PowerShell consolidates a group of cmdlets. These cmdlets can be used to manage Active Directory domains, Active Directory Lightweight Directory Services (AD LDS) configuration sets, and Active Directory Database Mounting Tool instances in a single, self-contained package. The correct statement(s) is (are)

* **A)** possui um conjunto de comandos PowerCluster que permite criar imagens com atualizações e drivers específicos, eliminando a necessidade de um dispositivo de boot nos hosts.
* **B)** permite a criação de um datastore NFS utilizando os discos locais de até 3 hosts ESXi. Oferece uma tecnologia de repli- cação que, mesmo no caso de queda de um dos hosts, não há perda de dados e nem indisponibilidade de VMs.
* **C)** inclui, também, a alocação inicial de uma VM, evitando-se analisar todos os hosts ESXi manualmente antes de criar uma nova VM no VSA storage, com base no espaço utilizado e na latência de I/O.
* **D)** agrega os recursos de memória e CPU dos hosts em um cluster, o VSA Storage DRS, permitindo que os recursos de várias VMs concentrem-se em um Datastore vCluster, de acordo com as definições do administrador.
* **E)** simplifica a implantação de novos hosts no ambiente. Com o VSA é possível disponibilizar os novos hosts ESXi e ainda existe a opção de especificar um Host-Clustering para ser aplicado no host, automatizando sua configuração.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "possui um conjunto de comandos PowerCluster que permite criar imagens com atualizações e drivers específicos...". De acordo com a teoria estudada em *2.1 Modelos e Algoritmos de Classificação*, truque do Kernel ( Kernel Trick ): Permite resolver problemas não linearmente separáveis sem a necessidade de calcular explicitamente as coordenadas em um espaço de dimensão infinita ou muito alta, substituindo o produto escalar por uma função de kernel: Linear, Polinomial ou Gaussiano RBF ( Radial Basis Function ).
> - **B)** **Correta.** Conforme fundamentado na seção *4.3 Treinamento: Backpropagation, Gradiente Descendente e Otimizadores* deste guia, propagação Direta ( Forward Pass ): Os dados avançam pelas camadas da rede até produzir uma saída predita $\hat{y}$, que é comparada ao rótulo real $y$ através de uma Função de Perda ($\mathcal{L}$). Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 24ª/2017) ao estabelecer que "permite a criação de um datastore NFS utilizando os discos locais de até 3 hosts ESXi. Oferece uma tecnologia de...".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "inclui, também, a alocação inicial de uma VM, evitando se analisar todos os hosts ESXi manualmente antes de criar...". De acordo com a teoria estudada em *2.1 Modelos e Algoritmos de Classificação*, durante a inferência, calcula a distância (Euclidiana, Manhattan ou Minkowski) entre a nova amostra e todos os pontos históricos da base, atribuindo a classe majoritária entre os $k$ vizinhos mais próximos. Sofre severamente com a maldição da dimensionalidade ( curse of dimensionality ).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "agrega os recursos de memória e CPU dos hosts em um cluster, o VSA Storage DRS, permitindo que os recursos de...". De acordo com a teoria estudada em *2.1 Modelos e Algoritmos de Classificação*, algoritmo não paramétrico baseado em instâncias ( instance based ) e classificado como aprendizado preguiçoso ( lazy learning ), pois não possui uma fase de treinamento explícita que gere coeficientes ou modelos matemáticos: ele simplesmente memoriza todos os dados de treino na memória.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "simplifica a implantação de novos hosts no ambiente. Com o VSA é possível disponibilizar os novos hosts ESXi e...". De acordo com a teoria estudada em *3.2 Redução de Dimensionalidade (PCA, t-SNE e UMAP)*, o primeiro componente principal captura a direção de máxima variância dos dados; o segundo componente captura a segunda maior variância sob a restrição de ser rigorosamente ortogonal ao primeiro, e assim por diante.
>
> **Gabarito: B**

---

### Teste 017
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Administrativa - Ciência de Dados)**
Alguns algoritmos de aprendizado de máquina foram desenvolvidos para trabalhar com atributos discretos. Porém, dados coletados no mundo real muitas vezes são contínuos. Nesses casos, podemos usar métodos de discretização no tratamento dos dados. Um desses métodos de discretização consiste em estabelecer os limites das partições de forma que cada partição tenha aproximadamente o mesmo número de elementos. O método acima descrito é o

* **A)** equal frequency.
* **B)** equal width.
* **C)** equal amplitude.
* **D)** k-means.
* **E)** entropy.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *1.1 Dimensões de Russell & Norvig e o Conceito de Agente Racional* deste guia, pensar Racionalmente: Baseia se em sistemas de lógica formal dedutiva (silogismos e cálculo proposicional). Limitação prática: incapacidade de lidar eficientemente com incertezas, dados probabilísticos e o conhecimento informal difuso do mundo real. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "equal frequency".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "equal width". De acordo com a teoria estudada em *2.1 Modelos e Algoritmos de Classificação*, árvores de decisão profundas e sem limites de crescimento sofrem gravemente de sobreajuste ( overfitting ) (alta variância). Para mitigar essa patologia, aplicam se técnicas de poda prévia ( pre pruning , limitando a profundidade máxima max depth ou número mínimo de amostras por nó) e poda posterior ( post pruning via complexidade de custo).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "equal amplitude". De acordo com a teoria estudada em *3.1 Algoritmos de Agrupamento (Clustering: K-Means, DBSCAN e Hierárquico)*, o número ideal $k$ é avaliado visualmente pelo Método do Cotovelo ( Elbow Method ) ou pelo Coeficiente de Silhueta (que oscila entre $ 1$ e $+1$).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "k means". De acordo com a teoria estudada em *3.1 Algoritmos de Agrupamento (Clustering: K-Means, DBSCAN e Hierárquico)*, o agrupamento descobre partições ou morfologias naturais em dados não rotulados.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "entropy". De acordo com a teoria estudada em *2.1 Modelos e Algoritmos de Classificação*, apesar dessa premissa ser quase sempre violada no mundo real, apresenta eficácia e velocidade ímpares na filtragem de spam, análise de sentimento e classificação de textos jurídicos.
>
> **Gabarito: A**

---

### Teste 018
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Administrativa - Ciência de Dados)**
Ao se utilizar bancos de dados reais no treinamento de métodos de aprendizado de máquina é normal se deparar com entradas que possuem um ou mais parâmetros (campos) ausentes. Com relação às estratégias para lidar com dados ausentes, analise as afirmativas a seguir. I. Só é possível realizar imputation quando o atributo (feature) ausente é numérico. II. Ao utilizar o k-nearest neighbors (KNN) para fazer o imputation é uma boa estratégia primeiro fazer a normalização ou padronização dos dados. III. Ao se trabalhar com bancos de dados com poucas amostras (itens), uma estratégia usualmente utilizada para lidar com as amostras) que possuem valores ausentes é a remoção. Está correto o que se afirma em

* **A)** I, apenas.
* **B)** II, apenas.
* **C)** III, apenas.
* **D)** I e II apenas.
* **E)** I, II e III.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I, apenas". De acordo com a teoria estudada em *4.3 Treinamento: Backpropagation, Gradiente Descendente e Otimizadores*, adam ( Adaptive Moment Estimation ): Combina os benefícios do Momentum (primeiro momento dos gradientes) e do RMSprop (segundo momento não centrado dos gradientes). É o otimizador padrão mais utilizado no estado da arte.
> - **B)** **Correta.** Conforme fundamentado na seção *2. Aprendizado de Máquina Supervisionado* deste guia, o Aprendizado Supervisionado opera sobre conjuntos de dados históricos previamente rotulados, formalizados pelo conjunto de treino $\{(x 1, y 1), (x 2, y 2), \dots, (x n, y n)\}$, onde $x i$ representa o vetor de características ( features ) e $y i$ representa o rótulo verdadeiro ( ground truth ). O objetivo do algoritmo é estimar uma função $f(x) \approx y$ com alta capacidade de generalização para amostras inéditas. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "II, apenas".
> - **C)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "III, apenas". De acordo com a teoria estudada em *4.2 Funções de Ativação Não Lineares e suas Patologias*, softmax: $\sigma(\mathbf{z}) i = \frac{e^{z i}}{\sum {j=1}^{K} e^{z j}}$ — $(0, 1)$, $\sum \sigma i = 1$ — Converte o vetor de valores reais brutos ( logits ) em uma distribuição de probabilidades normalizada. — Exclusiva da camada de saída em problemas de classificação multiclasse mutualmente exclusivos. Nunca deve ser usada em camadas ocultas intermediárias.
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e II apenas". De acordo com a teoria estudada em *1. Fundamentos e Paradigmas da Inteligência Artificial*, a Inteligência Artificial (IA) estuda e projeta entidades computacionais capazes de realizar tarefas cognitivas historicamente associadas à inteligência biológica humana, tais como percepção visual, tomada de decisão sob incerteza, raciocínio lógico dedutivo e aprendizado contínuo.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "I, II e III". De acordo com a teoria estudada em *1.1 Dimensões de Russell & Norvig e o Conceito de Agente Racional*, pensar Racionalmente: Baseia se em sistemas de lógica formal dedutiva (silogismos e cálculo proposicional). Limitação prática: incapacidade de lidar eficientemente com incertezas, dados probabilísticos e o conhecimento informal difuso do mundo real.
>
> **Gabarito: B**

---

### Teste 019
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Administrativa - Ciência de Dados)**
Sobre a Análise Exploratória de Dados (AED), avalie as afirmativas a seguir. I. A AED permite a obtenção do entendimento sobre os dados coletados. II. A AED fornece uma ideia de como os dados se distribuem e sua forma de apresentação. III. Algoritmos de Machine Learning são as principais ferramentas utilizadas na AED. Está correto o que se afirma em

* **A)** I, apenas.
* **B)** I e II, apenas.
* **C)** I e III, apenas.
* **D)** II e III, apenas.
* **E)** I, II e III.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I, apenas". De acordo com a teoria estudada em *2.1 Modelos e Algoritmos de Classificação*, apesar dessa premissa ser quase sempre violada no mundo real, apresenta eficácia e velocidade ímpares na filtragem de spam, análise de sentimento e classificação de textos jurídicos.
> - **B)** **Correta.** Conforme fundamentado na seção *2.1 Modelos e Algoritmos de Classificação* deste guia, algoritmo não paramétrico baseado em instâncias ( instance based ) e classificado como aprendizado preguiçoso ( lazy learning ), pois não possui uma fase de treinamento explícita que gere coeficientes ou modelos matemáticos: ele simplesmente memoriza todos os dados de treino na memória. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "I e II, apenas".
> - **C)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e III, apenas". De acordo com a teoria estudada em *2.1 Modelos e Algoritmos de Classificação*, truque do Kernel ( Kernel Trick ): Permite resolver problemas não linearmente separáveis sem a necessidade de calcular explicitamente as coordenadas em um espaço de dimensão infinita ou muito alta, substituindo o produto escalar por uma função de kernel: Linear, Polinomial ou Gaussiano RBF ( Radial Basis Function ).
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "II e III, apenas". De acordo com a teoria estudada em *4. Redes Neurais Artificiais e Deep Learning*, o Aprendizado Profundo ( Deep Learning ) fundamenta se em arquiteturas com múltiplas camadas ocultas empilhadas capazes de extrair representações hierárquicas e abstratas de dados não estruturados de ponta a ponta ( end to end ).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "I, II e III". De acordo com a teoria estudada em *3.2 Redução de Dimensionalidade (PCA, t-SNE e UMAP)*, técnica estatística linear e não supervisionada que transforma as variáveis originais em um novo conjunto de variáveis não correlacionadas denominadas Componentes Principais (PCs).
>
> **Gabarito: B**

---

### Teste 020
**(FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo - Administração)**
O TCE-SC desenvolveu um modelo de IA para detectar fraudes em licitações. Durante o treinamento, o modelo apresentou 99% de acerto na base de dados histórica, mas, ao ser aplicado em dados novos de 2026, a precisão caiu para 55%. Esse fenômeno técnico, no qual o modelo decora os dados de treinamento mas falha em generalizar para dados novos, é conhecido como

* **A)** Underfitting.
* **B)** Overfitting.
* **C)** Normalização de Dados.
* **D)** Aprendizado não supervisionado.
* **E)** Regressão Logística.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Underfitting". De acordo com a teoria estudada em *2.2 Comitês de Modelos (Ensemble): Bagging vs. Boosting*, foco Matemático no Erro: Reduzir a Variância (combater a tendência ao overfitting de modelos complexos). — Reduzir o Viés (combater o underfitting transformando modelos simples em preditores fortes).
> - **B)** **Correta.** Conforme fundamentado na seção *4.3 Treinamento: Backpropagation, Gradiente Descendente e Otimizadores* deste guia, early Stopping: Interrompe o treinamento quando o erro no conjunto de validação começa a subir consecutivamente, evitando o overfitting. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "Overfitting".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Normalização de Dados". De acordo com a teoria estudada em *4.4 Arquiteturas Profundas: CNNs, RNNs/LSTM e Transformers*, projetadas especificamente para processar dados estruturados em grades bidimensionais ou tridimensionais (visão computacional, imagens de satélite para fiscalização de obras pelo TCE GO).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Aprendizado não supervisionado". De acordo com a teoria estudada em *1.2 Níveis de IA: Narrow AI vs. AGI vs. Superinteligência*, sistema hipotético dotado de plasticidade e capacidade cognitiva comparáveis ou equivalentes às de um ser humano adulto. Uma AGI deve ser capaz de aprender, raciocinar, transferir aprendizado entre domínios totalmente distintos e solucionar desafios inéditos sem a necessidade de reconfiguração algorítmica ou retreinamento supervisionado por humanos.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Regressão Logística". De acordo com a teoria estudada em *2.1 Modelos e Algoritmos de Classificação*, apesar do termo "regressão", é um algoritmo de classificação linear. Estima a probabilidade a posteriori de uma classe binária através da função logística sigmoide.
>
> **Gabarito: B**

---

### Teste 021
**(FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo - Engenharia Elétrica)**
Em um diagnóstico energético industrial detalhado, a análise de um sistema de utilidades, como ar comprimido ou vapor, exige uma abordagem sistêmica. Em relação às metodologias e aos requisitos para a realização de um diagnóstico energético eficaz, assinale a afirmativa correta.

* **A)** O estabelecimento da Linha de Base Energética (LBE) deve ser fundamentado em dados históricos representativos, podendo ser aprimorado por meio de modelos matemáticos, como regressão linear ou múltipla.
* **B)** A soma das eficiências individuais dos componentes de um sistema é o indicador primário para a identificação de Oportunidades de Melhoria do Desempenho Energético (OMDE).
* **C)** O Uso Significativo de Energia (USE) é definido como o consumo de energia que oferece o maior potencial de economia financeira.
* **D)** Um erro de fechamento entre a energia medida na entrada e a soma das energias úteis e perdas na saída não é aceitável, no diagnóstico.
* **E)** As recomendações de melhoria resultantes do diagnóstico devem focar em mudanças de hardware, visto que alterações em procedimentos operacionais não são quantificáveis.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O estabelecimento da Linha de Base Energética (LBE) deve ser fundamentado em dados históricos representativos...". De acordo com a teoria estudada em *1.2 Níveis de IA: Narrow AI vs. AGI vs. Superinteligência*, sistema hipotético dotado de plasticidade e capacidade cognitiva comparáveis ou equivalentes às de um ser humano adulto. Uma AGI deve ser capaz de aprender, raciocinar, transferir aprendizado entre domínios totalmente distintos e solucionar desafios inéditos sem a necessidade de reconfiguração algorítmica ou retreinamento supervisionado por humanos.
> - **B)** **Correta.** Conforme fundamentado na seção *1.1 Dimensões de Russell & Norvig e o Conceito de Agente Racional* deste guia, agir como Humanos: Medido operacionalmente pelo célebre Teste de Turing (1950). Se um avaliador humano interagindo via terminal de texto não for capaz de distinguir confiavelmente se as respostas procedem de um operador humano ou de um computador, o sistema é considerado aprovado no teste comportamental. O filósofo John Searle contra argumentou com o experimento mental do Quarto Chinês ( Chinese Room ), afirmando que a mera manipulação sintática de regras e símbolos não confere compreensão semântica ou consciência real à máquina. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "A soma das eficiências individuais dos componentes de um sistema é o indicador primário para a identificação de...".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O Uso Significativo de Energia (USE) é definido como o consumo de energia que oferece o maior potencial de...". De acordo com a teoria estudada em *1.1 Dimensões de Russell & Norvig e o Conceito de Agente Racional*, agir Racionalmente (Abordagem de Agentes Racionais): Paradigma predominante na ciência da computação contemporânea. Um Agente Racional é definido formalmente como uma entidade autônoma que.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Um erro de fechamento entre a energia medida na entrada e a soma das energias úteis e perdas na saída não é...". De acordo com a teoria estudada em *1.1 Dimensões de Russell & Norvig e o Conceito de Agente Racional*, executa intervenções físicas ou virtuais no ambiente através de Atuadores com o objetivo explícito de maximizar a sua medida de desempenho esperada.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "As recomendações de melhoria resultantes do diagnóstico devem focar em mudanças de hardware, visto que alterações...". De acordo com a teoria estudada em *3.1 Algoritmos de Agrupamento (Clustering: K-Means, DBSCAN e Hierárquico)*, limitações Clássicas: Assume que todos os clusters são convexos e esféricos com variâncias semelhantes. Falha completamente na identificação de formatos orgânicos alongados e atribui compulsoriamente todo ponto a algum cluster, sendo muito sensível a outliers.
>
> **Gabarito: B**

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

### Teste 022
**(FGV – TCE/GO – 2024 – Analista de Controle Externo - Tecnologia da Informação)**
O algoritmo Naive Bayes é amplamente utilizado em problemas de classificação, especialmente em aplicações de processamento de linguagem natural e análise de texto. O princípio fundamental do algoritmo Naive Bayes

* **A)** baseia-se na técnica de clustering para agrupar instâncias semelhantes.
* **B)** calcula a média ponderada dos atributos para determinar a classe de um exemplo.
* **C)** considera a independência condicional entre os atributos dos dados.
* **D)** utiliza redes neurais profundas para modelar relações complexas entre os atributos.
* **E)** utiliza uma abordagem de força bruta para encontrar a solução ótima de classificação.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "baseia se na técnica de clustering para agrupar instâncias semelhantes". De acordo com a teoria estudada em *2.1 Modelos e Algoritmos de Classificação*, algoritmo não paramétrico baseado em instâncias ( instance based ) e classificado como aprendizado preguiçoso ( lazy learning ), pois não possui uma fase de treinamento explícita que gere coeficientes ou modelos matemáticos: ele simplesmente memoriza todos os dados de treino na memória.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "calcula a média ponderada dos atributos para determinar a classe de um exemplo". De acordo com a teoria estudada em *2.1 Modelos e Algoritmos de Classificação*, durante a inferência, calcula a distância (Euclidiana, Manhattan ou Minkowski) entre a nova amostra e todos os pontos históricos da base, atribuindo a classe majoritária entre os $k$ vizinhos mais próximos. Sofre severamente com a maldição da dimensionalidade ( curse of dimensionality ).
> - **C)** **Correta.** Conforme fundamentado na seção *2.1 Modelos e Algoritmos de Classificação* deste guia, suposição "Ingênua" ( Naive ): Assume categoricamente que todos os atributos preditores $x 1, x 2, \dots, x d$ são mutuamente independentes entre si, dado o rótulo de classe $y$. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/GO/2024) ao estabelecer que "considera a independência condicional entre os atributos dos dados".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "utiliza redes neurais profundas para modelar relações complexas entre os atributos". De acordo com a teoria estudada em *4. Redes Neurais Artificiais e Deep Learning*, o Aprendizado Profundo ( Deep Learning ) fundamenta se em arquiteturas com múltiplas camadas ocultas empilhadas capazes de extrair representações hierárquicas e abstratas de dados não estruturados de ponta a ponta ( end to end ).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "utiliza uma abordagem de força bruta para encontrar a solução ótima de classificação". De acordo com a teoria estudada em *2.1 Modelos e Algoritmos de Classificação*, vetores de Suporte: São unicamente as instâncias críticas situadas sobre as fronteiras da margem que determinam a posição matemática e inclinação do hiperplano; todos os outros pontos podem ser adicionados ou removidos sem afetar a solução ótima.
>
> **Gabarito: C**

---

### Teste 023
**(FGV – TCE/GO – 2024 – Analista de Controle Externo - Tecnologia da Informação)**
Algumas importantes bibliotecas de programação em Python desempenham papel crucial no desenvolvimento de soluções eficientes para uma variedade de problemas em Ciência de Dados e Aprendizado de Máquina. O objetivo principal da biblioteca Pandas no contexto da ciência de dados e análise de dados é

* **A)** facilitar a manipulação e análise de dados estruturados pela disponibilização de opções de estruturas de dados.
* **B)** fornecer ferramentas para processamento de linguagem natural e textos.
* **C)** oferecer uma interface de alto nível para construção e treinamento de modelos de redes neurais.
* **D)** prover funcionalidades para manipulação de datas e horas de forma eficiente.
* **E)** realizar cálculos numéricos eficientes e manipulação de arrays multidimensionais.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *4. Redes Neurais Artificiais e Deep Learning* deste guia, o Aprendizado Profundo ( Deep Learning ) fundamenta se em arquiteturas com múltiplas camadas ocultas empilhadas capazes de extrair representações hierárquicas e abstratas de dados não estruturados de ponta a ponta ( end to end ). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/GO/2024) ao estabelecer que "facilitar a manipulação e análise de dados estruturados pela disponibilização de opções de estruturas de dados".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "fornecer ferramentas para processamento de linguagem natural e textos". De acordo com a teoria estudada em *1.3 Paradigma Simbólico vs. Paradigma Conexionista*, vantagem: Robustez incomparável a ruídos estatísticos e capacidade superior de extrair padrões latentes de alta dimensionalidade (processamento de linguagem natural e visão computacional).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "oferecer uma interface de alto nível para construção e treinamento de modelos de redes neurais". De acordo com a teoria estudada em *2.1 Modelos e Algoritmos de Classificação*, apesar dessa premissa ser quase sempre violada no mundo real, apresenta eficácia e velocidade ímpares na filtragem de spam, análise de sentimento e classificação de textos jurídicos.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "prover funcionalidades para manipulação de datas e horas de forma eficiente". De acordo com a teoria estudada em *1.3 Paradigma Simbólico vs. Paradigma Conexionista*, gargalo Histórico: Dificuldade extrema de codificar regras manuais para conhecimento implícito complexo ( knowledge acquisition bottleneck ) e total fragilidade perante ruídos em dados não estruturados (áudio, vídeo, imagens).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "realizar cálculos numéricos eficientes e manipulação de arrays multidimensionais". De acordo com a teoria estudada em *1.3 Paradigma Simbólico vs. Paradigma Conexionista*, o conhecimento não reside em regras textuais explícitas, mas sim distribuído nos pesos numéricos aprendidos por otimização estatística direta sobre grandes massas de dados.
>
> **Gabarito: A**

---

### Teste 024
**(FGV – TCE/GO – 2024 – Analista de Controle Externo - Tecnologia da Informação)**
O Keras é uma API de aprendizagem profunda escrita em Python. Sobre o Keras é incorreto afirmar que

* **A)** as principais estruturas de dados são layers e models.
* **B)** ele foi integrado ao TensorFlow como sua API de alto nível padrão.
* **C)** ele utiliza tensores para representar os dados de entrada, saída e os parâmetros do modelo.
* **D)** ele é restrito a arquiteturas específicas de redes neurais.
* **E)** qualquer modelo do Keras pode ser instanciado como um módulo do PyTorch.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "as principais estruturas de dados são layers e models". De acordo com a teoria estudada em *4.4 Arquiteturas Profundas: CNNs, RNNs/LSTM e Transformers*, redes Neurais Convolucionais (CNNs).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "ele foi integrado ao TensorFlow como sua API de alto nível padrão". De acordo com a teoria estudada em *4.4 Arquiteturas Profundas: CNNs, RNNs/LSTM e Transformers*, redes Neurais Recorrentes (RNNs) e Células LSTM / GRU.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "ele utiliza tensores para representar os dados de entrada, saída e os parâmetros do modelo". De acordo com a teoria estudada em *4.2 Funções de Ativação Não Lineares e suas Patologias*, reLU ( Rectified Linear Unit ): $f(z) = \max(0, z)$ — $[0, +\infty)$ — Padrão da indústria para camadas ocultas. Não satura para valores positivos ($z 0$, onde a derivada é $1$), permitindo treinar redes profundas rapidamente sem vanishing gradient. — Problema do Neurônio Morto ( Dying ReLU ): se uma entrada $z \le 0$, tanto a saída quanto a derivada tornam se zero. Um neurônio empurrado para essa região inerte pode nunca mais atualizar seus pesos.
> - **D)** **Correta.** Conforme fundamentado na seção *4. Redes Neurais Artificiais e Deep Learning* deste guia, o Aprendizado Profundo ( Deep Learning ) fundamenta se em arquiteturas com múltiplas camadas ocultas empilhadas capazes de extrair representações hierárquicas e abstratas de dados não estruturados de ponta a ponta ( end to end ). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/GO/2024) ao estabelecer que "ele é restrito a arquiteturas específicas de redes neurais".
> - **E)** **Incorreta.** A opção promove generalização excessiva que desconsidera as condições técnicas e normativas ao afirmar que "qualquer modelo do Keras pode ser instanciado como um módulo do PyTorch". De acordo com a teoria estudada em *2.2 Comitês de Modelos (Ensemble): Bagging vs. Boosting*, a combinação coordenada de múltiplos estimadores fracos ( weak learners ) permite construir comitês com capacidade preditiva muito superior à de qualquer modelo individual isolado.
>
> **Gabarito: D**

---

### Teste 025
**(CEBRASPE – TRF 6ª – 2025 – Analista Judiciário - Apoio Especializado - Governança e Gestão de Tecnologia da Informação)**
No treinamento de modelos generativos em deep learning, o modelo remove, gradualmente, ruído dos dados reais; em seguida, o modelo aprende a reverter esse processo, adicionando ruído aos ponchos para gerar dados semelhantes aos originais.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Incorreta.** A proposição apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "No treinamento de modelos generativos em deep learning, o modelo remove, gradualmente, ruído dos dados reais...". De acordo com a teoria em *2.3 Modelos de Regressão e Técnicas de Regularização (Ridge, Lasso e Elastic Net)*, une a capacidade de gerar modelos esparsos do Lasso com a capacidade do Ridge de manter grupos inteiros de variáveis correlacionadas dentro do modelo.
> - **E)** **Correta.** O item está **Errado** (gabarito oficial: **E**), pois contraria a disciplina teórica aplicável.
>
> **Gabarito: E**

---

### Teste 026
**(CEBRASPE – TRF 6ª – 2025 – Analista Judiciário - Apoio Especializado - Governança e Gestão de Tecnologia da Informação)**
As redes neurais feedforward processam dados de entrada até a saída em uma única direção, passando por camadas ocultas, sem ciclos, e são amplamente aplicadas em tarefas supervisionadas, como classificação e regressão.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Correta.** O item está **Certo**. Conforme fundamentado na seção *4.1 Perceptron, Limitações Lineares e Redes Multicamadas (MLP)*, a introdução de uma ou mais camadas ocultas ( hidden layers ) com funções de ativação não lineares resolveu essa limitação histórica. Segundo o Teorema da Aproximação Universal (Cybenko, 1989 / Hornik, 1991), uma rede MLP feedforward com uma única camada oculta contendo uma quantidade finita de neurônios não lineares é capaz de aproximar qualquer função contínua arbitrária com precisão pré estabelecida. Dessa forma, está plenamente correta a assertiva da banca (CEBRASPE – TRF 6ª/2025) ao afirmar que "As redes neurais feedforward processam dados de entrada até a saída em uma única direção, passando por...".
> - **E)** **Incorreta.** A assertiva não incorre em erro conceitual, guardando conformidade com a teoria estudada.
>
> **Gabarito: C**

---

### Teste 027
**(CEBRASPE – TRF 6ª – 2025 – Analista Judiciário - Apoio Especializado - Governança e Gestão de Tecnologia da Informação)**
As redes neurais convolucionais são uma classe de redes neurais artificiais projetadas para processar dados sequenciais, como texto ou áudio, utilizando camadas convolucionais que aplicam filtros para prever, diretamente, a saída final, isto é, sem extrair características intermediárias.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Incorreta.** A proposição apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "As redes neurais convolucionais são uma classe de redes neurais artificiais projetadas para processar dados...". De acordo com a teoria em *4. Redes Neurais Artificiais e Deep Learning*, o Aprendizado Profundo ( Deep Learning ) fundamenta se em arquiteturas com múltiplas camadas ocultas empilhadas capazes de extrair representações hierárquicas e abstratas de dados não estruturados de ponta a ponta ( end to end ).
> - **E)** **Correta.** O item está **Errado** (gabarito oficial: **E**), pois contraria a disciplina teórica aplicável.
>
> **Gabarito: E**

---

### Teste 028
**(FGV – TJ/RR – 2024 – Analista Judiciario Gestao E Governanca De Tecnologia Da Informacao)**
A mineração de dados está inserida no processo de descoberta de conhecimento em bases de dados, empregando diversas técnicas e métodos na execução de diferentes tarefas. Assinale a opção que contém apenas tarefas de mineração de dados.

* **A)** Árvore de Decisão e Análise de Associação.
* **B)** Classificação e Análise de Associação.
* **C)** Classificação e Redes Neurais.
* **D)** Floresta Aleatória e k Vizinhos mais Próximos.
* **E)** Regressão e k-Médias.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Árvore de Decisão e Análise de Associação". De acordo com a teoria estudada em *2.1 Modelos e Algoritmos de Classificação*, árvores de decisão profundas e sem limites de crescimento sofrem gravemente de sobreajuste ( overfitting ) (alta variância). Para mitigar essa patologia, aplicam se técnicas de poda prévia ( pre pruning , limitando a profundidade máxima max depth ou número mínimo de amostras por nó) e poda posterior ( post pruning via complexidade de custo).
> - **B)** **Correta.** Conforme fundamentado na seção *2.1 Modelos e Algoritmos de Classificação* deste guia, apesar dessa premissa ser quase sempre violada no mundo real, apresenta eficácia e velocidade ímpares na filtragem de spam, análise de sentimento e classificação de textos jurídicos. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/RR/2024) ao estabelecer que "Classificação e Análise de Associação".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Classificação e Redes Neurais". De acordo com a teoria estudada em *4. Redes Neurais Artificiais e Deep Learning*, o Aprendizado Profundo ( Deep Learning ) fundamenta se em arquiteturas com múltiplas camadas ocultas empilhadas capazes de extrair representações hierárquicas e abstratas de dados não estruturados de ponta a ponta ( end to end ).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Floresta Aleatória e k Vizinhos mais Próximos". De acordo com a teoria estudada em *2.1 Modelos e Algoritmos de Classificação*, durante a inferência, calcula a distância (Euclidiana, Manhattan ou Minkowski) entre a nova amostra e todos os pontos históricos da base, atribuindo a classe majoritária entre os $k$ vizinhos mais próximos. Sofre severamente com a maldição da dimensionalidade ( curse of dimensionality ).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Regressão e k Médias". De acordo com a teoria estudada em *2.3 Modelos de Regressão e Técnicas de Regularização (Ridge, Lasso e Elastic Net)*, o método clássico dos Mínimos Quadrados Ordinários (OLS Ordinary Least Squares ) minimiza o Erro Quadrático Médio ($\text{MSE}$). Em bases com dezenas ou centenas de variáveis multicolineares, o OLS produz coeficientes com variância gigante e sobreajuste.
>
> **Gabarito: B**

---

### Teste 029
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Administrativa - Ciência de Dados)**
As redes neurais artificiais (Artificial Neural Networks - ANN) constituem um grupo de algoritmos inspirados nas funções dos neurônios no cérebro humano. Diversas arquiteturas de redes neurais são utilizadas para diferentes problemas, conforme suas funcionalidades. Existe uma arquitetura de rede neural específica, especialmente apropriada ao reconhecimento de padrões de imagens e vídeos, por possuir as seguintes propriedades: • As informações fluem apenas em uma direção. • As informações são propagadas em diferentes camadas neurais que filtram características (isto é, as features). • As informações são propagadas em diferentes camadas que reduzem sua dimensionalidade. Das opções a seguir, as redes que mais aderem às propriedades listadas acima são as redes

* **A)** de alimentação direta (feedforward).
* **B)** recorrentes.
* **C)** convolucionais.
* **D)** generativas adversárias (GANs).
* **E)** de Hopfield.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "de alimentação direta (feedforward)". De acordo com a teoria estudada em *4.1 Perceptron, Limitações Lineares e Redes Multicamadas (MLP)*, a introdução de uma ou mais camadas ocultas ( hidden layers ) com funções de ativação não lineares resolveu essa limitação histórica. Segundo o Teorema da Aproximação Universal (Cybenko, 1989 / Hornik, 1991), uma rede MLP feedforward com uma única camada oculta contendo uma quantidade finita de neurônios não lineares é capaz de aproximar qualquer função contínua arbitrária com precisão pré estabelecida.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "recorrentes". De acordo com a teoria estudada em *4.4 Arquiteturas Profundas: CNNs, RNNs/LSTM e Transformers*, redes Neurais Recorrentes (RNNs) e Células LSTM / GRU.
> - **C)** **Correta.** Conforme fundamentado na seção *4.4 Arquiteturas Profundas: CNNs, RNNs/LSTM e Transformers* deste guia, redes Neurais Convolucionais (CNNs). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "convolucionais".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "generativas adversárias (GANs)". De acordo com a teoria estudada em *4. Redes Neurais Artificiais e Deep Learning*, o Aprendizado Profundo ( Deep Learning ) fundamenta se em arquiteturas com múltiplas camadas ocultas empilhadas capazes de extrair representações hierárquicas e abstratas de dados não estruturados de ponta a ponta ( end to end ).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "de Hopfield". De acordo com a teoria estudada em *🌐 Fontes Oficiais e Referências Bibliográficas*, pyTorch Official Tutorials Deep Learning and Neural Networks Construção de redes multicamadas (MLP), camadas lineares, ativações ReLU/Softmax e backpropagation.
>
> **Gabarito: C**

---

### Teste 030
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Administrativa - Ciência de Dados)**
As arquiteturas de modelos de linguagem de larga escala (Large Language Models - LLM) surgiram recentemente, revolucionando a área de inteligência artificial nas áreas de processamento e geração de texto. A arquitetura desses modelos baseia-se, majoritariamente, nas redes neurais do tipo transformers. Relacione as arquiteturas a seguir com suas características principais: ( ) Utiliza decoders das redes transformer para prever novos tokens a partir de uma sequência, tornando-se ideal para a geração de textos. ( ) Utiliza encoders das redes transformer para "entender" o contexto de frases, tornando-se 1. BERT ideal para classificação de textos. 2. GPT ( ) Utiliza encoders e decoders das redes transformer, sendo adaptável a situações em 3. T5 que seja necessário gerar novos textos ou processar textos para "entender" o contexto das frases. ( ) Em comparação com as outras arquiteturas, tem menor necessidade de fine-tuning para melhora de performance. A relação correta, na ordem apresentada, é

* **A)** 1 – 3 – 2 – 2.
* **B)** 2 – 3 – 1 – 3.
* **C)** 3 – 2 – 1 – 2.
* **D)** 3 – 1 – 2 – 2.
* **E)** 2 – 1 – 3 – 3.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "1 – 3 – 2 – 2". De acordo com a teoria estudada em *1.2 Níveis de IA: Narrow AI vs. AGI vs. Superinteligência*, exemplos: Classificação de transações fraudulentas pelo TCE GO, sistemas de reconhecimento facial, motores de recomendação de comércio eletrônico, grandes modelos de linguagem (LLMs) e motores de xadrez/Go. Toda a inteligência artificial desenvolvida e operacional no mundo atual pertence exclusivamente à categoria Narrow AI.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "2 – 3 – 1 – 3". De acordo com a teoria estudada em *4.4 Arquiteturas Profundas: CNNs, RNNs/LSTM e Transformers*, arquitetura Transformer (Vaswani et al., 2017).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "3 – 2 – 1 – 2". De acordo com a teoria estudada em *4.4 Arquiteturas Profundas: CNNs, RNNs/LSTM e Transformers*, revolucionou o processamento de linguagem natural ao abandonar totalmente a recorrência sequencial em favor de mecanismos de Autoatenção ( Self Attention ) e Atenção Multi Cabeça ( Multi Head Attention ).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "3 – 1 – 2 – 2". De acordo com a teoria estudada em *4.4 Arquiteturas Profundas: CNNs, RNNs/LSTM e Transformers*, redes Neurais Convolucionais (CNNs).
> - **E)** **Correta.** Conforme fundamentado na seção *🌐 Fontes Oficiais e Referências Bibliográficas* deste guia, rUSSELL, Stuart; NORVIG, Peter. Inteligência Artificial: Uma Abordagem Moderna. 4. ed. Rio de Janeiro: GEN LTC, 2022. (Cap. 18 e 19 Aprendizado a Partir de Exemplos e Redes Neurais). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "2 – 1 – 3 – 3".
>
> **Gabarito: E**

---

### Teste 031
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Administrativa - Ciência de Dados)**
Alguns dos primeiros modelos de linguagem de larga escala desenvolvidos tendiam a gerar resultados incorretos com excesso de confiança, caracterizando o que se convencionou chamar de alucinações dos modelos. Uma estratégia de mitigação das alucinações é o uso da técnica de Geração Aumentada por Recuperação, ou Retrieval-Augmented Generation (RAG). A respeito da RAG, avalie as afirmativas a seguir. I. Baseia-se na combinação de sistemas de recuperação de informações e de modelos generativos capazes de produzir novos textos. II. Permite aos modelos buscarem informações relevantes em bases de dados mais confiáveis durante o processamento das consultas dos usuários (user queries), viabilizando melhor adequação a contextos e melhor qualidade das respostas. III. Não altera os parâmetros dos modelos generativos, e, portanto, não influencia o treinamento das redes neurais com informações recuperadas de bases de dados externas. Está correto o que se afirma em

* **A)** I, apenas.
* **B)** II, apenas.
* **C)** III, apenas.
* **D)** I e II, apenas.
* **E)** I, II e III.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I, apenas". De acordo com a teoria estudada em *1.1 Dimensões de Russell & Norvig e o Conceito de Agente Racional*, pensar Racionalmente: Baseia se em sistemas de lógica formal dedutiva (silogismos e cálculo proposicional). Limitação prática: incapacidade de lidar eficientemente com incertezas, dados probabilísticos e o conhecimento informal difuso do mundo real.
> - **B)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "II, apenas". De acordo com a teoria estudada em *4.3 Treinamento: Backpropagation, Gradiente Descendente e Otimizadores*, propagação Direta ( Forward Pass ): Os dados avançam pelas camadas da rede até produzir uma saída predita $\hat{y}$, que é comparada ao rótulo real $y$ através de uma Função de Perda ($\mathcal{L}$).
> - **C)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "III, apenas". De acordo com a teoria estudada em *2.1 Modelos e Algoritmos de Classificação*, hiperparâmetro $C$ (Margem Suave): Controla o compromisso entre a largura da margem e a tolerância a erros de classificação: um $C$ elevado penaliza violações severamente (margem estreita, risco de sobreajuste); um $C$ baixo admite mais violações em troca de margens mais amplas (maior viés e melhor generalização).
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e II, apenas". De acordo com a teoria estudada em *2.1 Modelos e Algoritmos de Classificação*, durante a inferência, calcula a distância (Euclidiana, Manhattan ou Minkowski) entre a nova amostra e todos os pontos históricos da base, atribuindo a classe majoritária entre os $k$ vizinhos mais próximos. Sofre severamente com a maldição da dimensionalidade ( curse of dimensionality ).
> - **E)** **Correta.** Conforme fundamentado na seção *4. Redes Neurais Artificiais e Deep Learning* deste guia, o Aprendizado Profundo ( Deep Learning ) fundamenta se em arquiteturas com múltiplas camadas ocultas empilhadas capazes de extrair representações hierárquicas e abstratas de dados não estruturados de ponta a ponta ( end to end ). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "I, II e III".
>
> **Gabarito: E**

---

## 🌐 Fontes Oficiais e Referências Bibliográficas

* [Scikit-Learn Official User Guide - Supervised Learning](https://scikit-learn.org/stable/supervised_learning.html) - Classificação e regressão: Regressão Linear, Árvores de Decisão, SVM, Naive Bayes e Ensembles.
* [Scikit-Learn Official User Guide - Unsupervised Learning](https://scikit-learn.org/stable/unsupervised_learning.html) - Algoritmos de agrupamento (K-Means, DBSCAN) e redução de dimensionalidade (PCA).
* [PyTorch Official Tutorials - Deep Learning and Neural Networks](https://pytorch.org/tutorials/beginner/basics/buildmodel_tutorial.html) - Construção de redes multicamadas (MLP), camadas lineares, ativações ReLU/Softmax e backpropagation.
* [ArXiv - Attention Is All You Need (Vaswani et al.)](https://arxiv.org/abs/1706.03762) - Arquitetura de rede Transformer e mecanismo de autoatenção pura.
* RUSSELL, Stuart; NORVIG, Peter. **Inteligência Artificial: Uma Abordagem Moderna**. 4. ed. Rio de Janeiro: GEN LTC, 2022. (Cap. 18 e 19 - Aprendizado a Partir de Exemplos e Redes Neurais).
* GÉRON, Aurélien. **Mãos à Obra: Aprendizado de Máquina com Scikit-Learn, Keras & TensorFlow**. 3. ed. Rio de Janeiro: Alta Books, 2023. (Cap. 4 a 6 - Modelos Lineares, SVMs e Árvores de Decisão).
* GOODFELLOW, Ian; BENGIO, Yoshua; COURVILLE, Aaron. **Deep Learning**. Cambridge: MIT Press, 2016. (Cap. 6 - Redes Profundas Feedforward; Cap. 9 - Redes Convolucionais).
