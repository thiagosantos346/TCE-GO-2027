# Módulo 09: Inteligência Artificial e Ciência de Dados
## 02. PLN, IA Generativa, Agentes Inteligentes e Multimodalidade

**Última Atualização:** 2026-03-31  
**Banca Foco:** FCC (Fundação Carlos Chagas)  
**Cargo:** Auditor de Controle Externo - Tecnologia da Informação  
**Status do Mapeamento:** 100% aderente ao edital TCE-GO

---

### 📌 Ementa / Itens do Edital
1. **Processamento de Linguagem Natural (PLN / NLP):** Pipeline clássico de pré-processamento (limpeza, normalização, tokenização por subpalavras com BPE/WordPiece, remoção de stopwords vs. impacto em modelos contextuais, normalização morfológica com Stemming vs. Lemmatization, POS Tagging e NER com esquema BIO); Representação vetorial de textos (Bag of Words, ponderação TF-IDF e embeddings estáticos Word2Vec CBOW/Skip-Gram e FastText com n-gramas de caracteres); e Modelos contextuais baseados em Transformers (Atenção escalada, Encoder-Only com BERT e Masked Language Modeling vs. Decoder-Only com GPT e Causal Language Modeling).
2. **Inteligência Artificial Generativa:** Conceito de distribuição generativa $P(X)$; Redes Adversárias Generativas (GANs: jogo de minimax entre Gerador e Discriminador, instabilidades e patologia do Colapso de Modo / *Mode Collapse*); Modelos de Difusão (*Diffusion Models*: processo direto com adição progressiva de ruído gaussiano e processo reverso de reconstrução com redes U-Net); e Modelos de Linguagem Autoregressivos (LLMs: amostragem probabilística, temperatura, Top-$k$ e Top-$p$ Nucleus Sampling).
3. **Agentes Inteligentes:** Conceituação formal de Agente Racional (sensores, atuadores, função de agente); Framework PEAS (*Performance, Environment, Actuators, Sensors*); Propriedades taxonômicas dos ambientes de tarefas (observabilidade, determinismo, episodicidade, dinamismo, continuidade e número de agentes); e Classificação clássica de Russell & Norvig (Agentes Reativos Simples, Reativos Baseados em Modelos com estado interno, Baseados em Objetivos, Baseados na Utilidade e Agentes com Aprendizado).
4. **Modelos Multimodais:** Fundamentos de multimodalidade sensorial (texto, imagem, áudio e vídeo); Alinhamento semântico cross-modal com aprendizado contrastivo (Arquitetura CLIP: codificadores paralelos de visão e texto, espaço latente compartilhado e classificação *Zero-Shot*); e Aplicações no setor público e controle externo (OCR inteligente de processos administrativos, auditoria de notas fiscais digitalizadas e cruzamento de imagens de satélite/drones com relatórios de medição de obras públicas).

---

### 🧭 Sumário
- [1. Processamento de Linguagem Natural (PLN / NLP)](#1-processamento-de-linguagem-natural-pln--nlp)
  - [1.1 Pipeline de Pré-Processamento Textual Clássico](#11-pipeline-de-pré-processamento-textual-clássico)
  - [1.2 Representação Numérica de Texto: BoW, TF-IDF e Embeddings Estáticos](#12-representação-numérica-de-texto-bow-tf-idf-e-embeddings-estáticos)
  - [1.3 A Revolução dos Transformers em PLN: BERT vs. GPT](#13-a-revolução-dos-transformers-em-pln-bert-vs-gpt)
- [2. Inteligência Artificial Generativa](#2-inteligência-artificial-generativa)
  - [2.1 Fundamentos e Arquiteturas Generativas](#21-fundamentos-e-arquiteturas-generativas)
  - [2.2 Redes Adversárias Generativas (GANs) e Colapso de Modo](#22-redes-adversárias-generativas-gans-e-colapso-de-modo)
  - [2.3 Modelos de Difusão (Diffusion Models)](#23-modelos-de-difusão-diffusion-models)
  - [2.4 Modelos de Linguagem Autoregressivos (LLMs) e Parâmetros de Amostragem](#24-modelos-de-linguagem-autoregressivos-llms-e-parâmetros-de-amostragem)
- [3. Agentes Inteligentes e Ambientes de Tarefa](#3-agentes-inteligentes-e-ambientes-de-tarefa)
  - [3.1 O Framework PEAS e Definição de Agente Racional](#31-o-framework-peas-e-definição-de-agente-racional)
  - [3.2 Propriedades dos Ambientes de Tarefa](#32-propriedades-dos-ambientes-de-tarefa)
  - [3.3 As Cinco Tipologias Clássicas de Agentes (Russell & Norvig)](#33-as-cinco-tipologias-clássicas-de-agentes-russell--norvig)
- [4. Modelos Multimodais e Aplicações no Setor Público](#4-modelos-multimodais-e-aplicações-no-setor-público)
  - [4.1 Alinhamento Semântico Multimodal e a Arquitetura CLIP](#41-alinhamento-semântico-multimodal-e-a-arquitetura-clip)
  - [4.2 Aplicações em Auditoria de Controle Externo (TCE-GO)](#42-aplicações-em-auditoria-de-controle-externo-tce-go)
- [5. Questões Comentadas (FCC)](#5-questões-comentadas-fcc)

---

## 1. Processamento de Linguagem Natural (PLN / NLP)

O Processamento de Linguagem Natural é a disciplina interdisciplinar na fronteira entre a Ciência da Computação, Inteligência Artificial e Linguística Formal voltada a viabilizar a compreensão, interpretação, análise e geração da linguagem humana em formato computacional.

### 1.1 Pipeline de Pré-Processamento Textual Clássico

O pré-processamento transforma textos brutos e não estruturados em representações limpas e padronizadas:

1. **Limpeza e Normalização:** Conversão de caracteres alfanuméricos para minúsculas (*lowercasing*), remoção de tags de marcação (HTML/XML), eliminação de caracteres de controle invisíveis e normalização de diacríticos e acentuações via formatos Unicode (NFC/NFD).
2. **Tokenização:** Decomposição do fluxo textual em unidades discretas denominadas *tokens*:
   - *Por palavras:* Separação baseada em espaços e pontuação. Falha gravemente na presença de termos compostos, contrações e gírias.
   - *Por subpalavras (*Subword Tokenization*):* Padrão hegemônico adotado por modelos baseados em Transformers. Algoritmos como **BPE (*Byte-Pair Encoding*)**, **WordPiece** e **SentencePiece** começam na granularidade de caracteres e unem progressivamente pares de símbolos estatisticamente frequentes na base de treino.
   - *Vantagem Crítica:* Palavras conhecidas permanecem unificadas em um único token, enquanto termos raros, neologismos ou jargões jurídicos são decompostos em morfemas inteligíveis (ex.: *"anticonstitucionalidade"* $\rightarrow$ `anti` + `constitucional` + `idade`), **eliminando completamente o problema de palavras fora do vocabulário (*Out-Of-Vocabulary - OOV*)**.
3. **Remoção de Stopwords:** Expurgamento de palavras funcionais com altíssima frequência estatística na língua, mas com teor discriminativo isolado ínfimo (artigos, preposições e conectivos como "de", "o", "em", "para", "que").
   - *Atenção:* Essa técnica é vital para reduzir dimensionalidade e ruído em modelos estatísticos de frequência (*Bag of Words*, TF-IDF); porém, **é contraindicada e jamais deve ser aplicada em modelos baseados em Transformers contextuais (BERT, GPT)**, pois pronomes e preposições são indispensáveis para o cálculo da autoatenção sintática e semântica entre termos na oração.
4. **Normalização Morfológica: Stemming vs. Lemmatization**

| Dimensão Comparativa | Stemming (Troncamento / Radicalização) | Lemmatization (Lematização) |
| :--- | :--- | :--- |
| **Abordagem Operacional** | Heurística, mecânica e puramente algorítmica. Corta prefixos e sufixos com regras fixas de expressões regulares. | Linguística, sintática e estrutural. Consulta léxicos, dicionários morfológicos oficiais e corpora gramaticais. |
| **Análise Morfossintática** | **Não analisa a classe gramatical**. Aplica as mesmas regras de corte sem considerar se a palavra funciona como verbo, substantivo ou adjetivo. | **Analisa a classe gramatical (POS)** no contexto da oração para extrair a forma de dicionário correta. |
| **Resultado Produzido** | Um **radical (*stem*)** que **frequentemente não é uma palavra válida** no léxico da língua portuguesa. | Um **lema (*lemma*)**, que é **obrigatoriamente uma palavra canônica válida** do vocabulário (ex.: verbos no infinitivo, substantivos no singular masculino). |
| **Exemplo Prático** | "Auditorias", "auditores", "auditar" $\rightarrow$ **"audit"** (radical truncado). | "Melhores" $\rightarrow$ **"bom"**; "foram" $\rightarrow$ **"ir"** ou **"ser"** (conforme a função sintática contextual). |
| **Custo Computacional** | Extremamente rápido, leve e de execução instantânea. | Mais lento; consome mais memória e depende de bibliotecas gramaticais robustas (ex.: spaCy, NLTK com WordNet). |
| **Algoritmos Canônicos** | Algoritmo de Porter, Snowball, RSLP (*Removedor de Sufixos da Língua Portuguesa*). | Lematizador morfológico spaCy, Lematizador WordNet. |

5. **Análise Linguística Especializada:**
   - **POS Tagging (*Part-of-Speech Tagging*):** Identificação e rotulação sintática da classe gramatical de cada token na oração (Substantivo, Verbo, Adjetivo, Preposição).
   - **NER (*Named Entity Recognition* - Reconhecimento de Entidades Nomeadas):** Identificação de termos específicos no texto estruturados em categorias predefinidas de interesse do órgão (Pessoas, Empresas/Organizações, Valores Monetários, Processos, Datas, CPFs e CNPJs), utilizando a notação padronizada **BIO**: `B-` (*Beginning*, início da entidade), `I-` (*Inside*, continuação interna da entidade) e `O` (*Outside*, fora de qualquer entidade).

> ⚠️ **Alerta de Prova (FCC):**
> A banca FCC costuma afirmar que o *Stemming* gera palavras de dicionário perfeitas e que a *Lematização* corta sufixos aleatoriamente. Lembre-se: é o contrário! O **Stemming corta sufixos de forma mecânica/cega gerando radicais inválidos**; a **Lematização utiliza dicionários e morfologia para extrair o lema canônico oficial**.

### 1.2 Representação Numérica de Texto: BoW, TF-IDF e Embeddings Estáticos

1. **Bag of Words (BoW - Saco de Palavras):**
   - Cria um vocabulário fixo de $V$ palavras a partir da base documental. Cada documento é representado por um vetor esparso de dimensão $V$ contendo a contagem simples de ocorrência de cada palavra.
   - *Limitações Graves:* Vetores com dimensionalidade massiva e esparsidade extrema; **perda total da sintaxe, contexto e ordem das palavras** (as frases *"o réu processou o auditor"* e *"o auditor processou o réu"* produzem vetores exatamente idênticos no BoW).

2. **TF-IDF (*Term Frequency - Inverse Document Frequency*):**
   - Modula a frequência local do termo ponderando-a pela sua raridade estatística na coleção global de documentos:
     $$\text{TF-IDF}(t, d, D) = \text{TF}(t, d) \times \text{IDF}(t, D)$$
     $$\text{IDF}(t, D) = \log\left(\frac{N}{|\{d \in D : t \in d\}|}\right)$$
     onde $N = |D|$ representa o total de documentos do corpus e o denominador representa quantos documentos contêm o termo $t$.
   - Se um termo aparece em 100% dos documentos da base ($|\{d \in d\}| = N$), a fração interna é $N/N = 1$ e seu $\text{IDF} = \log(1) = 0$. Assim, palavras genéricas ou termos institucionais comuns a todos os processos (ex.: "Tribunal", "Processo") são naturalmente silenciadas.
   - Termos específicos de fraudes ou itens incomuns de auditoria que aparecem repetidas vezes em poucos relatórios recebem altas pontuações de TF-IDF.

3. **Embeddings Estáticos Densos (Word2Vec e FastText):**
   - Mapeiam cada vocábulo em um vetor numérico denso contínuo (geralmente entre 100 e 300 dimensões).
   - Apoiam-se na célebre **Hipótese Distribucional** de J. R. Firth (1957): *"Você conhecerá uma palavra pela companhia que ela mantém"*. Termos que coocorrem em contextos vizinhos similares situam-se próximos geometricamente no espaço vetorial.
   - **Word2Vec (Mikolov et al., 2013):**
     - *CBOW (Continuous Bag of Words):* Prevê a palavra central alvo a partir da média dos vetores das palavras contextuais da janela circundante. Mais rápido para treinar e eficiente para vocabulários frequentes.
     - *Skip-Gram:* Recebe a palavra central e prevê a distribuição de probabilidade das palavras de contexto vizinhas. Apresenta performance superior para capturar palavras raras e vocabulários complexos.
   - **FastText (Facebook AI Research):**
     - Estende o Word2Vec ao representar cada palavra como um saco de **n-gramas de caracteres** (ex.: a palavra *"tribunal"* com $n=3$ é decomposta em `<tr`, `tri`, `rib`, `ibu`, `bun`, `una`, `nal`, `al>`).
     - Essa inovação permite capturar morfologia de palavras derivadas e **gerar embeddings consistentes para termos inéditos ou fora do vocabulário de treino (*OOV*)**.
   - *Limitação Canônica dos Embeddings Estáticos:* Atribuem um único vetor fixo estático para cada grafia de palavra, sendo incapazes de desambiguar sentidos polissêmicos (ex.: a palavra *"manga"* terá exatamente as mesmas coordenadas numéricas quer se refira a uma fruta, quer à manga de uma vestimenta).

### 1.3 A Revolução dos Transformers em PLN: BERT vs. GPT

A publicação do artigo histórico *"Attention Is All You Need"* (Vaswani et al., 2017) consolidou o mecanismo de **Atenção Escalada por Produto Escalar (*Scaled Dot-Product Attention*)**:
$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$
onde $Q$ são as Consultas (*Queries*), $K$ são as Chaves (*Keys*), $V$ são os Valores (*Values*) e $\sqrt{d_k}$ é o fator de escalonamento que impede que produtos escalares em alta dimensão atinjam magnitudes elevadas que saturariam a função softmax com derivadas nulas (*vanishing gradient*).

```
                      MECANISMO TRANSFORMER ORIGINAL
                                    │
           ┌────────────────────────┴────────────────────────┐
           ▼                                                 ▼
   [ ENCODER-ONLY ]                                  [ DECODER-ONLY ]
   Ex.: BERT, RoBERTa                                Ex.: Família GPT, Llama
   - Atenção Bidirecional Completa                   - Atenção Causal Unidirecional
   - Vê tokens à esquerda E à direita                - Vê estritamente tokens anteriores
   - Treino: Masked LM (preencher [MASK])            - Treino: Next Token Prediction
   - Foco: ENTENDIMENTO, Extração e                  - Foco: GERAÇÃO DE CONTEÚDO,
     Classificação Semântica                           Diálogo e Síntese Textual
```

* **BERT (Bidirectional Encoder Representations from Transformers):**
  - Modelo baseado puramente no **Codificador (*Encoder-Only*)**.
  - Opera em regime **estritamente bidirecional**: ao processar um token, as camadas de autoatenção conectam-no simultaneamente a todas as palavras à esquerda e à direita na sentença.
  - Pré-treinado via **Masked Language Modeling (MLM)** (ocultando 15% dos tokens aleatoriamente com a tag `[MASK]` para que o modelo aprenda a reconstruí-los a partir do contexto global) e **Next Sentence Prediction (NSP)**.
  - Ideal para tarefas de compreensão textual profunda: Classificação de Documentos, Reconhecimento de Entidades Nomeadas (NER), Pergunta-Resposta Extrativa e Busca Semântica em Bases Vetoriais.
* **GPT (Generative Pre-trained Transformer):**
  - Modelo baseado puramente no **Decodificador (*Decoder-Only*)**.
  - Opera em regime **autoregressivo unidirecional com máscara causal triangular**: para preservar a validade da geração contínua, cada token só pode consultar os tokens que o antecederam cronologicamente na sequência (atenção orientada da esquerda para a direita).
  - Pré-treinado via **Causal Language Modeling (CLM)**, ajustando pesos para prever iterativamente a probabilidade condicional do próximo token ($P(w_t \mid w_1, \dots, w_{t-1})$).
  - Ideal para geração criativa e contínua de texto, síntese de minutas processuais, tradução e diálogos interativos.

---

## 2. Inteligência Artificial Generativa

A IA Generativa fundamenta-se em arquiteturas matemáticas capazes de estimar a densidade de probabilidade $P(X)$ subjacente a distribuições empíricas de dados, permitindo a amostragem estocástica para sintetizar novos dados fidedignos e inéditos.

### 2.1 Fundamentos e Arquiteturas Generativas

Enquanto a IA Discriminativa calcula $P(y \mid X)$ para separar instâncias em classes, a IA Generativa modela os padrões intrínsecos de formação dos dados. As três principais famílias contemporâneas são: GANs, Modelos de Difusão e LLMs Autoregressivos.

### 2.2 Redes Adversárias Generativas (GANs) e Colapso de Modo

Introduzidas por Ian Goodfellow em 2014, as **GANs (*Generative Adversarial Networks*)** fundamentam-se em duas redes neurais profundas que competem entre si em um jogo de minimax de soma zero da teoria dos jogos:

```
[Ruído Estocástico z] ──► [ GERADOR (G) ] ──► Imagem Sintética ──┐
                                                                 ▼
[Dataset Real] ─────────────────────────────► Imagem Real ─────► [ DISCRIMINADOR (D) ]
                                                                        │
                                                                        ▼
                                                         Decisão: Real (1) ou Fake (0)?
                                                                        │
               (O erro realimenta D e o gradiente ajusta G) ◄───────────┘
```

- **Gerador ($G$):** Mapeia um vetor latente de ruído aleatório $z \sim p_z$ em uma amostra sintética que busca reproduzir com fidelidade a distribuição real dos dados $p_{\text{data}}$.
- **Discriminador ($D$):** Classificador binário que recebe uma amostra (genuína ou sintética) e emite a probabilidade $D(x) \in [0, 1]$ de a imagem ser real.
- **Função Minimax Objetiva:**
  $$\min_G \max_D V(D, G) = \mathbb{E}_{x \sim p_{\text{data}}}[\log D(x)] + \mathbb{E}_{z \sim p_z}[\log(1 - D(G(z)))]$$
- **Colapso de Modo (*Mode Collapse*):**
  - É a patologia mais célebre no treinamento de GANs.
  - Ocorre quando o Gerador encontra uma única amostra sintética específica (ou uma diversidade insignificante de amostras) altamente eficaz em enganar o Discriminador. O Gerador passa então a **produzir repetidamente e sempre a mesma saída idêntica**, ignorando a riqueza e variedade do restante do espaço amostral.

### 2.3 Modelos de Difusão (Diffusion Models)

Tornaram-se o estado da arte na síntese de imagens e mídias de alta fidelidade (DALL-E 3, Midjourney, Stable Diffusion):
- **Processo Direto (*Forward Diffusion Process*):** Degrada progressivamente uma imagem real através de uma cadeia de Markov em $T$ etapas temporais discretas, inserindo pequenas frações de ruído branco gaussiano até que a imagem original se converta integralmente em ruído térmico caótico não correlacionado.
- **Processo Reverso (*Reverse Diffusion Process*):** Uma rede neural profunda especializada (geralmente uma arquitetura U-Net associada a mecanismos de atenção cruzada condicionados por texto) é treinada para predizer e remover iterativamente a fração exata de ruído adicionada em cada passo. Partindo de puro ruído gaussiano aleatório, o modelo desconstrói o ruído passo a passo até reconstituir uma imagem hiper-realista.
- **Vantagem sobre GANs:** Apresentam treinamento estritamente estável, livre de dinâmicas adversárias em minimax e **completamente imunes ao colapso de modo**, cobrindo com excelência toda a distribuição do espaço latente.

### 2.4 Modelos de Linguagem Autoregressivos (LLMs) e Parâmetros de Amostragem

Os modelos autoregressivos geram textos computando a probabilidade condicional de cada token sucessivo com base em todos os tokens precedentes:
$$P(w_1, w_2, \dots, w_T) = \prod_{t=1}^{T} P(w_t \mid w_{<t})$$

A conversão do vetor de números reais (*logits*) emitido pela rede em tokens textuais finais é governada por parâmetros de amostragem na camada Softmax:

1. **Temperatura ($T$):**
   - Modula a magnitude dos logits antes da normalização pela função Softmax: $P(w_i) = \frac{e^{z_i / T}}{\sum_j e^{z_j / T}}$.
   - **Baixa Temperatura ($T \to 0$):** Concentra a probabilidade quase inteiramente no token mais provável, gerando respostas determinísticas, rígidas, concisas e factuais.
   - **Alta Temperatura ($T > 1$):** Suaviza a curva de probabilidades, elevando as chances de tokens menos frequentes serem sorteados, gerando respostas mais criativas, variadas e diversas (com maior propensão a alucinações se excessivamente alta).
2. **Top-$k$ Sampling:**
   - Restringe o sorteio do próximo token estritamente aos $k$ tokens que possuem as maiores probabilidades imediatas, truncando a cauda longa de tokens improváveis.
3. **Top-$p$ Sampling (Amostragem por Núcleo / *Nucleus Sampling*):**
   - Em vez de fixar uma contagem estática $k$, seleciona dinamicamente o menor conjunto de tokens cuja soma cumulativa de probabilidades atinja o limiar estipulado $p$ (ex.: $p = 0.90$).
   - Adapta-se fluidamente: em momentos de certeza gramatical, o núcleo pode conter apenas 1 ou 2 tokens; em contextos abertos, o núcleo expande-se dinamicamente para dezenas de opções viáveis.

---

## 3. Agentes Inteligentes e Ambientes de Tarefa

### 3.1 O Framework PEAS e Definição de Agente Racional

Na ciência da computação clássica formalizada por Stuart Russell e Peter Norvig, um **Agente** é qualquer entidade dotada de sensores para apreender percepções e de atuadores para intervir no mundo:

```
                  ┌───────────────────────────────────────────────┐
                  │                 AMBIENTE                      │
                  └──────┬─────────────────────────────────▲──────┘
                         │                                 │
                 Fluxo de Percepções                Ações Executadas
                         │                                 │
                         ▼                                 │
                  ┌───────────────┐               ┌────────────────┐
                  │   SENSORES    │               │   ATUADORES    │
                  └──────┬────────┘               └────────▲───────┘
                         │                                 │
                         ▼                                 │
                  ┌────────────────────────────────────────┴───────┐
                  │               FUNÇÃO DE AGENTE                 │
                  │ (Mapeamento formal: Percepções* ──► Ação)      │
                  └────────────────────────────────────────────────┘
```

Para projetar formalmente um agente inteligente, especifica-se o framework **PEAS**:
- **P (Performance / Medida de Desempenho):** O critério matemático ou lógico que define o sucesso da missão atribuída ao agente.
- **E (Environment / Ambiente):** O contexto operacional, sistemas de software ou espaço físico onde o agente atua.
- **A (Actuators / Atuadores):** Os canais ou dispositivos pelos quais o agente age sobre o ambiente.
- **S (Sensors / Sensores):** Os instrumentos de entrada pelos quais o agente recolhe dados do ambiente.

### 3.2 Propriedades dos Ambientes de Tarefa

A arquitetura e os algoritmos do agente são diretamente moldados pelas características de seu ambiente de tarefa:
1. **Totalmente Observável vs. Parcialmente Observável:** O ambiente é totalmente observável se os sensores acessam o estado global completo a cada instante (ex.: Xadrez). Se houver pontos cegos, variáveis ocultas ou incertezas sensoriais, é parcialmente observável (ex.: fiscalização de fraudes fiscais, trânsito).
2. **Determinístico vs. Estocástico:** É determinístico se o próximo estado do sistema é completamente definido pelo estado atual e pela ação empregada pelo agente. Se houver aleatoriedade, incerteza ou ruído externo, é estocástico.
3. **Episódico vs. Sequencial:** No ambiente episódico, a experiência divide-se em episódios atômicos isolados onde a ação presente não impacta o futuro (ex.: classificar uma imagem de nota fiscal). No sequencial, a decisão atual dita as oportunidades de todas as etapas seguintes (ex.: partidas de xadrez, direção autônoma).
4. **Estático vs. Dinâmico:** É estático se o ambiente não se altera enquanto o agente delibera; é dinâmico se o mundo continua evoluindo e mudando enquanto o algoritmo processa sua decisão.
5. **Discreto vs. Contínuo:** Se os estados, ações e percepções são contáveis em passos finitos ou representados por variáveis contínuas no tempo e espaço.
6. **Agente Único vs. Multiagente:** Se a entidade opera isoladamente no ambiente ou se interage com outros agentes em regimes cooperativos ou competitivos.

### 3.3 As Cinco Tipologias Clássicas de Agentes (Russell & Norvig)

1. **Agente Reativo Simples (*Simple Reflex Agent*):**
   - Decide sua ação baseando-se estritamente na percepção atual imediata por meio de regras de **Condição-Ação** ($if \text{ condição } then \text{ ação}$).
   - Não possui histórico nem memória de percepções passadas. Sofre com loops infinitos e falha em ambientes parcialmente observáveis.
2. **Agente Reativo Baseado em Modelos (*Model-Based Reflex Agent*):**
   - Mantém um **Estado Interno** persistente na memória que reflete o histórico de percepções e o conhecimento sobre "como o mundo evolui de forma independente" e "como as próprias ações do agente afetam o ambiente".
   - Consegue operar com excelência em **ambientes parcialmente observáveis**, deduzindo informações que não estão diretamente acessíveis nos sensores naquele instante.
3. **Agente Baseado em Objetivos (*Goal-Based Agent*):**
   - Combina o estado interno do mundo com a descrição explícita de uma ou mais **Metas/Objetivos**. Utiliza algoritmos de busca e planejamento para selecionar trajetórias de ações que conduzam ao estado final desejado.
4. **Agente Baseado na Utilidade (*Utility-Based Agent*):**
   - Substitui metas binárias por uma **Função de Utilidade** contínua ($U(s) \in \mathbb{R}$) que mensura formalmente o grau numérico de desejabilidade de cada estado do mundo.
   - Permite tomar decisões ótimas balanceando trade-offs entre múltiplos objetivos conflitantes (ex.: balancear velocidade de fiscalização vs. risco de falsos positivos sob incerteza probabilística).
5. **Agente com Aprendizado (*Learning Agent*):**
   - Transcende as limitações do projeto inicial programado, evoluindo seu comportamento ao longo do tempo. É dividido formalmente em quatro módulos funcionais:
     - *Elemento de Desempenho:* Seleciona as ações externas imediatas.
     - *Elemento de Aprendizado:* Responsável por introduzir melhorias nas regras do agente.
     - *Crítica:* Avalia o comportamento do agente comparando as percepções a um padrão externo de sucesso.
     - *Gerador de Problemas:* Propõe ações exploratórias inéditas para adquirir novos conhecimentos.

---

## 4. Modelos Multimodais e Aplicações no Setor Público

A Multimodalidade representa a capacidade dos sistemas modernos de IA de ingerir, alinhar, correlacionar e sintetizar simultaneamente informações provenientes de múltiplas modalidades sensoriais (texto, imagem, áudio e vídeo).

### 4.1 Alinhamento Semântico Multimodal e a Arquitetura CLIP

O marco fundamental que consolidou a visão-linguagem moderna foi o modelo **CLIP (*Contrastive Language-Image Pre-training* - Radford et al., OpenAI, 2021)**:

```
[Imagem de Obra Pública] ──► [ Codificador Visual (ViT/ResNet) ] ──► Vetor Imagem (I) ──┐
                                                                                         ├──► Espaço Vetorial Latente
[Texto: "Asfalto com trincas"] ──► [ Codificador Textual (Transformer) ] ──► Vetor Texto (T) ───┘    Compartilhado
                                                                                               (Alta Similaridade Cos)
```

- **Mecanismo de Aprendizado Contrastivo:**
  - O CLIP é alimentado por lotes massivos de pares correspondentes $(Imagem_i, Texto_i)$.
  - Os vetores gerados pelo codificador visual e pelo codificador de texto são projetados em um **espaço vetorial latente compartilhado de dimensão idêntica**.
  - A função de perda contrastiva (**InfoNCE Loss**) atua em duas frentes complementares:
    - **Maximiza** a similaridade de cosseno entre a imagem $I_i$ e seu texto descritivo correto $T_i$ (pares positivos);
    - **Minimiza** a similaridade de cosseno entre a imagem $I_i$ e todas as outras legendas incorretas $T_j$ no mesmo minilote (pares negativos).
- **Classificação Zero-Shot (*Zero-Shot Classification*):**
  - O CLIP dispensa retreinamento supervisionado para novas classes. Para classificar uma foto inédita, projeta-se o embedding da imagem e compara-se sua similaridade de cosseno contra os embeddings textuais de vários prompts candidatos gerados dinamicamente (ex.: *"uma foto de [obra concluída]"*, *"uma foto de [obra abandonada]"*). A classe com maior proximidade angular é selecionada.

### 4.2 Aplicações em Auditoria de Controle Externo (TCE-GO)

1. **Auditoria de Obras e Engenharia Pública:** Uso de Modelos de Visão-Linguagem (VLMs) para inspecionar fotografias de vistorias técnicas, imagens de satélite multiespectrais e vídeos capturados por drones, cruzando automaticamente evidências visuais com o cronograma físico-financeiro e as planilhas orçamentárias de medição da obra pública.
2. **OCR Semântico de Documentos Administrativos Legados:** Digitalização e leitura ótica inteligente de contratos históricos, certidões com caligrafia manual e processos digitalizados com baixa resolução, onde o modelo de linguagem contextual auxilia o modelo visual na recomposição de termos degradados pelo tempo.
3. **Detecção de Fraudes em Notas Fiscais Eletrônicas:** Análise combinada de comprovantes digitalizados, carimbos notariais e fotos de mercadorias entregues, identificando discrepâncias materiais em compras governamentais.

---

## 5. Questões Comentadas (FCC)

### Questão 01
**(FCC - DPE-RS - Analista de Tecnologia da Informação)**
Durante o planejamento de uma esteira analítica de Processamento de Linguagem Natural (PLN) para indexação temática e extração de entidades em acórdãos e peças jurídicas de um tribunal, os analistas debatem os métodos adequados de normalização textual e representação vetorial.
A respeito das técnicas de processamento de texto, assinale a alternativa correta:
A) O *Stemming* consiste na identificação morfológica e sintática da classe gramatical de cada vocábulo em um dicionário estruturado para retornar unicamente o infinitivo canônico oficial do termo, enquanto a *Lematização* descarta regras gramaticais e aplica supressões de sufixos de forma puramente mecânica.
B) O algoritmo de tokenização por subpalavras *Byte-Pair Encoding* (BPE) inicia com um vocabulário fixo composto exclusivamente por sentenças inteiras e as divide progressivamente até alcançar letras individuais, gerando matrizes esparsas sem redundância.
C) Em abordagens estatísticas de recuperação de informação baseadas em TF-IDF, a remoção de *stopwords* é indicada para mitigar a alta dimensionalidade e expurgar palavras frequentes de baixo teor discriminativo; contudo, em modelos contextuais baseados em Transformers (como o BERT), as *stopwords* não devem ser removidas, pois a presença de artigos, pronomes e preposições é indispensável para o cálculo das relações de autoatenção contextual.
D) O componente IDF (*Inverse Document Frequency*) da matriz TF-IDF atribui peso máximo a termos que ocorrem em cem por cento dos documentos da coleção, visto que termos universais são estatisticamente os melhores descritores da base temática.
E) O modelo *Word2Vec* gera representações vetoriais dinâmicas que alteram as coordenadas de uma palavra conforme o contexto imediato de cada sentença em que ela se encontra, superando a rigidez estática dos modelos contextuais BERT e GPT.

> **Comentário Detalhado:**
> - **A)** Incorreta. Houve inversão completa: a **Lematização** é quem consulta dicionários e analisa a morfossintaxe contextual para produzir o lema canônico de dicionário; o **Stemming** é quem aplica cortes brutos e mecânicos de afixos sem respaldo sintático.
> - **B)** Incorreta. O BPE opera na direção inversa (*bottom-up*): começa no nível de caracteres e funde iterativamente os pares de símbolos mais frequentes observados na base até formar as subpalavras.
> - **C)** **Correta.** Em modelos estatísticos de frequência (*Bag of Words*, TF-IDF), eliminar *stopwords* reduz a dimensionalidade e descarta ruídos irrelevantes. Por outro lado, em arquiteturas de *Deep Learning* fundamentadas na **Autoatenção de Transformers** (como BERT e GPT), a presença de palavras funcionais (preposições, conectivos, pronomes) é mandatória para que o mecanismo de atenção modele com precisão a estrutura semântica e sintática das sentenças.
> - **D)** Incorreta. O IDF é formulado como $\log(N / df)$. Se um termo figura em todos os documentos ($df = N$), a fração é $N/N = 1$ e seu $\text{IDF} = \log(1) = 0$, recebendo pontuação **nula**, e não máxima.
> - **E)** Incorreta. O *Word2Vec* gera embeddings **estáticos** (cada vocábulo recebe um vetor fixo e imutável); quem gera embeddings **contextuais e dinâmicos** são exatamente os modelos baseados em Transformers (BERT, RoBERTa, GPT).
> 
> **Gabarito: C**

---

### Questão 02
**(FCC - TCE-RS - Auditor Público Externo - Tecnologia da Informação)**
A teoria canônica de Inteligência Artificial formalizada por Stuart Russell e Peter Norvig organiza o projeto de sistemas computacionais autônomos com base no conceito de Agentes Racionais operando em Ambientes de Tarefas caracterizados pela taxonomia do framework PEAS (*Performance, Environment, Actuators, Sensors*).
A respeito da classificação e do comportamento dos agentes inteligentes, assinale a alternativa correta:
A) Os Agentes Reativos Simples tomam decisões baseadas no planejamento preditivo de cenários futuros contingenciais e mantêm um histórico analítico de todas as percepções passadas.
B) Os Agentes Reativos Baseados em Modelos mantêm um estado interno dependente do histórico de percepções, o que lhes permite atuar de forma coerente em ambientes parcialmente observáveis, inferindo variáveis e aspectos do mundo que não estão acessíveis nos sensores no instante da decisão.
C) Os Agentes Baseados em Objetivos utilizam uma função escalar contínua de utilidade para equilibrar matematicamente a compensação entre objetivos conflitantes quando nenhum resultado perfeito for passível de concretização.
D) O ambiente de auditoria e fiscalização fiscal de um órgão de controle externo é classificado no framework PEAS como totalmente observável e estático, pois todos os fatos econômicos dos jurisdicionados são imediatamente conhecidos sem latência ou incerteza.
E) Um agente racional é definido estritamente como aquele que reproduz com total exatidão as falhas cognitivas e o processo emocional do cérebro humano, rejeitando o conceito de maximização de medidas de desempenho esperadas.

> **Comentário Detalhado:**
> - **A)** Incorreta. Agentes Reativos Simples não realizam planejamento nem possuem memória interna; agem mecanicamente por regras condição-ação ($if \dots then \dots$) vinculadas exclusivamente à percepção imediata do instante presente.
> - **B)** **Correta.** O **Agente Reativo Baseado em Modelos** possui uma estrutura interna de **estado** que encapsula o histórico e o conhecimento sobre a evolução do mundo exterior, permitindo deduzir facetas do ambiente que não estão diretamente ao alcance de seus sensores naquele instante, superando os desafios de ambientes **parcialmente observáveis**.
> - **C)** Incorreta. A utilização de uma função de utilidade escalar contínua para mediar múltiplos objetivos conflitantes é atribuição do **Agente Baseado na Utilidade** (*Utility-Based Agent*). Agentes Baseados em Objetivos operam com avaliação booleana binária de metas (atingiu ou não atingiu o objetivo).
> - **D)** Incorreta. Ambientes de controle externo e auditoria tributária são comprovadamente **parcialmente observáveis** (fraudes e sonegações são camufladas) e **dinâmicos** (a economia e os jurisdicionados continuam operando enquanto os relatórios são elaborados).
> - **E)** Incorreta. O Agente Racional é formalmente conceituado como a entidade computacional que atua para **maximizar a sua medida de desempenho esperada**, apoiando-se em suas percepções e em seu conhecimento acumulado, e não como um simulador de limitações cognitivas humanas.
> 
> **Gabarito: B**

---

### Questão 03
**(FCC - SEFAZ-PE - Auditoria de Tecnologia da Informação)**
A publicação da arquitetura *Transformer* impulsionou a criação de modelos de linguagem pré-treinados profundos que hoje alicerçam grande parte do estado da arte em Processamento de Linguagem Natural. A partir desse paradigma, destacaram-se duas famílias arquiteturais com propriedades distintas: os modelos baseados no Codificador (*Encoder*) e os baseados no Decodificador (*Decoder*).
Sobre as diferenças técnicas entre as famílias BERT e GPT, assinale a afirmativa correta:
A) O modelo BERT baseia-se exclusivamente no Decodificador do Transformer, empregando máscaras causais triangulares para impedir que tokens à direita interfiram na classificação do texto presente.
B) O modelo GPT fundamenta-se no Codificador do Transformer e processa sentenças em regime estritamente bidirecional, sendo treinado para reconstruir palavras ocultadas aleatoriamente por tokens especiais de preenchimento.
C) O modelo BERT baseia-se no Codificador e processa as sequências de forma bidirecional no treinamento para aprender representações contextuais profundas, sendo excelente para tarefas de classificação, busca semântica e reconhecimento de entidades; enquanto os modelos da família GPT são decodificadores autoregressivos unidirecionais voltados precipuamente à geração contínua do próximo token.
D) O mecanismo de autoatenção escalada divide o produto escalar das matrizes de Consulta e Chave pelo cubo da dimensionalidade dos vetores para induzir a explosão intencional dos gradientes na fase de retropropagação.
E) Os modelos BERT e GPT dispensam etapas de pré-treinamento auto-supervisionado, sendo inicializados e treinados diretamente em conjuntos de dados supervisionados anotados manualmente por auditores.

> **Comentário Detalhado:**
> - **A)** Incorreta. O BERT utiliza o **Codificador (*Encoder-Only*)** e opera de forma livremente **bidirecional**, sem máscaras causais triangulares restritivas.
> - **B)** Incorreta. A família GPT baseia-se no **Decodificador (*Decoder-Only*)** e opera de forma autoregressiva unidirecional com a tarefa de previsão do próximo token (*Next Token Prediction*). Quem utiliza palavras mascaradas (*MLM*) é o BERT.
> - **C)** **Correta.** 
>   - **BERT (Encoder-Only):** Conecta tokens simultaneamente aos seus contextos à esquerda e à direita (bidirecional). Excelente para tarefas de análise, extração, classificação e busca semântica em bases vetoriais.
>   - **GPT (Decoder-Only):** Estrutura causal autoregressiva que prevê sequencialmente a probabilidade condicional do próximo token ($P(w_t \mid w_{<t})$), sendo o motor ideal para geração contínua de texto, sumarização e interação conversacional.
> - **D)** Incorreta. O fator de escalonamento da atenção divide o produto escalar pela **raiz quadrada** da dimensão ($\sqrt{d_k}$) com o objetivo expresso de **evitar a saturação da função softmax**, prevenindo o desvanecimento dos gradientes (*vanishing gradient*).
> - **E)** Incorreta. Ambos os modelos fundamentam-se no paradigma do pré-treinamento auto-supervisionado maciço em gigabytes/terabytes de textos não rotulados da internet.
> 
> **Gabarito: C**

---

### Questão 04
**(FCC - TRF-3ª Região - Analista Judiciário - Informática)**
No domínio da Inteligência Artificial Generativa, diferentes famílias de redes neurais profundas foram consolidadas para síntese realista de dados multidimensionais, destacando-se as Redes Adversárias Generativas (GANs) e os Modelos de Difusão (*Diffusion Models*).
A respeito das características arquiteturais dessas tecnologias generativas, assinale a alternativa correta:
A) As GANs consistem em um jogo de minimax competitivo no qual o Gerador busca mapear vetores de ruído em dados sintéticos fidedignos para enganar o Discriminador, sendo o fenômeno de Colapso de Modo (*Mode Collapse*) uma patologia clássica em que o Gerador passa a emitir saídas repetitivas de variedade extremamente restrita.
B) Os Modelos de Difusão são treinados por um jogo adversário de soma zero entre duas redes antagônicas que calculam a divergência estocástica de matrizes convolucionais estáticas.
C) O processo reverso dos Modelos de Difusão consiste na degradação contínua da imagem real mediante a injeção paulatina de ruído branco gaussiano, dispensando o uso de redes neurais para reconstrução de padrões.
D) As GANs são consagradas pelo meio acadêmico devido à sua garantia inata de estabilidade matemática irrestrita de convergência de gradientes durante o processo de treinamento, sendo imunes a desbalanceamentos de forças entre as redes.
E) Modelos de Difusão são incapazes de gerar imagens a partir de descrições textuais (*Text-to-Image*), operando exclusivamente sobre tensores tabulares esparsos de bancos relacionais.

> **Comentário Detalhado:**
> - **A)** **Correta.** Nas GANs (Goodfellow et al., 2014), o Gerador e o Discriminador disputam um jogo de minimax. A patologia do **Colapso de Modo (*Mode Collapse*)** é um dos seus maiores riscos operacionais: ocorre quando o Gerador encontra uma saída específica capaz de enganar o Discriminador com facilidade e passa a sintetizar repetidamente sempre aquela mesma imagem (ou poucas variantes), deixando de representar toda a diversidade do espaço amostral de treino.
> - **B)** Incorreta. Quem disputa jogos adversários em soma zero são as GANs. Modelos de Difusão baseiam-se em processos estocásticos graduais de adição e remoção de ruído via cadeias de Markov.
> - **C)** Incorreta. A injeção paulatina de ruído até a completa dissolução da imagem compõe o **Processo Direto (*Forward Process*)**. O **Processo Reverso (*Reverse Process*)** é o caminho inverso, onde uma rede neural profunda (geralmente uma U-Net) remove o ruído passo a passo para regenerar a imagem nítida.
> - **D)** Incorreta. O treino de GANs é notoriamente complexo e instável devido à delicadeza do equilíbrio de Nash entre os gradientes do Gerador e do Discriminador.
> - **E)** Incorreta. Modelos de difusão são exatamente a tecnologia padrão do estado da arte para geração de imagens a partir de prompts textuais (*Text-to-Image*, como Stable Diffusion e DALL-E 3).
> 
> **Gabarito: A**

---

### Questão 05
**(FCC - TRT-2ª Região - Analista Judiciário - Tecnologia da Informação)**
Em um projeto de inovação tecnológica do tribunal, a diretoria de TI pretende implementar uma ferramenta de fiscalização capaz de cruzar fotografias de canteiros de obras públicas com os relatórios descritivos de medição de engenharia civil. A equipe técnica optou pela arquitetura multimodal CLIP (*Contrastive Language-Image Pre-training*).
Sobre os fundamentos operacionais e os benefícios metodológicos da arquitetura CLIP, é correto afirmar:
A) O modelo CLIP opera unicamente como um software sequencial de OCR baseado em expressões regulares, sendo inapto a manipular fotografias de objetos do mundo real que não possuam letreiros gravados.
B) O treinamento contrastivo do modelo CLIP projeta os vetores emitidos por um codificador visual e por um codificador textual em um espaço latente compartilhado, maximizando a similaridade de cosseno entre pares correspondentes (imagem e legenda descritiva) e minimizando a similaridade de pares desacoplados.
C) O CLIP exige que qualquer nova categoria de classificação seja submetida a um retreinamento supervisionado completo de todos os seus bilhões de parâmetros (*full fine-tuning*), sendo incapaz de executar predições no modo *Zero-Shot*.
D) O codificador visual do CLIP converte obrigatoriamente matrizes bidimensionais de pixels em faixas de áudio comprimidas antes da extração de embeddings semânticos.
E) O alinhamento semântico cross-modal exige rigorosamente que as sentenças de texto possuam o mesmo número de pixels em resolução gráfica que as matrizes de entrada das imagens.

> **Comentário Detalhado:**
> - **A)** Incorreta. O CLIP não é um OCR puramente mecânico; é uma rede neural profunda multimodal capaz de reconhecer abstrações visuais, texturas, objetos, cenas e contextos fotográficos complexos sem a presença de textos gravados na imagem.
> - **B)** **Correta.** O princípio estrutural do **CLIP** (Radford et al., OpenAI) reside no **Treinamento Contrastivo**: um codificador de imagens (ViT/ResNet) e um codificador de textos (Transformer) operam em conjunto projetando representações em um **espaço vetorial latente compartilhado de mesma dimensionalidade**, onde imagens e suas legendas corretas têm sua **similaridade de cosseno maximizada**, ao passo que combinações incorretas de pares têm sua similaridade minimizada.
> - **C)** Incorreta. Uma das maiores conquistas do CLIP é justamente a sua consagrada capacidade de **Classificação Zero-Shot**, que permite classificar imagens em categorias inéditas sem qualquer treino adicional, apenas calculando a similaridade contra prompts textuais descritivos.
> - **D)** Incorreta. O codificador visual do CLIP opera sobre tensores de imagens usando visão computacional pura (Vision Transformers ou ResNets), sem transformações em arquivos de áudio.
> - **E)** Incorreta. Sentenças de texto são sequências de tokens discretos e imagens são matrizes contínuas de pixels; a unificação ocorre no nível de projeção matemática abstrata dos embeddings latentes vetoriais (ex.: 512 dimensões), sendo descabida qualquer correspondência de resolução gráfica de pixels entre eles.
> 
> **Gabarito: B**
