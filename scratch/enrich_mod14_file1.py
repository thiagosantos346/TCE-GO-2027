import os

file_path = "fontes_de_estudo/conhecimentos_especificos_b02_ti/14_lingua_inglesa_leitura_tecnica/01_estrategias_de_leitura_skimming_scanning_e_inferencia.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

q06 = """
---

### Questão 06 (FCC - Adaptada / Analista de Sistemas - Governança e Métodos)
*Read the paragraph below regarding English for Specific Purposes (ESP) applied to technical auditing:*

> *"Technical reading in computer science does not require exhaustive vocabulary knowledge of conversational English. Instead, an auditor relies on a tripartite cognitive model: domain-specific schemata (prior background knowledge), minimal grammatical architecture (such as modal auxiliaries and passive voice), and metacognitive reading strategies. During the pre-reading phase, examining the question stem and answer options before confronting the source text allows the reader to establish mental anchors and discard irrelevant details."*

According to the text and instrumental reading fundamentals:  

* **A)** An auditor must master all colloquial idioms and conversational slang of the English language before being able to interpret technical documentation.
* **B)** Prior background knowledge (*schemata*) in IT concepts compensates for lexical gaps in general vocabulary, accelerating comprehension when combined with metacognitive strategies like pre-reading.
* **C)** Pre-reading mandates that the candidate read the entire technical article three times before inspecting the question's alternatives.
* **D)** Metacognitive reading strategies are strictly forbidden in competitive public examinations for IT positions.
* **E)** The passive voice is never employed in formal technical and scientific reports in computing.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O texto afirma expressamente o oposto: a leitura técnica não exige vocabulário exaustivo de conversação geral (*"does not require exhaustive vocabulary knowledge of conversational English"*).
> - **B)** **Correta.** O conhecimento técnico prévio (*schemata*) ativa atalhos cognitivos que permitem ao candidato suprir lacunas vocabulares e focar nos elementos essenciais quando combinado com estratégias como a pré-leitura das alternativas e enunciados.
> - **C)** Incorreta. A pré-leitura (*pre-reading*) consiste justamente em ler primeiro o enunciado e alternativas para fixar âncoras antes de ler o texto longo.
> - **D)** Incorreta. As estratégias metacognitivas são amplamente recomendadas e essenciais para resolução de provas sob pressão de tempo.
> - **E)** Incorreta. A voz passiva é extremamente abundante na literatura técnica em inglês para conferir impessoalidade e objetividade aos relatórios.
> 
> **Gabarito: B**
"""

q07 = """
---

### Questão 07 (FCC - Adaptada / Tribunal de Contas - Auditoria de Inteligência Artificial)
*Carefully read the following excerpt on Artificial General Intelligence (AGI):*

> *"The emergence of Artificial General Intelligence represents a profound inflection point for modern civilization. While current narrow AI systems excel at specialized tasks like pattern matching or matrix multiplication, AGI posits autonomous agents capable of human-level reasoning across multidisciplinary domains. Consequently, organizational leaders must anticipate seismic shifts in workforce dynamics and digital governance. Addressing these challenges demands proactive regulatory frameworks that align autonomous optimization with societal ethics before full deployment occurs."*

Applying the **Skimming** strategy to identify the primary argument (*main idea*), the central thesis of the paragraph is that:  

* **A)** Current narrow AI systems have completely failed at performing matrix operations and mathematical calculations.
* **B)** Regulatory frameworks should be permanently dismantled to accelerate unsupervised algorithmic optimization.
* **C)** The advent of AGI requires anticipatory governance and proactive regulatory frameworks to align autonomous systems with human societal values and ethics.
* **D)** Human-level reasoning is impossible to achieve in computer software under any theoretical circumstance.
* **E)** Matrix multiplication is the ultimate goal of public digital governance in auditing.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O texto diz o oposto: sistemas atuais de IA estreita destacam-se (*excel*) em tarefas especializadas como multiplicação de matrizes.
> - **B)** Incorreta. O autor defende a instituição de marcos regulatórios proativos (*proactive regulatory frameworks*), e não seu desmantelamento.
> - **C)** **Correta.** Por meio do *Skimming* (leitura do tópico frasal e da oração conclusiva), constata-se que a tese central do parágrafo é a necessidade imperiosa de governança antecipada e marcos ético-regulatórios para conciliar o avanço de sistemas autônomos aos interesses da sociedade.
> - **D)** Incorreta. O texto discute a emergência da AGI exatamente como agentes capazes de raciocínio de nível humano.
> - **E)** Incorreta. Trata-se de mero exemplo de operação matemática pontual mencionado no texto, e não do tema central.
> 
> **Gabarito: C**
"""

q08 = """
---

### Questão 08 (FGV - TRT / TCE-GO - Analista de TI - Adaptada)
*Consider the sentence below extracted from a technical paper on computing scalability:*

> *"Over the past **roughly** fifty thousand hours of continuous automated monitoring, the distributed database cluster handled over ten billion transactional queries without a single unrecoverable data loss event."*

By employing **Scanning** and analyzing the semantic function of the highlighted word in context, the word **"roughly"** expresses:  

* **A)** an exact, indisputable measurement verified by laboratory standards.
* **B)** an estimation or approximation regarding the elapsed time period.
* **C)** a violent or aggressive manner of physical execution.
* **D)** a frequency of occurrence that happens exclusively on weekends.
* **E)** a legal condition that invalidates the operational metrics of the cluster.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O termo não indica exatidão ou rigor métrico absoluto.
> - **B)** **Correta.** No vocabulário técnico e acadêmico em inglês, o advérbio **"roughly"** (quando associado a números e grandezas temporais) funciona como sinônimo de *approximately / about* (aproximadamente, em torno de, em estimativa aproximada).
> - **C)** Incorreta. Embora *rough* na linguagem coloquial possa significar "áspero" ou "bruto", no contexto quantitativo de engenharia de sistemas *roughly* expressa aproximação/estimativa (*estimation*).
> - **D)** Incorreta. Não denota dias da semana ou periodicidade restrita.
> - **E)** Incorreta. Trata-se de qualificador de medida aproximada, sem conotação jurídica de nulidade.
> 
> **Gabarito: B**
"""

q09 = """
---

### Questão 09 (FCC - Adaptada / Analista de Sistemas - Arquitetura de Software)
*Read the architectural decision record below:*

> *"Migrating our core monolith to a microservices architecture introduces a major **trade-off**: although it enhances deployment agility and horizontal scalability, network latency becomes a significant **bottleneck**. To **remediate** this issue and ensure that unauthorized endpoints cannot **compromise** the service mesh, engineers implemented strict mTLS authentication and distributed caching."*

Regarding the technical vocabulary utilized in software engineering (*trade-off, bottleneck, remediate, compromise*), it is correct to state that:  

* **A)** A *trade-off* indicates a decision without any disadvantage, offering purely positive benefits with zero cost.
* **B)** A *bottleneck* represents a critical point of congestion or constraint that restricts the overall performance and throughput of the system.
* **C)** To *remediate* an architectural problem means to ignore it permanently until the hardware crashes.
* **D)** In cybersecurity, to *compromise* a service mesh means to sign an official peace treaty with external hackers.
* **E)** A *bottleneck* in distributed systems is synonymous with an infinite broadband connection.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Um *trade-off* é uma relação de compromisso ou escolha conflitante: ganha-se de um lado (ex.: escalabilidade) perdendo-se necessariamente de outro (ex.: maior complexidade ou latência).
> - **B)** **Correta.** Em arquitetura de software e redes, *bottleneck* (gargalo) é o elemento ou recurso limitante que restringe o fluxo (*throughput*) e a capacidade máxima do sistema como um todo.
> - **C)** Incorreta. *Remediate* significa remediar, corrigir, sanar ou mitigar uma falha.
> - **D)** Incorreta. No jargão de segurança cibernética, *to compromise* significa violar, invadir ou quebrar a integridade/confidencialidade de um sistema (*comprometimento de segurança*).
> - **E)** Incorreta. *Bottleneck* é o oposto de conexão irrestrita; é um ponto de afunilamento/estrangulamento.
> 
> **Gabarito: B**
"""

q10 = """
---

### Questão 10 (FCC - Adaptada / Auditoria Governamental - Tecnologia da Informação)
*Consider the excerpt below regarding cryptographic hash functions and data integrity:*

> *"Cryptographic hash functions generate a deterministic, fixed-size digest from arbitrary input data. When two distinct inputs produce the identical output hash, **this anomaly** is technically defined as a collision. Security analysts must continuously monitor legacy algorithms, as **they** may become vulnerable over time due to cryptanalytic advances."*

In terms of textual cohesion and pronominal reference in technical texts:  

* **A)** The noun phrase **"this anomaly"** refers conceptually to the fact that *"two distinct inputs produce the identical output hash"*.
* **B)** The personal pronoun **"they"** in the second sentence refers syntactically to *"security analysts"*.
* **C)** The demonstrative **"this"** indicates that the hash algorithm was developed by the author of the text.
* **D)** The pronoun **"they"** refers singular and neutrally to *"a deterministic digest"*.
* **E)** The expression **"this anomaly"** refers strictly to the word *"matrix"* mentioned in another chapter.

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Trata-se do clássico mecanismo de **encapsulamento conceitual com pronome demonstrativo** (*this anomaly*): a expressão sintetiza toda a proposição antecedente de que "duas entradas distintas geram o mesmo hash de saída" (fenômeno conhecido como colisão criptográfica).
> - **B)** Incorreta. Pela análise sintático-semântica, o pronome plural **"they"** retoma o substantivo antecedente **"legacy algorithms"** (*"analysts monitor legacy algorithms, as they [the legacy algorithms] may become vulnerable"*), e não os analistas de segurança.
> - **C)** Incorreta. O pronome *this* funciona como recurso anafórico coesivo, sem conotação de autoria pessoal.
> - **D)** Incorreta. *Digest* está no singular (*a digest*), ao passo que *they* é pronome plural que retoma *legacy algorithms*.
> - **E)** Incorreta. A anáfora é intraparágrafo e retoma o evento da colisão explicitado na oração imediatamente anterior.
> 
> **Gabarito: A**
"""

# Insertions:
# 1. After Section 1.2 (line ~76)
p1 = "- **Pós-leitura (*Post-reading*):** Confrontação das evidências colhidas no texto com as asserções de cada alternativa de A a E, desmascarando distorções, generalizações indevidas e falsos cognatos.\n"
assert p1 in content, "Pattern 1 not found"
content = content.replace(p1, p1 + q06 + "\n")

# 2. After Section 2.2 alert box (line ~102)
p2 = "> Ao resolver questões de ideia principal (*Skimming*), elimine imediatamente alternativas que apresentem fatos verdadeiros contidos no texto, mas que se refiram a detalhes secundários ou exemplos pontuais de um único parágrafo. Uma ideia central deve cobrir a totalidade do texto, e não um aspecto isolado.\n"
assert p2 in content, "Pattern 2 not found"
content = content.replace(p2, p2 + q07 + "\n")

# 3. After Section 3.2 diagram (line ~145)
p3 = "    SC3 --> SC4[\"Validar a verdade ou falsidade da alternativa pontual\"]\n```\n"
assert p3 in content, "Pattern 3 not found"
content = content.replace(p3, p3 + q08 + "\n")

# 4. After Section 4.4 (line ~251)
p4 = "    - *Sensitive:* Sensível, delicado, confidencial (*sensitive data*, dados sensíveis sob a LGPD).\n"
assert p4 in content, "Pattern 4 not found"
content = content.replace(p4, p4 + q09 + "\n")

# 5. After Section 6.1 (line ~354)
p5 = "    - **Which / That:** Aplica-se a coisas, sistemas e conceitos inanimados.\n"
assert p5 in content, "Pattern 5 not found"
content = content.replace(p5, p5 + q10 + "\n")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("File 14_01 successfully updated!")
