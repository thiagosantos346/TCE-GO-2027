# 03 - Desenvolvimento Web Frontend: HTML5, CSS3, React e TypeScript

> **Matéria:** Desenvolvimento de Sistemas  
> **Cargo:** B02 – Técnico de Controle Externo – Especialidade: Tecnologia da Informação  
> **Arquivo:** `03_desenvolvimento_frontend_html_css_react_typescript.md`  



---


## 📌 Ementa / Itens do Edital
- Desenvolvimento web: HTML5, CSS3 e TypeScript
- Desenvolvimento front-end com biblioteca React

---

## 🧭 Sumário

1. [Fundamentos de HTML5 Semântico e Acessibilidade](#1-fundamentos-de-html5-semantico-e-acessibilidade)
    1. [Estrutura Básica do Documento e Metatags Essenciais](#11-estrutura-basica-do-documento-e-metatags-essenciais)
    2. [Elementos Semânticos e Seccionamento de Conteúdo](#12-elementos-semanticos-e-seccionamento-de-conteudo)
    3. [Formulários Modernos e Validação Nativa](#13-formularios-modernos-e-validacao-nativa)
    4. [Mídia, Gráficos e Acessibilidade Digital (WCAG e WAI-ARIA)](#14-midia-graficos-e-acessibilidade-digital-wcag-e-wai-aria)
    5. [Teste 076](#Teste-076)
    6. [Teste 077](#Teste-077)
2. [Estilização com CSS3](#2-estilizacao-com-css3)
    1. [Cascata, Seletores e Cálculo de Especificidade CSS](#21-cascata-seletores-e-calculo-de-especificidade-css)
    2. [Modelo de Caixa (Box Model) e a Propriedade `box-sizing`](#22-modelo-de-caixa-box-model-e-a-propriedade-box-sizing)
    3. [Layouts Flexíveis com Flexbox (Unidimensional)](#23-layouts-flexiveis-com-flexbox-unidimensional)
    4. [Grid Bidimensional (CSS Grid Layout)](#24-grid-bidimensional-css-grid-layout)
    5. [Design Responsivo, Mobile-First e Unidades de Medida](#25-design-responsivo-mobile-first-e-unidades-de-medida)
    6. [Transições, Transformações e Animações CSS](#26-transicoes-transformacoes-e-animacoes-css)
    7. [Teste 078](#Teste-078)
    8. [Teste 079](#Teste-079)
    9. [Teste 080](#Teste-080)
3. [TypeScript: Tipagem Estática no Front-end](#3-typescript-tipagem-estatica-no-front-end)
    1. [Arquitetura, Transpilação e o Arquivo `tsconfig.json`](#31-arquitetura-transpilacao-e-o-arquivo-tsconfigjson)
    2. [Sistema de Tipos: Primitivos e Tipos Especiais (`any`, `unknown`, `never`, `void`)](#32-sistema-de-tipos-primitivos-e-tipos-especiais-any-unknown-never-void)
    3. [Union, Intersection Types e Type Narrowing](#33-union-intersection-types-e-type-narrowing)
    4. [Interfaces vs. Type Aliases e Declaration Merging](#34-interfaces-vs-type-aliases-e-declaration-merging)
    5. [Generics e Utility Types Fundamentais](#35-generics-e-utility-types-fundamentais)
    6. [Teste 081](#Teste-081)
    7. [Teste 082](#Teste-082)
    8. [Teste 083](#Teste-083)
4. [Desenvolvimento Front-end com a Biblioteca React](#4-desenvolvimento-front-end-com-a-biblioteca-react)
    1. [Paradigma Declarativo, Componentização e Sintaxe JSX](#41-paradigma-declarativo-componentizacao-e-sintaxe-jsx)
    2. [Virtual DOM e o Algoritmo de Reconciliação (Fiber)](#42-virtual-dom-e-o-algoritmo-de-reconciliacao-fiber)
    3. [Propriedades (Props), Fluxo Unidirecional e Renderização de Listas com `key`](#43-propriedades-props-fluxo-unidirecional-e-renderizacao-de-listas-com-key)
    4. [Gerenciamento de Estado e Ciclo de Vida com Hooks (`useState`, `useEffect`)](#44-gerenciamento-de-estado-e-ciclo-de-vida-com-hooks-usestate-useeffect)
    5. [Gerenciamento Global com `useContext` e Hooks de Performance (`useMemo`, `useCallback`, `useRef`)](#45-gerenciamento-global-com-usecontext-e-hooks-de-performance-usememo-usecallback-useref)
    6. [Formulários: Componentes Controlados vs. Não Controlados](#46-formularios-componentes-controlados-vs-nao-controlados)
    7. [Teste 084](#Teste-084)
    8. [Teste 085](#Teste-085)
    9. [Teste 086](#Teste-086)
5. [Fontes Recomendadas na Internet](#5-fontes-recomendadas-na-internet)

---

## 1. Fundamentos de HTML5 Semântico e Acessibilidade

### 1.1 Estrutura Básica do Documento e Metatags Essenciais
O HTML5 padronizou a especificação dos documentos web com o objetivo de simplificar a sintaxe e enriquecer o vocabulário semântico. A estrutura básica canônica de qualquer documento HTML5 é composta por:

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Portal do TCE-GO</title>
</head>
<body>
  <!-- Conteúdo renderizado na tela -->
</body>
</html>
```

- **`<!DOCTYPE html>`:** Declaração de tipo de documento simplificada. Informa aos navegadores que a página deve ser interpretada no modo padrão estrito (*standards mode*), prevenindo a ativação do modo de compatibilidade retrógrada (*quirks mode*).
- **`<meta charset="UTF-8">`:** Define o conjunto de caracteres universal Unicode UTF-8, garantindo a exibição precisa de caracteres acentuados, cedilhas e símbolos especiais sem problemas de corrupção (*mojibake*).
- **`<meta name="viewport" content="width=device-width, initial-scale=1.0">`:** Diretiva obrigatória para layouts responsivos em dispositivos móveis. Instruciona o navegador do smartphone a ajustar a largura da janela de exibição (*viewport*) à largura real da tela física do dispositivo (`width=device-width`), estabelecendo a escala inicial de zoom em 100% (`initial-scale=1.0`).

### 1.2 Elementos Semânticos e Seccionamento de Conteúdo
Antes do HTML5, páginas web eram estruturadas genericamente com divisões neutras (`<div class="header">`, `<div class="footer">`), o que dificultava a indexação por motores de busca e impedia tecnologias assistivas de entender a hierarquia do conteúdo. O HTML5 introduziu tags estruturais com significado inerente:

```mermaid
flowchart TD
    subgraph Documento["Estrutura Semântica da Página"]
        H["&lt;header&gt; Cabeçalho Institucional / Logotipos"]
        N["&lt;nav&gt; Navegação Principal da Aplicação"]
        M["&lt;main&gt; Conteúdo Central Dominante (Exclusivo)"]
        subgraph Sec["Dentro de &lt;main&gt;"]
            S["&lt;section&gt; Agrupamento Temático de Conteúdo"]
            A["&lt;article&gt; Conteúdo Autônomo e Autocontido"]
        end
        AS["&lt;aside&gt; Conteúdo Tangencial / Barra Lateral"]
        F["&lt;footer&gt; Rodapé Institucional / Metadados"]
    end
    H --> N
    N --> M
    M --> AS
    AS --> F
```

1. **`<header>`:** Representa um contêiner para conteúdo introdutório ou conjunto de links de navegação. Pode existir no topo da página ou no início de um `<article>` ou `<section>`.
2. **`<nav>`:** Destinado exclusivamente a blocos contendo os links principais de navegação do site ou da aplicação. Não deve ser usado para qualquer agrupamento de links soltos no rodapé.
3. **`<main>`:** Encapsula o conteúdo central, específico e exclusivo do documento `<body>`. **Regra da W3C:** Deve existir **apenas um único elemento `<main>` visível por página**. Conteúdos que se repetem de forma idêntica em múltiplas páginas do sistema (barras de navegação globais, logos de topo, termos de uso no rodapé) **não podem** ser inseridos dentro do `<main>`.
4. **`<article>`:** Representa uma composição autônoma, completa e autocontida que faça sentido pleno mesmo se for extraída do site e distribuída em outro veículo (ex.: um acórdão judicial, uma notícia, uma publicação de blog, um comentário individual).
5. **`<section>`:** Agrupamento temático genérico de conteúdo conexo, tipicamente introduzido por um título de cabeçalho (`<h2>` a `<h6>`). Se o conteúdo não possui relação temática própria e serve apenas para estilização visual, deve-se usar uma tag neutra `<div>`.
6. **`<aside>`:** Representa uma seção cujo conteúdo é tangencial ou secundário em relação ao conteúdo em torno dele (barras laterais, citações em destaque, caixas de glossário, publicidade).
7. **`<footer>`:** Rodapé de uma seção ou do documento inteiro. Costuma conter informações sobre o autor, termos de uso, licenças e links institucionais.
8. **`<figure>` e `<figcaption>`:** Encapsulam conteúdos ilustrativos (gráficos, fotos, listagens de código) acompanhados de uma legenda textual associada (`<figcaption>`).

### 1.3 Formulários Modernos e Validação Nativa
O HTML5 modernizou a coleta de dados com novos tipos semânticos de `<input>` e atributos de validação integrados no próprio navegador, dispensando scripts JavaScript complexos para validações básicas:

- **Novos Tipos de Input:**
    - `type="email"`: Valida o formato sintático de endereço de correio eletrônico (`usuario@dominio.com`).
    - `type="number"`: Força entrada numérica, permitindo definir limites com `min="1"`, `max="100"` e granularidade com `step="1"`.
    - `type="date"`, `time`, `datetime-local`: Renderiza seletores nativos de calendário e horário adaptados ao sistema operacional.
    - `type="url"`: Valida URLs absolutas com protocolo (`https://..`).
    - `type="tel"`: Otimizado para teclado numérico de discagem em celulares.
- **Atributos de Validação:**
    - `required`: Torna o preenchimento do campo estritamente obrigatório para submissão do formulário.
    - `pattern="[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}"`: Valida o campo contra uma expressão regular (Regex) em tempo de cliente (ex.: máscara de CPF).
    - `placeholder`: Fornece uma dica curta do formato esperado (não substitui o elemento `<label>`).
    - `disabled` vs. `readonly`: Um campo `disabled` é desativado visualmente e **não é enviado** na submissão do formulário (`POST/GET`). Já um campo `readonly` impede a edição pelo usuário, mas **é devidamente transmitido** na submissão.

### 1.4 Mídia, Gráficos e Acessibilidade Digital (WCAG e WAI-ARIA)

#### Áudio, Vídeo e Gráficos
- **`<audio>` e `<video>`:** Execução nativa de mídia sem dependência de plugins externos:

```html
<video controls width="600" poster="capa.jpg">
  <source src="sessao_plenaria.mp4" type="video/mp4">
  <source src="sessao_plenaria.webm" type="video/webm">
  Seu navegador não suporta a reprodução de vídeo.
</video>
```

- **`<canvas>`:** Fornece uma área de bitmap desenhável via código procedural JavaScript (ideal para gráficos estatísticos rápidos ou jogos).
- **SVG (Scalable Vector Graphics):** Gráficos vetoriais baseados em XML integrados no DOM, permitindo estilização direta com CSS, escalabilidade infinita sem perda de resolução e excelente suporte para acessibilidade.

#### Diretrizes WCAG e Atributos WAI-ARIA
As diretrizes WCAG (*Web Content Accessibility Guidelines*) da W3C são organizadas em torno dos 4 princípios fundamentais (**POUR**):

1. **Perceptível (*Perceivable*):** Informações e componentes visuais devem ser apresentados de modo que todos os usuários possam percebê-los (ex.: fornecer textos alternativos `alt` em imagens e legendas em vídeos).
2. **Operável (*Operable*):** Todos os componentes da interface devem poder ser operados via teclado, sem armadilhas de foco (*keyboard traps*).
3. **Compreensível (*Understandable*):** A operação e a leitura devem ser previsíveis e sem jargões confusos.
4. **Robusto (*Robust*):** O código deve ser interoperável com uma ampla variedade de navegadores e tecnologias assistivas.

**Atributos WAI-ARIA (*Accessible Rich Internet Applications*):**

- `role`: Define o papel semântico do elemento caso não haja tag HTML5 equivalente (ex.: `role="alert"`, `role="dialog"`, `role="status"`).
- `aria-label`: Fornece um rótulo textual audível para elementos visuais que não possuem texto visível (ex.: `<button aria-label="Fechar janela">X</button>`).
- `aria-labelledby` e `aria-describedby`: Apontam para IDs de elementos existentes que dão título ou descrição adicional ao componente.
- `aria-live`: Define regiões de atualização dinâmica assíncrona para que leitores de tela avisem imediatamente o usuário:
    - `aria-live="polite"`: O leitor de tela aguarda o usuário terminar sua ação atual antes de ler o aviso.
    - `aria-live="assertive"`: Interrompe a fala do leitor de tela imediatamente para alertar sobre erros críticos.
- `aria-hidden="true"`: **Oculta o elemento de leitores de tela**, mantendo-o visível visualmente (útil para ícones puramente decorativos).
- **Atributo `tabindex`:**
    - `tabindex="0"`: Insere o elemento na sequência natural de tabulação do teclado.
    - `tabindex="-1"`: Remove o elemento da ordem do teclado, permitindo foco programático via JavaScript (`elemento.focus()`).
    - `tabindex="1+"` (positivo): **Antipadrão severo**. Quebra a ordem de leitura do documento e confunde usuários dependentes de navegação por teclado.

---

### Teste 076
**(FCC – TRT-1 – Analista Judiciario Tecnologia da Informacao – 2014)**
O trecho de programa a seguir foi elaborado na linguagem HTML com JavaScript e será aberto por um navegador que as suporte. `<html>` `<body>` `<h1>`Página Principal`</h1>` `<form>` comando y `</form>` `</body>` `</html>` Após a sua execução, é exibido pelo navegador: O comando que deve ser colocado no lugar do comando y, de modo que, ao se pressionar o botão Nova Página, seja aberta a página P1.html, é

* **A)** <input type="button" text="Nova Página" click="window.location='P1.html'">
* **B)** <input type="button" text="Nova Página" onclick="window.location='P1.html'">
* **C)** <input type="onbutton" text="Nova Página" onclick="window.location='P1.html'">
* **D)** <input type="button" value="Nova Página" onclick="window.location='P1.html'">
* **E)** <input type="onbutton" value="Nova Página" click="window.location='P1.html'">

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "<input type="button" text="Nova Página" click="window.location='P1.html'">". De acordo com a teoria estudada em *1.2 Elementos Semânticos e Seccionamento de Conteúdo*, `<main>`: Encapsula o conteúdo central, específico e exclusivo do documento `<body>`. Regra da W3C: Deve existir apenas um único elemento `<main>` visível por página.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "<input type="button" text="Nova Página" onclick="window.location='P1.html'">". De acordo com a teoria estudada em *1. Hook `useState`*, chamar a função atualizadora do estado agenda uma nova execução (re-renderização) do componente pelo React.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "<input type="onbutton" text="Nova Página" onclick="window.location='P1.html'">". De acordo com a teoria estudada em *1.3 Formulários Modernos e Validação Nativa*, o HTML5 modernizou a coleta de dados com novos tipos semânticos de `<input>` e atributos de validação integrados no próprio navegador, dispensando scripts JavaScript complexos para validações básicas.
> - **D)** **Correta.** Conforme fundamentado na seção *1.1 Estrutura Básica do Documento e Metatags Essenciais* deste guia, `<!DOCTYPE html>`: Declaração de tipo de documento simplificada. Informa aos navegadores que a página deve ser interpretada no modo padrão estrito (*standards mode*), prevenindo a ativação do modo de compatibilidade retrógrada (*quirks mode*). Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT-1/2014) ao estabelecer que "<input type="button" value="Nova Página" onclick="window.location='P1.html'">".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "<input type="onbutton" value="Nova Página" click="window.location='P1.html'">". De acordo com a teoria estudada em *1.2 Elementos Semânticos e Seccionamento de Conteúdo*, `<header>`: Representa um contêiner para conteúdo introdutório ou conjunto de links de navegação. Pode existir no topo da página ou no início de um `<article>` ou `<section>`.
>
> **Gabarito: D**

---

### Teste 077
**(FGV – TRT-24 – Analista Judiciario Area Apoio Especializado Tecnologia da Informacao – 2025)**
HTML5 introduziu uma série de novos recursos, elementos e atributos que ajudam os desenvolvedores na construção de sites mais modernos. Considerando essa nova versão da linguagem HTML, analise as afirmativas a seguir sobre os recursos que ela introduziu. I. ServerSockets – trata-se de uma tecnologia de comunicação bidirecional de última geração para o estabelecimento de conexões seguras entre os aplicativos web e o servidor. II. Eventos enviados pelo servidor – permite que servidores enviem dados para páginas da web mediante o protocolo HTTP, em que apenas os eventos críticos fluem do servidor web para os navegadores. III. Microdados − possibilita que os desenvolvedores criem seus próprios vocabulários além do HTML5 e estendam as páginas da web com semântica personalizada. IV. Geolocalização – viabiliza que visitantes possam optar por compartilhar sua localização física mediante seus aplicativos web. Está correto o que se afirma em

* **A)** I e II, apenas.
* **B)** II e III, apenas.
* **C)** III e IV, apenas.
* **D)** I, II e IV, apenas.
* **E)** I, II e III, apenas.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I e II, apenas". De acordo com a teoria estudada em *1.2 Elementos Semânticos e Seccionamento de Conteúdo*, antes do HTML5, páginas web eram estruturadas genericamente com divisões neutras (`<div class="header">`, `<div class="footer">`), o que dificultava a indexação por motores de busca e impedia tecnologias assistivas de entender a hierarquia do conteúdo.
> - **B)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "II e III, apenas". De acordo com a teoria estudada em *5. Fontes Recomendadas na Internet*, mDN Web Docs - HTML Semântico e Estruturação Web - Elementos estruturais e semântica de marcação moderna.
> - **C)** **Correta.** Conforme fundamentado na seção *1.3 Formulários Modernos e Validação Nativa* deste guia, o HTML5 modernizou a coleta de dados com novos tipos semânticos de `<input>` e atributos de validação integrados no próprio navegador, dispensando scripts JavaScript complexos para validações básicas. Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT-24/2025) ao estabelecer que "III e IV, apenas".
> - **D)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I, II e IV, apenas". De acordo com a teoria estudada em *1.2 Elementos Semânticos e Seccionamento de Conteúdo*, o HTML5 introduziu tags estruturais com significado inerente.
> - **E)** **Incorreta.** A opção incorre em restrição indevida ao limitar o escopo conceitual ao afirmar que "I, II e III, apenas". De acordo com a teoria estudada em *5. Fontes Recomendadas na Internet*, kEITH, Jeremy; ANDREW, Rachel. HTML5 para Designers Web. São Paulo: Bookman, 2011. (Cap. 3 - Marcação Semântica Estruturada).
>
> **Gabarito: C**

---

## 2. Estilização com CSS3

### 2.1 Cascata, Seletores e Cálculo de Especificidade CSS
O CSS (*Cascading Style Sheets*) baseia-se no princípio da **Cascata** para resolver conflitos entre múltiplas declarações de estilo apontando para o mesmo elemento HTML. A resolução segue a hierarquia:

1. **Importância:** Regras marcadas com `!important` sobrepõem qualquer regra ordinária.
2. **Especificidade:** Se não houver `!important`, vence a regra que tiver a pontuação de especificidade mais alta.
3. **Ordem de Aparição no Código:** Se houver empate exato de especificidade, vence a última regra declarada no arquivo CSS.

```mermaid
flowchart LR
    subgraph Cascata["Ordem de Prioridade na Cascata CSS"]
        Imp["!important (Prioridade Máxima)"]
        Inline["Estilo Inline: style='..' (Peso: 1,0,0,0)"]
        IDs["Seletores de ID: #menu (Peso: 0,1,0,0)"]
        Classes["Classes, Atributos e Pseudo-classes: .card, [type='text'], :hover (Peso: 0,0,1,0)"]
        Tags["Tags e Pseudo-elementos: div, h1, ::before (Peso: 0,0,0,1)"]
    end
    Imp --> Inline --> IDs --> Classes --> Tags
```

#### A Pontuação Quádrupla da W3C `(a, b, c, d)`
- **$a$ (Inline):** Estilos aplicados diretamente no atributo `style=""` da tag HTML ($1, 0, 0, 0$).
- **$b$ (IDs):** Número de seletores de identificador (`#meu-id`) na regra ($0, 1, 0, 0$).
- **$c$ (Classes, Atributos e Pseudo-classes):** Número de seletores de classe (`.minha-classe`), seletores de atributos (`[type="text"]`) e pseudo-classes (`:hover`, `:first-child`, `:nth-child(n)`) ($0, 0, 1, 0$).
- **$d$ (Tags e Pseudo-elementos):** Número de tags de elementos (`div`, `p`, `span`) e pseudo-elementos (`::before`, `::after`) ($0, 0, 0, 1$).
- **Seletor Universal (`*`) e Combinadores (`>`, `+`, `~`):** Possuem peso nulo $(0, 0, 0, 0)$.

> 🚨 **ALERTA DE PROVA / FCC:**  
> A comparação de especificidade é posicional da esquerda para a direita, **nunca somatória linear simples**:
>
> - Uma regra com 1 único ID `(0, 1, 0, 0)` tem maior prioridade que uma regra contendo 15 classes combinadas `(0, 0, 15, 0)`.
> - A declaração `!important` não acrescenta "pontos" à tupla; ela altera a fase da cascata. Havendo duas declarações com `!important`, o desempate volta a ser feito pela pontuação normal de especificidade entre elas.

### 2.2 Modelo de Caixa (Box Model) e a Propriedade `box-sizing`
No CSS, todo elemento renderizado é estruturado visualmente como uma caixa composta por 4 áreas concêntricas:

```mermaid
flowchart TD
    subgraph BoxModel["Box Model do CSS"]
        M["Margin (Espaçamento Externo - Transparente)"]
        B["Border (Borda Visível ou Oculta)"]
        P["Padding (Espaçamento Interno entre Conteúdo e Borda)"]
        C["Content (Área do Conteúdo Real: Texto, Imagem)"]
    end
    M --> B --> P --> C
```

- **`box-sizing: content-box` (Padrão nativo do navegador):**
    - A largura definida na propriedade `width` é aplicada **estritamente à área de conteúdo (*Content*)**.
    - O `padding` e a `border` são adicionados **por fora** dessa largura.
    - Se definirmos `width: 300px; padding: 20px; border: 5px solid black;`, a largura total ocupada na tela pelo elemento será:
    $$\text{Largura Total} = 300 + (20 \times 2) + (5 \times 2) = 350\text{ px}$$
- **`box-sizing: border-box` (Padrão moderno da indústria de software):**
    - A propriedade `width` define a **largura total da caixa visível**, incluindo a borda e o padding.
    - A área útil de conteúdo encolhe automaticamente para acomodar o espaçamento interno.
    - No mesmo exemplo (`width: 300px; padding: 20px; border: 5px solid black;`), a largura final na tela será **exatamente $300\text{ px}$**.

### 2.3 Layouts Flexíveis com Flexbox (Unidimensional)
O Flexbox (`display: flex`) é um modelo de layout voltado para a distribuição de espaço e alinhamento de itens ao longo de um **único eixo por vez** (linha ou coluna).

- **Eixo Principal (*Main Axis*) vs. Eixo Transversal (*Cross Axis*):**
    - `flex-direction: row` (padrão): O eixo principal é horizontal (esquerda para a direita); o eixo transversal é vertical.
    - `flex-direction: column`: O eixo principal é vertical; o transversal torna-se horizontal.
- **Propriedades do Contêiner Flex (*Flex Container*):**
    - `justify-content`: Alinha os itens ao longo do **eixo principal** (`flex-start`, `flex-end`, `center`, `space-between`, `space-around`, `space-evenly`).
    - `align-items`: Alinha os itens ao longo do **eixo transversal** (`stretch`, `flex-start`, `flex-end`, `center`, `baseline`).
    - `flex-wrap`: Define se os itens que ultrapassam a largura do contêiner devem quebrar para a próxima linha (`nowrap` ou `wrap`).
    - `gap`: Define o espaçamento entre os itens filhos sem recorrer a margens manuais.
- **Propriedades dos Filhos (*Flex Items*):**
    - `flex-grow`: Fator de crescimento relativo do item para preencher o espaço restante disponível.
    - `flex-shrink`: Fator de encolhimento relativo quando o espaço total for insuficiente.
    - `flex-basis`: Tamanho inicial padrão do item antes da distribuição de sobras.

### 2.4 Grid Bidimensional (CSS Grid Layout)
Diferentemente do Flexbox, o CSS Grid (`display: grid`) é um sistema **bidimensional nativo**, permitindo controlar simultaneamente linhas (*rows*) e colunas (*columns*).

- **Criação de Trilhas e Unidade Fracional (`fr`):**
    - `grid-template-columns: 200px 1fr 2fr`: Define três colunas: a primeira fixa com 200px, e o restante dividido em 3 partes fracionais (1 parte para a segunda coluna e 2 partes para a terceira).
    - `repeat(3, 1fr)`: Cria 3 colunas de larguras rigorosamente iguais.
- **Responsividade Automática sem Media Queries:**
    - `grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));`: Os cards se ajustam dinamicamente na tela; se houver menos espaço que 250px, quebram sozinhos para a próxima linha.
- **Áreas Nomeadas (`grid-template-areas`):**

```css
.container {
  display: grid;
  grid-template-areas:
    "cabecalho cabecalho"
    "lateral principal"
    "rodape rodape";
}
```

### 2.5 Design Responsivo, Mobile-First e Unidades de Medida
- **Abordagem Mobile-First:** Metodologia onde a folha de estilos base é desenvolvida primeiramente para telas pequenas (smartphones). As adaptações para telas maiores são adicionadas incrementalmente através de **Media Queries com `min-width`**:

```css
/* Estilo padrão: Mobile */
.grid-noticias { display: flex; flex-direction: column; }

/* Telas a partir de tablets */
@media (min-width: 768px) {
  .grid-noticias { display: grid; grid-template-columns: repeat(2, 1fr); }
}
```

- **Unidades de Medida Relativas:**
    - `rem` (*Root EM*): Relativa ao tamanho da fonte do elemento raiz (`<html>`), tipicamente `1rem = 16px`. Garante acessibilidade quando o usuário altera o tamanho padrão de fonte no navegador.
    - `em`: Relativa ao tamanho da fonte do próprio elemento pai imediato.
    - `%`: Relativa à dimensão do elemento contêiner pai direto.
    - `vw` e `vh`: Porcentagens relativas à largura (*viewport width*) e altura (*viewport height*) da janela de visualização do navegador ($100\text{vw} = 100\%$ da tela).

### 2.6 Transições, Transformações e Animações CSS
- **Transições (`transition`):** Permite suavizar a mudança de propriedades CSS ao longo do tempo (ex.: `:hover` alterando cores ou opacidade). Sintaxe: `transition: property duration timing-function delay;`.
- **Transformações 2D/3D (`transform`):** Modifica a geometria visual do elemento sem disparar recálculo de fluxo de página (*reflow*). Funções comuns: `translate(x, y)`, `scale(1.1)`, `rotate(45deg)`.
- **Animações Complexas (`@keyframes`):** Permitem criar sequências visuais com múltiplos pontos intermediários (*keyframes* de 0% a 100%):

```css
@keyframes pulsar {
  0% { transform: scale(1); }
  50% { transform: scale(1.05); }
  100% { transform: scale(1); }
}
.alerta { animation: pulsar 2s infinite ease-in-out; }
```

---

### Teste 078
**(FCC – TRT-23 – Analista Judiciario Apoio Especializado Tecnologia da Informacao – 2016)**
Considere uma página HTML5 que possui um elemento `<div class="texto">` contendo em seu interior um texto grande, de, aproximadamente, uma página. Para colocar este texto em 3 colunas nos navegadores Chrome, Safari e Opera, utilizando CSS3, deve-se inserir, no bloco CSS incorporado, a instrução

* **A)** .texto{-webkit-column-count:3}
* **B)** .texto{-moz-column-count:3}
* **C)** #texto{column-count:3}
* **D)** .texto{column-width:3}
* **E)** .texto{-column-count-width:3}

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *Diretrizes WCAG e Atributos WAI-ARIA* deste guia, `aria-label`: Fornece um rótulo textual audível para elementos visuais que não possuem texto visível (ex.: `<button aria-label="Fechar janela">X</button>`). Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT-23/2016) ao estabelecer que ".texto{-webkit-column-count:3}".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que ".texto{-moz-column-count:3}". De acordo com a teoria estudada em *2.3 Layouts Flexíveis com Flexbox (Unidimensional)*, `flex-direction: column`: O eixo principal é vertical; o transversal torna-se horizontal.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "#texto{column-count:3}". De acordo com a teoria estudada em *1.2 Elementos Semânticos e Seccionamento de Conteúdo*, `<section>`: Agrupamento temático genérico de conteúdo conexo, tipicamente introduzido por um título de cabeçalho (`<h2>` a `<h6>`). Se o conteúdo não possui relação temática própria e serve apenas para estilização visual, deve-se usar uma tag neutra `<div>`.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que ".texto{column-width:3}". De acordo com a teoria estudada em *2.2 Modelo de Caixa (Box Model) e a Propriedade `box-sizing`*, se definirmos `width: 300px; padding: 20px; border: 5px solid black;`, a largura total ocupada na tela pelo elemento será.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que ".texto{-column-count-width:3}". De acordo com a teoria estudada em *1.2 Elementos Semânticos e Seccionamento de Conteúdo*, antes do HTML5, páginas web eram estruturadas genericamente com divisões neutras (`<div class="header">`, `<div class="footer">`), o que dificultava a indexação por motores de busca e impedia tecnologias assistivas de entender a hierarquia do conteúdo.
>
> **Gabarito: A**

---

### Teste 079
**(FUMARC – TRT-3 – Analista Judiciario Apoio Especializado Tecnologia da Informacao – 2022)**
Considere a página HTML renderizada por um navegador web e o código fonte HTML5/CSS3 a seguir: CÓDIGO FONTE PÁGINA HTML RENDERIZADA <!DOCTYPE html>`<html>` <................> `<body>``<table>` `<tr>``<th>`Nome`</th>``<th>`Idade`</th>``</tr>` `<tr>``<td>`Ze`</td>``<td>`23`</td>``</tr>` `<tr>``<td>`Maria`</td>``<td>`26`</td>``</tr>` `</table>``</body>``</html>` 25 Assinale a alternativa CORRETA com o código HTML5/CSS3 que irá substituir o trecho “<................>” do código fonte para gerar a página HTML renderizada:

* **A)** `<head>``<style>` table, th, td { border: 1px solid black; border-radius: 10px; width: 200px; } `</style>``</head>`
* **B)** `<head>``<style>` table, th, td { border: 1px solid black; border-radius: 10px; } `</style>``</head>`
* **C)** `<head>``<style>` table, th, td { border: 1px solid black; border-radius: 10px; width: 200%; } `</style>``</head>`
* **D)** `<head>``<style>` table, th, td { border: 1px solid black; width: 200%; } `</style>``</head>`
* **E)** `<head>``<style>` table, th, td { border: 1px solid black; border-radius: rounded; } `</style>``</head>`

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *2.2 Modelo de Caixa (Box Model) e a Propriedade `box-sizing`* deste guia, se definirmos `width: 300px; padding: 20px; border: 5px solid black;`, a largura total ocupada na tela pelo elemento será. Dessa forma, está plenamente correta a assertiva da banca (FUMARC – TRT-3/2022) ao estabelecer que "`<head>``<style>` table, th, td { border: 1px solid black; border-radius: 10px; width: 200px; } `</style>``</head>`".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "`<head>``<style>` table, th, td { border: 1px solid black; border-radius: 10px; } `</style>``</head>`". De acordo com a teoria estudada em *2.2 Modelo de Caixa (Box Model) e a Propriedade `box-sizing`*, no mesmo exemplo (`width: 300px; padding: 20px; border: 5px solid black;`), a largura final na tela será exatamente \$300\text{ px}\$.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "`<head>``<style>` table, th, td { border: 1px solid black; border-radius: 10px; width: 200%; } `</style>``</head>`". De acordo com a teoria estudada em *2.1 Cascata, Seletores e Cálculo de Especificidade CSS*, o CSS (*Cascading Style Sheets*) baseia-se no princípio da Cascata para resolver conflitos entre múltiplas declarações de estilo apontando para o mesmo elemento HTML. A resolução segue a hierarquia.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "`<head>``<style>` table, th, td { border: 1px solid black; width: 200%; } `</style>``</head>`". De acordo com a teoria estudada em *A Pontuação Quádrupla da W3C `(a, b, c, d)`*, \$a\$ (Inline): Estilos aplicados diretamente no atributo `style=""` da tag HTML (\$1, 0, 0, 0\$).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "`<head>``<style>` table, th, td { border: 1px solid black; border-radius: rounded; } `</style>``</head>`". De acordo com a teoria estudada em *2.4 Grid Bidimensional (CSS Grid Layout)*, `grid-template-columns: 200px 1fr 2fr`: Define três colunas: a primeira fixa com 200px, e o restante dividido em 3 partes fracionais (1 parte para a segunda coluna e 2 partes para a terceira).
>
> **Gabarito: A**

---

### Teste 080
**(FCC – TRT-15 – Analista Judiciario Tecnologia da Informacao – 2015)**
A propriedade position da CSS3 especifica o tipo do método de posicionamento usado para um determinado elemento HTML. Esta propriedade permite os valores

* **A)** static, relative, absolute ou fixed.
* **B)** public, private, default ou static.
* **C)** top, bottom, left, right ou center.
* **D)** default, relative, absolute ou variable.
* **E)** bottom, left, right, wrap ou center.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *2.1 Cascata, Seletores e Cálculo de Especificidade CSS* deste guia, o CSS (*Cascading Style Sheets*) baseia-se no princípio da Cascata para resolver conflitos entre múltiplas declarações de estilo apontando para o mesmo elemento HTML. A resolução segue a hierarquia. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT-15/2015) ao estabelecer que "static, relative, absolute ou fixed".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "public, private, default ou static". De acordo com a teoria estudada em *2.5 Design Responsivo, Mobile-First e Unidades de Medida*, `rem` (*Root EM*): Relativa ao tamanho da fonte do elemento raiz (`<html>`), tipicamente `1rem = 16px`. Garante acessibilidade quando o usuário altera o tamanho padrão de fonte no navegador.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "top, bottom, left, right ou center". De acordo com a teoria estudada em *2.3 Layouts Flexíveis com Flexbox (Unidimensional)*, `justify-content`: Alinha os itens ao longo do eixo principal (`flex-start`, `flex-end`, `center`, `space-between`, `space-around`, `space-evenly`).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "default, relative, absolute ou variable". De acordo com a teoria estudada em *4.1 Paradigma Declarativo, Componentização e Sintaxe JSX*, sintaxe JSX (JavaScript XML): Extensão sintática que permite escrever marcação semelhante a HTML diretamente dentro do código JavaScript. O JSX é transpilado para chamadas de função `React.createElement()` ou para o transformador moderno `_jsx()`.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "bottom, left, right, wrap ou center". De acordo com a teoria estudada em *2.3 Layouts Flexíveis com Flexbox (Unidimensional)*, `flex-wrap`: Define se os itens que ultrapassam a largura do contêiner devem quebrar para a próxima linha (`nowrap` ou `wrap`).
>
> **Gabarito: A**

---

## 3. TypeScript: Tipagem Estática no Front-end

### 3.1 Arquitetura, Transpilação e o Arquivo `tsconfig.json`
O TypeScript é um **superconjunto tipado de JavaScript** (*typed superset*) desenvolvido pela Microsoft. Navegadores não executam TypeScript diretamente; os arquivos `.ts` ou `.tsx` devem ser compilados/transpilados para JavaScript puro (`.js`) por meio do compilador oficial `tsc` ou ferramentas de empacotamento modernas (Vite, esbuild, Babel).

- **Verificação em Tempo de Compilação:** O TypeScript detecta erros de tipagem, acessos a propriedades nulas e incompatibilidades antes da execução. Em tempo de execução, todos os tipos são eliminados (*Type Erasure*).
- **`tsconfig.json`:** Arquivo de configuração raiz do projeto TypeScript. Opções cruciais:
    - `"target"`: Versão do ECMAScript de destino para a qual o código será transpilado (ex.: `"ES2022"`).
    - `"module"`: Sistema de módulos de saída (ex.: `"CommonJS"` ou `"ESNext"`).
    - `"strict": true`: Habilita todas as checagens rígidas de tipo (incluindo `strictNullChecks` e `noImplicitAny`).
    - `"jsx"`: Modo de transpilação do JSX no React (ex.: `"react-jsx"`).

### 3.2 Sistema de Tipos: Primitivos e Tipos Especiais (`any`, `unknown`, `never`, `void`)
Além dos tipos primitivos comuns (`string`, `number`, `boolean`, `null`, `undefined`, `symbol`), o TypeScript introduz tipos especiais cruciais para provas:

| Tipo | Descrição | Segurança de Tipo (*Type-Safe*) | Permitido Acessar Membros? |
|---|---|:---:|:---:|
| **`any`** | Desativa completamente o sistema de tipos estático do compilador. | **Nenhuma** | Sim, sem qualquer validação |
| **`unknown`** | Representa um tipo desconhecido em tempo de compilação. | **Total** | **Não**, sem afunilamento prévio (*narrowing*) |
| **`void`** | Indica que uma função não retorna nenhum valor utilizável. | Sim | Não |
| **`never`** | Representa valores que **nunca podem existir ou ocorrer**. | Sim | Não |

- **`never` em detalhe:** É o tipo retornado por funções que sempre lançam exceção (`throw new Error()`) ou entram em loops sem fim (`while(true)`). Também é empregado para assegurar checagens exaustivas (*exhaustive checks*) em cláusulas `switch/case`.

### 3.3 Union, Intersection Types e Type Narrowing
- **Union Types (`|`):** Uma variável pode assumir um entre múltiplos tipos permitidos:

```typescript
type Identificador = string | number;
```

- **Intersection Types (`&`):** Combina múltiplos tipos em um único tipo que satisfaz todas as restrições simultaneamente:

```typescript
type Pessoa = { nome: string };
type Funcionario = Pessoa & { matricula: number };
```

- **Type Narrowing (Afunilamento de Tipo):** O TypeScript refina dinamicamente o tipo de uma variável dentro de blocos condicionais utilizando guardas de tipo (*type guards*):
    - `typeof x === "string"`
    - `x instanceof Date`
    - `"propriedade" in objeto`
    - Funções de predicado de tipo customizadas (`pet is Cachorro`).

### 3.4 Interfaces vs. Type Aliases e Declaration Merging
Tanto `interface` quanto `type` podem ser usados para modelar a forma de objetos, mas possuem diferenças estruturais:

```typescript
// Interface: Suporta extensão (extends) e junção de declarações (Declaration Merging)
interface Auditor {
  nome: string;
}
interface Auditor {
  registroOAB?: string; // Mesclado automaticamente à interface Auditor original!
}

// Type Alias: Suporta primitivos, uniões literais e tuplas, mas NÃO permite declaração duplicada
type NivelAcesso = "ADMIN" | "CONSULTOR" | "OPERADOR";
type Ponto2D = [number, number];
```

> 🚨 **ALERTA DE PROVA / FCC:**  
> Duas interfaces com o mesmo nome no mesmo escopo realizam **Declaration Merging** (fusão de declarações), somando seus membros em uma única interface conjunta. Já dois `type` com o mesmo nome geram imediatamente um erro de compilação de identificador duplicado (`Duplicate identifier`).

### 3.5 Generics e Utility Types Fundamentais

#### Generics (`<T>`)
Permitem que funções, interfaces e classes operem com diferentes tipos preservando a segurança estática:

```typescript
function obterPrimeiroElemento<T>(lista: T[]): T | undefined {
  return lista[0];
}
```

#### Utility Types Nativos
O TypeScript inclui um conjunto poderoso de utilitários de transformação de tipos:

| Utility Type | Transformação Efetuada | Exemplo Prático |
|---|---|---|
| **`Partial<T>`** | Torna **todas as propriedades de `T` opcionais** (`?`). | `Partial<Processo>` (usado em requisições PATCH) |
| **`Required<T>`** | Torna **todas as propriedades de `T` estritamente obrigatórias**. | `Required<Processo>` (remove todas as interrogações `?`) |
| **`Readonly<T>`** | Torna **todas as propriedades de `T` imutáveis** (somente leitura). | Impede reatribuição: `p.status = "NOVO"` dá erro de compilação |
| **`Pick<T, K>`** | Constrói um tipo contendo apenas o **subconjunto `K` de propriedades** de `T`. | `Pick<Processo, "id" \| "numero">` |
| **`Omit<T, K>`** | Constrói um tipo contendo todas as propriedades de `T` **exceto `K`**. | `Omit<Usuario, "senhaHash">` |
| **`Record<K, T>`** | Constrói um tipo de objeto mapeando chaves do tipo `K` para valores `T`. | `Record<string, Auditor>` (dicionários chave-valor) |
| **`Exclude<T, U>`** | Exclui de uma união `T` todos os tipos que são atribuíveis a `U`. | `Exclude<"a" \| "b" \| "c", "a">` $\rightarrow$ `"b" \| "c"` |

---

### Teste 081
**(FCC – TRT-9 – Analista Judiciario Apoio Especializado Tecnologia da Informacao – 2015)**
Um Analista da área de TI deseja incluir uma formatação CSS diretamente na tag `<h:inputText/>` de uma página construída com JSF e também definir um nome de classe de CSS para a tag. O Analista deverá utilizar, para isso, as propriedades

* **A)** id e class.
* **B)** cssStyle e className.
* **C)** style e styleClass.
* **D)** styleType e insertClass.
* **E)** cssFormat e rendererClass.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "id e class". De acordo com a teoria estudada em *2.1 Cascata, Seletores e Cálculo de Especificidade CSS*, o CSS (*Cascading Style Sheets*) baseia-se no princípio da Cascata para resolver conflitos entre múltiplas declarações de estilo apontando para o mesmo elemento HTML. A resolução segue a hierarquia.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "cssStyle e className". De acordo com a teoria estudada em *4.1 Paradigma Declarativo, Componentização e Sintaxe JSX*, `class` torna-se `className` (pois `class` é palavra reservada em JS).
> - **C)** **Correta.** Conforme fundamentado na seção *A Pontuação Quádrupla da W3C `(a, b, c, d)`* deste guia, \$a\$ (Inline): Estilos aplicados diretamente no atributo `style=""` da tag HTML (\$1, 0, 0, 0\$). Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT-9/2015) ao estabelecer que "style e styleClass".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "styleType e insertClass". De acordo com a teoria estudada em *2.6 Transições, Transformações e Animações CSS*, transformações 2D/3D (`transform`): Modifica a geometria visual do elemento sem disparar recálculo de fluxo de página (*reflow*). Funções comuns: `translate(x, y)`, `scale(1.1)`, `rotate(45deg)`.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "cssFormat e rendererClass". De acordo com a teoria estudada em *3.4 Interfaces vs. Type Aliases e Declaration Merging*, duas interfaces com o mesmo nome no mesmo escopo realizam Declaration Merging (fusão de declarações), somando seus membros em uma única interface conjunta.
>
> **Gabarito: C**

---

### Teste 082
**(FCC – TRT-11 – Analista Judiciario Tecnologia da Informacao – 2017)**
Considere o documento XML abaixo e as regras definidas na Document Type Definition – DTD. <?xml version="1.0" encoding="UTF-8"?> <!DOCTYPE Processos [ <!ELEMENT Processos (Processo+)> <!ELEMENT Processo (NumeroSequencial, DigitoVerificador, AnoAjuizamento?, OrgaoJudiciario, Tribunal, Vara)> <!ELEMENT NumeroSequencial (#PCDATA)> <!ELEMENT DigitoVerificador (#PCDATA)> <!ELEMENT AnoAjuizamento (#PCDATA)> <!ELEMENT OrgaoJudiciario (#PCDATA)> <!ELEMENT Tribunal (#PCDATA)> <!ELEMENT Vara (#PCDATA)> ]> `<Processos>` `<Processo>` `<NumeroSequencial>`0012300`</NumeroSequencial>` `<DigitoVerificador>`04`</DigitoVerificador>` `<AnoAjuizamento>` 2007`</AnoAjuizamento>` `<OrgaoJudiciario>`5`</OrgaoJudiciario>` `<Tribunal>`11`</Tribunal>` `<Vara>`0030`</Vara>` `</Processo>` `</Processos>` A DTD define que

* **A)** pode haver elementos Processo sem o elemento AnoAjuizamento em seu interior.
* **B)** os elementos no interior de um elemento Processo podem se repetir diversas vezes, se necessário.
* **C)** os elementos só podem conter valores numéricos inteiros, já que são do tipo #PCDATA.
* **D)** um elemento Processos pode ter, no máximo, um elemento Processo em seu interior.
* **E)** todo elemento Processo deverá conter, obrigatoriamente, os elementos NumeroSequencial, DigitoVerificador, AnoAjuizamento, OrgaoJudiciario, Tribunal e Vara.

---

> **Comentário Detalhado:**
>
> - **A)** **Correta.** Conforme fundamentado na seção *1.2 Elementos Semânticos e Seccionamento de Conteúdo* deste guia, `<header>`: Representa um contêiner para conteúdo introdutório ou conjunto de links de navegação. Pode existir no topo da página ou no início de um `<article>` ou `<section>`. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT-11/2017) ao estabelecer que "pode haver elementos Processo sem o elemento AnoAjuizamento em seu interior".
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "os elementos no interior de um elemento Processo podem se repetir diversas vezes, se necessário". De acordo com a teoria estudada em *1.2 Elementos Semânticos e Seccionamento de Conteúdo*, conteúdos que se repetem de forma idêntica em múltiplas páginas do sistema (barras de navegação globais, logos de topo, termos de uso no rodapé) não podem ser inseridos dentro do `<main>`.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "os elementos só podem conter valores numéricos inteiros, já que são do tipo #PCDATA". De acordo com a teoria estudada em *Utility Types Nativos*, `Pick<T, K>`: Constrói um tipo contendo apenas o subconjunto `K` de propriedades de `T`. — `Pick<Processo, "id" \ — "numero">`.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "um elemento Processos pode ter, no máximo, um elemento Processo em seu interior". De acordo com a teoria estudada em *Utility Types Nativos*, `Partial<T>`: Torna todas as propriedades de `T` opcionais (`?`). — `Partial<Processo>` (usado em requisições PATCH).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "todo elemento Processo deverá conter, obrigatoriamente, os elementos NumeroSequencial, DigitoVerificador...". De acordo com a teoria estudada em *1.2 Elementos Semânticos e Seccionamento de Conteúdo*, `<footer>`: Rodapé de uma seção ou do documento inteiro. Costuma conter informações sobre o autor, termos de uso, licenças e links institucionais.
>
> **Gabarito: A**

---

### Teste 083
**(FGV – TJ-BA – Analista Judiciario Tecnologia da Informacao – 2015)**
Uma determinada agência reguladora disponibiliza um schema para validação de mensagens XML que estabelece, entre outras coisas, os tipos simples tais como datas, códigos de serviços, etc. Um desses tipos deve admitir apenas strings contendo de 1 a 5 caracteres, formadas pelas letras OLMVDIP. A definição correta para essa restrição de valor é:

* **A)** `<restriction base="substring">` <pattern value="OLMVDIP” size=5/> `<restriction>`
* **B)** `<restriction base="string">` <pattern value="[OLMVDIP]{1,5}"/> `<restriction>`
* **C)** `<restriction base="string">` <pattern value="[O][L][M][V][D][I][P]1,5"/> `<restriction>`
* **D)** `<restriction base="string">` `<pattern value= substring of "OLMVDIP"/>` `<restriction>`
* **E)** `<restriction base="substring">` <pattern value="OLMVDIP” 1 to 5"/> `<restriction>`

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "`<restriction base="substring">` <pattern value="OLMVDIP” size=5/> `<restriction>`". De acordo com a teoria estudada em *4.6 Formulários: Componentes Controlados vs. Não Controlados*, componentes Controlados (*Controlled Components*): O valor do campo de formulário é controlado integralmente pelo estado do React via `value` e evento `onChange`. O estado do React atua como a única fonte da verdade (*single source of truth*).
> - **B)** **Correta.** Conforme fundamentado na seção *Utility Types Nativos* deste guia, `Record<K, T>`: Constrói um tipo de objeto mapeando chaves do tipo `K` para valores `T`. — `Record<string, Auditor>` (dicionários chave-valor). Dessa forma, está plenamente correta a assertiva da banca (FGV – TJ-BA/2015) ao estabelecer que "`<restriction base="string">` <pattern value="[OLMVDIP]{1,5}"/> `<restriction>`".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "`<restriction base="string">` <pattern value="[O][L][M][V][D][I][P]1,5"/> `<restriction>`". De acordo com a teoria estudada em *1.3 Formulários Modernos e Validação Nativa*, `pattern="[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}"`: Valida o campo contra uma expressão regular (Regex) em tempo de cliente (ex.: máscara de CPF).
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "`<restriction base="string">` `<pattern value= substring of "OLMVDIP"/>` `<restriction>`". De acordo com a teoria estudada em *3.2 Sistema de Tipos: Primitivos e Tipos Especiais (`any`, `unknown`, `never`, `void`)*, além dos tipos primitivos comuns (`string`, `number`, `boolean`, `null`, `undefined`, `symbol`), o TypeScript introduz tipos especiais cruciais para provas.
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "`<restriction base="substring">` <pattern value="OLMVDIP” 1 to 5"/> `<restriction>`". De acordo com a teoria estudada em *2.5 Design Responsivo, Mobile-First e Unidades de Medida*, abordagem Mobile-First: Metodologia onde a folha de estilos base é desenvolvida primeiramente para telas pequenas (smartphones). As adaptações para telas maiores são adicionadas incrementalmente através de Media Queries com `min-width`.
>
> **Gabarito: B**

---

## 4. Desenvolvimento Front-end com a Biblioteca React

### 4.1 Paradigma Declarativo, Componentização e Sintaxe JSX
React é uma biblioteca JavaScript declarativa para a construção de interfaces de usuário, criada pela Meta (Facebook).

- **Declarativo:** O desenvolvedor descreve **como a UI deve parecer** dado um determinado estado da aplicação, e o React encarrega-se de atualizar o DOM real de forma eficiente.
- **Componentização:** A interface é decomposta em blocos independentes, isolados e reutilizáveis (hoje prioritariamente em formato de funções JavaScript puras).
- **Sintaxe JSX (JavaScript XML):** Extensão sintática que permite escrever marcação semelhante a HTML diretamente dentro do código JavaScript. O JSX é transpilado para chamadas de função `React.createElement()` ou para o transformador moderno `_jsx()`.
    - Diferenças fundamentais em relação ao HTML:
    - `class` torna-se `className` (pois `class` é palavra reservada em JS).
    - `for` em `<label>` torna-se `htmlFor`.
    - Atributos de evento utilizam convenção camelCase (`onClick`, `onChange`, `onSubmit`).
    - Todos os elementos devem ser fechados explicitamente (`<input />`, `<img />`).
    - Múltiplos elementos na raiz devem ser envelopados por um elemento pai ou por um Fragment (`<> .. </>`).

### 4.2 Virtual DOM e o Algoritmo de Reconciliação (Fiber)
Manipular o DOM real do navegador diretamente é uma operação custosa computacionalmente devido aos ciclos de *Reflow* e *Repaint*. O React resolve isso por meio do **Virtual DOM (VDOM)**:

```mermaid
flowchart TD
    subgraph Reconciliacao["Fluxo de Reconciliação no React"]
        E1["1. Alteração de Estado (setState)"] --> VDOM_Novo["2. Criação do novo Virtual DOM"]
        VDOM_Antigo["Virtual DOM Anterior"] --> Diff["3. Algoritmo de Diffing (React Fiber)"]
        VDOM_Novo --> Diff
        Diff -->|"Calcula a menor mutação necessária"| Commit["4. Commit: Atualiza apenas nós modificados no DOM Real"]
    end
```

- **Algoritmo de *Diffing* Heurístico ($\mathcal{O}(n)$):** O React compara a árvore antiga do VDOM com a nova árvore e calcula o conjunto mínimo de mutações necessárias.
    - Se dois elementos forem de tipos diferentes (ex.: `<div>` mudou para `<span>`), o React destrói a subárvore antiga por completo e monta uma nova do zero.
    - Para listas de elementos irmãos, o React utiliza a propriedade `key` para saber quais nós foram apenas movidos ou reorganizados.

### 4.3 Propriedades (Props), Fluxo Unidirecional e Renderização de Listas com `key`

#### Fluxo Unidirecional de Dados (*One-Way Data Binding*)
As propriedades (*props*) fluem exclusivamente de cima para baixo na hierarquia da árvore de componentes (do componente Pai para os componentes Filhos).

- As `props` são **estritamente imutáveis** para o componente que as recebe (tratam-se como valores somente leitura). Se o componente filho precisar alterar um valor do pai, o pai deve repassar uma função de callback via prop para que o filho a invoque.

#### Renderização de Listas e a Propriedade `key`
Ao utilizar `.map()` para transformar um array de objetos em elementos visuais, cada item retornado deve receber compulsoriamente a prop especial `key`.

> 🚨 **ALERTA DE PROVA / FCC:**  
>
> - A propriedade `key` deve ser um **identificador único, estável e previsível** (como o ID primário da entidade vindo do banco de dados).
> - **Nunca use o índice do array (`key={index}`)** para itens que possam ser reordenados, filtrados, excluídos ou adicionados no início da fila! O uso do índice faz o React reaproveitar instâncias de componentes erradas, provocando bugs visuais e perda de dados em inputs.
> - **Nunca gere chaves randômicas (`key={Math.random()}`)**, pois isso força a destruição e recriação do nó a cada frame de renderização.
> - A prop `key` é reservada para o algoritmo interno do React e **NÃO é repassada** para o componente filho (não pode ser lida via `props.key`).

### 4.4 Gerenciamento de Estado e Ciclo de Vida com Hooks (`useState`, `useEffect`)

#### 1. Hook `useState`
Permite associar estado reativo local a um componente funcional:

```jsx
const [contador, setContador] = useState(0);

// Atualização funcional (garante o valor mais recente)
setContador(anterior => anterior + 1);
```

Chamar a função atualizadora do estado agenda uma nova execução (re-renderização) do componente pelo React.

#### 2. Hook `useEffect`
Executa **efeitos colaterais** (*side effects*) no ciclo de vida do componente (como chamadas HTTP via `fetch`/`axios`, escuta de eventos do navegador ou inicialização de temporizadores).

```mermaid
flowchart TD
    subgraph Ciclo["Ciclo de Execução do useEffect"]
        Mount["Componente Montado na Tela"] --> Run["Executa Callback do Efeito"]
        Run --> Wait["Aguardando Interações"]
        Wait -->|"Mudança em valor de [dep]"| Clean1["Executa Cleanup da Rodada Anterior"]
        Clean1 --> Run
        Wait -->|"Desmontagem do Componente"| CleanFinal["Executa Cleanup Final (Retorno do Efeito)"]
    end
```

- **As Três Formas do Vetor de Dependências:**
    1. `useEffect(fn)` (sem segundo parâmetro): Executa na montagem e **após absolutamente toda e qualquer re-renderização**.
    2. `useEffect(fn, [])` (vetor vazio): Executa **apenas uma única vez**, logo após a primeira renderização do componente (equivalente ao antigo `componentDidMount`).
    3. `useEffect(fn, [id, filtro])` (com dependências): Executa na montagem e sempre que houver alteração de valor em `id` ou `filtro`.

- **Função de Limpeza (*Cleanup*):** Se o callback do `useEffect` retornar uma função (`return () => { clearInterval(id); };`), essa função será executada pelo React **antes de reexecutar o efeito na próxima renderização** e na **desmontagem final (*unmount*) do componente**, prevenindo vazamento de memória (*memory leaks*).

### 4.5 Gerenciamento Global com `useContext` e Hooks de Performance (`useMemo`, `useCallback`, `useRef`)

#### `useContext` e a Context API
Evita o problema de **Prop Drilling** (ter que repassar props manualmente por dezenas de componentes intermediários que não usam aquele dado):

```jsx
// Criação do Contexto
const TemaContext = React.createContext("light");

// Provedor
<TemaContext.Provider value="dark">
  <BarraSuperior />
</TemaContext.Provider>

// Consumo em qualquer componente descendente
function Botao() {
  const tema = useContext(TemaContext);
  return <button className={tema}>Salvar</button>;
}
```

#### Hooks de Otimização e Referências
- **`useMemo`:** Memoriza o **resultado computado** de um cálculo complexo para evitar reprocessamentos desnecessários em re-renderizações:

```jsx
const relatorioComplexo = useMemo(() => calcularEstatisticas(dados), [dados]);
```

- **`useCallback`:** Memoriza a **referência de uma função de callback** entre renderizações, evitando que componentes filhos que a recebem via props sejam re-renderizados desnecessariamente:

```jsx
const handleClick = useCallback(() => { enviarAuditoria(id); }, [id]);
```

- **`useRef`:** Cria um objeto de referência mutável `{ current: valor }` que persiste durante todo o ciclo de vida do componente:
    - Permite acesso direto ao nó do DOM real (`<input ref={inputRef} />` $\rightarrow$ `inputRef.current.focus()`).
    - Armazena valores mutáveis que, quando alterados, **não disparam re-renderização** do componente.

### 4.6 Formulários: Componentes Controlados vs. Não Controlados
- **Componentes Controlados (*Controlled Components*):** O valor do campo de formulário é controlado integralmente pelo estado do React via `value` e evento `onChange`. O estado do React atua como a única fonte da verdade (*single source of truth*).

```jsx
<input type="text" value={nome} onChange={e => setNome(e.target.value)} />
```

- **Componentes Não Controlados (*Uncontrolled Components*):** O valor do campo é gerenciado internamente pelo próprio DOM do navegador. O React recupera o valor sob demanda no momento do submit utilizando uma referência (`useRef`).

---

### Teste 084
**(FCC – TRT-11 – Analista Judiciario Tecnologia da Informacao – 2017)**
Considere o formulário HTML abaixo. `<form action="controle.php" method="post">` `<p>`Usuário: `<input type="text" name="usuario" />``</p>` `<p>`Senha: `<input type="password" name="senha" />``</p>` `<p>``<input type="submit" value="Entrar" />``</p>` `</form>` Para receber o conteúdo do campo usuário, transformando eventuais caracteres especiais do HTML na sua forma codificada para que não seja possível injetar tags HTML ou JavaScript através do campo, utiliza-se, no arquivo controle.php, a instrução

* **A)** htmlconvert(\$_REQUEST['usuario'])
* **B)** htmlnoinjection(\$_REQUEST['usuario'])
* **C)** htmlconvertentities(\$_POST['usuario'])
* **D)** htmlspecialchars(\$_POST['usuario'])
* **E)** htmlconvertchars(\$_GETPARAMETER['usuario'])

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "htmlconvert(\$_REQUEST['usuario'])". De acordo com a teoria estudada em *4.1 Paradigma Declarativo, Componentização e Sintaxe JSX*, react é uma biblioteca JavaScript declarativa para a construção de interfaces de usuário, criada pela Meta (Facebook).
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "htmlnoinjection(\$_REQUEST['usuario'])". De acordo com a teoria estudada em *2.5 Design Responsivo, Mobile-First e Unidades de Medida*, `rem` (*Root EM*): Relativa ao tamanho da fonte do elemento raiz (`<html>`), tipicamente `1rem = 16px`. Garante acessibilidade quando o usuário altera o tamanho padrão de fonte no navegador.
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "htmlconvertentities(\$_POST['usuario'])". De acordo com a teoria estudada em *1.3 Formulários Modernos e Validação Nativa*, `type="email"`: Valida o formato sintático de endereço de correio eletrônico (`usuario@dominio.com`).
> - **D)** **Correta.** Conforme fundamentado na seção *1.3 Formulários Modernos e Validação Nativa* deste guia, `disabled` vs. `readonly`: Um campo `disabled` é desativado visualmente e não é enviado na submissão do formulário (`POST/GET`). Já um campo `readonly` impede a edição pelo usuário, mas é devidamente transmitido na submissão. Dessa forma, está plenamente correta a assertiva da banca (FCC – TRT-11/2017) ao estabelecer que "htmlspecialchars(\$_POST['usuario'])".
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "htmlconvertchars(\$_GETPARAMETER['usuario'])". De acordo com a teoria estudada em *4.6 Formulários: Componentes Controlados vs. Não Controlados*, componentes Controlados (*Controlled Components*): O valor do campo de formulário é controlado integralmente pelo estado do React via `value` e evento `onChange`. O estado do React atua como a única fonte da verdade (*single source of truth*).
>
> **Gabarito: D**

---

### Teste 085
**(FGV – TCE-GO – Analista de Controle Externo Tecnologia da Informacao – 2024)**
Roberto está desenvolvendo uma aplicação web usando React, e decidiu utilizar o Bootstrap para que a aplicação seja responsiva. Analise o trecho do código a seguir como parte da aplicação: Marque a opção que aponta problemas para a implementação correta deste projeto.

* **A)** O código não necessita da importação do React pois a exportação já vai incorporar no projeto o React.
* **B)** É necessário acrescentar a importação do CSS do Bootstrap.
* **C)** O uso de classes como "container", "text-center", e "btn btnprimary" precisa ser mudado pois não funciona no React.
* **D)** O Bootstrap não pode ser utilizado em projetos React devido a incompatibilidades entre as bibliotecas.
* **E)** A tag `<div>` utilizada não é suportada pelo HTML5.

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O código não necessita da importação do React pois a exportação já vai incorporar no projeto o React". De acordo com a teoria estudada em *4.1 Paradigma Declarativo, Componentização e Sintaxe JSX*, sintaxe JSX (JavaScript XML): Extensão sintática que permite escrever marcação semelhante a HTML diretamente dentro do código JavaScript. O JSX é transpilado para chamadas de função `React.createElement()` ou para o transformador moderno `_jsx()`.
> - **B)** **Correta.** Conforme fundamentado na seção *2.4 Grid Bidimensional (CSS Grid Layout)* deste guia, `grid-template-columns: 200px 1fr 2fr`: Define três colunas: a primeira fixa com 200px, e o restante dividido em 3 partes fracionais (1 parte para a segunda coluna e 2 partes para a terceira). Dessa forma, está plenamente correta a assertiva da banca (FGV – TCE-GO/2024) ao estabelecer que "É necessário acrescentar a importação do CSS do Bootstrap".
> - **C)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O uso de classes como "container", "text-center", e "btn btnprimary" precisa ser mudado pois não funciona no React". De acordo com a teoria estudada em *Renderização de Listas e a Propriedade `key`*, nunca use o índice do array (`key={index}`) para itens que possam ser reordenados, filtrados, excluídos ou adicionados no início da fila! O uso do índice faz o React reaproveitar instâncias de componentes erradas, provocando bugs visuais e perda de dados em inputs.
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "O Bootstrap não pode ser utilizado em projetos React devido a incompatibilidades entre as bibliotecas". De acordo com a teoria estudada em *Renderização de Listas e a Propriedade `key`*, a prop `key` é reservada para o algoritmo interno do React e NÃO é repassada para o componente filho (não pode ser lida via `props.key`).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "A tag `<div>` utilizada não é suportada pelo HTML5". De acordo com a teoria estudada em *1.2 Elementos Semânticos e Seccionamento de Conteúdo*, antes do HTML5, páginas web eram estruturadas genericamente com divisões neutras (`<div class="header">`, `<div class="footer">`), o que dificultava a indexação por motores de busca e impedia tecnologias assistivas de entender a hierarquia do conteúdo.
>
> **Gabarito: B**

---

### Teste 086
**(FGV – TRT-13 – Analista Judiciario Tecnologia da Informacao – 2022)**
PrimeFaces versão 8.0 é uma biblioteca amplamente utilizada por empresas de software. O código da página web a seguir foi escrito utilizando essa biblioteca: Para especificar que o componente `<p:textEditor />` não seja exibido após a renderização da página, este componente deve ser utilizado da seguinte forma:

* **A)** `<p:textEditor disabled="true" />`
* **B)** `<p:textEditor display="none" />`
* **C)** `<p:textEditor rendered="false" />`
* **D)** `<p:textEditor show="false" />`
* **E)** `<p:textEditor visible="false" />`

---

> **Comentário Detalhado:**
>
> - **A)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "`<p:textEditor disabled="true" />`". De acordo com a teoria estudada em *1.3 Formulários Modernos e Validação Nativa*, `disabled` vs. `readonly`: Um campo `disabled` é desativado visualmente e não é enviado na submissão do formulário (`POST/GET`). Já um campo `readonly` impede a edição pelo usuário, mas é devidamente transmitido na submissão.
> - **B)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "`<p:textEditor display="none" />`". De acordo com a teoria estudada em *2.3 Layouts Flexíveis com Flexbox (Unidimensional)*, o Flexbox (`display: flex`) é um modelo de layout voltado para a distribuição de espaço e alinhamento de itens ao longo de um único eixo por vez (linha ou coluna).
> - **C)** **Correta.** Conforme fundamentado na seção *2. Hook `useEffect`* deste guia, `useEffect(fn, [])` (vetor vazio): Executa apenas uma única vez, logo após a primeira renderização do componente (equivalente ao antigo `componentDidMount`). Dessa forma, está plenamente correta a assertiva da banca (FGV – TRT-13/2022) ao estabelecer que "`<p:textEditor rendered="false" />`".
> - **D)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "`<p:textEditor show="false" />`". De acordo com a teoria estudada em *Renderização de Listas e a Propriedade `key`*, a propriedade `key` deve ser um identificador único, estável e previsível (como o ID primário da entidade vindo do banco de dados).
> - **E)** **Incorreta.** A opção apresenta proposição em desacordo com os fundamentos teóricos e técnicos do tópico ao afirmar que "`<p:textEditor visible="false" />`". De acordo com a teoria estudada em *Renderização de Listas e a Propriedade `key`*, a prop `key` é reservada para o algoritmo interno do React e NÃO é repassada para o componente filho (não pode ser lida via `props.key`).
>
> **Gabarito: C**

---

## 5. Fontes Recomendadas na Internet

* [React Official Documentation - Learn React](https://react.dev/learn) - Fundamentos de componentes declarativos, props, JSX, Virtual DOM e reconciliação.
* [React Official Documentation - Built-in React Hooks](https://react.dev/reference/react/hooks) - Especificação detalhada de useState, useEffect, useContext, useReducer, useMemo e useCallback.
* [TypeScript Official Handbook - TypeScript for JavaScript Programmers](https://www.typescriptlang.org/docs/handbook/intro.html) - Sistema de tipos estático, interfaces, type aliases, union types e type narrowing.
* [TypeScript Official Handbook - Utility Types](https://www.typescriptlang.org/docs/handbook/utility-types.html) - Catálogo de Partial, Required, Readonly, Pick, Omit e Record.
* [MDN Web Docs - HTML Semântico e Estruturação Web](https://developer.mozilla.org/pt-BR/docs/Web/HTML) - Elementos estruturais e semântica de marcação moderna.
* [MDN Web Docs - CSS Layout: Flexbox e Grid](https://developer.mozilla.org/pt-BR/docs/Learn_web_development/Core/CSS_layout) - Posicionamento bidimensional com CSS Grid e unidimensional com Flexbox.
* BANKS, Alex; PORCELLO, Eve. **React Aprenda Praticando: Construindo Aplicações Web com React e Redux**. São Paulo: Novatec, 2021. (Cap. 4 a 6 - Estado, Hooks e Renderização).
* CHERNY, Boris. **TypeScript Essencial: Acelerando o Desenvolvimento JavaScript**. São Paulo: Novatec, 2020. (Cap. 3 e 4 - Tipagem Estática e Funções).
* KEITH, Jeremy; ANDREW, Rachel. **HTML5 para Designers Web**. São Paulo: Bookman, 2011. (Cap. 3 - Marcação Semântica Estruturada).
