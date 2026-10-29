import os, re

target_file = 'fontes_de_estudo/conhecimentos_especificos_b02_ti/04_engenharia_de_software/03_arquitetura_de_software_e_principios_solid.md'

with open(target_file, 'r', encoding='utf-8') as f:
    content = f.read()

rewrites = {}

rewrites['Teste 023'] = '''### Teste 023
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
O modelo arquitetural "4+1 Visões", concebido por Philippe Kruchten, organiza a descrição de uma arquitetura de software sob diferentes perspectivas de múltiplos *stakeholders*. Em uma auditoria de sistemas de fiscalização, a equipe técnica necessita inspecionar a visão que se destina primordialmente aos desenvolvedores e gerentes de configuração, descrevendo a organização estática dos módulos de código-fonte, pacotes, camadas e gerenciamento de dependências. Essa perspectiva denomina-se Visão:

* **A)** de Desenvolvimento ou de Implementação (*Development/Implementation View*).
* **B)** Lógica (*Logical View*).
* **C)** de Processo (*Process View*).
* **D)** Física ou de Implantação (*Physical/Deployment View*).
* **E)** de Casos de Uso ou Cenários (*Scenarios / +1 View*).


---

> **Comentário Detalhado:**
>
> - **A) CORRETA.** No modelo "4+1" de Kruchten, a **Visão de Desenvolvimento (ou de Implementação)** aborda a organização estática dos módulos de software no ambiente de desenvolvimento: hierarquia de pacotes, bibliotecas, subsistemas, frameworks e código-fonte, tendo como público-alvo prioritário os programadores e engenheiros de software.
> - **B) Incorreta.** A Visão Lógica (*Logical View*) atende aos analistas de negócio e usuários finais, representando as abstrações do domínio, classes, interfaces e diagramas de classes e estados.
> - **C) Incorreta.** A Visão de Processo (*Process View*) foca em integradores e arquitetos de infraestrutura, descrevendo os aspectos dinâmicos de concorrência, threads, sincronização e desempenho em tempo de execução.
> - **D) Incorreta.** A Visão Física ou de Implantação (*Physical/Deployment View*) mapeia a distribuição dos componentes de software sobre a topologia física de hardware, servidores e nós de rede.
> - **E) Incorreta.** A Visão de Cenários (*+1 View*) reúne casos de uso essenciais que ilustram, validam e costuram harmonicamente as quatro outras visões arquiteturais.
>
> **Gabarito: A**'''

rewrites['Teste 024'] = '''### Teste 024
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
Na engenharia de software modular e no projeto arquitetural orientado a objetos, dois conceitos fundamentais que condicionam diretamente a manutenibilidade, testabilidade e elegância técnica do sistema são a Coesão e o Acoplamento. A respeito desses conceitos, assinale a afirmativa tecnicamente correta:

* **A)** A alta coesão indica que os elementos e responsabilidades de um mesmo módulo estão intimamente relacionados a um único propósito conceitual claro e bem delimitado, devendo ser buscada em conjunto com o baixo acoplamento entre módulos distintos.
* **B)** O projeto arquitetural ideal busca módulos com baixo acoplamento e baixa coesão, para que cada classe compartilhe o maior número possível de responsabilidades operacionais.
* **C)** O acoplamento afere a afinidade lógica interna entre os métodos privados de uma mesma classe, devendo ser maximizado para garantir integridade transacional.
* **D)** O alto acoplamento entre subsistemas é altamente desejável em arquiteturas corporativas, pois assegura que alterações em uma classe reflitam compulsoriamente em todos os demais componentes.
* **E)** Módulos com alta coesão dependem compulsoriamente de conexões rígidas com as classes concretas de banco de dados para validar suas regras de negócio.


---

> **Comentário Detalhado:**
>
> - **A) CORRETA.** O princípio mestre da boa arquitetura de software é a busca contínua por **Alta Coesão** (módulos focados em uma única responsabilidade conceitual bem delimitada) e **Baixo Acoplamento** (independência mútua entre módulos, minimizando dependências diretas e permitindo alterações isoladas sem efeitos colaterais em cascata).
> - **B) Incorreta.** Baixa coesão é indesejável (gera classes inchadas com responsabilidades desconexas, conhecidas como *God Classes*).
> - **C) Incorreta.** Inversão: o relacionamento interno entre os elementos de uma mesma classe define a **coesão**; o **acoplamento** mede o grau de interdependência entre classes ou módulos distintos.
> - **D) Incorreta.** O alto acoplamento gera fragilidade e rigidez arquitetural, fazendo com que uma modificação simples propague erros inesperados por todo o sistema.
> - **E) Incorreta.** Alta coesão independe de banco de dados; pelo contrário, conectar o domínio diretamente a tabelas físicas eleva o acoplamento tecnológico e viola o isolamento de camadas.
>
> **Gabarito: A**'''

rewrites['Teste 025'] = '''### Teste 025
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
A Arquitetura Hexagonal (*Ports and Adapters*), idealizada por Alistair Cockburn, consolidou-se como um referencial arquitetural para sistemas corporativos que buscam isolar o núcleo das regras de negócio de tecnologias de persistência, protocolos de rede e interfaces com o usuário. A respeito dos princípios formais dessa arquitetura, é correto afirmar:

* **A)** O núcleo de domínio da aplicação reside no interior do hexágono e interage com o ambiente externo estritamente por meio de Portas (*Ports* - interfaces abstratas), cujas implementações tecnológicas concretas são providas por Adaptadores (*Adapters*).
* **B)** A interface gráfica com o usuário e as bibliotecas de persistência relacional devem ser acopladas diretamente às entidades de domínio para viabilizar auditorias imediatas.
* **C)** O padrão veda a execução de testes unitários automatizados no domínio interno sem a presença ativa de um servidor de aplicação web e banco de dados físico em produção.
* **D)** A arquitetura exige a alocação de seis servidores físicos redundantes para implementar cada um dos vértices do hexágono computacional.
* **E)** As portas e adaptadores somente podem ser empregados se a camada de comunicação externa utilizar exclusivamente mensagens em padrão SOAP com assinatura digital.


---

> **Comentário Detalhado:**
>
> - **A) CORRETA.** Na **Arquitetura Hexagonal (Portas e Adaptadores)**, o domínio central de negócio é completamente agnóstico a detalhes de infraestrutura. Ele se comunica com o mundo exterior por meio de **Portas** (interfaces de entrada/saída) e **Adaptadores** (componentes periféricos que convertem sinais externos — como requisições HTTP, filas Kafka ou repositórios SQL — para as chamadas de método definidas pelas portas).
> - **B) Incorreta.** Viola o princípio basilar da arquitetura, que é exatamente desacoplar o domínio de bancos de dados ou frameworks de interface gráfica.
> - **C) Incorreta.** Uma das maiores vantagens da arquitetura hexagonal é a alta testabilidade: o domínio pode ser integralmente testado por testes unitários puros em memória com *mocks* de portas, sem dependência de servidores web ou bancos reais.
> - **D) Incorreta.** O "hexágono" é uma metáfora visual de desenho lógico, não uma exigência física de hardware ou servidores de rede.
> - **E) Incorreta.** Os adaptadores podem adotar qualquer protocolo (REST, GraphQL, gRPC, CLI, JDBC, etc.), não havendo restrição a SOAP.
>
> **Gabarito: A**'''

rewrites['Teste 026'] = '''### Teste 026
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
No modelo de Arquitetura Orientada a Serviços (SOA), o Barramento Corporativo de Serviços (*Enterprise Service Bus* - ESB) desempenha papel central de infraestrutura na integração de sistemas heterogêneos. Dentre as capacidades e responsabilidades técnicas atribuídas a um ESB em ambientes de alta governança pública, destaca-se:

* **A)** O roteamento inteligente de mensagens, a mediação de serviços e a transformação transparente entre diferentes protocolos e formatos de dados corporativos.
* **B)** A compilação em tempo real e injeção dinâmica de código-fonte nas estações de trabalho de todos os usuários finais do órgão.
* **C)** A eliminação definitiva de sistemas de gerenciamento de banco de dados relacionais em proveito de tabelas gravadas exclusivamente em memória volátil no barramento.
* **D)** A obrigatoriedade de reescrever todas as aplicações legadas da instituição na linguagem Java antes de conectá-las ao barramento.
* **E)** A delegação automática de deliberações decisórias de auditoria a algoritmos não supervisionados sem registro de trilha de auditoria.


---

> **Comentário Detalhado:**
>
> - **A) CORRETA.** Em uma infraestrutura SOA clássica, o **ESB (Enterprise Service Bus)** fornece conectividade desacoplada, oferecendo **roteamento baseado em conteúdo**, **transformação de protocolos e formatos de mensagens** (ex.: converter JSON REST em SOAP XML ou arquivos posicionais), enriquecimento de dados, controle de tráfego e aplicação de políticas de segurança e auditoria corporativa.
> - **B) Incorreta.** O ESB lida com transporte e integração de mensagens entre serviços de backend, não com compilação de código ou injeção em clientes de front-end.
> - **C) Incorreta.** O barramento não substitui bancos de dados; a persistência de dados permanece sob gestão dos serviços e repositórios especialistas de cada aplicação.
> - **D) Incorreta.** Um dos maiores atrativos do ESB é justamente a capacidade de integrar sistemas legados heterogêneos escritos em COBOL, C, .NET, Java, etc., sem necessidade de reescrita da base legada.
> - **E) Incorreta.** Afirmação absurda que colide com princípios de governança, conformidade e rastreabilidade pública.
>
> **Gabarito: A**'''

rewrites['Teste 027'] = '''### Teste 027
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
Em uma arquitetura de microsserviços distribuídos voltada a serviços de auditoria digital, um serviço principal depende de sucessivas chamadas a uma API externa de consulta cadastral. Para evitar que eventuais lentidões severas ou a indisponibilidade dessa API externa provoquem o esgotamento dos recursos de processamento (*thread starvation*) do serviço chamador e desencadeiem falhas em cascata em todo o ecossistema, adota-se um padrão de resiliência que intercepta as invocações. Caso a proporção de falhas ultrapasse um limiar crítico, esse mecanismo interrompe temporariamente as chamadas subsequentes, retornando imediatamente uma resposta alternativa (*fallback*), e passa a monitorar em intervalos programados se o serviço remoto restabeleceu sua operação estável. Esse padrão arquitetural é denominado:

* **A)** Circuit Breaker.
* **B)** API Gateway.
* **C)** Service Registry.
* **D)** Event Sourcing.
* **E)** Command Query Responsibility Segregation (CQRS).


---

> **Comentário Detalhado:**
>
> - **A) CORRETA.** O padrão **Circuit Breaker (Disjuntor)**, popularizado por Michael Nygard em sistemas distribuídos, atua exatamente como um disjuntor elétrico em três estados: **Fechado (*Closed*)** (requisições passam normalmente); **Aberto (*Open*)** (após sucessivas falhas ou latências acima do limiar, as chamadas são bloqueadas de imediato, disparando fallbacks sem onerar a rede ou travar threads); e **Meio-Aberto (*Half-Open*)** (após um tempo de espera, permite um número controlado de chamadas de teste para verificar a recuperação do serviço).
> - **B) Incorreta.** O API Gateway é um ponto único de entrada para clientes externos, responsável por roteamento reverso, agregação de chamadas, autenticação e limitação de taxa (*rate limiting*).
> - **C) Incorreta.** O Service Registry atua como um catálogo de serviços para localização dinâmica de instâncias e balanceamento de carga (*service discovery*).
> - **D) Incorreta.** O Event Sourcing armazena as mudanças de estado da aplicação como uma sequência histórica append-only de eventos de negócio imutáveis.
> - **E) Incorreta.** O CQRS segrega as operações de mutação de dados (Commands) das operações de consulta (Queries) em modelos separados.
>
> **Gabarito: A**'''

rewrites['Teste 028'] = '''### Teste 028
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
A Arquitetura Orientada a Eventos (*Event-Driven Architecture* - EDA) baseia-se na troca assíncrona de estímulos corporativos entre produtores e consumidores de eventos, promovendo alto desacoplamento e escalabilidade. Quando associada ao padrão arquitetural CQRS (*Command Query Responsibility Segregation*), estabelece-se que:

* **A)** as operações de mutação de estado (*Commands*) e as operações de consulta (*Queries*) utilizam modelos conceituais segregados, viabilizando a otimização independente do banco de escrita e dos bancos de leitura.
* **B)** todas as transações de escrita e leitura devem ocorrer obrigatoriamente sobre o mesmo esquema de banco de dados relacional para garantir bloqueio pessimista imediato.
* **C)** os produtores de eventos necessitam manter acoplamento síncrono com o endereço IP de todos os consumidores cadastrados antes de liberar o evento na fila.
* **D)** as operações de consulta (*Queries*) passam a ter a prerrogativa de disparar alterações definitivas no modelo de escrita a fim de atualizar estatísticas de acesso.
* **E)** o padrão veda expressamente o uso de consistência eventual (*eventual consistency*) entre os repositórios de leitura e o repositório principal de comandos.


---

> **Comentário Detalhado:**
>
> - **A) CORRETA.** O padrão **CQRS** (segregação de responsabilidade entre comandos e consultas) divide estruturalmente a aplicação em dois fluxos: o lado de **Escrita/Comandos (*Commands*)**, focado em regras de consistência transacional profunda e validação de negócio; e o lado de **Leitura/Consultas (*Queries*)**, focado em alta velocidade de resposta por meio de visões desnormalizadas, índices especializados e caches, que podem ser sincronizados assincronamente via eventos (EDA).
> - **B) Incorreta.** O objetivo primário do CQRS é justamente libertar a aplicação do modelo único compartilhado de dados para escrita e leitura.
> - **C) Incorreta.** Na arquitetura orientada a eventos, os produtores são desacoplados dos consumidores (publicam no barramento/tópico sem conhecimento da identidade ou endereço dos consumidores).
> - **D) Incorreta.** Princípio estrito de comandos e consultas: consultas nunca devem produzir efeitos colaterais de alteração de estado no domínio (*queries do not change state*).
> - **E) Incorreta.** Pelo contrário: a consistência eventual é o modelo comumente adotado na sincronização assíncrona entre o banco de escrita e as projeções de leitura no CQRS.
>
> **Gabarito: A**'''

rewrites['Teste 029'] = '''### Teste 029
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
Em relação aos estilos arquiteturais para sistemas corporativos, analise as afirmativas a respeito da Arquitetura Orientada a Serviços (SOA) e da Arquitetura de Microsserviços:

I. Na arquitetura SOA clássica, é comum a utilização de um Barramento de Serviços Corporativo (ESB) centralizado que concentra regras de mediação, roteamento e transformação de protocolos complexos.  
II. Na arquitetura de microsserviços, a boa prática de engenharia prescreve o compartilhamento obrigatório de uma única base de dados relacional entre todos os serviços do ecossistema, a fim de assegurar transações atômicas globais imediatas.  
III. A arquitetura de microsserviços privilegia serviços autônomos com ciclos de implantação independentes, pautando-se pelo princípio de *smart endpoints and dumb pipes*, em que a inteligência de negócio reside nos próprios serviços e o transporte de mensagens utiliza mecanismos leves e desacoplados.  

Em relação aos conceitos arquiteturais consagrados na literatura técnica, está correto o que se afirma em:

* **A)** I e III, apenas.
* **B)** I e II, apenas.
* **C)** II e III, apenas.
* **D)** I, II e III.
* **E)** III, apenas.


---

> **Comentário Detalhado:**
>
> - **I. Correta.** SOA tradicionalmente adota um barramento corporativo (ESB) central que orquestra a comunicação, converte formatos de dados pesados (XML/SOAP) e concentra a inteligência da integração corporativa.
> - **II. Incorreta.** Em microsserviços, compartilhar um banco de dados central único (*Database-per-service anti-pattern*) cria um acoplamento oculto severo que inviabiliza implantações independentes e gera gargalos de escala. A recomendação mestre é o padrão **Database-per-Service** (cada microsserviço gerencia privativamente seu próprio banco de dados).
> - **III. Correta.** Princípio cunhado por Martin Fowler: microsserviços adotam *"endpoints inteligentes e canais burros"* (*smart endpoints and dumb pipes*), mantendo a lógica de processamento e validações dentro dos microsserviços e utilizando canais de comunicação leves e padronizados (como HTTP REST ou mensageria Kafka/RabbitMQ).
>
> **Gabarito: A**'''

rewrites['Teste 030'] = '''### Teste 030
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
Durante a revisão de código de um sistema corporativo de gestão de processos administrativos em Java, um Auditor de TI inspecionou uma interface denominada `DispositivoMultifuncional`, que declarava os seguintes métodos: `imprimirDocumento()`, `digitalizarDocumento()`, `enviarFax()` e `grampearFolhas()`. Verificou-se que a classe `ImpressoraBasicaGabinete` implementava essa interface, mas, por tratar-se de um equipamento simples que não possui scanner, módulo de fax nem grampeador mecânico, seu código era forçado a lançar exceções do tipo `UnsupportedOperationException` no corpo dos três últimos métodos. De acordo com os princípios de orientação a objetos SOLID preconizados por Robert C. Martin, essa modelagem viola frontalmente o:

* **A)** Princípio da Segregação de Interfaces (ISP).
* **B)** Princípio da Responsabilidade Única (SRP).
* **C)** Princípio Aberto/Fechado (OCP).
* **D)** Princípio da Inversão de Dependência (DIP).
* **E)** Princípio da Substituição de Liskov (LSP).


---

> **Comentário Detalhado:**
>
> - **A) CORRETA.** O **Princípio da Segregação de Interfaces (ISP - *Interface Segregation Principle*)** estabelece formalmente que *"nenhum cliente deve ser forçado a depender de métodos que não utiliza"*. Em vez de interfaces genéricas e volumosas (*fat interfaces*), o arquiteto deve decompor a interface em contratos menores e específicos (ex.: `Imprimivel`, `Digitalizavel`, `Grampeavel`), permitindo que as classes clientes implementem estritamente as capacidades que de fato possuem.
> - **B) Incorreta.** O SRP dita que uma classe ou módulo deve ter um, e apenas um, motivo para mudar (*single reason to change*).
> - **C) Incorreta.** O OCP estabelece que entidades de software devem estar abertas para extensão, mas fechadas para modificação.
> - **D) Incorreta.** O DIP prescreve que módulos de alto nível não devem depender de módulos de baixo nível, mas sim de abstrações.
> - **E) Incorreta.** O LSP preconiza que objetos de subclasses devem poder substituir objetos da superclasse sem alterar a corretude do sistema (embora o lançamento de UnsupportedOperationException configure um sintoma prático na hierarquia, a raiz direta da má modelagem de contratos inchados é a violação do ISP).
>
> **Gabarito: A**'''

rewrites['Teste 031'] = '''### Teste 031
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
Considere uma classe Java responsável pelo cálculo da tarifa de serviços operacionais em um Tribunal de Contas. O método `calcularTarifa` possui uma estrutura sequencial de instruções condicionais `if-else-if` encadeadas: caso o tipo de procedimento seja "INSPECAO", aplica uma fórmula; se for "AUDITORIA", aplica outra; se for "PERICIA", aplica uma terceira. Sempre que o Tribunal regulamenta uma nova modalidade de procedimento fiscalizatório, os analistas são obrigados a abrir a classe de serviço já testada em produção e adicionar manualmente uma nova cláusula `else-if`. Do ponto de vista dos princípios arquiteturais SOLID, essa estrutura viola diretamente o:

* **A)** Princípio Aberto/Fechado (OCP - *Open/Closed Principle*).
* **B)** Princípio da Substituição de Liskov (LSP - *Liskov Substitution Principle*).
* **C)** Princípio da Segregação de Interfaces (ISP - *Interface Segregation Principle*).
* **D)** Princípio *Don't Repeat Yourself* (DRY).
* **E)** Princípio *You Aren't Gonna Need It* (YAGNI).


---

> **Comentário Detalhado:**
>
> - **A) CORRETA.** O **Princípio Aberto/Fechado (OCP)** dita que *"artefatos de software devem estar abertos para extensão, porém fechados para modificação"*. Quando a introdução de um novo comportamento exige alterar o código-fonte de uma classe pré-existente e estável (adicionando condicionais `if/else` ou `switch`), o princípio é violado. A solução técnica correta é aplicar polimorfismo (por exemplo, com o padrão *Strategy*), criando novas classes especializadas que implementem uma interface comum, estendendo o sistema sem alterar o código estável original.
> - **B) Incorreta.** O LSP assegura que tipos derivados possam substituir perfeitamente seus tipos base sem quebrar o comportamento do programa.
> - **C) Incorreta.** O ISP trata do tamanho e foco de interfaces abstratas, evitando contratos inchados.
> - **D) Incorreta.** DRY combate a duplicação de conhecimento e regras de negócio no sistema.
> - **E) Incorreta.** YAGNI recomenda não implementar recursos antecipadamente até que sejam comprovadamente necessários.
>
> **Gabarito: A**'''

rewrites['Teste 032'] = '''### Teste 032
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
No âmbito das boas práticas de arquitetura e qualidade de código em desenvolvimento de software, os acrônimos DRY (*Don't Repeat Yourself*) e YAGNI (*You Aren't Gonna Need It*) são amplamente referenciados como balizadores de simplificação e manutenibilidade. A respeito da correta fundamentação técnica desses dois princípios, assinale a afirmativa correta:

* **A)** O princípio DRY preconiza que cada porção de conhecimento ou lógica de negócio em um sistema deve possuir uma representação única, não ambígua e definitiva; ao passo que o YAGNI orienta os desenvolvedores a não implementarem funcionalidades ou abstrações antecipadas com base em meras suposições de necessidades futuras.
* **B)** O princípio DRY impede que classes distintas possuam métodos com a mesma assinatura ou nomenclatura; ao passo que o YAGNI proíbe expressamente a utilização de testes unitários automatizados em ambientes de produção.
* **C)** O princípio DRY aplica-se unicamente à padronização de nomenclatura de colunas em bancos de dados relacionais; enquanto o YAGNI recomenda a criação preventiva de tabelas adicionais para acomodar futuras demandas.
* **D)** O princípio YAGNI impõe a obrigatoriedade de reescrever integralmente o código legado a cada ciclo anual; enquanto o DRY determina que todo software público deve ser licenciado em código aberto.
* **E)** Ambos os princípios foram originalmente formulados pela norma ISO 9001 para auditar contratos de aquisição de bens permanentes de TI.


---

> **Comentário Detalhado:**
>
> - **A) CORRETA.** Formulados pela comunidade de engenharia ágil e desenvolvimento pragmático:
>     - **DRY (*Don't Repeat Yourself* - Andy Hunt e Dave Thomas):** Estabelece que toda porção de conhecimento e regra de negócio deve ter uma representação única, autoritativa e não ambígua no sistema, combatendo duplicação de lógica e inconsistências;
>     - **YAGNI (*You Aren't Gonna Need It* - Extreme Programming):** Recomenda implementar apenas o que é estritamente necessário para atender aos requisitos atuais, evitando o desperdício de codificar arquiteturas ou funcionalidades hipotéticas para o futuro ("prematuridade especulativa").
> - **B) Incorreta.** Assinaturas idênticas de métodos em classes diferentes fazem parte do polimorfismo natural; testes automatizados são indispensáveis e incentivados pelo YAGNI/XP.
> - **C) Incorreta.** Distorção completa: criar tabelas preventivas para suposições futuras viola diretamente a essência do YAGNI.
> - **D) Incorreta.** Não há nenhuma regra de reescrita compulsória anual de legado nem obrigatoriedade de licenciamento no teor do DRY/YAGNI.
> - **E) Incorreta.** São princípios de engenharia e boas práticas de codificação artesanal de software (*software craftsmanship*), não cláusulas da norma ISO 9001.
>
> **Gabarito: A**'''

for t_id, block in rewrites.items():
    full_pattern = rf'### {t_id}\s*\n+\*\*[^\n]+\*\*\s*\n+.*?>\s*\*\*Gabarito:\s*[A-E]\*\*'
    match = re.search(full_pattern, content, re.DOTALL)
    if not match:
        print(f'ERRO: Bloco {t_id} nao localizado com regex!')
    else:
        content = content[:match.start()] + block + content[match.end():]
        print(f'SUCESSO: Bloco {t_id} substituido perfeitamente.')

with open(target_file, 'w', encoding='utf-8') as f:
    f.write(content)

print('Arquivo 03_arquitetura_de_software_e_principios_solid.md atualizado com sucesso!')

