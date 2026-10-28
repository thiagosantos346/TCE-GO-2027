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

1. [Conteúdo Teórico Aprofundado](#conteudo-teorico-aprofundado)
    1. [Planejamento da Fiscalização e Avaliação de Risco](#1-planejamento-da-fiscalizacao-e-avaliacao-de-risco)
    2. [Teste 187](#Teste-187)
    3. [Teste 188](#Teste-188)
    4. [Programas de Auditoria e Documentação (Papéis de Trabalho)](#2-programas-de-auditoria-e-documentacao-papeis-de-trabalho)
    5. [Teste 189](#Teste-189)
    6. [Teste 190](#Teste-190)
    7. [Técnicas e Procedimentos de Auditoria Governamental](#3-tecnicas-e-procedimentos-de-auditoria-governamental)
    8. [Teste 191](#Teste-191)
    9. [Teste 192](#Teste-192)
    10. [Teste 193](#Teste-193)
    11. [Evidências de Auditoria: Os Três Pilares da Validade](#4-evidencias-de-auditoria-os-tres-pilares-da-validade)
    12. [Teste 194](#Teste-194)
    13. [A Estrutura Anatômica do Achado de Auditoria](#5-a-estrutura-anatomica-do-achado-de-auditoria)
    14. [Teste 195](#Teste-195)
    15. [Teste 196](#Teste-196)
    16. [Teste 197](#Teste-197)
2. [Fontes Oficiais & Manuais Técnicos Recomendados](#fontes-oficiais-manuais-tecnicos-recomendados)

---


## 📖 Conteúdo Teórico Aprofundado

### 1. Planejamento da Fiscalização e Avaliação de Risco

O Tribunal de Contas atua pautado pelo planejamento estratégico e pela alocação racional e eficiente de seus auditores e recursos técnicos.

#### 1.1 Critérios de Seleção de Objetos de Controle (Critérios MRC)
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

---

#### 1.2 O Modelo do Risco de Auditoria (Auditoria Risk - AR)
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

---



### Teste 187
**(FCC - Auditor de Controle Externo / TCE-GO)**
No planejamento de uma auditoria governamental, a avaliação do risco de auditoria é fundamental para dimensionar a extensão, a oportunidade e a natureza dos procedimentos a serem aplicados.

Sobre os componentes do risco de auditoria (risco inerente, risco de controle e risco de detecção), assinale a afirmativa correta.

* **A)** O risco de detecção decorre da suscetibilidade de uma afirmação a uma distorção relevante antes da consideração de quaisquer controles internos compensatórios.
* **B)** O risco inerente e o risco de controle existem independentemente da auditoria e são próprios da entidade auditada e de seus processos internos de governança.
* **C)** O risco de controle é o risco de que os procedimentos executados pelo auditor não detectem uma distorção relevante existente no órgão fiscalizado.
* **D)** O auditor do Tribunal de Contas pode controlar e modificar diretamente o nível de risco inerente existente na secretaria auditada.
* **E)** Se o auditor avaliar o risco de controle interno como muito alto, ele deve reduzir o volume de testes substantivos de auditoria para economizar recursos.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A suscetibilidade intrínseca a distorções antes de considerar os controles é o **risco inerente** (NBASP 200).
> - **B)** Correta. A doutrina e as normas de auditoria internacional (NBASP 100/200) estabelecem que o **risco inerente** (inerente à complexidade ou volatilidade da atividade pública) e o **risco de controle** (risco de o sistema de controle interno do órgão falhar em prevenir ou detectar tempestivamente uma distorção) são riscos próprios da entidade auditada, existindo independentemente da realização de auditoria externa.
> - **C)** Incorreta. O risco de que os procedimentos do auditor falhem em detectar o erro é o **risco de detecção**, que é o único componente diretamente controlado pela equipe de auditoria (por meio do tamanho da amostra e profundidade dos testes).
> - **D)** Incorreta. O risco inerente independe da atuação do auditor; o auditor apenas o avalia.
> - **E)** Incorreta. Quanto mais alto o risco de controle, **maior** deve ser a quantidade de testes substantivos e procedimentos de detecção do auditor para mitigar o risco global de auditoria.
>
> **Gabarito: B**

---

### Teste 188
**(FCC - Adaptada / Auditor Governamental)**
Acerca do modelo de avaliação de risco de auditoria e dos fatores de risco considerados no planejamento das ações de controle externo, assinale a opção correta:

* **A)** O risco de detecção é o risco de que os controles internos da entidade auditada não consigam prevenir tempestivamente uma fraude contábil relevante.
* **B)** O risco inerente decorre exclusivamente de erros cometidos pela própria equipe de auditores durante a aplicação de seus testes substantivos.
* **C)** O risco de controle e o risco inerente são intrínsecos ao ambiente do órgão auditado, cabendo ao auditor gerenciar e reduzir o risco de detecção para manter o risco global de auditoria em patamar aceitável.
* **D)** Diante de controles internos eficientes e ausência de risco inerente, o auditor de controle externo pode dispensar a aplicação de quaisquer testes e aprovar as contas sumariamente.
* **E)** O risco de auditoria independe da extensão dos procedimentos aplicados pelo órgão de controle externo.


---

> **Comentário Detalhado:**
>
> - **A) Incorreta:** O risco de o controle interno falhar denomina-se **Risco de Controle (RC)**. Risco de detecção é a falha dos procedimentos do próprio auditor.  
> - **B) Incorreta:** O risco inerente refere-se à suscetibilidade da própria atividade auditada ao erro antes de qualquer controle.  
> - **C) CORRETA:** O auditor não pode alterar o risco inerente nem o risco de controle do jurisdicionado. Portanto, ao se deparar com um órgão de elevado risco (alto risco inerente e fragilidade de controles internos), o auditor deve **reduzir o risco de detecção (RD)** mediante a aplicação de testes mais profundos, com amostras maiores e maior ceticismo profissional.  
> - **D) Incorreta:** Testes substantivos nunca podem ser totalmente dispensados pelas normas de auditoria governamental.  
> - **E) Incorreta:** O risco global de auditoria varia em proporção inversa à extensão e qualidade dos procedimentos executados pela equipe.
> 
> **Gabarito: C**

---



#### 1.3 Amostragem em Auditoria Governamental e Riscos Amostrais
- **Amostragem Estatística (Probabilística):** Seleção aleatória de itens na qual cada item da população possui chance conhecida e diferente de zero de ser selecionado. Permite a avaliação quantitativa do risco de amostragem mediante intervalos de confiança matemáticos.
    - *Tipos:* Aleatória simples, sistemática (intervalo regular de seleção), estratificada (subdivisão da população em estratos homogêneos) e por unidade monetária (foco em valores financeiros mais expressivos).
- **Amostragem Não Estatística (Não Probabilística):** Seleção fundamentada exclusivamente no julgamento profissional, conhecimento prévio ou intuição do auditor.
- **Riscos de Amostragem na FCC:**
    - *Risco Alfa (Risco de Rejeição Incorreta):* Concluir que a amostra apresenta falhas graves quando a população total está em conformidade. Afeta a **eficiência** do trabalho (gera retrabalho e testes desnecessários).
    - *Risco Beta (Risco de Aceitação Incorreta):* Concluir que a amostra está adequada quando a população total contém erros relevantes graves. Afeta a **eficácia** da auditoria e é o mais perigoso, pois o auditor chancela contas viciadas.

---

### 2. Programas de Auditoria e Documentação (Papéis de Trabalho)

- **Programa de Auditoria:** Roteiro operacional e detalhado das etapas, procedimentos e testes substantivos e de conformidade que os membros da equipe devem executar no trabalho de campo.
- **Papéis de Trabalho (Documentação de Auditoria):**
    - *Finalidade:* Registrar as evidências colhidas, suportar técnica e juridicamente o relatório final e comprovar o cumprimento das normas profissionais da NBASP.
    - *Titularidade e Custódia:* São de **propriedade exclusiva do Tribunal de Contas**, sujeitos a sigilo legal durante a fase de instrução e arquivamento regulamentar.
    - *Classificação Arquivística:*
    - **Arquivo Corrente:** Guarda documentos e papéis específicos daquela auditoria em exercício financeiro determinado (ex.: notas fiscais, empenhos daquele mês e atas de medição);
    - **Arquivo Permanente:** Guarda documentos de uso contínuo por vários exercícios (ex.: lei de criação da entidade, organogramas, regimentos internos e manuais de rotina).

---

### Teste 189
**(FCC - Adaptada / Técnico de Controle Externo)**
Em relação aos papéis de trabalho (documentação de auditoria) elaborados e custodiados no âmbito dos Tribunais de Contas, é correto afirmar:

* **A)** Pertencem pessoalmente ao auditor que os confeccionou, que detém o direito autoral de levá-los consigo ao se aposentar.
* **B)** O arquivo permanente é destinado à guarda de documentos específicos de uma única auditoria em exercício financeiro determinado, como notas fiscais daquele mês.
* **C)** Os papéis de trabalho pertencem ao Tribunal de Contas, destinando-se a fundamentar as conclusões do relatório técnico e a comprovar a observância das normas profissionais de auditoria.
* **D)** São de livre acesso público irrestrito e devem ser divulgados em tempo real na internet durante a realização dos testes de campo.
* **E)** Devem ser destruídos imediatamente após a publicação da deliberação plenária terminativa do processo de controle externo.


---

> **Comentário Detalhado:**
>
> - **A) Incorreta:** Os papéis de trabalho são patrimônio documental oficial e institucional exclusivo do Tribunal de Contas.  
> - **B) Incorreta:** O arquivo que guarda os dados de uma única auditoria anual é o **arquivo corrente**. O arquivo permanente abriga dados de uso continuado por anos (leis de criação do órgão, organogramas, estatutos).  
> - **C) CORRETA:** Conforme as normas técnicas da NBASP e Manuais de Auditoria, a documentação de auditoria pertence privativamente ao Tribunal e tem o objetivo primordial de registrar as evidências, fundamentar a opinião expressa e demonstrar a qualidade dos testes executados.  
> - **D) Incorreta:** Durante a fase de instrução e coleta, os papéis de trabalho mantêm-se sob sigilo e confidencialidade profissional para resguardar a integridade das apurações.  
> - **E) Incorreta:** Os papéis de trabalho devem ser mantidos sob guarda e custódia arquivística pelo prazo regulamentar para fins de segurança jurídica e eventual reexame.
> 
> **Gabarito: C**

---



### Teste 190
**(FGV - Analista de Controle Externo / TCE-GO)**
Os papéis de trabalho (documentação de auditoria) constituem o registro físico ou eletrônico de todo o planejamento, dos procedimentos técnicos aplicados, das evidências obtidas e das conclusões alcançadas pela equipe de fiscalização do Tribunal de Contas.

A respeito dos papéis de trabalho na auditoria do setor público (NBASP 100 e NBASP 230), assinale a afirmativa correta.

* **A)** Os papéis de trabalho são de propriedade exclusiva do gestor público auditado, devendo ser devolvidos ao órgão no encerramento da inspeção in loco.
* **B)** A documentação de auditoria deve ser suficientemente completa e detalhada para permitir que um auditor experiente, sem nenhum contato prévio com a auditoria, compreenda a natureza, a época, a extensão dos procedimentos executados, as evidências obtidas e as conclusões alcançadas.
* **C)** É dispensável registrar nos papéis de trabalho a metodologia empregada na seleção de amostras estatísticas.
* **D)** O auditor pode destruir de ofício papéis de trabalho que contenham evidências divergentes das conclusões emitidas no relatório final.
* **E)** Os papéis de trabalho elaborados em fiscalizações de controle externo não possuem valor probatório para fins de instauração de tomada de contas especial.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Os papéis de trabalho são de **propriedade da Entidade Fiscalizadora Superior (Tribunal de Contas)** e ficam sob sua custódia e responsabilidade permanente.
> - **B)** Correta. A NBASP 230 (Documentação de Auditoria) estabelece a chamada regra do **auditor experiente**: a documentação deve ser preparada em nível de detalhamento e clareza suficiente para que um auditor experiente, que não tenha participado anteriormente do trabalho, compreenda os objetivos, a metodologia, os testes realizados, as evidências que suportam os achados e a fundamentação técnica das conclusões e recomendações emitidas.
> - **C)** Incorreta. Toda a memória de cálculo e os parâmetros amostrais devem constar obrigatoriamente nos papéis de trabalho.
> - **D)** Incorreta. A destruição ou sonegação de evidências é infração gravíssima; evidências contraditórias devem ser registradas e tratadas tecnicamente.
> - **E)** Incorreta. Os papéis de trabalho formam a base probatória idônea e documental indispensável que lastreia os achados e os processos de responsabilização no Tribunal de Contas.
>
> **Gabarito: B**

---



### 3. Técnicas e Procedimentos de Auditoria Governamental

#### 3.1 Quadro Geral dos Procedimentos de Obtenção de Evidências

| Procedimento / Técnica | Conceito Operacional | Exemplo Prático de Aplicação |
| :--- | :--- | :--- |
| **Exame Documental** | Análise minuciosa da validade, idoneidade e legalidade formal de documentos fiscais, administrativos e contratuais. | Exame de termos de referência, certidões de regularidade, notas de empenho e notas fiscais eletrônicas. |
| **Inspeção Física** | Constatação presencial e sensorial direta da existência física e qualidade de bens, estoques ou obras públicas. | Vistoria presencial em trecho de rodovia estadual para aferir espessura de asfalto e drenagem. |
| **Conferência de Cálculos (Recálculo)** | Reexecução aritmética independente de operações matemáticas realizadas pelo órgão auditado. | Recálculo de fórmulas de reajuste de tarifas de transporte ou índices de BDI em planilhas de obras. |
| **Observação Direta** | Acompanhamento ocular presencial de uma atividade operacional no momento exato em que é realizada. | Observação do procedimento de descarte de resíduos hospitalares pelo pessoal terceirizado. |
| **Circularização (Confirmação Externa)** | Obtenção de declaração direta por escrito de terceiros independentes alheios ao órgão fiscalizado. | Envio de ofício a banco conveniado solicitando confirmação do saldo e titularidade de conta de convênio. |
| **Procedimentos Analíticos (Revisão Analítica)** | Estudo e comparação de flutuações, índices e relações plausíveis entre dados operacionais e financeiros. | Confronto mensal entre o total de horas extras pagas e o volume de procedimentos médicos cirúrgicos realizados. |

---



### Teste 191
**(FCC - Analista Judiciário - Área Administrativa)**
No planejamento da execução de auditoria contábil e de conformidade em uma secretaria estadual com milhares de processos de pagamento anuais, a equipe de auditoria optou pelo emprego de amostragem em auditoria.

Sobre as técnicas e modalidades de amostragem em auditoria governamental, assinale a afirmativa correta.

* **A)** A amostragem não estatística (por julgamento) permite ao auditor mensurar matematicamente o risco de amostragem e extrapolar com precisão probabilística os resultados para toda a população.
* **B)** Na amostragem estatística, a seleção dos itens da amostra ocorre de forma aleatória ou sistemática fundamentada no cálculo de probabilidades, permitindo que todos os itens da população tenham chance conhecida de serem selecionados, viabilizando a mensuração do risco de amostragem.
* **C)** O risco de amostragem é o risco de o auditor aplicar testes inadequados ou interpretar incorretamente os documentos fiscais analisados.
* **D)** A amostragem é obrigatória em 100% das fiscalizações de controle externo, sendo proibido aos auditores o exame integral (censo) de qualquer contrato.
* **E)** O tamanho da amostra estatística independe do nível de confiança e da taxa de desvio tolerável definidos no plano de auditoria.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A amostragem não estatística (baseada exclusivamente no tirocínio ou julgamento do auditor) não permite calcular matematicamente o risco de amostragem nem extrapolar os resultados com rigor probabilístico.
> - **B)** Correta. Na **amostragem estatística**, os itens são selecionados aleatoriamente com apoio no cálculo de probabilidades, conferindo a todos os elementos do universo a mesma probabilidade matemática de seleção e permitindo quantificar objetivamente o **risco de amostragem** e o nível de precisão dos testes.
> - **C)** Incorreta. Falhas humanas na interpretação ou seleção de procedimentos inadequados configuram o **risco não amostral**. O risco de amostragem é a possibilidade de a conclusão baseada na amostra ser diferente daquela que seria obtida se toda a população fosse examinada.
> - **D)** Incorreta. O auditor pode optar pelo exame integral (100% da população) quando o universo for pequeno ou quando os itens tiverem valor econômico extremamente elevado ou risco crítico.
> - **E)** Incorreta. O tamanho da amostra é calculado em função direta do nível de confiança desejado, da margem de erro e da taxa de desvio tolerável.
>
> **Gabarito: B**

---

### Teste 192
**(FCC - Adaptada / TCE-RS - Auditor de Controle Externo)**
No âmbito dos trabalhos de fiscalização governamental conduzidos por equipe de controle externo do Tribunal de Contas, os auditores compararam o volume mensal de combustível faturado por uma secretaria de estado com a quilometragem média rodada pelos veículos no mesmo período, constatando desvios e picos anômalos de consumo em determinados meses. A técnica de auditoria utilizada pela equipe denomina-se:

* **A)** Circularização ativa.
* **B)** Revisão analítica (ou procedimentos analíticos).
* **C)** Inspeção física.
* **D)** Conciliação contábil.
* **E)** Conferência de cálculos.


---

> **Comentário Detalhado:**
>
> - **A) Incorreta:** Circularização consiste em obter confirmação externa formal de terceiros alheios à entidade auditada.  
> - **B) CORRETA:** Os procedimentos analíticos (ou revisão analítica) compreendem a avaliação de informações financeiras e operacionais por meio de estudo e comparação das relações plausíveis entre dados financeiros e não financeiros, permitindo a detecção de flutuações, índices incoerentes ou variações atípicas que exijam investigação direcionada.  
> - **C) Incorreta:** Inspeção física exige o exame presencial e sensorial da existência palpável de bens, obras ou estoques.  
> - **D) Incorreta:** Conciliação contábil consiste em confrontar saldos contábeis internos com documentos de suporte (ex.: razão contábil e extrato bancário).  
> - **E) Incorreta:** Conferência de cálculos consiste na mera repetição aritmética de cálculos prévios efetuados pela administração pública.
> 
> **Gabarito: B**

---



### Teste 193
**(FGV - Auditor de Controle Externo / TCE-SC)**
Durante auditoria de conformidade em contrato de fornecimento de merenda escolar, a equipe técnica do Tribunal de Contas necessitou confirmar os saldos financeiros e as entregas efetivas de mercadorias declaradas pela empresa contratada em notas fiscais suspeitas.

Para tanto, os auditores enviaram correspondência formal direta aos fornecedores atacadistas primários da empresa, solicitando a confirmação formal e por escrito das quantidades e dos valores das notas emitidas contra a contratada.

O procedimento de auditoria adotado denomina-se:

* **A)** Inspeção física, que consiste no exame in loco das características visuais de um canteiro de obras.
* **B)** Confirmação externa (circularização), caracterizada pela obtenção direta de uma declaração por escrito de um terceiro independente sobre determinadas informações fiscais, bancárias ou operacionais.
* **C)** Procedimento analítico preliminar, baseado unicamente em gráficos e estatísticas orçamentárias gerais.
* **D)** Reexecução, consubstanciada na repetição independente pelo auditor de cálculos aritméticos efetuados pela contabilidade.
* **E)** Observação direta passiva de uma rotina burocrática de almoxarifado.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Inspeção física é a verificação material presencial da existência de bens ou obras.
> - **B)** Correta. A **confirmação externa (ou circularização)**, disciplinada pela NBASP 505 / NBC TA 505, é a evidência obtida pelo auditor como uma resposta direta, por escrito e emitida por um terceiro independente (a parte que confirma) ao auditor, seja em formato de papel, eletrônico ou outro meio. É considerada uma das evidências de maior confiabilidade em auditoria governamental.
> - **C)** Incorreta. Procedimentos analíticos envolvem avaliações de informações financeiras por meio de análise de relações plausíveis entre dados financeiros e não financeiros (análise de tendências e índices).
> - **D)** Incorreta. A conferência matemática de somas e produtos denomina-se **recálculo**; **reexecução** é a realização independente de processos ou controles.
> - **E)** Incorreta. Observação consiste em acompanhar presencialmente a realização de um procedimento executado por terceiros.
>
> **Gabarito: B**

---


#### 3.2 Modalidades de Circularização (Confirmação Externa)

```mermaid
flowchart TD
    Circ["Modalidades de Circularização (Confirmação Externa)"]
    Circ --> PosB["Positiva em Branco:<br/>Não informa o valor; terceiro preenche o saldo.<br/>(Altíssima confiabilidade)"]
    Circ --> PosP["Positiva em Preto:<br/>Informa o saldo e pede confirmação de exatidão.<br/>(Alta confiabilidade)"]
    Circ --> Neg["Negativa:<br/>Terceiro só responde se DISCORDAR do valor.<br/>(Baixa confiabilidade - silêncio gera dúvida)"]
```

---

### 4. Evidências de Auditoria: Os Três Pilares da Validade

As conclusões do relatório de auditoria dependem da colheita de evidências que satisfaçam cumulativamente:

1. **Suficiência (Aspecto Quantitativo):** Mede a quantidade de evidência colhida. Deve ser persuasiva o bastante para convencer uma pessoa sensata e prudente.
2. **Adequação / Relevância (Aspecto Qualitativo):** Pertinência da evidência em relação aos objetivos dos testes e às questões de auditoria formuladas.
3. **Confiabilidade:** Grau de autenticidade da evidência.
    - Evidências obtidas de **fontes externas independentes** são mais confiáveis do que as obtidas dentro da entidade auditada.
    - Evidências obtidas **diretamente pelo auditor** (ex.: inspeção física pessoal) são mais confiáveis do que as obtidas indiretamente.
    - Documentos **originais** são mais confiáveis do que fotocópias ou impressões digitalizadas.

---



### Teste 194
**(FCC - Procurador do Estado / Adaptada)**
A validade e a força persuasiva de um relatório de auditoria emitido pelo Tribunal de Contas dependem diretamente da qualidade das evidências coligidas pela equipe técnica durante os trabalhos de fiscalização.

Nos termos da NBASP 100, para que sustentem adequadamente um achado de auditoria, as evidências devem ser:

* **A)** Secretas e mantidas fora do alcance do contraditório do gestor responsável até a publicação do acórdão condenatório.
* **B)** Suficientes (em quantidade adequada para convencer uma pessoa razoável) e apropriadas (relevantes, válidas e confiáveis em relação ao critério e ao objeto da auditoria).
* **C)** Obtidas exclusivamente mediante confissão expressa do servidor público em termo de oitiva formal.
* **D)** Subjetivas e fundamentadas em ilações conjecturais da imprensa local.
* **E)** Restritas a cópias reprográficas autenticadas em cartório por tabelião de notas.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. As evidências devem ser disponibilizadas ao auditado para assegurar o contraditório e a ampla defesa.
> - **B)** Correta. A NBASP 100 estatui categoricamente que o auditor deve obter **evidência de auditoria suficiente e apropriada** para fundamentar suas conclusões e recomendações: (1) **Suficiência** é a medida da *quantidade* de evidência necessária; (2) **Apropriação** é a medida da *qualidade* da evidência (sua relevância em relação ao critério e sua confiabilidade na representação da realidade).
> - **C)** Incorreta. Em auditoria governamental a evidência documental, física e analítica prevalece sobre o mero testemunho verbal.
> - **D)** Incorreta. Achados não podem ser embasados em meras suposições, boatos ou conjecturas; exigem substrato probatório fático e documental idôneo.
> - **E)** Incorreta. O princípio da verdade material e o art. 37 da CF dispensam a autenticação cartorária de documentos oficiais da administração pública.
>
> **Gabarito: B**

---

### 5. A Estrutura Anatômica do Achado de Auditoria

#### 5.1 Os Quatro Elementos do Achado
O **Achado de Auditoria** é a discrepância relevante identificada entre a situação real constatada e o parâmetro ideal normativo:

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        ANATOMIA DO ACHADO DE AUDITORIA                 │
├───────────────────┬────────────────────────────────────────────────────┤
│ 1. CRITÉRIO       │ O padrão normativo ideal ("O que deveria ser")     │
│                   │ Ex.: O art. 72 da Lei 14.133/21 exige prévio ETP.  │
├───────────────────┼────────────────────────────────────────────────────┤
│ 2. CONDIÇÃO       │ A realidade fática encontrada ("O que é")          │
│                   │ Ex.: Contratação de R$ 3 milhões executada sem ETP.│
├───────────────────┼────────────────────────────────────────────────────┤
│ 3. CAUSA          │ A razão explicativa do desvio ("Por que ocorreu")  │
│                   │ Ex.: Falha no controle interno e falta de servidores.│
├───────────────────┼────────────────────────────────────────────────────┤
│ 4. EFEITO         │ A consequência real ou potencial ("Qual o impacto")│
│                   │ Ex.: Superfaturamento e contratação superdimensionada.│
└───────────────────┴────────────────────────────────────────────────────┘
```

---

### Teste 195
**(FCC - Adaptada / TCE-AM - Auditor de Controle Externo)**
Em relatório de fiscalização de obras rodoviárias, a equipe técnica do Tribunal de Contas registrou a ocorrência de fissuras e afundamentos prematuros no asfalto decorrentes da utilização de ligante betuminoso com espessura inferior à exigida nas especificações do projeto executivo aprovado pela Agência Goiana de Infraestrutura. De acordo com a metodologia de estruturação de achados de auditoria preconizada pelas normas de auditoria do setor público (NBASP), a especificação do projeto executivo e o asfalto com espessura inferior constituem, respectivamente:

* **A)** Condição e Critério.
* **B)** Causa e Efeito.
* **C)** Critério e Condição.
* **D)** Efeito e Causa.
* **E)** Matriz de Risco e Evidência.


---

> **Comentário Detalhado:**
>
> - **A) Incorreta:** A ordem está invertida.  
> - **B) Incorreta:** A causa foi a falha na dosagem ou fiscalização do executor; o efeito foram as fissuras e o prejuízo financeiro.  
> - **C) CORRETA:** Na metodologia do achado de auditoria:  
>     - **Critério:** É o padrão normativo, contratual ou técnico ideal ("o que deveria ser") – neste caso, as especificações técnicas obrigatórias do projeto executivo aprovado.  
>     - **Condição (ou Situação Encontrada):** É a realidade fática verificada pelo auditor *in loco* ("o que é") – neste caso, a aplicação de camada asfáltica com espessura inferior à contratada.  
> - **D) Incorreta:** As deformidades e fissuras representam o efeito/impacto danoso gerado na rodovia.  
> - **E) Incorreta:** Matriz de risco é ferramenta prévia de planejamento, e não elemento integrante da anatomia do achado.
> 
> **Gabarito: C**

---


#### 5.2 Matriz de Responsabilização e a LINDB (Art. 28)
Ao propor imputação de débito ou cominação de multas sancionatórias a agentes públicos, a equipe de auditoria deve confeccionar obrigatoriamente a **Matriz de Responsabilização**, demonstrando:

- **Identificação Individual:** Nome, CPF e cargo do agente público ou privado;
- **Conduta:** Ação ou omissão específica imputada ao gestor;
- **Nexo de Causalidade:** Vínculo fático entre o ato praticado e o resultado lesivo gerado ao erário;
- **Culpabilidade:** Demonstração expressa de que o agente agiu com **dolo ou erro grosseiro** (culpa manifesta e inescusável), nos exatos termos do **Art. 28 da LINDB**.

---

### Teste 196
**(FCC - Adaptada / Analista Jurídico de Controle)**
Ao elaborar a Matriz de Responsabilização em processo de tomada de contas especial decorrente de auditoria, a unidade técnica do Tribunal de Contas imputou dever de ressarcir o erário a determinado Secretário de Estado em virtude de pagamento indevido de adicional de periculosidade a servidores administrativos.

Nos termos do artigo 28 da Lei de Introdução às Normas do Direito Brasileiro (LINDB), para que o agente público responda pessoalmente por suas decisões perante o Tribunal de Contas, é necessário demonstrar que ele agiu:

* **A)** Com qualquer modalidade de culpa leve, aplicando-se a teoria do risco integral administrativo.
* **B)** Com dolo ou erro grosseiro.
* **C)** Sem aprovação prévia da Procuradoria-Geral do Estado, independentemente de demonstração de culpabilidade.
* **D)** Exclusivamente com motivação político-partidária de oposição.
* **E)** Em contrariedade a parecer técnico não vinculante emitido por estagiário do órgão.


---

> **Comentário Detalhado:**
>
> - **A) Incorreta:** A responsabilidade pessoal sancionatória e ressarcitória do gestor perante o Tribunal de Contas não é objetiva (risco integral), exigindo elemento subjetivo qualificado. Culpa levíssima ou escusável não autoriza condenação pessoal.  
> - **B) CORRETA:** O art. 28 da LINDB (com redação dada pela Lei nº 13.655/2018) estabelece categoricamente: *"O agente público responderá pessoalmente por suas decisões ou opiniões técnicas em caso de **dolo ou erro grosseiro**."* O erro grosseiro é a culpa grave, inescusável, resultante de desatenção manifesta que o gestor médio não cometeria.  
> - **C) Incorreta:** A ausência de consulta jurídica isoladamente não presume a culpa grave do agente.  
> - **D) Incorreta:** O art. 28 exige dolo ou erro grosseiro no plano da conduta material, e não motivação partidária.  
> - **E) Incorreta:** Pareceres informais não vinculantes não constituem critério objetivo para definição da responsabilidade do gestor.
> 
> **Gabarito: B**

---





### Teste 197
**(FGV - Analista Jurídico de Controle Externo / TCE-GO)**
Ao finalizar os trabalhos de fiscalização, a equipe de auditoria do Tribunal de Contas estruturou a matriz de achados, identificando deficiências materiais na execução de um programa estadual de incentivo à agricultura familiar.

A respeito dos elementos constitutivos de um achado de auditoria e das deliberações propositivas emitidas pelo Tribunal de Contas, assinale a afirmativa correta.

* **A)** A condição é o padrão ideal que deveria existir conforme estabelecido na lei ou nas melhores práticas de gestão.
* **B)** O achado de auditoria estrutura-se em quatro elementos fundamentais: a condição (a situação encontrada na prática), o critério (o que deveria ser segundo a lei ou padrão), a causa (a razão pela qual a condição ocorreu) e o efeito (a consequência prática ou impacto do desvio).
* **C)** A recomendação constitui mandamento cogente e impositivo que obriga o gestor a cumprir ordem específica sob pena de prisão imediata.
* **D)** A determinação é mera sugestão de melhoria operacional desprovida de qualquer força coercitiva.
* **E)** O efeito de um achado de auditoria limita-se unicamente ao valor monetário do prejuízo contábil imediato.


---

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O padrão normativo que deveria existir denomina-se **critério**. A situação fática real encontrada no órgão é a **condição**.
> - **B)** Correta. Dogmática clássica de auditoria governamental (NBASP 300 e Manual de Auditoria Operacional do TCU/TCEs): todo **achado de auditoria** compõe-se de quatro elementos indissociáveis: (1) **Condição**: o que é (a realidade fática constatada); (2) **Critério**: o que deveria ser (a norma legal, técnica ou boa prática); (3) **Causa**: por que ocorreu (a falha estrutural, omissão ou deficiência); (4) **Efeito**: qual a consequência (o dano patrimonial, social ou ineficiência gerada).
> - **C)** Incorreta. A recomendação tem caráter propositivo e orientativo para aperfeiçoar a gestão; não é ordem coativa punível com prisão.
> - **D)** Incorreta. A **determinação** tem caráter cogente e impositivo, determinando a correção de ilegalidade sob pena de multa e responsabilização funcional do gestor.
> - **E)** Incorreta. O efeito abrange tanto impactos financeiros quanto sociais, qualitativos, ambientais e institucionais.
>
> **Gabarito: B**



---


## 🌐 Fontes Oficiais & Manuais Técnicos Recomendados

* [TCU - Boas Práticas e Padrões de Auditoria Governamental](https://portal.tcu.gov.br/governanca/governanca-no-tcu/) - Diretrizes institucionais de auditoria, matriz de planejamento, achados e matriz de responsabilização.
* [Lei Estadual nº 16.168/2007 - Do Planejamento das Fiscalizações](https://legisla.casacivil.go.gov.br/pesquisa_legislacao/86708/lei-16168) - Regras para inclusão de matérias no plano anual de fiscalização e dever de colaboração dos gestores.
* [TCE-GO - Plano Institucional de Fiscalização e Governança](https://portal.tce.go.gov.br/governanca-planejamento-e-gestao/planos-institucionais/plano-de-fiscalizacao) - Planejamento anual e plurianual das ações de fiscalização externa no Estado de Goiás.
* [TCE-GO - Competências e Jurisdição Institucional](https://portal.tce.go.gov.br/competencias) - Bases legais para requisição de documentos, fixação de prazos e fiscalização de convênios e contratos.
* [Constituição Federal de 1988 - Arts. 70 a 74 (Controle Interno e Externo)](https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm#art70) - Apoio obrigatório do controle interno ao controle externo e dever de comunicação de irregularidades sob pena de responsabilidade solidária.
* CHAVES, Francisco Eduardo Carrilho. **Controle Externo da Gestão Pública**. 3. ed. Niterói: Impetus, 2016. (Cap. 5 - Fases da Auditoria: Planejamento, Execução e Achados).
* CASTRO, Domingos Poubel de. **Auditoria e Controle Interno na Administração Pública**. 3. ed. São Paulo: Atlas, 2019. (Cap. 6 - Procedimentos de Auditoria, Amostragem e Evidências).
* ZYMLER, Benjamin. **Direito Administrativo e Controle**. 3. ed. Belo Horizonte: Fórum, 2015. (Cap. 4 - O Achado de Auditoria e a Matriz de Responsabilização).
