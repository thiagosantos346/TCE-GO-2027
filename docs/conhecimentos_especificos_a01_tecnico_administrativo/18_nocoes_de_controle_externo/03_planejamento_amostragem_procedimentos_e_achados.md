# 03 - Planejamento, Amostragem, Técnicas de Auditoria e Matriz de Achados

> **Matéria:** Noções de Controle Externo  
> **Cargo:** A01 – Técnico de Controle Externo – Especialidade: Técnico Administrativo  
> **Arquivo:** `03_planejamento_amostragem_procedimentos_e_achados.md`  
> **Status:** 🟢 Teoria Aprofundada + 5 Questões FCC Comentadas (A a E)



---


## 📌 Ementa / Itens do Edital

- Planejamento da auditoria de controle externo: delimitação do escopo, visão geral do objeto e questões de auditoria;
- Critérios de seleção e priorização da fiscalização: Materialidade, Relevância e Criticidade (Critérios MRC);
- Modelo de Avaliação de Risco de Auditoria e seus componentes: Risco Inerente, Risco de Controle e Risco de Detecção;
- Amostragem em auditoria governamental: amostragem probabilística (estatística) e não probabilística (por julgamento); métodos de amostragem e risco de amostragem (Risco Alfa e Risco Beta);
- Programas de auditoria e papéis de trabalho (documentação de auditoria): finalidades, requisitos de clareza e completude, confidencialidade, arquivos correntes e permanentes;
- Técnicas e procedimentos de auditoria governamental:
    - Exame documental, inspeção física, conferência de cálculos (recálculo), observação direta, entrevistas técnicas;
    - Circularização (confirmação externa: modalidades positiva em branco, positiva em preto e negativa);
    - Conciliação contábil e bancária;
    - Procedimentos analíticos / Revisão analítica (estudo de relações plausíveis, flutuações e índices);
- Evidências de auditoria: atributos essenciais de validade (suficiência, adequação/pertinência e confiabilidade);
- Estruturação anatômica dos achados de auditoria: Critério, Condição, Causa e Efeito;
- Matriz de Achados e Matriz de Responsabilização (conduta, nexo de causalidade e culpabilidade à luz do Art. 28 da LINDB).

---

## 🧭 Sumário

1. [Planejamento da Fiscalização e Avaliação de Risco](#1-planejamento-da-fiscalizacao-e-avaliacao-de-risco)
    1. [Critérios de Seleção de Objetos de Controle (Critérios MRC)](#11-criterios-de-selecao-de-objetos-de-controle-criterios-mrc)
    2. [O Modelo do Risco de Auditoria (Auditoria Risk - AR)](#12-o-modelo-do-risco-de-auditoria-auditoria-risk-ar)
    3. [Amostragem em Auditoria Governamental e Riscos Amostrais](#13-amostragem-em-auditoria-governamental-e-riscos-amostrais)
    4. [Teste 187](#Teste-187)
    5. [Teste 188](#Teste-188)
2. [Programas de Auditoria e Documentação (Papéis de Trabalho)](#2-programas-de-auditoria-e-documentacao-papeis-de-trabalho)
    1. [Teste 189](#Teste-189)
    2. [Teste 190](#Teste-190)
3. [Técnicas e Procedimentos de Auditoria Governamental](#3-tecnicas-e-procedimentos-de-auditoria-governamental)
    1. [Quadro Geral dos Procedimentos de Obtenção de Evidências](#31-quadro-geral-dos-procedimentos-de-obtencao-de-evidencias)
    2. [Modalidades de Circularização (Confirmação Externa)](#32-modalidades-de-circularizacao-confirmacao-externa)
    3. [Teste 191](#Teste-191)
    4. [Teste 192](#Teste-192)
    5. [Teste 193](#Teste-193)
4. [Evidências de Auditoria: Os Três Pilares da Validade](#4-evidencias-de-auditoria-os-tres-pilares-da-validade)
    1. [Teste 194](#Teste-194)
5. [A Estrutura Anatômica do Achado de Auditoria](#5-a-estrutura-anatomica-do-achado-de-auditoria)
    1. [Os Quatro Elementos do Achado](#51-os-quatro-elementos-do-achado)
    2. [Matriz de Responsabilização e a LINDB (Art. 28)](#52-matriz-de-responsabilizacao-e-a-lindb-art-28)
    3. [Teste 195](#Teste-195)
    4. [Teste 196](#Teste-196)
    5. [Teste 197](#Teste-197)
6. [🌐 Fontes Oficiais & Manuais Técnicos Recomendados](#fontes-oficiais-manuais-tecnicos-recomendados)

---

## 1. Planejamento da Fiscalização e Avaliação de Risco

O Tribunal de Contas atua pautado pelo planejamento estratégico e pela alocação racional e eficiente de seus auditores e recursos técnicos.

### 1.1 Critérios de Seleção de Objetos de Controle (Critérios MRC)
Os objetos de controle a serem incluídos no Plano Anual de Fiscalização são priorizados com base nos consagrados critérios **MRC**:

- **Materialidade:** Representatividade monetária dos recursos geridos pelo órgão (volume financeiro, orçamentário e patrimonial envolvido).
- **Relevância:** Importância socioeconômica, ambiental ou político-estratégica das ações governamentais auditadas para a sociedade.
- **Criticidade:** Nível de vulnerabilidade do ambiente institucional, complexidade técnica, histórico de fraudes e irregularidades, ou fragilidade evidente dos controles internos.

```mermaid
flowchart TD
    subgraph Selecao["Critérios de Seleção MRC"]
        M["Materialidade<br/>(Volume Financeiro)"]
        R["Relevância<br/>(Impacto Socioeconômico)"]
        C["Criticidade<br/>(Fragilidade de Controle)"]
    end
    M --> Prioridade["Priorização no Plano Anual<br/>de Fiscalização do TCE-GO"]
    R --> Prioridade
    C --> Prioridade
```

### 1.2 O Modelo do Risco de Auditoria (Auditoria Risk - AR)
O **Risco de Auditoria (RA)** é o risco de o auditor expressar uma conclusão inadequada quando as informações objeto de fiscalização contiverem distorções relevantes.
O modelo decompõe-se na seguinte relação:

$$\text{Risco de Auditoria} = \text{Risco Inerente (RI)} \times \text{Risco de Controle (RC)} \times \text{Risco de Detecção (RD)}$$

```mermaid
flowchart TD
    AR["Risco de Auditoria (RA)"]
    AR --> RDC["Risco de Distorção Relevante (RDR)<br/>Pertence ao Jurisdicionado"]
    AR --> RD["Risco de Detecção (RD)<br/>Controlado pelo Auditor"]

    RDC --> RI["Risco Inerente (RI):<br/>Suscetibilidade natural da atividade a erros/fraudes"]
    RDC --> RC["Risco de Controle (RC):<br/>Incapacidade do controle interno em prevenir/detectar erros"]

    RD --> Acao["Aumentar a extensão e profundidade dos testes<br/>para reduzir o Risco de Detecção!"]
```

> 🚨 **ALERTA DE PROVA / PEGADINHA FCC:**  
>
> - O auditor **NÃO altera nem controla o Risco Inerente (RI) nem o Risco de Controle (RC)**, pois estes pertencem exclusivamente à estrutura do órgão auditado e à eficiência de sua administração.  
> - O único risco que o auditor pode e deve controlar diretamente é o **Risco de Detecção (RD)**! Se o auditor identifica que o ambiente auditado tem alto risco inerente e péssimo controle interno (alto RDR), ele deve planejar testes mais rigorosos, com amostras maiores e procedimentos aprofundados, diminuindo o seu risco de detecção para manter o risco de auditoria global em nível aceitável.

### 1.3 Amostragem em Auditoria Governamental e Riscos Amostrais
- **Amostragem Estatística (Probabilística):** Seleção aleatória de itens na qual cada item da população possui chance conhecida e diferente de zero de ser selecionado. Permite a avaliação quantitativa do risco de amostragem mediante intervalos de confiança matemáticos.
    - *Tipos:* Aleatória simples, sistemática (intervalo regular de seleção), estratificada (subdivisão da população em estratos homogêneos) e por unidade monetária (foco em valores financeiros mais expressivos).
- **Amostragem Não Estatística (Não Probabilística):** Seleção fundamentada exclusivamente no julgamento profissional, conhecimento prévio ou intuição do auditor.
- **Riscos de Amostragem na FCC:**
    - *Risco Alfa (Risco de Rejeição Incorreta):* Concluir que a amostra apresenta falhas graves quando a população total está em conformidade. Afeta a **eficiência** do trabalho (gera retrabalho e testes desnecessários).
    - *Risco Beta (Risco de Aceitação Incorreta):* Concluir que a amostra está adequada quando a população total contém erros relevantes graves. Afeta a **eficácia** da auditoria e é o mais perigoso, pois o auditor chancela contas viciadas.

---

### Teste 187
**(FGV – TCE/PI – 2025 – Auditor de Controle Externo - Controle Externo - Específica de Área Comum)**
O Auditor Governamental, ao seguir os requisitos gerais da NBASP 3000, realiza auditorias operacionais com integridade, independência e competência, garantindo a credibilidade e a qualidade do trabalho. Esses requisitos asseguram que o auditor aplique ceticismo profissional, obtenha evidências apropriadas e suficientes, e adote uma abordagem baseada em risco. Quanto à NBASP 3000, avalie as afirmativas a seguir e assinale (V) para a verdadeira e (F) para a falsa. ( ) O auditor deve, como parte do planejamento e/ou da condução da auditoria, discutir os critérios de auditoria com a entidade auditada. ( ) O auditor deve gerenciar ativamente o risco de auditoria para evitar o desenvolvimento de achados, conclusões e recomendações incorretos ou incompletos, fornecendo informações inconsistentes ou que não agregam valor. ( ) O auditor deve planejar e manter uma comunicação eficaz e adequada dos aspectos-chave da auditoria com a entidade auditada e as partes interessadas durante todo o processo de auditoria. As afirmativas são, respectivamente,

* **A)** V – F – V.
* **B)** F – V – V.
* **C)** V – V – V.
* **D)** V – V – F.
* **E)** V – F – F.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "V – F – V". De acordo com a teoria estudada em *1.3 Amostragem em Auditoria Governamental e Riscos Amostrais*, *Risco Alfa (Risco de Rejeição Incorreta):* Concluir que a amostra apresenta falhas graves quando a população total está em conformidade. Afeta a eficiência do trabalho (gera retrabalho e testes desnecessários).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "F – V – V". De acordo com a teoria estudada em *1.3 Amostragem em Auditoria Governamental e Riscos Amostrais*, *Risco Beta (Risco de Aceitação Incorreta):* Concluir que a amostra está adequada quando a população total contém erros relevantes graves. Afeta a eficácia da auditoria e é o mais perigoso, pois o auditor chancela contas viciadas.
> - **C)** **Correta.** Conforme fundamentado na seção *1.2 O Modelo do Risco de Auditoria (Auditoria Risk - AR)* deste guia, o único risco que o auditor pode e deve controlar diretamente é o Risco de Detecção (RD)! Se o auditor identifica que o ambiente auditado tem alto risco inerente e péssimo controle interno (alto RDR), ele deve planejar testes mais rigorosos, com amostras maiores e procedimentos aprofundados, diminuindo o seu risco de detecção para manter o risco de auditoria global em nível aceitável. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PI/2025) ao estabelecer que "V – V – V".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "V – V – F". De acordo com a teoria estudada em *1.3 Amostragem em Auditoria Governamental e Riscos Amostrais*, amostragem Não Estatística (Não Probabilística): Seleção fundamentada exclusivamente no julgamento profissional, conhecimento prévio ou intuição do auditor.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "V – F – F". De acordo com a teoria estudada em *1.2 O Modelo do Risco de Auditoria (Auditoria Risk - AR)*, o Risco de Auditoria (RA) é o risco de o auditor expressar uma conclusão inadequada quando as informações objeto de fiscalização contiverem distorções relevantes.
>
> **Gabarito: C**

---

### Teste 188
**(FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo - Economia)**
Durante a execução de uma auditoria governamental, a equipe de auditoria adotou os seguintes procedimentos: I. O supervisor da equipe autorizou somente a realização dos procedimentos de auditoria previstos na matriz de planejamento, negando pedido da equipe para aplicação de técnicas adicionais. II. Foi dispensada a realização da reunião de apresentação da equipe de auditoria ao dirigente da unidade auditada, tendo em vista a superação da fase de planejamento. III. Ao final da etapa de execução, a equipe de auditoria mostrou os achados ao dirigente da unidade auditada, apresentando os critérios adotados, a situação encontrada e as evidências coletadas. Nos termos do Manual de Procedimentos de Auditoria de Conformidade do TCE-SC, está correto o que se indica em

* **A)** I, apenas.
* **B)** III, apenas.
* **C)** III, apenas.
* **D)** I e II, apenas.
* **E)** I e III, apenas.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I, apenas". De acordo com a teoria estudada em *1.3 Amostragem em Auditoria Governamental e Riscos Amostrais*, *Risco Alfa (Risco de Rejeição Incorreta):* Concluir que a amostra apresenta falhas graves quando a população total está em conformidade. Afeta a eficiência do trabalho (gera retrabalho e testes desnecessários).
> - **B)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "III, apenas". De acordo com a teoria estudada em *1.2 O Modelo do Risco de Auditoria (Auditoria Risk - AR)*, o único risco que o auditor pode e deve controlar diretamente é o Risco de Detecção (RD)! Se o auditor identifica que o ambiente auditado tem alto risco inerente e péssimo controle interno (alto RDR), ele deve planejar testes mais rigorosos, com amostras maiores e procedimentos aprofundados, diminuindo o seu risco de detecção para manter o risco de auditoria global em nível aceitável.
> - **C)** **Correta.** Conforme fundamentado na seção *1.3 Amostragem em Auditoria Governamental e Riscos Amostrais* deste guia, *Tipos:* Aleatória simples, sistemática (intervalo regular de seleção), estratificada (subdivisão da população em estratos homogêneos) e por unidade monetária (foco em valores financeiros mais expressivos). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "III, apenas".
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e II, apenas". De acordo com a teoria estudada em *1. Planejamento da Fiscalização e Avaliação de Risco*, o Tribunal de Contas atua pautado pelo planejamento estratégico e pela alocação racional e eficiente de seus auditores e recursos técnicos.
> - **E)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e III, apenas". De acordo com a teoria estudada em *1.3 Amostragem em Auditoria Governamental e Riscos Amostrais*, amostragem Estatística (Probabilística): Seleção aleatória de itens na qual cada item da população possui chance conhecida e diferente de zero de ser selecionado.
>
> **Gabarito: C**

---

### Teste 189
**(FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo - Administração)**
Ao elaborar a matriz de planejamento, a equipe designada para realização de uma auditoria governamental consignou as seguintes informações no referido documento: I. As atividades que a equipe de auditoria deve realizar para obter evidências suficientes e adequadas, possibilitando a avaliação da conformidade do objeto em relação aos critérios de auditoria. II. As eventuais constatações que podem ser obtidas a partir dos exames realizados, resultando nas não conformidades que a equipe espera identificar. III. A definição do tema central que delimita o trabalho de auditoria e define o seu propósito. Nos termos do Manual de Procedimentos da Auditoria de Conformidade do TCE-SC, os campos da matriz de planejamento a que se referem as informações acima são denominados, respectivamente,

* **A)** procedimentos e técnicas, possíveis achados e questões de auditoria.
* **B)** metodologia, possíveis incongruências e objetivo geral.
* **C)** técnicas de auditoria, possíveis achados e questões de auditoria.
* **D)** metodologia, possíveis achados e fontes de informações.
* **E)** procedimentos e técnicas, possíveis achados e objetivo geral.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "procedimentos e técnicas, possíveis achados e questões de auditoria". De acordo com a teoria estudada em *1.3 Amostragem em Auditoria Governamental e Riscos Amostrais*, *Risco Alfa (Risco de Rejeição Incorreta):* Concluir que a amostra apresenta falhas graves quando a população total está em conformidade. Afeta a eficiência do trabalho (gera retrabalho e testes desnecessários).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "metodologia, possíveis incongruências e objetivo geral". De acordo com a teoria estudada em *1.2 O Modelo do Risco de Auditoria (Auditoria Risk - AR)*, o Risco de Auditoria (RA) é o risco de o auditor expressar uma conclusão inadequada quando as informações objeto de fiscalização contiverem distorções relevantes.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "técnicas de auditoria, possíveis achados e questões de auditoria". De acordo com a teoria estudada em *1.3 Amostragem em Auditoria Governamental e Riscos Amostrais*, amostragem Estatística (Probabilística): Seleção aleatória de itens na qual cada item da população possui chance conhecida e diferente de zero de ser selecionado.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "metodologia, possíveis achados e fontes de informações". De acordo com a teoria estudada em *1. Planejamento da Fiscalização e Avaliação de Risco*, o Tribunal de Contas atua pautado pelo planejamento estratégico e pela alocação racional e eficiente de seus auditores e recursos técnicos.
> - **E)** **Correta.** Conforme fundamentado na seção *1.2 O Modelo do Risco de Auditoria (Auditoria Risk - AR)* deste guia, o único risco que o auditor pode e deve controlar diretamente é o Risco de Detecção (RD)! Se o auditor identifica que o ambiente auditado tem alto risco inerente e péssimo controle interno (alto RDR), ele deve planejar testes mais rigorosos, com amostras maiores e procedimentos aprofundados, diminuindo o seu risco de detecção para manter o risco de auditoria global em nível aceitável. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "procedimentos e técnicas, possíveis achados e objetivo geral".
>
> **Gabarito: E**

---

### Teste 190
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Administrativa - Gestão Governamental)**
A NBASP 9020 fornece informações sobre as principais questões para a auditoria operacional e para a avaliação de políticas públicas, de modo a diferenciá-las. Sobre as semelhanças e diferenças entre os dois instrumentos, analise as afirmativas a seguir. I. A auditoria operacional avalia principalmente a economicidade, a eficiência e a efetividade até o nível do resultado imediato, enquanto a avaliação de política pública é definida como o exame desses mesmos aspectos e de resultados mais amplos e adicionalmente de impactos globais e socioeconômicos. II. A avaliação de políticas públicas se concentra na relevância da política, que é a adequação dos seus objetivos em relação às necessidades sociais, econômicas ou ambientais que a política pública quer atender. III. A avaliação de políticas públicas se concentra na utilidade da política, que lida com a questão de conhecer se a política foi vantajosa, levando em consideração, por um lado, todos os seus efeitos diretos (resultados) e indiretos (impactos), inclusive os não-intencionais ou não-esperados, e por outro, as necessidades que pretendia atender. IV. A avaliação de políticas públicas não deve se limitar a objetivos pré-estabelecidos, uma vez que pode questionar os objetivos estabelecidos na legislação. Estão corretas as afirmativas

* **A)** I, II e III, somente.
* **B)** II, III e IV, somente.
* **C)** I, II, III e IV.
* **D)** I, II e IV, somente.
* **E)** II e III, somente.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I, II e III, somente". De acordo com a teoria estudada em *1.2 O Modelo do Risco de Auditoria (Auditoria Risk - AR)*, o Risco de Auditoria (RA) é o risco de o auditor expressar uma conclusão inadequada quando as informações objeto de fiscalização contiverem distorções relevantes.
> - **B)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "II, III e IV, somente". De acordo com a teoria estudada em *1.2 O Modelo do Risco de Auditoria (Auditoria Risk - AR)*, o modelo decompõe-se na seguinte relação.
> - **C)** **Correta.** Conforme fundamentado na seção *1.2 O Modelo do Risco de Auditoria (Auditoria Risk - AR)* deste guia, o único risco que o auditor pode e deve controlar diretamente é o Risco de Detecção (RD)! Se o auditor identifica que o ambiente auditado tem alto risco inerente e péssimo controle interno (alto RDR), ele deve planejar testes mais rigorosos, com amostras maiores e procedimentos aprofundados, diminuindo o seu risco de detecção para manter o risco de auditoria global em nível aceitável. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "I, II, III e IV".
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I, II e IV, somente". De acordo com a teoria estudada em *1.1 Critérios de Seleção de Objetos de Controle (Critérios MRC)*, relevância: Importância socioeconômica, ambiental ou político-estratégica das ações governamentais auditadas para a sociedade.
> - **E)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "II e III, somente". De acordo com a teoria estudada em *1.2 O Modelo do Risco de Auditoria (Auditoria Risk - AR)*, o auditor NÃO altera nem controla o Risco Inerente (RI) nem o Risco de Controle (RC), pois estes pertencem exclusivamente à estrutura do órgão auditado e à eficiência de sua administração.
>
> **Gabarito: C**

---

### Teste 191
**(FGV – TCE/SC – 2026 – Auditor Fiscal De Controle Externo Engenharia Sanitaria)**
À luz da NR nº 6/2024 da Agência Nacional de Águas e Saneamento Básico, analise as afirmativas a seguir sobre as diferenças entre os modelos de regulação contratual e discricionária. I. No modelo contratual, as principais regras e procedimentos de remuneração, formação da tarifa, metas de cobertura e de expansão do atendimento dos serviços, níveis de desempenho e de qualidade da prestação, e alocação de riscos são definidos nos termos do instrumento contratual pactuado. II. O modelo contratual deve ser aplicado exclusivamente aos prestadores públicos de natureza autárquica, sendo vedada sua aplicação em contratos de concessão comum ou em parcerias público-privadas (PPPs). III. No modelo de regulação discricionária, a definição e revisão das metas de universalização dependem predominantemente de atos normativos e decisões técnicas da entidade reguladora, podendo ocorrer independentemente de previsão contratual detalhada. Está correto apenas o que se afirma em

* **A)** I.
* **B)** III.
* **C)** I e II.
* **D)** I e III.
* **E)** II e III.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "I". De acordo com a teoria estudada em *1.3 Amostragem em Auditoria Governamental e Riscos Amostrais*, amostragem Estatística (Probabilística): Seleção aleatória de itens na qual cada item da população possui chance conhecida e diferente de zero de ser selecionado.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "III". De acordo com a teoria estudada em *1.2 O Modelo do Risco de Auditoria (Auditoria Risk - AR)*, o auditor NÃO altera nem controla o Risco Inerente (RI) nem o Risco de Controle (RC), pois estes pertencem exclusivamente à estrutura do órgão auditado e à eficiência de sua administração.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "I e II". De acordo com a teoria estudada em *1.3 Amostragem em Auditoria Governamental e Riscos Amostrais*, amostragem Não Estatística (Não Probabilística): Seleção fundamentada exclusivamente no julgamento profissional, conhecimento prévio ou intuição do auditor.
> - **D)** **Correta.** Conforme fundamentado na seção *1.2 O Modelo do Risco de Auditoria (Auditoria Risk - AR)* deste guia, o único risco que o auditor pode e deve controlar diretamente é o Risco de Detecção (RD)! Se o auditor identifica que o ambiente auditado tem alto risco inerente e péssimo controle interno (alto RDR), ele deve planejar testes mais rigorosos, com amostras maiores e procedimentos aprofundados, diminuindo o seu risco de detecção para manter o risco de auditoria global em nível aceitável. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "I e III".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "II e III". De acordo com a teoria estudada em *1. Planejamento da Fiscalização e Avaliação de Risco*, o Tribunal de Contas atua pautado pelo planejamento estratégico e pela alocação racional e eficiente de seus auditores e recursos técnicos.
>
> **Gabarito: D**

---

### Teste 192
**(FGV – TRT da 24º Região – 2025 – Analista Judiciário - Área Administrativa - Sem Especialidade)**
Um problema importante em inferência estatística decorre da necessidade de se obter uma amostra de uma determinada população para se estudar determinado fenômeno. Nesse caso, um problema crucial é se obter uma mostra que seja, em algum sentido, representativa da população em estudo, o que nos leva a pensar em como nossa amostra pode ser obtida. Um método importante, nesse sentido, é a amostragem aleatória simples, na qual

* **A)** a população apresenta uma subdivisão em pequenos grupos, e é possível e conveniente sortear um número suficiente desses grupos, cujos elementos constituirão a amostra.
* **B)** a população se divide em subpopulações, de tal modo que podemos especificar quantos elementos da amostra serão retirados em cada subpopulação.
* **C)** todos os elementos da população têm igual probabilidade de pertencer à amostra, e todas as possíveis amostras têm também igual probabilidade de ocorrer.
* **D)** a população pode ser ordenada e cada elemento da amostra é obtido a partir de uma escolha sistemática e periódica.
* **E)** a amostra é retirada em diversas etapas sucessivas e, dependendo dos resultados obtidos, etapas suplementares são necessárias ou dispensadas.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "a população apresenta uma subdivisão em pequenos grupos, e é possível e conveniente sortear um número suficiente...". De acordo com a teoria estudada em *1.3 Amostragem em Auditoria Governamental e Riscos Amostrais*, *Tipos:* Aleatória simples, sistemática (intervalo regular de seleção), estratificada (subdivisão da população em estratos homogêneos) e por unidade monetária (foco em valores financeiros mais expressivos).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "a população se divide em subpopulações, de tal modo que podemos especificar quantos elementos da amostra serão...". De acordo com a teoria estudada em *1.3 Amostragem em Auditoria Governamental e Riscos Amostrais*, *Risco Beta (Risco de Aceitação Incorreta):* Concluir que a amostra está adequada quando a população total contém erros relevantes graves. Afeta a eficácia da auditoria e é o mais perigoso, pois o auditor chancela contas viciadas.
> - **C)** **Correta.** Conforme fundamentado na seção *1.3 Amostragem em Auditoria Governamental e Riscos Amostrais* deste guia, *Risco Alfa (Risco de Rejeição Incorreta):* Concluir que a amostra apresenta falhas graves quando a população total está em conformidade. Afeta a eficiência do trabalho (gera retrabalho e testes desnecessários). Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT da 24º Região/2025) ao estabelecer que "todos os elementos da população têm igual probabilidade de pertencer à amostra, e todas as possíveis amostras têm...".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "a população pode ser ordenada e cada elemento da amostra é obtido a partir de uma escolha sistemática e periódica". De acordo com a teoria estudada em *1.3 Amostragem em Auditoria Governamental e Riscos Amostrais*, amostragem Estatística (Probabilística): Seleção aleatória de itens na qual cada item da população possui chance conhecida e diferente de zero de ser selecionado.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "a amostra é retirada em diversas etapas sucessivas e, dependendo dos resultados obtidos, etapas suplementares são...". De acordo com a teoria estudada em *1.2 O Modelo do Risco de Auditoria (Auditoria Risk - AR)*, o único risco que o auditor pode e deve controlar diretamente é o Risco de Detecção (RD)! Se o auditor identifica que o ambiente auditado tem alto risco inerente e péssimo controle interno (alto RDR), ele deve planejar testes mais rigorosos, com amostras maiores e procedimentos aprofundados, diminuindo o seu risco de detecção para manter o risco de auditoria global em nível aceitável.
>
> **Gabarito: C**

---

### Teste 193
**(FGV – TCE/PI – 2025 – Auditor de Controle Externo - Controle Externo - Específica de Área Comum)**
Luciana, auditora de controle externo do Tribunal de Contas do Estado do Piauí, obteve, no curso de auditoria governamental, informações sigilosas de órgão jurisdicionado da Corte de Contas, tomando a devida cautela no seu armazenamento e na restrição de acesso. Visando robustecer ainda mais as evidências obtidas, Luciana realizou entrevistas de auditoria com outros órgãos jurisdicionados do TCE-PI e com representantes da sociedade civil, disponibilizando as informações sigilosas recebidas para fins de confronto e circularização. Nos termos do Estatuto dos Servidores Públicos do Estado do Piauí, a conduta de Luciana de divulgar informações sigilosas obtidas no exercício das funções pode sujeitá-la à penalidade disciplinar de

* **A)** demissão.
* **B)** suspensão.
* **C)** advertência.
* **D)** destituição de função gratificada.
* **E)** destituição de cargo em comissão.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *1.3 Amostragem em Auditoria Governamental e Riscos Amostrais* deste guia, *Risco Beta (Risco de Aceitação Incorreta):* Concluir que a amostra está adequada quando a população total contém erros relevantes graves. Afeta a eficácia da auditoria e é o mais perigoso, pois o auditor chancela contas viciadas. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PI/2025) ao estabelecer que "demissão".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "suspensão". De acordo com a teoria estudada em *1.2 O Modelo do Risco de Auditoria (Auditoria Risk - AR)*, o único risco que o auditor pode e deve controlar diretamente é o Risco de Detecção (RD)! Se o auditor identifica que o ambiente auditado tem alto risco inerente e péssimo controle interno (alto RDR), ele deve planejar testes mais rigorosos, com amostras maiores e procedimentos aprofundados, diminuindo o seu risco de detecção para manter o risco de auditoria global em nível aceitável.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "advertência". De acordo com a teoria estudada em *1.3 Amostragem em Auditoria Governamental e Riscos Amostrais*, *Tipos:* Aleatória simples, sistemática (intervalo regular de seleção), estratificada (subdivisão da população em estratos homogêneos) e por unidade monetária (foco em valores financeiros mais expressivos).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "destituição de função gratificada". De acordo com a teoria estudada em *1.2 O Modelo do Risco de Auditoria (Auditoria Risk - AR)*, o Risco de Auditoria (RA) é o risco de o auditor expressar uma conclusão inadequada quando as informações objeto de fiscalização contiverem distorções relevantes.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "destituição de cargo em comissão". De acordo com a teoria estudada em *1.1 Critérios de Seleção de Objetos de Controle (Critérios MRC)*, relevância: Importância socioeconômica, ambiental ou político-estratégica das ações governamentais auditadas para a sociedade.
>
> **Gabarito: A**

---

### Teste 194
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Fiscalização - Contabilidade)**
Quanto à amostragem em auditoria assinale a afirmativa correta.

* **A)** A amostragem por atributos tem por objetivo estimar uma proporção, sendo relacionada aos testes de controle.
* **B)** A amostragem por atributos tem por objetivo estimar a média por unidade monetária, sendo relacionada aos testes substantivos.
* **C)** A amostragem de unidades monetárias tem por objetivo estimar uma proporção, sendo relacionada aos testes de controle.
* **D)** A amostragem de unidades monetárias tem por objetivo estimar uma proporção, sendo relacionada aos testes substantivos.
* **E)** A amostragem por atributos tem por objetivo estimar a média um valor monetário, sendo relacionada aos testes substantivos.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *1.3 Amostragem em Auditoria Governamental e Riscos Amostrais* deste guia, *Risco Alfa (Risco de Rejeição Incorreta):* Concluir que a amostra apresenta falhas graves quando a população total está em conformidade. Afeta a eficiência do trabalho (gera retrabalho e testes desnecessários). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "A amostragem por atributos tem por objetivo estimar uma proporção, sendo relacionada aos testes de controle".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A amostragem por atributos tem por objetivo estimar a média por unidade monetária, sendo relacionada aos testes...". De acordo com a teoria estudada em *1.3 Amostragem em Auditoria Governamental e Riscos Amostrais*, *Tipos:* Aleatória simples, sistemática (intervalo regular de seleção), estratificada (subdivisão da população em estratos homogêneos) e por unidade monetária (foco em valores financeiros mais expressivos).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A amostragem de unidades monetárias tem por objetivo estimar uma proporção, sendo relacionada aos testes de...". De acordo com a teoria estudada em *1.2 O Modelo do Risco de Auditoria (Auditoria Risk - AR)*, o único risco que o auditor pode e deve controlar diretamente é o Risco de Detecção (RD)! Se o auditor identifica que o ambiente auditado tem alto risco inerente e péssimo controle interno (alto RDR), ele deve planejar testes mais rigorosos, com amostras maiores e procedimentos aprofundados, diminuindo o seu risco de detecção para manter o risco de auditoria global em nível aceitável.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A amostragem de unidades monetárias tem por objetivo estimar uma proporção, sendo relacionada aos testes...". De acordo com a teoria estudada em *1.3 Amostragem em Auditoria Governamental e Riscos Amostrais*, amostragem Estatística (Probabilística): Seleção aleatória de itens na qual cada item da população possui chance conhecida e diferente de zero de ser selecionado.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A amostragem por atributos tem por objetivo estimar a média um valor monetário, sendo relacionada aos testes...". De acordo com a teoria estudada em *1.3 Amostragem em Auditoria Governamental e Riscos Amostrais*, permite a avaliação quantitativa do risco de amostragem mediante intervalos de confiança matemáticos.
>
> **Gabarito: A**

---

### Teste 195
**(FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo - Administração)**
A respeito dos procedimentos de auditoria, avalie as afirmativas a seguir. I. A observação é limitada pelo fato de que o ato de ser observado pode afetar como o processo ou procedimento é executado. II. O resultado de entrevistas e da aplicação de questionários a fiscais de contratos geram evidências apropriadas e suficientes à comprovação de fraudes em licitações. III. A inspeção envolve buscar informações de pessoas pertinentes, dentro e fora da entidade auditada, assim como o exame de livros e documentos, inclusive externos à organização. Está correto o que se afirma em

* **A)** I, apenas.
* **B)** III, apenas.
* **C)** I e III, apenas.
* **D)** II e III, apenas.
* **E)** I, II e III.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *1.2 O Modelo do Risco de Auditoria (Auditoria Risk - AR)* deste guia, o único risco que o auditor pode e deve controlar diretamente é o Risco de Detecção (RD)! Se o auditor identifica que o ambiente auditado tem alto risco inerente e péssimo controle interno (alto RDR), ele deve planejar testes mais rigorosos, com amostras maiores e procedimentos aprofundados, diminuindo o seu risco de detecção para manter o risco de auditoria global em nível aceitável. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "I, apenas".
> - **B)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "III, apenas". De acordo com a teoria estudada em *1.2 O Modelo do Risco de Auditoria (Auditoria Risk - AR)*, o Risco de Auditoria (RA) é o risco de o auditor expressar uma conclusão inadequada quando as informações objeto de fiscalização contiverem distorções relevantes.
> - **C)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e III, apenas". De acordo com a teoria estudada em *1.3 Amostragem em Auditoria Governamental e Riscos Amostrais*, amostragem Estatística (Probabilística): Seleção aleatória de itens na qual cada item da população possui chance conhecida e diferente de zero de ser selecionado.
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "II e III, apenas". De acordo com a teoria estudada em *1.1 Critérios de Seleção de Objetos de Controle (Critérios MRC)*, criticidade: Nível de vulnerabilidade do ambiente institucional, complexidade técnica, histórico de fraudes e irregularidades, ou fragilidade evidente dos controles internos.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "I, II e III". De acordo com a teoria estudada em *1.2 O Modelo do Risco de Auditoria (Auditoria Risk - AR)*, o modelo decompõe-se na seguinte relação.
>
> **Gabarito: A**

---

### Teste 196
**(FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo - Ciências Contábeis)**
Um auditor realizou diversos testes de detalhes para obter evidência de auditoria suficiente e apropriada de que não existem distorções relevantes no nível das afirmações sobre a entidade auditada. Nesse sentido, assinale a opção que indica uma técnica de auditoria e um exemplo que corresponde a ela, de acordo com o Manual de Auditoria Financeira.

* **A)** Confirmação: análises e conciliações de contas e/ou saldos.
* **B)** Recálculo: conferência de valores consolidados e eliminação de transações intergrupo, quando apropriada.
* **C)** Análises: exame de relatórios da auditoria interna sobre a confiabilidade das contas.
* **D)** Inspeção: verificação do correto lançamento na contabilidade de transações selecionadas.
* **E)** Indagação: verificação de que o balanço de abertura do ano em curso corresponde ao balanço de encerramento do ano anterior.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Confirmação: análises e conciliações de contas e/ou saldos". De acordo com a teoria estudada em *1.3 Amostragem em Auditoria Governamental e Riscos Amostrais*, *Risco Beta (Risco de Aceitação Incorreta):* Concluir que a amostra está adequada quando a população total contém erros relevantes graves. Afeta a eficácia da auditoria e é o mais perigoso, pois o auditor chancela contas viciadas.
> - **B)** **Correta.** Conforme fundamentado na seção *1.3 Amostragem em Auditoria Governamental e Riscos Amostrais* deste guia, *Tipos:* Aleatória simples, sistemática (intervalo regular de seleção), estratificada (subdivisão da população em estratos homogêneos) e por unidade monetária (foco em valores financeiros mais expressivos). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "Recálculo: conferência de valores consolidados e eliminação de transações intergrupo, quando apropriada".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Análises: exame de relatórios da auditoria interna sobre a confiabilidade das contas". De acordo com a teoria estudada em *1.2 O Modelo do Risco de Auditoria (Auditoria Risk - AR)*, o Risco de Auditoria (RA) é o risco de o auditor expressar uma conclusão inadequada quando as informações objeto de fiscalização contiverem distorções relevantes.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Inspeção: verificação do correto lançamento na contabilidade de transações selecionadas". De acordo com a teoria estudada em *1.1 Critérios de Seleção de Objetos de Controle (Critérios MRC)*, criticidade: Nível de vulnerabilidade do ambiente institucional, complexidade técnica, histórico de fraudes e irregularidades, ou fragilidade evidente dos controles internos.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Indagação: verificação de que o balanço de abertura do ano em curso corresponde ao balanço de encerramento do ano...". De acordo com a teoria estudada em *1.2 O Modelo do Risco de Auditoria (Auditoria Risk - AR)*, o único risco que o auditor pode e deve controlar diretamente é o Risco de Detecção (RD)! Se o auditor identifica que o ambiente auditado tem alto risco inerente e péssimo controle interno (alto RDR), ele deve planejar testes mais rigorosos, com amostras maiores e procedimentos aprofundados, diminuindo o seu risco de detecção para manter o risco de auditoria global em nível aceitável.
>
> **Gabarito: B**

---

### Teste 197
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Fiscalização - Contabilidade)**
No encerramento do trabalho de auditoria governamental deve ser apresentado relatório com as constatações da equipe de auditoria. Junto a este relatório, para além de outros documentos, são apresentadas matrizes relativas aos achados de auditoria e à responsabilização daqueles a que deram causa as impropriedades verificadas. Em relação às matrizes de achado e responsabilização assinale a afirmativa incorreta.

* **A)** A matriz de achados sintetiza os elementos dos achados e demais informações úteis para a assimilação das respostas às questões planejadas, servindo de base para discussões sobre os resultados alcançados e auxiliando a elaboração do relatório de auditoria.
* **B)** A evidência, elemento da matriz de achados, é referente as informações obtidas durante a auditoria, no intuito de documentar os achados e respaldar as conclusões e opiniões da equipe de auditoria.
* **C)** A matriz de responsabilização fornece o detalhamento para a formulação da proposta que balizará o preenchimento dos encaminhamentos a serem sugeridos no âmbito da matriz de achados.
* **D)** Para a devida responsabilização dos agentes que deram causa às impropriedades detectadas deve-se avaliar a reprovabilidade da contudo, utilizando os preceitos da Lei de Introdução do Direito Brasileiro.
* **E)** A conduta, elemento da matriz de achados, trata da situação existente e identificada, inclusive com período de ocorrência, e documentada durante a fase de execução da auditoria.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A matriz de achados sintetiza os elementos dos achados e demais informações úteis para a assimilação das respostas...". De acordo com a teoria estudada em *1.2 O Modelo do Risco de Auditoria (Auditoria Risk - AR)*, o Risco de Auditoria (RA) é o risco de o auditor expressar uma conclusão inadequada quando as informações objeto de fiscalização contiverem distorções relevantes.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A evidência, elemento da matriz de achados, é referente as informações obtidas durante a auditoria, no intuito de...". De acordo com a teoria estudada em *1.3 Amostragem em Auditoria Governamental e Riscos Amostrais*, *Risco Alfa (Risco de Rejeição Incorreta):* Concluir que a amostra apresenta falhas graves quando a população total está em conformidade. Afeta a eficiência do trabalho (gera retrabalho e testes desnecessários).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A matriz de responsabilização fornece o detalhamento para a formulação da proposta que balizará o preenchimento...". De acordo com a teoria estudada em *1.1 Critérios de Seleção de Objetos de Controle (Critérios MRC)*, os objetos de controle a serem incluídos no Plano Anual de Fiscalização são priorizados com base nos consagrados critérios MRC.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Para a devida responsabilização dos agentes que deram causa às impropriedades detectadas deve-se avaliar a...". De acordo com a teoria estudada em *1.2 O Modelo do Risco de Auditoria (Auditoria Risk - AR)*, o único risco que o auditor pode e deve controlar diretamente é o Risco de Detecção (RD)! Se o auditor identifica que o ambiente auditado tem alto risco inerente e péssimo controle interno (alto RDR), ele deve planejar testes mais rigorosos, com amostras maiores e procedimentos aprofundados, diminuindo o seu risco de detecção para manter o risco de auditoria global em nível aceitável.
> - **E)** **Correta.** Conforme fundamentado na seção *1.3 Amostragem em Auditoria Governamental e Riscos Amostrais* deste guia, amostragem Estatística (Probabilística): Seleção aleatória de itens na qual cada item da população possui chance conhecida e diferente de zero de ser selecionado. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "A conduta, elemento da matriz de achados, trata da situação existente e identificada, inclusive com período de...".
>
> **Gabarito: E**

---

