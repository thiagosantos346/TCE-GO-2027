# -*- coding: utf-8 -*-
"""
Script de Enriquecimento dos Arquivos Restantes do Módulo 14:
- 02_vocabulario_tecnico_de_ti_e_conjuncoes.md (Adiciona Questões 06 a 10)
- 03_interpretacao_de_documentacao_de_apis_e_manuais.md (Adiciona Questões 06 a 10)
- Atualização do README.md para 🟢 Concluído (10 Qs)
"""

import os

BASE_DIR = "fontes_de_estudo/conhecimentos_especificos_b02_ti/14_lingua_inglesa_leitura_tecnica"

# ==============================================================================
# ENRIQUECIMENTO DO ARQUIVO 02
# ==============================================================================
def enrich_file_02():
    path = os.path.join(BASE_DIR, "02_vocabulario_tecnico_de_ti_e_conjuncoes.md")
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    if "### Questão 06" in text:
        print("[02] Arquivo já contém Questão 06.")
        return

    # Q06: Após Seção 1.2 Regra do Despite (antes de ### 1.3 Relações de Causa)
    target_q06 = "### 1.3 Relações de Causa, Explicação e Motivo"
    q06_content = """---

### Questão 06 (FCC - Adaptada / TRT - Analista Judiciário - Tecnologia da Informação)
*Carefully read the technical excerpt below on distributed systems:*

> *"**Despite** the sudden network partition and sporadic hardware failures, the distributed ledger maintained strong data consistency across all active nodes. **Although** write throughput temporarily stalled during leader election, no uncommitted transactions were lost. The engineering team, **however**, scheduled an emergency firmware update to mitigate residual latency spikes."*

Com base no texto técnico e nas regras morfossintáticas e coesivas da língua inglesa, assinale a afirmação correta:

* **A)** A substituição do conectivo **"Despite"** pela locução **"Despite of"** preservaria a correção gramatical e o sentido original do período.
* **B)** A oração introduzida por **"Although"** expressa uma concessão que poderia ser substituída sem prejuízo sintático ou semântico por **"Even though"**.
* **C)** O termo **"however"** introduz uma oração subordinada causal explicativa sobre a atualização de firmware.
* **D)** A expressão **"in spite of"** não poderia substituir **"Despite"** no primeiro período, pois exige oração subordinada com verbo conjugado.
* **E)** O vocábulo **"Although"** deve ser necessariamente acompanhado de substantivo simples desacompanhado de verbo finito.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. A forma **"Despite of" NÃO EXISTE** na língua inglesa padrão. É uma clássica armadilha de bancas de concurso (FCC/FGV). O correto é utilizar **"Despite"** (sem preposição) ou **"In spite of"** (com preposição).
> - **B)** Correta. As conjunções subordinativas concessivas **"Although"**, **"Even though"** e **"Though"** são semanticamente intercambiáveis e exigem a mesma estrutura sintática (sujeito + verbo finito conjugado: *"write throughput temporarily stalled"*).
> - **C)** Incorreta. O vocábulo **"however"** é um advérbio conjuntivo adversativo que expressa **contraste, ressalva ou oposição** (no entanto, porém, contudo), e não causa ou explicação.
> - **D)** Incorreta. A locução prepositiva **"in spite of"** é sinônima exata de **"despite"** e exige sintagma nominal (*noun phrase*): *"In spite of the sudden network partition..."* seria plenamente correto.
> - **E)** Incorreta. **"Although"** é uma conjunção e exige oração completa com verbo (*"write throughput temporarily stalled"*). Quem exige sintagma nominal é *despite* ou *in spite of*.
> 
> **Gabarito: B**

---

"""

    if target_q06 not in text:
        raise ValueError(f"Target Q06 '{target_q06}' not found in File 02")
    text = text.replace(target_q06, q06_content + target_q06)

    # Q07: Após Seção 1.6 Regra do Unless (antes de ### 1.7 Tabela Canônica)
    target_q07 = "### 1.7 Tabela Canônica de Conectivos e Substituições Intercambiáveis"
    q07_content = """---

### Questão 07 (FCC - Adaptada / Tribunal de Contas - Auditoria Governamental de TI)
*Read the continuous delivery policy statement below:*

> *"The automated deployment pipeline will not release the production artifact into the sovereign cloud cluster **unless** all static code analysis checks report zero critical vulnerabilities **and** the regression suite passes with 100% compliance."*

No contexto da infraestrutura de CI/CD apresentada e da semântica dos conectivos na língua inglesa, a diretriz condicional regida pela conjunção **"unless"** expressa que o artefato só será publicado se:

* **A)** Todos os testes estáticos reportarem zero vulnerabilidades críticas e os testes de regressão obtiverem 100% de conformidade.
* **B)** Os testes estáticos acusarem vulnerabilidades críticas ou os testes de regressão falharem.
* **C)** A equipe de auditoria dispensar formalmente a verificação de vulnerabilidades em virtude de prazos urgentes.
* **D)** O cluster de nuvem registrar latência nula, independentemente do resultado dos analisadores estáticos.
* **E)** O deploy ocorrer em ambiente de homologação (*staging*) desprovido de regras de integridade.

> **Comentário Detalhado:**
>
> - **A)** Correta. A conjunção condicional **"unless"** equivale estritamente a **"if... not"** (*a não ser que, a menos que, exceto se*). A frase estabelece: *"O pipeline não fará o release a não ser que (unless) A e B ocorram"*. Portanto, para que haja o release, é mandatório que **ambas** as condições (A e B) sejam plenamente satisfeitas.
> - **B)** Incorreta. Se houver vulnerabilidades ou se os testes de regressão falharem, o pipeline **bloqueará** a implantação, exatamente o inverso da afirmativa.
> - **C)** Incorreta. A regra é automatizada e não prevê dispensa por urgência no texto técnico.
> - **D)** Incorreta. Não há menção a latência ou dispensa de analisadores estáticos.
> - **E)** Incorreta. O texto restringe o envio para o cluster sovereign de produção.
> 
> **Gabarito: A**

---

"""

    if target_q07 not in text:
        raise ValueError(f"Target Q07 '{target_q07}' not found in File 02")
    text = text.replace(target_q07, q07_content + target_q07)

    # Q08: Após Seção 2.2 Sufixos Gramaticais (antes de ### 2.3 Substantivos Compostos)
    target_q08 = "### 2.3 Substantivos Compostos e Leitura Reversa (Noun Adjuncts)"
    q08_content = """---

### Questão 08 (FCC - Adaptada / Analista de Sistemas - Desenvolvimento)
*Analyze the technical sentence below regarding cloud computing architecture:*

> *"The architectural **maintainability** and **scalability** of cloud-native microservices ensure that distributed workloads degrade **gracefully** during unexpected traffic bursts."*

Em relação à morfologia das palavras em destaque e seus sufixos na língua inglesa, assinale a afirmativa correta:

* **A)** Os vocábulos **"maintainability"** e **"scalability"** são substantivos abstratos derivados de adjetivos com sufixo *-able* acrescidos do sufixo nominalizador *-ity*.
* **B)** A terminação *-ly* em **"gracefully"** caracteriza um adjetivo descritivo invariável que qualifica o substantivo *workloads*.
* **C)** O sufixo *-ity* transforma substantivos em verbos no infinitivo.
* **D)** As palavras *maintainability* e *scalability* funcionam sintaticamente como advérbios de modo que indicam tempo de resposta.
* **E)** A terminação *-able* presente na raiz das palavras traduz uma impossibilidade ou veto técnico categórico.

> **Comentário Detalhado:**
>
> - **A)** Correta. O processo de formação é claro: *maintain* (verbo) $\rightarrow$ *maintainable* (adjetivo) $\rightarrow$ *maintainability* (substantivo que expressa qualidade/capacidade); e *scale* (verbo) $\rightarrow$ *scalable* (adjetivo) $\rightarrow$ *scalability* (substantivo). O sufixo derivacional **-ity** forma **substantivos abstratos** indicando condição, estado ou propriedade técnica.
> - **B)** Incorreta. O sufixo **-ly** em *gracefully* forma um **advérbio de modo** (*de forma graciosa / suavemente / sem colapsar*), que modifica o verbo *degrade*, e não um adjetivo.
> - **C)** Incorreta. O sufixo *-ity* forma substantivos, nunca verbos.
> - **D)** Incorreta. *Maintainability* e *scalability* são substantivos nucleares do sujeito oracional, e não advérbios.
> - **E)** Incorreta. O sufixo *-able / -ible* denota capacidade, passibilidade ou viabilidade técnica (passível de manutenção, passível de escalabilidade).
> 
> **Gabarito: A**

---

"""

    if target_q08 not in text:
        raise ValueError(f"Target Q08 '{target_q08}' not found in File 02")
    text = text.replace(target_q08, q08_content + target_q08)

    # Q09: Após Seção 3.1 Arquitetura e Engenharia de Software (antes de ### 3.2 Concorrência)
    target_q09 = "### 3.2 Concorrência e Sistemas Operacionais"
    q09_content = """---

### Questão 09 (FCC - Adaptada / TCE-GO - Engenharia de Software)
*Read the architectural review summary below:*

> *"The audit team observed excessive **boilerplate** code across the data access layer, coupled with high **coupling** and low **cohesion** between payment services. To resolve this technical debt, the lead architect proposed continuous **refactoring**, acknowledging the inevitable **trade-off** between immediate delivery speed and long-term maintainability."*

Com base na terminologia técnica consagrada na engenharia de software e no texto acima:

* **A)** O termo **"refactoring"** designa a reescrita de código com a finalidade exclusiva de alterar as saídas e regras de negócio externas observáveis pelos usuários.
* **B)** A expressão **"trade-off"** refere-se a uma decisão de engenharia na qual a obtenção de uma vantagem técnica implica forçosamente abrir mão de outro benefício ou aceitar um custo correlato.
* **C)** O conceito de **"boilerplate"** define módulos de software altamente customizados e exclusivos que encerram algoritmos confidenciais de negócio.
* **D)** O estado de **"high coupling"** (alto acoplamento) constitui a melhor prática arquitetural recomendada, pois assegura que módulos dependam criticamente uns dos outros para operar.
* **E)** O vocábulo **"cohesion"** (coesão) indica a quantidade de pacotes de dados perdidos em uma transmissão de rede local.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O termo **"refactoring"** (refatoração) consiste na melhoria da estrutura interna do código fonte **sem alterar seu comportamento observável externo**. Se o comportamento externo é alterado, não é refatoração pura, mas redesign ou nova feature.
> - **B)** Correta. Na literatura técnica e em provas de concurso, **"trade-off"** define a relação de compromisso ou concessão mútua: escolher uma abordagem arquitetural vantajosa em determinado aspecto (ex.: velocidade de entrega) acarretando desvantagens em outro (ex.: manutenibilidade).
> - **C)** Incorreta. **"Boilerplate"** refere-se a código repetitivo, verboso e padronizado necessário para suporte ou configuração, desprovido de valor específico de negócio.
> - **D)** Incorreta. A regra áurea de design arquitetural prega **baixo acoplamento** (*low coupling*) e **alta coesão** (*high cohesion*). Alto acoplamento gera dependências frágeis e propagação de falhas em cascata.
> - **E)** Incorreta. **"Cohesion"** (coesão) mede o grau de afinidade e foco das responsabilidades de uma classe ou módulo (responsabilidade única), nada tendo a ver com perda de pacotes de rede.
> 
> **Gabarito: B**

---

"""

    if target_q09 not in text:
        raise ValueError(f"Target Q09 '{target_q09}' not found in File 02")
    text = text.replace(target_q09, q09_content + target_q09)

    # Q10: Após Seção 3.4 Segurança Cibernética (antes de ## 6. Fontes Recomendadas)
    target_q10 = "## 6. Fontes Recomendadas na Internet"
    q10_content = """### Questão 10 (FCC - Adaptada / Segurança Cibernética e Auditoria de Sistemas)
*Read the cybersecurity incident report excerpt below:*

> *"During the external penetration test, the adversary attempted to bypass perimeter firewalls via **IP spoofing** and gain administrative access through targeted **phishing**. However, cryptographic **tamper-proof** event logs maintained on an immutable write-once store allowed forensic auditors to establish **non-repudiation** and swiftly execute threat **mitigation** procedures."*

No âmbito da segurança da informação e auditoria de sistemas, a correta interpretação dos termos destacados indica que:

* **A)** **"IP spoofing"** consiste na criptografia legítima do endereço IP de origem para acelerar o roteamento de pacotes prioritários.
* **B)** Registros descritos como **"tamper-proof"** são trilhas de auditoria dotadas de salvaguardas que impedem ou evidenciam qualquer adulteração ou manipulação não autorizada de dados.
* **C)** O princípio de **"non-repudiation"** (não repúdio) confere ao autor da ação a faculdade técnica de negar a autoria de qualquer transação efetuada no sistema.
* **D)** O termo **"mitigation"** descreve a intensificação intencional de vulnerabilidades operacionais em servidores expostos na internet.
* **E)** **"Phishing"** caracteriza a exclusão definitiva de logs de eventos mediante ataques de inundação de pacotes syn-flood.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. **"IP spoofing"** (falsificação/mascaramento de IP) é uma técnica de ataque em que o invasor forja o cabeçalho IP para se passar por um endereço de confiança.
> - **B)** Correta. A expressão **"tamper-proof"** (à prova de adulteração) qualifica repositórios, trilhas ou mecanismos criptográficos imutáveis (como WORM - *Write Once, Read Many*) projetados para impossibilitar a modificação ou exclusão de registros de auditoria por usuários maliciosos ou comprometidos.
> - **C)** Incorreta. O princípio de **"non-repudiation"** (não repúdio ou irrefutabilidade) **garante a impossibilidade de negar** a autoria ou integridade da transação realizada.
> - **D)** Incorreta. **"Mitigation"** (mitigação) consiste na redução, contenção e controle de riscos ou danos decorrentes de vulnerabilidades ou incidentes.
> - **E)** Incorreta. **"Phishing"** é técnica de engenharia social voltada a induzir usuários a fornecer senhas e dados confidenciais, não exclusão de logs.
> 
> **Gabarito: B**

---

"""

    if target_q10 not in text:
        raise ValueError(f"Target Q10 '{target_q10}' not found in File 02")
    text = text.replace(target_q10, q10_content + target_q10)

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("[02] Enriquecimento concluído com sucesso!")


# ==============================================================================
# ENRIQUECIMENTO DO ARQUIVO 03
# ==============================================================================
def enrich_file_03():
    path = os.path.join(BASE_DIR, "03_interpretacao_de_documentacao_de_apis_e_manuais.md")
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    if "### Questão 06" in text:
        print("[03] Arquivo já contém Questão 06.")
        return

    # Q06: Após Seção 1.1 Os Níveis Normativos Canônicos (antes de ### 1.2 Matriz)
    target_q06 = "### 1.2 Matriz de Conformidade Técnica da RFC 2119"
    q06_content = """---

### Questão 06 (FCC - Adaptada / Tribunal de Contas - Auditoria de TI)
*Read the standard specification clause below regarding secure communications:*

> *"The authentication service **MUST NOT** transmit user credentials in plaintext over unencrypted communication channels. Furthermore, client applications **SHOULD** implement exponential backoff upon receiving status 429, and **MAY** include a custom telemetry header for diagnostic monitoring."*

De acordo com as diretrizes formais de interpretação normativa da IETF (RFC 2119 e RFC 8174), é correto afirmar que:

* **A)** A locução **"MUST NOT"** representa mera recomendação estilística de segurança, cuja inobservância pode ser ignorada pelos desenvolvedores sem comprometer a conformidade com a especificação.
* **B)** O termo **"SHOULD"** impõe uma recomendação técnica enfática que, embora possa admitir exceções motivadas em circunstâncias específicas, não deve ser desprezada sem plena avaliação e justificativa de suas implicações.
* **C)** O vocábulo **"MAY"** estabelece um requisito obrigatório e estritamente mandatório para todos os clientes compatíveis.
* **D)** O verbo modal **"MUST NOT"** autoriza o envio de senhas em texto puro desde que a rede interna seja cabeada e protegida por firewall perimetral.
* **E)** As palavras-chave normativas da RFC 2119 perdem seu caráter prescritivo quando redigidas inteiramente em letras maiúsculas.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. **"MUST NOT"** (ou *SHALL NOT*) expressa uma **proibição absoluta** (*absolute prohibition*). Qualquer implementação que desobedeça a esse mandamento é classificada tecnicamente como não-conforme (*non-compliant*).
> - **B)** Correta. Segundo a RFC 2119, **"SHOULD"** (ou *RECOMMENDED*) indica que existem razões operacionais válidas para que o recurso seja ignorado em cenários muito específicos, mas que todas as implicações de risco devem ser compreendidas e sopesadas antes de adotar conduta diversa. Representa a boa prática preconizada.
> - **C)** Incorreta. **"MAY"** (ou *OPTIONAL*) define um recurso estritamente **opcional / discricionário**, cuja inclusão ou ausência depende da conveniência do desenvolvedor.
> - **D)** Incorreta. O veto estipulado por *MUST NOT* é absoluto e incondicional na especificação.
> - **E)** Incorreta. A regra central da RFC 2119 e RFC 8174 é justamente que essas palavras têm significado prescritivo estrito quando grafadas em **letras maiúsculas** (*UPPERCASE*).
> 
> **Gabarito: B**

---

"""

    if target_q06 not in text:
        raise ValueError(f"Target Q06 '{target_q06}' not found in File 03")
    text = text.replace(target_q06, q06_content + target_q06)

    # Q07: Após Seção 2.1 Estrutura de Rotas e Idempotência (antes de ### 2.2 Parâmetros)
    target_q07 = "### 2.2 Parâmetros de Requisição e Schemas de Dados JSON"
    q07_content = """---

### Questão 07 (FCC - Adaptada / Analista de Sistemas - Integração e Microsserviços)
*Read the API reference documentation snippet below:*

> *"The payment gateway exposes the following endpoint:*  
> `POST /api/v1/settlements`  
> *Each incoming request instantiates a new settlement ledger entry and triggers bank clearance. Because this operation is **not idempotent**, consumers must supply an `Idempotency-Key` header to prevent duplicate charges in the event of network timeouts."*

Considerando a semântica dos verbos HTTP na arquitetura RESTful e a documentação apresentada, assinale a alternativa correta:

* **A)** As requisições executadas com o verbo **GET** são consideradas operações não-seguras e não-idempotentes, pois invariavelmente alteram o estado do banco de dados no servidor.
* **B)** A operação via método **POST** descrita é não-idempotente porque requisições sucessivas idênticas com o mesmo corpo podem criar múltiplos lançamentos e cobranças bancárias duplicadas.
* **C)** O método **PUT** destina-se primordialmente a consultas parciais de dados e possui comportamento inerentemente não-idempotente pelo padrão HTTP.
* **D)** O verbo **DELETE** é considerado não-idempotente, uma vez que a exclusão repetida de um recurso já removido resulta na restauração automática da entidade.
* **E)** Todos os métodos do protocolo HTTP tornam-se automaticamente idempotentes quando transportados por conexões TLS/HTTPS.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O método **GET** é categorizado pelo protocolo HTTP (RFC 9110) como **seguro** (*safe* - não causa efeitos colaterais de escrita) e **idempotente** (*idempotent* - repetidas chamadas têm o mesmo efeito de uma única).
> - **B)** Correta. O método **POST** é tipicamente **não-idempotente** (*non-idempotent*). Se o cliente submeter a mesma requisição três vezes em razão de falhas de timeout, o servidor poderá gerar três registros distintos de liquidação e três débitos, exigindo mecanismos de proteção como chaves de idempotência (*Idempotency-Key*).
> - **C)** Incorreta. O método **PUT** realiza a substituição total de um recurso em uma URI conhecida e é formalmente **idempotente** (executar 1 ou 10 vezes o mesmo PUT com os mesmos dados deixa o recurso no mesmo estado final).
> - **D)** Incorreta. O método **DELETE** é **idempotente**: a primeira chamada remove o recurso; as chamadas subsequentes encontram o recurso já ausente (podendo retornar 404), mas o estado final do servidor permanece inalterado (recurso ausente).
> - **E)** Incorreta. A segurança da camada de transporte (HTTPS/TLS) protege a confidencialidade e integridade dos dados em trânsito, mas em nada altera a semântica operacional de idempotência da camada de aplicação HTTP.
> 
> **Gabarito: B**

---

"""

    if target_q07 not in text:
        raise ValueError(f"Target Q07 '{target_q07}' not found in File 03")
    text = text.replace(target_q07, q07_content + target_q07)

    # Q08: Após Seção 2.4 Documentação de APIs GraphQL (antes de ## 3. Interpretação de Manuais)
    target_q08 = "## 3. Interpretação de Manuais Técnicos e Guias de Configuração de Sistemas"
    q08_content = """### Questão 08 (FCC - Adaptada / SEFAZ - Auditoria Fiscal e Sistemas)
*Read the GraphQL Schema Definition Language (SDL) snippet below:*

```graphql
type TaxpayerAudit {
  registrationId: ID!
  companyName: String!
  fiscalScore: Float
  isFlagged: Boolean!
}

type Query {
  getAuditRecord(registrationId: ID!): TaxpayerAudit
}

type Mutation {
  flagIrregularity(registrationId: ID!, reason: String!): TaxpayerAudit!
}
```

Com base nas convenções sintáticas e conceituais do padrão GraphQL e no schema apresentado, assinale a opção correta:

* **A)** O ponto de exclamação `!` associado aos tipos (ex.: `ID!`, `String!`) indica que o campo é puramente opcional e admite valor nulo (*null*).
* **B)** A operação categorizada sob o tipo **Query** é destinada a realizar mutações de escrita e atualizar trilhas de auditoria no servidor.
* **C)** O campo `fiscalScore` pode retornar valor nulo (*null*), uma vez que não possui o modificador de obrigatoriedade `!`.
* **D)** As operações do tipo **Mutation** são consultas de somente-leitura que não aceitam parâmetros de entrada nem alteram dados.
* **E)** O GraphQL requer a criação de endpoints HTTP distintos (URIs dedicadas) para cada uma das consultas e mutações declaradas no esquema.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. No GraphQL SDL, o modificador de exclamação **`!`** indica **não-nulidade** (*Non-Null* / obrigatório). Campos com `!` jamais podem retornar ou receber valores nulos.
> - **B)** Incorreta. A raiz **Query** destina-se a operações de **consulta e leitura** de dados, sem efeitos colaterais de modificação de estado no servidor.
> - **C)** Correta. No tipo `TaxpayerAudit`, o campo `fiscalScore: Float` não é seguido pelo caractere `!`, o que significa que é um campo anulável (*nullable*), podendo retornar um número de ponto flutuante ou o valor `null`.
> - **D)** Incorreta. As **Mutations** são operações que realizam modificações no servidor (criação, edição, exclusão de dados), equivalentes conceituais a POST, PUT ou DELETE em REST.
> - **E)** Incorreta. Diferentemente do REST, o GraphQL concentra todas as queries e mutations em um **único endpoint HTTP** padronizado (comumente `POST /graphql`).
> 
> **Gabarito: C**

---

"""

    if target_q08 not in text:
        raise ValueError(f"Target Q08 '{target_q08}' not found in File 03")
    text = text.replace(target_q08, q08_content + target_q08)

    # Q09: Após Seção 3.4 Ciclo de Vida: Deprecated vs. Decommissioned (antes de ## 4. Leitura Crítica)
    target_q09 = "## 4. Leitura Crítica de Artigos Científicos e Papers de TI (IEEE / ACM / ArXiv)"
    q09_content = """### Questão 09 (FCC - Adaptada / Analista de TI - Governança de Software)
*Read the technical release note excerpt below regarding an enterprise authentication library:*

> *"**Notice:** Version 3.4 marks the endpoint `/v1/auth/legacy-token` as **deprecated**. While the endpoint remains functional throughout the 3.x release series to ensure backward compatibility, security teams are strongly advised to migrate to `/v2/oauth/token`. In version 4.0, this endpoint will be fully **decommissioned**, and any subsequent invocation will immediately return HTTP 410 Gone."*

Com base na terminologia técnica empregada para definir o ciclo de vida de componentes de software e no texto acima:

* **A)** Um componente classificado como **"deprecated"** já foi completamente removido da base de código e não processa nenhuma requisição desde o lançamento da versão 3.4.
* **B)** A classificação de um recurso como **"deprecated"** adverte que, embora ainda permaneça funcional na versão corrente, seu uso é formalmente desaconselhado e sua remoção definitiva (*decommissioning*) ocorrerá em versão futura.
* **C)** O termo **"decommissioned"** significa que o recurso continuará recebendo novas funcionalidades e atualizações prioritárias de segurança indefinidamente.
* **D)** A resposta `HTTP 410 Gone` indica que a requisição ao endpoint `/v1/auth/legacy-token` foi atendida com pleno sucesso e autorização irrestrita.
* **E)** O conceito de *backward compatibility* traduz a incompatibilidade intencional com versões legadas para forçar a contratação de novos fornecedores.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O texto explicita que o endpoint continua funcional: *"While the endpoint remains functional throughout the 3.x release series to ensure backward compatibility"*.
> - **B)** Correta. No ciclo de vida de APIs e software, **"deprecated"** (obsoleto / descontinuado) indica que a funcionalidade ainda está presente para não quebrar sistemas existentes (*backward compatibility*), mas seu uso deve ser cessado porque ela será desativada/removida (*decommissioned*) em versões vindouras.
> - **C)** Incorreta. **"Decommissioned"** (descomissionado / desativado) significa que o serviço foi desligado ou o endpoint foi fisicamente removido do sistema.
> - **D)** Incorreta. O código de status `410 Gone` é um erro do cliente (*Client Error*) que indica que o recurso solicitado não está mais disponível no servidor e foi intencional e permanentemente removido.
> - **E)** Incorreta. *Backward compatibility* (retrocompatibilidade) é a capacidade de uma nova versão de software interoperar com sistemas legados sem quebras inesperadas.
> 
> **Gabarito: B**

---

"""

    if target_q09 not in text:
        raise ValueError(f"Target Q09 '{target_q09}' not found in File 03")
    text = text.replace(target_q09, q09_content + target_q09)

    # Q10: Após Seção 4.3 Léxico de Validação Experimental (antes de ## 6. Fontes Recomendadas)
    target_q10 = "## 6. Fontes Recomendadas na Internet"
    q10_content = """### Questão 10 (FCC - Adaptada / Auditor de Controle Externo - Tecnologia da Informação)
*Read the research paper excerpt on distributed storage systems:*

> *"In this paper, we evaluate **AuroraKV**, a novel distributed key-value store designed for geo-replicated transactional workloads. In extensive empirical evaluations using the Yahoo! Cloud Serving **Benchmark** (YCSB), AuroraKV **outperforms** state-of-the-art baselines by up to 45% in write throughput while keeping tail latency (P99) under 15ms. Furthermore, our consensus optimizations introduce an operational **overhead** of less than 2.8% on server CPU utilization, demonstrating the feasibility of near-instant multi-region consistency."*

Com base nas convenções léxicas e metodológicas da literatura científica internacional de TI e no trecho acima, assinale a afirmativa correta:

* **A)** O termo **"outperforms"** expressa que a solução proposta apresentou desempenho inferior ao das tecnologias comparadas.
* **B)** A palavra **"Benchmark"** designa um conjunto padronizado de testes e cargas de trabalho concebido para avaliar e comparar o desempenho de sistemas computacionais de maneira empírica.
* **C)** A expressão **"overhead"** descreve o ganho patrimonial direto obtido pela equipe de desenvolvedores ao publicar o artigo.
* **D)** A métrica de **"tail latency (P99)"** expressa o tempo médio de resposta apurado sobre 99% das requisições mais velozes do cluster.
* **E)** O vocábulo **"baselines"** designa erros de compilação irreparáveis detectados no código-fonte dos servidores.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O verbo transitivo **"outperform"** significa **superar em desempenho, ter rendimento superior** (*"AuroraKV supera as soluções de referência em até 45% na vazão de escrita"*).
> - **B)** Correta. Em ciência da computação e engenharia de software, um **"benchmark"** é um programa, teste padronizado ou conjunto de cargas (*workloads*) de referência utilizado para avaliar e comparar quantitativamente a performance de hardwares, bancos de dados ou sistemas distribuídos.
> - **C)** Incorreta. **"Overhead"** é o custo computacional indireto ou marginal adicionado por um mecanismo (ex.: consumo adicional de ciclos de CPU ou memória RAM), e não vantagem financeira.
> - **D)** Incorreta. A latência de cauda (*tail latency* P99) mede o tempo de resposta do percentil 99, ou seja, o limite superior de lentidão experimentado pelo 1% das requisições mais lentas e críticas do sistema.
> - **E)** Incorreta. Em metodologia científica de TI, **"baselines"** são os sistemas de referência consagrados ou modelos tradicionais existentes com os quais a nova solução é comparada.
> 
> **Gabarito: B**

---

"""

    if target_q10 not in text:
        raise ValueError(f"Target Q10 '{target_q10}' not found in File 03")
    text = text.replace(target_q10, q10_content + target_q10)

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("[03] Enriquecimento concluído com sucesso!")


# ==============================================================================
# ATUALIZAÇÃO DO README DO MÓDULO 14
# ==============================================================================
def update_readme_14():
    path = os.path.join(BASE_DIR, "README.md")
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace(
        "> **Status Geral:** 🟡 Em mapeamento de fontes teóricas",
        "> **Status Geral:** 🟢 Concluído (100% enriquecido e auditado)"
    )

    text = text.replace(
        "| 01 | [Estratégias de Leitura Instrumental: Skimming, Scanning e Inferência](./01_estrategias_de_leitura_skimming_scanning_e_inferencia.md) | `01_estrategias_de_leitura_skimming_scanning_e_inferencia.md` | Skimming (ideia principal); Scanning (dados pontuais); Falsos cognatos e inferência de sentido | ⚪ Aguardando Fontes |",
        "| 01 | [Estratégias de Leitura Instrumental: Skimming, Scanning e Inferência](./01_estrategias_de_leitura_skimming_scanning_e_inferencia.md) | `01_estrategias_de_leitura_skimming_scanning_e_inferencia.md` | Skimming (ideia principal); Scanning (dados pontuais); Falsos cognatos e inferência de sentido | 🟢 Concluído (10 Qs) |"
    )

    text = text.replace(
        "| 02 | [Vocabulário Técnico de TI, Coesão e Conectivos](./02_vocabulario_tecnico_de_ti_e_conjuncoes.md) | `02_vocabulario_tecnico_de_ti_e_conjuncoes.md` | Glossário técnico de TI; Conectivos lógicos (Linking Words); Morfologia e afixos em inglês | ⚪ Aguardando Fontes |",
        "| 02 | [Vocabulário Técnico de TI, Coesão e Conectivos](./02_vocabulario_tecnico_de_ti_e_conjuncoes.md) | `02_vocabulario_tecnico_de_ti_e_conjuncoes.md` | Glossário técnico de TI; Conectivos lógicos (Linking Words); Morfologia e afixos em inglês | 🟢 Concluído (10 Qs) |"
    )

    text = text.replace(
        "| 03 | [Interpretação de Documentação de APIs, Manuais e Artigos](./03_interpretacao_de_documentacao_de_apis_e_manuais.md) | `03_interpretacao_de_documentacao_de_apis_e_manuais.md` | Leitura de contratos e respostas de APIs; Manuais de configuração e papers/artigos técnicos | ⚪ Aguardando Fontes |",
        "| 03 | [Interpretação de Documentação de APIs, Manuais e Artigos](./03_interpretacao_de_documentacao_de_apis_e_manuais.md) | `03_interpretacao_de_documentacao_de_apis_e_manuais.md` | Leitura de contratos e respostas de APIs; Manuais de configuração e papers/artigos técnicos | 🟢 Concluído (10 Qs) |"
    )

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("[README] README.md do Módulo 14 atualizado com sucesso!")


if __name__ == "__main__":
    enrich_file_02()
    enrich_file_03()
    update_readme_14()
