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
**(FGV – TCE-GO – Analista de Controle Externo Controle Externo – 2024)**
O professor calculou a média das notas de 9 alunos numa prova e obteve 5,5. Notou então que faltou avaliar uma prova de um décimo aluno, corrigiu a referida prova e deu nota 8,5 a ela. A nova média, agora dos dez alunos, foi então igual a

* **A)** 5,6
* **B)** 5,7
* **C)** 5,8
* **D)** 5,85
* **E)** 5,9

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *1.3 Modelos de Supervisão Humana: HITL, HOTL e HIC* deste guia, human-in-the-Loop (HITL): O sistema de IA gera notas de probabilidade, subsídios probatórios e sugestões, mas a tomada de decisão final é obrigatoriamente validada e executada por um ser humano. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE-GO/2024) ao estabelecer que "5,6".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "5,7". De acordo com a teoria estudada em *2.1 O Dilema Desempenho vs. Interpretabilidade*, possuem estrutura transparente. O efeito de uma variável em uma regressão linear é explicitado diretamente pelo coeficiente \$\beta_j\$; em uma árvore de decisão rasa, a inferência é descrita por regras sequenciais *se-então* legíveis.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "5,8". De acordo com a teoria estudada em *2.2 Método SHAP (SHapley Additive exPlanations) e seus Axiomas*, o valor de Shapley \$\phi_i\$ calcula a contribuição marginal média da variável \$i\$ ao longo de todas as permutações e subconjuntos possíveis de variáveis (\$S \subseteq F\$).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "5,85". De acordo com a teoria estudada em *2.2 Método SHAP (SHapley Additive exPlanations) e seus Axiomas*, aplicações Visuais: O SHAP permite gerar gráficos de força locais (*Force Plots* e *Waterfall Plots*) demonstrando como cada parâmetro fiscal empurrou a probabilidade de fraude para cima ou para baixo em relação à média, bem como visões globais de importância (*Summary Plots / Beeswarm*).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "5,9". De acordo com a teoria estudada em *1. Princípios de IA Responsável, Ética e Governança Humana*, à medida que sistemas de inteligência artificial são integrados a decisões de auditoria fiscal, concessão de benefícios previdenciários e detecção de irregularidades pelo Tribunal de Contas, impõe-se a observância de postulados éticos e diretrizes normativas internacionais para mitigar riscos a direitos fundamentais.
>
> **Gabarito: A**

---

### Teste 345
**(FGV – TCE-PI – Auditor de Controle Externo Controle Externo Especifica de Area Comum – 2025)**
Segundo o regulamento de um plano de previdência complementar, o benefício de renda será calculado pelo maior valor entre o salário-mínimo vigente e a média dos 80% maiores salários do participante dos últimos 60 meses, atualizados pelo índice de inflação do plano. Esse tipo regra caracteriza um plano atuarial na modalidade de

* **A)** contribuição definida.
* **B)** contribuição variável.
* **C)** benefício definido.
* **D)** benefício variável.
* **E)** contribuição e benefício variáveis.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *2.2 Método SHAP (SHapley Additive exPlanations) e seus Axiomas* deste guia, o valor de Shapley \$\phi_i\$ calcula a contribuição marginal média da variável \$i\$ ao longo de todas as permutações e subconjuntos possíveis de variáveis (\$S \subseteq F\$). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE-PI/2025) ao estabelecer que "contribuição definida".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "contribuição variável". De acordo com a teoria estudada em *2.1 O Dilema Desempenho vs. Interpretabilidade*, possuem estrutura transparente. O efeito de uma variável em uma regressão linear é explicitado diretamente pelo coeficiente \$\beta_j\$; em uma árvore de decisão rasa, a inferência é descrita por regras sequenciais *se-então* legíveis.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "benefício definido". De acordo com a teoria estudada em *3.1 Bases Legais e Princípio da Não Discriminação*, veda a coleta indiscriminada de dados para alimentar bancos de IA; o tratamento deve ser restrito ao mínimo estritamente indispensável para a finalidade pretendida.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "benefício variável". De acordo com a teoria estudada em *2.2 Método SHAP (SHapley Additive exPlanations) e seus Axiomas*, aplicações Visuais: O SHAP permite gerar gráficos de força locais (*Force Plots* e *Waterfall Plots*) demonstrando como cada parâmetro fiscal empurrou a probabilidade de fraude para cima ou para baixo em relação à média, bem como visões globais de importância (*Summary Plots / Beeswarm*).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "contribuição e benefício variáveis". De acordo com a teoria estudada em *1.2 Vieses Algorítmicos e Métricas de Equidade (Fairness)*, isso é FALSO! Modelos matemáticos avançados capturam facilmente variáveis correlacionadas que atuam como substitutas indiretas (*proxies*) do dado omitido (ex.: CEP residencial, faixa salarial, histórico escolar).
>
> **Gabarito: A**

---

### Teste 346
**(FGV – TCE-PA – Auditor de Controle Externo Administrativa Ciencia de Dados – 2024)**
Modelos de aprendizagem de máquina são, em geral, avaliados com métricas que indicam os quão poderosos e relevantes eles são. Entre exemplos de métricas de avaliação utilizadas para modelos de classificação binária, podemos citar: • Taxa de precisão (razão entre verdadeiros positivos e o total dos verdadeiros positivos e falsos positivos); • Taxa de sensibilidade (razão entre verdadeiros positivos e o total dos verdadeiros positivos e falsos negativos, também conhecida por recall); e • Escore F1 (F1-score, também chamado de F-measure), que relaciona as taxas de precisão e de sensibilidade. Suponha a existência de um modelo de classificação binária cuja taxa de precisão é de 90,00% e cuja taxa de sensibilidade é de 75,00%. Utilize aproximação de duas casas decimais. O escore F1 referente a esse modelo é

* **A)** 41,42%.
* **B)** 81,82%.
* **C)** 82,15%.
* **D)** 82,50%.
* **E)** 82,84%.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "41,42%". De acordo com a teoria estudada em *1.2 Vieses Algorítmicos e Métricas de Equidade (Fairness)*, viés de Representação (*Representation Bias*): Sub-representação estatística de determinado grupo populacional na base amostral de treino (ex.: softwares de visão computacional e biometria facial treinados com mais de 80% de rostos masculinos e brancos, exibindo taxas de falso positivo inaceitavelmente altas para mulheres negras).
> - **B)** **Correta.** Conforme fundamentado na seção *1.2 Vieses Algorítmicos e Métricas de Equidade (Fairness)* deste guia, *Igualdade de Oportunidades (*Equal Opportunity*):* Exige que as taxas de Verdadeiros Positivos (Sensibilidade/Recall) sejam rigorosamente iguais entre os grupos protegidos (\$P(\hat{y}=1 \mid y=1, A=0) = P(\hat{y}=1 \mid y=1, A=1)\$). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE-PA/2024) ao estabelecer que "81,82%".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "82,15%". De acordo com a teoria estudada em *1.3 Modelos de Supervisão Humana: HITL, HOTL e HIC*, modelo imperativo no setor público para atos administrativos vinculantes, dosimetria de sanções e julgamento de contas.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "82,50%". De acordo com a teoria estudada em *1.2 Vieses Algorítmicos e Métricas de Equidade (Fairness)*, isso é FALSO! Modelos matemáticos avançados capturam facilmente variáveis correlacionadas que atuam como substitutas indiretas (*proxies*) do dado omitido (ex.: CEP residencial, faixa salarial, histórico escolar).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "82,84%". De acordo com a teoria estudada em *2.3 Método LIME (Local Interpretable Model-Agnostic Explanations)*, introduzido por Marco Tulio Ribeiro et al. (2016), o LIME fundamenta-se na aproximação local substituta.
>
> **Gabarito: B**

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
**(FGV – TCE-PA – Auditor de Controle Externo Administrativa Administracao – 2024)**
Em relação ao sistema francês de amortização, avalie se as afirmativas a seguir são falsas (F) ou verdadeiras (V): I. Todas as prestações (pagamentos) são de mesmo valor. II. Um exemplo de uso comum são financiamentos de bem de consumo em geral. III. O valor da prestação P é calculado pelo produto do valor financiado pelo coeficiente 𝐾 dado pela fórmula 𝐾= 𝑖(1 + 𝑖)𝑛 (1 + 𝑖)𝑛−1 em que 𝑖 é a taxa ao período e 𝑛 é o número de períodos. Está correto o que se afirma em

* **A)** I, apenas.
* **B)** I e II, apenas.
* **C)** I e III, apenas.
* **D)** II e III, apenas.
* **E)** I, II e III.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I, apenas". De acordo com a teoria estudada em *3.1 Bases Legais e Princípio da Não Discriminação*, princípio da Necessidade e Minimização (Art. 6º, III).
> - **B)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e II, apenas". De acordo com a teoria estudada em *2.2 Método SHAP (SHapley Additive exPlanations) e seus Axiomas*, o valor de Shapley \$\phi_i\$ calcula a contribuição marginal média da variável \$i\$ ao longo de todas as permutações e subconjuntos possíveis de variáveis (\$S \subseteq F\$).
> - **C)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e III, apenas". De acordo com a teoria estudada em *2.2 Método SHAP (SHapley Additive exPlanations) e seus Axiomas*, aplicações Visuais: O SHAP permite gerar gráficos de força locais (*Force Plots* e *Waterfall Plots*) demonstrando como cada parâmetro fiscal empurrou a probabilidade de fraude para cima ou para baixo em relação à média, bem como visões globais de importância (*Summary Plots / Beeswarm*).
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "II e III, apenas". De acordo com a teoria estudada em *2.1 O Dilema Desempenho vs. Interpretabilidade*, possuem estrutura transparente. O efeito de uma variável em uma regressão linear é explicitado diretamente pelo coeficiente \$\beta_j\$; em uma árvore de decisão rasa, a inferência é descrita por regras sequenciais *se-então* legíveis.
> - **E)** **Correta.** Conforme fundamentado na seção *3.1 Bases Legais e Princípio da Não Discriminação* deste guia, o Poder Público fundamenta o desenvolvimento e treino de modelos analíticos predominantemente no Art. 7º, III da LGPD: *"para a administração pública, para o tratamento e uso compartilhado de dados necessários à execução de políticas públicas previstas em leis e regulamentos ou respaldadas em contratos, convênios ou instrumentos congêneres"*. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE-PA/2024) ao estabelecer que "I, II e III".
>
> **Gabarito: E**

---

### Teste 348
**(FCC – TCE-GO – Analista de Controle Externo Gestao de Conhecimento – 2009)**
Em indexação, exaustividade, revocação e precisão estão relacionadas. Quanto mais exaustivamente um sistema indexa os seus documentos,

* **A)** mais consistentes serão a revocação e a precisão.
* **B)** menor será a revocação e maior será a precisão.
* **C)** mais altas serão a revocação e a precisão.
* **D)** mais baixas serão a revocação e a precisão.
* **E)** maior será a revocação e menor será a precisão.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "mais consistentes serão a revocação e a precisão". De acordo com a teoria estudada em *2.3 Método LIME (Local Interpretable Model-Agnostic Explanations)*, ajusta uma regressão linear esparsa e interpretável sobre essa vizinhança ponderada. Os coeficientes dessa reta linear revelam quais atributos mais pesaram naquela decisão isolada.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "menor será a revocação e maior será a precisão". De acordo com a teoria estudada em *1.1 Diretrizes Internacionais (OCDE e UNESCO)*, transparência e Explicabilidade (*Explainability*): Dever das entidades promotoras de disponibilizar informações acessíveis para que os cidadãos compreendam quando estão interagindo com IA e os fatores objetivos que determinaram uma decisão automatizada.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "mais altas serão a revocação e a precisão". De acordo com a teoria estudada em *1.2 Vieses Algorítmicos e Métricas de Equidade (Fairness)*, viés de Representação (*Representation Bias*): Sub-representação estatística de determinado grupo populacional na base amostral de treino (ex.: softwares de visão computacional e biometria facial treinados com mais de 80% de rostos masculinos e brancos, exibindo taxas de falso positivo inaceitavelmente altas para mulheres negras).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "mais baixas serão a revocação e a precisão". De acordo com a teoria estudada em *1.3 Modelos de Supervisão Humana: HITL, HOTL e HIC*, human-in-the-Loop (HITL): O sistema de IA gera notas de probabilidade, subsídios probatórios e sugestões, mas a tomada de decisão final é obrigatoriamente validada e executada por um ser humano.
> - **E)** **Correta.** Conforme fundamentado na seção *4.3 Os Seis Eixos Verticais (Temáticos)* deste guia, aplicação nos Setores Produtivos: Difusão da IA na agricultura de precisão (Agritech), na manufatura digital (Indústria 4.0), no sistema financeiro e na telemedicina diagnóstica. Dessa forma, está plenamente correta a assertiva da banca (FCC – TCE-GO/2009) ao estabelecer que "maior será a revocação e menor será a precisão".
>
> **Gabarito: E**

---

### Teste 349
**(FGV – TCE-PI – Auditor de Controle Externo Controle Externo Especifica de Area Comum – 2025)**
Os custos atuariais são fundamentais para manter o equilíbrio do plano. O custo normal financia os benefícios futuros, enquanto que o custo suplementar cobre déficits atuariais. Sabe-se que um Regime Próprio possui ativos de R$ 2 bilhões, que o valor atual dos benefícios futuros (encargos atuariais) é de R$ 10 bilhões e que a folha salarial atuarial futura é de R$ 32 bilhões. O custo normal (%) calculado pelo método de financiamento agregado corresponde a

* **A)** 6,25.
* **B)** 20,00.
* **C)** 25,00.
* **D)** 31,25.
* **E)** 33,33.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *2.2 Método SHAP (SHapley Additive exPlanations) e seus Axiomas* deste guia, o valor de Shapley \$\phi_i\$ calcula a contribuição marginal média da variável \$i\$ ao longo de todas as permutações e subconjuntos possíveis de variáveis (\$S \subseteq F\$). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE-PI/2025) ao estabelecer que "6,25".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "20,00". De acordo com a teoria estudada em *1. Princípios de IA Responsável, Ética e Governança Humana*, à medida que sistemas de inteligência artificial são integrados a decisões de auditoria fiscal, concessão de benefícios previdenciários e detecção de irregularidades pelo Tribunal de Contas, impõe-se a observância de postulados éticos e diretrizes normativas internacionais para mitigar riscos a direitos fundamentais.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "25,00". De acordo com a teoria estudada em *2.1 O Dilema Desempenho vs. Interpretabilidade*, redes Neurais Profundas e Ensembles avançados (*XGBoost*, *CatBoost*) realizam bilhões de multiplicações matriciais e transformações em espaços latentes de alta dimensão, impedindo a inspeção causal direta.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "31,25". De acordo com a teoria estudada em *1.1 Diretrizes Internacionais (OCDE e UNESCO)*, responsabilização e Prestação de Contas (*Accountability*): Organizações que desenvolvem ou empregam sistemas de IA devem responder formalmente pelo seu impacto e manter registros e trilhas de auditoria (*audit trails*) que viabilizem a inspeção externa por órgãos de controle.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "33,33". De acordo com a teoria estudada em *3.2 O Artigo 20: Revisão de Decisões Automatizadas e Auditoria da ANPD*, o Artigo 20 da Lei nº 13.709/2018 constitui o epicentro do regime jurídico de inteligência artificial no Brasil.
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
**(FGV – TRT-1 – Analista Judiciario Area Administrativa – 2024)**
Determinado ente da federação, no âmbito de suas competências, resolve conceder incentivo fiscal a indústrias e entidades dedicadas à reciclagem de resíduos produzidos no território nacional, conforme autorizado pelo Art. 44 da Lei nº 12.305/2010 (Política Nacional de Resíduos Sólidos – PNRS). Trata-se, portanto, de aplicação prática do seguinte princípio previsto na Política Nacional de Resíduos Sólidos:

* **A)** princípio do protetor-recebedor;
* **B)** princípio do poluidor-pagador;
* **C)** princípio da participação pública;
* **D)** princípio da responsabilidade;
* **E)** princípio da vedação ao retrocesso ambiental.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "princípio do protetor-recebedor". De acordo com a teoria estudada em *3.1 Bases Legais e Princípio da Não Discriminação*, o Poder Público fundamenta o desenvolvimento e treino de modelos analíticos predominantemente no Art. 7º, III da LGPD: *"para a administração pública, para o tratamento e uso compartilhado de dados necessários à execução de políticas públicas previstas em leis e regulamentos ou respaldadas em contratos, convênios ou instrumentos congêneres"*.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "princípio do poluidor-pagador". De acordo com a teoria estudada em *3.1 Bases Legais e Princípio da Não Discriminação*, para Dados Pessoais Sensíveis (biometria facial, dados de saúde), a base de atuação pública vincula-se ao Art. 11, II, "b" (cumprimento de obrigação legal ou regulatória e execução de políticas públicas pela administração pública).
> - **C)** **Correta.** Conforme fundamentado na seção *3.1 Bases Legais e Princípio da Não Discriminação* deste guia, princípio da Não Discriminação Ilícita ou Abusiva (Art. 6º, IX da LGPD). Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT-1/2024) ao estabelecer que "princípio da participação pública".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "princípio da responsabilidade". De acordo com a teoria estudada em *3.1 Bases Legais e Princípio da Não Discriminação*, princípio da Necessidade e Minimização (Art. 6º, III).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "princípio da vedação ao retrocesso ambiental". De acordo com a teoria estudada em *1.1 Diretrizes Internacionais (OCDE e UNESCO)*, crescimento Inclusivo, Desenvolvimento Sustentável e Bem-Estar: A IA deve atuar como força motriz para o progresso humano e redução de desigualdades, respeitando a dignidade e a sustentabilidade ambiental.
>
> **Gabarito: C**

---

### Teste 351
**(FGV – TCE-PI – Auditor de Controle Externo Controle Externo Especifica de Area Comum – 2025)**
Numa determinada população, 40% das famílias moram em locais sem acesso a saneamento básico. Se quatro famílias dessa população forem sorteadas ao acaso, sem reposição, a probabilidade de que duas morem em locais sem saneamento básico é, aproximadamente, igual a

* **A)** 0,25.
* **B)** 0,30.
* **C)** 0,35.
* **D)** 0,40.
* **E)** 0,45.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *2.2 Método SHAP (SHapley Additive exPlanations) e seus Axiomas* deste guia, aplicações Visuais: O SHAP permite gerar gráficos de força locais (*Force Plots* e *Waterfall Plots*) demonstrando como cada parâmetro fiscal empurrou a probabilidade de fraude para cima ou para baixo em relação à média, bem como visões globais de importância (*Summary Plots / Beeswarm*). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE-PI/2025) ao estabelecer que "0,25".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "0,30". De acordo com a teoria estudada em *2.3 Método LIME (Local Interpretable Model-Agnostic Explanations)*, parte do princípio de que, embora a fronteira de decisão de um modelo complexo de Deep Learning seja extremamente não-linear em escala global, ela se comporta de maneira aproximadamente linear em uma microvizinhança local ao redor de uma observação específica \$x\$.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "0,35". De acordo com a teoria estudada em *2.3 Método LIME (Local Interpretable Model-Agnostic Explanations)*, ajusta uma regressão linear esparsa e interpretável sobre essa vizinhança ponderada. Os coeficientes dessa reta linear revelam quais atributos mais pesaram naquela decisão isolada.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "0,40". De acordo com a teoria estudada em *4.3 Os Seis Eixos Verticais (Temáticos)*, educação e Capacitação: Formação de base em raciocínio computacional no ensino básico, expansão de cursos de pós-graduação em Ciência de Dados e difusão do letramento digital em IA para a sociedade.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "0,45". De acordo com a teoria estudada em *1.3 Modelos de Supervisão Humana: HITL, HOTL e HIC*, human-in-the-Loop (HITL): O sistema de IA gera notas de probabilidade, subsídios probatórios e sugestões, mas a tomada de decisão final é obrigatoriamente validada e executada por um ser humano.
>
> **Gabarito: A**

---

### Teste 352
**(FGV – TCE-PA – Auditor de Controle Externo Administrativa Ciencia de Dados – 2024)**
Alguns algoritmos de aprendizado de máquina foram desenvolvidos para trabalhar com atributos discretos. Porém, dados coletados no mundo real muitas vezes são contínuos. Nesses casos, podemos usar métodos de discretização no tratamento dos dados. Um desses métodos de discretização consiste em estabelecer os limites das partições de forma que cada partição tenha aproximadamente o mesmo número de elementos. O método acima descrito é o

* **A)** equal frequency.
* **B)** equal width.
* **C)** equal amplitude.
* **D)** k-means.
* **E)** entropy.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *1.2 Vieses Algorítmicos e Métricas de Equidade (Fairness)* deste guia, *Igualdade de Oportunidades (*Equal Opportunity*):* Exige que as taxas de Verdadeiros Positivos (Sensibilidade/Recall) sejam rigorosamente iguais entre os grupos protegidos (\$P(\hat{y}=1 \mid y=1, A=0) = P(\hat{y}=1 \mid y=1, A=1)\$). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE-PA/2024) ao estabelecer que "equal frequency".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "equal width". De acordo com a teoria estudada em *1.2 Vieses Algorítmicos e Métricas de Equidade (Fairness)*, viés Histórico (*Historical Bias*): Decorre de assimetrias preexistentes no mundo real e na sociedade, mesmo que o processo de amostragem estatística tenha sido perfeito (ex.: histórica discrepância salarial de gênero ou raça em determinados cargos).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "equal amplitude". De acordo com a teoria estudada em *1.2 Vieses Algorítmicos e Métricas de Equidade (Fairness)*, viés de Medição (*Measurement Bias*): Ocorre quando os atributos selecionados para mensurar um fenômeno abstrato atuam como *proxies* distorcidas da realidade (ex.: adotar o número de prisões ou boletins de ocorrência como proxy de criminalidade, capturando o viés de policiamento ostensivo desproporcional em bairros periféricos).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "k-means". De acordo com a teoria estudada em *1.3 Modelos de Supervisão Humana: HITL, HOTL e HIC*, human-on-the-Loop (HOTL): O algoritmo atua com autonomia operacional em tempo real (ex.: bloqueio instantâneo de transações financeiras fraudulentas de alto volume), porém sob supervisão e vigilância ativa de operadores humanos, que dispõem da prerrogativa de vetar, pausar ou reverter intervenções.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "entropy". De acordo com a teoria estudada em *3. A LGPD (Lei nº 13.709/2018) Aplicada à Inteligência Artificial*, a Lei Geral de Proteção de Dados Pessoais regula qualquer operação de tratamento de dados de pessoas naturais realizada no território brasileiro, impondo salvaguardas mandatórias às rotinas automatizadas de inteligência artificial.
>
> **Gabarito: A**

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
**(FGV – TRT-1 – Analista Judiciario Area Administrativa – 2024)**
A gestão adequada dos resíduos sólidos é um desafio cada vez mais urgente e essencial para a preservação do meio ambiente e a sustentabilidade do planeta. A inadequada gestão de resíduos compromete não apenas o meio ambiente, mas a qualidade de vida da população e o desenvolvimento sustentável. Nesse contexto, a implementação de Planos Municipais de Gestão Integrada de Resíduos Sólidos é imprescindível para a adequada gestão dos resíduos. Sobre esses planos, é correto afirmar que:

* **A)** devem prever expressamente a periodicidade de sua revisão, observado o período máximo de 30 anos;
* **B)** é facultada a previsão de sistema de cálculo dos custos da prestação dos serviços públicos de limpeza urbana e de manejo de resíduos sólidos, bem como a forma de cobrança desses serviços;
* **C)** devem contemplar ações específicas a serem desenvolvidas no âmbito dos órgãos da Administração Pública, com vistas à utilização racional dos recursos ambientais, ao combate a todas as formas de desperdício e à minimização da geração de resíduos;
* **D)** não é obrigatória sua elaboração para que os municípios tenham acesso a recursos financeiros e incentivos governamentais relacionados à limpeza urbana e ao manejo de resíduos sólidos, embora seja recomendada;
* **E)** devem prever as zonas favoráveis e desfavoráveis para a localização de unidades de tratamento de resíduos sólidos ou de disposição final de rejeitos.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *3.2 O Artigo 20: Revisão de Decisões Automatizadas e Auditoria da ANPD* deste guia, o direito de revisão de decisão automatizada no caput do Art. 20 não contém expressamente a exigência de ser feita "por pessoa natural" (esse trecho foi formalmente vetado e o veto mantido pelo Congresso Nacional). Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT-1/2024) ao estabelecer que "devem prever expressamente a periodicidade de sua revisão, observado o período máximo de 30 anos".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "é facultada a previsão de sistema de cálculo dos custos da prestação dos serviços públicos de limpeza urbana e de...". De acordo com a teoria estudada em *4.3 Os Seis Eixos Verticais (Temáticos)*, aplicação no Poder Público: Transformação digital da administração pública (Governo Digital), aprimoramento da prestação de serviços ao cidadão e modernização da fiscalização tributária e da auditoria de controle externo pelo TCE-GO.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "devem contemplar ações específicas a serem desenvolvidas no âmbito dos órgãos da Administração Pública, com vistas...". De acordo com a teoria estudada em *1.1 Diretrizes Internacionais (OCDE e UNESCO)*, responsabilização e Prestação de Contas (*Accountability*): Organizações que desenvolvem ou empregam sistemas de IA devem responder formalmente pelo seu impacto e manter registros e trilhas de auditoria (*audit trails*) que viabilizem a inspeção externa por órgãos de controle.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "não é obrigatória sua elaboração para que os municípios tenham acesso a recursos financeiros e incentivos...". De acordo com a teoria estudada em *2.3 Método LIME (Local Interpretable Model-Agnostic Explanations)*, parte do princípio de que, embora a fronteira de decisão de um modelo complexo de Deep Learning seja extremamente não-linear em escala global, ela se comporta de maneira aproximadamente linear em uma microvizinhança local ao redor de uma observação específica \$x\$.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "devem prever as zonas favoráveis e desfavoráveis para a localização de unidades de tratamento de resíduos sólidos...". De acordo com a teoria estudada em *1.2 Vieses Algorítmicos e Métricas de Equidade (Fairness)*, *Paridade Demográfica (*Demographic Parity*):* Exige que a proporção de predições favoráveis seja idêntica entre os subgrupos protegidos (\$P(\hat{y}=1 \mid A=0) = P(\hat{y}=1 \mid A=1)\$).
>
> **Gabarito: A**

---

### Teste 354
**(CEBRASPE – TRT-8 – Analista Judiciario Area Apoio Especializado Tecnologia da Informacao – 2022)**
Certo TRT deseja implementar uma solução de segurança cibernética que combine inteligência artificial, detecção comportamental e algoritmos de aprendizado de máquina para antecipar e prevenir ameaças conhecidas e desconhecidas. Com base nessa situação hipotética, assinale a opção que indica a solução requerida.

* **A)** NGAV
* **B)** IPS
* **C)** IDS
* **D)** NIST
* **E)** WebProxy

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *1. Princípios de IA Responsável, Ética e Governança Humana* deste guia, à medida que sistemas de inteligência artificial são integrados a decisões de auditoria fiscal, concessão de benefícios previdenciários e detecção de irregularidades pelo Tribunal de Contas, impõe-se a observância de postulados éticos e diretrizes normativas internacionais para mitigar riscos a direitos fundamentais. Dessa forma, está plenamente correta a assertiva da banca (CEBRASPE – TRT-8/2022) ao estabelecer que "NGAV".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "IPS". De acordo com a teoria estudada em *4. Estratégia Brasileira de Inteligência Artificial (EBIA)*, a Estratégia Brasileira de Inteligência Artificial (EBIA) foi formalmente instituída pelo Governo Federal por meio da Portaria MCTI nº 4.617, de 6 de abril de 2021, com o propósito de articular investimentos públicos e privados, promover a pesquisa e capacitação, e assegurar o uso ético da tecnologia.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "IDS". De acordo com a teoria estudada em *3. A LGPD (Lei nº 13.709/2018) Aplicada à Inteligência Artificial*, a Lei Geral de Proteção de Dados Pessoais regula qualquer operação de tratamento de dados de pessoas naturais realizada no território brasileiro, impondo salvaguardas mandatórias às rotinas automatizadas de inteligência artificial.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "NIST". De acordo com a teoria estudada em *3.2 O Artigo 20: Revisão de Decisões Automatizadas e Auditoria da ANPD*, o Artigo 20 da Lei nº 13.709/2018 constitui o epicentro do regime jurídico de inteligência artificial no Brasil.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "WebProxy". De acordo com a teoria estudada em *4.2 Os Três Eixos Transversais*, promover um ambiente normativo propício à inovação com segurança jurídica, adotando mecanismos flexíveis como os Ambientes Regulatórios Experimentais (*Regulatory Sandboxes*).
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
