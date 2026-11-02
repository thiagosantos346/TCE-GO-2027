# 06 - Git, Gerenciamento de Dependências e Empacotamento

> **Matéria:** Desenvolvimento de Sistemas  
> **Cargo:** B02 – Técnico de Controle Externo – Especialidade: Tecnologia da Informação  
> **Arquivo:** `06_git_gerenciamento_de_dependencias_e_empacotamento.md`  

---

## 📌 Ementa / Itens do Edital
- Controle de versão distribuído com Git (conceitos e comandos essenciais)
- Gerenciamento de dependências
- Empacotamento de aplicações (bundlers e artefatos)
- Publicação e distribuição de aplicações

---

## 🧭 Sumário

1. [Controle de Versão Distribuído com Git](#1-controle-de-versao-distribuido-com-git)
    1. [Arquitetura Interna: Distribuído vs. Centralizado e Snapshots vs. Deltas](#11-arquitetura-interna-distribuido-vs-centralizado-e-snapshots-vs-deltas)
    2. [O Modelo de Objetos do Git: Blobs, Trees, Commits e Tags](#12-o-modelo-de-objetos-do-git-blobs-trees-commits-e-tags)
    3. [As Três Áreas Locais e o Ciclo de Vida dos Arquivos](#13-as-tres-areas-locais-e-o-ciclo-de-vida-dos-arquivos)
    4. [Comandos Fundamentais de Inspeção, Rastreamento e Histórico](#14-comandos-fundamentais-de-inspecao-rastreamento-e-historico)
    5. [Ramificação e Integração: `git merge` vs. `git rebase`](#15-ramificacao-e-integracao-git-merge-vs-git-rebase)
    6. [Operações de Recuperação e Desfazer: `reset`, `revert`, `stash` e `cherry-pick`](#16-operacoes-de-recuperacao-e-desfazer-reset-revert-stash-e-cherry-pick)
    7. [Sincronização e Fluxo Remoto: `fetch`, `pull` e `push`](#17-sincronizacao-e-fluxo-remoto-fetch-pull-e-push)
    8. [Teste 108](#Teste-108)
    9. [Teste 109](#Teste-109)
    10. [Teste 110](#Teste-110)
    11. [Teste 111](#Teste-111)
    12. [Teste 112](#Teste-112)
2. [Gerenciamento de Dependências de Software](#2-gerenciamento-de-dependencias-de-software)
    1. [Grafos de Dependência, Dependências Transitivas e Conflitos](#21-grafos-de-dependencia-dependencias-transitivas-e-conflitos)
    2. [Versionamento Semântico (SemVer 2.0.0)](#22-versionamento-semantico-semver-200)
    3. [Manifestos vs. Arquivos de Trava (Lockfiles) e o Comando `npm ci`](#23-manifestos-vs-arquivos-de-trava-lockfiles-e-o-comando-npm-ci)
    4. [Ecossistemas de Dependências: Node.js (npm), Python (pip/Poetry) e Java (Maven)](#24-ecossistemas-de-dependencias-nodejs-npm-python-pippoetry-e-java-maven)
    5. [O Ciclo de Vida Padrão do Apache Maven](#25-o-ciclo-de-vida-padrao-do-apache-maven)
    6. [Teste 113](#Teste-113)
    7. [Teste 114](#Teste-114)
    8. [Teste 115](#Teste-115)
    9. [Teste 116](#Teste-116)
3. [Empacotamento Web e Publicação de Aplicações](#3-empacotamento-web-e-publicacao-de-aplicacoes)
    1. [Empacotadores Web Modernos (Webpack, Vite, Rollup e esbuild)](#31-empacotadores-web-modernos-webpack-vite-rollup-e-esbuild)
    2. [Otimizações de Produção: Tree Shaking, Code Splitting e Minificação](#32-otimizacoes-de-producao-tree-shaking-code-splitting-e-minificacao)
    3. [Empacotamento de Backend: JAR/WAR, Wheels Python e Repositórios Corporativos](#33-empacotamento-de-backend-jarwar-wheels-python-e-repositorios-corporativos)
    4. [Teste 117](#Teste-117)
    5. [Teste 118](#Teste-118)
4. [Fontes Recomendadas na Internet](#4-fontes-recomendadas-na-internet)

---

## 1. Controle de Versão Distribuído com Git

### 1.1 Arquitetura Interna: Distribuído vs. Centralizado e Snapshots vs. Deltas
O Git, projetado originalmente por Linus Torvalds em 2005 para o desenvolvimento do kernel Linux, representa uma ruptura paradigmática em relação aos sistemas de controle de versão legados:

```mermaid
flowchart TD
    subgraph Centralizado["Modelo Centralizado Legado (SVN / CVS)"]
        SRV["Servidor Central (Único detentor do histórico)"]
        DEV1["Dev 1 (Apenas arquivos de trabalho)"]
        DEV2["Dev 2 (Apenas arquivos de trabalho)"]
        DEV1 <-->|"Conexão de rede obrigatória para commit"| SRV
        DEV2 <-->|"Ponto único de falha"| SRV
    end
    subgraph Distribuido["Modelo Distribuído Moderno (Git)"]
        REM["Repositório Remoto (GitHub / GitLab)"]
        R1["Dev 1 (Repositório Local Completo)"]
        R2["Dev 2 (Repositório Local Completo)"]
        R1 <-->|"git push / pull"| REM
        R2 <-->|"git push / pull"| REM
        R1 <-->|"Trabalho 100% offline e descentralizado"| R2
    end
```

- **Sistemas Centralizados (SVN / CVS):** Há um único repositório centralizado. Para inspecionar logs de commits antigos, ramificar código ou confirmar alterações, o desenvolvedor precisa de conectividade direta com o servidor. Se o servidor queimar sem backup, todo o histórico é irremediavelmente perdido.
- **Sistemas Distribuídos (Git):** Cada desenvolvedor que executa um `git clone` recebe uma **cópia integral e idêntica do repositório**, contendo cada branch, cada commit e todos os metadados históricos desde a criação do projeto. Cada máquina opera como um servidor autônomo, viabilizando operações offline instantâneas e tolerância a falhas catastróficas.
- **Snapshots vs. Deltas:**
    - Sistemas legados salvam dados como conjuntos de alterações linha a linha baseados em arquivos (**deltas baseados em diferenças**).
    - O Git não pensa em termos de deltas de arquivos: ele enxerga seus dados como um conjunto de **instantâneos completos (*snapshots*)** da árvore de arquivos no momento exato do commit. Para não desperdiçar espaço em disco, se um arquivo não sofreu nenhuma modificação entre versões, o Git não grava o arquivo novamente: ele apenas insere um ponteiro direto apontando para o snapshot anterior já armazenado.

### 1.2 O Modelo de Objetos do Git: Blobs, Trees, Commits e Tags
Toda informação persistida pelo Git reside dentro do diretório oculto `.git/objects` e é identificada unicamente pelo seu hash criptográfico (originalmente SHA-1 de 40 dígitos hexadecimais, evoluindo para SHA-256). O Git organiza seus dados em quatro tipos fundamentais de objetos:

```mermaid
flowchart TD
    C["Objeto Commit
    - Mensagem: 'feat: auditoria'
    - Autor / Committer / Timestamp
    - Pai: Hash(C0)"]
    T["Objeto Tree (Diretório Raiz)
    - src/ (Tree)
    - README.md (Blob)"]
    T2["Objeto Tree (src/)
    - index.js (Blob)
    - app.py (Blob)"]
    B1["Objeto Blob (Conteúdo de README.md)"]
    B2["Objeto Blob (Conteúdo de index.js)"]
    B3["Objeto Blob (Conteúdo de app.py)"]

    C --> T
    T --> T2
    T --> B1
    T2 --> B2
    T2 --> B3
```

1. **Blob (*Binary Large Object*):** Armazena estritamente o conteúdo binário dos dados de um arquivo. O blob **não armazena o nome do arquivo nem suas permissões de acesso** (POSIX); guarda unicamente os bytes puros. Se dois arquivos em pastas diferentes tiverem conteúdos idênticos, o Git cria um único blob para ambos.
2. **Tree (Árvore):** Representa o equivalente a uma pasta/diretório no sistema de arquivos. Uma Tree mapeia os nomes de arquivos, permissões de execução e aponta para os respectivos hashes dos Blobs ou de outras Trees filhas (subpastas).
3. **Commit:** Representa a fotografia definitiva do projeto. Aponta para a Tree raiz daquele snapshot, armazena referências para o(s) commit(s) ancestral(is) (*parents*), nome e e-mail do autor e do committer, data/hora e a mensagem descritiva do commit.
4. **Annotated Tag (Tag Anotada):** Aponta para um commit específico, contendo um nome de versão (ex.: `v1.0.0`), mensagem explicativa e assinatura criptográfica opcional (GPG).

### 1.3 As Três Áreas Locais e o Ciclo de Vida dos Arquivos
No computador local do desenvolvedor, o Git segmenta os arquivos em três áreas distintas:

```mermaid
flowchart LR
    WD["1. Working Directory
    (Arquivos físicos no disco)"] -->|"git add"| SA["2. Staging Area / Index
    (Snapshot preparado)"]
    SA -->|"git commit"| REP["3. Repositório Local / HEAD
    (Banco de objetos .git)"]
    REP -->|"git reset --soft"| SA
    REP -->|"git reset --mixed"| WD
    SA -->|"git restore --staged"| WD
```

1. **Working Directory (Diretório de Trabalho):** Diretório físico no disco rígido do sistema operacional onde os arquivos do projeto residem descompactados e onde o programador efetivamente escreve e modifica o código-fonte.
2. **Staging Area / Index (Área de Preparação):** Arquivo binário localizado em `.git/index`. Funciona como uma mesa de preparação onde o desenvolvedor seleciona e pré-agrupa exatamente quais arquivos e quais trechos modificados farão parte do próximo commit.
3. **Repositório Local (.git directory / HEAD):** O banco de dados imutável onde os commits consolidados são gravados permanentemente. O ponteiro especial **HEAD** aponta para o ramo e commit em que o desenvolvedor está atualmente trabalhando.

### 1.4 Comandos Fundamentais de Inspeção, Rastreamento e Histórico
- **`git init`:** Inicializa um repositório Git vazio criando a pasta oculta `.git`.
- **`git clone <url>`:** Clona um repositório remoto completo com todo o histórico de branches para a máquina local.
- **`git status`:** Exibe o estado comparativo das três áreas, listando arquivos não rastreados (*untracked*), modificados e preparados (*staged*).
- **`git diff`:** Exibe diferenças linha a linha:
    - `git diff`: Diferenças entre o *Working Directory* e a *Staging Area*.
    - `git diff --staged` (ou `--cached`): Diferenças entre a *Staging Area* e o último commit no *HEAD*.
- **`git add <arquivo>`:** Adiciona o snapshot do arquivo à Staging Area.
- **`git commit -m "mensagem"`:** Grava o snapshot da Staging Area permanentemente no repositório local.
- **`git log`:** Exibe a linha do tempo de commits (`--oneline`, `--graph` para visualizar ramificações).
- **`git blame <arquivo>`:** Exibe o arquivo linha por linha, informando qual autor e qual hash de commit foi responsável pela última edição de cada linha (ferramenta essencial para auditoria forense de código).

### 1.5 Ramificação e Integração: `git merge` vs. `git rebase`
Branches no Git são apenas ponteiros móveis levíssimos de 41 bytes que apontam para um hash de commit. Ao integrar alterações de ramos diferentes, existem duas abordagens fundamentais:

```mermaid
flowchart TD
    subgraph EstrategiaMerge["1. Abordagem com git merge"]
        M1["main: C1 -> C2"]
        F1["feature: C3 -> C4"]
        MC["C5: Merge Commit (Dois pais: C2 e C4)"]
        M1 --> MC
        F1 --> MC
    end
    subgraph EstrategiaRebase["2. Abordagem com git rebase"]
        R1["main: C1 -> C2"]
        R2["Reaplica C3' e C4' linearmente no topo de C2"]
        R1 --> R2
    end
```

#### Comparativo entre Merge e Rebase

| Critério | `git merge` | `git rebase` |
|---|---|---|
| **Mecânica Operacional** | Combina os ramos criando um **novo commit de junção (*Merge Commit*)** com múltiplos pais (salvo em *Fast-Forward*). | Pega os commits do ramo atual e os **reaplica individualmente um a um** no topo do ramo de destino. |
| **Linha Histórica** | Preserva o histórico não-linear fiel à cronologia dos fatos, documentando bifurcações e fusões de branches. | **Reescreve o histórico**, produzindo uma linha do tempo **estritamente linear e contínua**, sem commits de merge adicionais. |
| **Hashes Criptográficos** | **Preserva intactos** os hashes SHA-1/256 de todos os commits originais. | **Gera novos hashes criptográficos** para todos os commits que foram deslocados. |
| **Regra de Ouro da Equipe** | Seguro para qualquer branch, seja ela privada ou pública compartilhada. | ⭐ **NUNCA aplique rebase em branches públicas/compartilhadas!** Reescrever o histórico de commits já sincronizados por outros desenvolvedores quebra os repositórios locais de toda a equipe. |

### 1.6 Operações de Recuperação e Desfazer: `reset`, `revert`, `stash` e `cherry-pick`

#### 1. As Três Modalidades de `git reset`
O comando `git reset <hash>` move o ponteiro HEAD para trás:

| Modo do Reset | Efeito no HEAD | Efeito na Staging Area (Index) | Efeito no Working Directory | Caso de Uso Típico |
|---|---|---|---|---|
| **`--soft`** | Recua para o `<hash>` indicado | **Preserva todas as mudanças** (arquivos continuam *staged*) | Inalterado | Agrupar os últimos 3 commits em um único commit antes de enviar. |
| **`--mixed`** *(padrão)* | Recua para o `<hash>` indicado | **Limpa a Staging Area** (remove do *stage*) | **Preserva todas as mudanças** (arquivos ficam no disco como modificados) | Desfazer um commit para revisar alterações antes de commitar de novo. |
| **`--hard`** | Recua para o `<hash>` indicado | **Descarta e limpa tudo** | **Destrói e apaga tudo no disco** | Descartar sumariamente código recente com perda total de alterações locais. |

### 1.7 Sincronização e Fluxo Remoto: `fetch`, `pull` e `push`
- **`git remote add origin <url>`:** Vincula o repositório local a um repositório remoto.
- **`git fetch`:** Baixa todos os novos objetos e branches do servidor remoto para o repositório local, mas **não altera nem mescla nada no diretório de trabalho** do desenvolvedor (operação 100% segura para inspeção).
- **`git pull`:** Executa sequencialmente um `git fetch` seguido imediatamente por um `git merge` (ou `git rebase` se configurado) no ramo local atual.
- **`git push origin <branch>`:** Envia os novos commits locais para o servidor remoto centralizado.

---

## 2. Gerenciamento de Dependências de Software

### 2.1 Grafos de Dependência, Dependências Transitivas e Conflitos
Em engenharia de software contemporânea, quase nenhuma aplicação é construída do zero; projetos utilizam bibliotecas de terceiros que, por sua vez, dependem de outras bibliotecas:

```mermaid
flowchart TD
    App["Aplicação de Auditoria"] --> LibA["Dependência Direta: LibA v1.2"]
    App --> LibB["Dependência Direta: LibB v2.0"]
    LibA --> LibC1["Dependência Transitiva: LibC v1.0"]
    LibB --> LibC2["Dependência Transitiva: LibC v2.0 (Conflito de Versão!)"]
```

- **Dependências Diretas:** Bibliotecas declaradas explicitamente pelo desenvolvedor no arquivo de manifesto do projeto.
- **Dependências Transitivas:** Bibliotecas exigidas pelas suas dependências diretas.
- **Conflito de Dependências:** Ocorre quando duas bibliotecas exigem versões mutuamente incompatíveis de uma mesma biblioteca transitiva (ex.: a famosa problemática do *"Dependency Hell"*).

### 2.2 Versionamento Semântico (SemVer 2.0.0)
A especificação universal SemVer define como os softwares devem rotular suas versões públicas através do formato de três inteiros separados por ponto:

$$\textbf{MAJOR} \,.\, \textbf{MINOR} \,.\, \textbf{PATCH}$$

```mermaid
flowchart LR
    V["Versão Atual: 2.4.1"]
    V -->|"Correção de bug retrocompatível"| P["2.4.2 (PATCH)"]
    V -->|"Nova função retrocompatível"| M["2.5.0 (MINOR)"]
    V -->|"Alteração que quebra a API"| MAJ["3.0.0 (MAJOR)"]
```

1. **MAJOR (Quebra de Compatibilidade Reversa / *Breaking Changes*):** Incrementado quando são realizadas modificações substanciais na API pública que tornam o código incompatível com versões anteriores. Consumidores precisam alterar seus códigos para não quebrar.
2. **MINOR (Novas Funcionalidades Retrocompatíveis):** Incrementado quando novos métodos, classes ou funcionalidades são adicionados à biblioteca, mas preservando 100% da compatibilidade com o código pré-existente (*backwards-compatible*).
3. **PATCH (Correções de Bugs Retrocompatíveis):** Incrementado estritamente para correção de defeitos internos, bugs ou vulnerabilidades de segurança que não alteram a assinatura nem o comportamento da API pública.

#### Sintaxe de Prefixos de Versão no `npm` (Node.js)
- **Til (`~1.2.3`):** Autoriza atualizações apenas no nível de **PATCH** ($\ge 1.2.3 \text{ e } < 1.3.0$).
- **Circunflexo (`^1.2.3`):** Autoriza atualizações no nível de **MINOR e PATCH** ($\ge 1.2.3 \text{ e } < 2.0.0$).
- **Versão Exata (`1.2.3`):** Sem prefixos; trava estritamente naquela versão.

### 2.3 Manifestos vs. Arquivos de Trava (Lockfiles) e o Comando `npm ci`
- **Arquivo de Manifesto (`package.json`, `pom.xml`, `requirements.txt`):** Descreve os metadados do projeto e declara faixas de tolerância flexíveis para as dependências (ex.: `"express": "^4.18.0"`).
- **Arquivo de Trava (*Lockfile* - `package-lock.json`, `poetry.lock`, `yarn.lock`):** É gerado automaticamente pelo gerenciador de pacotes para congelar a **árvore completa e exata de dependências transitivas**, gravando a versão exata de cada subdependência instalada e o seu **hash criptográfico de integridade** (`integrity: sha512-..`). Garante compilações 100% determinísticas e reproduzíveis em qualquer máquina.

> 🚨 **ALERTA DE PROVA / FCC:**  
> **`npm install` vs. `npm ci` em Esteiras de CI/CD:**  
>
> - Em esteiras de Integração Contínua (CI/CD) de produção, **NUNCA se deve rodar `npm install`**. O `npm install` pode atualizar dependências permitidas pelas faixas do manifesto e regerar o `package-lock.json`, introduzindo código não testado em produção.
> - O comando correto e padronizado para esteiras automatizadas é o **`npm ci`** (*Clean Install*). Ele apaga a pasta `node_modules` inteira e instala rigorosamente o que está congelado no `package-lock.json`. Se houver qualquer discrepância entre o manifesto e o lockfile, ele aborta a esteira com erro.

### 2.4 Ecossistemas de Dependências: Node.js (npm), Python (pip/Poetry) e Java (Maven)

| Ecossistema | Gerenciador de Pacotes | Arquivo de Manifesto | Arquivo de Trava (*Lockfile*) | Repositório Central Público |
|---|---|---|---|---|
| **JavaScript / Node.js** | npm / Yarn / pnpm | `package.json` | `package-lock.json` / `yarn.lock` | npmjs.com |
| **Python** | pip / Poetry / Pipenv | `pyproject.toml` / `requirements.txt` | `poetry.lock` / `Pipfile.lock` | PyPI (*Python Package Index*) |
| **Java** | Apache Maven / Gradle | `pom.xml` / `build.gradle` | `gradle.lockfile` (ou hashes locais) | Maven Central |

### 2.5 O Ciclo de Vida Padrão do Apache Maven
No ecossistema Java corporativo, o Apache Maven organiza o processo de construção em fases sequenciais imutáveis dentro do seu ciclo de vida padrão (*default lifecycle*):

```mermaid
flowchart LR
    V["validate"] --> C["compile"]
    C --> T["test"]
    T --> P["package"]
    P --> VF["verify"]
    VF --> I["install"]
    I --> D["deploy"]
```

1. **`validate`:** Valida se a estrutura do projeto está correta e se todas as informações do `pom.xml` estão preenchidas.
2. **`compile`:** Compila o código-fonte Java (`.java`) localizado em `src/main/java` gerando os arquivos de bytecode (`.class`).
3. **`test`:** Executa os testes automatizados unitários (JUnit) localizados em `src/test/java`.
4. **`package`:** Empacota o código compilado no formato de distribuição configurado (`.jar` ou `.war`).
5. **`verify`:** Executa testes de integração para verificar critérios de qualidade e conformidade do pacote.
6. **`install`:** Copia o pacote gerado para o **repositório local do desenvolvedor** (localizado em `~/.m2/repository`), disponibilizando o artefato como dependência para outros projetos locais na mesma máquina.
7. **`deploy`:** Copia o pacote final para o **repositório corporativo remoto compartilhado** (ex.: Nexus ou JFrog Artifactory) para distribuição oficial.

---

## 3. Empacotamento Web e Publicação de Aplicações

### 3.1 Empacotadores Web Modernos (Webpack, Vite, Rollup e esbuild)
No desenvolvimento front-end moderno, o código-fonte é decomposto em centenas de componentes JSX/TSX, folhas de estilo SASS/CSS e imagens. Navegadores não executam esses formatos diretamente de forma eficiente sem empacotamento.

- **Module Bundling:** Processo que analisa o grafo de dependências a partir de um arquivo de entrada (*entry point* como `index.tsx`) e consolida todos os recursos em arquivos estáticos otimizados (HTML, JS, CSS) dentro da pasta de produção (geralmente `dist/` ou `build/`).
- **Ferramentas:**
    - **Webpack:** O empacotador tradicional mais maduro e configurável do mercado.
    - **Vite:** Ferramenta moderna de alta velocidade que utiliza o motor **esbuild** (escrito em Go) para pré-empacotamento instantâneo em desenvolvimento e o **Rollup** para gerar o bundle final de produção.

### 3.2 Otimizações de Produção: Tree Shaking, Code Splitting e Minificação

```mermaid
flowchart TD
    subgraph Otimizacoes["Técnicas de Otimização no Empacotamento"]
        TS["Tree Shaking
        Eliminação de código morto (dead code)
        Baseado na sintaxe estática de ES Modules (import/export)"]
        CS["Code Splitting
        Divisão do bundle em múltiplos pedaços (chunks)
        Carregamento sob demanda (lazy loading)"]
        MIN["Minificação
        Remoção de espaços, comentários e encurtamento de identificadores
        Reduz drásticamente o tamanho em bytes"]
    end
```

- **Tree Shaking (Eliminação de Código Morto):** Técnica onde o empacotador inspeciona a árvore de dependências e **descarta funções, classes ou variáveis importadas que nunca são invocadas na lógica do sistema**. Baseia-se exclusivamente na análise estática dos módulos ECMAScript (ESM `import` e `export`). Não funciona adequadamente com CommonJS (`require()`), pois o CommonJS é dinâmico.
- **Code Splitting (Divisão de Código):** Estratégia de dividir o pacote JavaScript final em arquivos menores (*chunks*). Em vez de o usuário baixar 5 MB de código para abrir a tela de login, o navegador baixa apenas o essencial, carregando outras telas sob demanda via importações dinâmicas (`React.lazy()` / `import()`).
- **Minificação e Ofuscação:** Processo automatizado que remove todos os espaços em branco, quebras de linha e comentários, além de renomear variáveis longas para letras únicas (`function processarAuditoriaFiscal()` $\rightarrow$ `function a()`), reduzindo o payload e dificultando a engenharia reversa.

### 3.3 Empacotamento de Backend: JAR/WAR, Wheels Python e Repositórios Corporativos

#### Formatos de Distribuição
- **Java Executável (*Fat JAR* / *Uber JAR*):** Padrão dominante em microsserviços modernos (como Spring Boot). Empacota em um único arquivo `.jar` todo o código compilado da aplicação, todas as bibliotecas de dependência de terceiros e um **servidor web embutido** (Tomcat ou Jetty), permitindo execução direta pelo comando `java -jar aplicacao.jar` sem depender de servidores pré-instalados.
- **Java WAR (*Web Application Archive*):** Padrão corporativo legado contendo a estrutura de pastas `WEB-INF`, concebido para ser implantado dentro de servidores de aplicação compartilhados (*standalone application servers* como WildFly ou WebLogic).
- **Python Wheel (`.whl` - PEP 427):** Formato padrão de distribuição de pacotes binários pré-compilados em Python. Evita a execução de scripts de compilação C (`setup.py`) durante a instalação pelo `pip`, garantindo instalações até 10 vezes mais rápidas.

#### Repositórios Corporativos de Artefatos
Em ambientes corporativos como tribunais de contas, o acesso a repositórios públicos (npm, PyPI, Maven Central) é intermediado por gerenciadores de repositório privados como **Sonatype Nexus**, **JFrog Artifactory** ou **GitHub Packages**.

- Funcionam como proxy de cache local de dependências externas.
- Permitem aplicar varreduras automatizadas de segurança e vulnerabilidades conhecidas (CVEs) antes de permitir a instalação no ambiente governamental.

---

## 4. Fontes Recomendadas na Internet

* [Git Official Documentation - Git Rebase](https://git-scm.com/docs/git-rebase) - Reescrevendo histórico, rebase linear vs. merge commit e resolução de conflitos.
* [Git Official Documentation - Git Merge](https://git-scm.com/docs/git-merge) - Algoritmos de junção de branches, Fast-Forward e 3-way merge.
* [Semantic Versioning 2.0.0 Specification](https://semver.org/lang/pt-BR/) - Regras formais para versionamento MAJOR.MINOR.PATCH e compatibilidade de API.
* [Martin Fowler - Patterns for Managing Source Code Branches](https://martinfowler.com/articles/branching-patterns.html) - Padrões de branching, Trunk-Based Development e Feature Branches.
* CHACON, Scott; STRAUB, Ben. **Pro Git**. 2. ed. Nova York: Apress, 2014. (Cap. 3 - Git Branching e Integração).
* HUMBLE, Jez; FARLEY, David. **Entrega Contínua: Como Entregar Software de Forma Rápida e Confiável**. Porto Alegre: Bookman, 2014. (Cap. 14 - Gestão Avançada de Versionamento e Dependências).
* LOELIGER, Jon; MCCULLOUGH, Matthew. **Version Control with Git**. 2. ed. Sebastopol: O'Reilly Media, 2012. (Cap. 8 e 9 - Rebase, Hook Scripts e Gestão de Branches).
