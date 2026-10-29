import os, re

target_file = 'fontes_de_estudo/conhecimentos_especificos_b02_ti/04_engenharia_de_software/04_padroes_de_projeto_design_patterns.md'

with open(target_file, 'r', encoding='utf-8') as f:
    content = f.read()

rewrites = {}

rewrites['Teste 033'] = '''### Teste 033
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
O catálogo clássico de padrões de projeto de software formulado pelo *Gang of Four* (GoF) organiza os 23 padrões em duas matrizes classificatórias: o **Propósito** (Criacional, Estrutural ou Comportamental) e o **Escopo** (de Classe ou de Objeto). No que tange ao escopo de **Classe** — no qual as relações entre classes são essencialmente estáticas, fixadas em tempo de compilação prioritariamente por mecanismos de herança —, assinale o padrão criacional GoF que opera genuinamente sob esse escopo:

* **A)** *Factory Method*.
* **B)** *Abstract Factory*.
* **C)** *Singleton*.
* **D)** *Builder*.
* **E)** *Prototype*.


---

> **Comentário Detalhado:**
>
> - **A) CORRETA.** Na taxonomia formal do GoF, o **Factory Method** é o único padrão puramente **criacional de escopo de Classe**. Ele define uma interface para criar um objeto, mas delega a instanciação concreta para subclasses por meio de herança estática em tempo de compilação.
> - **B) Incorreta.** O *Abstract Factory* atua sob escopo de **Objeto**, pois compõe famílias de objetos por meio de delegação e interfaces polimórficas dinâmicas.
> - **C) Incorreta.** O *Singleton* atua sob escopo de **Objeto**, garantindo a existência de uma instância única em tempo de execução.
> - **D) Incorreta.** O *Builder* atua sob escopo de **Objeto**, orquestrando partes de um objeto complexo via delegação (*Director* e *Builder*).
> - **E) Incorreta.** O *Prototype* atua sob escopo de **Objeto**, clonando instâncias dinamicamente em tempo de execução.
>
> **Gabarito: A**'''

rewrites['Teste 034'] = '''### Teste 034
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
Em um projeto de desenvolvimento do novo portal de serviços ao cidadão de um Tribunal de Contas, a arquitetura de front-end deve suportar múltiplos temas visuais e padrões de acessibilidade (por exemplo: Tema Alto Contraste para PCDs e Tema Padrão Institucional). Cada tema é composto por uma família coordenada de componentes visuais integrados (botões, campos de formulário, caixas de diálogo e menus suspensos). Para garantir que a aplicação instancie os elementos visuais de uma família específica sem acoplar o código cliente às classes concretas de cada componente visual, deve-se adotar o padrão GoF:

* **A)** Abstract Factory.
* **B)** Factory Method.
* **C)** Memento.
* **D)** Visitor.
* **E)** State.


---

> **Comentário Detalhado:**
>
> - **A) CORRETA.** O padrão criacional **Abstract Factory (Fábrica Abstrata)** tem como propósito fornecer uma interface única para **criar famílias de objetos relacionados ou dependentes sem especificar suas classes concretas**. É a solução arquitetural ideal para temas visuais, suítes de componentes de interface gráfica ou famílias de drivers de persistência.
> - **B) Incorreta.** O *Factory Method* cria uma única categoria de produto por meio de herança em subclasses, enquanto o *Abstract Factory* orquestra a criação de múltiplos produtos relacionados pertencentes a uma família.
> - **C) Incorreta.** O *Memento* é um padrão comportamental voltado à captura e restauração de estados internos de objetos (*undo*).
> - **D) Incorreta.** O *Visitor* é um padrão comportamental que permite adicionar novas operações a uma estrutura de objetos sem alterar suas classes.
> - **E) Incorreta.** O *State* é um padrão comportamental que altera o comportamento de um objeto conforme suas transições internas de estado.
>
> **Gabarito: A**'''

rewrites['Teste 035'] = '''### Teste 035
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
Considere uma situação em que o sistema eletrônico de auditoria de um Tribunal de Contas necessita construir relatórios analíticos complexos contendo múltiplos blocos heterogêneos opcionais (cabeçalho regimental, matriz de achados, gráficos estatísticos de conformidade, parecer conclusivo e anexos periciais). A equipe de TI deseja separar o algoritmo que orquestra o processo de montagem sequencial do relatório da representação concreta de cada um de seus formatos finais (PDF, HTML5 interativo e planilha de dados), de modo que o mesmo fluxo de montagem possa produzir representações finais distintas. O padrão criacional do GoF que soluciona essa demanda de projeto é o:

* **A)** *Builder*.
* **B)** *Prototype*.
* **C)** *Singleton*.
* **D)** *Decorator*.
* **E)** *Proxy*.


---

> **Comentário Detalhado:**
>
> - **A) CORRETA.** O padrão **Builder (Construtor)** destina-se a **separar a construção de um objeto complexo da sua representação**, de modo que o mesmo processo de montagem (orquestrado pelo *Director*) possa gerar diferentes representações do produto final (implementadas por diferentes classes concretas de *Builder*).
> - **B) Incorreta.** O *Prototype* cria novos objetos clonando instâncias prototípicas pré-configuradas.
> - **C) Incorreta.** O *Singleton* assegura a unicidade de uma única instância em memória, provendo um ponto global de acesso.
> - **D) Incorreta.** O *Decorator* é um padrão estrutural que agrega novas responsabilidades a um objeto dinamicamente em tempo de execução.
> - **E) Incorreta.** O *Proxy* é um padrão estrutural que atua como substituto (*surrogate*) para controlar o acesso a outro objeto.
>
> **Gabarito: A**'''

rewrites['Teste 036'] = '''### Teste 036
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
Durante uma auditoria de sistemas legados, um Auditor de TI constatou a necessidade de integrar um novo módulo web moderno ao subsistema de processamento contábil do órgão, implantado há mais de duas décadas. O subsistema contábil legado é constituído por dezenas de classes interdependentes, com chamadas complexas e APIs de difícil utilização. A equipe de desenvolvimento deseja disponibilizar uma interface unificada, simplificada e de alto nível para os desenvolvedores do novo módulo web, blindando-os da complexidade interna do subsistema legado sem modificar o código-fonte pré-existente. O padrão de projeto estrutural GoF indicado para esse cenário é o:

* **A)** Facade.
* **B)** Decorator.
* **C)** Singleton.
* **D)** Prototype.
* **E)** Chain of Responsibility.


---

> **Comentário Detalhado:**
>
> - **A) CORRETA.** O padrão estrutural **Facade (Fachada)** tem como propósito fornecer uma **interface unificada e simplificada para um conjunto de interfaces de um subsistema**. Ele define uma camada de mais alto nível que torna o subsistema mais fácil de usar, reduzindo drasticamente o acoplamento entre os clientes externos e as múltiplas classes internas complexas.
> - **B) Incorreta.** O *Decorator* adiciona responsabilidades e comportamentos a um objeto dinamicamente, mantendo a mesma interface do componente envelopado.
> - **C) Incorreta.** O *Singleton* é um padrão criacional de instância única, não uma interface de simplificação de subsistemas.
> - **D) Incorreta.** O *Prototype* é um padrão criacional baseado em clonagem de objetos.
> - **E) Incorreta.** O *Chain of Responsibility* é um padrão comportamental para encadear objetos receptores no tratamento de requisições.
>
> **Gabarito: A**'''

rewrites['Teste 037'] = '''### Teste 037
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
Em um sistema de processo eletrônico e gestão documental de um Tribunal de Contas, necessita-se modelar os autos processuais, os quais podem ser constituídos tanto por peças documentais atômicas (certidões, votos, ofícios) quanto por pastas compostas que agregam outras subpastas e documentos avulsos em estruturas hierárquicas em árvore. O requisito arquitetural impõe que o cliente da aplicação possa tratar documentos individuais simples e pastas compostas de forma inteiramente transparente e uniforme, invocando métodos como `assinarDigitalmente()` e `calcularTamanhoBytes()` sem distinguir se o alvo é uma folha única ou um volume composto. O padrão de projeto estrutural GoF que materializa essa estrutura recursiva é o:

* **A)** Composite.
* **B)** Flyweight.
* **C)** Bridge.
* **D)** Mediator.
* **E)** Abstract Factory.


---

> **Comentário Detalhado:**
>
> - **A) CORRETA.** O padrão estrutural **Composite** compõe objetos em estruturas de árvore para representar hierarquias do tipo "parte-todo". Ele permite que os clientes tratem objetos individuais (*Leaf*) e composições de objetos (*Composite*) de maneira **uniforme**, compartilhando uma interface comum de operações recursivas.
> - **B) Incorreta.** O *Flyweight* tem como foco economizar memória através do compartilhamento eficiente de grandes quantidades de objetos granulares de estado intrínseco comum.
> - **C) Incorreta.** O *Bridge* desacopla uma abstração da sua implementação, permitindo que ambas variem independentemente.
> - **D) Incorreta.** O *Mediator* é um padrão comportamental que centraliza as interações complexas entre múltiplos objetos colegas (*colleagues*).
> - **E) Incorreta.** O *Abstract Factory* é um padrão criacional para famílias de produtos.
>
> **Gabarito: A**'''

rewrites['Teste 038'] = '''### Teste 038
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
Considere os dois cenários técnicos a seguir, identificados durante uma auditoria de código-fonte de sistemas judiciais:

Cenário 1: Deseja-se agregar dinamicamente responsabilidades adicionais (como compressão de dados e cálculo de hash de integridade) a instâncias individuais de fluxos de entrada e saída (*Streams*), de forma transparente para o cliente e sem recorrer à explosão de subclasses estáticas por herança.  
Cenário 2: Uma rotina de auditoria consome um objeto volumoso que carrega centenas de megabytes de imagens de notas fiscais digitalizadas do banco de dados; deseja-se postergar a carga pesada desse objeto na memória até o instante exato em que o usuário acione a primeira operação de exibição (*lazy loading*), mantendo um substituto leve que controle esse acesso.  

Os padrões de projeto estruturais do catálogo GoF que atendem com precisão aos Cenários 1 e 2 são, respectivamente:

* **A)** *Decorator* e *Proxy* Virtual.
* **B)** *Facade* e *Bridge*.
* **C)** *Composite* e *Adapter*.
* **D)** *Proxy* de Proteção e *Flyweight*.
* **E)** *Adapter* e *Decorator*.


---

> **Comentário Detalhado:**
>
> - **A) CORRETA.** 
>     - **Cenário 1:** O padrão **Decorator (Decorador)** anexa responsabilidades adicionais a um objeto dinamicamente. Oferece uma alternativa flexível ao uso de subclasses para extensão de funcionalidade em tempo de execução (típico da biblioteca `java.io`, ex.: `BufferedOutputStream(GZIPOutputStream(FileOutputStream))`);
>     - **Cenário 2:** O padrão **Proxy Virtual** atua como um procurador/substituto leve para um objeto real pesado, interceptando as requisições e adiando a sua criação ou instanciação em memória até o momento da real necessidade (*lazy initialization*).
> - **B) Incorreta.** O *Facade* cria uma interface simplificada para um subsistema e o *Bridge* desacopla abstração e implementação.
> - **C) Incorreta.** O *Composite* organiza hierarquias em árvore e o *Adapter* converte a interface de uma classe em outra esperada pelo cliente.
> - **D) Incorreta.** O *Proxy de Proteção* controla direitos de acesso/permissões de segurança, não lazy loading; *Flyweight* lida com economia de memória por compartilhamento massivo de objetos idênticos.
> - **E) Incorreta.** Apresenta os papéis invertidos em relação aos cenários propostos.
>
> **Gabarito: A**'''

rewrites['Teste 039'] = '''### Teste 039
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
Em um sistema de auditoria de compras públicas, o módulo de fiscalização financeira precisa liquidar sanções contratuais aplicando fórmulas de cálculo distintas (multa de mora diária, multa rescisória e glosa de faturamento), as quais são selecionadas dinamicamente dependendo da gravidade e da tipicidade da infração cometida pela contratada. O arquiteto de software determinou que novas fórmulas de sanção possam ser incorporadas no futuro sem que seja necessário alterar a classe de fiscalização existente e sem recorrer a blocos aninhados de instruções condicionais `if-else` ou `switch`. O padrão de projeto comportamental GoF concebido para encapsular cada algoritmo em classes autônomas e torná-los intercambiáveis pelo cliente em tempo de execução é o:

* **A)** Strategy.
* **B)** Template Method.
* **C)** Observer.
* **D)** Builder.
* **E)** Proxy.


---

> **Comentário Detalhado:**
>
> - **A) CORRETA.** O padrão comportamental **Strategy (Estratégia)** define uma família de algoritmos, encapsula cada um deles em uma classe isolada e os torna **intercambiáveis**. Permite que o algoritmo varie independentemente dos clientes que o utilizam, materializando o Princípio Aberto/Fechado (OCP) ao eliminar extensas estruturas condicionais de desvio (`switch-case`).
> - **B) Incorreta.** O *Template Method* define o esqueleto de um algoritmo em um método na superclasse, delegando etapas específicas para subclasses por meio de herança, enquanto o *Strategy* usa composição/delegação com algoritmos totalmente intercambiáveis em tempo de execução.
> - **C) Incorreta.** O *Observer* estabelece notificações de mudança de estado em dependência um-para-muitos.
> - **D) Incorreta.** O *Builder* é um padrão criacional para construção de objetos complexos em etapas.
> - **E) Incorreta.** O *Proxy* é um padrão estrutural que controla o acesso a um objeto.
>
> **Gabarito: A**'''

rewrites['Teste 040'] = '''### Teste 040
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
O padrão de projeto comportamental Observer é frequentemente empregado em arquiteturas orientadas a eventos e no desenvolvimento de interfaces gráficas para desacoplar as entidades que alteram seu estado interno das classes que necessitam reagir a essa mutação. A respeito da mecânica estrutural e conceitual do padrão Observer segundo o GoF, é correto afirmar:

* **A)** Estabelece uma dependência do tipo "um-para-muitos" entre objetos, de forma que quando o estado do objeto sujeito (*Subject*) se modifica, todos os seus observadores dependentes (*Observers*) são notificados e atualizados automaticamente.
* **B)** Exige que o objeto sujeito mantenha referências concretas e conheça a implementação interna detalhada de cada classe observadora cadastrada.
* **C)** Restringe o número de ouvintes a no máximo dois observadores cadastrados simultaneamente por objeto monitorado.
* **D)** Fundamenta-se em herança múltipla obrigatória para injetar os comportamentos de notificação diretamente no núcleo do sistema operacional.
* **E)** Opera exclusivamente sob o modelo síncrono bloqueante no escopo de Classe, sendo vedada sua implementação por meio de interfaces abstratas de retorno (*callbacks*).


---

> **Comentário Detalhado:**
>
> - **A) CORRETA.** É a definição oficial do padrão **Observer**: define uma dependência do tipo um-para-muitos entre objetos, de modo que quando um objeto (o *Subject*) muda de estado, todos os seus dependentes (os *Observers*) são **automaticamente notificados e atualizados**. A comunicação dá-se por meio de uma interface abstrata de observador, mantendo o sujeito desvinculado das classes concretas que o monitoram.
> - **B) Incorreta.** O sujeito conhece os observadores unicamente através de uma interface genérica abstrata (`Observer`), operando com acoplamento fraco.
> - **C) Incorreta.** Não há limitação quantitativa; o sujeito mantém uma lista dinâmica que suporta qualquer número de observadores inscritos.
> - **D) Incorreta.** O padrão utiliza composição/delegação simples de objetos (lista de inscritos), prescindindo de herança múltipla ou acoplamento a sistemas operacionais.
> - **E) Incorreta.** O Observer é um padrão de escopo de **Objeto**, amplamente utilizado tanto em modelos síncronos quanto em arquiteturas assíncronas de eventos (*pub/sub*).
>
> **Gabarito: A**'''

rewrites['Teste 041'] = '''### Teste 041
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
No catálogo de padrões comportamentais do GoF, o padrão cuja intenção oficial consagrada é *"evitar o acoplamento do remetente de uma requisição ao seu destinatário, dando a mais de um objeto a oportunidade de tratar a requisição, encadeando os objetos receptores e passando a requisição ao longo da cadeia até que um deles a processe"* denomina-se:

* **A)** *Chain of Responsibility*.
* **B)** *Command*.
* **C)** *Mediator*.
* **D)** *Observer*.
* **E)** *Visitor*.


---

> **Comentário Detalhado:**
>
> - **A) CORRETA.** Definição literal da especificação canônica do **Chain of Responsibility (Cadeia de Responsabilidade)**: evita o acoplamento do remetente ao destinatário ao criar uma linha sequencial de receptores em que cada elo da cadeia decide se processa a solicitação ou a propaga para o próximo elo. Muito utilizado em filtros web (ex.: `FilterChain` do Java EE), autenticação e fluxos de aprovação de despesas em cascata.
> - **B) Incorreta.** O *Command* encapsula uma requisição como um objeto, permitindo parametrização de clientes, enfileiramento de operações e suporte a operações reversíveis (*undo*).
> - **C) Incorreta.** O *Mediator* encapsula como um conjunto de objetos interage, centralizando as comunicações para evitar que classes façam referências explícitas umas às outras.
> - **D) Incorreta.** O *Observer* notifica múltiplos dependentes sobre mudanças de estado de um sujeito central.
> - **E) Incorreta.** O *Visitor* permite definir uma nova operação sem mudar as classes dos elementos sobre os quais opera.
>
> **Gabarito: A**'''

rewrites['Teste 042'] = '''### Teste 042
**(Questão Inédita / Simulada Estilo FCC – Nível: Controle Externo / TI)**  
Em um sistema de auditoria eletrônica de dados fiscais, os auditores executam operações complexas de simulação de cruzamento de dados. Para garantir segurança operacional, a aplicação deve disponibilizar a funcionalidade de "Desfazer" (*Undo*), permitindo restaurar o estado integral do documento pericial a um ponto anterior de verificação (*checkpoint*). A exigência do projeto de software é que o estado interno do documento possa ser capturado e posteriormente recuperado sem expor sua estrutura privada ou violar o princípio do encapsulamento. O padrão comportamental GoF que soluciona essa demanda técnica é o:

* **A)** *Memento*.
* **B)** *State*.
* **C)** *Template Method*.
* **D)** *Prototype*.
* **E)** *Flyweight*.


---

> **Comentário Detalhado:**
>
> - **A) CORRETA.** O padrão **Memento (Lembrança)** atende expressamente a esse requisito: ele captura e externaliza o estado interno de um objeto (o *Originator*) em um objeto memento sem quebrar ou expor seu encapsulamento, de modo que o objeto possa ser restaurado a esse estado posteriormente, sendo gerenciado por um zelador (*Caretaker*).
> - **B) Incorreta.** O *State* altera o comportamento de um objeto quando seu estado interno se modifica, comportando-se como se a classe do objeto tivesse mudado.
> - **C) Incorreta.** O *Template Method* define o esqueleto de um algoritmo em uma superclasse abstrata, postergando etapas para subclasses.
> - **D) Incorreta.** O *Prototype* é um padrão criacional para clonagem de instâncias pré-configuradas.
> - **E) Incorreta.** O *Flyweight* é um padrão estrutural de otimização de memória por compartilhamento de estado.
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

print('Arquivo 04_padroes_de_projeto_design_patterns.md atualizado com sucesso!')

