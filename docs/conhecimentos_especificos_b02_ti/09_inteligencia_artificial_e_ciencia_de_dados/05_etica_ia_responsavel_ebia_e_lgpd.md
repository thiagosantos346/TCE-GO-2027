# 05 - Ética, IA Responsável, LGPD e Estratégia Brasileira de IA (EBIA)
**Última Atualização:** 2026-03-31  
**Banca Foco:** FCC (Fundação Carlos Chagas)  
**Cargo:** Auditor de Controle Externo - Tecnologia da Informação  
**Status do Mapeamento:** 100% aderente ao edital TCE-GO



---


## 📌 Ementa / Itens do Edital
1. **Ética em Inteligência Artificial e Princípios de IA Responsável:** Diretrizes internacionais (OCDE, UNESCO); Princípios de Beneficência, Justiça, Equidade (*Fairness*) e Não Discriminação; Tipologias de viés algorítmico (Histórico, Representação e Medição); Responsabilização e Prestação de Contas (*Accountability* e trilhas de auditoria); e Modelos de Supervisão Humana (*Human-in-the-Loop*, *Human-on-the-Loop* e *Human-in-Command*).
2. **Explicabilidade e Interpretabilidade Algorítmica (XAI - *Explainable AI*):** O dilema Desempenho vs. Interpretabilidade; Modelos Intrinsecamente Interpretáveis (*White-Box*: Regressões, Árvores de Decisão rasas) vs. Modelos Caixa-Preta (*Black-Box*: Ensembles complexos, Deep Learning); e Métodos de Interpretação Post-Hoc Agósticos: **SHAP** (Valores de Shapley da Teoria dos Jogos Cooperativos e axiomas de eficiência, simetria, jogador nulo e consistência) e **LIME** (perturbações locais e modelos lineares substitutos).
3. **Aplicação da LGPD (Lei nº 13.709/2018) à Inteligência Artificial:** Princípios da Não Discriminação Ilícita (Art. 6º, IX) e da Necessidade/Minimização; Bases legais para treinamento de modelos de IA no Poder Público (Art. 7º, III - execução de políticas públicas); Tratamento de Dados Pessoais Sensíveis (Art. 11); **O Artigo 20 da LGPD** (Direito à revisão de decisões unicamente automatizadas, dever de transparência sobre critérios e parâmetros, e poder de auditoria técnica direta pela ANPD em caso de alegação de segredo comercial/industrial); e Relatório de Impacto à Proteção de Dados Pessoais (RIPD / DPIA) em projetos de alto risco.
4. **Estratégia Brasileira de Inteligência Artificial (EBIA - Portaria MCTI nº 4.617/2021):** Marco regulatório nacional; Objetivos estratégicos; **Os Três Eixos Transversais** (Legislação, Regulação e Uso Ético; Governança de IA; e Aspectos Internacionais); e **Os Seis Eixos Verticais/Temáticos** (Educação e Capacitação; Força de Trabalho e Capacitação; Pesquisa, Desenvolvimento, Inovação e Empreendedorismo; Aplicação nos Setores Produtivos; Aplicação no Poder Público; e Segurança Pública).

---

## 🧭 Sumário

1. [Princípios de IA Responsável, Ética e Governança Humana](#1-principios-de-ia-responsavel-etica-e-governanca-humana)
    1. [Diretrizes Internacionais (OCDE e UNESCO)](#11-diretrizes-internacionais-ocde-e-unesco)
    2. [Vieses Algorítmicos e Métricas de Equidade (Fairness)](#12-vieses-algoritmicos-e-metricas-de-equidade-fairness)
    3. [Modelos de Supervisão Humana: HITL, HOTL e HIC](#13-modelos-de-supervisao-humana-hitl-hotl-e-hic)
    4. [Teste 344](#Teste-344)
    5. [Teste 345](#Teste-345)
    6. [Teste 346](#Teste-346)
2. [Explicabilidade e Interpretabilidade de IA (XAI)](#2-explicabilidade-e-interpretabilidade-de-ia-xai)
    1. [O Dilema Desempenho vs. Interpretabilidade](#21-o-dilema-desempenho-vs-interpretabilidade)
    2. [Método SHAP (SHapley Additive exPlanations) e seus Axiomas](#22-metodo-shap-shapley-additive-explanations-e-seus-axiomas)
    3. [Método LIME (Local Interpretable Model-Agnostic Explanations)](#23-metodo-lime-local-interpretable-model-agnostic-explanations)
    4. [Teste 347](#Teste-347)
    5. [Teste 348](#Teste-348)
    6. [Teste 349](#Teste-349)
3. [A LGPD (Lei nº 13.709/2018) Aplicada à Inteligência Artificial](#3-a-lgpd-lei-no-137092018-aplicada-a-inteligencia-artificial)
    1. [Bases Legais e Princípio da Não Discriminação](#31-bases-legais-e-principio-da-nao-discriminacao)
    2. [O Artigo 20: Revisão de Decisões Automatizadas e Auditoria da ANPD](#32-o-artigo-20-revisao-de-decisoes-automatizadas-e-auditoria-da-anpd)
    3. [Relatório de Impacto à Proteção de Dados Pessoais (RIPD)](#33-relatorio-de-impacto-a-protecao-de-dados-pessoais-ripd)
    4. [Teste 350](#Teste-350)
    5. [Teste 351](#Teste-351)
    6. [Teste 352](#Teste-352)
4. [Estratégia Brasileira de Inteligência Artificial (EBIA)](#4-estrategia-brasileira-de-inteligencia-artificial-ebia)
    1. [Marco Regulatório (Portaria MCTI nº 4.617/2021)](#41-marco-regulatorio-portaria-mcti-no-46172021)
    2. [Os Três Eixos Transversais](#42-os-tres-eixos-transversais)
    3. [Os Seis Eixos Verticais (Temáticos)](#43-os-seis-eixos-verticais-tematicos)
    4. [Teste 353](#Teste-353)
    5. [Teste 354](#Teste-354)
5. [🌐 Fontes Oficiais e Referências Bibliográficas](#fontes-oficiais-e-referencias-bibliograficas)

---

## 1. Princípios de IA Responsável, Ética e Governança Humana

À medida que sistemas de inteligência artificial são integrados a decisões de auditoria fiscal, concessão de benefícios previdenciários e detecção de irregularidades pelo Tribunal de Contas, impõe-se a observância de postulados éticos e diretrizes normativas internacionais para mitigar riscos a direitos fundamentais.

### 1.1 Diretrizes Internacionais (OCDE e UNESCO)

O arcabouço internacional de IA Responsável fundamenta-se nos princípios aprovados pela OCDE (2019) e ratificados pelo Brasil:

1. **Crescimento Inclusivo, Desenvolvimento Sustentável e Bem-Estar:** A IA deve atuar como força motriz para o progresso humano e redução de desigualdades, respeitando a dignidade e a sustentabilidade ambiental.
2. **Valores Centrados no Ser Humano e Equidade (*Human-Centric Values and Fairness*):** Os sistemas de IA devem assegurar o primado da lei, dos direitos humanos e de valores democráticos, prevenindo preconceitos e discriminações estruturais.
3. **Transparência e Explicabilidade (*Explainability*):** Dever das entidades promotoras de disponibilizar informações acessíveis para que os cidadãos compreendam quando estão interagindo com IA e os fatores objetivos que determinaram uma decisão automatizada.
4. **Robustez, Segurança e Proteção (*Robustness and Safety*):** Garantia de resiliência algorítmica contra falhas, ataques adversariais (*adversarial attacks*) e vazamentos de dados, operando de modo previsível ao longo de todo o ciclo de vida.
5. **Responsabilização e Prestação de Contas (*Accountability*):** Organizações que desenvolvem ou empregam sistemas de IA devem responder formalmente pelo seu impacto e manter registros e **trilhas de auditoria (*audit trails*)** que viabilizem a inspeção externa por órgãos de controle.

### 1.2 Vieses Algorítmicos e Métricas de Equidade (Fairness)

Algoritmos não operam no vácuo ético; eles extraem padrões matemáticos diretamente de dados históricos empíricos. Se os dados passados espelharem disparidades ou exclusões sociais, a rede neural aprenderá a perpetuar e multiplicar esses vieses (*bias in, bias out*).

* **Tipologias Canônicas de Viés Algorítmico:**
    - **Viés Histórico (*Historical Bias*):** Decorre de assimetrias preexistentes no mundo real e na sociedade, mesmo que o processo de amostragem estatística tenha sido perfeito (ex.: histórica discrepância salarial de gênero ou raça em determinados cargos).
    - **Viés de Representação (*Representation Bias*):** Sub-representação estatística de determinado grupo populacional na base amostral de treino (ex.: softwares de visão computacional e biometria facial treinados com mais de 80% de rostos masculinos e brancos, exibindo taxas de falso positivo inaceitavelmente altas para mulheres negras).
    - **Viés de Medição (*Measurement Bias*):** Ocorre quando os atributos selecionados para mensurar um fenômeno abstrato atuam como *proxies* distorcidas da realidade (ex.: adotar o número de prisões ou boletins de ocorrência como proxy de criminalidade, capturando o viés de policiamento ostensivo desproporcional em bairros periféricos).
* **Métricas Formais de Equidade (*Fairness Metrics*):**
    - *Paridade Demográfica (*Demographic Parity*):* Exige que a proporção de predições favoráveis seja idêntica entre os subgrupos protegidos ($P(\hat{y}=1 \mid A=0) = P(\hat{y}=1 \mid A=1)$).
    - *Igualdade de Oportunidades (*Equal Opportunity*):* Exige que as taxas de Verdadeiros Positivos (Sensibilidade/Recall) sejam rigorosamente iguais entre os grupos protegidos ($P(\hat{y}=1 \mid y=1, A=0) = P(\hat{y}=1 \mid y=1, A=1)$).

> ⚠️ **Alerta de Prova (FCC):**
> Atenção à falácia da "Equidade por Desconhecimento" (*Fairness through Unawareness*): a banca FCC frequentemente afirma que "para garantir que um algoritmo não discrimine, basta remover as colunas de dados sensíveis como raça ou gênero". Isso é **FALSO**! Modelos matemáticos avançados capturam facilmente variáveis correlacionadas que atuam como **substitutas indiretas (*proxies*)** do dado omitido (ex.: CEP residencial, faixa salarial, histórico escolar).

### 1.3 Modelos de Supervisão Humana: HITL, HOTL e HIC

Para mitigar decisões automatizadas danosas e salvaguardar garantias constitucionais, adotam-se três arquiteturas de governança humana:

```
[1. HUMAN-IN-THE-LOOP - HITL]
 Algoritmo Analisa Dados ──► Emite Recomendação ──► [ Decisão Final e Vínculo HUMANO ]
 (Obrigatório em sanções, condenações e cancelamentos fiscais)

[2. HUMAN-ON-THE-LOOP - HOTL]
 Algoritmo Opera Autônomo em Tempo Real ◄── [ Monitoramento Humano Contínuo ]
 (Operador possui o botão de emergência / kill switch para intervir a qualquer instante)

[3. HUMAN-IN-COMMAND - HIC]
 [ Supervisores Humanos ] ──► Definem Diretrizes Estratégicas, Políticas e Governança
```

- **Human-in-the-Loop (HITL):** O sistema de IA gera notas de probabilidade, subsídios probatórios e sugestões, mas a tomada de decisão final é **obrigatoriamente validada e executada por um ser humano**. Modelo imperativo no setor público para atos administrativos vinculantes, dosimetria de sanções e julgamento de contas.
- **Human-on-the-Loop (HOTL):** O algoritmo atua com autonomia operacional em tempo real (ex.: bloqueio instantâneo de transações financeiras fraudulentas de alto volume), porém sob **supervisão e vigilância ativa de operadores humanos**, que dispõem da prerrogativa de vetar, pausar ou reverter intervenções.
- **Human-in-Command (HIC):** A autoridade humana define as políticas éticas globais, os limites de risco, os marcos de conformidade legal e avalia periodicamente o impacto social da tecnologia.

---

### Teste 344
**(FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo - Ciências da Computação, Sistemas de Informação...)**
O Auditor fiscaliza a arquitetura de um novo banco de dados NoSQL distribuído para o TCE-SC. O sistema precisa garantir que, em caso de falha na rede entre dois data centers, o sistema continue aceitando gravações, mesmo que os dados fiquem temporariamente inconsistentes entre os nós. De acordo com o Teorema CAP, esse sistema prioriza as propriedades de

* **A)** e Tolerância a Partições (P).
* **B)** Consistência
* **C)** Disponibilidade
* **D)** Atomicidade e Durabilidade.
* **E)** Apenas Disponibilidade, ignorando partições.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "e Tolerância a Partições (P)". De acordo com a teoria estudada em *1.2 Vieses Algorítmicos e Métricas de Equidade (Fairness)*, atenção à falácia da "Equidade por Desconhecimento" (*Fairness through Unawareness*): a banca FCC frequentemente afirma que "para garantir que um algoritmo não discrimine, basta remover as colunas de dados sensíveis como raça ou gênero".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Consistência". De acordo com a teoria estudada em *1.3 Modelos de Supervisão Humana: HITL, HOTL e HIC*, human-in-the-Loop (HITL): O sistema de IA gera notas de probabilidade, subsídios probatórios e sugestões, mas a tomada de decisão final é obrigatoriamente validada e executada por um ser humano.
> - **C)** **Correta.** Conforme fundamentado na seção *1.2 Vieses Algorítmicos e Métricas de Equidade (Fairness)* deste guia, se os dados passados espelharem disparidades ou exclusões sociais, a rede neural aprenderá a perpetuar e multiplicar esses vieses (*bias in, bias out*). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "Disponibilidade".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Atomicidade e Durabilidade". De acordo com a teoria estudada em *3.2 O Artigo 20: Revisão de Decisões Automatizadas e Auditoria da ANPD*, a alegação de "segredo comercial e industrial" pelo controlador não blinda o sistema contra o Estado: o § 2º faculta formalmente à ANPD (Autoridade Nacional de Proteção de Dados) deflagrar auditoria técnica direta no código e nos dados para checar se houve discriminação abusiva.
> - **E)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "Apenas Disponibilidade, ignorando partições". De acordo com a teoria estudada em *3.2 O Artigo 20: Revisão de Decisões Automatizadas e Auditoria da ANPD*, a banca FCC costuma colocar pegadinhas em dois pontos da letra da lei.
>
> **Gabarito: C**

---

### Teste 345
**(CEBRASPE – STF – 2008 – Analista Judiciario Suporte Em Tecnologia Da Informacao)**
Preservando-se a correção gramatical do texto, bem como De acordo com as relações argumentativas do texto, se uma 9 sua coerência argumentativa, a forma verbal “mudam-se” ação não for “virtuosa” ((cid:53).7), ela não resulta de decisão ((cid:53).4) poderia ser empregada também no singular. interior; se não for “ética” ((cid:53).6), ela não será consciente, livre e responsável.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Correta.** O item está **Certo**. Conforme fundamentado na seção *1. Princípios de IA Responsável, Ética e Governança Humana* deste guia, à medida que sistemas de inteligência artificial são integrados a decisões de auditoria fiscal, concessão de benefícios previdenciários e detecção de irregularidades pelo Tribunal de Contas, impõe-se a observância de postulados éticos e diretrizes normativas internacionais para mitigar riscos a direitos fundamentais. Dessa forma, está plenamente correta a proposição da banca (CEBRASPE – STF/2008) ao afirmar que "Preservando-se a correção gramatical do texto, bem como De acordo com as relações argumentativas do texto, se...".
> - **E)** **Incorreta.** A marcação como **Errado** não procede, visto que a assertiva guarda integral conformidade com a teoria estudada em *1.3 Modelos de Supervisão Humana: HITL, HOTL e HIC*, segundo a qual human-in-the-Loop (HITL): O sistema de IA gera notas de probabilidade, subsídios probatórios e sugestões, mas a tomada de decisão final é obrigatoriamente validada e executada por um ser humano.
>
> **Gabarito: C**

---

### Teste 346
**(FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo - Economia)**
Uma pesquisadora deseja estimar o efeito da escolaridade sobre o salário mensal de trabalhadores formais por meio de uma regressão múltipla. No planejamento da pesquisa, ela discute quais variáveis incluir no modelo e como interpretar os coeficientes estimados. Do ponto de vista econométrico, a estratégia mais adequada para melhorar a identificação do efeito da escolaridade sobre o salário é

* **A)** incluir no modelo variáveis relevantes correlacionadas com salário e escolaridade, como experiência e região, para reduzir o risco de viés por variável omitida.
* **B)** estimar uma regressão simples entre salário e escolaridade, pois a inclusão de outras variáveis sempre reduz a precisão e introduz viés.
* **C)** excluir variáveis como experiência, setor e sexo, pois o objetivo da regressão múltipla é captar o efeito total da escolaridade sem controles.
* **D)** incluir o maior número possível de variáveis, ainda que irrelevantes, pois isso garante ausência de viés e causalidade.
* **E)** coletar dados apenas de trabalhadores com ensino superior completo, pois isso elimina heterogeneidade e permite estimar melhor o efeito da escolaridade.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "incluir no modelo variáveis relevantes correlacionadas com salário e escolaridade, como experiência e região, para...". De acordo com a teoria estudada em *1.2 Vieses Algorítmicos e Métricas de Equidade (Fairness)*, isso é FALSO! Modelos matemáticos avançados capturam facilmente variáveis correlacionadas que atuam como substitutas indiretas (*proxies*) do dado omitido (ex.: CEP residencial, faixa salarial, histórico escolar).
> - **B)** **Incorreta.** A opção promove generalização excessiva que desconsidera as condições técnicas e normativas ao afirmar que "estimar uma regressão simples entre salário e escolaridade, pois a inclusão de outras variáveis sempre reduz a...". De acordo com a teoria estudada em *2.3 Método LIME (Local Interpretable Model-Agnostic Explanations)*, ajusta uma regressão linear esparsa e interpretável sobre essa vizinhança ponderada. Os coeficientes dessa reta linear revelam quais atributos mais pesaram naquela decisão isolada.
> - **C)** **Correta.** Conforme fundamentado na seção *2.1 O Dilema Desempenho vs. Interpretabilidade* deste guia, possuem estrutura transparente. O efeito de uma variável em uma regressão linear é explicitado diretamente pelo coeficiente $\beta_j$; em uma árvore de decisão rasa, a inferência é descrita por regras sequenciais *se-então* legíveis. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "excluir variáveis como experiência, setor e sexo, pois o objetivo da regressão múltipla é captar o efeito total da...".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "incluir o maior número possível de variáveis, ainda que irrelevantes, pois isso garante ausência de viés e...". De acordo com a teoria estudada em *1.2 Vieses Algorítmicos e Métricas de Equidade (Fairness)*, viés de Medição (*Measurement Bias*): Ocorre quando os atributos selecionados para mensurar um fenômeno abstrato atuam como *proxies* distorcidas da realidade (ex.: adotar o número de prisões ou boletins de ocorrência como proxy de criminalidade, capturando o viés de policiamento ostensivo desproporcional em bairros periféricos).
> - **E)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "coletar dados apenas de trabalhadores com ensino superior completo, pois isso elimina heterogeneidade e permite...". De acordo com a teoria estudada em *4.3 Os Seis Eixos Verticais (Temáticos)*, educação e Capacitação: Formação de base em raciocínio computacional no ensino básico, expansão de cursos de pós-graduação em Ciência de Dados e difusão do letramento digital em IA para a sociedade.
>
> **Gabarito: C**

---

## 2. Explicabilidade e Interpretabilidade de IA (XAI)

A disciplina de IA Explicável (*Explainable Artificial Intelligence - XAI*) desenvolve métodos matemáticos para tornar as predições e decisões de modelos preditivos compreensíveis para auditores, magistrados e cidadãos.

### 2.1 O Dilema Desempenho vs. Interpretabilidade

A engenharia de dados depara-se com um compromisso arquitetural clássico:

```
ALTA  ▲  [Regressão Linear / Logística]
      │  [Árvores de Decisão Rasas]
 I    │  (Modelos White-Box: totalmente interpretáveis,
 N    │   porém com menor poder expressivo não-linear)
 T    │
 E    │                    [Random Forest / Gradient Boosting]
 R    │                    (Modelos de Ensemble)
 P    │                                         [Deep Learning / Transformers]
 R    │                                         (Modelos Black-Box: máxima precisão,
      │                                          porém matematicamente opacos)
BAIXA ┼────────────────────────────────────────────────────────────────────────►
      BAIXA                                                               ALTA
                                  DESEMPENHO PREDITIVO
```

* **Modelos Intrinsecamente Interpretáveis (*White-Box*):**
  Possuem estrutura transparente. O efeito de uma variável em uma regressão linear é explicitado diretamente pelo coeficiente $\beta_j$; em uma árvore de decisão rasa, a inferência é descrita por regras sequenciais *se-então* legíveis.
* **Modelos Caixa-Preta (*Black-Box*):**
  Redes Neurais Profundas e Ensembles avançados (*XGBoost*, *CatBoost*) realizam bilhões de multiplicações matriciais e transformações em espaços latentes de alta dimensão, impedindo a inspeção causal direta.
* **Imperativo no Setor Público:** Os Artigos 37 (*Publicidade*) e 93, IX (*Motivação dos Atos*) da Constituição Federal de 1988 vedam decisões administrativas secretas ou imotivadas. Um ato de autuação fiscal ou reprovação de contas públicas apoiado em IA exige fundamentação fática e jurídica demonstrável, tornando mandatória a aplicação de ferramentas XAI.

### 2.2 Método SHAP (SHapley Additive exPlanations) e seus Axiomas

Introduzido por Scott Lundberg e Su-In Lee (2017), o **SHAP** fundamenta-se nos **Valores de Shapley** da Teoria dos Jogos Cooperativos (reconhecida com o Prêmio Nobel de Economia concedido a Lloyd Shapley):

- **Fundamento Matemático:** Trata as variáveis preditoras (*features*) como "jogadores" em uma coalizão cooperativa. O ganho da coalizão é a predição emitida pelo modelo. O valor de Shapley $\phi_i$ calcula a **contribuição marginal média** da variável $i$ ao longo de **todas as permutações e subconjuntos possíveis de variáveis ($S \subseteq F$)**:
  $$\phi_i = \sum_{S \subseteq F \setminus \{i\}} \frac{|S|!(|F| - |S| - 1)!}{|F|!} \left[ f(S \cup \{i\}) - f(S) \right]$$

```
[Axiomas Matemáticos Canônicos do SHAP]
 1. EFICIÊNCIA / ADITIVIDADE LOCAL: f(x) = E[f(x)] + Σ φ_i
    (A soma dos valores SHAP das variáveis é RIGOROSAMENTE IGUAL à diferença
     entre a previsão da instância f(x) e a previsão média base da população)
 2. SIMETRIA: Variáveis que contribuem igualmente recebem valores SHAP idênticos.
 3. JOGADOR NULO (Dummy): Variável que não afeta a predição recebe φ_i = 0.
 4. CONSISTÊNCIA: Se um modelo muda e a contribuição marginal de uma variável
    aumenta ou permanece igual, seu valor de Shapley NUNCA diminui.
```

- **Aplicações Visuais:** O SHAP permite gerar gráficos de força locais (*Force Plots* e *Waterfall Plots*) demonstrando como cada parâmetro fiscal empurrou a probabilidade de fraude para cima ou para baixo em relação à média, bem como visões globais de importância (*Summary Plots / Beeswarm*).

### 2.3 Método LIME (Local Interpretable Model-Agnostic Explanations)

Introduzido por Marco Tulio Ribeiro et al. (2016), o **LIME** fundamenta-se na **aproximação local substituta**:

- Parte do princípio de que, embora a fronteira de decisão de um modelo complexo de Deep Learning seja extremamente não-linear em escala global, **ela se comporta de maneira aproximadamente linear em uma microvizinhança local** ao redor de uma observação específica $x$.
- **Mecânica Operacional:**
    1. Cria amostras artificiais no entorno imediato do ponto analisado mediante perturbações estocásticas nos dados;
    2. Obtém as predições do modelo caixa-preta original para todos esses vizinhos sintéticos;
    3. Pondera essas amostras de acordo com a proximidade física em relação ao ponto original (usando um kernel exponencial);
    4. Ajusta uma **regressão linear esparsa e interpretável** sobre essa vizinhança ponderada. Os coeficientes dessa reta linear revelam quais atributos mais pesaram naquela decisão isolada.

---

### Teste 347
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
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "1". De acordo com a teoria estudada em *2.1 O Dilema Desempenho vs. Interpretabilidade*, possuem estrutura transparente. O efeito de uma variável em uma regressão linear é explicitado diretamente pelo coeficiente $\beta_j$; em uma árvore de decisão rasa, a inferência é descrita por regras sequenciais *se-então* legíveis.
> - **B)** **Correta.** Conforme fundamentado na seção *2.1 O Dilema Desempenho vs. Interpretabilidade* deste guia, um ato de autuação fiscal ou reprovação de contas públicas apoiado em IA exige fundamentação fática e jurídica demonstrável, tornando mandatória a aplicação de ferramentas XAI. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/GO/2024) ao estabelecer que "2".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "3". De acordo com a teoria estudada em *2.3 Método LIME (Local Interpretable Model-Agnostic Explanations)*, ajusta uma regressão linear esparsa e interpretável sobre essa vizinhança ponderada. Os coeficientes dessa reta linear revelam quais atributos mais pesaram naquela decisão isolada.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "4". De acordo com a teoria estudada em *2.2 Método SHAP (SHapley Additive exPlanations) e seus Axiomas*, fundamento Matemático: Trata as variáveis preditoras (*features*) como "jogadores" em uma coalizão cooperativa. O ganho da coalizão é a predição emitida pelo modelo.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "5". De acordo com a teoria estudada em *2.3 Método LIME (Local Interpretable Model-Agnostic Explanations)*, parte do princípio de que, embora a fronteira de decisão de um modelo complexo de Deep Learning seja extremamente não-linear em escala global, ela se comporta de maneira aproximadamente linear em uma microvizinhança local ao redor de uma observação específica $x$.
>
> **Gabarito: B**

---

### Teste 348
**(FGV – TJ/RR – 2024 – Analista Judiciario Infraestrutura De Tecnologia Da Informacao)**
PostgreSQL 16 suporta tanto Views (Visões) quanto Materialized Views (Visões Materializadas). Considere as seguintes afirmações relacionadas a esses conceitos. I. Tanto uma Materialized View como uma View são apenas cópias virtuais, sem que haja um armazenamento físico dos dados (resultados da consulta). II. O comando REFRESH MATERIALIZED VIEW nome_da_visao_materializada; substitui completamente o conteúdo da Materialized View, descartando os dados antigos. III. A utilização da cláusula WITH NO DATA, no comando de criação de uma Materialized View, faz com que sua estrutura seja criada, mas sem preenchê-la, isto é, sem popular com dados no momento da criação. Está correto o que se afirma em

* **A)** I, apenas.
* **B)** I e II, apenas.
* **C)** I e III, apenas.
* **D)** II e III, apenas.
* **E)** I, II e III.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I, apenas". De acordo com a teoria estudada em *3.1 Bases Legais e Princípio da Não Discriminação*, princípio da Necessidade e Minimização (Art. 6º, III).
> - **B)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e II, apenas". De acordo com a teoria estudada em *2.2 Método SHAP (SHapley Additive exPlanations) e seus Axiomas*, aplicações Visuais: O SHAP permite gerar gráficos de força locais (*Force Plots* e *Waterfall Plots*) demonstrando como cada parâmetro fiscal empurrou a probabilidade de fraude para cima ou para baixo em relação à média, bem como visões globais de importância (*Summary Plots / Beeswarm*).
> - **C)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e III, apenas". De acordo com a teoria estudada em *1.2 Vieses Algorítmicos e Métricas de Equidade (Fairness)*, atenção à falácia da "Equidade por Desconhecimento" (*Fairness through Unawareness*): a banca FCC frequentemente afirma que "para garantir que um algoritmo não discrimine, basta remover as colunas de dados sensíveis como raça ou gênero".
> - **D)** **Correta.** Conforme fundamentado na seção *3.1 Bases Legais e Princípio da Não Discriminação* deste guia, o Poder Público fundamenta o desenvolvimento e treino de modelos analíticos predominantemente no Art. 7º, III da LGPD: *"para a administração pública, para o tratamento e uso compartilhado de dados necessários à execução de políticas públicas previstas em leis e regulamentos ou respaldadas em contratos, convênios ou instrumentos congêneres"*. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/RR/2024) ao estabelecer que "II e III, apenas".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "I, II e III". De acordo com a teoria estudada em *2.1 O Dilema Desempenho vs. Interpretabilidade*, possuem estrutura transparente. O efeito de uma variável em uma regressão linear é explicitado diretamente pelo coeficiente $\beta_j$; em uma árvore de decisão rasa, a inferência é descrita por regras sequenciais *se-então* legíveis.
>
> **Gabarito: D**

---

### Teste 349
**(FGV – TRT 16ª – 2022 – Analista Judiciário (Área Administrativa - Tecnologia da Informação))**
O JavaScript Object Notation (JSON) é um formato de intercâmbio de dados baseado em texto. De acordo com a gramática JSON, especificada na RFC 8259, é correto afirmar que

* **A)** um array é representado como colchetes em torno de zero ou mais elementos.
* **B)** uma string começa e termina com crases.
* **C)** nomes literais devem ser utilizados em caixa alta.
* **D)** um número é representado na base 16 usando símbolos alfanuméricos.
* **E)** um objeto é representado como um par de parênteses em torno de zero ou mais pares nome/valor.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *2.3 Método LIME (Local Interpretable Model-Agnostic Explanations)* deste guia, ajusta uma regressão linear esparsa e interpretável sobre essa vizinhança ponderada. Os coeficientes dessa reta linear revelam quais atributos mais pesaram naquela decisão isolada. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT 16ª/2022) ao estabelecer que "um array é representado como colchetes em torno de zero ou mais elementos".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "uma string começa e termina com crases". De acordo com a teoria estudada em *1.2 Vieses Algorítmicos e Métricas de Equidade (Fairness)*, viés de Representação (*Representation Bias*): Sub-representação estatística de determinado grupo populacional na base amostral de treino (ex.: softwares de visão computacional e biometria facial treinados com mais de 80% de rostos masculinos e brancos, exibindo taxas de falso positivo inaceitavelmente altas para mulheres negras).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "nomes literais devem ser utilizados em caixa alta". De acordo com a teoria estudada em *1.1 Diretrizes Internacionais (OCDE e UNESCO)*, valores Centrados no Ser Humano e Equidade (*Human-Centric Values and Fairness*): Os sistemas de IA devem assegurar o primado da lei, dos direitos humanos e de valores democráticos, prevenindo preconceitos e discriminações estruturais.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "um número é representado na base 16 usando símbolos alfanuméricos". De acordo com a teoria estudada em *2.3 Método LIME (Local Interpretable Model-Agnostic Explanations)*, pondera essas amostras de acordo com a proximidade física em relação ao ponto original (usando um kernel exponencial).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "um objeto é representado como um par de parênteses em torno de zero ou mais pares nome/valor". De acordo com a teoria estudada em *2.2 Método SHAP (SHapley Additive exPlanations) e seus Axiomas*, o valor de Shapley $\phi_i$ calcula a contribuição marginal média da variável $i$ ao longo de todas as permutações e subconjuntos possíveis de variáveis ($S \subseteq F$).
>
> **Gabarito: A**

---

## 3. A LGPD (Lei nº 13.709/2018) Aplicada à Inteligência Artificial

A Lei Geral de Proteção de Dados Pessoais regula qualquer operação de tratamento de dados de pessoas naturais realizada no território brasileiro, impondo salvaguardas mandatórias às rotinas automatizadas de inteligência artificial.

### 3.1 Bases Legais e Princípio da Não Discriminação

* **Princípio da Não Discriminação Ilícita ou Abusiva (Art. 6º, IX da LGPD):**
  Impõe como princípio cogente a *"impossibilidade de realização do tratamento para fins discriminatórios ilícitos ou abusivos"*. Obriga as instituições a realizarem auditorias preventivas contínuas sobre algoritmos para expurgar preconceitos e distorções estatísticas.
* **Bases Legais para IA no Setor Público:**
    - O Poder Público fundamenta o desenvolvimento e treino de modelos analíticos predominantemente no **Art. 7º, III da LGPD**: *"para a administração pública, para o tratamento e uso compartilhado de dados necessários à execução de políticas públicas previstas em leis e regulamentos ou respaldadas em contratos, convênios ou instrumentos congêneres"*.
    - Para Dados Pessoais Sensíveis (biometria facial, dados de saúde), a base de atuação pública vincula-se ao **Art. 11, II, "b"** (cumprimento de obrigação legal ou regulatória e execução de políticas públicas pela administração pública).
* **Princípio da Necessidade e Minimização (Art. 6º, III):**
  Veda a coleta indiscriminada de dados para alimentar bancos de IA; o tratamento deve ser restrito ao mínimo estritamente indispensável para a finalidade pretendida.

### 3.2 O Artigo 20: Revisão de Decisões Automatizadas e Auditoria da ANPD

O Artigo 20 da Lei nº 13.709/2018 constitui o epicentro do regime jurídico de inteligência artificial no Brasil:

```
┌────────────────────────────────────────────────────────────────────────────┐
│                    O ARTIGO 20 DA LGPD E SEUS DISPOSITIVOS                 │
└────────────────────────────────────────────────────────────────────────────┘
  CAPUT ──► O titular tem direito a solicitar a REVISÃO de decisões tomadas
            unicamente com base em tratamento automatizado de dados pessoais.
            (NOTA: O termo "por pessoa natural" foi VETADO na sanção presidencial)
  § 1º  ──► O controlador DEVE fornecer informações claras e adequadas a respeito
            dos CRITÉRIOS e PROCEDIMENTOS utilizados para a decisão automatizada.
            (Ressalvados eventuais segredos comercial e industrial legítimos)
  § 2º  ──► Se o controlador RECUSAR explicações invocando segredo comercial/
            industrial, a ANPD PODERÁ REALIZAR AUDITORIA TÉCNICA DIRETA para
            verificar eventuais aspectos discriminatórios abusivos no algoritmo!
```

> ⚠️ **Alerta de Prova (FCC):**
> A banca FCC costuma colocar pegadinhas em dois pontos da letra da lei:
>
> 1. O direito de revisão de decisão automatizada no caput do Art. 20 **não contém expressamente a exigência de ser feita "por pessoa natural"** (esse trecho foi formalmente vetado e o veto mantido pelo Congresso Nacional).
> 2. A alegação de "segredo comercial e industrial" pelo controlador **não blinda o sistema contra o Estado**: o § 2º faculta formalmente à **ANPD (Autoridade Nacional de Proteção de Dados)** deflagrar **auditoria técnica direta no código e nos dados** para checar se houve discriminação abusiva.

### 3.3 Relatório de Impacto à Proteção de Dados Pessoais (RIPD)

Nos termos do Art. 38 da LGPD, a ANPD pode exigir a elaboração de um **Relatório de Impacto à Proteção de Dados Pessoais (RIPD / DPIA)** para operações de tratamento que possam gerar elevado risco aos direitos fundamentais e liberdades civis.

- *Projetos de IA de Alto Risco:* Reconhecimento facial em vias públicas, escoragem preditiva automatizada de cidadãos, perfilamento em larga escala e sistemas de concessão ou cancelamento de direitos sociais devem conter obrigatoriamente um RIPD descrevendo a necessidade, a proporcionalidade e as medidas de mitigação de riscos e segurança implementadas.

---

### Teste 350
**(FGV – TJ/AP – 2023 – Analista Judiciario Apoio Especializado Tecnologia Da Informacao Seguranca Da Informacao)**
Um órgão público, vinculado à União, contratou a solução de inteligência artificial da empresa SmartDecisionIA com a finalidade específica de realizar o tratamento automatizado de decisões com base em um banco de dados gerido pelo órgão. Seguindo as instruções fornecidas pelo gestor público responsável e estabelecidas em contrato, a SmartDecisionIA realiza as operações necessárias para viabilizar o tratamento dos dados em questão. Nesse cenário, o papel da empresa SmartDecisionIA é:

* **A)** operadora;
* **B)** controladora;
* **C)** órgão de pesquisa;
* **D)** encarregada;
* **E)** data protection officer.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *3. A LGPD (Lei nº 13.709/2018) Aplicada à Inteligência Artificial* deste guia, a Lei Geral de Proteção de Dados Pessoais regula qualquer operação de tratamento de dados de pessoas naturais realizada no território brasileiro, impondo salvaguardas mandatórias às rotinas automatizadas de inteligência artificial. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/AP/2023) ao estabelecer que "operadora".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "controladora". De acordo com a teoria estudada em *1. Princípios de IA Responsável, Ética e Governança Humana*, à medida que sistemas de inteligência artificial são integrados a decisões de auditoria fiscal, concessão de benefícios previdenciários e detecção de irregularidades pelo Tribunal de Contas, impõe-se a observância de postulados éticos e diretrizes normativas internacionais para mitigar riscos a direitos fundamentais.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "órgão de pesquisa". De acordo com a teoria estudada em *4. Estratégia Brasileira de Inteligência Artificial (EBIA)*, a Estratégia Brasileira de Inteligência Artificial (EBIA) foi formalmente instituída pelo Governo Federal por meio da Portaria MCTI nº 4.617, de 6 de abril de 2021, com o propósito de articular investimentos públicos e privados, promover a pesquisa e capacitação, e assegurar o uso ético da tecnologia.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "encarregada". De acordo com a teoria estudada em *3.1 Bases Legais e Princípio da Não Discriminação*, veda a coleta indiscriminada de dados para alimentar bancos de IA; o tratamento deve ser restrito ao mínimo estritamente indispensável para a finalidade pretendida.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "data protection officer". De acordo com a teoria estudada em *3.3 Relatório de Impacto à Proteção de Dados Pessoais (RIPD)*, nos termos do Art. 38 da LGPD, a ANPD pode exigir a elaboração de um Relatório de Impacto à Proteção de Dados Pessoais (RIPD / DPIA) para operações de tratamento que possam gerar elevado risco aos direitos fundamentais e liberdades civis.
>
> **Gabarito: A**

---

### Teste 351
**(FGV – TCE/GO – 2024 – Analista de Controle Externo - Jurídica)**
Em um município do interior do país, Joaquim Maria, com objetivo de desfrutar da sua aposentadoria, comprou uma chácara de Franciso José por meio de escritura pública com pagamento à vista com imissão imediata da posse. As despesas com a celebração do contrato foram pagas por Joaquim. Seis meses após a celebração do contrato, Joaquim tem ciência que Franciso havia adquirido a chácara de Brás Cubas, contudo a venda foi anulada por vício formal. Destaca-se que Joaquim e Francisco não tinham ciência do vício ou da possibilidade de anulação. No contrato de compra e venda, inexistia qualquer cláusula a respeito da evicção. Analise a situação hipotética com base no tema evicção e assinale a opção correta.

* **A)** A boa-fé do alienante exclui sua responsabilidade pela evicção, devendo o adquirente acionar diretamente o causador do vício formal.
* **B)** Como se trata de princípio de ordem pública, é vedada as partes a inclusão de cláusula contratual que exclua a garantia contra a evicção.
* **C)** Entre outros valores, Joaquim Maria tem direito à restituição integral do preço e à indenização pelas despesas do contrato de compra e venda.
* **D)** Caso Joaquim Maria tenha realizada benfeitorias na chácara, somente as necessárias serão restituídas por Francisco José.
* **E)** A evicção se caracteriza como fenômeno jurídico subjetivo e, por isso, depende do conhecimento ou da culpa do alienante para a sua ocorrência.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A boa-fé do alienante exclui sua responsabilidade pela evicção, devendo o adquirente acionar diretamente o...". De acordo com a teoria estudada em *4.3 Os Seis Eixos Verticais (Temáticos)*, força de Trabalho e Capacitação: Requalificação profissional contínua (*reskilling* e *upskilling*) para mitigar os impactos da automação no mercado de trabalho formal e preparar trabalhadores para novas funções tecnológicas.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Como se trata de princípio de ordem pública, é vedada as partes a inclusão de cláusula contratual que exclua a...". De acordo com a teoria estudada em *1.1 Diretrizes Internacionais (OCDE e UNESCO)*, robustez, Segurança e Proteção (*Robustness and Safety*): Garantia de resiliência algorítmica contra falhas, ataques adversariais (*adversarial attacks*) e vazamentos de dados, operando de modo previsível ao longo de todo o ciclo de vida.
> - **C)** **Correta.** Conforme fundamentado na seção *3.2 O Artigo 20: Revisão de Decisões Automatizadas e Auditoria da ANPD* deste guia, o direito de revisão de decisão automatizada no caput do Art. 20 não contém expressamente a exigência de ser feita "por pessoa natural" (esse trecho foi formalmente vetado e o veto mantido pelo Congresso Nacional). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/GO/2024) ao estabelecer que "Entre outros valores, Joaquim Maria tem direito à restituição integral do preço e à indenização pelas despesas do...".
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "Caso Joaquim Maria tenha realizada benfeitorias na chácara, somente as necessárias serão restituídas por Francisco...". De acordo com a teoria estudada em *3. A LGPD (Lei nº 13.709/2018) Aplicada à Inteligência Artificial*, a Lei Geral de Proteção de Dados Pessoais regula qualquer operação de tratamento de dados de pessoas naturais realizada no território brasileiro, impondo salvaguardas mandatórias às rotinas automatizadas de inteligência artificial.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A evicção se caracteriza como fenômeno jurídico subjetivo e, por isso, depende do conhecimento ou da culpa do...". De acordo com a teoria estudada em *1.2 Vieses Algorítmicos e Métricas de Equidade (Fairness)*, viés de Medição (*Measurement Bias*): Ocorre quando os atributos selecionados para mensurar um fenômeno abstrato atuam como *proxies* distorcidas da realidade (ex.: adotar o número de prisões ou boletins de ocorrência como proxy de criminalidade, capturando o viés de policiamento ostensivo desproporcional em bairros periféricos).
>
> **Gabarito: C**

---

### Teste 352
**(FGV – TJ/MT – 2024 – Analista Judiciario Tecnologia Da Informacao)**
A linguagem de programação R é uma linguagem especializada em análise estatística e manipulação de dados, muito popular em áreas como ciência de dados, estatísticas, biotecnologia, econometria e inteligência artificial. Desenvolvida por Ross Ihaka e Robert Gentleman na década de 1990, R foi projetada para fornecer um ambiente de desenvolvimento para análise de dados, com um foco particular em estatísticas e gráficos. Em R, o operador %in%

* **A)** compara dois vetores e retorna TRUE se todos os elementos do primeiro vetor estiverem contidos no segundo.
* **B)** realiza a união de dois vetores, retornando um vetor com todos os elementos exclusivos dos dois vetores.
* **C)** verifica se dois vetores têm exatamente os mesmos elementos e na mesma ordem, retornando TRUE ou FALSE.
* **D)** calcula a interseção entre dois vetores, retornando apenas os elementos que são comuns entre eles.
* **E)** verifica se um elemento ou conjunto de elementos do primeiro vetor está presente no segundo vetor, retornando um vetor lógico.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "compara dois vetores e retorna TRUE se todos os elementos do primeiro vetor estiverem contidos no segundo". De acordo com a teoria estudada em *3.2 O Artigo 20: Revisão de Decisões Automatizadas e Auditoria da ANPD*, a banca FCC costuma colocar pegadinhas em dois pontos da letra da lei.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "realiza a união de dois vetores, retornando um vetor com todos os elementos exclusivos dos dois vetores". De acordo com a teoria estudada em *3.2 O Artigo 20: Revisão de Decisões Automatizadas e Auditoria da ANPD*, o Artigo 20 da Lei nº 13.709/2018 constitui o epicentro do regime jurídico de inteligência artificial no Brasil.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "verifica se dois vetores têm exatamente os mesmos elementos e na mesma ordem, retornando TRUE ou FALSE". De acordo com a teoria estudada em *3.1 Bases Legais e Princípio da Não Discriminação*, o Poder Público fundamenta o desenvolvimento e treino de modelos analíticos predominantemente no Art. 7º, III da LGPD: *"para a administração pública, para o tratamento e uso compartilhado de dados necessários à execução de políticas públicas previstas em leis e regulamentos ou respaldadas em contratos, convênios ou instrumentos congêneres"*.
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "calcula a interseção entre dois vetores, retornando apenas os elementos que são comuns entre eles". De acordo com a teoria estudada em *2.2 Método SHAP (SHapley Additive exPlanations) e seus Axiomas*, o valor de Shapley $\phi_i$ calcula a contribuição marginal média da variável $i$ ao longo de todas as permutações e subconjuntos possíveis de variáveis ($S \subseteq F$).
> - **E)** **Correta.** Conforme fundamentado na seção *3. A LGPD (Lei nº 13.709/2018) Aplicada à Inteligência Artificial* deste guia, a Lei Geral de Proteção de Dados Pessoais regula qualquer operação de tratamento de dados de pessoas naturais realizada no território brasileiro, impondo salvaguardas mandatórias às rotinas automatizadas de inteligência artificial. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/MT/2024) ao estabelecer que "verifica se um elemento ou conjunto de elementos do primeiro vetor está presente no segundo vetor, retornando um...".
>
> **Gabarito: E**

---

## 4. Estratégia Brasileira de Inteligência Artificial (EBIA)

A **Estratégia Brasileira de Inteligência Artificial (EBIA)** foi formalmente instituída pelo Governo Federal por meio da **Portaria MCTI nº 4.617, de 6 de abril de 2021**, com o propósito de articular investimentos públicos e privados, promover a pesquisa e capacitação, e assegurar o uso ético da tecnologia.

### 4.1 Marco Regulatório (Portaria MCTI nº 4.617/2021)

A EBIA estrutura-se em uma arquitetura matricial dividida categoricamente entre **3 Eixos Transversais** (fundamentos regulatórios, éticos e globais) e **6 Eixos Verticais** (áreas temáticas concretas de aplicação socioeconômica).

```
┌────────────────────────────────────────────────────────────────────────────┐
│         ARQUITETURA CANÔNICA DA EBIA (PORTARIA MCTI Nº 4.617/2021)         │
└────────────────────────────────────────────────────────────────────────────┘
         3 EIXOS TRANSVERSAIS (Fundamentos Sistêmicos Globais)
         ├── 1. Legislação, Regulação e Uso Ético
         ├── 2. Governança de IA
         └── 3. Aspectos Internacionais (Harmonização com a OCDE)

         6 EIXOS VERTICAIS (Áreas Temáticas de Aplicação)
         ├── 1. Educação e Capacitação
         ├── 2. Força de Trabalho e Capacitação (Reskilling / Transição)
         ├── 3. Pesquisa, Desenvolvimento, Inovação e Empreendedorismo
         ├── 4. Aplicação nos Setores Produtivos (Agro, Indústria, Saúde)
         ├── 5. Aplicação no Poder Público (Governo Digital e Controle)
         └── 6. Segurança Pública (Forense e Combate ao Crime Organizado)
```

### 4.2 Os Três Eixos Transversais

1. **Legislação, Regulação e Uso Ético:**
    - Promover um ambiente normativo propício à inovação com segurança jurídica, adotando mecanismos flexíveis como os **Ambientes Regulatórios Experimentais (*Regulatory Sandboxes*)**.
    - Garantir a observância irrestrita aos princípios éticos centrados na dignidade humana, nos direitos fundamentais e na não discriminação.

2. **Governança de IA:**
    - Estruturar fóruns multissetoriais participativos (governo, academia, setor produtivo e sociedade civil organizada) para monitorar diretrizes, métricas de transparência e auditoria algorítmica.

3. **Aspectos Internacionais:**
    - Posicionar ativamente o Brasil nos debates internacionais multilaterais (OCDE, UNESCO, G20 e Mercosul), alinhando padrões e fomentando a cooperação científica transfronteiriça.

### 4.3 Os Seis Eixos Verticais (Temáticos)

1. **Educação e Capacitação:** Formação de base em raciocínio computacional no ensino básico, expansão de cursos de pós-graduação em Ciência de Dados e difusão do letramento digital em IA para a sociedade.
2. **Força de Trabalho e Capacitação:** Requalificação profissional contínua (*reskilling* e *upskilling*) para mitigar os impactos da automação no mercado de trabalho formal e preparar trabalhadores para novas funções tecnológicas.
3. **Pesquisa, Desenvolvimento, Inovação e Empreendedorismo:** Financiamento aos Centros de Pesquisas Aplicadas (CPAs) em IA, fomento a startups de base científica (*deep techs*) e atração de capital de risco privado.
4. **Aplicação nos Setores Produtivos:** Difusão da IA na agricultura de precisão (Agritech), na manufatura digital (Indústria 4.0), no sistema financeiro e na telemedicina diagnóstica.
5. **Aplicação no Poder Público:** Transformação digital da administração pública (Governo Digital), aprimoramento da prestação de serviços ao cidadão e modernização da fiscalização tributária e da auditoria de controle externo pelo TCE-GO.
6. **Segurança Pública:** Emprego legítimo de modelos preditivos e visão computacional na elucidação de crimes complexos, perícia forense digital, vigilância de fronteiras e proteção de infraestruturas cibernéticas críticas, sob estrita conformidade legal e supervisão judicial.

---

### Teste 353
**(FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo - Economia)**
Em 1985, no início do governo Sarney, a economia brasileira saía da recessão do começo da década, mas convivia com inflação muito elevada, forte indexação de contratos e crescente incerteza sobre qual estratégia seria mais adequada para estabilizar os preços. Nesse contexto, ganhou força o debate entre interpretações ortodoxas e heterodoxas da inflação brasileira, que orientou diferentes tentativas de combate inflacionário ao longo da segunda metade dos anos 1980, como os planos Cruzado, Bresser e Verão. Considerando esse debate e as políticas então adotadas, assinale a afirmativa correta.

* **A)** A visão ortodoxa atribuía a inflação sobretudo à indexação e, por isso, defendia prioritariamente congelamento de preços e reforma monetária, enquanto a visão heterodoxa enfatizava o excesso de demanda e o ajuste fiscal recessivo.
* **B)** A heterodoxia enfatizava a inflação inercial e, por isso, defendia congelamento de preços e desindexação; já o Plano Bresser combinou esse diagnóstico com preocupação também com o excesso de demanda.
* **C)** O Plano Cruzado, embora heterodoxo, distinguiu-se por ter sido precedido de forte ajuste fiscal e monetário, o que explica seu sucesso duradouro no controle da inflação.
* **D)** O Plano Verão afastou-se tanto da ortodoxia quanto da heterodoxia, pois rejeitou simultaneamente o congelamento de preços, a desindexação e o controle da demanda agregada.
* **E)** Todos os planos de estabilização dos anos 1980 partiram exclusivamente do diagnóstico ortodoxo de que a inflação decorria do déficit público, razão pela qual abandonaram reformas monetárias e controles de preços.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *1.2 Vieses Algorítmicos e Métricas de Equidade (Fairness)* deste guia, viés de Representação (*Representation Bias*): Sub-representação estatística de determinado grupo populacional na base amostral de treino (ex.: softwares de visão computacional e biometria facial treinados com mais de 80% de rostos masculinos e brancos, exibindo taxas de falso positivo inaceitavelmente altas para mulheres negras). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "A visão ortodoxa atribuía a inflação sobretudo à indexação e, por isso, defendia prioritariamente congelamento de...".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A heterodoxia enfatizava a inflação inercial e, por isso, defendia congelamento de preços e desindexação; já o...". De acordo com a teoria estudada em *4. Estratégia Brasileira de Inteligência Artificial (EBIA)*, a Estratégia Brasileira de Inteligência Artificial (EBIA) foi formalmente instituída pelo Governo Federal por meio da Portaria MCTI nº 4.617, de 6 de abril de 2021, com o propósito de articular investimentos públicos e privados, promover a pesquisa e capacitação, e assegurar o uso ético da tecnologia.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O Plano Cruzado, embora heterodoxo, distinguiu-se por ter sido precedido de forte ajuste fiscal e monetário, o que...". De acordo com a teoria estudada em *2.2 Método SHAP (SHapley Additive exPlanations) e seus Axiomas*, aplicações Visuais: O SHAP permite gerar gráficos de força locais (*Force Plots* e *Waterfall Plots*) demonstrando como cada parâmetro fiscal empurrou a probabilidade de fraude para cima ou para baixo em relação à média, bem como visões globais de importância (*Summary Plots / Beeswarm*).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O Plano Verão afastou-se tanto da ortodoxia quanto da heterodoxia, pois rejeitou simultaneamente o congelamento de...". De acordo com a teoria estudada em *4.3 Os Seis Eixos Verticais (Temáticos)*, segurança Pública: Emprego legítimo de modelos preditivos e visão computacional na elucidação de crimes complexos, perícia forense digital, vigilância de fronteiras e proteção de infraestruturas cibernéticas críticas, sob estrita conformidade legal e supervisão judicial.
> - **E)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "Todos os planos de estabilização dos anos 1980 partiram exclusivamente do diagnóstico ortodoxo de que a inflação...". De acordo com a teoria estudada em *1. Princípios de IA Responsável, Ética e Governança Humana*, à medida que sistemas de inteligência artificial são integrados a decisões de auditoria fiscal, concessão de benefícios previdenciários e detecção de irregularidades pelo Tribunal de Contas, impõe-se a observância de postulados éticos e diretrizes normativas internacionais para mitigar riscos a direitos fundamentais.
>
> **Gabarito: A**

---

### Teste 354
**(FCC – TRT 13ª – 2014 – Analista Judiciário - Tecnologia da Informação)**
O recurso de VPN − Virtual Private Network é utilizado para a transmissão de informações de forma segura em redes de computadores. Caso se faça uma análise do pacote transmitido utilizando uma VPN,

* **A)** apenas os dados e o cabeçalho são encriptados.
* **B)** ambos os endereços IPs, destino e origem, são encriptados.
* **C)** apenas o endereço IP destino é encriptado para evitar a modificação.
* **D)** apenas o endereço IP origem é encriptado para evitar o rastreamento.
* **E)** o pacote, que inclui os endereços, o cabeçalho e os dados, é encriptado por completo.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *4.3 Os Seis Eixos Verticais (Temáticos)* deste guia, educação e Capacitação: Formação de base em raciocínio computacional no ensino básico, expansão de cursos de pós-graduação em Ciência de Dados e difusão do letramento digital em IA para a sociedade. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 13ª/2014) ao estabelecer que "apenas os dados e o cabeçalho são encriptados".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "ambos os endereços IPs, destino e origem, são encriptados". De acordo com a teoria estudada em *1.1 Diretrizes Internacionais (OCDE e UNESCO)*, robustez, Segurança e Proteção (*Robustness and Safety*): Garantia de resiliência algorítmica contra falhas, ataques adversariais (*adversarial attacks*) e vazamentos de dados, operando de modo previsível ao longo de todo o ciclo de vida.
> - **C)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "apenas o endereço IP destino é encriptado para evitar a modificação". De acordo com a teoria estudada em *1.2 Vieses Algorítmicos e Métricas de Equidade (Fairness)*, algoritmos não operam no vácuo ético; eles extraem padrões matemáticos diretamente de dados históricos empíricos.
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "apenas o endereço IP origem é encriptado para evitar o rastreamento". De acordo com a teoria estudada em *1.2 Vieses Algorítmicos e Métricas de Equidade (Fairness)*, se os dados passados espelharem disparidades ou exclusões sociais, a rede neural aprenderá a perpetuar e multiplicar esses vieses (*bias in, bias out*).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "o pacote, que inclui os endereços, o cabeçalho e os dados, é encriptado por completo". De acordo com a teoria estudada em *1.2 Vieses Algorítmicos e Métricas de Equidade (Fairness)*, atenção à falácia da "Equidade por Desconhecimento" (*Fairness through Unawareness*): a banca FCC frequentemente afirma que "para garantir que um algoritmo não discrimine, basta remover as colunas de dados sensíveis como raça ou gênero".
>
> **Gabarito: A**

---

## 🌐 Fontes Oficiais e Referências Bibliográficas

* [Lei Federal nº 13.709/2018 - LGPD (Planalto)](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm) - Princípios da finalidade, adequação, necessidade, não discriminação e revisão de decisões automatizadas (Art. 20).
* [Lei Complementar Estadual de Goiás nº 205/2025 - Política de IA (Casa Civil/GO)](https://legisla.casacivil.go.gov.br/pesquisa_legislacao/110694/lei-complementar-205) - Política Estadual de Fomento à Inovação em Inteligência Artificial no Estado de Goiás.
* [Governo Digital - Inteligência Artificial no Setor Público Federal](https://www.gov.br/governodigital/pt-br/infraestrutura-nacional-de-dados/inteligencia-artificial-1) - Diretrizes governamentais para uso responsável e inovação em IA na administração pública.
* [NIST AI Risk Management Framework (AI RMF 1.0)](https://www.nist.gov/itl/ai-risk-management-framework) - Princípios de explicabilidade, governança de dados, mitigação de viés e transparência algorítmica.
* [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) - Segurança e proteção contra envenenamento de dados e vulnerabilidades críticas em modelos de IA.
* O'NEIL, Cathy. **Algoritmos de Destruição em Massa: Como o Big Data Aumenta a Desigualdade e Ameaça a Democracia**. Santo André: Editora Rua do Sabão, 2020. (Cap. 1 a 3 - Modelos Ocultos e Discriminação Estatística).
* BIONI, Bruno Ricardo. **Proteção de Dados Pessoais: A Função e os Limites do Consentimento**. 2. ed. Rio de Janeiro: Forense, 2021. (Cap. 4 - O Impacto das Decisões Automatizadas e os Direitos dos Titulares).
* RUSSELL, Stuart; NORVIG, Peter. **Inteligência Artificial: Uma Abordagem Moderna**. 4. ed. Rio de Janeiro: GEN LTC, 2022. (Cap. 27 - Ética, Segurança e Futuro da IA).
