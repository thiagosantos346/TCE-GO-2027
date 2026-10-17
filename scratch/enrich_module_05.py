# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from enricher_base import inject_questions_into_file

# ==========================================
# FILE 1: 01_algoritmos_estruturas_de_dados_e_paradigmas.md
# ==========================================
file_1 = "fontes_de_estudo/conhecimentos_especificos_b02_ti/05_desenvolvimento_de_sistemas/01_algoritmos_estruturas_de_dados_e_paradigmas.md"
injections_1 = [
    {
        "target_sec": "### 1.2 Recursão e Pilha de Execução (Call Stack)",
        "question_text": """### Questão 06
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
A recursão é uma técnica algorítmica fundamental na qual uma função invoca a si mesma para resolver subproblemas menores de mesma natureza. A respeito do funcionamento da recursão e de sua pilha de execução (*Call Stack*), é correto afirmar:

* **A)** Toda função recursiva deve possuir pelo menos uma condição de parada (caso base), sob pena de provocar um estouro de pilha (*Stack Overflow*) em virtude de chamadas infinitas.
* **B)** A execução de uma chamada recursiva não consome espaço na memória RAM, pois todas as variáveis locais utilizam o mesmo endereço físico de registradores da CPU.
* **C)** Algoritmos recursivos são sempre mais velozes e consomem menos memória do que suas versões iterativas equivalentes.
* **D)** A pilha de chamadas (*Call Stack*) opera sob o princípio FIFO (*First-In, First-Out*), finalizando primeiro a primeira função chamada.
* **E)** A recursão em cauda (*tail recursion*) impede que o compilador realize qualquer otimização de espaço na pilha de execução.

> **Comentário Detalhado:**
>
> - **A) Correta.** Sem o caso base (condição de parada), a função empilha novos registros de ativação indefinidamente até esgotar o limite da pilha de execução, gerando *Stack Overflow*.
> - **B) Incorreta.** Cada invocação recursiva aloca um novo quadro (*stack frame*) na pilha com suas variáveis e endereço de retorno.
> - **C) Incorreta.** Funções recursivas geralmente apresentam *overhead* de empilhamento e desempilhamento de frames, sendo frequentemente mais lentas que laços iterativos simples.
> - **D) Incorreta.** A pilha opera sob o princípio LIFO (*Last-In, First-Out*); a última função chamada é a primeira a retornar.
> - **E) Incorreta.** A recursão em cauda (*tail call optimization*) permite que compiladores reutilizem o frame atual sem alocar novos frames na pilha.
>
> **Gabarito: A**"""
    },
    {
        "target_sec": "### 1.3 Análise Assintótica e a Notação Big-O",
        "question_text": """### Questão 07
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
A análise assintótica de complexidade de algoritmos permite quantificar o crescimento do consumo de tempo de execução e memória à medida que o tamanho da entrada ($n$) cresce assintoticamente. Em relação aos algoritmos clássicos de ordenação de vetores em memória interna, é correto afirmar que:

* **A)** O algoritmo *Bubble Sort* possui complexidade de tempo de pior caso igual a $O(n \\log n)$.
* **B)** O algoritmo *Merge Sort* baseia-se no paradigma de divisão e conquista e possui complexidade de tempo no pior caso estritamente delimitada por $O(n \\log n)$.
* **C)** O *Quicksort* garante complexidade de tempo $O(n)$ em qualquer cenário de partição de pivôs.
* **D)** O pior caso de tempo do *Quicksort* ocorre com complexidade de tempo $O(\\log n)$.
* **E)** Todos os algoritmos de ordenação baseados em comparação de chaves conseguem ordenar um vetor em tempo linear $O(n)$ no pior caso.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** O *Bubble Sort* tem complexidade de pior caso quadrática: $O(n^2)$.
> - **B) Correta.** O *Merge Sort* divide recursivamente o vetor ao meio e intercala as metades ordenadas, garantindo complexidade $O(n \\log n)$ em todos os cenários (melhor, médio e pior caso).
> - **C) Incorreta.** O *Quicksort* tem complexidade média $O(n \\log n)$, mas pode degradar para $O(n^2)$ no pior caso.
> - **D) Incorreta.** O pior caso do *Quicksort* é quadrático: $O(n^2)$.
> - **E) Incorreta.** O limite inferior matemático teórico para ordenação por comparação é $\\Omega(n \\log n)$.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 2.4 Árvores Auto-Balanceadas (AVL e Rubro-Negra) e Grafos",
        "question_text": """### Questão 08
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
Uma Árvore AVL é uma Árvore Binária de Busca (BST) estritamente auto-balanceada na qual a diferença de altura entre as subárvores esquerda e direita de qualquer nó (fator de balanceamento $FB = h_{esq} - h_{dir}$) deve pertencer obrigatoriamente ao conjunto:

* **A)** $\\{-2, 0, +2\\}$
* **B)** $\\{-1, 0, +1\\}$
* **C)** $\\{0, 1, 2\\}$
* **D)** $\\{-3, 0, +3\\}$
* **E)** $\\{1, 2, 3\\}$

> **Comentário Detalhado:**
>
> - **A) Incorreta.** Um fator de balanceamento em $\\pm 2$ indica que a árvore perdeu o equilíbrio e exige uma rotação imediata de rebalanceamento.
> - **B) Correta.** Na definição canônica de Adelson-Velsky e Landis (AVL), o fator de balanceamento de cada nó deve ser $-1, 0$ ou $+1$. Se uma inserção ou remoção resultar em $FB = \\pm 2$, executam-se rotações (simples ou duplas) para restaurar a invariante de equilíbrio em tempo $O(\\log n)$.
> - **C) Incorreta.** Fatores de balanceamento negativos são válidos e necessários quando a subárvore direita é mais alta.
> - **D) Incorreta.** Valores acima de 1 violam a propriedade da árvore AVL.
> - **E) Incorreta.** Viola a definição canônica da AVL.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 3.1 Os Quatro Pilares da POO: Abstração, Encapsulamento, Herança e Polimorfismo",
        "question_text": """### Questão 09
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
No paradigma de Programação Orientada a Objetos, o pilar que estabelece a técnica de ocultar os detalhes internos de implementação e o estado de um objeto, restringindo o acesso direto aos seus atributos e expondo apenas uma interface pública controlada de métodos, denomina-se:

* **A)** Herança múltipla.
* **B)** Polimorfismo paramétrico.
* **C)** Encapsulamento.
* **D)** Sobrecarga de operadores.
* **E)** Coesão temporal.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** Herança é o mecanismo pelo qual classes filhas herdam características de classes mães.
> - **B) Incorreta.** Polimorfismo paramétrico refere-se a tipos genéricos (*generics*).
> - **C) Correta.** O **Encapsulamento** oculta o estado interno e a representação de dados do objeto (*information hiding*), protegendo a integridade contra manipulação indevida externa.
> - **D) Incorreta.** Sobrecarga permite redefinir operadores ou métodos com assinaturas distintas.
> - **E) Incorreta.** Coesão temporal é um nível fraco de coesão procedimental.
>
> **Gabarito: C**"""
    },
    {
        "target_sec": "### 3.3 Relações Estruturais: Classes Abstratas, Interfaces, Coesão e Acoplamento",
        "question_text": """### Questão 10
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
A respeito das distinções conceituais entre Classes Abstratas e Interfaces na modelagem orientada a objetos clássica, é correto afirmar:

* **A)** Interfaces podem ser instanciadas diretamente por meio do operador `new`, ao passo que classes abstratas nunca podem conter código compilado.
* **B)** Uma classe concreta pode herdar de múltiplas classes abstratas em Java, mas pode implementar apenas uma única interface.
* **C)** Uma classe abstrata não pode ser instanciada diretamente e pode conter tanto métodos abstratos (sem corpo) quanto métodos concretos com implementação completa e estado (atributos de instância).
* **D)** Interfaces são obrigadas a implementar todos os métodos de persistência no banco de dados.
* **E)** Classes abstratas são usadas exclusivamente para definir variáveis de escopo global no sistema operacional.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** Nem interfaces nem classes abstratas podem ser instanciadas diretamente com `new`.
> - **B) Incorreta.** Em linguagens como Java e C#, há herança simples de classes (apenas uma superclasse) e herança múltipla de interfaces (implementação de múltiplas interfaces).
> - **C) Correta.** Classes abstratas servem como base arquitetural de extensão: não permitem instanciação direta, mas oferecem código reutilizável (métodos concretos e atributos de instância) juntamente com contratos a serem implementados pelas subclasses.
> - **D) Incorreta.** Interfaces estabelecem contratos de comportamento, sem qualquer obrigatoriedade com persistência.
> - **E) Incorreta.** Conceito totalmente descabido.
>
> **Gabarito: C**"""
    },
    {
        "target_sec": "### 4.1 Princípios Fundamentais: Funções Puras, Imutabilidade e Transparência Referencial",
        "question_text": """### Questão 11
**(FGV – TJ – Analista Judiciário / Tecnologia da Informação)**  
No paradigma de Programação Funcional (PF), uma função é considerada **pura** (*pure function*) quando satisfaz a dois critérios rigorosos:

* **A)** Altera variáveis globais do sistema e consome dados de sensores de hardware aleatórios a cada execução.
* **B)** Produz o mesmo valor de saída para os mesmos argumentos de entrada e não gera efeitos colaterais (*side effects*) observáveis no ambiente externo.
* **C)** Executa exclusivamente operações de escrita síncrona em bancos de dados relacionais transacionais.
* **D)** Depende do horário do relógio da CPU e de geradores de números pseudoaleatórios para calcular seu resultado.
* **E)** Exige que todos os parâmetros sejam passados obrigatoriamente por referência com permissão de escrita.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** Funções puras não geram nem dependem de efeitos colaterais como modificação de variáveis globais.
> - **B) Correta.** A pureza funcional exige determinismo estrito (mesmas entradas $\\rightarrow$ mesma saída) e ausência de efeitos colaterais (sem alteração de estado mutável externo ou I/O não controlado), garantindo a **transparência referencial**.
> - **C) Incorreta.** Operações de escrita em banco são efeitos colaterais clássicos de I/O.
> - **D) Incorreta.** Consultar relógio ou números aleatórios torna a função impura e não determinística.
> - **E) Incorreta.** O paradigma funcional baseia-se na **imutabilidade** dos dados.
>
> **Gabarito: B**"""
    }
]

# ==========================================
# FILE 2: 02_linguagens_java_javascript_nodejs_python.md
# ==========================================
file_2 = "fontes_de_estudo/conhecimentos_especificos_b02_ti/05_desenvolvimento_de_sistemas/02_linguagens_java_javascript_nodejs_python.md"
injections_2 = [
    {
        "target_sec": "### 1.2 Gerenciamento de Memória: Stack vs. Heap e Garbage Collection",
        "question_text": """### Questão 06
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
Na Máquina Virtual Java (JVM), o gerenciamento de memória divide-se principalmente entre a memória *Stack* (Pilha) e a memória *Heap*. A respeito da organização e do ciclo de vida dos dados nessas áreas, é correto afirmar:

* **A)** Todas as instâncias de objetos criadas via operador `new` são alocadas na memória *Heap*, enquanto as variáveis locais de tipos primitivos e as referências aos objetos residem na memória *Stack*.
* **B)** A memória *Stack* é compartilhada por todas as threads da JVM, sendo limpa exclusivamente pelo *Garbage Collector*.
* **C)** Os objetos instanciados na *Heap* são desalocados imediatamente no instante exato em que a chave de fechamento do método atual é executada.
* **D)** O *Garbage Collector* da JVM varre e gerencia a memória *Stack*, mas nunca atua sobre os objetos da *Heap*.
* **E)** A memória *Heap* opera sob a política de primeiro a entrar, primeiro a sair (FIFO), impedindo o reaproveitamento de blocos liberados.

> **Comentário Detalhado:**
>
> - **A) Correta.** Na arquitetura da JVM, a *Stack* armazena frames de métodos, tipos primitivos locais e ponteiros de referência; todos os objetos instanciados residem dinamicamente na *Heap*.
> - **B) Incorreta.** Cada thread possui sua própria *Stack* privada; a *Heap* é que é compartilhada globalmente por todas as threads.
> - **C) Incorreta.** Objetos na *Heap* permanecem vivos até que não haja mais referências ativas a eles a partir do grafo de raízes (*GC Roots*), sendo coletados de forma assíncrona pelo *Garbage Collector*.
> - **D) Incorreta.** O *Garbage Collector* gerencia primordialmente a memória *Heap*; a *Stack* é liberada automaticamente no retorno de cada função.
> - **E) Incorreta.** A *Heap* é organizada em gerações (*Young*, *Old/Tenured*) e não segue disciplina FIFO de fila.
>
> **Gabarito: A**"""
    },
    {
        "target_sec": "### 1.6 Java Collections Framework: List, Set, Queue e Map",
        "question_text": """### Questão 07
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
No *Java Collections Framework*, as três interfaces fundamentais de coleção (`List`, `Set` e `Map`) apresentam características estruturais distintas. A respeito dessas estruturas, é correto afirmar:

* **A)** A interface `Set` permite armazenar elementos duplicados e garante a recuperação estrita na ordem exata de inserção em todas as suas implementações.
* **B)** A interface `List` representa uma coleção ordenada que admite elementos duplicados e permite o acesso posicional aos elementos por meio de índices inteiros.
* **C)** A classe `HashMap` proíbe o armazenamento de valores nulos e garante que as chaves fiquem automaticamente ordenadas alfabeticamente.
* **D)** A classe `TreeSet` não exige que seus elementos implementem a interface `Comparable` ou utilizem um `Comparator`.
* **E)** As chaves de um `Map` podem conter elementos repetidos, desde que seus valores associados sejam estritamente nulos.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** `Set` não permite elementos duplicados; implementações como `HashSet` não garantem ordem alguma.
> - **B) Correta.** `List` é uma sequência ordenada (*index-based*) que aceita elementos duplicados e permite consultas diretas via índice (como `get(i)`).
> - **C) Incorreta.** `HashMap` permite uma chave nula e múltiplos valores nulos, e não garante ordenação (a classe que ordena é `TreeMap`).
> - **D) Incorreta.** `TreeSet` ordena seus elementos com base na ordem natural (`Comparable`) ou em um `Comparator` explícito.
> - **E) Incorreta.** As chaves de um `Map` são únicas (comportam-se como um `Set`).
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 2.2 Tipos de Dados, Coerção e Operadores de Igualdade (`==` vs. `===`)",
        "question_text": """### Questão 08
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
Em JavaScript moderno, a comparação de valores pode ser realizada por meio do operador de igualdade abstrata (`==`) ou do operador de igualdade estrita (`===`). Considere as seguintes expressões avaliadas pelo interpretador JavaScript:  

I. `5 == "5"`  
II. `5 === "5"`  
III. `null === undefined`  

Os valores booleanos resultantes da avaliação das expressões I, II e III são, respectivamente:

* **A)** `true`, `true` e `true`
* **B)** `true`, `false` e `false`
* **C)** `false`, `true` e `false`
* **D)** `false`, `false` e `true`
* **E)** `true`, `false` e `true`

> **Comentário Detalhado:**
>
> - **I. `5 == "5"`:** Retorna `true` porque o operador de igualdade abstrata (`==`) realiza coerção de tipos (*type coercion*), convertendo a string `"5"` para o número `5`.
> - **II. `5 === "5"`:** Retorna `false` porque o operador de igualdade estrita (`===`) verifica tipo e valor sem coerção (`number !== string`).
> - **III. `null === undefined`:** Retorna `false` porque são tipos primitivos distintos (`Null` vs `Undefined`). Nota: sob igualdade abstrata (`null == undefined`), o retorno seria `true`.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 3.3 Promises e a Sintaxe async / await",
        "question_text": """### Questão 09
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
Em relação ao tratamento de operações assíncronas em JavaScript e Node.js utilizando *Promises* e a sintaxe `async/await`, assinale a afirmativa correta:

* **A)** Uma função declarada com o modificador `async` sempre retorna implicitamente uma *Promise*, que resolve com o valor retornado pela função.
* **B)** A palavra-chave `await` pode ser utilizada no corpo de qualquer função tradicional síncrona sem necessidade de declaração assíncrona.
* **C)** Uma *Promise* rejeitada só pode ser tratada por meio de blocos de repetição `while(true)`.
* **D)** O método `Promise.all()` aguarda a resolução de todas as promises do array, mesmo se uma delas for rejeitada imediatamente.
* **E)** A execução de `await` bloqueia a thread principal do sistema operacional, impedindo a CPU de executar qualquer outro processo.

> **Comentário Detalhado:**
>
> - **A) Correta.** Toda função `async` empacota seu retorno automaticamente em uma `Promise.resolve(valor)`. Caso a função lance um erro, ela retorna uma `Promise.reject(erro)`.
> - **B) Incorreta.** O operador `await` só pode ser usado dentro de funções declaradas como `async` (ou em módulos ES em nível superior - *top-level await*).
> - **C) Incorreta.** Promises rejeitadas são tratadas com `.catch()` ou blocos `try/catch` ao redor de `await`.
> - **D) Incorreta.** `Promise.all()` adota comportamento *fail-fast*: se qualquer promise falhar, ele rejeita imediatamente.
> - **E) Incorreta.** `await` suspende apenas a execução da função assíncrona corrente sem bloquear a thread do Event Loop do Node.js (*non-blocking*).
>
> **Gabarito: A**"""
    },
    {
        "target_sec": "### 4.2 Estruturas de Dados Nativas: Listas, Tuplas, Dicionários e Conjuntos",
        "question_text": """### Questão 10
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
Na linguagem Python 3, duas das estruturas de dados sequenciais mais empregadas são as Listas (`list`) e as Tuplas (`tuple`). A diferença fundamental entre essas duas estruturas reside no fato de que:

* **A)** As listas são imutáveis e delimitadas por parênteses `()`, enquanto as tuplas são mutáveis e delimitadas por colchetes `[]`.
* **B)** As listas são mutáveis (podem ter elementos adicionados, alterados ou removidos após a criação), enquanto as tuplas são estritamente imutáveis.
* **C)** As tuplas aceitam apenas dados numéricos inteiros, enquanto as listas aceitam apenas cadeias de texto (*strings*).
* **D)** As listas não admitem elementos duplicados, enquanto as tuplas permitem duplicações infinitas.
* **E)** As tuplas são armazenadas em disco rígido, enquanto as listas residem na memória cache do processador.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** A relação de delimitadores e mutabilidade está invertida.
> - **B) Correta.** Listas (`[1, 2, 3]`) são coleções mutáveis; Tuplas (`(1, 2, 3)`) são imutáveis após a instanciação (o que confere segurança, performance e permite que tuplas de elementos imutáveis sejam usadas como chaves em dicionários).
> - **C) Incorreta.** Ambas são heterogêneas e aceitam qualquer tipo de objeto Python.
> - **D) Incorreta.** Ambas aceitam elementos duplicados.
> - **E) Incorreta.** Ambas residem na memória RAM gerenciada pelo interpretador Python.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 4.3 Fatiamento (*Slicing*), Comprehensions e Funções Geradoras (`yield`)",
        "question_text": """### Questão 11
**(FGV – TJ – Analista Judiciário / Tecnologia da Informação)**  
Considere o seguinte trecho de código em Python 3:  

```python
dados = [1, 2, 3, 4, 5, 6]
resultado = [x * 2 for x in dados if x % 2 == 0]
```

Após a execução do código acima, o valor da variável `resultado` será:

* **A)** `[2, 4, 6, 8, 10, 12]`
* **B)** `[4, 8, 12]`
* **C)** `[2, 6, 10]`
* **D)** `[1, 2, 3]`
* **E)** `[8, 12]`

> **Comentário Detalhado:**
>
> - A expressão `[x * 2 for x in dados if x % 2 == 0]` utiliza *List Comprehension*:
>   1. O filtro `if x % 2 == 0` seleciona os números pares de `dados`: $2, 4, 6$.
>   2. A expressão `x * 2` multiplica cada número selecionado por 2:
>      - $2 \\times 2 = 4$
>      - $4 \\times 2 = 8$
>      - $6 \\times 2 = 12$
>   3. A lista final resultante é `[4, 8, 12]`.
>
> **Gabarito: B**"""
    }
]

# ==========================================
# FILE 3: 03_desenvolvimento_frontend_html_css_react_typescript.md
# ==========================================
file_3 = "fontes_de_estudo/conhecimentos_especificos_b02_ti/05_desenvolvimento_de_sistemas/03_desenvolvimento_frontend_html_css_react_typescript.md"
injections_3 = [
    {
        "target_sec": "### 1.4 Mídia, Gráficos e Acessibilidade Digital (WCAG e WAI-ARIA)",
        "question_text": """### Questão 06
**(FCC – TCE – Auditor de Controle Externo / Tecnologia da Informação)**  
As diretrizes de acessibilidade para conteúdo web (WCAG 2.1) e a especificação WAI-ARIA definem normas e atributos semânticos para tornar aplicações web acessíveis a pessoas com deficiência. Em relação a essas normas, é correto afirmar:

* **A)** O atributo `alt` em elementos `<img>` deve ser sempre preenchido com textos genéricos como "imagem" ou "foto" para atender ao critério de acessibilidade.
* **B)** O atributo `aria-label` permite fornecer um rótulo textual acessível a leitores de tela para elementos interativos que não possuem texto visível na interface (como botões representados apenas por ícones).
* **C)** O atributo `aria-hidden="true"` força o elemento a ser lido prioritariamente em voz alta por leitores de tela.
* **D)** As WCAG preconizam que o contraste entre texto e fundo deve ser o menor possível para não ofuscar a visão do usuário.
* **E)** Aplicações web acessíveis são proibidas de permitir navegação por teclado, exigindo uso exclusivo de mouses de alta precisão.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** O texto alternativo `alt` deve descrever o significado ou função da imagem; textos genéricos como "imagem" prejudicam a acessibilidade. Imagens puramente decorativas devem usar `alt=""`.
> - **B) Correta.** O `aria-label` define uma cadeia de texto que rotula o elemento interativo diretamente para tecnologias assistivas (*screen readers*), suprindo a ausência de texto visual direto.
> - **C) Incorreta.** O `aria-hidden="true"` oculta o elemento e seus descendentes dos leitores de tela.
> - **D) Incorreta.** A WCAG exige taxa de contraste mínima (ex: 4.5:1 para texto normal no nível AA) para garantir legibilidade.
> - **E) Incorreta.** O acesso completo a todas as funcionalidades por meio do teclado é um dos princípios basilares de acessibilidade (Operável).
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 2.2 Modelo de Caixa (Box Model) e a Propriedade `box-sizing`",
        "question_text": """### Questão 07
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
No modelo de caixa do CSS3 (*Box Model*), a propriedade `box-sizing` altera a forma como a largura (*width*) e a altura (*height*) totais de um elemento HTML são calculadas no layout da página. Ao aplicar a regra `box-sizing: border-box;` a um elemento com `width: 300px; padding: 20px; border: 5px solid black;`, tem-se que:

* **A)** A largura total renderizada do elemento será de 350px, somando o conteúdo, os paddings e as bordas.
* **B)** A largura total renderizada do elemento permanecerá exatamente em 300px, sendo o padding e a borda absorvidos internamente no espaço total especificado.
* **C)** O navegador ignorará o padding e exibirá o conteúdo com largura de 300px e borda invisível.
* **D)** A propriedade `border-box` elimina a margem externa (*margin*) do elemento em todas as resoluções.
* **E)** O elemento será renderizado com largura infinita por colapso do modelo de renderização.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** Esse cálculo ($300 + 20 + 20 + 5 + 5 = 350\\text{px}$) ocorreria no modelo tradicional `content-box`.
> - **B) Correta.** Com `box-sizing: border-box`, a largura total do elemento na tela respeita rigorosamente o valor declarado em `width` (300px); o padding (20px de cada lado) e a borda (5px de cada lado) são deduzidos da área interna do conteúdo, que passa a ter $300 - 40 - 10 = 250\\text{px}$.
> - **C) Incorreta.** O padding e a borda são exibidos normalmente.
> - **D) Incorreta.** O `border-box` afeta conteúdo, padding e borda; as margens (*margins*) continuam externas.
> - **E) Incorreta.** Afirmação sem fundamento técnico.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 2.3 Layouts Flexíveis com Flexbox (Unidimensional)",
        "question_text": """### Questão 08
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
No módulo CSS Flexible Box Layout (*Flexbox*), para alinhar os itens filhos (*flex items*) ao longo do eixo transversal ou cruzado (*cross axis*) dentro do contêiner flexível, utiliza-se no elemento pai a propriedade:

* **A)** `justify-content`
* **B)** `align-items`
* **C)** `flex-direction`
* **D)** `flex-wrap`
* **E)** `order`

> **Comentário Detalhado:**
>
> - **A) Incorreta.** `justify-content` alinha os itens ao longo do eixo principal (*main axis*).
> - **B) Correta.** `align-items` define o alinhamento padrão dos itens ao longo do eixo transversal (*cross axis*) perpendicular ao eixo principal.
> - **C) Incorreta.** `flex-direction` define a orientação do eixo principal (`row`, `column`, etc.).
> - **D) Incorreta.** `flex-wrap` controla se os itens quebram linha ou permanecem em linha única.
> - **E) Incorreta.** `order` é aplicada nos itens filhos para reordenar a sequência de renderização.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 3.2 Sistema de Tipos: Primitivos e Tipos Especiais (`any`, `unknown`, `never`, `void`)",
        "question_text": """### Questão 09
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
Na linguagem TypeScript, os tipos especiais `any` e `unknown` fornecem suporte a valores cujos tipos não são conhecidos a priori. A diferença crucial de segurança de tipos (*type safety*) entre `any` e `unknown` consiste em:

* **A)** `any` força a checagem rigorosa de tipos pelo compilador, enquanto `unknown` desativa todas as regras de tipagem estática.
* **B)** variáveis tipadas como `unknown` não permitem a invocação direta de métodos ou acesso a propriedades sem que ocorra previamente uma verificação ou refinamento de tipo (*type narrowing*), ao passo que variáveis tipadas como `any` desabilitam completamente a checagem do compilador.
* **C)** `unknown` só pode armazenar valores booleanos primitivos, enquanto `any` aceita qualquer objeto.
* **D)** o TypeScript não aceita atribuição de novos valores a variáveis do tipo `unknown`.
* **E)** variáveis do tipo `any` são convertidas automaticamente para `never` em tempo de execução.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** É exatamente o inverso: `any` desliga a checagem do compilador.
> - **B) Correta.** `unknown` é o tipo seguro (*type-safe counterpart of any*): qualquer valor pode ser atribuído a `unknown`, mas você não pode chamar métodos nele nem passá-lo a funções tipadas sem antes estreitar o tipo (*type narrowing* via `typeof`, `instanceof` etc.). Já o `any` desabilita todas as checagens do compilador.
> - **C) Incorreta.** `unknown` aceita qualquer valor.
> - **D) Incorreta.** Reatribuição é permitida em `unknown`.
> - **E) Incorreta.** Em tempo de execução, os tipos do TypeScript são apagados (*type erasure*).
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 3.4 Interfaces vs. Type Aliases e Declaration Merging",
        "question_text": """### Questão 10
**(FGV – TJ – Analista de Sistemas / Front-end)**  
No ecossistema TypeScript, desenvolvedores podem declarar formatos estruturais utilizando `interface` ou `type` (*type alias*). Um recurso exclusivo das `interfaces` que não é suportado por `type aliases` é:

* **A)** A declaração de propriedades opcionais com `?`.
* **B)** A mesclagem automática de declarações (*declaration merging*), permitindo que múltiplas declarações de uma interface com o mesmo identificador sejam unificadas em uma única interface composta.
* **C)** A criação de uniões de tipos primitivos utilizando o operador `|`.
* **D)** A compatibilidade com tipagem estática em tempo de compilação.
* **E)** O suporte a parâmetros genéricos.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** Ambos suportam propriedades opcionais (`prop?: string`).
> - **B) Correta.** Se você declarar duas interfaces com o mesmo nome no mesmo escopo, o TypeScript mescla seus atributos (*declaration merging*). Já tentar redeclarar um `type` com o mesmo nome resulta em erro de compilação (*Duplicate identifier*).
> - **C) Incorreta.** A união de tipos com `|` é suportada nativamente por `type` (*type alias*), mas não pode ser a base de uma `interface`.
> - **D) Incorreta.** Ambos oferecem tipagem estática.
> - **E) Incorreta.** Ambos suportam *Generics*.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 4.5 Gerenciamento Global com `useContext` e Hooks de Performance (`useMemo`, `useCallback`, `useRef`)",
        "question_text": """### Questão 11
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
Na biblioteca React (versões 16.8+ baseadas em Hooks), a otimização de performance e a manipulação de instâncias mutáveis utilizam hooks especializados. A correta distinção conceitual entre `useMemo`, `useCallback` e `useRef` estabelece que:

* **A)** `useMemo` memoriza a referência de uma função, `useCallback` memoriza o valor de retorno calculado de uma função, e `useRef` força uma nova renderização imediata do componente sempre que seu atributo `.current` é modificado.
* **B)** `useMemo` armazena em cache o resultado computacional de uma função cara evitando recálculos desnecessários; `useCallback` memoriza a própria instância da definição de uma função entre renderizações; e `useRef` cria um objeto mutável persistente cuja propriedade `.current` pode ser alterada sem disparar nova renderização do componente.
* **C)** todos os três hooks são executados exclusivamente após a aplicação ser desinstalada da máquina do cliente.
* **D)** `useRef` só pode ser utilizado para conectar a aplicação ao banco de dados PostgreSQL.
* **E)** `useCallback` recalcula o valor sempre que qualquer componente irmão for renderizado no Virtual DOM.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** Houve inversão entre `useMemo` (retorna valor calculado) e `useCallback` (retorna função memorizada), e alterar `.current` de `useRef` *não* dispara re-render.
> - **B) Correta.** Síntese técnica perfeita dos três hooks de performance e estado persistente: `useMemo` memoriza valores calculados; `useCallback` memoriza referências de funções; `useRef` retém referências mutáveis a elementos do DOM ou valores sem desencadear re-renderização.
> - **C) Incorreta.** Afirmação absurda.
> - **D) Incorreta.** `useRef` opera no lado cliente do React.
> - **E) Incorreta.** `useCallback` só recria a função se as variáveis declaradas no seu array de dependências mudarem.
>
> **Gabarito: B**"""
    }
]

# ==========================================
# FILE 4: 04_apis_restful_graphql_websockets_documentacao.md
# ==========================================
file_4 = "fontes_de_estudo/conhecimentos_especificos_b02_ti/05_desenvolvimento_de_sistemas/04_apis_restful_graphql_websockets_documentacao.md"
injections_4 = [
    {
        "target_sec": "### 1.1 Princípios Arquiteturais do REST (Roy Fielding)",
        "question_text": """### Questão 06
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
O estilo arquitetural REST (*Representational State Transfer*), formulado por Roy Fielding em sua tese de doutorado (2000), baseia-se em um conjunto de restrições arquiteturais fundamentais. Dentre os princípios canônicos obrigatórios do REST, inclui-se a restrição *Stateless* (Comunicação sem Estado), a qual estabelece que:

* **A)** O cliente não precisa armazenar dados confidenciais do servidor em disco local.
* **B)** Cada requisição enviada pelo cliente ao servidor deve conter todas as informações contextuais necessárias para que o servidor possa compreendê-la e processá-la, não devendo o servidor reter sessões de estado do cliente entre requisições.
* **C)** O servidor deve registrar o histórico das telas navegadas pelo cliente na memória primária para autenticar as próximas requisições.
* **D)** O protocolo HTTP deve ser substituído permanentemente por sockets TCP com canais abertos contínuos.
* **E)** Nenhuma resposta de API pode ser armazenada em cache por intermediários ou clientes.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** A restrição *Stateless* diz respeito ao servidor não guardar o estado da sessão do cliente.
> - **B) Correta.** Na restrição *Stateless*, a requisição é autocontida (*self-contained*): autenticação, parâmetros e dados viajam em cada requisição individual, permitindo alta escalabilidade horizontal do backend sem dependência de memória de sessão compartilhada (*session affinity*).
> - **C) Incorreta.** Guardar sessão de telas na memória do servidor viola expressamente a restrição *Stateless*.
> - **D) Incorreta.** REST opera tipicamente sobre o protocolo HTTP.
> - **E) Incorreta.** *Cacheable* é outro princípio formal do REST, que incentiva o uso de cache para otimizar requisições.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 1.5 Boas Práticas no Design de URIs e Recursos RESTful",
        "question_text": """### Questão 07
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
No design de APIs RESTful orientadas a recursos e em consonância com as melhores práticas da indústria, a identificação dos endpoints de comunicação deve seguir diretrizes semânticas consistentes. A esse respeito, assinale o padrão de URI considerado correto para recuperar a lista de processos de um tribunal filtrada por ano:

* **A)** `GET /api/v1/obterTodosProcessosJudiciaisDoAno?ano=2024`
* **B)** `POST /api/v1/processos/ano/2024/buscar`
* **C)** `GET /api/v1/processos?ano=2024`
* **D)** `DELETE /api/v1/processos/buscar/2024`
* **E)** `GET /api/v1/processos/acao/listar/ano/2024`

> **Comentário Detalhado:**
>
> - **A) Incorreta.** Utilizar verbos no caminho (`/obterTodosProcessos...`) viola o princípio RESTful de utilizar substantivos para representar recursos e deixar a ação para o método HTTP (`GET`).
> - **B) Incorreta.** Utilizar `POST` para consultas simples viola a semântica HTTP de leitura e o uso de verbos no caminho (`/buscar`).
> - **C) Correta.** Padrão idiomático RESTful: recurso substantivo no plural (`/processos`), método semântico de leitura (`GET`), versionamento na URI (`/v1`) e filtros aplicados via *Query Parameters* (`?ano=2024`).
> - **D) Incorreta.** `DELETE` possui semântica de exclusão de recursos.
> - **E) Incorreta.** O uso de segmentos de caminho contendo verbos como `/acao/listar` é um anti-padrão comum que degrada o design RESTful.
>
> **Gabarito: C**"""
    },
    {
        "target_sec": "### 2.3 Operações Centrais: Queries, Mutations, Subscriptions e Resolvers",
        "question_text": """### Questão 08
**(FGV – TJ – Analista Judiciário / Tecnologia da Informação)**  
Em uma API implementada com tecnologia GraphQL, as três operações centrais previstas no esquema (*schema*) desempenham papéis estritamente definidos. A operação cujo objetivo primordial é criar, atualizar ou excluir dados no servidor, disparando efeitos colaterais de modificação de estado, é a:

* **A)** *Query*
* **B)** *Subscription*
* **C)** *Mutation*
* **D)** *Fragment*
* **E)** *Directive*

> **Comentário Detalhado:**
>
> - **A) Incorreta.** *Query* é a operação de consulta somente-leitura em GraphQL (análoga ao `GET` do REST).
> - **B) Incorreta.** *Subscription* estabelece um canal reativo (via WebSockets) para recebimento de eventos contínuos em tempo real.
> - **C) Correta.** *Mutation* é a operação formal do GraphQL utilizada para qualquer operação que modifique dados de negócio no backend (análoga aos métodos `POST`, `PUT`, `PATCH` e `DELETE` do HTTP).
> - **D) Incorreta.** *Fragment* é uma unidade reutilizável de seleção de campos na sintaxe GraphQL.
> - **E) Incorreta.** *Directive* decora campos ou operações para alterar sua execução condicionalmente (como `@include` e `@skip`).
>
> **Gabarito: C**"""
    },
    {
        "target_sec": "### 3.3 Comparativo: Polling, Long-Polling, Server-Sent Events (SSE) e WebSocket",
        "question_text": """### Questão 09
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
Na escolha de arquiteturas para transmissão de informações entre navegadores e servidores web em tempo real, os Server-Sent Events (SSE) e o protocolo WebSocket apresentam distinções técnicas marcantes. A esse respeito, é correto afirmar:

* **A)** O SSE estabelece comunicação bidirecional de baixa latência em canais binários TCP puros, enquanto o WebSocket só permite envio de mensagens do servidor para o cliente.
* **B)** O SSE é um protocolo unidirecional (do servidor para o cliente) que opera nativamente sobre conexões HTTP padrão transportando eventos formatados em `text/event-stream`, ao passo que o WebSocket estabelece uma conexão persistente e bidirecional (*full-duplex*) sobre um único socket TCP após o handshake.
* **C)** O WebSocket exige a reabertura completa de uma nova conexão TCP a cada mensagem transmitida na rede.
* **D)** O SSE é incompatível com navegadores modernos e requer a instalação de plugins legados no sistema operacional.
* **E)** O protocolo WebSocket só suporta a transmissão de dados no formato de imagens Bitmap.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** O SSE é unidirecional (servidor $\\rightarrow$ cliente); quem é bidirecional *full-duplex* é o WebSocket.
> - **B) Correta.** SSE opera sobre HTTP regular com *MIME type* `text/event-stream` enviando dados unidirecionalmente para o cliente, com reconexão automática nativa. O WebSocket provê comunicação bidirecional simétrica *full-duplex* com cabeçalhos mínimos após o handshake inicial.
> - **C) Incorreta.** O WebSocket mantém uma conexão TCP contínua e aberta; não abre conexões adicionais a cada mensagem.
> - **D) Incorreta.** O SSE é suportado nativamente pelos principais navegadores modernos por meio da API `EventSource`.
> - **E) Incorreta.** O WebSocket trafega tanto texto estruturado (UTF-8) quanto dados binários (*ArrayBuffer*, *Blob*).
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 4.1 JSON: Tipagem, Sintaxe Estrita e Validação com JSON Schema",
        "question_text": """### Questão 10
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
O formato JSON (*JavaScript Object Notation*, padronizado pela RFC 8259) é amplamente utilizado como formato padrão para troca de mensagens estruturadas na web. Quanto às regras estritas de sintaxe do JSON, é correto afirmar:

* **A)** Os nomes das chaves (propriedades) podem ser declarados sem aspas ou utilizando aspas simples (`'chave'`).
* **B)** O padrão JSON aceita nativamente a inclusão de comentários de código no formato `//` e `/* */`.
* **C)** Os nomes das chaves devem ser delimitados obrigatoriamente por aspas duplas (`"chave"`), e o formato suporta os tipos de dados básicos: string, número, booleano, nulo (`null`), objeto e array.
* **D)** O formato JSON permite serializar funções executáveis e métodos de classes sem conversão adicional.
* **E)** Vírgulas adicionais após o último elemento de um objeto ou array (*trailing commas*) são obrigatórias na especificação JSON.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** A especificação RFC 8259 exige que todas as chaves de objetos sejam obrigatoriamente delimitadas por aspas duplas (`"chave"`).
> - **B) Incorreta.** JSON padrão não suporta comentários de qualquer natureza.
> - **C) Correta.** No JSON padrão: chaves exigem aspas duplas; tipos primitivos aceitos são apenas texto entre aspas duplas, números (inteiros e decimais), `true`, `false`, `null`, além de estruturas compostas `{}` (objetos) e `[]` (arrays).
> - **D) Incorreta.** Funções executáveis não são dados suportados pelo formato JSON.
> - **E) Incorreta.** *Trailing commas* são estritamente proibidas no formato JSON canônico (geram erro de sintaxe de parsing).
>
> **Gabarito: C**"""
    },
    {
        "target_sec": "### 5.1 A Especificação OpenAPI (OAS 3.0 / 3.1)",
        "question_text": """### Questão 11
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
A especificação OpenAPI (OpenAPI Specification - OAS, originária do ecossistema Swagger) fornece uma descrição padronizada, agnóstica de linguagem de programação, para APIs RESTful. No documento de especificação OpenAPI formatado em YAML ou JSON, a seção de nível superior responsável por descrever os caminhos dos endpoints disponíveis e suas respectivas operações HTTP suportadas é:

* **A)** `servers`
* **B)** `info`
* **C)** `paths`
* **D)** `components`
* **E)** `security`

> **Comentário Detalhado:**
>
> - **A) Incorreta.** `servers` define a lista de URLs base de conexão dos ambientes da API (ex: `https://api.tce.go.gov.br/v1`).
> - **B) Incorreta.** `info` contém metadados gerais da API, como título, versão (`version: 1.0.0`) e descrição textual.
> - **C) Correta.** O nó `paths` é o coração do documento OpenAPI: mapeia as rotas/endpoints disponíveis (ex: `/processos`) e os métodos HTTP associados (`get`, `post`, `delete`) com seus parâmetros, corpos de requisição e respostas.
> - **D) Incorreta.** `components` armazena esquemas reutilizáveis (*schemas* de dados, respostas, parâmetros e esquemas de segurança) referenciados por `$ref`.
> - **E) Incorreta.** `security` declara os requisitos globais de autenticação aplicáveis aos endpoints.
>
> **Gabarito: C**"""
    }
]

# ==========================================
# FILE 5: 05_autenticacao_identidade_oauth2_oidc_jwt.md
# ==========================================
file_5 = "fontes_de_estudo/conhecimentos_especificos_b02_ti/05_desenvolvimento_de_sistemas/05_autenticacao_identidade_oauth2_oidc_jwt.md"
injections_5 = [
    {
        "target_sec": "### 1.1 Autenticação (AuthN) vs. Autorização (AuthZ)",
        "question_text": """### Questão 06
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
Na gestão de segurança de aplicações corporativas, a distinção conceitual entre Autenticação (*Authentication* - AuthN) e Autorização (*Authorization* - AuthZ) estabelece que:

* **A)** Autenticação verifica a identidade declarada por um usuário ou sistema ("quem é você?"), ao passo que Autorização determina as permissões de acesso e ações que o usuário autenticado pode executar ("o que você pode fazer?").
* **B)** Autenticação concede privilégios administrativos no banco de dados, enquanto Autorização verifica a assinatura digital do certificado TLS.
* **C)** Autenticação e Autorização são termos estritamente sinônimos na norma ISO/IEC 27001, podendo ser implementados indiferentemente pela mesma rotina de hash SHA-256.
* **D)** A autorização deve ser realizada necessariamente antes da autenticação em qualquer sistema computacional.
* **E)** A autenticação define o teto salarial de um servidor público no portal da transparência.

> **Comentário Detalhado:**
>
> - **A) Correta.** A **Autenticação (AuthN)** responde à pergunta *"Quem é você?"*, validando as credenciais (senhas, biometria, tokens). A **Autorização (AuthZ)** responde à pergunta *"O que você tem permissão para fazer?"*, aplicando políticas de controle de acesso (RBAC, ABAC) sobre os recursos solicitados.
> - **B) Incorreta.** Concessão de privilégios é tarefa de autorização.
> - **C) Incorreta.** São conceitos distintos da segurança da informação.
> - **D) Incorreta.** A autenticação precede cronologicamente a autorização; você só pode autorizar quem você primeiro identificou/autenticou.
> - **E) Incorreta.** Afirmação sem relação com arquitetura de segurança.
>
> **Gabarito: A**"""
    },
    {
        "target_sec": "### 1.2 Fatores de Autenticação e MFA",
        "question_text": """### Questão 07
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
A Autenticação Multifator (*Multi-Factor Authentication* - MFA) eleva substancialmente o nível de segurança do acesso ao exigir a combinação de múltiplos elementos probatórios pertencentes a categorias independentes. Os três fatores de autenticação clássicos são categorizados como:

* **A)** Senha alfanumérica, senha numérica e senha biométrica.
* **B)** Algo que você sabe (conhecimento), algo que você tem (posse) e algo que você é (biometria/inerência).
* **C)** Endereço de IP de rede, máscara de sub-rede e porta lógica TCP.
* **D)** Certificado público, certificado privado e autoridade certificadora intermediária.
* **E)** Teclado mecânico, monitor de alta definição e leitor óptico.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** Duas senhas distintas pertencem à mesma categoria ("algo que você sabe"), configurando autenticação de fator único repetido, e não MFA genuíno.
> - **B) Correta.** A taxonomia padrão da segurança estabelece a tríade de fatores: **Conhecimento** (algo que você sabe: senhas, PINs), **Posse** (algo que você tem: token físico, aplicativo autenticador TOTP, cartão inteligente) e **Inerência** (algo que você é: impressão digital, reconhecimento facial, íris).
> - **C) Incorreta.** Parâmetros de rede não configuram fatores humanos de autenticação de usuários.
> - **D) Incorreta.** Componentes de infraestrutura de chaves públicas (PKI).
> - **E) Incorreta.** Periféricos de hardware.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 2.1 Os Quatro Papéis Fundamentais",
        "question_text": """### Questão 08
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
O framework de autorização OAuth 2.0 (RFC 6749) define quatro papéis (*roles*) operacionais no ecossistema de delegação de acesso seguro. A entidade capaz de conceder acesso a um recurso protegido (tipicamente o próprio usuário final proprietário dos dados) é denominada:

* **A)** *Resource Server* (Servidor de Recursos).
* **B)** *Authorization Server* (Servidor de Autorização).
* **C)** *Resource Owner* (Proprietário do Recurso).
* **D)** *Client* (Cliente).
* **E)** *Token Broker*.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** O *Resource Server* hospeda as APIs e recursos protegidos, aceitando e validando tokens de acesso.
> - **B) Incorreta.** O *Authorization Server* autentica o Resource Owner e emite tokens de acesso após consentimento.
> - **C) Correta.** O **Resource Owner** (Proprietário do Recurso) é a entidade que possui a custódia dos dados e o poder de autorizar o acesso a eles (usualmente o usuário final).
> - **D) Incorreta.** O *Client* é a aplicação (web, mobile, backend) que requisita acesso aos recursos em nome do Resource Owner.
> - **E) Incorreta.** Não é um dos quatro papéis oficiais da RFC 6749.
>
> **Gabarito: C**"""
    },
    {
        "target_sec": "### 2.3 A Extensão PKCE (RFC 7636) para Clientes Públicos",
        "question_text": """### Questão 09
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
Para proteger aplicações clientes públicas (como SPAs executando em navegadores e aplicativos móveis nativos) contra o ataque de interceptação do código de autorização, a especificação OAuth 2.0 define a extensão PKCE (*Proof Key for Code Exchange*, RFC 7636). O funcionamento do fluxo PKCE baseia-se na geração de:

* **A)** Uma senha mestra criptografada com algoritmo DES de 56 bits armazenada no código-fonte do cliente.
* **B)** Um segredo criptográfico temporário denominado *code_verifier*, cuja versão transformada em hash SHA-256 (*code_challenge*) é enviada na requisição inicial de autorização, sendo o *code_verifier* original revelado apenas no momento da troca do código pelo token de acesso.
* **C)** Um token estático com validade indeterminada de 10 anos.
* **D)** Um certificado SSL autoassinado instalado na pasta raiz do aparelho celular do usuário.
* **E)** Uma chave privada RSA de 4096 bits embutida nos cookies do navegador.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** Clientes públicos não podem reter segredos estáticos com segurança (*client_secret* nunca deve ser embutido em SPA/App).
> - **B) Correta.** No PKCE: o cliente cria dinamicamente um segredo de alta entropia (*code_verifier*) e gera seu hash (*code_challenge = BASE64URL(SHA256(code_verifier))*). Ele envia o *code_challenge* na requisição de autorização; ao receber o código e solicitar o token ao *Authorization Server*, envia o *code_verifier* original em texto claro sobre TLS. O servidor calcula o hash e valida a autenticidade, prevenindo ataques de injeção de código.
> - **C) Incorreta.** Viola as boas práticas de segurança de curta duração.
> - **D) Incorreta.** Mecanismo desprovido de relação com o protocolo PKCE.
> - **E) Incorreta.** PKCE não exige emissão de certificados RSA complexos no cliente.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 3.1 Distinção Essencial: OAuth 2.0 vs. OpenID Connect",
        "question_text": """### Questão 10
**(FGV – TJ – Analista Judiciário / Tecnologia da Informação)**  
Na arquitetura de segurança moderna para sistemas distribuídos e Single Sign-On (SSO), o protocolo OpenID Connect (OIDC 1.0) estende as capacidades do framework OAuth 2.0. A principal diferença de propósito entre o OAuth 2.0 e o OpenID Connect reside no fato de que:

* **A)** O OAuth 2.0 foi projetado originalmente como um framework de **Autorização** (delegação de acesso a recursos por meio de Access Tokens), enquanto o OpenID Connect adiciona uma camada padronizada de **Autenticação e Identidade** sobre o OAuth 2.0, introduzindo o *ID Token* (formatado em JWT) para transmitir informações do usuário autenticado.
* **B)** O OAuth 2.0 não permite a transmissão de dados pela Internet sem cabos de fibra óptica dedicados.
* **C)** O OpenID Connect substitui todos os bancos de dados por arquivos de texto simples não criptografados.
* **D)** O OAuth 2.0 serve exclusivamente para autenticação facial, ao passo que o OIDC gerencia exclusivamente senhas biométricas digitais.
* **E)** O OIDC proíbe a utilização de tokens no padrão JSON Web Token (JWT).

> **Comentário Detalhado:**
>
> - **A) Correta.** É a célebre máxima da segurança moderna: **OAuth 2.0 é sobre Autorização** (dá à aplicação uma "chave de hotel" / *Access Token* com escopos específicos); **OpenID Connect é sobre Autenticação** (fornece uma "carteira de identidade" / *ID Token* padronizado em formato JWT contendo *claims* do perfil do usuário).
> - **B) Incorreta.** Ambos operam sobre protocolos web padrão (HTTP/TLS).
> - **C) Incorreta.** Totalmente descabida.
> - **D) Incorreta.** Afirmação absurda.
> - **E) Incorreta.** O OIDC define obrigatoriamente o *ID Token* na estrutura formal do padrão JWT.
>
> **Gabarito: A**"""
    }
]

# ==========================================
# FILE 6: 06_git_gerenciamento_de_dependencias_e_empacotamento.md
# ==========================================
file_6 = "fontes_de_estudo/conhecimentos_especificos_b02_ti/05_desenvolvimento_de_sistemas/06_git_gerenciamento_de_dependencias_e_empacotamento.md"
injections_6 = [
    {
        "target_sec": "### 1.2 O Modelo de Objetos do Git: Blobs, Trees, Commits e Tags",
        "question_text": """### Questão 06
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
Internamente, o Git armazena todo o histórico e a árvore de arquivos de um projeto em um repositório orientado a objetos (*Content-Addressable Storage*) dentro da pasta `.git/objects`. Os objetos fundamentais desse modelo estruturam-se em:

* **A)** Arquivos `.doc`, planilhas `.xls` e executáveis `.exe`.
* **B)** *Blobs* (que armazenam o conteúdo dos arquivos), *Trees* (que representam diretórios e mapeiam nomes de arquivos e permissões para blobs ou outras trees) e *Commits* (que apontam para uma tree raiz e armazenam autor, data, mensagem e ponteiros para os commits pais).
* **C)** Registros relacionais indexados por chaves primárias do tipo auto-incremento.
* **D)** Tabelas de partição de sistema de arquivos NTFS.
* **E)** Sockets de rede virtuais com endereçamento IPv6.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** O Git opera sobre abstrações internas de objetos universais agnósticos ao tipo de arquivo.
> - **B) Correta.** O modelo canônico de objetos do Git fundamenta-se em:
>   - **Blob:** guarda os bytes brutos do conteúdo do arquivo (sem o nome ou permissão);
>   - **Tree:** atua como diretório, associando permissões, nomes de arquivos e hashes de blobs ou sub-trees;
>   - **Commit:** captura o snapshot da tree raiz, registrando autor, committer, timestamp, mensagem e hash do(s) commit(s) pai(s);
>   - **Tag anotada:** objeto de referência imutável apontando para um commit específico.
> - **C) Incorreta.** O Git não usa banco relacional nem chaves de auto-incremento; indexa tudo por hashes criptográficos SHA-1 / SHA-256.
> - **D) Incorreta.** O modelo do Git opera em nível de aplicação multiplataforma.
> - **E) Incorreta.** Sem relação com a estrutura interna do Git.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 1.3 As Três Áreas Locais e o Ciclo de Vida dos Arquivos",
        "question_text": """### Questão 07
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
Um repositório Git local organiza o ciclo de vida dos arquivos em três áreas conceituais fundamentais: a Área de Trabalho (*Working Directory*), a Área de Preparação (*Staging Area* ou *Index*) e o Repositório Local (*Commit History* / `.git`). O comando utilizado para mover arquivos modificados do *Working Directory* para a *Staging Area*, preparando-os para o próximo commit, é:

* **A)** `git push`
* **B)** `git commit`
* **C)** `git add`
* **D)** `git fetch`
* **E)** `git checkout`

> **Comentário Detalhado:**
>
> - **A) Incorreta.** `git push` envia commits locais para um repositório remoto.
> - **B) Incorreta.** `git commit` grava as alterações presentes na Staging Area no histórico do repositório local.
> - **C) Correta.** O comando `git add <arquivo>` adiciona o conteúdo modificado do diretório de trabalho à *Staging Area* (*Index*), registrando o novo blob na base de objetos.
> - **D) Incorreta.** `git fetch` baixa metadados e objetos de branches remotas sem mesclá-los ao diretório de trabalho.
> - **E) Incorreta.** `git checkout` alterna entre branches ou restaura arquivos no diretório de trabalho.
>
> **Gabarito: C**"""
    },
    {
        "target_sec": "### 1.5 Ramificação e Integração: `git merge` vs. `git rebase`",
        "question_text": """### Questão 08
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
Ao integrar o código de uma branch de desenvolvimento (*feature branch*) à branch principal (*main*), o desenvolvedor pode optar pelo comando `git merge` ou pelo comando `git rebase`. A respeito das consequências dessas duas abordagens no histórico do projeto, é correto afirmar:

* **A)** O `git merge` lineariza o histórico reescrevendo os hashes de todos os commits anteriores, eliminando bifurcações.
* **B)** O `git merge` (sem fast-forward) preserva o histórico original intacto e cria um novo commit de junção (*merge commit*) com dois pais, ao passo que o `git rebase` reaplica os commits da feature branch um a um no topo da branch de destino, reescrevendo o histórico de commits de forma linear.
* **C)** O `git rebase` é uma operação estritamente recomendada para branches públicas compartilhadas por múltiplos desenvolvedores remotos.
* **D)** Ambos os comandos executam exatamente a mesma rotina física sem alterar qualquer ponteiro de commit.
* **E)** O `git merge` só pode ser executado se o computador estiver conectado à Internet.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** Quem lineariza e reescreve commits é o `rebase`, não o `merge`.
> - **B) Correta.** O `git merge` cria um nó de convergência (*merge commit*) com múltiplos pais, preservando o contexto temporal e a topologia real. O `git rebase` retira os commits da branch local e os reproduz sobre a ponta da branch base, criando novos hashes SHA e gerando um histórico estritamente linear (sem commits de mescla).
> - **C) Incorreta.** A "Regra de Ouro do Rebase" estabelece que nunca se deve fazer rebase em branches públicas compartilhadas, sob pena de gerar divergência nos históricos de outros desenvolvedores.
> - **D) Incorreta.** Possuem efeitos topológicos e conceituais completamente distintos.
> - **E) Incorreta.** Ambas são operações locais do Git.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 2.1 Grafos de Dependência, Dependências Transitivas e Conflitos",
        "question_text": """### Questão 09
**(FCC – TCE – Auditor de Controle Externo / Tecnologia da Informação)**  
No gerenciamento de dependências de software moderno (como Maven, npm ou Poetry), quando um projeto declara explicitamente a biblioteca A, e esta, por sua vez, requer internamente a biblioteca B para funcionar, a biblioteca B é caracterizada na arquitetura do projeto como uma:

* **A)** Dependência circular primária.
* **B)** Dependência estática de hardware.
* **C)** Dependência transitiva.
* **D)** Dependência depreciada (*deprecated*).
* **E)** Dependência exclusiva de compilação C++.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** Dependência circular ocorre quando A depende de B e B depende de A.
> - **B) Incorreta.** Trata-se de dependência de software de terceiros.
> - **C) Correta.** **Dependências transitivas** são bibliotecas das quais as suas dependências diretas dependem para operar. O gerenciador de pacotes constrói um Grafo Acíclico Dirigido (DAG) para resolver e baixar automaticamente todas as dependências transitivas.
> - **D) Incorreta.** Dependência transitiva é um conceito arquitetural de grafo, independente de estar ou não obsoleta.
> - **E) Incorreta.** Aplica-se a qualquer ecossistema de dependências de alto nível.
>
> **Gabarito: C**"""
    },
    {
        "target_sec": "### 2.3 Manifestos vs. Arquivos de Trava (Lockfiles) e o Comando `npm ci`",
        "question_text": """### Questão 10
**(FCC – TRT – Analista Judiciário / Tecnologia da Informação)**  
Em ambientes de Integração Contínua (CI/CD) com Node.js, recomenda-se a utilização do comando `npm ci` em substituição ao clássico `npm install`. Essa recomendação fundamenta-se no fato de que o `npm ci`:

* **A)** Atualiza automaticamente todas as bibliotecas para a última versão disponível no repositório público do npm.
* **B)** Requer a presença obrigatória do arquivo de trava `package-lock.json` e instala rigorosamente as versões exatas de dependências especificadas no lockfile, deletando previamente a pasta `node_modules` e garantindo builds estritamente reprodutíveis e determinísticos.
* **C)** Ignora completamente o arquivo `package-lock.json` e compila apenas o código C++.
* **D)** Permite a instalação de pacotes sem acesso à rede local ou remota, criando o código das bibliotecas via inteligência artificial.
* **E)** Funciona exclusivamente se o servidor de CI estiver executando sobre o sistema operacional Windows 98.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** Atualizar pacotes automaticamente em pipeline quebra o determinismo do build.
> - **B) Correta.** O comando `npm ci` (*Clean Install*) é otimizado para pipelines de automação: ele valida se `package.json` e `package-lock.json` estão sincronizados, remove a pasta `node_modules` existente e instala estritamente as versões travadas no lockfile com máxima velocidade e integridade.
> - **C) Incorreta.** O `npm ci` baseia-se primordialmente no `package-lock.json`.
> - **D) Incorreta.** `npm ci` baixa os artefatos do registro configurado caso não estejam em cache.
> - **E) Incorreta.** Multiplataforma.
>
> **Gabarito: B**"""
    },
    {
        "target_sec": "### 3.1 Empacotadores Web Modernos (Webpack, Vite, Rollup e esbuild)",
        "question_text": """### Questão 11
**(FGV – TJ – Analista Judiciário / Tecnologia da Informação)**  
As ferramentas de empacotamento web (*bundlers*) evoluíram significativamente com o surgimento do Vite. A principal inovação arquitetural que confere ao Vite velocidade de inicialização do servidor de desenvolvimento ordens de grandeza superior à do Webpack tradicional reside no fato de que o Vite:

* **A)** Não permite o uso de arquivos TypeScript ou JavaScript moderno.
* **B)** Aproveita a disponibilidade nativa de módulos JavaScript (*Native ES Modules* - ESM) nos navegadores modernos e delega o pré-empacotamento de dependências pesadas a ferramentas escritas em Go de alta performance (*esbuild*), empacotando sob demanda apenas o módulo requisitado pelo navegador.
* **C)** Exige que todo o código seja convertido em imagens vetoriais SVG antes da visualização na tela.
* **D)** Elimina a necessidade do navegador web, executando todo o front-end diretamente no prompt de comando do terminal.
* **E)** Compila todos os arquivos CSS para código binário em linguagem Assembly.

> **Comentário Detalhado:**
>
> - **A) Incorreta.** O Vite oferece suporte nativo e instantâneo a TypeScript, JSX, TSX e Vue/Svelte.
> - **B) Correta.** O Vite revolucionou o desenvolvimento web ao dispensar o empacotamento integral (*bundle*) de todo o código da aplicação antes de subir o servidor: ele serve o código-fonte via ESM nativo do browser (Hot Module Replacement instantâneo) e usa o *esbuild* (escrito em Go, dezenas de vezes mais veloz que transpiladores JS tradicionais) para pré-empacotar dependências.
> - **C) Incorreta.** Afirmação sem nexo.
> - **D) Incorreta.** O front-end continua sendo executado no navegador.
> - **E) Incorreta.** Descrição fantasiosa.
>
> **Gabarito: B**"""
    }
]

print("Injecting into Module 05...")
inject_questions_into_file(file_1, injections_1)
inject_questions_into_file(file_2, injections_2)
inject_questions_into_file(file_3, injections_3)
inject_questions_into_file(file_4, injections_4)
inject_questions_into_file(file_5, injections_5)
inject_questions_into_file(file_6, injections_6)
print("\nModule 05 completed successfully!")
