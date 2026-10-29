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
**(FGV - TRT / Analista Judiciário - Governança de TI - Diretrizes Internacionais de Ética em IA: OCDE e UNESCO)**
A governança ética da Inteligência Artificial consolidou-se internacionalmente a partir da Recomendação sobre Inteligência Artificial da OCDE (2019) e da Recomendação sobre a Ética da Inteligência Artificial da UNESCO (2021).

A respeito dos princípios reitores estabelecidos pela OCDE para sistemas de IA confiáveis (*Trustworthy AI*), assinale a afirmativa correta:

* **A)** A OCDE recomenda que o desenvolvimento de sistemas de IA seja mantido em sigilo governamental, dispensando transparência e rastreabilidade para acelerar a inovação considerando os requisitos operacionais de segurança, escalabilidade, auditoria e desempenho corporativo considerando os requisitos operacionais de segurança, escalabilidade, auditoria e desempenho corporativo.
* **B)** Os princípios da OCDE determinam que os sistemas de IA devem: (1) impulsionar o crescimento inclusivo, desenvolvimento sustentável e bem-estar; (2) respeitar os direitos humanos, Estado de Direito e equidade; (3) operar com transparência e explicabilidade responsável; (4) garantir robustez técnica, segurança contínua e proteção; e (5) contar com responsabilização e prestação de contas (*accountability*) dos atores de IA.
* **C)** A OCDE estabelece a proibição global de qualquer aplicação de IA no setor público e no poder judiciário.
* **D)** A Recomendação da UNESCO preconiza que modelos de linguagem devem substituir juízes e conselheiros de tribunais em decisões colegiadas vinculantes.
* **E)** O princípio da robustez da OCDE autoriza que modelos de IA ignorem vulnerabilidades cibernéticas se a taxa de acurácia for superior a 80%.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Transparência e explicabilidade responsável (*transparency and explainability*) são princípios obrigatórios expressos pela OCDE.
> - **B)** **CORRETA.** Os **Cinco Princípios da OCDE para IA Responsável** (subscritos pelo Brasil e base da EBIA):
>   1. **Crescimento Inclusivo, Desenvolvimento Sustentável e Bem-Estar:** Beneficiar as pessoas e o planeta.
>   2. **Valores Centrados no Ser Humano e Equidade:** Respeito à dignidade humana, autonomia, privacidade, diversidade e vedação à discriminação injusta.
>   3. **Transparência e Explicabilidade:** Fornecer informações claras para permitir que os indivíduos compreendam os resultados e possam contestá-los.
>   4. **Robustez, Segurança e Proteção:** Operar de modo seguro sob condições normais e sob ataques adversariais (*robustness and cybersecurity*).
>   5. **Responsabilização (Accountability):** Os desenvolvedores e operadores de IA devem prestar contas pelo correto funcionamento e conformidade ética de seus sistemas.
> - **C)** Incorreta. A OCDE incentiva ativamente o uso ético e eficiente da IA para aprimoramento dos serviços públicos.
> - **D)** Incorreta. As normas internacionais vedam a substituição cega da prerrogativa de julgamento humano em decisões que impactem direitos fundamentais.
> - **E)** Incorreta. A robustez exige resiliência sistemática a falhas e ataques, sem flexibilização de riscos.
> 
> **Gabarito: B**

---

### Teste 345
**(FGV - TRT / Analista Judiciário - TI - Métricas de Equidade e Impacto Desproporcional em IA)**
Sistemas automatizados de triagem e classificação baseados em Machine Learning podem perpetuar ou amplificar discriminações históricas presentes nas bases de treinamento. Para detectar e quantificar esses vieses, a área de *Fairness in AI* (Equidade em IA) emprega testes formais de paridade estatística.

No contexto de avaliação de preconceito algorítmico, o critério do **Impacto Desproporcional** (*Disparate Impact / Regra dos Quatro Quintos ou dos 80%*) é definido formalmente quando:

* **A)** A taxa de seleção positiva do grupo historicamente desfavorecido ou protegido é menor do que 80% (quatro quintos) da taxa de seleção do grupo com maior privilégio no processo seletivo ou concessão de benefício.
* **B)** Exatamente 80% das linhas do banco de dados contêm valores nulos na coluna demográfica.
* **C)** O modelo atinge acurácia global de 80% em testes sintéticos em laboratório.
* **D)** O sistema de IA descarta 80% de todas as candidaturas sem qualquer leitura de atributos.
* **E)** O modelo é aprovado sem vieses se o número de conexões na rede neural for múltiplo de 80 considerando os requisitos operacionais de segurança, escalabilidade, auditoria e desempenho corporativo em conformidade com as diretrizes e padrões de arquitetura corporativa.


---

> **Comentário Detalhado:**
>
> - **A)** **CORRETA.** O conceito de **Disparate Impact (Impacto Desproporcional)**:
>   - Originou-se na jurisprudência trabalhista americana (*Uniform Guidelines on Employee Selection Procedures*) e foi adotado como padrão matemático em auditoria algorítmica:
>   $$\text{Disparate Impact Ratio} = \frac{P(\hat{Y}=1 | D=\text{desfavorecido})}{P(\hat{Y}=1 | D=\text{favorecido})}$$
>   - **Regra dos 4/5 (80%):** Se a razão for inferior a $0,80$, há forte indício de viés discriminatório adverso (*adverse impact*), mesmo que o algoritmo não utilize variáveis protegidas diretamente (como raça ou gênero), demonstrando discriminação indireta por variáveis substitutas (*proxy variables*, como CEP ou histórico de crédito).
> - **B)** Incorreta. Refere-se à esparsidade de valores ausentes, não a viés demográfico.
> - **C)** Incorreta. Acurácia geral não garante justiça algorítmica (pode haver alta acurácia com forte discriminação contra minorias em dados desbalanceados).
> - **D)** Incorreta. Falsa interpretação do percentual de 80%.
> - **E)** Incorreta. Não tem qualquer relação com pesos ou neurônios da rede.
> 
> **Gabarito: A**

---

### Teste 346
**(FCC - TRT-15ª Região - Analista Judiciário - Tecnologia da Informação)**
Ao implantar um sistema inteligente de triagem automática de processos trabalhistas e recursos judiciais, o Tribunal estabeleceu diretrizes éticas para impedir vieses algorítmicos e assegurar a adequada governança institucional sobre as decisões automatizadas.
A respeito dos conceitos de equidade (*fairness*) e dos modelos de supervisão humana em sistemas de inteligência artificial, assinale a afirmativa correta:

* **A)** O modelo *Human-in-the-Loop* (HITL) caracteriza-se pela completa ausência de supervisores humanos na esteira operacional, permitindo que a IA tome decisões definitivas de maneira 100% autônoma e irrecorrível.
* **B)** O viés de representação (*representation bias*) ocorre quando determinadas classes ou grupos sociais estão insuficientemente representados ou ausentes da base amostral de treinamento do modelo, o que pode provocar degradação de desempenho e maior taxa de erros contra esses grupos.
* **C)** O princípio da Não Discriminação é plenamente atendido pela simples eliminação formal do atributo "gênero" ou "raça" da tabela, sendo impossível que outras variáveis presentes (como CEP ou ocupação) funcionem como variáveis substitutas (*proxies*) indiretas no âmbito da administração pública direta e indireta.
* **D)** O modelo *Human-on-the-Loop* (HOTL) exige que o magistrado humano execute manualmente todos os cálculos matriciais de tensores antes de autorizar o processamento do algoritmo.
* **E)** A equidade algorítmica é um conceito puramente comercial sem relevância para os órgãos públicos do Poder Judiciário e Tribunais de Contas.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O modelo **Human-in-the-Loop (HITL)** exige compulsoriamente a validação e intervenção de um **operador humano na decisão final**.
> - **B)** **Correta.** O **Viés de Representação (*Representation Bias*)** surge quando certos estratos ou grupos sociais são sub-representados na base amostral de treinamento. O modelo não aprende os padrões particulares desse subgrupo, gerando taxas de erro e classificações incorretas sensivelmente maiores contra essas minorias.
> - **C)** Incorreta. A falácia da "Equidade por Desconhecimento" comprova que simplesmente remover uma coluna não impede o viés, visto que modelos capturam facilmente variáveis correlacionadas que atuam como **proxies indiretos** (ex.: CEP residencial, faixa de renda, histórico profissional).
> - **D)** Incorreta. O modelo *Human-on-the-Loop (HOTL)* consiste na supervisão contínua em tempo real com poder de intervir ou acionar botões de emergência (*kill switch*), sem demandar cálculos manuais.
> - **E)** Incorreta. A equidade algorítmica é princípio cardeal no setor público, decorrente das garantias republicanas e constitucionais de isonomia e não discriminação.
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
**(FGV - TRT / Analista Judiciário - TI - O Dilema Acurácia vs. Interpretabilidade em XAI)**
Em projetos de Inteligência Artificial aplicada ao setor público, gestores e cientistas de dados confrontam com frequência o chamado **Dilema entre Desempenho Preditivo e Interpretabilidade** (*Performance vs. Interpretability Trade-off*).

A respeito da classificação dos modelos segundo esse paradigma, assinale a afirmativa correta:

* **A)** Redes neurais convolucionais profundas e modelos *Ensemble* baseados em *Gradient Boosting* (como XGBoost) são modelos intrinsecamente interpretáveis por natureza (*White-Box*), permitindo inspecionar cada decisão por meio de simples fórmulas aritméticas de uma única linha.
* **B)** Modelos como Regressão Linear, Regressão Logística e Árvores de Decisão de baixa profundidade possuem alta interpretabilidade intrínseca (*Simulated Transparency*).
* **C)** A explicabilidade de um modelo é irrelevante em auditorias governamentais e processos judiciais eletrônicos, visto que a legislação brasileira proíbe qualquer questionamento sobre decisões automatizadas por software.
* **D)** Aumentar o número de camadas ocultas e parâmetros de uma rede neural profunda melhora automaticamente sua transparência e facilidade de auditoria.
* **E)** Todos os algoritmos de Machine Learning possuem exatamente o mesmo nível de opacidade matemática.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Redes profundas e modelos como XGBoost/Random Forest são modelos **Caixa-Preta (Black-Box)**, formados por milhões de pesos ou centenas de árvores combinadas, sendo humanamente impossível rastrear o cálculo direto de cada decisão sem ferramentas de explicabilidade *post-hoc* (como SHAP ou LIME).
> - **B)** **CORRETA.** O espectro clássico de **XAI (Explainable AI)**:
>   - **Modelos Interpretáveis Intrínsecos (White-Box):** Regressões lineares/logísticas, árvores de decisão rasas, modelos baseados em regras (*decision lists*). Oferecem transparência direta, permitindo entender exatamente qual peso ou condição determinou a saída.
>   - **Modelos Caixa-Preta (Black-Box):** Redes Neurais Profundas, Transformers, Random Forest, XGBoost. Extraordinário desempenho em dados não estruturados e relações complexas, mas com alta opacidade funcional.
> - **C)** Incorreta. No setor público, o princípio da publicidade, a motivação dos atos administrativos e a LGPD (art. 20) **exigem compulsoriamente a explicabilidade** e justificativa das decisões automatizadas.
> - **D)** Incorreta. Quanto mais parâmetros e camadas, maior a opacidade e o custo de auditoria.
> - **E)** Incorreta. Há uma variação drástica entre algoritmos transparentes e modelos caixa-preta.
> 
> **Gabarito: B**

---

### Teste 348
**(FCC - TCE-RS - Auditor Público Externo - Tecnologia da Informação)**
Em auditorias de controle externo com uso intensivo de modelos de aprendizado de máquina supervisionados para detecção de conluio em licitações públicas, a explicabilidade técnica dos algoritmos é pré-requisito indispensável para a sustentação jurídica dos relatórios periciais. Dois dos métodos agósticos de explicação mais consolidados na literatura são o SHAP (*SHapley Additive exPlanations*) e o LIME (*Local Interpretable Model-agnostic Explanations*).
A respeito dos fundamentos matemáticos e características do SHAP e do LIME, assinale a afirmativa correta:

* **A)** O SHAP baseia-se na Teoria dos Jogos Cooperativos formulada por Lloyd Shapley, garantindo propriedades axiomáticas de consistência, simetria e aditividade local ao mensurar a contribuição marginal de cada variável para a predição.
* **B)** O LIME é um método estritamente global que só é capaz de explicar o comportamento de modelos lineares de regressão, sendo incapaz de processar redes neurais ou árvores de decisão.
* **C)** O SHAP descarta as permutações de coalizões de atributos e atribui pesos aleatórios aos dados com base em uma função de densidade de Poisson uniforme.
* **D)** O método LIME calcula o valor exato de todas as coalizões de atributos em nível populacional global com garantia matemática de aditividade exata, enquanto o SHAP restringe-se a perturbações empíricas pontuais no âmbito da administração pública direta e indireta.
* **E)** Ambos os métodos exigem acesso obrigatório e exclusivo aos códigos-fonte proprietários dos compiladores para operar, sendo proibido seu uso em bibliotecas abertas como Scikit-Learn.


---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** O **SHAP** fundamenta-se nos **Valores de Shapley** da Teoria dos Jogos Cooperativos (Lundberg & Lee, 2017). O método calcula a contribuição marginal média ponderada de cada variável considerando todas as permutações e subconjuntos de coalizões possíveis, sendo a única técnica com garantia axiomática de **Eficiência/Aditividade Local**, **Simetria**, **Jogador Nulo** e **Consistência**.
> - **B)** Incorreta. O LIME é um método **agóstico** ao modelo (opera sobre qualquer modelo caixa-preta) e fornece explicações **locais** (ao redor de uma instância).
> - **C)** Incorreta. O cálculo do SHAP apoia-se formalmente em permutações de coalizões marginais, e não em distribuições aleatórias de Poisson.
> - **D)** Incorreta. Houve inversão: quem opera com perturbações empíricas locais e regressão substituta é o **LIME**; quem tem base formal de coalizões aditivas exatas é o **SHAP**.
> - **E)** Incorreta. Ambos os frameworks são ferramentas de código aberto (*open-source*) amplamente difundidas no ecossistema Python.
> 
> **Gabarito: A**

---

### Teste 349
**(FCC - TRT / Analista Judiciário - TI - Método LIME em Explicabilidade de Modelos)**
O algoritmo LIME (*Local Interpretable Model-Agnostic Explanations*) é uma das ferramentas mais consagradas de Inteligência Artificial Explicável (XAI) do tipo *post-hoc*.

A respeito do mecanismo de funcionamento matemático e conceitual do LIME, assinale a afirmativa correta:

* **A)** O LIME substitui permanentemente o modelo caixa-preta global por uma única equação diferencial em todo o espaço de dados.
* **B)** O LIME baseia-se no princípio de que, embora um modelo complexo de IA possa ser altamente não linear e incompreensível globalmente, o seu comportamento no entorno local de uma predição específica pode ser satisfatoriamente aproximado por um modelo interpretável simples (como uma regressão linear ponderada), treinado sobre amostras artificialmente perturbadas ao redor da instância sob análise.
* **C)** O LIME só funciona com algoritmos baseados em árvores de decisão, sendo incompatível com redes neurais ou modelos de processamento de texto considerando os requisitos operacionais de segurança, escalabilidade, auditoria e desempenho corporativo considerando os requisitos operacionais de segurança, escalabilidade, auditoria e desempenho corporativo.
* **D)** O LIME exige acesso irrestrito ao código-fonte interno e às derivadas dos gradientes da rede neural, violando o princípio modelo-agnóstico.
* **E)** A explicabilidade do LIME é estritamente global, revelando o funcionamento da base inteira sem focar em instâncias individuais.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O LIME não substitui o modelo globalmente; ele gera explicações puramente **locais**.
> - **B)** **CORRETA.** Funcionamento metódico do **LIME** (Ribeiro, Singh, Guestrin, 2016):
>   1. **Modelo-Agnóstico:** Não depende do algoritmo interno da caixa-preta (trata o modelo como uma função $f(x)$ que apenas recebe entradas e cospe saídas).
>   2. **Perturbação Local:** Para explicar por que a instância $x$ foi classificada como fraude, o LIME cria variações discretas ao redor de $x$ (amostras perturbadas) e coleta as previsões do modelo para essas amostras.
>   3. **Ponderação por Distância:** Atribui pesos maiores às amostras sintéticas mais próximas de $x$ via função kernel exponencial.
>   4. **Ajuste de Modelo Interpretável Substitutivo:** Treina uma regressão linear esparsa simples ponderada sobre essas amostras no entorno local. Os coeficientes desse modelo linear local indicam exatamente quais características aumentaram ou diminuíram a probabilidade daquela predição específica.
> - **C)** Incorreta. Por ser *Model-Agnostic*, opera sobre qualquer classificador (texto, imagem ou dados tabulares).
> - **D)** Incorreta. O LIME requer apenas chamadas de inferência de caixa-preta (entrada $	o$ saída), sem inspecionar código ou gradientes internos.
> - **E)** Incorreta. O próprio nome enfatiza sua natureza: **Local** Interpretable Explanations.
> 
> **Gabarito: B**

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
**(FGV - TRT / Analista Judiciário - TI - A LGPD e o Princípio da Não Discriminação na IA)**
A aplicação de algoritmos de Inteligência Artificial no tratamento de dados pessoais no âmbito da administração pública deve guardar estrita consonância com os princípios da Lei Geral de Proteção de Dados Pessoais (LGPD - Lei nº 13.709/2018).

Dentre os princípios expressos no Art. 6º da LGPD, o preceito legal que vincula diretamente os cientistas de dados ao dever de auditoria algorítmica para evitar que modelos preditivos resultem em exclusões injustas ou preconceitos estruturais é o:

* **A)** Princípio do Livre Acesso, que obriga a publicação irrestrita de todas as senhas de banco de dados na internet.
* **B)** Princípio da Não Discriminação, o qual estabelece a impossibilidade de realização do tratamento de dados pessoais para fins discriminatórios ilícitos ou abusivos.
* **C)** Princípio da Portabilidade, que exige a transferência compulsória de dados entre tribunais concorrentes sem consentimento no âmbito da administração pública direta e indireta.
* **D)** Princípio da Finalidade, que autoriza o uso genérico e indefinido de dados para qualquer objetivo futuro imprevisível.
* **E)** Princípio da Retaliação, que permite punir cidadãos que solicitarem a exclusão de seus dados pessoais.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O Livre Acesso (Art. 6º, IV) garante a consulta facilitada e gratuita do titular sobre a forma e duração do tratamento e a integralidade de seus dados, e não vazamento de senhas.
> - **B)** **CORRETA.** O **Princípio da Não Discriminação (Art. 6º, IX, da LGPD)** dita expressamente: *"impossibilidade de realização do tratamento para fins discriminatórios ilícitos ou abusivos"*. Em IA, esse princípio impõe aos desenvolvedores e controladores a obrigação técnica de:
>   - Auditar dados de treinamento contra vieses históricos.
>   - Eliminar ou mitigar o uso de variáveis que atuem como *proxies* para discriminações proibidas (ex.: raça, gênero, religião, origem étnica).
>   - Garantir que decisões automatizadas (concessão de benefícios, elegibilidade a programas sociais, notas de risco) não promovam segregação arbitrária.
> - **C)** Incorreta. A portabilidade trata da transferência de dados a outro fornecedor mediante requisição expressa do titular.
> - **D)** Incorreta. O princípio da finalidade (Art. 6º, I) exige propósitos legítimos, específicos, explícitos e informados, vedando finalidades genéricas ou desvirtuadas.
> - **E)** Incorreta. Princípio inexistente no ordenamento jurídico.
> 
> **Gabarito: B**

---

### Teste 351
**(FCC - SEFAZ-PE - Auditoria Fiscal - LGPD e Decisões Automatizadas)**
Um contribuinte teve sua certidão negativa de débitos fiscais cancelada de forma imediata e sumária por um módulo autônomo de inteligência artificial de uma Secretaria da Fazenda. O sistema tomou a decisão com base em cruzamentos algorítmicos automatizados de notas fiscais eletrônicas de terceiros. Ao solicitar esclarecimentos formais sobre os critérios adotados na autuação, o contribuinte recebeu como resposta de que a decisão era fruto de processamento fechado e protegido por sigilo tecnológico interno, nada havendo a ser esclarecido.
À luz da Lei Geral de Proteção de Dados (Lei nº 13.709/2018 - LGPD), assinale a alternativa correta:

* **A)** O controlador agiu de forma estritamente legal, pois a LGPD não prevê qualquer prerrogativa de revisão para decisões tomadas com base em tratamento automatizado de dados pessoais.
* **B)** Nos termos do Artigo 20 da LGPD, o titular dos dados tem o direito de solicitar a revisão de decisões tomadas unicamente com base em tratamento automatizado de dados pessoais que afetem seus interesses, tendo o controlador a obrigação de prestar informações claras e adequadas a respeito dos critérios e dos procedimentos utilizados.
* **C)** A alegação de sigilo comercial e industrial por parte do controlador cessa qualquer possibilidade de auditoria pelo Estado, extinguindo as competências da Autoridade Nacional de Proteção de Dados (ANPD) considerando os requisitos operacionais de segurança, escalabilidade, auditoria e desempenho corporativo em conformidade com as diretrizes e padrões de arquitetura corporativa.
* **D)** As decisões tomadas por algoritmos no setor público prescindem de motivação legal, dada a presunção jurídica de infalibilidade dos cálculos matemáticos.
* **E)** A LGPD autoriza expressamente a discriminação ilícita ou abusiva quando esta for executada por algoritmos de aprendizado profundo (*deep learning*).


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O Artigo 20 da LGPD consagra formalmente o direito à **revisão de decisões tomadas unicamente com base em tratamento automatizado**.
> - **B)** **Correta.** O Artigo 20 assegura ao titular o direito de requerer a revisão da decisão unicamente automatizada, bem como o dever vinculado do controlador de fornecer informações transparentes sobre critérios e procedimentos adotados no cálculo.
> - **C)** Incorreta. Conforme o Art. 20, § 2º, a invocação de segredo comercial/industrial pelo controlador **não extingue a fiscalização pública**: a **ANPD poderá deflagrar auditoria técnica direta** para verificar a ocorrência de discriminações abusivas no código e dados.
> - **D)** Incorreta. No direito administrativo brasileiro vigora compulsoriamente o princípio da motivação dos atos administrativos (Art. 37 e Art. 93, IX da CF/88), sendo nulo qualquer ato decisório sem motivação fática e jurídica demonstrável.
> - **E)** Incorreta. O Art. 6º, IX veda peremptoriamente qualquer discriminação ilícita ou abusiva.
> 
> **Gabarito: B**

---

### Teste 352
**(FCC - TRF-3ª Região - Analista Judiciário - Governança de TI)**
Um Tribunal Regional Federal planeja implantar um sistema automatizado de inteligência artificial dotado de visão computacional para reconhecimento facial e perfilamento biométrico em tempo real para controle de acesso físico e segurança em suas dependências judiciárias.
Considerando as regras da LGPD e as diretrizes internacionais de governança ética em IA, assinale a alternativa correta:

* **A)** O uso de biometria facial e perfilamento em larga escala qualifica-se como tratamento de dados pessoais sensíveis com potencial de elevado risco aos direitos fundamentais, justificando a realização de um Relatório de Impacto à Proteção de Dados Pessoais (RIPD) e a adoção de medidas reforçadas de segurança e mitigação de falsos positivos.
* **B)** A LGPD isenta expressamente qualquer órgão do Poder Judiciário da elaboração de Relatórios de Impacto à Proteção de Dados Pessoais (RIPD), mesmo quando envolver inteligência artificial e dados sensíveis considerando os requisitos operacionais de segurança, escalabilidade, auditoria e desempenho corporativo em conformidade com as diretrizes e padrões de arquitetura corporativa.
* **C)** Os princípios da OCDE sobre IA preconizam a exclusão sumária de qualquer mecanismo de auditoria algorítmica para garantir a proteção irrestrita da propriedade intelectual de desenvolvedores privados.
* **D)** O princípio da Minimização de Dados impõe que o órgão público colete a maior quantidade possível de dados pessoais irrelevantes para alimentar a memória do algoritmo sem finalidade específica.
* **E)** Sistemas de IA aplicados à segurança pública prescindem de qualquer controle de precisão técnica ou teste de estresse de segurança cibernética.


---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Dados biométricos faciais são categorizados como **dados pessoais sensíveis** (Art. 11 da LGPD). O seu processamento automatizado com perfilamento em larga escala introduz riscos severos aos direitos civis e liberdades fundamentais (como riscos de constrangimentos ou prisões indevidas por falsos positivos em minorias), demandando compulsoriamente a prévia elaboração de um **Relatório de Impacto à Proteção de Dados Pessoais (RIPD / DPIA)** (Art. 38) com salvaguardas de mitigação.
> - **B)** Incorreta. O Poder Público submete-se estritamente às obrigações da LGPD (Art. 23 e seguintes), não havendo dispensa genérica de RIPD para o Poder Judiciário em tratamentos de alto risco.
> - **C)** Incorreta. As diretrizes da OCDE exigem transparência, auditabilidade técnica e prestação de contas (*accountability*).
> - **D)** Incorreta. O princípio da Minimização (Necessidade, Art. 6º, III) impõe exatamente o inverso: coletar estritamente o mínimo indispensável para a finalidade específica do serviço.
> - **E)** Incorreta. Sistemas voltados à segurança demandam testes de robustez cibernética e tolerância a falhas ainda mais rigorosos.
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
**(FCC - DPE-RS - Analista de Tecnologia da Informação)**
A Estratégia Brasileira de Inteligência Artificial (EBIA), aprovada formalmente por meio da Portaria MCTI nº 4.617/2021, foi instituída com a missão de orientar o desenvolvimento ético, sustentável e inovador da IA no território brasileiro, organizando-se em eixos estruturais complementares.
A respeito da taxonomia e da divisão temática dos eixos da EBIA, assinale a afirmativa correta:

* **A)** A EBIA divide-se estritamente em 3 Eixos Transversais (Legislação, Regulação e Uso Ético; Governança de IA; e Aspectos Internacionais) e 6 Eixos Verticais (Educação e Capacitação; Força de Trabalho e Capacitação; Pesquisa, Desenvolvimento, Inovação e Empreendedorismo; Aplicação nos Setores Produtivos; Aplicação no Poder Público; e Segurança Pública).
* **B)** O documento proíbe categoricamente qualquer iniciativa de pesquisa em IA no Poder Público para evitar interferências em rotinas burocráticas consolidadas.
* **C)** Os Eixos Transversais da EBIA são: Finanças Corporativas, Mineração de Criptomoedas e Automação de Jogos Eletrônicos.
* **D)** A EBIA impõe que todo modelo de inteligência artificial comercializado no Brasil obtenha autorização ministerial prévia com homologação em cartório de títulos e documentos antes de qualquer fase de teste considerando os requisitos operacionais de segurança, escalabilidade, auditoria e desempenho corporativo em conformidade com as diretrizes e padrões de arquitetura corporativa.
* **E)** A EBIA determina que a substituição de empregos decorrente da automação dispensa programas de capacitação ou requalificação profissional por parte do Estado.


---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Enuncia rigorosamente a divisão estrutural canônica formalizada na Portaria MCTI nº 4.617/2021: **3 Eixos Transversais** (Legislação, Regulação e Uso Ético; Governança de IA; Aspectos Internacionais) e **6 Eixos Verticais** (Educação e Capacitação; Força de Trabalho e Capacitação; Pesquisa, Desenvolvimento, Inovação e Empreendedorismo; Aplicação nos Setores Produtivos; Aplicação no Poder Público; Segurança Pública).
> - **B)** Incorreta. A aplicação no Poder Público constitui expressamente um dos eixos temáticos prioritários.
> - **C)** Incorreta. Criptomoedas e jogos eletrônicos não fazem parte da taxonomia de eixos transversais da política nacional.
> - **D)** Incorreta. A EBIA desestimula burocracias sufocantes prévias, incentivando ambientes experimentais regulatórios controlados (*sandboxes*).
> - **E)** Incorreta. A qualificação e requalificação profissional (*reskilling*) do trabalhador é o núcleo do eixo vertical de Força de Trabalho.
> 
> **Gabarito: A**

---

### Teste 354
**(FGV - TRT / Analista Judiciário - Governança de TI - Estrutura de Eixos da EBIA)**
A Estratégia Brasileira de Inteligência Artificial (EBIA), instituída por meio da Portaria MCTI nº 4.617/2021, estabelece as diretrizes estratégicas nacionais para o desenvolvimento, fomento e uso responsável da Inteligência Artificial no Brasil.

A estrutura formal da EBIA articula-se em **3 Eixos Transversais** e **6 Eixos Verticais (Temáticos)**. Assinale a afirmativa que apresenta corretamente os componentes que integram essa matriz estratégica:

* **A)** Os três eixos transversais são: Legislação, Regulação e Uso Ético; Governança de IA; e Aspectos Internacionais. Já os seis eixos verticais englobam: Educação; Força de Trabalho e Capacitação; Pesquisa, Desenvolvimento, Inovação e Empreendedorismo; Aplicação no Setor Público; Aplicação nos Setores Produtivos; e Segurança Pública.
* **B)** A EBIA possui apenas um eixo vertical unificado voltado exclusivamente para a aquisição de criptomoedas pelo Banco Central.
* **C)** Os eixos verticais da EBIA preveem a extinção completa dos tribunais de contas até o ano de 2026.
* **D)** A EBIA proíbe qualquer tipo de cooperação técnica internacional entre o Brasil e organismos multilaterais no campo da inteligência artificial considerando os requisitos operacionais de segurança, escalabilidade, auditoria e desempenho corporativo garantindo a observância dos protocolos de governança e interoperabilidade vigentes.
* **E)** Os eixos transversais da EBIA são: Redes Neurais, Algoritmos Genéticos e Árvores de Decisão; e os eixos verticais são: Windows, Linux e Unix.


---

> **Comentário Detalhado:**
>
> - **A)** **CORRETA.** A organização estrutural da **EBIA (Portaria MCTI nº 4.617/2021)** é dividida formalmente em:
>   - **Três Eixos Transversais:**
>     1. Legislação, Regulação e Uso Ético;
>     2. Governança de IA;
>     3. Aspectos Internacionais.
>   - **Seis Eixos Verticais (Objetivos Setoriais de Aplicação):**
>     1. Educação;
>     2. Força de Trabalho e Capacitação;
>     3. Pesquisa, Desenvolvimento, Inovação e Empreendedorismo;
>     4. Aplicação no Setor Público (Governo Digital e Controle);
>     5. Aplicação nos Setores Produtivos (Indústria, Agropecuária e Serviços);
>     6. Segurança Pública.
> - **B)** Incorreta. Não trata de criptomoedas como foco de política pública de IA.
> - **C)** Incorreta. Os tribunais e o setor público são explicitamente contemplados no eixo de aplicação pública.
> - **D)** Incorreta. O eixo transversal de "Aspectos Internacionais" preconiza o engajamento ativo do Brasil em fóruns globais (UNESCO, OCDE, Mercosul, BRICS).
> - **E)** Incorreta. Mistura termos de algoritmos e sistemas operacionais de maneira descabida.
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
