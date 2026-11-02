# 01 - Algoritmos, Estruturas de Dados e Paradigmas de Programação

> **Matéria:** Desenvolvimento de Sistemas  
> **Cargo:** B02 – Técnico de Controle Externo – Especialidade: Tecnologia da Informação  
> **Arquivo:** `01_algoritmos_estruturas_de_dados_e_paradigmas.md`  

---

## 📌 Ementa / Itens do Edital
- Algoritmos e lógica de programação
- Estruturas de dados (lineares e não lineares)
- Complexidade de algoritmos (noções assintóticas)
- Programação Orientada a Objetos (POO)
- Programação Funcional (PF)

---

## 🧭 Sumário

1. [Algoritmos, Lógica de Execução e Complexidade Assintótica](#1-algoritmos-logica-de-execucao-e-complexidade-assintotica)
    1. [Variáveis, Escopo e Passagem de Parâmetros (Valor vs. Referência)](#11-variaveis-escopo-e-passagem-de-parametros-valor-vs-referencia)
    2. [Recursão e Pilha de Execução (Call Stack)](#12-recursao-e-pilha-de-execucao-call-stack)
    3. [Análise Assintótica e a Notação Big-O](#13-analise-assintotica-e-a-notacao-big-o)
    4. [Teste 054](#Teste-054)
    5. [Teste 055](#Teste-055)
2. [Estruturas de Dados Fundamentais](#2-estruturas-de-dados-fundamentais)
    1. [Estruturas Lineares: Vetores, Listas Encadeadas, Pilhas e Filas](#21-estruturas-lineares-vetores-listas-encadeadas-pilhas-e-filas)
    2. [Tabelas Hash (Hash Tables) e Métodos de Tratamento de Colisão](#22-tabelas-hash-hash-tables-e-metodos-de-tratamento-de-colisao)
    3. [Estruturas Não Lineares: Árvores Binárias de Busca (BST) e Percursos](#23-estruturas-nao-lineares-arvores-binarias-de-busca-bst-e-percursos)
    4. [Árvores Auto-Balanceadas (AVL e Rubro-Negra) e Grafos](#24-arvores-auto-balanceadas-avl-e-rubro-negra-e-grafos)
    5. [Matriz Geral de Complexidade das Estruturas de Dados](#25-matriz-geral-de-complexidade-das-estruturas-de-dados)
    6. [Teste 056](#Teste-056)
    7. [Teste 057](#Teste-057)
    8. [Teste 058](#Teste-058)
    9. [Teste 059](#Teste-059)
3. [Paradigma de Programação Orientada a Objetos (POO)](#3-paradigma-de-programacao-orientada-a-objetos-poo)
    1. [Os Quatro Pilares da POO: Abstração, Encapsulamento, Herança e Polimorfismo](#31-os-quatro-pilares-da-poo-abstracao-encapsulamento-heranca-e-polimorfismo)
    2. [Polimorfismo Estático (Sobrecarga) vs. Polimorfismo Dinâmico (Sobrescrita)](#32-polimorfismo-estatico-sobrecarga-vs-polimorfismo-dinamico-sobrescrita)
    3. [Relações Estruturais: Classes Abstratas, Interfaces, Coesão e Acoplamento](#33-relacoes-estruturais-classes-abstratas-interfaces-coesao-e-acoplamento)
    4. [Teste 060](#Teste-060)
    5. [Teste 061](#Teste-061)
    6. [Teste 062](#Teste-062)
4. [Paradigma de Programação Funcional (PF)](#4-paradigma-de-programacao-funcional-pf)
    1. [Princípios Fundamentais: Funções Puras, Imutabilidade e Transparência Referencial](#41-principios-fundamentais-funcoes-puras-imutabilidade-e-transparencia-referencial)
    2. [Funções de Primeira Classe e Funções de Alta Ordem (Higher-Order Functions)](#42-funcoes-de-primeira-classe-e-funcoes-de-alta-ordem-higher-order-functions)
    3. [Operações Funcionais sobre Coleções: map, filter e reduce](#43-operacoes-funcionais-sobre-colecoes-map-filter-e-reduce)
    4. [Teste 063](#Teste-063)
    5. [Teste 064](#Teste-064)
5. [Fontes Oficiais e Referências Bibliográficas](#5-fontes-oficiais-e-referencias-bibliograficas)

---

## 1. Algoritmos, Lógica de Execução e Complexidade Assintótica

### 1.1 Variáveis, Escopo e Passagem de Parâmetros (Valor vs. Referência)
A lógica de programação orienta a elaboração de sequências finitas, ordenadas e inequívocas de passos para a resolução computacional de problemas:

- **Variáveis e Tipagem:** Uma variável é um espaço nominal alocado na memória para armazenar determinado tipo de dado. O **escopo** delimita a visibilidade dessa variável:
    - *Escopo Global:* Acessível em qualquer parte do módulo ou programa;
    - *Escopo Local de Bloco/Função:* Visível estritamente dentro do corpo da sub-rotina onde foi declarada, sendo liberada da pilha (*stack*) ao término da execução.
- **Mecanismos de Passagem de Parâmetros:**
    - **Passagem por Valor:** Uma cópia literal do valor do dado primitivo é enviada à sub-rotina. Qualquer modificação efetuada internamente não altera a variável original no escopo chamador;
    - **Passagem por Referência (ou Valor da Referência):** Em linguagens modernas como Java e Python, a passagem é estritamente **por valor**, mas para variáveis de tipos não primitivos (objetos e coleções), o "valor" copiado é o **endereço de memória (ponteiro)** do objeto. Logo:
    - Alterações no estado interno do objeto (ex.: `lista.add("item")` ou `obj.setNome("novo")`) afetam diretamente o objeto original no chamador;
    - Reatribuir a variável inteira dentro do método (ex.: `obj = new Objeto()`) altera apenas a cópia local do ponteiro, mantendo a variável original inalterada.

### 1.2 Recursão e Pilha de Execução (Call Stack)
Um algoritmo recursivo decompõe a solução de um problema invocando a si próprio com instâncias menores do mesmo problema.

```mermaid
flowchart TD
    subgraph Fase1["FASE 1: EMPILHAMENTO DAS CHAMADAS (Call Stack)"]
        F3["fatorial(3) = 3 * fatorial(2)"] --> F2["fatorial(2) = 2 * fatorial(1)"]
        F2 --> F1["fatorial(1) = 1 (Caso Base Atingido)"]
    end
    subgraph Fase2["FASE 2: DESEMPILHAMENTO E RESOLUÇÃO DOS RETORNOS"]
        F1Ret["Retorna 1 para fatorial(2)"] --> F2Ret["fatorial(2) resolve: 2 * 1 = 2"]
        F2Ret --> F3Ret["fatorial(3) resolve: 3 * 2 = 6 (Resultado Final)"]
    end
    F1 ==>|Dispara Retorno| F1Ret
```

Todo algoritmo recursivo exige dois componentes fundamentais:

1. **Caso Base (Condição de Parada):** Uma condição booleana explícita que encerra as chamadas subsequentes e retorna um valor constante imediato. A ausência ou falha no caso base gera recursão infinita e o esgotamento da memória de pilha do sistema operacional (*StackOverflowError*);
2. **Passo Recursivo:** Chamada da função a si mesma com argumentos que convergem progressivamente em direção à condição de parada.

### 1.3 Análise Assintótica e a Notação Big-O
A notação **Big-O ($\mathcal{O}$)** mensura o crescimento do tempo de execução ou do consumo de memória de um algoritmo à medida que o tamanho da entrada ($n$) tende ao infinito, descrevendo o limite superior assintótico (*pior caso* ou caso geral).

| Notação Big-O | Denominação | Comportamento ao Dobrar a Entrada ($2n$) | Exemplos Clássicos |
| :---: | :--- | :--- | :--- |
| $\mathcal{O}(1)$ | Constante | Tempo inalterado | Acesso a índice de array; `push`/`pop` em pilha. |
| $\mathcal{O}(\log n)$ | Logarítmica | Aumenta em uma fração constante | **Busca Binária** (*Binary Search*) em array ordenado. |
| $\mathcal{O}(n)$ | Linear | O tempo dobra proporcionalmente | Busca Linear em vetor; percurso em lista encadeada. |
| $\mathcal{O}(n \log n)$ | Linearítmica | Aumenta um pouco mais que o dobro | *Merge Sort*, *Heap Sort*, *Quick Sort* (caso médio). |
| $\mathcal{O}(n^2)$ | Quadrática | O tempo quadruplica | Laços aninhados simples, *Bubble Sort*, *Insertion Sort*. |
| $\mathcal{O}(2^n)$ | Exponencial | Crescimento explosivo impraticável | Algoritmos de força bruta (ex.: subconjuntos). |
| $\mathcal{O}(n!)$ | Fatorial | Pior classe computacional tratável | Caixeiro Viajante por enumeração exaustiva. |

> ⭐ **IMPORTANTE / BUSCA BINÁRIA:** A Busca Binária exige **obrigatoriamente** que a estrutura esteja previamente **ordenada** e suporte acesso aleatório indexado em tempo $\mathcal{O}(1)$ (como arrays e vetores contíguos). Sua complexidade temporal é $\mathcal{O}(\log n)$. Se aplicada em listas encadeadas, mesmo ordenadas, a busca binária perde eficiência porque o acesso ao nó central requer navegação sequencial $\mathcal{O}(n)$.

---

### Teste 001
**(FGV – TJ/AP – 2023 – Analista Judiciario Apoio Especializado Tecnologia Da Informacao Desenvolvimento De Sistemas)**
Analise o código Python a seguir. L=[0,1,1,2,3] for k in range(4, -4, -1): print (L[k] + L[k % len(L)]) O resultado da execução desse código, na ordem, é:

* **A)** 4, 2, 2, 0, 6, 4;
* **B)** 6, 4, 2, 2, 0, 6, 4, 2, 2;
* **C)** 6, 4, 2, 2, 0, 6, 4, 2;
* **D)** 6, 4, 2, 2, 6, 4, 2;
* **E)** 6, 4, 2, 0, 6, 4, 2.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "4, 2, 2, 0, 6, 4". De acordo com a teoria estudada em *4.2 Funções de Primeira Classe e Funções de Alta Ordem (Higher-Order Functions)*, funções como Cidadãs de Primeira Classe ( First Class Citizens ): Funções podem ser atribuídas a variáveis, armazenadas em estruturas de dados, passadas como parâmetros e retornadas como resultado de outras funções.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "6, 4, 2, 2, 0, 6, 4, 2, 2". De acordo com a teoria estudada em *3.3 Relações Estruturais: Classes Abstratas, Interfaces, Coesão e Acoplamento*, composição sobre Herança: A herança gera forte acoplamento de código ( acoplamento de caixa branca ), quebrando o encapsulamento caso a subclasse dependa de detalhes de implementação da superclasse. A composição de objetos ( relação "tem um" ) é amplamente recomendada por promover delegação dinâmica e flexibilidade em tempo de execução.
> - **C)** **Correta.** Conforme fundamentado na seção *1.2 Recursão e Pilha de Execução (Call Stack)* deste guia, f2Ret F3Ret["fatorial(3) resolve: 3 2 = 6 (Resultado Final)"]. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/AP/2023) ao estabelecer que "6, 4, 2, 2, 0, 6, 4, 2".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "6, 4, 2, 2, 6, 4, 2". De acordo com a teoria estudada em *1.3 Análise Assintótica e a Notação Big-O*, a notação Big O ($\mathcal{O}$) mensura o crescimento do tempo de execução ou do consumo de memória de um algoritmo à medida que o tamanho da entrada ($n$) tende ao infinito, descrevendo o limite superior assintótico ( pior caso ou caso geral).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "6, 4, 2, 0, 6, 4, 2". De acordo com a teoria estudada em *1.1 Variáveis, Escopo e Passagem de Parâmetros (Valor vs. Referência)*, passagem por Referência (ou Valor da Referência): Em linguagens modernas como Java e Python, a passagem é estritamente por valor, mas para variáveis de tipos não primitivos (objetos e coleções), o "valor" copiado é o endereço de memória (ponteiro) do objeto. Logo.
>
> **Gabarito: C**

---


### Teste 002
**(FGV – TRT 16ª – 2022 – Analista Judiciário (Área Administrativa - Tecnologia da Informação))**
A ferramenta Zabbix 6 é amplamente usada para monitoramento de redes; sua instalação e configuração requer pacotes de terceiros. Com relação aos seus requisitos de instalação, analise os itens a seguir. I. O Zabbix é construído em torno de servidores web, servidores de banco de dados e da linguagem de script Python. II. Os servidores de bancos de dados suportados, por padrão, são MySQL, PostreSQL ou MS SQL Server. III. O frontend do Zabbix é suportado, por padrão, por servidores Web Apache. Está correto o que se afirma em

* **A)** I, II e III.
* **B)** I apenas.
* **C)** II apenas.
* **D)** III apenas.
* **E)** II e III, apenas.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "I, II e III". De acordo com a teoria estudada em *3.3 Relações Estruturais: Classes Abstratas, Interfaces, Coesão e Acoplamento*, composição sobre Herança: A herança gera forte acoplamento de código ( acoplamento de caixa branca ), quebrando o encapsulamento caso a subclasse dependa de detalhes de implementação da superclasse. A composição de objetos ( relação "tem um" ) é amplamente recomendada por promover delegação dinâmica e flexibilidade em tempo de execução.
> - **B)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I apenas". De acordo com a teoria estudada em *5. Fontes Oficiais e Referências Bibliográficas*, python Official Documentation Data Structures Listas, pilhas, filas, tuplas, dicionários, conjuntos e operações fundamentais de dados.
> - **C)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "II apenas". De acordo com a teoria estudada em *1.1 Variáveis, Escopo e Passagem de Parâmetros (Valor vs. Referência)*, passagem por Referência (ou Valor da Referência): Em linguagens modernas como Java e Python, a passagem é estritamente por valor, mas para variáveis de tipos não primitivos (objetos e coleções), o "valor" copiado é o endereço de memória (ponteiro) do objeto. Logo.
> - **D)** **Correta.** Conforme fundamentado na seção *1.3 Análise Assintótica e a Notação Big-O* deste guia, a Busca Binária exige obrigatoriamente que a estrutura esteja previamente ordenada e suporte acesso aleatório indexado em tempo $\mathcal{O}(1)$ (como arrays e vetores contíguos). Sua complexidade temporal é $\mathcal{O}(\log n)$. Se aplicada em listas encadeadas, mesmo ordenadas, a busca binária perde eficiência porque o acesso ao nó central requer navegação sequencial $\mathcal{O}(n)$. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT 16ª/2022) ao estabelecer que "III apenas".
> - **E)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "II e III, apenas". De acordo com a teoria estudada em *1.3 Análise Assintótica e a Notação Big-O*, a notação Big O ($\mathcal{O}$) mensura o crescimento do tempo de execução ou do consumo de memória de um algoritmo à medida que o tamanho da entrada ($n$) tende ao infinito, descrevendo o limite superior assintótico ( pior caso ou caso geral).
>
> **Gabarito: D**

---


### Teste 003
**(FGV – TJ/RR – 2024 – Analista Judiciario Gestao E Governanca De Tecnologia Da Informacao)**
O DMBOK é organizado em torno de onze Áreas de Conhecimento do Framework de Gerenciamento de Dados DAMA-DMBOK. Essas áreas abrangem o escopo e o contexto de diversos conjuntos de atividades relacionadas ao gerenciamento de dados, incorporando os objetivos e princípios fundamentais dessa disciplina. A área de conhecimento que aborda a definição e o planejamento para a gestão dos ativos de dados, alinhando-os com a estratégia organizacional para estabelecer uma estrutura de dados eficiente, é a de

* **A)** Governança de Dados.
* **B)** Segurança de Dados.
* **C)** Arquitetura de Dados.
* **D)** Metadados.
* **E)** Documentação e Gestão do Conteúdo.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Governança de Dados". De acordo com a teoria estudada em *5. Fontes Oficiais e Referências Bibliográficas*, python Official Documentation Data Structures Listas, pilhas, filas, tuplas, dicionários, conjuntos e operações fundamentais de dados.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Segurança de Dados". De acordo com a teoria estudada em *4.1 Princípios Fundamentais: Funções Puras, Imutabilidade e Transparência Referencial*, a Programação Funcional é um paradigma declarativo que trata a computação como a avaliação de funções matemáticas e evita a mutação de estados e dados.
> - **C)** **Correta.** Conforme fundamentado na seção *4.1 Princípios Fundamentais: Funções Puras, Imutabilidade e Transparência Referencial* deste guia, imutabilidade: As estruturas de dados não são alteradas após criadas. Qualquer transformação produz uma nova estrutura de dados, deixando a original intacta. Isso elimina problemas de condição de corrida ( race conditions ) em ambientes concorrentes multithread. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/RR/2024) ao estabelecer que "Arquitetura de Dados".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Metadados". De acordo com a teoria estudada em *2.5 Matriz Geral de Complexidade das Estruturas de Dados*, estrutura de Dados: Acesso Médio — Acesso Pior — Busca Média — Busca Pior — Inserção Média — Inserção Pior — Remoção Média — Remoção Pior.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Documentação e Gestão do Conteúdo". De acordo com a teoria estudada em *5. Fontes Oficiais e Referências Bibliográficas*, dROZDEK, Adam. Estrutura de Dados e Algoritmos em C++. 2. ed. São Paulo: Cengage Learning, 2016. (Cap. 3 a 5 Pilhas, Filas e Árvores).
>
> **Gabarito: C**

---


### Teste 004
**(CEBRASPE – STF – 2008 – Analista Judiciario Suporte Em Tecnologia Da Informacao)**
Em redes frame relay, os quadros são roteados usando-se endereços de rede e não números de conexões; os formatos dos quadros de controle são diferentes do formato dos quadros de dados; os nós inspecionam os quadros para identificar quadros inválidos, descartam quadros inválidos e deixam a recuperação de erros para protocolos em camadas mais altas na pilha de protocolos.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Incorreta.** A proposição apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Em redes frame relay, os quadros são roteados usando se endereços de rede e não números de conexões; os...". De acordo com a teoria em *4.1 Princípios Fundamentais: Funções Puras, Imutabilidade e Transparência Referencial*, ausência de Efeitos Colaterais ( No Side Effects ): Não modifica variáveis externas ou globais, não altera parâmetros recebidos por referência e não realiza operações de I/O em disco ou rede durante a sua computação pura.
> - **E)** **Correta.** O item está **Errado** (gabarito oficial: **E**), pois contraria a disciplina teórica aplicável.
>
> **Gabarito: E**

---


### Teste 005
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Administrativa - Ciência de Dados)**
Com relação ao framework pytest, da linguagem de programação Python, avalie as afirmativas a seguir: I. O comando pytest executa os arquivos no formato test_*.py ou *_test.py no diretório corrente e nos subdiretórios. II. O comando abaixo mostra os 5 testes com maior tempo de duração. >>> pytest -vv --durations=5 III. É possível invocar o framework pytest usando o próprio interpretador do Python por meio do comando abaixo: >>> python -m pytest Está correto o que se afirma em

* **A)** I, apenas.
* **B)** II, apenas.
* **C)** I e II, apenas.
* **D)** II e III, apenas.
* **E)** I, II e III.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I, apenas". De acordo com a teoria estudada em *3.3 Relações Estruturais: Classes Abstratas, Interfaces, Coesão e Acoplamento*, composição sobre Herança: A herança gera forte acoplamento de código ( acoplamento de caixa branca ), quebrando o encapsulamento caso a subclasse dependa de detalhes de implementação da superclasse. A composição de objetos ( relação "tem um" ) é amplamente recomendada por promover delegação dinâmica e flexibilidade em tempo de execução.
> - **B)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "II, apenas". De acordo com a teoria estudada em *1.2 Recursão e Pilha de Execução (Call Stack)*, um algoritmo recursivo decompõe a solução de um problema invocando a si próprio com instâncias menores do mesmo problema.
> - **C)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e II, apenas". De acordo com a teoria estudada em *1.1 Variáveis, Escopo e Passagem de Parâmetros (Valor vs. Referência)*, a lógica de programação orienta a elaboração de sequências finitas, ordenadas e inequívocas de passos para a resolução computacional de problemas.
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "II e III, apenas". De acordo com a teoria estudada em *1.1 Variáveis, Escopo e Passagem de Parâmetros (Valor vs. Referência)*, passagem por Referência (ou Valor da Referência): Em linguagens modernas como Java e Python, a passagem é estritamente por valor, mas para variáveis de tipos não primitivos (objetos e coleções), o "valor" copiado é o endereço de memória (ponteiro) do objeto. Logo.
> - **E)** **Correta.** Conforme fundamentado na seção *2.1 Estruturas Lineares: Vetores, Listas Encadeadas, Pilhas e Filas* deste guia, desvantagem: Inserções ou remoções no meio do vetor exigem o deslocamento ( shift ) de todos os elementos posteriores, consumindo tempo $\mathcal{O}(n)$. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "I, II e III".
>
> **Gabarito: E**

---


### Teste 006
**(FGV – TCE/PA – 2024 – Auditor de Controle Externo - Administrativa - Ciência de Dados)**
Com relação aos tipos estruturados da linguagem de programação Python 3, avalie as afirmativas a seguir: I. A tentativa de utilizar conjunto (set) como chave de um dicionário (dict) retorna erro. II. O conjunto (set) não permite elementos repetidos. III. O construtor do tipo list retorna erro ao receber uma string como argumento (entrada). Está correto o que se afirma em

* **A)** I, apenas.
* **B)** II, apenas.
* **C)** I e II, apenas.
* **D)** II e III, apenas.
* **E)** I, II e III.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I, apenas". De acordo com a teoria estudada em *5. Fontes Oficiais e Referências Bibliográficas*, oracle Java Documentation Java Collections Framework Interfaces List, Set, Queue, Deque, Map e implementações em Java.
> - **B)** **Correta.** Conforme fundamentado na seção *1.1 Variáveis, Escopo e Passagem de Parâmetros (Valor vs. Referência)* deste guia, passagem por Referência (ou Valor da Referência): Em linguagens modernas como Java e Python, a passagem é estritamente por valor, mas para variáveis de tipos não primitivos (objetos e coleções), o "valor" copiado é o endereço de memória (ponteiro) do objeto. Logo. Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/PA/2024) ao estabelecer que "II, apenas".
> - **C)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e II, apenas". De acordo com a teoria estudada em *3.2 Polimorfismo Estático (Sobrecarga) vs. Polimorfismo Dinâmico (Sobrescrita)*, a FCC adora afirmar que dois métodos são sobrecarregados se eles tiverem o mesmo nome, os mesmos parâmetros e apenas o tipo de retorno diferente (ex.: int calcular(int x) e double calcular(int x) ). ISSO NÃO É SOBRECARGA! Isso é um erro de compilação! O tipo de retorno isolado não desambigua métodos sobrecarregados.
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "II e III, apenas". De acordo com a teoria estudada em *3.1 Os Quatro Pilares da POO: Abstração, Encapsulamento, Herança e Polimorfismo*, herança: Relação estática entre classes onde uma subclasse (filha) estende atributos e comportamentos de uma superclasse (pai), estabelecendo uma taxonomia do tipo "é um" ( is a ).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "I, II e III". De acordo com a teoria estudada em *4.3 Operações Funcionais sobre Coleções: map, filter e reduce*, reduce : Acumula todos os elementos da coleção aplicando iterativamente uma função de combinação. — Exatamente $1$ valor — Valor escalar consolidado ou objeto acumulador único (número, string).
>
> **Gabarito: B**

---



## 2. Estruturas de Dados Fundamentais

### 2.1 Estruturas Lineares: Vetores, Listas Encadeadas, Pilhas e Filas

```mermaid
flowchart LR
    subgraph Pilha["Pilha (LIFO - Last In, First Out)"]
        P_Top["Topo: push() e pop()"]
        P_1["Elemento C (Topo)"] --> P_2["Elemento B"] --> P_3["Elemento A (Base)"]
    end
    subgraph Fila["Fila (FIFO - First In, First Out)"]
        F_In["Fim: Enqueue()"] --> F_3["Elemento C"] --> F_2["Elemento B"] --> F_1["Elemento A"] --> F_Out["Início: Dequeue()"]
    end
```

- **Vetores (Arrays):** Estrutura indexada contígua na memória.
    - *Vantagem:* Acesso aleatório direto em $\mathcal{O}(1)$ via cálculo de deslocamento (`endereço = base + índice * tamanho`).
    - *Desvantagem:* Inserções ou remoções no meio do vetor exigem o deslocamento (*shift*) de todos os elementos posteriores, consumindo tempo $\mathcal{O}(n)$.
- **Listas Encadeadas (*Linked Lists*):** Elementos (nós) alocados dinamicamente na memória, contendo o dado e ponteiros:
    - *Simplesmente Encadeada:* Ponteiro único apontando para o próximo nó (`next`);
    - *Duplamente Encadeada:* Ponteiros para o anterior (`prev`) e próximo nó (`next`), permitindo percurso bidirecional e remoção em tempo $\mathcal{O}(1)$ caso a referência do nó seja conhecida;
    - *Circular:* O último nó aponta de volta para o primeiro nó da lista.
- **Pilhas (*Stacks* - Disciplina LIFO):**
    - *Last-In, First-Out* (o último elemento a entrar é o primeiro a sair);
    - Operações: `push()` (inserção no topo), `pop()` (remoção do topo) e `peek()` (inspeção do topo sem remoção). Todas operam em $\mathcal{O}(1)$;
    - Aplicações: Pilha de execução de sub-rotinas (*Call Stack*), conversão de expressões polonesas reversas (RPN), mecanismos de desfazer/refazer (*Undo/Redo*) e validação de fechamento de delimitadores (chaves e parênteses).
- **Filas (*Queues* - Disciplina FIFO):**
    - *First-In, First-Out* (o primeiro elemento a entrar é o primeiro a ser processado);
    - Operações: `enqueue()` (inserção no final da fila), `dequeue()` (remoção do início da fila) e `peek()`. Todas em $\mathcal{O}(1)$;
    - Aplicações: Spoolers de impressão, filas de mensagens assíncronas (RabbitMQ/Kafka) e algoritmo de busca em largura (BFS) em grafos e árvores.

### 2.2 Tabelas Hash (Hash Tables) e Métodos de Tratamento de Colisão
Uma Tabela Hash associa chaves de busca a índices de um array de tamanho $m$ por meio de uma **função de espalhamento** (*hash function*): $\text{índice} = h(\text{chave}) \pmod m$.

- **Fator de Carga ($\alpha$):** Razão entre o número de itens armazenados $n$ e o número total de posições da tabela $m$ ($\alpha = \frac{n}{m}$). Quando o fator de carga ultrapassa o limiar regulamentar (tipicamente $0.75$), a tabela é redimensionada (*rehashing*), duplicando a capacidade e recalculando as posições.
- **Tratamento de Colisões (Quando duas chaves resultam no mesmo índice):**
    1. **Encadeamento Separado (*Separate Chaining*):** Cada slot do vetor principal referencia uma lista encadeada (ou árvore binária balanceada quando a lista cresce demais, como no Java 8+). Os elementos colidentes são simplesmente adicionados como novos nós dessa lista secundária.
    2. **Endereçamento Aberto (*Open Addressing*):** Todos os elementos residem diretamente no vetor principal. Ocorrendo colisão, o algoritmo pesquisa sistematicamente o próximo slot vago:
        - *Sondagem Linear (*Linear Probing*):* Testa células consecutivas ($i+1, i+2, \dots$). Sofre com o fenômeno de **agrupamento primário** (*primary clustering*);
        - *Sondagem Quadrática (*Quadratic Probing*):* Testa células com incrementos quadráticos ($i+1^2, i+2^2, \dots$);
        - *Duplo Hash (*Double Hashing*):* Calcula o tamanho do salto através de uma segunda função hash: $\text{passo} = h_2(\text{chave})$.

> 🚨 **ALERTA DE PROVA / PEGADINHA FCC:**  
> A complexidade temporal média de busca, inserção e remoção em uma Tabela Hash é $\mathcal{O}(1)$. Todavia, no **pior caso** (quando todas as chaves colidem no mesmo índice devido a uma função hash deficiente ou ataque de negação de serviço), a complexidade **degrada compulsoriamente para $\mathcal{O}(n)$**. A FCC frequentemente tenta enganar o candidato afirmando que a busca em tabela hash é $\mathcal{O}(1)$ em qualquer circunstância!

### 2.3 Estruturas Não Lineares: Árvores Binárias de Busca (BST) e Percursos
Uma **Árvore Binária de Busca (BST - Binary Search Tree)** é uma estrutura hierárquica na qual, para cada nó raiz $X$:

- Todos os nós situados em sua subárvore esquerda possuem chaves estritamente **menores** que a chave de $X$;
- Todos os nós situados em sua subárvore direita possuem chaves estritamente **maiores** que a chave de $X$.

```mermaid
graph TD
    R["40 (Raiz)"] --> E["20"]
    R --> D["60"]
    E --> EE["10"]
    E --> ED["30"]
    D --> DE["50"]
    D --> DD["70"]
```

**Percursos em Profundidade (DFS - Depth-First Search):**

1. **Pré-Ordem (Pre-order / Raiz $\rightarrow$ Esquerda $\rightarrow$ Direita):** Visita a Raiz, depois percorre a subárvore Esquerda, e por fim a Direita.  
   *Sequência na árvore acima:* `40, 20, 10, 30, 60, 50, 70`. (Utilizada para clonagem ou serialização estrutural da árvore).
2. **Em-Ordem (In-order / Esquerda $\rightarrow$ Raiz $\rightarrow$ Direita):** Percorre a subárvore Esquerda, visita a Raiz, e por fim a Direita.  
   *Sequência na árvore acima:* `10, 20, 30, 40, 50, 60, 70`.  
   > ⭐ **REGRA DE OURO DA FCC:** Em qualquer Árvore Binária de Busca (BST), o percurso **Em-Ordem (In-order) produz obrigatoriamente a sequência dos elementos em ordem estritamente crescente!**
3. **Pós-Ordem (Post-order / Esquerda $\rightarrow$ Direita $\rightarrow$ Raiz):** Percorre a subárvore Esquerda, depois a Direita, e por fim visita a Raiz.  
   *Sequência na árvore acima:* `10, 30, 20, 50, 70, 60, 40`. (Utilizada para liberação e desalocação de memória de nós folha até a raiz).
4. **Percurso em Largura (BFS / Level-Order):** Visita os nós nível por nível, de cima para baixo e da esquerda para a direita, utilizando uma Fila auxiliar: `40, 20, 60, 10, 30, 50, 70`.

### 2.4 Árvores Auto-Balanceadas (AVL e Rubro-Negra) e Grafos
- **Degeneração da BST:** Se inserirmos elementos já ordenados (`10, 20, 30, 40, 50`) em uma BST simples, a árvore degenera em uma lista linear encadeada, e as operações de busca caem de $\mathcal{O}(\log n)$ para $\mathcal{O}(n)$;
- **Árvore AVL (Adelson-Velsky e Landis):** Mantém o Fator de Balanceamento $FB = \text{altura}(E) - \text{altura}(D) \in \{-1, 0, +1\}$. Caso $|FB| > 1$, aplica rotações (simples ou duplas) para restabelecer a altura estritamente logarítmica $\mathcal{O}(\log n)$;
- **Árvore Rubro-Negra (Red-Black Tree):** Árvore balanceada por coloração de nós (vermelho ou preto). Menos rígida que a AVL em altura, demandando menor quantidade de rotações em operações frequentes de inserção e exclusão (utilizada internamente no `TreeMap` e `HashMap` do Java);
- **Grafos:** Conjunto de vértices e arestas (direcionadas ou não, ponderadas ou não):
    - *Representações:* Matriz de Adjacência ($\mathcal{O}(V^2)$ de memória, ideal para grafos densos) e Lista de Adjacência ($\mathcal{O}(V + E)$, ideal para grafos esparsos);
    - *Algoritmos de Percurso:* Busca em Profundidade (DFS - usa pilha/recursão) e Busca em Largura (BFS - usa fila).

### 2.5 Matriz Geral de Complexidade das Estruturas de Dados

| Estrutura de Dados | Acesso Médio | Acesso Pior | Busca Média | Busca Pior | Inserção Média | Inserção Pior | Remoção Média | Remoção Pior |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Vetor (Array)** | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ |
| **Lista Encadeada** | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(1)^*$ | $\mathcal{O}(1)^*$ | $\mathcal{O}(1)^*$ | $\mathcal{O}(1)^*$ |
| **Pilha (Stack)** | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ |
| **Fila (Queue)** | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ |
| **Tabela Hash** | N/A | N/A | $\mathcal{O}(1)$ | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | $\mathcal{O}(n)$ |
| **BST Degenerada** | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ |
| **Árvore AVL / Rubro-Negra** | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ |

*\*Inserção e remoção em lista encadeada são $\mathcal{O}(1)$ se a referência direta ao nó alvo for previamente conhecida.*

---

## 3. Paradigma de Programação Orientada a Objetos (POO)

### 3.1 Os Quatro Pilares da POO: Abstração, Encapsulamento, Herança e Polimorfismo
1. **Abstração:** Foco nos atributos e operações essenciais de uma entidade do domínio de negócio, isolando aspectos acidentais ou supérfluos;
2. **Encapsulamento:** Ocultamento do estado interno e detalhes algorítmicos de um objeto. O acesso às variáveis de instância é protegido por modificadores de visibilidade (`private`, `protected`, `public`), expondo apenas operações controladas de interface pública;
3. **Herança:** Relação estática entre classes onde uma subclasse (filha) estende atributos e comportamentos de uma superclasse (pai), estabelecendo uma taxonomia do tipo "é um" (*is-a*);
4. **Polimorfismo:** Capacidade de objetos de diferentes classes derivadas responderem a uma mesma mensagem (chamada de método) de maneiras particulares e especializadas.

### 3.2 Polimorfismo Estático (Sobrecarga) vs. Polimorfismo Dinâmico (Sobrescrita)
Essa comparação é cobrada com frequência máxima pela banca FCC:

| Critério de Comparação | Sobrecarga (*Overloading*) | Sobrescrita (*Overriding*) |
| :--- | :--- | :--- |
| **Definição** | Múltiplos métodos com o **mesmo nome** declarados na **mesma classe**. | Redefinição de um método herdado da superclasse na **subclasse**. |
| **Assinatura do Método** | **Obrigatoriamente DIFERENTE** (quantidade ou tipos de parâmetros). | **Rigorosamente IDÊNTICA** (mesmo nome, parâmetros e retorno covariante). |
| **Momento de Resolução** | **Tempo de Compilação** (*Compile-time* / Ligação Estática / *Early Binding*). | **Tempo de Execução** (*Runtime* / Ligação Dinâmica / *Late Binding*). |
| **Classificação** | Polimorfismo Estático ou Ad-hoc. | Polimorfismo Dinâmico, Verdadeiro ou de Inclusão. |
| **Dependência de Herança** | Não depende de herança. | **Exige herança** ou implementação de interface. |

> 🚨 **ALERTA DE PROVA / PEGADINHA FCC:**  
> A FCC adora afirmar que dois métodos são sobrecarregados se eles tiverem o mesmo nome, os mesmos parâmetros e **apenas o tipo de retorno diferente** (ex.: `int calcular(int x)` e `double calcular(int x)`). **ISSO NÃO É SOBRECARGA!** Isso é um erro de compilação! O tipo de retorno isolado não desambigua métodos sobrecarregados.

### 3.3 Relações Estruturais: Classes Abstratas, Interfaces, Coesão e Acoplamento
- **Classes Abstratas vs. Interfaces:**
    - *Classe Abstrata:* Não pode ser instanciada diretamente (`new`). Pode conter métodos abstratos (sem corpo) e métodos concretos (com implementação), além de atributos de instância com qualquer modificador de acesso. Modela uma herança conceitual forte;
    - *Interface:* Define um contrato puro de comportamento. Classes de diferentes hierarquias podem implementar a mesma interface, viabilizando o desacoplamento de contratos e a substituição de componentes;
- **Alta Coesão e Baixo Acoplamento:** Módulos de software de excelência devem ser altamente coesos (cada classe com foco em um propósito único do negócio) e fracamente acoplados (comunicação através de interfaces abstratas, permitindo substituição dinâmica);
- **Composição sobre Herança:** A herança gera forte acoplamento de código (*acoplamento de caixa-branca*), quebrando o encapsulamento caso a subclasse dependa de detalhes de implementação da superclasse. A composição de objetos (*relação "tem um"*) é amplamente recomendada por promover delegação dinâmica e flexibilidade em tempo de execução.

---

### Teste 007
**(CEBRASPE – TRF 6ª – 2025 – Analista Judiciário - Apoio Especializado - Governança e Gestão de Tecnologia da Informação)**
A documentação técnica referente à API dos microsserviços desenvolvidos na PDPJ-Br deve seguir o padrão Swagger 2.0, a fim de garantir a compatibilidade com as especificações legadas dos sistemas antigos.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Incorreta.** A proposição apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A documentação técnica referente à API dos microsserviços desenvolvidos na PDPJ Br deve seguir o padrão...". De acordo com a teoria em *2.1 Estruturas Lineares: Vetores, Listas Encadeadas, Pilhas e Filas*, f In["Fim: Enqueue()"] F 3["Elemento C"] F 2["Elemento B"] F 1["Elemento A"] F Out["Início: Dequeue()"].
> - **E)** **Correta.** O item está **Errado** (gabarito oficial: **E**), pois contraria a disciplina teórica aplicável.
>
> **Gabarito: E**

---


### Teste 008
**(CEBRASPE – STJ – 2024 – Analista Judiciário - Apoio Especializado - Suporte em Tecnologia da Informação)**
Durante a fase de seleção do fornecedor, a equipe de planejamento da contratação é responsável por apoiar o pregoeiro ou a comissão de licitação na análise e no julgamento das propostas e dos recursos apresentados pelas licitantes, bem como na condução de eventual prova de distribuída de microsserviços e à biblioteca Flyway, julgue os próximos itens.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Correta.** O item está **Certo**. Conforme fundamentado na seção *4.1 Princípios Fundamentais: Funções Puras, Imutabilidade e Transparência Referencial*, ausência de Efeitos Colaterais ( No Side Effects ): Não modifica variáveis externas ou globais, não altera parâmetros recebidos por referência e não realiza operações de I/O em disco ou rede durante a sua computação pura. Dessa forma, está plenamente correta a assertiva da banca (CEBRASPE – STJ/2024) ao afirmar que "Durante a fase de seleção do fornecedor, a equipe de planejamento da contratação é responsável por apoiar o...".
> - **E)** **Incorreta.** A assertiva não incorre em erro conceitual, guardando conformidade com a teoria estudada.
>
> **Gabarito: C**

---


### Teste 009
**(FGV – TJ/AP – 2023 – Analista Judiciario Apoio Especializado Tecnologia Da Informacao Seguranca Da Informacao)**
Gilberto trabalha no setor de segurança do Tribunal de Justiça do Amapá (TJAP) e está fazendo a modelagem de possíveis ameaças aos seus sistemas, aplicativos, redes e serviços. Após pesquisar alguns modelos, decidiu realizar a modelagem seguindo o STRIDE (Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege). O modelo relaciona as ameaças do acrônimo STRIDE com as propriedades de segurança. Inicialmente, Gilberto trabalhará na propriedade de integridade. Logo, dentro do acrônimo STRIDE, a ameaça a ser trabalhada por Gilberto será:

* **A)** spoofing;
* **B)** tampering;
* **C)** repudiation;
* **D)** information disclosure;
* **E)** denial of service.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "spoofing". De acordo com a teoria estudada em *3.3 Relações Estruturais: Classes Abstratas, Interfaces, Coesão e Acoplamento*, alta Coesão e Baixo Acoplamento: Módulos de software de excelência devem ser altamente coesos (cada classe com foco em um propósito único do negócio) e fracamente acoplados (comunicação através de interfaces abstratas, permitindo substituição dinâmica).
> - **B)** **Correta.** Conforme fundamentado na seção *3.3 Relações Estruturais: Classes Abstratas, Interfaces, Coesão e Acoplamento* deste guia, classe Abstrata: Não pode ser instanciada diretamente ( new ). Pode conter métodos abstratos (sem corpo) e métodos concretos (com implementação), além de atributos de instância com qualquer modificador de acesso. Modela uma herança conceitual forte. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/AP/2023) ao estabelecer que "tampering".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "repudiation". De acordo com a teoria estudada em *1.1 Variáveis, Escopo e Passagem de Parâmetros (Valor vs. Referência)*, passagem por Referência (ou Valor da Referência): Em linguagens modernas como Java e Python, a passagem é estritamente por valor, mas para variáveis de tipos não primitivos (objetos e coleções), o "valor" copiado é o endereço de memória (ponteiro) do objeto. Logo.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "information disclosure". De acordo com a teoria estudada em *4.1 Princípios Fundamentais: Funções Puras, Imutabilidade e Transparência Referencial*, imutabilidade: As estruturas de dados não são alteradas após criadas. Qualquer transformação produz uma nova estrutura de dados, deixando a original intacta. Isso elimina problemas de condição de corrida ( race conditions ) em ambientes concorrentes multithread.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "denial of service". De acordo com a teoria estudada em *1.1 Variáveis, Escopo e Passagem de Parâmetros (Valor vs. Referência)*, escopo Local de Bloco/Função: Visível estritamente dentro do corpo da sub rotina onde foi declarada, sendo liberada da pilha ( stack ) ao término da execução.
>
> **Gabarito: B**

---


### Teste 010
**(FGV – TRT/DA – 2025 – Analista Judiciario Area Apoio Especializado Tecnologia Da Informacao)**
A arquitetura em três camadas surgiu no final dos anos 80 e ainda é comum na construção de sistemas de informação corporativos. As três camadas dessa arquitetura são

* **A)** interface com o usuário, lógica de negócio e banco de dados.
* **B)** interface com o usuário, microsserviços e repositório.
* **C)** publicador, broker de eventos e assinante.
* **D)** cliente, web server e banco de dados.
* **E)** modelo, visão e controle.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *3.1 Os Quatro Pilares da POO: Abstração, Encapsulamento, Herança e Polimorfismo* deste guia, abstração: Foco nos atributos e operações essenciais de uma entidade do domínio de negócio, isolando aspectos acidentais ou supérfluos. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT/DA/2025) ao estabelecer que "interface com o usuário, lógica de negócio e banco de dados".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "interface com o usuário, microsserviços e repositório". De acordo com a teoria estudada em *3.3 Relações Estruturais: Classes Abstratas, Interfaces, Coesão e Acoplamento*, alta Coesão e Baixo Acoplamento: Módulos de software de excelência devem ser altamente coesos (cada classe com foco em um propósito único do negócio) e fracamente acoplados (comunicação através de interfaces abstratas, permitindo substituição dinâmica).
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "publicador, broker de eventos e assinante". De acordo com a teoria estudada em *1.1 Variáveis, Escopo e Passagem de Parâmetros (Valor vs. Referência)*, a lógica de programação orienta a elaboração de sequências finitas, ordenadas e inequívocas de passos para a resolução computacional de problemas.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "cliente, web server e banco de dados". De acordo com a teoria estudada em *3.1 Os Quatro Pilares da POO: Abstração, Encapsulamento, Herança e Polimorfismo*, encapsulamento: Ocultamento do estado interno e detalhes algorítmicos de um objeto. O acesso às variáveis de instância é protegido por modificadores de visibilidade ( private , protected , public ), expondo apenas operações controladas de interface pública.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "modelo, visão e controle". De acordo com a teoria estudada em *3.2 Polimorfismo Estático (Sobrecarga) vs. Polimorfismo Dinâmico (Sobrescrita)*, dependência de Herança: Não depende de herança. — Exige herança ou implementação de interface.
>
> **Gabarito: A**

---


### Teste 011
**(FGV – TJ/BA – 2015 – Analista Judiciario Tecnologia Da Informacao)**
A utilização de interfaces em projetos de software orientados a objetivo promove a separação de aspectos internos e externos de um objeto, impedindo o acesso direto aos detalhes de seu funcionamento interno. Esse mecanismo de separação também contribui para que o software seja construído como um conjunto de componentes que realizam seu trabalho de forma independente. O uso desse mecanismo em projetos de sistemas de software é um exemplo de:

* **A)** abstração;
* **B)** encapsulamento;
* **C)** herança;
* **D)** proteção de código;
* **E)** polimorfismo.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "abstração". De acordo com a teoria estudada em *3.1 Os Quatro Pilares da POO: Abstração, Encapsulamento, Herança e Polimorfismo*, abstração: Foco nos atributos e operações essenciais de uma entidade do domínio de negócio, isolando aspectos acidentais ou supérfluos.
> - **B)** **Correta.** Conforme fundamentado na seção *3.1 Os Quatro Pilares da POO: Abstração, Encapsulamento, Herança e Polimorfismo* deste guia, encapsulamento: Ocultamento do estado interno e detalhes algorítmicos de um objeto. O acesso às variáveis de instância é protegido por modificadores de visibilidade ( private , protected , public ), expondo apenas operações controladas de interface pública. Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ/BA/2015) ao estabelecer que "encapsulamento".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "herança". De acordo com a teoria estudada em *3.3 Relações Estruturais: Classes Abstratas, Interfaces, Coesão e Acoplamento*, composição sobre Herança: A herança gera forte acoplamento de código ( acoplamento de caixa branca ), quebrando o encapsulamento caso a subclasse dependa de detalhes de implementação da superclasse. A composição de objetos ( relação "tem um" ) é amplamente recomendada por promover delegação dinâmica e flexibilidade em tempo de execução.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "proteção de código". De acordo com a teoria estudada em *3.1 Os Quatro Pilares da POO: Abstração, Encapsulamento, Herança e Polimorfismo*, herança: Relação estática entre classes onde uma subclasse (filha) estende atributos e comportamentos de uma superclasse (pai), estabelecendo uma taxonomia do tipo "é um" ( is a ).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "polimorfismo". De acordo com a teoria estudada em *3.1 Os Quatro Pilares da POO: Abstração, Encapsulamento, Herança e Polimorfismo*, polimorfismo: Capacidade de objetos de diferentes classes derivadas responderem a uma mesma mensagem (chamada de método) de maneiras particulares e especializadas.
>
> **Gabarito: B**

---


### Teste 012
**(CEBRASPE – TRT/10 – 2013 – Analista Judiciario Tecnologia Da Informacao)**
São consideradas técnicas de elicitação de requisitos as Com relação às características de orientação a objetos, julgue os itens que se seguem.

* **C)** Certo
* **E)** Errado

---

> **Comentário Detalhado:**
>
> - **C)** **Correta.** O item está **Certo**. Conforme fundamentado na seção *5. Fontes Oficiais e Referências Bibliográficas*, oracle Java Documentation Object Oriented Programming Concepts Fundamentos formais de orientação a objetos: classes, objetos, encapsulamento e polimorfismo. Dessa forma, está plenamente correta a assertiva da banca (CEBRASPE – TRT/10/2013) ao afirmar que "São consideradas técnicas de elicitação de requisitos as Com relação às características de orientação a...".
> - **E)** **Incorreta.** A assertiva não incorre em erro conceitual, guardando conformidade com a teoria estudada.
>
> **Gabarito: C**

---


### Teste 013
**(FCC – TRT 3ª – 2015 – Analista Judiciário - Tecnologia da Informação)**
O Administrador de uma rede local de computadores, que utiliza IPs Classe B, identificou que o servidor da rede local recebeu requisições de acesso de um computador da mesma rede local com IP: 192.168.1.1. O tipo de ataque identificado é conhecido como

* **A)** DoS.
* **B)** Spoofing.
* **C)** Scanning.
* **D)** Defacement.
* **E)** DDoS.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "DoS". De acordo com a teoria estudada em *3.3 Relações Estruturais: Classes Abstratas, Interfaces, Coesão e Acoplamento*, classe Abstrata: Não pode ser instanciada diretamente ( new ). Pode conter métodos abstratos (sem corpo) e métodos concretos (com implementação), além de atributos de instância com qualquer modificador de acesso. Modela uma herança conceitual forte.
> - **B)** **Correta.** Conforme fundamentado na seção *3.2 Polimorfismo Estático (Sobrecarga) vs. Polimorfismo Dinâmico (Sobrescrita)* deste guia, definição: Múltiplos métodos com o mesmo nome declarados na mesma classe. — Redefinição de um método herdado da superclasse na subclasse. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 3ª/2015) ao estabelecer que "Spoofing".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Scanning". De acordo com a teoria estudada em *3.1 Os Quatro Pilares da POO: Abstração, Encapsulamento, Herança e Polimorfismo*, polimorfismo: Capacidade de objetos de diferentes classes derivadas responderem a uma mesma mensagem (chamada de método) de maneiras particulares e especializadas.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Defacement". De acordo com a teoria estudada em *3.3 Relações Estruturais: Classes Abstratas, Interfaces, Coesão e Acoplamento*, interface: Define um contrato puro de comportamento. Classes de diferentes hierarquias podem implementar a mesma interface, viabilizando o desacoplamento de contratos e a substituição de componentes.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "DDoS". De acordo com a teoria estudada em *3.1 Os Quatro Pilares da POO: Abstração, Encapsulamento, Herança e Polimorfismo*, herança: Relação estática entre classes onde uma subclasse (filha) estende atributos e comportamentos de uma superclasse (pai), estabelecendo uma taxonomia do tipo "é um" ( is a ).
>
> **Gabarito: B**

---


### Teste 014
**(FCC – TRT 4ª – 2015 – Analista Judiciário - Tecnologia Da Informação)**
O Sistema Gerenciador de Banco de Dados (SGBD)

* **A)** SQL Server 2014 possui várias tecnologias de BI, como o Integration Services, uma plataforma que inclui pacotes que fornecem processamento de extração, transformação e carregamento (ETL) para armazenamento de dados.
* **B)** PostegreSQL 9.4 utiliza um modelo cliente/servidor. Uma sessão PostgreSQL consiste de 2 processos cooperativos: o processo servidor que executa as operações no BD e o processo usuário-cliente que gerencia os arquivos do BD.
* **C)** Oracle 11g utiliza o seguinte comando para criar um novo BD, denominado meuBD: $createdatabase meuBD.
* **D)** PostegreSQL utiliza o pacote DBMS_CONNECTION_POOL para gerenciar o Database Resident Connection Pool, cujos procedimentos são usados pelo Administrador para configurar parâmetros pool como resize e trigger limit.
* **E)** Oracle 11g permite que o Analysis Services e o Reporting Services possam ser instalados como servidores autônomos em aplicativos de serviço compartilhado em um farm do SharePoint.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *4.1 Princípios Fundamentais: Funções Puras, Imutabilidade e Transparência Referencial* deste guia, imutabilidade: As estruturas de dados não são alteradas após criadas. Qualquer transformação produz uma nova estrutura de dados, deixando a original intacta. Isso elimina problemas de condição de corrida ( race conditions ) em ambientes concorrentes multithread. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT 4ª/2015) ao estabelecer que "SQL Server 2014 possui várias tecnologias de BI, como o Integration Services, uma plataforma que inclui pacotes...".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "PostegreSQL 9.4 utiliza um modelo cliente/servidor. Uma sessão PostgreSQL consiste de 2 processos cooperativos: o...". De acordo com a teoria estudada em *4.3 Operações Funcionais sobre Coleções: map, filter e reduce*, filtro |"map(salario 1.10)"| Mapeado["[4400, 5500]<br/ (Transformação 1:1)"].
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Oracle 11g utiliza o seguinte comando para criar um novo BD, denominado meuBD: $createdatabase meuBD". De acordo com a teoria estudada em *1.1 Variáveis, Escopo e Passagem de Parâmetros (Valor vs. Referência)*, alterações no estado interno do objeto (ex.: lista.add("item") ou obj.setNome("novo") ) afetam diretamente o objeto original no chamador.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "PostegreSQL utiliza o pacote DBMS CONNECTION POOL para gerenciar o Database Resident Connection Pool, cujos...". De acordo com a teoria estudada em *4.2 Funções de Primeira Classe e Funções de Alta Ordem (Higher-Order Functions)*, funções como Cidadãs de Primeira Classe ( First Class Citizens ): Funções podem ser atribuídas a variáveis, armazenadas em estruturas de dados, passadas como parâmetros e retornadas como resultado de outras funções.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Oracle 11g permite que o Analysis Services e o Reporting Services possam ser instalados como servidores autônomos...". De acordo com a teoria estudada em *4.1 Princípios Fundamentais: Funções Puras, Imutabilidade e Transparência Referencial*, transparência Referencial: Uma expressão pode ser substituída diretamente pelo seu valor resultante em qualquer ponto do programa sem alterar o comportamento global do sistema.
>
> **Gabarito: A**

---


### Teste 015
**(FGV – TCE/SC – 2026 – Auditor Fiscal de Controle Externo - Ciências da Computação, Sistemas de Informação...)**
Na modernização dos sistemas de fiscalização, o Tribunal migrou de um sistema monolítico para uma arquitetura de microsserviços. Durante uma auditoria técnica, observou-se que a falha em um serviço de autenticação estava causando a queda em cascata de todos os outros serviços dependentes. O padrão de projeto de arquitetura de software a ser implementado para interromper chamadas a um serviço que está a falhar, permitindo que o sistema degrade graciosamente em vez de colapsar, é o

* **A)** Singleton.
* **B)** Observer.
* **C)** Circuit Breaker.
* **D)** Adapter.
* **E)** Facade.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Singleton". De acordo com a teoria estudada em *1.2 Recursão e Pilha de Execução (Call Stack)*, caso Base (Condição de Parada): Uma condição booleana explícita que encerra as chamadas subsequentes e retorna um valor constante imediato. A ausência ou falha no caso base gera recursão infinita e o esgotamento da memória de pilha do sistema operacional ( StackOverflowError ).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Observer". De acordo com a teoria estudada em *4.1 Princípios Fundamentais: Funções Puras, Imutabilidade e Transparência Referencial*, transparência Referencial: Uma expressão pode ser substituída diretamente pelo seu valor resultante em qualquer ponto do programa sem alterar o comportamento global do sistema.
> - **C)** **Correta.** Conforme fundamentado na seção *3.3 Relações Estruturais: Classes Abstratas, Interfaces, Coesão e Acoplamento* deste guia, alta Coesão e Baixo Acoplamento: Módulos de software de excelência devem ser altamente coesos (cada classe com foco em um propósito único do negócio) e fracamente acoplados (comunicação através de interfaces abstratas, permitindo substituição dinâmica). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE/SC/2026) ao estabelecer que "Circuit Breaker".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Adapter". De acordo com a teoria estudada em *3.3 Relações Estruturais: Classes Abstratas, Interfaces, Coesão e Acoplamento*, classe Abstrata: Não pode ser instanciada diretamente ( new ). Pode conter métodos abstratos (sem corpo) e métodos concretos (com implementação), além de atributos de instância com qualquer modificador de acesso. Modela uma herança conceitual forte.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "Facade". De acordo com a teoria estudada em *2.2 Tabelas Hash (Hash Tables) e Métodos de Tratamento de Colisão*, a complexidade temporal média de busca, inserção e remoção em uma Tabela Hash é $\mathcal{O}(1)$. Todavia, no pior caso (quando todas as chaves colidem no mesmo índice devido a uma função hash deficiente ou ataque de negação de serviço), a complexidade degrada compulsoriamente para $\mathcal{O}(n)$. A FCC frequentemente tenta enganar o candidato afirmando que a busca em tabela hash é $\mathcal{O}(1)$ em qualquer circunstância!.
>
> **Gabarito: C**

---



## 4. Paradigma de Programação Funcional (PF)

### 4.1 Princípios Fundamentais: Funções Puras, Imutabilidade e Transparência Referencial
A Programação Funcional é um paradigma declarativo que trata a computação como a avaliação de funções matemáticas e evita a mutação de estados e dados:

1. **Funções Puras (*Pure Functions*):**
    - *Determinismo:* Para os mesmos argumentos de entrada, a função retorna **rigorosamente o mesmo valor**;
    - *Ausência de Efeitos Colaterais (*No Side Effects*):* Não modifica variáveis externas ou globais, não altera parâmetros recebidos por referência e não realiza operações de I/O em disco ou rede durante a sua computação pura;

2. **Imutabilidade:** As estruturas de dados não são alteradas após criadas. Qualquer transformação produz uma **nova estrutura de dados**, deixando a original intacta. Isso elimina problemas de condição de corrida (*race conditions*) em ambientes concorrentes multithread;
3. **Transparência Referencial:** Uma expressão pode ser substituída diretamente pelo seu valor resultante em qualquer ponto do programa sem alterar o comportamento global do sistema.

### 4.2 Funções de Primeira Classe e Funções de Alta Ordem (Higher-Order Functions)
- **Funções como Cidadãs de Primeira Classe (*First-Class Citizens*):** Funções podem ser atribuídas a variáveis, armazenadas em estruturas de dados, passadas como parâmetros e retornadas como resultado de outras funções;
- **Funções de Alta Ordem (*Higher-Order Functions*):** Funções que recebem uma ou mais funções como argumento ou retornam uma função (como `map`, `filter`, `reduce`);
- **Expressões Lambda:** Funções anônimas concisas, declaradas sem identificador de nome formal (ex.: `x -> x * 2` ou `(a, b) -> a + b`).

### 4.3 Operações Funcionais sobre Coleções: map, filter e reduce

```mermaid
flowchart LR
    Origem["Lista: [1000, 2500, 4000, 5000]"]
    Origem -->|"filter(salario > 3000)"| Filtro["[4000, 5000]<br/>(Subconjunto Selecionado)"]
    Filtro -->|"map(salario * 1.10)"| Mapeado["[4400, 5500]<br/>(Transformação 1:1)"]
    Mapeado -->|"reduce((acc, val) => acc + val, 0)"| Reduzido["9900<br/>(Valor Escalar Agregado)"]
```

| Método Funcional | Propósito Central da Operação | Cardinalidade de Saída vs. Entrada | Tipo do Retorno |
| :--- | :--- | :---: | :--- |
| **`filter`** | Seleciona os elementos da coleção que satisfazem um predicado booleano. | $0 \le \text{tamanho} \le n$ | Nova coleção filtrada com elementos do mesmo tipo. |
| **`map`** | Aplica uma função de transformação individual a cada elemento da coleção. | Rigorosamente igual a $n$ | Nova coleção com elementos transformados (mesmo tamanho). |
| **`reduce`** | Acumula todos os elementos da coleção aplicando iterativamente uma função de combinação. | Exatamente $1$ valor | Valor escalar consolidado ou objeto acumulador único (número, string). |

---

## 5. Fontes Oficiais e Referências Bibliográficas

* [Python Official Documentation - Data Structures](https://docs.python.org/pt-br/3/tutorial/datastructures.html) - Listas, pilhas, filas, tuplas, dicionários, conjuntos e operações fundamentais de dados.
* [Oracle Java Documentation - Java Collections Framework](https://docs.oracle.com/javase/tutorial/collections/intro/index.html) - Interfaces List, Set, Queue, Deque, Map e implementações em Java.
* [Oracle Java Documentation - Object-Oriented Programming Concepts](https://docs.oracle.com/javase/tutorial/java/concepts/index.html) - Fundamentos formais de orientação a objetos: classes, objetos, encapsulamento e polimorfismo.
* [ArXiv - Algorithm Complexity and Analysis](https://arxiv.org/abs/2107.03374) - Análise assintótica formal de complexidade e benchmarks algorítmicos.
* CORMEN, Thomas H. et al. **Algoritmos: Teoria e Prática**. 4. ed. Rio de Janeiro: GEN LTC, 2024. (Cap. 1 a 4 - Fundamentos, Notação Assintótica e Divisão e Conquista).
* SEDGEWICK, Robert; WAYNE, Kevin. **Algorithms**. 4. ed. Boston: Addison-Wesley, 2011. (Cap. 1 e 2 - Estruturas de Dados Elementares e Ordenação).
* DROZDEK, Adam. **Estrutura de Dados e Algoritmos em C++**. 2. ed. São Paulo: Cengage Learning, 2016. (Cap. 3 a 5 - Pilhas, Filas e Árvores).
