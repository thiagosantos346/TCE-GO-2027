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

### Teste 001
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Administrativa - Gestão Governamental)**
Nos termos da Declaração de Lima, as Entidades Fiscalizadoras Superiores (EFS) só podem desempenhar suas tarefas objetiva e efetivamente quando são independentes da auditada. Ademais, a norma preceitua que em suas carreiras profissionais, os auditores de Entidades Fiscalizadoras Superiores não devem ser influenciados pelas organizações auditadas e não devem ser dependentes dessas organizações. Ao discorrer sobre a independência das EFS, Ismar Viana destaca que ... a independência técnico-funcional do agente de controle não se limita ao plano formal, mediante a definição, em lei, das atribuições do cargo, e da arregimentação de servidores públicos pela via do concurso específico... (2019, p.15). Para o autor, a independência das EFS se relaciona à ausência de interferências no exercício da função de controle, o que se concretiza, no plano material, pela

* **A)** garantia legal de estabilidade no serviço público.
* **B)** previsão constitucional de seleção de membros e auditores com base no nível de complexidade do cargo.
* **C)** garantia de meios para elaboração de pareceres técnicos que reflitam com fidedignidade os achados de auditoria.
* **D)** exigência de notórios conhecimentos jurídicos e contábeis, dentre outros, para seleção dos membros dos Tribunais de Contas.
* **E)** definição, em Lei, das atribuições dos membros e auditores dos Tribunais de Contas.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "garantia legal de estabilidade no serviço público". De acordo com a teoria estudada em *1.3 Amostragem em Auditoria Governamental e Riscos Amostrais*, amostragem Estatística (Probabilística): Seleção aleatória de itens na qual cada item da população possui chance conhecida e diferente de zero de ser selecionado. Permite a avaliação quantitativa do risco de amostragem mediante intervalos de confiança matemáticos.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "previsão constitucional de seleção de membros e auditores com base no nível de complexidade do cargo". De acordo com a teoria estudada em *1.1 Critérios de Seleção de Objetos de Controle (Critérios MRC)*, criticidade: Nível de vulnerabilidade do ambiente institucional, complexidade técnica, histórico de fraudes e irregularidades, ou fragilidade evidente dos controles internos.
> - **C)** **Correta.** Conforme fundamentado na seção *1. Planejamento da Fiscalização e Avaliação de Risco* deste guia, o Tribunal de Contas atua pautado pelo planejamento estratégico e pela alocação racional e eficiente de seus auditores e recursos técnicos. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "garantia de meios para elaboração de pareceres técnicos que reflitam com fidedignidade os achados de auditoria".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "exigência de notórios conhecimentos jurídicos e contábeis, dentre outros, para seleção dos membros dos Tribunais...". De acordo com a teoria estudada em *1.3 Amostragem em Auditoria Governamental e Riscos Amostrais*, risco Beta (Risco de Aceitação Incorreta): Concluir que a amostra está adequada quando a população total contém erros relevantes graves. Afeta a eficácia da auditoria e é o mais perigoso, pois o auditor chancela contas viciadas.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "definição, em Lei, das atribuições dos membros e auditores dos Tribunais de Contas". De acordo com a teoria estudada em *1.1 Critérios de Seleção de Objetos de Controle (Critérios MRC)*, relevância: Importância socioeconômica, ambiental ou político estratégica das ações governamentais auditadas para a sociedade.
>
> **Gabarito: C**

---

### Teste 002
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
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A evidência, elemento da matriz de achados, é referente as informações obtidas durante a auditoria, no intuito de...". De acordo com a teoria estudada em *1.3 Amostragem em Auditoria Governamental e Riscos Amostrais*, risco Alfa (Risco de Rejeição Incorreta): Concluir que a amostra apresenta falhas graves quando a população total está em conformidade. Afeta a eficiência do trabalho (gera retrabalho e testes desnecessários).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A matriz de responsabilização fornece o detalhamento para a formulação da proposta que balizará o preenchimento...". De acordo com a teoria estudada em *1.1 Critérios de Seleção de Objetos de Controle (Critérios MRC)*, os objetos de controle a serem incluídos no Plano Anual de Fiscalização são priorizados com base nos consagrados critérios MRC.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Para a devida responsabilização dos agentes que deram causa às impropriedades detectadas deve se avaliar a...". De acordo com a teoria estudada em *1.2 O Modelo do Risco de Auditoria (Auditoria Risk - AR)*, o único risco que o auditor pode e deve controlar diretamente é o Risco de Detecção (RD)! Se o auditor identifica que o ambiente auditado tem alto risco inerente e péssimo controle interno (alto RDR), ele deve planejar testes mais rigorosos, com amostras maiores e procedimentos aprofundados, diminuindo o seu risco de detecção para manter o risco de auditoria global em nível aceitável.
> - **E)** **Correta.** Conforme fundamentado na seção *1.3 Amostragem em Auditoria Governamental e Riscos Amostrais* deste guia, amostragem Estatística (Probabilística): Seleção aleatória de itens na qual cada item da população possui chance conhecida e diferente de zero de ser selecionado. Permite a avaliação quantitativa do risco de amostragem mediante intervalos de confiança matemáticos. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "A conduta, elemento da matriz de achados, trata da situação existente e identificada, inclusive com período de...".
>
> **Gabarito: E**

---

### Teste 003
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
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "procedimentos e técnicas, possíveis achados e questões de auditoria". De acordo com a teoria estudada em *1.3 Amostragem em Auditoria Governamental e Riscos Amostrais*, risco Alfa (Risco de Rejeição Incorreta): Concluir que a amostra apresenta falhas graves quando a população total está em conformidade. Afeta a eficiência do trabalho (gera retrabalho e testes desnecessários).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "metodologia, possíveis incongruências e objetivo geral". De acordo com a teoria estudada em *1.3 Amostragem em Auditoria Governamental e Riscos Amostrais*, amostragem Estatística (Probabilística): Seleção aleatória de itens na qual cada item da população possui chance conhecida e diferente de zero de ser selecionado. Permite a avaliação quantitativa do risco de amostragem mediante intervalos de confiança matemáticos.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "técnicas de auditoria, possíveis achados e questões de auditoria". De acordo com a teoria estudada em *Fundamentos Teóricos*, status: 🟢 Teoria Aprofundada + 5 Questões FCC Comentadas (A a E).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "metodologia, possíveis achados e fontes de informações". De acordo com a teoria estudada em *1.2 O Modelo do Risco de Auditoria (Auditoria Risk - AR)*, o Risco de Auditoria (RA) é o risco de o auditor expressar uma conclusão inadequada quando as informações objeto de fiscalização contiverem distorções relevantes.
> - **E)** **Correta.** Conforme fundamentado na seção *1.2 O Modelo do Risco de Auditoria (Auditoria Risk - AR)* deste guia, o único risco que o auditor pode e deve controlar diretamente é o Risco de Detecção (RD)! Se o auditor identifica que o ambiente auditado tem alto risco inerente e péssimo controle interno (alto RDR), ele deve planejar testes mais rigorosos, com amostras maiores e procedimentos aprofundados, diminuindo o seu risco de detecção para manter o risco de auditoria global em nível aceitável. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "procedimentos e técnicas, possíveis achados e objetivo geral".
>
> **Gabarito: E**

---

### Teste 004
**(FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo - Administração)**
Com a finalidade de apurar desvio de finalidade em uma dispensa de licitação, a equipe de auditoria levantou documentos que comprovaram que a empresa contratada fora criada dias antes de sua contratação, que pertencia a parentes próximos do titular da pasta contratante e que seu patrimônio era dez mil vezes inferior ao objeto do contrato, registrando esses fatos em papéis de trabalho. Nesse sentido, os referidos papéis de trabalho são denominados

* **A)** achados de auditoria.
* **B)** evidências.
* **C)** testes de auditoria.
* **D)** métodos de auditoria.
* **E)** riscos inerentes.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "achados de auditoria". De acordo com a teoria estudada em *1.3 Amostragem em Auditoria Governamental e Riscos Amostrais*, risco Alfa (Risco de Rejeição Incorreta): Concluir que a amostra apresenta falhas graves quando a população total está em conformidade. Afeta a eficiência do trabalho (gera retrabalho e testes desnecessários).
> - **B)** **Correta.** Conforme fundamentado na seção *1.2 O Modelo do Risco de Auditoria (Auditoria Risk - AR)* deste guia, o Risco de Auditoria (RA) é o risco de o auditor expressar uma conclusão inadequada quando as informações objeto de fiscalização contiverem distorções relevantes. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "evidências".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "testes de auditoria". De acordo com a teoria estudada em *1.2 O Modelo do Risco de Auditoria (Auditoria Risk - AR)*, rD Acao["Aumentar a extensão e profundidade dos testes<br/ para reduzir o Risco de Detecção!"].
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "métodos de auditoria". De acordo com a teoria estudada em *1.2 O Modelo do Risco de Auditoria (Auditoria Risk - AR)*, o modelo decompõe se na seguinte relação.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "riscos inerentes". De acordo com a teoria estudada em *1.3 Amostragem em Auditoria Governamental e Riscos Amostrais*, amostragem Estatística (Probabilística): Seleção aleatória de itens na qual cada item da população possui chance conhecida e diferente de zero de ser selecionado. Permite a avaliação quantitativa do risco de amostragem mediante intervalos de confiança matemáticos.
>
> **Gabarito: B**

---

### Teste 005
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
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I, apenas". De acordo com a teoria estudada em *1.3 Amostragem em Auditoria Governamental e Riscos Amostrais*, risco Alfa (Risco de Rejeição Incorreta): Concluir que a amostra apresenta falhas graves quando a população total está em conformidade. Afeta a eficiência do trabalho (gera retrabalho e testes desnecessários).
> - **B)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "III, apenas". De acordo com a teoria estudada em *1.1 Critérios de Seleção de Objetos de Controle (Critérios MRC)*, m Prioridade["Priorização no Plano Anual<br/ de Fiscalização do TCE GO"].
> - **C)** **Correta.** Conforme fundamentado na seção *1.3 Amostragem em Auditoria Governamental e Riscos Amostrais* deste guia, tipos: Aleatória simples, sistemática (intervalo regular de seleção), estratificada (subdivisão da população em estratos homogêneos) e por unidade monetária (foco em valores financeiros mais expressivos). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "III, apenas".
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e II, apenas". De acordo com a teoria estudada em *1.2 O Modelo do Risco de Auditoria (Auditoria Risk - AR)*, o único risco que o auditor pode e deve controlar diretamente é o Risco de Detecção (RD)! Se o auditor identifica que o ambiente auditado tem alto risco inerente e péssimo controle interno (alto RDR), ele deve planejar testes mais rigorosos, com amostras maiores e procedimentos aprofundados, diminuindo o seu risco de detecção para manter o risco de auditoria global em nível aceitável.
> - **E)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e III, apenas". De acordo com a teoria estudada em *1. Planejamento da Fiscalização e Avaliação de Risco*, o Tribunal de Contas atua pautado pelo planejamento estratégico e pela alocação racional e eficiente de seus auditores e recursos técnicos.
>
> **Gabarito: C**

---

