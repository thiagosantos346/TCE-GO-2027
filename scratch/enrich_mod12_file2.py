import os

file_path = "fontes_de_estudo/conhecimentos_especificos_b02_ti/12_governanca_de_ti/02_gestao_de_servicos_de_ti_itil_v4.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

q06 = """
---

### Questão 06 (FGV - TJ-RR - Analista Judiciário - Governança e Gestão de TI - Adaptada)
**Enunciado:** A ITIL v4 redefine o conceito central de serviço e a forma como o valor é percebido pelas organizações. Acerca dos conceitos fundamentais de serviço, co-criação de valor, utilidade e garantia, assinale a alternativa correta:  

* **A)** A utilidade (*utility*) refere-se exclusivamente à segurança da informação e à taxa de disponibilidade mensal do hardware, sendo sinônimo estrito de garantia técnica.
* **B)** A garantia (*warranty*) representa a aptidão para o propósito (*fit for purpose*), avaliando unicamente se o software possui os botões e telas solicitados pelo usuário final.
* **C)** O valor de um serviço é criado e entregue de forma puramente unilateral pelo departamento de TI, sendo dispensável qualquer interação, feedback ou co-criação por parte do consumidor do serviço.
* **D)** Para que um serviço viabilize a criação de valor, ele deve fornecer simultaneamente utilidade (*fit for purpose* - o que o serviço faz) e garantia (*fit for use* - como o serviço atende a disponibilidade, capacidade, segurança e continuidade).
* **E)** A ITIL v4 determina que um serviço só pode ser considerado existente se for composto estritamente por bens materiais físicos tangíveis, excluindo softwares em nuvem e fluxos lógicos de suporte.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Disponibilidade, segurança, capacidade e continuidade são atributos de Garantia (*Warranty* - *fit for use*), e não de Utilidade.
> - **B)** Incorreta. A garantia é a aptidão para o uso (*fit for use*). Quem representa a aptidão para o propósito (*fit for purpose*) é a Utilidade (*Utility*).
> - **C)** Incorreta. Um dos pilares centrais da ITIL v4 é que o valor não é empurrado unilateralmente, mas sim co-criado em parceria contínua entre provedor e consumidor.
> - **D)** **Correta.** O valor requer obrigatoriamente a convergência de Utilidade (*o que o serviço faz para suprir a necessidade*) e Garantia (*como o serviço performa em níveis aceitáveis de disponibilidade, capacidade, continuidade e segurança*).
> - **E)** Incorreta. Serviços não precisam ser materiais ou físicos; a grande maioria dos serviços modernos de TI é baseada em software, nuvem e processos operacionais intangíveis.
> 
> **Gabarito: D**
"""

q07 = """
---

### Questão 07 (FCC - Analista de Sistemas - Governança de TI - Adaptada)
**Enunciado:** A Cadeia de Valor de Serviço (SVC - *Service Value Chain*) é o elemento operacional nuclear do Sistema de Valor de Serviço (SVS) da ITIL v4, sendo composta por seis atividades-chave interconectadas. Assinale a alternativa que relaciona corretamente a atividade da cadeia de valor ao seu respectivo propósito:  

* **A)** A atividade 'Obter/Construir' (*Obtain/Build*) tem como foco principal realizar o atendimento de suporte telefônico e registrar chamados de help desk dos usuários.
* **B)** A atividade 'Engajar' (*Engage*) visa proporcionar um bom entendimento das necessidades dos stakeholders, transparência e engajamento contínuo em todo o ciclo de vida dos serviços.
* **C)** A atividade 'Planejar' (*Plan*) é restrita à codificação em linguagens de baixo nível e à compilação de binários para servidores locais.
* **D)** A atividade 'Melhorar' (*Improve*) é realizada uma única vez durante a homologação do sistema, sendo expressamente vedada a sua repetição em serviços já em produção.
* **E)** A atividade 'Entregar e Suportar' (*Deliver & Support*) visa exclusivamente negociar termos de distrato com fornecedores externos sancionados pelo Tribunal.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Atendimento de chamados e suporte a incidentes pertencem à atividade 'Entregar e Suportar' (*Deliver & Support*). 'Obter/Construir' assegura a disponibilidade e desenvolvimento dos componentes de serviço.
> - **B)** **Correta.** A atividade 'Engajar' (*Engage*) gerencia o relacionamento com todas as partes interessadas, captando demandas, compreendendo expectativas e mantendo transparência bidirecional.
> - **C)** Incorreta. A atividade 'Planejar' (*Plan*) garante um entendimento compartilhado da visão, situação atual e direcionamento de evolução estratégica dos serviços e produtos.
> - **D)** Incorreta. 'Melhorar' (*Improve*) é uma atividade contínua aplicada transversalmente a todos os serviços, práticas e componentes da cadeia de valor.
> - **E)** Incorreta. 'Entregar e Suportar' foca na operação diária e na manutenção da entrega contínua dos serviços acordados aos usuários finais.
> 
> **Gabarito: B**
"""

q08 = """
---

### Questão 08 (FCC - Técnico de Controle Externo / TI - Adaptada)
**Enunciado:** Na ITIL v4, a prática da Central de Serviços (*Service Desk*) desempenha um papel tático indispensável na relação cotidiana entre os usuários institucionais e a Diretoria de Tecnologia da Informação. Sobre as características, modelos organizacionais e competências da Central de Serviços, assinale a alternativa correta:  

* **A)** A Central de Serviços atua precipuamente como Ponto Único de Contato (SPOC - *Single Point of Contact*), sendo o canal centralizador para relatos de incidentes e solicitações de serviços da organização.
* **B)** O modelo organizacional de Central de Serviços denominado 'Siga o Sol' (*Follow the Sun*) exige a alocação de todos os analistas exclusivamente em uma única sala física sede, sem qualquer trabalho remoto ou integração de fusos horários.
* **C)** Para analistas da Central de Serviços moderna, o conhecimento puramente técnico sobre protocolos de rede e registradores de CPU é a única competência relevante, dispensando habilidades de comunicação, empatia e visão de processos de negócio.
* **D)** A Central de Serviços é proibida de utilizar canais digitais automatizados, como portais de autoatendimento, chatbots com inteligência artificial ou correio eletrônico corporativo.
* **E)** Compete à Central de Serviços executar pessoalmente a auditoria externa contábil e a emissão dos acórdãos definitivos do Tribunal de Contas.

> **Comentário Detalhado:**
>
> - **A)** **Correta.** A Central de Serviços atua como o Ponto Único de Contato (SPOC) para usuários, acolhendo incidentes, requisições de serviço, orientações e comunicações operacionais.
> - **B)** Incorreta. O modelo *Follow the Sun* distribui equipes ao redor do globo em diferentes fusos horários para oferecer cobertura 24/7 de forma contínua durante o horário diurno de cada localidade.
> - **C)** Incorreta. A Central de Serviços exige forte orientação ao cliente, empatia interpessoal, comunicação clara e compreensão do impacto dos serviços na atividade-fim institucional.
> - **D)** Incorreta. A Central de Serviços utiliza amplamente portais web, autoatendimento, bots e automação para otimizar o fluxo de atendimento.
> - **E)** Incorreta. A emissão de acórdãos e auditorias contábeis são funções finalísticas de controle externo do TCE-GO, totalmente alheias ao escopo do Service Desk.
> 
> **Gabarito: A**
"""

q09 = """
---

### Questão 09 (FGV - TRT - Analista Judiciário - Suporte e Infraestrutura de TI - Adaptada)
**Enunciado:** Segundo o ITIL versão 4, a prática que define metas claras e baseadas no negócio para o desempenho dos serviços, permitindo que a entrega de um serviço seja devidamente avaliada, monitorada e gerenciada com relação a essas metas, articulando instrumentos como SLA, OLA e Contratos de Apoio (UC), é o gerenciamento de:  

* **A)** Capacidade e Desempenho de Serviços.
* **B)** Configuração de Serviços (CMDB).
* **C)** Continuidade de Serviços de TI (ITSCM).
* **D)** Ativos de TI (ITAM).
* **E)** Nível de Serviço (*Service Level Management*).

> **Comentário Detalhado:**
>
> - **A)** Incorreta. Gerenciamento de capacidade assegura que os serviços tenham capacidade computacional suficiente para atender à demanda de forma custo-efetiva.
> - **B)** Incorreta. Gerenciamento de configuração cuida dos registros precisos sobre Itens de Configuração (CIs) e seus relacionamentos no CMDB.
> - **C)** Incorreta. Continuidade de serviços gerencia riscos de desastres catastróficos para garantir sobrevivência da infraestrutura (RTO e RPO).
> - **D)** Incorreta. Gerenciamento de ativos (ITAM) planeja e gerencia o ciclo de vida financeiro e contratual de hardware e licenças de software.
> - **E)** **Correta.** O propósito da prática de Gerenciamento de Nível de Serviço (*Service Level Management*) é exatamente estabelecer uma visão de ponta a ponta dos serviços baseada no negócio, negociando SLAs (com clientes), OLAs (com áreas internas de TI) e UCs (com fornecedores externos).
> 
> **Gabarito: E**
"""

q10 = """
---

### Questão 10 (FCC - Tribunal de Contas - Auditor de TI - Adaptada)
**Enunciado:** Em uma auditoria de resiliência e segurança operacional no data center de um Tribunal de Contas, os auditores avaliaram o Plano de Continuidade de Serviços de TI (ITSCM). A respeito das métricas RTO (*Recovery Time Objective*) e RPO (*Recovery Point Objective*), assinale a afirmativa correta:  

* **A)** O RTO representa a quantidade máxima admissível de dados perdidos em uma falha, mensurada em gigabytes de memória RAM.
* **B)** O RPO estipula o tempo decorrido até que a equipe de desenvolvimento termine a escrita do manual de usuário de uma aplicação.
* **C)** O RTO define o tempo máximo aceitável para restaurar a operação de um serviço de TI após uma interrupção, enquanto o RPO define a tolerância máxima a perdas de dados transacionais ocorrida entre o último ponto de restauração válido e o desastre.
* **D)** Valores de RTO iguais a zero e RPO iguais a zero indicam ausência de proteção tecnológica e desídia administrativa por parte dos gestores de TI.
* **E)** A definição de RTO e RPO é uma decisão puramente técnica que deve ser tomada pela equipe de suporte básico de TI, sem qualquer consulta aos gestores de negócio ou à alta administração do Tribunal.

> **Comentário Detalhado:**
>
> - **A)** Incorreta. O RTO mede tempo de indisponibilidade (velocidade de restauração do serviço), não volume de perda de dados.
> - **B)** Incorreta. RPO não mede documentação; mede o ponto no tempo até onde os dados devem ser recuperados (ex.: tolerar perder no máximo 15 minutos de transações).
> - **C)** **Correta.** RTO (*Recovery Time Objective*) é o tempo limite tolerável para restabelecer o serviço em produção. RPO (*Recovery Point Objective*) é o limite tolerável de perda de transações/dados no tempo.
> - **D)** Incorreta. RTO=0 e RPO=0 representam o mais alto grau de resiliência tecnológica (replicação síncrona ativa-ativa em tempo real com failover instantâneo).
> - **E)** Incorreta. As metas de RTO e RPO dependem do impacto das interrupções no negócio da organização (obtidas por meio da Análise de Impacto no Negócio - BIA) e devem ser validadas pela alta administração.
> 
> **Gabarito: C**
"""

# Insertions:
# 1. After Section 1.1 alert box (line ~72)
p1 = "Se um sistema de processo eletrônico tem todas as telas e funções que os auditores precisam (utilidade), mas cai a cada meia hora ou vaza dados (falha de garantia), o serviço gera valor zero ou negativo.\n"
assert p1 in content, "Pattern 1 not found"
content = content.replace(p1, p1 + q06 + "\n")

# 2. After Section 1.5 item 6 (line ~239)
p2 = "6. **Entregar e Suportar (*Deliver & Support*):** Assegurar que os serviços sejam executados, operados e suportados de acordo com os níveis de serviço acordados com os usuários.\n"
assert p2 in content, "Pattern 2 not found"
content = content.replace(p2, p2 + q07 + "\n")

# 3. After Section 2.1 Service Desk (line ~265)
p3 = "- **Cultura e Habilidades:** Mais do que mero conhecimento técnico profundo, a Central de Serviços exige excelência em atendimento ao cliente, empatia interpessoal e compreensão do impacto das falhas nas atividades institucionais.\n"
assert p3 in content, "Pattern 3 not found"
content = content.replace(p3, p3 + q08 + "\n")

# 4. After Section 2.5 item 3 (line ~438)
p4 = "3. **UC (*Underpinning Contract* - Contrato de Apoio):** Contrato jurídico firmado entre o provedor de TI e um **fornecedor externo terceirizado** (ex.: contrato de link de fibra óptica celebrado com a operadora de telecomunicações, estipulando multas por indisponibilidade).\n"
assert p4 in content, "Pattern 4 not found"
content = content.replace(p4, p4 + q09 + "\n")

# 5. After Section 2.6 item 2 (line ~447)
p5 = "- **RPO (*Recovery Point Objective* - Ponto Objetivo de Recuperação):** Quantidade máxima tolerável de perda de dados expressa em tempo decorrido desde o último backup válido até o momento do incidente. Mede a tolerância à perda de transações.\n"
assert p5 in content, "Pattern 5 not found"
content = content.replace(p5, p5 + q10 + "\n")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("File 12_02 successfully updated!")
