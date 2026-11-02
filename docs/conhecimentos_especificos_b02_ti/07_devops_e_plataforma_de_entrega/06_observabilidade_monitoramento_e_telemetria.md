# 06 - Observabilidade, Monitoramento e Telemetria

> **Matéria:** DevOps, Plataforma de Desenvolvimento e Engenharia de Entrega  
> **Cargo:** B02 – Técnico de Controle Externo – Especialidade: Tecnologia da Informação  
> **Arquivo:** `06_observabilidade_monitoramento_e_telemetria.md`  



---


## 📌 Ementa / Itens do Edital
- Conceitos de Monitoramento Tradicional vs. Observabilidade
- Os Quatro Sinais Dourados do Google SRE (Latência, Tráfego, Erros e Saturação)
- Os Três Pilares da Observabilidade: Métricas, Logs Estruturados e Rastreamento Distribuído (Traces)
- Padrão OpenTelemetry (OTel), instrumentação e propagação de contexto
- Engenharia de Confiabilidade de Sites (SRE): SLI, SLO, SLA e Orçamento de Erro (Error Budget)
- Métricas DORA (DevOps Research and Assessment) e gestão de incidentes

---

## 🧭 Sumário

1. [Monitoramento Tradicional vs. Observabilidade Moderna](#1-monitoramento-tradicional-vs-observabilidade-moderna)
    1. [Transição de Sintomas para Estados Internos](#11-transicao-de-sintomas-para-estados-internos)
    2. [Os Quatro Sinais Dourados do Google SRE (Four Golden Signals)](#12-os-quatro-sinais-dourados-do-google-sre-four-golden-signals)
    3. [Metodologias Complementares: USE (Brendan Gregg) e RED (Tom Wilkie)](#13-metodologias-complementares-use-brendan-gregg-e-red-tom-wilkie)
    4. [Teste 224](#Teste-224)
    5. [Teste 225](#Teste-225)
    6. [Teste 226](#Teste-226)
2. [Os Três Pilares da Observabilidade](#2-os-tres-pilares-da-observabilidade)
    1. [Métricas (Metrics) e Tipos Primários no Prometheus (Counter, Gauge, Histogram, Summary)](#21-metricas-metrics-e-tipos-primarios-no-prometheus-counter-gauge-histogram-summary)
    2. [Logs Estruturados (Structured Logging) e Pilhas de Agregação (ELK, EFK, Loki)](#22-logs-estruturados-structured-logging-e-pilhas-de-agregacao-elk-efk-loki)
    3. [Rastreamento Distribuído (Distributed Tracing): Traces, Spans e Identificadores Globais](#23-rastreamento-distribuido-distributed-tracing-traces-spans-e-identificadores-globais)
    4. [Tabela Comparativa de Propósitos e Custos dos Três Pilares](#24-tabela-comparativa-de-propositos-e-custos-dos-tres-pilares)
    5. [Teste 227](#Teste-227)
    6. [Teste 228](#Teste-228)
    7. [Teste 229](#Teste-229)
3. [O Padrão Aberto OpenTelemetry (OTel)](#3-o-padrao-aberto-opentelemetry-otel)
    1. [Arquitetura Unificada: OTel API, OTel SDK e OTel Collector](#31-arquitetura-unificada-otel-api-otel-sdk-e-otel-collector)
    2. [Propagação de Contexto W3C Trace Context (traceparent e tracestate)](#32-propagacao-de-contexto-w3c-trace-context-traceparent-e-tracestate)
    3. [Teste 230](#Teste-230)
4. [Engenharia de Confiabilidade SRE: O Triângulo SLI, SLO, SLA e Error Budgets](#4-engenharia-de-confiabilidade-sre-o-triangulo-sli-slo-sla-e-error-budgets)
    1. [Distinção Formal entre SLI, SLO e SLA](#41-distincao-formal-entre-sli-slo-e-sla)
    2. [O Orçamento de Erro (Error Budget) como Equilíbrio entre Inovação e Confiabilidade](#42-o-orcamento-de-erro-error-budget-como-equilibrio-entre-inovacao-e-confiabilidade)
    3. [Teste 231](#Teste-231)
    4. [Teste 232](#Teste-232)
5. [Métricas DORA e Desempenho Operacional em Engenharia](#5-metricas-dora-e-desempenho-operacional-em-engenharia)
    1. [As Quatro Dimensões DORA: Throughput vs. Stability](#51-as-quatro-dimensoes-dora-throughput-vs-stability)
    2. [Teste 233](#Teste-233)
6. [🌐 Fontes Oficiais e Referências Bibliográficas](#fontes-oficiais-e-referencias-bibliograficas)

---

## 1. Monitoramento Tradicional vs. Observabilidade Moderna

Em infraestruturas tradicionais monolíticas e hospedadas em datacenters físicos, a gerência de operações baseava-se em **monitoramento reativo**: checagens periódicas via ping (*heartbeats* ICMP) e disparos de alertas fundamentados em limiares estáticos (*thresholds*, ex.: disparar e-mail de alerta quando o consumo de CPU da VM ultrapassar 80%).

Com a emergência de arquiteturas distribuídas nativas em nuvem (*cloud native*), milhares de microsserviços efêmeros, orquestração de contêineres e funções serverless, essa abordagem mostrou-se insuficiente. O sistema pode estar com todos os servidores operando em 30% de CPU e, ainda assim, milhares de cidadãos enfrentarem erros HTTP 500 intermitentes devido a travamentos de conexões em banco de dados ou falhas de comunicação em malhas de rede.

```mermaid
flowchart LR
    subgraph Tradicional["Monitoramento Tradicional"]
        M_FOCO["Foco em Sintomas:<br/>'O servidor está ligado?'"]
        M_ALERTA["Alertas por Threshold Fixo:<br/>'CPU > 80% dispara alarme'"]
        M_PROBLEMA["Resolve falhas conhecidas:<br/>'Conhecidos desconhecidos'"]
        M_FOCO --> M_ALERTA --> M_PROBLEMA
    end

    subgraph Observabilidade["Observabilidade Moderna"]
        O_FOCO["Foco em Estados Internos:<br/>'Por que o usuário X recebeu erro 500?'"]
        O_EXPLORA["Investigação Ad-hoc e Multidimensional"]
        O_PROBLEMA["Depura falhas inéditas e imprevistas:<br/>'Desconhecidos desconhecidos'"]
        O_FOCO --> O_EXPLORA --> O_PROBLEMA
    end
```

### 1.1 Transição de Sintomas para Estados Internos

- **Definição Matemática e Canônica:** Originária da Teoria do Controle Linear formalizada por Rudolf E. Kálmán (1960) e consolidada na computação por Charity Majors:
  > *"Um sistema é observável se o seu estado interno puder ser integralmente inferido a partir do conhecimento de suas saídas externas expostas."*
- **A Fronteira Conceitual:**
    - **Monitoramento Tradicional:** Informa **quando** algo está quebrado (*"O sistema está fora do ar?"*). Presta-se a diagnosticar problemas previsíveis cujas causas já são familiares à equipe (*known unknowns*).
    - **Observabilidade:** Permite entender **por que** algo quebrou (*"Por que a transação do usuário X demorou 12 segundos e gerou falha na emissão da certidão?"*). Viabiliza a investigação aberta e multidimensional de problemas inéditos e imprevistos decorrentes do comportamento caótico de sistemas distribuídos (*unknown unknowns*).

### 1.2 Os Quatro Sinais Dourados do Google SRE (Four Golden Signals)

No seminal *Google Site Reliability Engineering Book*, a equipe de confiabilidade do Google catalogou os quatro pilares essenciais de telemetria para qualquer serviço voltado ao usuário:

1. **Latência (*Latency*):** O tempo decorrido para processar e responder a uma requisição.
    - **Regra de Ouro:** É imperativo **separar a latência das requisições bem-sucedidas da latência das requisições com erro**. Frequentemente, uma falha de autenticação ou erro de rota retorna imediatamente em 3 ms com código HTTP 500; agregar essa resposta rápida à média geral mascararia a lentidão real das requisições legítimas que estão demorando 4 segundos para carregar dados.

2. **Tráfego (*Traffic*):** A medição da demanda imposta ao sistema. Em serviços web e APIs REST, afere-se tipicamente pelo número de requisições HTTP por segundo (RPS); em serviços de banco de dados, pelo volume de transações por segundo (TPS); em redes de streaming, pela quantidade de conexões ativas ou vazão de dados em megabits por segundo.
3. **Erros (*Errors*):** A taxa de requisições que falharam. Divide-se em:
    - *Erros Explícitos:* Respostas com códigos de erro HTTP 5xx (500, 502, 503), timeouts de soquete ou falhas de conexão recusada.
    - *Erros Implícitos:* Requisições que retornam código HTTP 200 (OK), mas cujo conteúdo transporta uma mensagem de falha funcional (ex.: resposta com `{"status": "erro", "mensagem": "falha na comunicação com a Receita Federal"}`).

4. **Saturação (*Saturation*):** Quão "cheio" está o sistema. Mede a fração utilizada de um recurso computacional finito e restrito (ex.: percentual de ocupação da memória RAM física, esgotamento do pool de threads do Tomcat, taxa de utilização de discos SSD ou filas de espera em conexões com bancos relacionais). À medida que a saturação se aproxima de 100%, o sistema degrada subitamente seu desempenho.

> 🚨 **ALERTA DE PROVA / PEGADINHA FCC:**  
> A FCC adora cobrar os Quatro Sinais Dourados do Google SRE. Memorize a sigla **L-T-E-S**: **L**atência, **T**ráfego, **E**rros e **S**aturação.  
> As alternativas incorretas costumam substituir "Saturação" por "Segurança", "Simplicidade" ou "Sincronização" para induzir o candidato ao erro.

### 1.3 Metodologias Complementares: USE (Brendan Gregg) e RED (Tom Wilkie)

Além dos Quatro Sinais Dourados, destacam-se duas metodologias amplamente cobradas em avaliações de arquitetura:

- **Método USE (Brendan Gregg - Foco em Recursos e Infraestrutura):** Para cada recurso de hardware/sistema (CPU, disco, barramento de rede), analisa-se:
    - **U (Utilization):** Percentual médio de tempo em que o recurso esteve ocupado.
    - **S (Saturation):** Volume de trabalho pendente na fila aguardando processamento.
    - **E (Errors):** Contagem de erros de hardware ou de driver associados ao recurso.
- **Método RED (Tom Wilkie - Foco em Microsserviços e Requisições):** Adequado para avaliar serviços que processam chamadas de rede:
    - **R (Rate):** Taxa de requisições por segundo.
    - **E (Errors):** Quantidade ou taxa de requisições que falharam.
    - **D (Duration):** Duração/tempo gasto pelas requisições (latência).

---

### Teste 224
**(FCC – TCE/GO – 2009 – Analista de Controle Externo - Gestão de Conhecimento)**
Quanto maior a diversidade de dados ou registros de circulação passíveis de serem utilizados em um estudo de

* **A)** menor o esforço a ser dispendido pelos avaliadores.
* **B)** maior o índice de dúvida (ID) em relação aos resul- da. tados.
* **C)** maior a margem de erro. for baixa.
* **D)** bases de dados ocupam pouco espaço na memória dos computadores.
* **E)** apenas redes de bibliotecas podem ter bases de _________________________________________________________ dados em CD-ROM, se considerada a relação entre os custos e os benefícios.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "menor o esforço a ser dispendido pelos avaliadores". De acordo com a teoria estudada em *2.4 Tabela Comparativa de Propósitos e Custos dos Três Pilares*, métricas: "Quando e onde algo está quebrado?" — Numérica, agregada e contínua (*Time Series*). — Muito Baixo (ótima relação custo/benefício para retenção longa). — Prometheus, Datadog, InfluxDB, Grafana.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "maior o índice de dúvida (ID) em relação aos resul- da. tados". De acordo com a teoria estudada em *2.4 Tabela Comparativa de Propósitos e Custos dos Três Pilares*, pilar: Pergunta que Responde — Granularidade dos Dados — Custo de Armazenamento e Processamento — Ferramentas de Referência.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "maior a margem de erro. for baixa". De acordo com a teoria estudada em *4.2 O Orçamento de Erro (Error Budget) como Equilíbrio entre Inovação e Confiabilidade*, o Error Budget é definido matematicamente como a margem de falha tolerada pelo SLO.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "bases de dados ocupam pouco espaço na memória dos computadores". De acordo com a teoria estudada em *2.1 Métricas (Metrics) e Tipos Primários no Prometheus (Counter, Gauge, Histogram, Summary)*, usado para representar o estado momentâneo de um recurso variável: quantidade de memória RAM livre em bytes, temperatura da CPU, número de conexões ativas no pool do banco de dados ou contagem de réplicas de Pods rodando.
> - **E)** **Correta.** Conforme fundamentado na seção *1.2 Os Quatro Sinais Dourados do Google SRE (Four Golden Signals)* deste guia, em serviços web e APIs REST, afere-se tipicamente pelo número de requisições HTTP por segundo (RPS); em serviços de banco de dados, pelo volume de transações por segundo (TPS); em redes de streaming, pela quantidade de conexões ativas ou vazão de dados em megabits por segundo. Dessa forma, está plenamente correta a assertiva da banca (FCC – TCE/GO/2009) ao estabelecer que "apenas redes de bibliotecas podem ter bases de _________________________________________________________ dados em...".
>
> **Gabarito: E**

---

### Teste 225
**(FGV – TJ/RR – 2024 – Analista Judiciario Gestao E Governanca De Tecnologia Da Informacao)**
Com relação aos tipos de redes de computadores e suas arquiteturas, considere as afirmativas a seguir. I. Uma rede LAN e uma rede WAN se diferenciam apenas pelo fato de a WAN ser uma rede sem fio. II. As WAN costumam usar meios físicos apropriados para longas distâncias, como fibras óticas, pois os enlaces entre dois nós podem ter que cobrir distâncias grandes. III. A topologia em estrela minimiza o tamanho do cabeamento necessário em uma rede de mais de 8 nós regularmente espaçados pela área de uma WAN. Está correto o que se afirma em

* **A)** I, apenas.
* **B)** II, apenas.
* **C)** III, apenas.
* **D)** I e II, apenas.
* **E)** II e III, apenas.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I, apenas". De acordo com a teoria estudada em *1. Monitoramento Tradicional vs. Observabilidade Moderna*, em infraestruturas tradicionais monolíticas e hospedadas em datacenters físicos, a gerência de operações baseava-se em monitoramento reativo: checagens periódicas via ping (*heartbeats* ICMP) e disparos de alertas fundamentados em limiares estáticos (*thresholds*, ex.: disparar e-mail de alerta quando o consumo de CPU da VM ultrapassar 80%).
> - **B)** **Correta.** Conforme fundamentado na seção *2.1 Métricas (Metrics) e Tipos Primários no Prometheus (Counter, Gauge, Histogram, Summary)* deste guia, amostra observações (geralmente latências de requisições ou tamanhos de payloads) e as conta em baldes de tamanho configurável (*buckets*). Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/RR/2024) ao estabelecer que "II, apenas".
> - **C)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "III, apenas". De acordo com a teoria estudada em *1.1 Transição de Sintomas para Estados Internos*, *"Um sistema é observável se o seu estado interno puder ser integralmente inferido a partir do conhecimento de suas saídas externas expostas."*.
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e II, apenas". De acordo com a teoria estudada em *1.2 Os Quatro Sinais Dourados do Google SRE (Four Golden Signals)*, em serviços web e APIs REST, afere-se tipicamente pelo número de requisições HTTP por segundo (RPS); em serviços de banco de dados, pelo volume de transações por segundo (TPS); em redes de streaming, pela quantidade de conexões ativas ou vazão de dados em megabits por segundo.
> - **E)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "II e III, apenas". De acordo com a teoria estudada em *1.2 Os Quatro Sinais Dourados do Google SRE (Four Golden Signals)*, as alternativas incorretas costumam substituir "Saturação" por "Segurança", "Simplicidade" ou "Sincronização" para induzir o candidato ao erro.
>
> **Gabarito: B**

---

### Teste 226
**(FCC – TRT 13ª – 2014 – Analista Judiciário - Tecnologia da Informação)**
É sabido que um dos motivantes para a proposição do IPv6 para substituir o IPv4 foi a capacidade limitada de endereçamento do IPv4. Entretanto, e aproveitando a oportunidade para melhorar a funcionalidade do protocolo IP, outros recursos foram modificados ou introduzidos no IPv6. Dentre eles,

* **A)** a introdução do recurso de QoS (Qualidade de Serviço) utilizando o campo Flow Label.
* **B)** o uso do ARP incorporado no campo EXT do cabeçalho IPv6.
* **C)** a redução do tamanho dos fragmentos dos pacotes para minimizar os erros de transmissão.
* **D)** a incorporação do serviço TCP para fragmentar os pacotes no roteador.
* **E)** o uso de endereços Broadcast ao invés de Multicast para aumentar a eficiência.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *4.1 Distinção Formal entre SLI, SLO e SLA* deste guia, define o nível de qualidade que o serviço deve manter para que os usuários finais estejam plenamente satisfeitos. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 13ª/2014) ao estabelecer que "a introdução do recurso de QoS (Qualidade de Serviço) utilizando o campo Flow Label".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "o uso do ARP incorporado no campo EXT do cabeçalho IPv6". De acordo com a teoria estudada em *2.4 Tabela Comparativa de Propósitos e Custos dos Três Pilares*, traces: "Qual serviço no fluxo causou o atraso ou falha?" — Grafo hierárquico causal de transação distribuída. — Médio (requer uso de amostragem/*sampling* em alta escala). — Jaeger, Zipkin, OpenTelemetry.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "a redução do tamanho dos fragmentos dos pacotes para minimizar os erros de transmissão". De acordo com a teoria estudada em *1.2 Os Quatro Sinais Dourados do Google SRE (Four Golden Signals)*, mede a fração utilizada de um recurso computacional finito e restrito (ex.: percentual de ocupação da memória RAM física, esgotamento do pool de threads do Tomcat, taxa de utilização de discos SSD ou filas de espera em conexões com bancos relacionais). À medida que a saturação se aproxima de 100%, o sistema degrada subitamente seu desempenho.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "a incorporação do serviço TCP para fragmentar os pacotes no roteador". De acordo com a teoria estudada em *2.1 Métricas (Metrics) e Tipos Primários no Prometheus (Counter, Gauge, Histogram, Summary)*, usado para representar o estado momentâneo de um recurso variável: quantidade de memória RAM livre em bytes, temperatura da CPU, número de conexões ativas no pool do banco de dados ou contagem de réplicas de Pods rodando.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "o uso de endereços Broadcast ao invés de Multicast para aumentar a eficiência". De acordo com a teoria estudada em *4. Engenharia de Confiabilidade SRE: O Triângulo SLI, SLO, SLA e Error Budgets*, o modelo de confiabilidade do Google SRE substitui debates subjetivos sobre qualidade por acordos matemáticos e operacionais claros.
>
> **Gabarito: A**

---

## 2. Os Três Pilares da Observabilidade

A observabilidade moderna estrutura-se sobre a convergência de três tipos de dados de telemetria independentes, porém rigorosamente complementares: **Métricas, Logs e Rastreamento Distribuído (*Traces*)**.

```mermaid
flowchart TD
    subgraph Pilares["Os Três Pilares da Observabilidade"]
        METRICS["1. Métricas (Prometheus)<br/>- Séries temporais numéricas agregadas<br/>- Pergunta: 'QUANDO e ONDE algo está quebrado?'<br/>- Custo: Baixo e rápido"]
        TRACES["3. Traces (Jaeger / OTel)<br/>- Jornada causal distribuída (Spans)<br/>- Pergunta: 'QUAL microsserviço causou a lentidão?'<br/>- Custo: Médio"]
        LOGS["2. Logs (Elasticsearch / Loki)<br/>- Registros textuais detalhados com timestamp<br/>- Pergunta: 'POR QUE exatamente a falha aconteceu?'<br/>- Custo: Alto armazenamento"]
        
        METRICS -.->|Alerta disparado| TRACES
        TRACES -.->|Span ID correlacionado| LOGS
    end
```

### 2.1 Métricas (Metrics) e Tipos Primários no Prometheus (Counter, Gauge, Histogram, Summary)

As **métricas** são valores numéricos atômicos agregados ao longo do tempo (*Time Series*), enriquecidos com pares chave-valor denominados rótulos (*labels*). Exemplo no Prometheus: `http_requests_total{method="POST", handler="/pagamento", status="500"}`.

O modelo de dados do **Prometheus** (padrão ouro para Kubernetes) estabelece quatro tipos canônicos de métricas:

1. **Counter (Contador):**
    - É uma métrica cumulativa monotônica cujo valor **apenas sobe** (ou é reiniciado em zero quando a aplicação reinicia).
    - **Nunca decresce** sob condições normais de operação.
    - Usado para contar o número total de requisições atendidas, o total de erros registrados ou bytes transmitidos. No PromQL, utiliza-se a função `rate(http_requests_total[5m])` para derivar a taxa de requisições por segundo.

2. **Gauge (Medidor):**
    - É um valor numérico instantâneo que **pode subir e descer livremente** ao longo do tempo.
    - Usado para representar o estado momentâneo de um recurso variável: quantidade de memória RAM livre em bytes, temperatura da CPU, número de conexões ativas no pool do banco de dados ou contagem de réplicas de Pods rodando.

3. **Histogram (Histograma):**
    - Amostra observações (geralmente latências de requisições ou tamanhos de payloads) e as conta em **baldes de tamanho configurável (*buckets*)**.
    - Expõe automaticamente métricas auxiliares: contagem total de observações (`_count`) e soma total dos valores (`_sum`).
    - É a estrutura fundamental para calcular estatisticamente os **percentis de latência ($p50, p90, p95, p99$)** no lado do servidor com a função `histogram_quantile()`.

4. **Summary (Sumário):**
    - Semelhante ao histograma, mas calcula os percentis diretamente na própria aplicação instrumentada (no cliente) sobre uma janela de tempo deslizante, expondo os quantis já prontos. Não permite agregação matemática de percentis entre múltiplas instâncias no servidor.

### 2.2 Logs Estruturados (Structured Logging) e Pilhas de Agregação (ELK, EFK, Loki)

Os **logs** são registros textuais cronológicos e imutáveis de eventos discretos que ocorreram em um ponto específico no tempo dentro de uma aplicação:

- **A Importância dos Logs Estruturados em JSON:** Em vez de emitir strings desordenadas (`[INFO] O usuario 123 logou`), as aplicações modernas devem emitir logs estruturados em objetos JSON:

```json
{
  "timestamp": "2027-04-15T14:32:00.123Z",
  "level": "ERROR",
  "service": "auditoria-fiscal",
  "message": "Falha na comunicacao com base de dados tributaria",
  "user_id": "usr-8891",
  "trace_id": "4bf92f3577b34da6a3ce929d0e0e4736",
  "span_id": "00f067aa0ba902b7",
  "error_details": "ConnectionTimeoutException: database unreachable"
}
```

  A inclusão de campos como `trace_id` viabiliza a correlação cruzada imediata entre o log e o rastreamento distribuído correspondente.

- **Pilhas de Agregação de Logs:**
    - **Stack ELK (Elasticsearch, Logstash, Kibana):** O Logstash coleta e processa os logs; o Elasticsearch atua como mecanismo de busca e indexação distribuída em texto integral; o Kibana provê os dashboards visuais de consulta.
    - **Stack EFK (Elasticsearch, Fluentd/Fluent Bit, Kibana):** Substitui o Logstash pelo **Fluent Bit** (leitor de logs levíssimo em C instalado como `DaemonSet` em cada nó do Kubernetes) para enviar os logs dos contêineres para o Elasticsearch.
    - **Grafana Loki:** Abordagem moderna e econômica inspirada no Prometheus. Em vez de indexar o texto integral de cada log (o que consome gigabytes de RAM e disco), o Loki indexa apenas os metadados e rótulos (*labels*), armazenando o texto comprimido em buckets de armazenamento de objetos (como Amazon S3 ou MinIO).

### 2.3 Rastreamento Distribuído (Distributed Tracing): Traces, Spans e Identificadores Globais

Em arquiteturas de microsserviços, uma única ação do usuário desencadeia uma cascata de dezenas de chamadas assíncronas entre serviços distribuídos. O **Rastreamento Distribuído (*Distributed Tracing*)** reconstrói o grafo causal e temporal de ponta a ponta dessa transação.

```mermaid
flowchart TD
    subgraph DistributedTrace["Anatomia de um Trace (Trace ID: a1b2c3d4)"]
        SPAN1["Span Raiz: Frontend Gateway (Duração: 220ms)"]
        SPAN2["Span Filho A: Auth Service (Duração: 40ms)"]
        SPAN3["Span Filho B: Auditoria Service (Duração: 160ms)"]
        SPAN4["Span Neto: Consulta PostgreSQL (Duração: 130ms - Gargalo!)"]
        
        SPAN1 --> SPAN2
        SPAN1 --> SPAN3
        SPAN3 --> SPAN4
    end
```

- **Trace (Rastreio):** O grafo acíclico direcionado completo da jornada de uma requisição pelo ecossistema de software. É identificado por um identificador global único chamado **`Trace ID`** (número hexadecimal de 128 bits).
- **Span (Segmento):** A unidade atômica básica de trabalho executada por um serviço individual durante o processamento do Trace. Um Span encapsula:
    - **`Span ID`:** Identificador único daquela operação local (64 bits);
    - **`Parent Span ID`:** O identificador do Span que o invocou (se for o primeiro da cadeia, é o *Root Span*);
    - **Timestamps:** Horário exato de início e fim da operação (permitindo calcular a duração e latência);
    - **Tags / Atributos:** Metadados estruturados (ex.: `http.method: POST`, `db.statement: SELECT * FROM notas_fiscais`);
    - **Eventos:** Anotações temporais com mensagens ou erros de exceção ocorridos durante a execução do span.

### 2.4 Tabela Comparativa de Propósitos e Custos dos Três Pilares

| Pilar | Pergunta que Responde | Granularidade dos Dados | Custo de Armazenamento e Processamento | Ferramentas de Referência |
| :--- | :--- | :--- | :--- | :--- |
| **Métricas** | **"Quando e onde algo está quebrado?"** | Numérica, agregada e contínua (*Time Series*). | **Muito Baixo** (ótima relação custo/benefício para retenção longa). | Prometheus, Datadog, InfluxDB, Grafana |
| **Logs** | **"Por que exatamente o erro aconteceu?"** | Textual individualizada por evento discreto. | **Muito Alto** (exige compressão e descarte programado por TTL). | Stack ELK, Fluent Bit, Grafana Loki |
| **Traces** | **"Qual serviço no fluxo causou o atraso ou falha?"** | Grafo hierárquico causal de transação distribuída. | **Médio** (requer uso de amostragem/*sampling* em alta escala). | Jaeger, Zipkin, OpenTelemetry |

---

### Teste 227
**(FGV – TJ/RR – 2024 – Analista Judiciario Gestao E Governanca De Tecnologia Da Informacao)**
Em relação aos eventos e aos artefatos do framework Scrum, analise as afirmativas a seguir. I. O backlog do produto é um documento preenchido antes do início do projeto e que não sofre alterações mesmo que os desejos do cliente mudem ao longo do tempo. II. A reunião diária, daily Scrum, é um evento de curta duração que permite identificar impedimentos, melhorar as comunicações, promover rápida tomada de decisões e reduzir a necessidade de outras reuniões ao longo do dia. III. A reunião de revisão da Sprint é um evento em que são definidas as histórias de usuário que serão trabalhadas naquela Sprint. Está correto o que se afirma em

* **A)** I, apenas.
* **B)** II, apenas.
* **C)** III, apenas.
* **D)** I e II, apenas.
* **E)** II e III, apenas.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I, apenas". De acordo com a teoria estudada em *2.1 Métricas (Metrics) e Tipos Primários no Prometheus (Counter, Gauge, Histogram, Summary)*, semelhante ao histograma, mas calcula os percentis diretamente na própria aplicação instrumentada (no cliente) sobre uma janela de tempo deslizante, expondo os quantis já prontos.
> - **B)** **Correta.** Conforme fundamentado na seção *2.3 Rastreamento Distribuído (Distributed Tracing): Traces, Spans e Identificadores Globais* deste guia, timestamps: Horário exato de início e fim da operação (permitindo calcular a duração e latência). Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/RR/2024) ao estabelecer que "II, apenas".
> - **C)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "III, apenas". De acordo com a teoria estudada em *2.1 Métricas (Metrics) e Tipos Primários no Prometheus (Counter, Gauge, Histogram, Summary)*, as métricas são valores numéricos atômicos agregados ao longo do tempo (*Time Series*), enriquecidos com pares chave-valor denominados rótulos (*labels*). Exemplo no Prometheus: `http_requests_total{method="POST", handler="/pagamento", status="500"}`.
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e II, apenas". De acordo com a teoria estudada em *2.1 Métricas (Metrics) e Tipos Primários no Prometheus (Counter, Gauge, Histogram, Summary)*, é um valor numérico instantâneo que pode subir e descer livremente ao longo do tempo.
> - **E)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "II e III, apenas". De acordo com a teoria estudada em *4.1 Distinção Formal entre SLI, SLO e SLA*, essa diferença matemática cria uma zona de amortecimento (*buffer de segurança*) que permite à equipe técnica detectar falhas, agir e restaurar o serviço antes que o descumprimento atinja o limite do SLA e gere multas financeiras para a organização.
>
> **Gabarito: B**

---

### Teste 228
**(FCC – TRT 23ª – 2016 – Analista Judiciário - Apoio Especializado - Tecnologia da Informação)**
Considere o texto a seguir: Em computadores baseados na arquitetura de Von Neumann, assim que a instrução que vai ser executada é buscada da memória principal para a CPU, o sistema efetiva automaticamente a modificação do conteúdo desse registrador de modo que ele passe a armazenar o endereço da próxima instrução na sequência, sendo crucial para o processo de controle e de sequenciamento da execução dos programas. O texto se refere ao registrador conhecido como

* **A)** Registrador de Dados de Memória − RDM.
* **B)** Registrador de Decodificação de Instruções − RDI.
* **C)** Contador de Instruções − CI.
* **D)** Registrador de Endereçamento de Instruções − REI.
* **E)** Registrador de Instruções − RI.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Registrador de Dados de Memória − RDM". De acordo com a teoria estudada em *2.1 Métricas (Metrics) e Tipos Primários no Prometheus (Counter, Gauge, Histogram, Summary)*, usado para representar o estado momentâneo de um recurso variável: quantidade de memória RAM livre em bytes, temperatura da CPU, número de conexões ativas no pool do banco de dados ou contagem de réplicas de Pods rodando.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Registrador de Decodificação de Instruções − RDI". De acordo com a teoria estudada em *1.1 Transição de Sintomas para Estados Internos*, *"Um sistema é observável se o seu estado interno puder ser integralmente inferido a partir do conhecimento de suas saídas externas expostas."*.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Contador de Instruções − CI". De acordo com a teoria estudada em *1.2 Os Quatro Sinais Dourados do Google SRE (Four Golden Signals)*, mede a fração utilizada de um recurso computacional finito e restrito (ex.: percentual de ocupação da memória RAM física, esgotamento do pool de threads do Tomcat, taxa de utilização de discos SSD ou filas de espera em conexões com bancos relacionais). À medida que a saturação se aproxima de 100%, o sistema degrada subitamente seu desempenho.
> - **D)** **Correta.** Conforme fundamentado na seção *1. Monitoramento Tradicional vs. Observabilidade Moderna* deste guia, o sistema pode estar com todos os servidores operando em 30% de CPU e, ainda assim, milhares de cidadãos enfrentarem erros HTTP 500 intermitentes devido a travamentos de conexões em banco de dados ou falhas de comunicação em malhas de rede. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 23ª/2016) ao estabelecer que "Registrador de Endereçamento de Instruções − REI".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Registrador de Instruções − RI". De acordo com a teoria estudada em *2.1 Métricas (Metrics) e Tipos Primários no Prometheus (Counter, Gauge, Histogram, Summary)*, expõe automaticamente métricas auxiliares: contagem total de observações (`_count`) e soma total dos valores (`_sum`).
>
> **Gabarito: D**

---

### Teste 229
**(FGV – TRT 16ª – 2022 – Analista Judiciário (Área Administrativa - Tecnologia da Informação))**
Os firewalls podem ser um meio eficaz de proteger sistemas e redes contra ameaças de segurança. Com relação às suas limitações, analise os itens a seguir. I. Não são capazes de proteger contra os ataques que contornam o firewall. II. Não protegem contra ameaças internas, como funcionários insatisfeitos ou que cooperam com um atacante externo. III. Não protegem contra a transferência de programas ou arquivos infectados com vírus. Está correto o que se afirma em

* **A)** I, apenas.
* **B)** II, apenas.
* **C)** III, apenas.
* **D)** I, II e III.
* **E)** II e III, apenas.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I, apenas". De acordo com a teoria estudada em *1.1 Transição de Sintomas para Estados Internos*, *"Um sistema é observável se o seu estado interno puder ser integralmente inferido a partir do conhecimento de suas saídas externas expostas."*.
> - **B)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "II, apenas". De acordo com a teoria estudada em *1.1 Transição de Sintomas para Estados Internos*, viabiliza a investigação aberta e multidimensional de problemas inéditos e imprevistos decorrentes do comportamento caótico de sistemas distribuídos (*unknown unknowns*).
> - **C)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "III, apenas". De acordo com a teoria estudada em *1.2 Os Quatro Sinais Dourados do Google SRE (Four Golden Signals)*, em serviços web e APIs REST, afere-se tipicamente pelo número de requisições HTTP por segundo (RPS); em serviços de banco de dados, pelo volume de transações por segundo (TPS); em redes de streaming, pela quantidade de conexões ativas ou vazão de dados em megabits por segundo.
> - **D)** **Correta.** Conforme fundamentado na seção *2.4 Tabela Comparativa de Propósitos e Custos dos Três Pilares* deste guia, métricas: "Quando e onde algo está quebrado?" — Numérica, agregada e contínua (*Time Series*). — Muito Baixo (ótima relação custo/benefício para retenção longa). — Prometheus, Datadog, InfluxDB, Grafana. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT 16ª/2022) ao estabelecer que "I, II e III".
> - **E)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "II e III, apenas". De acordo com a teoria estudada em *3.1 Arquitetura Unificada: OTel API, OTel SDK e OTel Collector*, o código da aplicação instrumentado contra a API OTel não depende de nenhum backend específico e compila sem referenciar ferramentas de terceiros.
>
> **Gabarito: D**

---

## 3. O Padrão Aberto OpenTelemetry (OTel)

Historicamente, as equipes de TI ficavam presas a bibliotecas proprietárias de telemetria específicas de cada fabricante (*Vendor Lock-in*). Para sanar essa fragmentação, a CNCF fundiu os projetos abertos *OpenTracing* e *OpenCensus*, criando o **OpenTelemetry (OTel)** como o padrão aberto e unificado da indústria para instrumentação de software.

```mermaid
flowchart LR
    subgraph OTelCollector["Arquitetura do OpenTelemetry Collector"]
        APP["Aplicação Instrumentada (SDK)"] -->|"OTLP / HTTP / gRPC"| REC["Receivers<br/>(Recebem dados)"]
        REC --> PROC["Processors<br/>(Batch, Filtro, Redação PII)"]
        PROC --> EXP["Exporters<br/>(Exportam em formatos específicos)"]
        
        EXP --> PROM["Prometheus (Métricas)"]
        EXP --> JAEGER["Jaeger (Traces)"]
        EXP --> LOKI["Loki (Logs)"]
    end
```

### 3.1 Arquitetura Unificada: OTel API, OTel SDK e OTel Collector

O ecossistema OpenTelemetry organiza-se em três camadas estritamente desacopladas:

1. **OTel API:** A camada de abstração com a qual o código da aplicação interage. Define as interfaces para criar métricas, traces e logs. O código da aplicação instrumentado contra a API OTel **não depende de nenhum backend específico** e compila sem referenciar ferramentas de terceiros.
2. **OTel SDK:** A implementação concreta da API. Gerencia filas de memória, suporte a amostragem (*sampling*), empacotamento em lotes e conversão dos dados de telemetria no protocolo nativo **OTLP (*OpenTelemetry Protocol*)** via gRPC ou HTTP.
3. **OTel Collector:** Um serviço proxy independente que atua como centralizador de telemetria. É composto por um pipeline de três estágios lineares:
    - **Receivers:** Portas de entrada configuráveis que recebem dados de telemetria em múltiplos protocolos (OTLP, Jaeger, Zipkin, Prometheus).
    - **Processors:** Tratam os dados em trânsito (agrupamento em lotes para economia de rede, amostragem estatística, filtragem de métricas e **ofuscação/redação de dados sensíveis e PII** protegidos pela LGPD).
    - **Exporters:** Traduzem e despacham a telemetria processada para os destinos de persistência configurados (Prometheus para métricas, Jaeger para traces, Elasticsearch para logs).

### 3.2 Propagação de Contexto W3C Trace Context (traceparent e tracestate)

Para que o `Trace ID` seja preservado quando uma chamada cruza a fronteira de um microsserviço para outro via HTTP ou filas de mensageria, o OpenTelemetry utiliza a especificação padronizada **W3C Trace Context**:

- **Cabeçalho `traceparent`:** Estrutura compacta transmitida na requisição:
  `traceparent: 00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01`
    - `00`: Versão da especificação W3C.
    - `4bf92f3577b34da6a3ce929d0e0e4736`: O **`Trace ID`** global compartilhado por todos os serviços.
    - `00f067aa0ba902b7`: O **`Parent Span ID`** da operação que originou o disparo.
    - `01`: Flags de rastreamento (onde `01` indica que a requisição foi selecionada para amostragem/gravação).

---

### Teste 230
**(CEBRASPE – STF – 2013 – Analista Judiciario Suporte Em Tecnologia Da Informacao)**
Ataques de negação de serviço distribuído com base em HTTP devem ser mitigados em firewall de camada de aplicação. Nesse caso, se for utilizado o protocolo HTTPS, a mitigação não será possível porque os dados trafegados são cifrados.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Incorreta.** A marcação como **Certo** não procede, pois o enunciado apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Ataques de negação de serviço distribuído com base em HTTP devem ser mitigados em firewall de camada de...". De acordo com a teoria estudada em *3.1 Arquitetura Unificada: OTel API, OTel SDK e OTel Collector*, oTel API: A camada de abstração com a qual o código da aplicação interage. Define as interfaces para criar métricas, traces e logs.
> - **E)** **Correta.** O item está **Errado** (gabarito oficial: **E**). Conforme fundamentado na seção *3.1 Arquitetura Unificada: OTel API, OTel SDK e OTel Collector* deste guia, oTel SDK: A implementação concreta da API. Gerencia filas de memória, suporte a amostragem (*sampling*), empacotamento em lotes e conversão dos dados de telemetria no protocolo nativo OTLP (*OpenTelemetry Protocol*) via gRPC ou HTTP. Portanto, a assertiva examinada pela banca (CEBRASPE – STF/2013) viola os preceitos técnicos do tópico.
>
> **Gabarito: E**

---

## 4. Engenharia de Confiabilidade SRE: O Triângulo SLI, SLO, SLA e Error Budgets

O modelo de confiabilidade do Google SRE substitui debates subjetivos sobre qualidade por acordos matemáticos e operacionais claros.

```mermaid
flowchart TD
    subgraph Triangulo_SRE["Hierarquia de Confiabilidade SRE"]
        SLI["SLI (Service Level Indicator)<br/>Medição Real Empírica: 'Hoje a taxa de sucesso é 99,94%'"]
        SLO["SLO (Service Level Objective)<br/>Meta Interna da Engenharia: 'Queremos atingir >= 99,90% ao mês'"]
        SLA["SLA (Service Level Agreement)<br/>Contrato Legal com Cliente: 'Se cair abaixo de 99,50%, pagamos multa'"]
        EB["Error Budget (Orçamento de Erro)<br/>Margem Aceitável: 100% - SLO (Neste caso: 0,10%)"]
        
        SLI --> SLO
        SLO --> SLA
        SLO -.-> EB
    end
```

### 4.1 Distinção Formal entre SLI, SLO e SLA

1. **SLI (*Service Level Indicator* - Indicador de Nível de Serviço):**
    - É a **medida quantitativa real e empírica observada em produção em tempo real**.
    - É calculado como uma razão percentual de eventos aceitáveis sobre o total de eventos válidos:
     $$\text{SLI} = \frac{\text{Número de Requisições com Sucesso (Status < 500)}}{\text{Total de Requisições Válidas}} \times 100\%$$
    - *Exemplo:* "Nas últimas 24 horas, o SLI de disponibilidade medido foi de 99,94%".

2. **SLO (*Service Level Objective* - Objetivo de Nível de Serviço):**
    - É a **meta interna almejada pela equipe de engenharia e operações**.
    - Define o nível de qualidade que o serviço deve manter para que os usuários finais estejam plenamente satisfeitos.
    - *Exemplo:* "Nosso SLO é que 99,90% das requisições respondam em menos de 300 ms em qualquer janela móvel de 30 dias".

3. **SLA (*Service Level Agreement* - Acordo de Nível de Serviço):**
    - É o **contrato formal, jurídico ou comercial celebrado com os clientes externos ou cidadãos**.
    - Estabelece as obrigações do provedor e as **consequências formais (penalidades financeiras, ressarcimentos ou sanções contratuais)** caso o nível de serviço seja violado.

> ⭐ **REGRA DE OURO DA FCC / RELAÇÃO ENTRE SLO E SLA:**  
> O **SLA é sempre MAIS TOLERANTE (menos restritivo) que o SLO interno**!  
> Exemplo clássico:  
>
> - **SLO interno da engenharia:** $99{,}9\%$ de disponibilidade.  
> - **SLA comercial do contrato:** $99{,}5\%$ de disponibilidade.  
> Essa diferença matemática cria uma zona de amortecimento (*buffer de segurança*) que permite à equipe técnica detectar falhas, agir e restaurar o serviço antes que o descumprimento atinja o limite do SLA e gere multas financeiras para a organização.

### 4.2 O Orçamento de Erro (Error Budget) como Equilíbrio entre Inovação e Confiabilidade

O conceito mais transformador do SRE é o **Orçamento de Erro (*Error Budget*)**:

- Parte do princípio de que **100% de disponibilidade é um objetivo equivocado e economicamente inviável**. Exigir 100% paralisa a capacidade da equipe de inovar e lançar novas funcionalidades, pois qualquer deploy carrega risco residual.
- O Error Budget é definido matematicamente como a margem de falha tolerada pelo SLO:
  $$\text{Error Budget} = 100\% - \text{SLO}$$
    - Se o SLO estabelecido é de $99{,}9\%$ ao mês, o Orçamento de Erro é de $0{,}1\%$.

**A Política Operacional de Conflito Dev vs. Ops:**

- **Saldo Positivo no Error Budget:** A equipe de desenvolvimento possui "crédito de risco" para acelerar deploys, experimentar novas funcionalidades e aceitar pequenos incidentes controlados.
- **Orçamento de Erro Esgotado (Saldo Zerado ou Negativo):** Quando incidentes recentes consomem todo o orçamento de erro daquele mês, **todos os novos lançamentos de funcionalidades são compulsoriamente suspensos (*freeze de inovação*)**. A equipe de engenharia inteira é mobilizada para trabalhar em confiabilidade: refatoração de código frágil, automação de testes, melhorias de observabilidade e fortalecimento de pipelines, até que o sistema recupere sua margem de estabilidade.

---

### Teste 231
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Administrativa - Engenharia Civil)**
Com base na Lei nº 14.133/2021, avalie se as afirmativas a seguir são verdadeiras (V) ou falsas (F). ( ) A licitação é inexigível quando for inviável a competição, nos casos em que os serviços só possam ser fornecidos por um produtor. ( ) No caso de obras e serviços de engenharia , o limite estabelecido para dispensa de licitação em obras de engenharia é de R$200mil. ( ) A licitação pode ser dispensada em contratações que tenham como objeto produtos para pesquisa e desenvolvimento, respeitado o limite estabelecido por lei. As afirmativas são, respectivamente,

* **A)** F – V – F.
* **B)** F – V – V.
* **C)** V – V – F.
* **D)** V – F – F.
* **E)** V – F – V.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "F – V – F". De acordo com a teoria estudada em *4.1 Distinção Formal entre SLI, SLO e SLA*, essa diferença matemática cria uma zona de amortecimento (*buffer de segurança*) que permite à equipe técnica detectar falhas, agir e restaurar o serviço antes que o descumprimento atinja o limite do SLA e gere multas financeiras para a organização.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "F – V – V". De acordo com a teoria estudada em *4.2 O Orçamento de Erro (Error Budget) como Equilíbrio entre Inovação e Confiabilidade*, parte do princípio de que 100% de disponibilidade é um objetivo equivocado e economicamente inviável. Exigir 100% paralisa a capacidade da equipe de inovar e lançar novas funcionalidades, pois qualquer deploy carrega risco residual.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "V – V – F". De acordo com a teoria estudada em *4.2 O Orçamento de Erro (Error Budget) como Equilíbrio entre Inovação e Confiabilidade*, se o SLO estabelecido é de $99{,}9\%$ ao mês, o Orçamento de Erro é de $0{,}1\%$.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "V – F – F". De acordo com a teoria estudada em *4.2 O Orçamento de Erro (Error Budget) como Equilíbrio entre Inovação e Confiabilidade*, saldo Positivo no Error Budget: A equipe de desenvolvimento possui "crédito de risco" para acelerar deploys, experimentar novas funcionalidades e aceitar pequenos incidentes controlados.
> - **E)** **Correta.** Conforme fundamentado na seção *4.1 Distinção Formal entre SLI, SLO e SLA* deste guia, estabelece as obrigações do provedor e as consequências formais (penalidades financeiras, ressarcimentos ou sanções contratuais) caso o nível de serviço seja violado. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "V – F – V".
>
> **Gabarito: E**

---

### Teste 232
**(FGV – TRF/1 – 2024 – Analista Judiciario Area Apoio Especializado Especialidade Suporte Em Tecnologia Da Informacao)**
A analista Paula foi designada como responsável por um projeto com as seguintes características: inovação, alto grau de incerteza, não ter sido realizado nenhum outro similar em seu órgão e provavelmente passar por muitas mudanças durante o processo. Considerando essas características do projeto, Paula decidiu pela abordagem ágil usando o framework Scrum. A atividade empregada pelo framework Scrum que Paula deve utilizar, para tratar a alta incerteza do projeto, é:

* **A)** realização de sprints;
* **B)** manutenção da declaração de escopo;
* **C)** confecção de documentação abrangente;
* **D)** revisões periódicas de processos e ferramentas;
* **E)** acompanhamento permanente da equipe de desenvolvimento.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *4.1 Distinção Formal entre SLI, SLO e SLA* deste guia, define o nível de qualidade que o serviço deve manter para que os usuários finais estejam plenamente satisfeitos. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRF/1/2024) ao estabelecer que "realização de sprints".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "manutenção da declaração de escopo". De acordo com a teoria estudada em *2.4 Tabela Comparativa de Propósitos e Custos dos Três Pilares*, logs: "Por que exatamente o erro aconteceu?" — Textual individualizada por evento discreto. — Muito Alto (exige compressão e descarte programado por TTL). — Stack ELK, Fluent Bit, Grafana Loki.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "confecção de documentação abrangente". De acordo com a teoria estudada em *3.1 Arquitetura Unificada: OTel API, OTel SDK e OTel Collector*, o código da aplicação instrumentado contra a API OTel não depende de nenhum backend específico e compila sem referenciar ferramentas de terceiros.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "revisões periódicas de processos e ferramentas". De acordo com a teoria estudada em *1. Monitoramento Tradicional vs. Observabilidade Moderna*, em infraestruturas tradicionais monolíticas e hospedadas em datacenters físicos, a gerência de operações baseava-se em monitoramento reativo: checagens periódicas via ping (*heartbeats* ICMP) e disparos de alertas fundamentados em limiares estáticos (*thresholds*, ex.: disparar e-mail de alerta quando o consumo de CPU da VM ultrapassar 80%).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "acompanhamento permanente da equipe de desenvolvimento". De acordo com a teoria estudada em *4.2 O Orçamento de Erro (Error Budget) como Equilíbrio entre Inovação e Confiabilidade*, saldo Positivo no Error Budget: A equipe de desenvolvimento possui "crédito de risco" para acelerar deploys, experimentar novas funcionalidades e aceitar pequenos incidentes controlados.
>
> **Gabarito: A**

---

## 5. Métricas DORA e Desempenho Operacional em Engenharia

Desenvolvido pelo grupo *DevOps Research and Assessment* (DORA / Google Cloud), este framework científico consolidou os quatro indicadores universais para avaliar o desempenho de entrega e estabilidade de software:

### 5.1 As Quatro Dimensões DORA: Throughput vs. Stability

| Métrica DORA | Eixo Operacional | O que ela Mede | Nível de Alta Performance (Elite) |
| :--- | :--- | :--- | :--- |
| **Deployment Frequency (DF)** | **Velocidade (*Throughput*)** | Com que frequência a organização implanta com sucesso alterações em produção. | **Múltiplos deploys por dia** (sob demanda contínua). |
| **Lead Time for Changes (LTTC)** | **Velocidade (*Throughput*)** | O tempo transcorrido desde o primeiro commit no controle de versão até a entrada efetiva em produção. | **Menos de 1 hora**. |
| **Change Failure Rate (CFR)** | **Estabilidade (*Stability*)** | O percentual de implantações em produção que resultam em falha operacional imediata (exigindo hotfix ou rollback). | **0% a 15%** de falhas. |
| **Time to Restore Service (MTTR)** | **Estabilidade (*Stability*)** | O tempo médio decorrido para restabelecer a operação plena quando ocorre uma degradação ou indisponibilidade em produção. | **Menos de 1 hora**. |

---

### Teste 233
**(CEBRASPE – TRT/10 – 2013 – Analista Judiciario Tecnologia Da Informacao)**
A engenharia de software engloba processos, métodos e ferramentas. Um de seus focos é a produção de software de alta qualidade a custos adequados.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Correta.** O item está **Certo**. Conforme fundamentado na seção *2.4 Tabela Comparativa de Propósitos e Custos dos Três Pilares* deste guia, pilar: Pergunta que Responde — Granularidade dos Dados — Custo de Armazenamento e Processamento — Ferramentas de Referência. Dessa forma, está plenamente correta a proposição da banca (CEBRASPE – TRT/10/2013) ao afirmar que "A engenharia de software engloba processos, métodos e ferramentas. Um de seus focos é a produção de software...".
> - **E)** **Incorreta.** A marcação como **Errado** não procede, visto que a assertiva guarda integral conformidade com a teoria estudada em *2.4 Tabela Comparativa de Propósitos e Custos dos Três Pilares*, segundo a qual traces: "Qual serviço no fluxo causou o atraso ou falha?" — Grafo hierárquico causal de transação distribuída. — Médio (requer uso de amostragem/*sampling* em alta escala). — Jaeger, Zipkin, OpenTelemetry.
>
> **Gabarito: C**

---

## 🌐 Fontes Oficiais e Referências Bibliográficas

* [OpenTelemetry Official Documentation - Core Concepts](https://opentelemetry.io/docs/concepts/signals/) - Os três pilares fundamentais da observabilidade moderna: Métricas, Logs estruturados e Traces distribuídos.
* [Prometheus Official Documentation - Metric Types](https://prometheus.io/docs/concepts/metric_types/) - Tipologia de séries temporais: Counter, Gauge, Histogram e Summary.
* [Google SRE Book - Service Level Objectives (SLI, SLO, SLA)](https://sre.google/sre-book/service-level-objectives/) - Engenharia de confiabilidade de sites, cálculo de orçamentos de erro (*error budgets*) e acordos de nível de serviço.
* [DORA - Four Keys Metrics and Continuous Delivery](https://dora.dev/guides/dora-metrics-four-keys/) - Monitoramento contínuo de tempo de restauração e taxa de falhas operacionais.
* BEYER, Betsy et al. **Site Reliability Engineering: How Google Runs Production Systems**. Sebastopol: O'Reilly Media, 2016. (Cap. 4 - Service Level Objectives; Cap. 6 - Monitoring Distributed Systems).
* MAJORS, Charity; FONG-JONES, Liz; MIRANDA, George. **Observabilidade em Engenharia de Software**. São Paulo: Novatec, 2023. (Cap. 2 a 4 - Tracing Distribuído e Telemetria em Sistemas Complexos).
* TURNBULL, James. **The Art of Monitoring**. Nova York: James Turnbull, 2016. (Cap. 3 e 4 - Métricas de Séries Temporais e Alertas Inteligentes).
