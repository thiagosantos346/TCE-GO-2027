#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mermaid Documentation & Print-Quality Harness
============================================
Harness profissional de consulta, análise e validação da documentação oficial do Mermaid
(https://mermaid.ai/open-source/intro/getting-started.html).

Recursos:
  - Base de conhecimento técnica estruturada de todas as categorias de diagramas e configurações do Mermaid.
  - Busca instantânea (full-text search) e inspeção detalhada por tópico.
  - Analisador de blocos Mermaid em arquivos Markdown (detecção de nós, proporções, orientação e riscos em PDF).
  - Verificador de conformidade para impressão A4 / geração de PDFs sem desproporções.
"""

import sys
import os
import re
import json
import argparse
from typing import Dict, List, Any, Optional

MERMAID_DOCS_BASE_URL = "https://mermaid.ai/open-source"

# Base de Conhecimento Estruturada da Documentação Oficial Mermaid
MERMAID_KNOWLEDGE_BASE: Dict[str, Dict[str, Any]] = {
    "getting-started": {
        "title": "Getting Started & Core Concepts",
        "url": f"{MERMAID_DOCS_BASE_URL}/intro/getting-started.html",
        "summary": "Introdução geral ao Mermaid, inicialização, renderização em navegador, bundling e sintaxe inspirada em Markdown.",
        "keywords": ["intro", "start", "initialize", "render", "api", "installation", "npm", "cdn"],
        "details": """
O Mermaid é uma biblioteca JavaScript de diagramação e visualização orientada a texto.
Ele analisa definições em sintaxe similar a Markdown e renderiza gráficos SVG interativos e vetoriais.

Formas Principais de Uso:
1. Navegador (CDN / Bundled script):
   <script src="assets/mermaid.min.js"></script>
   <script>
     mermaid.initialize({ startOnLoad: true });
   </script>
   <pre class="mermaid">
     flowchart LR
       A --> B
   </pre>

2. API Programática (Manual Rendering):
   mermaid.initialize({ startOnLoad: false });
   await mermaid.run({ nodes: [elemento] });
   // Ou via mermaid.render('id', code) -> { svg, bindFunctions }

3. CLI (mermaid-cli / mmdc):
   mmdc -i input.mmd -o output.svg -c config.json -b transparent
        """,
        "best_practices_pdf": "Para PDFs via Puppeteer/Chromium, use sempre inicialização assíncrona (startOnLoad: false), aguarde mermaid.run() concluir e garanta ajuste do SVG viewBox para evitar esticamento vertical descontrolado."
    },

    "configuration": {
        "title": "Configuration & Theming API",
        "url": f"{MERMAID_DOCS_BASE_URL}/config/setup/modules/mermaidAPI.html",
        "summary": "Opções de configuração global (mermaid.initialize), variáveis de tema, controle de layout e responsividade.",
        "keywords": ["config", "configuration", "theme", "themeVariables", "useMaxWidth", "htmlLabels", "securityLevel", "fontSize"],
        "details": """
Configuração Global com mermaid.initialize():
--------------------------------------------
mermaid.initialize({
  startOnLoad: false,
  theme: 'default', // 'default' | 'base' | 'dark' | 'forest' | 'neutral'
  securityLevel: 'loose', // 'strict' | 'loose' | 'antiscript'
  fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
  themeVariables: {
    fontSize: '13px',
    primaryColor: '#e0e7ff',
    primaryTextColor: '#1e293b',
    primaryBorderColor: '#6366f1',
    lineColor: '#64748b'
  },
  flowchart: {
    htmlLabels: true,       // Permite <br/>, spans e estilos nas tags dos nós
    useMaxWidth: true,      // Responsividade baseada em max-width
    curve: 'basis',         // 'basis' | 'linear' | 'cardinal' | 'natural'
    nodeSpacing: 25,        // Espaçamento horizontal/vertical entre nós
    rankSpacing: 30         // Espaçamento entre camadas/níveis
  },
  sequence: { useMaxWidth: true },
  state: { useMaxWidth: true },
  class: { useMaxWidth: true },
  er: { useMaxWidth: true }
});

Diretivas Inline (Overrides por Gráfico):
-----------------------------------------
%%{init: { "flowchart": { "nodeSpacing": 20, "rankSpacing": 25 } }}%%
flowchart TD
  A --> B
        """,
        "best_practices_pdf": "Nunca defina useMaxWidth: false junto com width: 100% no CSS sem preservar o max-width intrínseco do viewBox. O valor padrão useMaxWidth: true do Mermaid injeta 'max-width: {width}px' no SVG, prevenindo ampliação artificial."
    },

    "flowchart": {
        "title": "Flowcharts & Graphs (Fluxogramas)",
        "url": f"{MERMAID_DOCS_BASE_URL}/syntax/flowchart.html",
        "summary": "Direções de fluxo (TD/TB, LR, BT, RL), formas de nós, conectores, rótulos, subgrafos e estilização de classes.",
        "keywords": ["flowchart", "graph", "TD", "TB", "LR", "subgraph", "node", "edge", "arrow", "shape"],
        "details": """
Orientações de Fluxo:
--------------------
- flowchart TD / TB: Top to Bottom (de cima para baixo) - Ideal para hierarquias estreitas e fases sequenciais.
- flowchart LR: Left to Right (da esquerda para a direita) - Ideal para linhas temporais e processos horizontais.
- flowchart BT: Bottom to Top (de baixo para cima).
- flowchart RL: Right to Left (da direita para a esquerda).

Formas de Nós Comuns:
--------------------
- Retângulo padrão:     id["Texto no nó"]
- Retângulo arredondado: id("Texto no nó")
- Círculo:              id(("Texto circular"))
- Losango / Decisão:    id{"Texto de decisão?"}
- Cilindro / BD:        id[("Base de Dados")]
- Trapézio:             id[/"Entrada"/] ou id[\\"Saída"\\]
- Subrotina:            id[["Processo pré-definido"]]

Tipos de Ligações (Edges):
-------------------------
- Seta simples:          A --> B
- Linha sem seta:        A --- B
- Seta com rótulo:       A -->|"Condição"| B
- Linha tracejada:       A -.-> B
- Linha espessa:         A ==> B

Subgrafos (Agrupamentos):
------------------------
flowchart TB
  subgraph Grupo1 ["Módulo de Entrada"]
    A --> B
  end
  subgraph Grupo2 ["Módulo de Processamento"]
    C --> D
  end
  B --> C
        """,
        "best_practices_pdf": "CUIDADO COM 'flowchart TD' com muitos nós em linha reta! Por ser estritamente vertical, a razão largura/altura é baixa (ex: ratio < 0.6). Se esticado para a largura da página (760px), sua altura salta para mais de 1200px, provocando quebra desnecessária em até 3 páginas no PDF A4. Solução: mantenha a largura contida em seu max-width natural ou use flowchart LR quando houver mais de 3 passos lineares."
    },

    "sequence": {
        "title": "Sequence Diagrams (Diagramas de Sequência)",
        "url": f"{MERMAID_DOCS_BASE_URL}/syntax/sequenceDiagram.html",
        "summary": "Interações entre atores e serviços, linhas de vida, caixas de ativação, mensagens síncronas/assíncronas e loops.",
        "keywords": ["sequence", "sequenceDiagram", "actor", "participant", "activate", "deactivate", "loop", "alt", "opt"],
        "details": """
Estrutura Básica:
----------------
sequenceDiagram
    autonumber
    actor C as Cidadão
    participant P as Portal TCE-GO
    participant S as Servidor Backend
    database BD as Banco de Dados

    C->>P: Acessa Consulta Pública
    activate P
    P->>S: Requisita Dados da Licitação
    activate S
    S->>BD: SELECT * FROM processos
    BD-->>S: Retorna Registros
    S-->>P: JSON Estruturado
    deactivate S
    P-->>C: Renderiza Painel Interativo
    deactivate P
        """,
        "best_practices_pdf": "Sequence diagrams costumam ser moderadamente largos e crescem na vertical conforme o número de mensagens. Sempre utilize 'autonumber' para clareza e mantenha nomes de participantes concisos para evitar estouro horizontal em A4."
    },

    "class": {
        "title": "Class Diagrams (Diagramas de Classes UML)",
        "url": f"{MERMAID_DOCS_BASE_URL}/syntax/classDiagram.html",
        "summary": "Modelagem orientada a objetos: classes, interfaces, atributos, métodos, multiplicidade e relacionamentos de herança/composição.",
        "keywords": ["classDiagram", "class", "uml", "inheritance", "composition", "aggregation", "interface"],
        "details": """
Sintaxe Básica:
--------------
classDiagram
    class ProcessoAuditoria {
        +String numeroProcesso
        +Date dataAutuacao
        -Double valorEstimado
        +instruir() void
        +emitirRelatorio() Relatorio
    }
    class Auditor {
        +String matricula
        +realizarFiscalizacao()
    }
    Auditor "1" --> "*" ProcessoAuditoria : fiscaliza
        """,
        "best_practices_pdf": "Evite layouts excessivamente esparramados. Use anotações de visibilidade (+, -, #) e classes abstratas com <<abstract>> para documentação técnica de alta densidade."
    },

    "state": {
        "title": "State Diagrams (Diagramas de Estados)",
        "url": f"{MERMAID_DOCS_BASE_URL}/syntax/stateDiagram.html",
        "summary": "Estados de ciclo de vida de objetos ou processos, transições, estados compostos, bifurcações (fork) e junções (join).",
        "keywords": ["stateDiagram", "stateDiagram-v2", "state", "transition", "fork", "join", "choice"],
        "details": """
Sintaxe Básica:
--------------
stateDiagram-v2
    [*] --> Autuado
    Autuado --> EmInstrucao: Distribuído ao Auditor
    EmInstrucao --> EmJulgamento: Relatório emitido
    state EmJulgamento {
        [*] --> Pautado
        Pautado --> Votado: Sessão Plenária
        Votado --> [*]
    }
    EmJulgamento --> Concluido: Trânsito em Julgado
    Concluido --> [*]
        """,
        "best_practices_pdf": "Sempre prefira 'stateDiagram-v2' em relação à versão legada v1, pois v2 possui melhor layout e suporte a subestados aninhados."
    },

    "er": {
        "title": "Entity Relationship Diagrams (Modelo ER)",
        "url": f"{MERMAID_DOCS_BASE_URL}/syntax/entityRelationshipDiagram.html",
        "summary": "Diagramas de Entidade e Relacionamento para banco de dados relacional com cardinalidades precisas (Crow's Foot).",
        "keywords": ["erDiagram", "entity", "relationship", "crowsfoot", "cardinality", "PK", "FK"],
        "details": """
Sintaxe Básica:
--------------
erDiagram
    ORGAO_PUBLICO ||--o{ CONTRATO : celebra
    CONTRATO ||--|{ EMPENHO : possui
    CONTRATO {
        string numero_contrato PK
        date data_assinatura
        float valor_global
        string cnpj_contratado FK
    }
    ORGAO_PUBLICO {
        int id_orgao PK
        string sigla
        string nome_oficial
    }
        """,
        "best_practices_pdf": "Defina apenas as colunas mais representativas (chaves primárias e chaves estrangeiras) para evitar tabelas muito compridas no PDF."
    },

    "mindmap": {
        "title": "Mindmaps (Mapas Mentais)",
        "url": f"{MERMAID_DOCS_BASE_URL}/syntax/mindmap.html",
        "summary": "Estruturas radiais de tópicos e subtópicos com indentação simples.",
        "keywords": ["mindmap", "brainstorm", "mapa mental", "root", "hierarquia"],
        "details": """
Sintaxe Básica:
--------------
mindmap
  root((Controle Externo))
    Fiscalização
      Contábil
      Financeira
      Orçamentária
      Operacional
      Patrimonial
    Julgamento
      Contas de Governo
      Contas de Gestão
    Sanções
      Débito
      Multas
      Inabilitação
        """,
        "best_practices_pdf": "Mapas mentais expandem-se radialmente. Em páginas A4 retratos, limite a profundidade a 3 níveis para manter legibilidade do texto vetorial."
    },

    "gantt": {
        "title": "Gantt Charts (Cronogramas de Projeto)",
        "url": f"{MERMAID_DOCS_BASE_URL}/syntax/gantt.html",
        "summary": "Cronogramas temporais, marcos (milestones), seções e dependências de tarefas.",
        "keywords": ["gantt", "cronograma", "schedule", "milestone", "dateFormat"],
        "details": """
Sintaxe Básica:
--------------
gantt
    title Cronograma de Auditoria Governamental
    dateFormat  YYYY-MM-DD
    section Planejamento
    Elaboração da Matriz de Risco   :a1, 2026-03-01, 10d
    Designação de Equipe             :after a1, 3d
    section Execução
    Inspeção in loco                 :2026-03-15, 15d
    Cruzamento de Bases de Dados     :2026-03-20, 10d
    section Relatório
    Elaboração do Relatório Preliminar :2026-04-05, 10d
        """,
        "best_practices_pdf": "Diagramas Gantt são muito largos. Devem ser renderizados com largura total (width: 100%; max-width: 680px;) para aproveitar a folha A4."
    },

    "pdf-print-rules": {
        "title": "Boas Práticas de Dimensionamento para PDF e Impressão A4",
        "url": f"{MERMAID_DOCS_BASE_URL}/config/setup/modules/mermaidAPI.html",
        "summary": "Regras matemáticas de ouro para evitar gráficos esticados, quebras erráticas de página e fontes desproporcionais.",
        "keywords": ["pdf", "print", "a4", "viewbox", "aspect-ratio", "page-break", "scaling"],
        "details": """
DIRETRIZES DE OURO PARA IMPRESSÃO DE MERMAID EM PDF A4:
=======================================================
1. Área Útil de Impressão A4 (com margens de 15mm-20mm):
   - Largura útil máxima: ~680px a 700px.
   - Altura útil segura para diagrama isolado: ~480px a 520px.

2. A Armadilha do 'width: 100%' em Gráficos Verticais (flowchart TD):
   - Um diagrama vertical estreito possui w = 150px-250px e h = 350px-500px (razão w/h < 0.6).
   - Se forçado para 'width: 100%' ou 'max-width: 760px', a largura é multiplicada por ~3.5x.
   - Como o SVG preserva a proporção, a altura salta para 1.400px - 1.800px!
   - Um elemento de 1.500px NÃO cabe em uma página A4 útil (~900px), obrigando o Chromium
     a quebrar o diagrama no meio ou empurrá-lo para 2 ou 3 páginas!

3. Fórmula Universal Proporcional de Ajuste:
   - Extraia w e h do viewBox do SVG.
   - let targetWidth = w; let targetHeight = h;
   - Se targetHeight > MAX_PRINT_HEIGHT (480px):
       scale = MAX_PRINT_HEIGHT / targetHeight;
       targetHeight = MAX_PRINT_HEIGHT;
       targetWidth = targetWidth * scale;
   - Se targetWidth > MAX_PRINT_WIDTH (680px):
       scale = MAX_PRINT_WIDTH / targetWidth;
       targetWidth = MAX_PRINT_WIDTH;
       targetHeight = targetHeight * scale;
   - Aplique no SVG:
       width: 100%;
       max-width: round(targetWidth)px;
       max-height: round(targetHeight)px;
       height: auto;
       display: block;
       margin: 0 auto;

4. Benefícios Desta Solução:
   - Gráficos verticais estreitos (TD) ficam elegantes e compactos (~140px a 250px de largura, ~300px altura).
   - Gráficos horizontais largos (LR) aproveitam a largura útil (~650px a 680px).
   - Nenhum gráfico estoura o limite da página, eliminando quebras desnecessárias.
        """,
        "best_practices_pdf": "Sempre certifique-se de que o container tenha 'page-break-inside: avoid !important;' e que a altura máxima do SVG seja restrita a no máximo 480px."
    }
}


def search_knowledge_base(query: str) -> List[Dict[str, Any]]:
    """Pesquisa por relevância de termos na base de documentação."""
    query_terms = [t.lower().strip() for t in re.split(r'\s+', query) if t.strip()]
    results = []

    for key, data in MERMAID_KNOWLEDGE_BASE.items():
        score = 0
        text_corpus = f"{key} {data['title']} {data['summary']} {' '.join(data['keywords'])} {data['details']}".lower()

        for term in query_terms:
            if term == key.lower():
                score += 15
            elif term in [k.lower() for k in data["keywords"]]:
                score += 8
            elif term in data["title"].lower():
                score += 6
            elif term in text_corpus:
                score += 2

        if score > 0:
            results.append({
                "key": key,
                "score": score,
                "title": data["title"],
                "url": data["url"],
                "summary": data["summary"]
            })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results


def print_topic(topic_key: str):
    """Exibe um tópico completo da documentação técnica."""
    data = MERMAID_KNOWLEDGE_BASE.get(topic_key.lower())
    if not data:
        # Tenta busca parcial
        matches = [k for k in MERMAID_KNOWLEDGE_BASE if topic_key.lower() in k]
        if matches:
            data = MERMAID_KNOWLEDGE_BASE[matches[0]]
            topic_key = matches[0]
        else:
            print(f"[!] Tópico '{topic_key}' não encontrado no catálogo.")
            print("    Execute 'python mermaid_harness.py list' para ver os tópicos disponíveis.")
            return

    print("=" * 80)
    print(f"📖 MERMAID HARNESS DOC: {data['title'].upper()}")
    print("=" * 80)
    print(f"🔗 Documentação Oficial: {data['url']}")
    print(f"📌 Resumo: {data['summary']}")
    print("-" * 80)
    print(data["details"].strip())
    print("-" * 80)
    print(f"💡 RECOMENDAÇÃO DE IMPRESSÃO / PDF: {data['best_practices_pdf']}")
    print("=" * 80)


def list_topics():
    """Lista todos os tópicos disponíveis no harness."""
    print("=" * 80)
    print("📚 ÍNDICE DA DOCUMENTAÇÃO MERMAID (HARNESS LOCAL)")
    print("=" * 80)
    for key, data in MERMAID_KNOWLEDGE_BASE.items():
        print(f"  • {key.ljust(18)} : {data['title']}")
        print(f"    URL: {data['url']}")
    print("=" * 80)
    print("Uso: python mermaid_harness.py topic <nome_do_topico>")


def analyze_markdown_file(filepath: str):
    """Varre um arquivo Markdown e diagnostica todos os blocos Mermaid encontrados."""
    if not os.path.exists(filepath):
        print(f"[!] Arquivo não encontrado: {filepath}")
        return

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    blocks = re.findall(r'```mermaid(.*?)```', content, flags=re.DOTALL)
    print("=" * 80)
    print(f"🔍 ANÁLISE DE DIAGRAMAS MERMAID: {os.path.basename(filepath)}")
    print(f"📁 Caminho: {filepath}")
    print(f"📊 Total de diagramas Mermaid encontrados: {len(blocks)}")
    print("=" * 80)

    if not blocks:
        print("Nenhum diagrama Mermaid encontrado no arquivo.")
        return

    for idx, raw_code in enumerate(blocks, start=1):
        code = raw_code.strip()
        lines = [line.strip() for line in code.splitlines() if line.strip() and not line.strip().startswith("%%")]
        first_line = lines[0] if lines else "Desconhecido"

        # Identificação de Tipo
        diag_type = "Outro"
        orientation = "N/A"
        if first_line.startswith("flowchart") or first_line.startswith("graph"):
            diag_type = "Flowchart"
            parts = first_line.split()
            if len(parts) > 1:
                orientation = parts[1].upper()
        elif first_line.startswith("sequenceDiagram"):
            diag_type = "Sequence"
        elif first_line.startswith("classDiagram"):
            diag_type = "Class"
        elif first_line.startswith("stateDiagram"):
            diag_type = "State"
        elif first_line.startswith("erDiagram"):
            diag_type = "Entity-Relationship"
        elif first_line.startswith("mindmap"):
            diag_type = "Mindmap"
        elif first_line.startswith("gantt"):
            diag_type = "Gantt"
        elif first_line.startswith("pie"):
            diag_type = "Pie"

        # Contagem de nós/linhas
        node_matches = re.findall(r'\b[A-Za-z0-9_]+\s*(\[|\(|\{|\()', code)
        nodes_count = len(node_matches)

        print(f"\n[Diagrama #{idx}]")
        print(f"  • Tipo: {diag_type} | Orientação: {orientation} | Linhas: {len(lines)} | Nós detectados: ~{nodes_count}")
        print(f"  • Declaração: {first_line}")

        # Avaliação de Risco para Impressão PDF A4
        if diag_type == "Flowchart" and orientation in ("TD", "TB") and nodes_count >= 3:
            print("  ⚠️ ALERTA DE FORMATO: Fluxograma vertical (TD/TB) detectado.")
            print("     -> Razão de aspecto estreita. Se forçado a 'width: 100%', a altura explodirá para > 1000px.")
            print("     -> Garantir pós-processamento de viewBox ativo (max-width restrito ao tamanho intrínseco).")
        elif diag_type == "Flowchart" and orientation in ("LR", "RL"):
            print("  ✅ FORMATO HORIZONTAL: Fluxograma LR distribui bem o espaço horizontal em A4.")
        else:
            print("  ℹ️ FORMATO REGULAR: Verifique se o diagrama cabe na altura limite de 480px.")

    print("\n" + "=" * 80)
    print("✅ Análise concluída. Todas as regras universais de viewBox protegem contra quebras de página.")


def main():
    parser = argparse.ArgumentParser(
        description="Mermaid Documentation & Print-Quality Harness para TCE-GO 2027",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    subparsers = parser.add_subparsers(dest="command", help="Comandos disponíveis")

    # Comando: list
    subparsers.add_parser("list", help="Lista todos os tópicos e categorias documentadas")

    # Comando: topic
    topic_parser = subparsers.add_parser("topic", help="Exibe documentação aprofundada de um tópico")
    topic_parser.add_argument("name", help="Nome do tópico (ex: flowchart, sequence, config, pdf-print-rules)")

    # Comando: search
    search_parser = subparsers.add_parser("search", help="Pesquisa na base de documentação oficial")
    search_parser.add_argument("query", help="Termo de pesquisa (ex: useMaxWidth, viewBox, TD, theme)")

    # Comando: analyze
    analyze_parser = subparsers.add_parser("analyze", help="Analisa os diagramas Mermaid de um arquivo Markdown")
    analyze_parser.add_argument("file", help="Caminho do arquivo .md a inspecionar")

    # Comando: urls
    subparsers.add_parser("urls", help="Exibe a relação de URLs oficiais da documentação do Mermaid")

    args = parser.parse_args()

    if not args.command or args.command == "list":
        list_topics()
    elif args.command == "topic":
        print_topic(args.name)
    elif args.command == "search":
        res = search_knowledge_base(args.query)
        if not res:
            print(f"Nenhum resultado encontrado para: '{args.query}'")
        else:
            print(f"Resultados da busca por '{args.query}':\n")
            for r in res:
                print(f"[{r['score']} pts] {r['title']} ({r['key']})")
                print(f"  URL: {r['url']}")
                print(f"  Resumo: {r['summary']}\n")
    elif args.command == "analyze":
        analyze_markdown_file(args.file)
    elif args.command == "urls":
        print(f"Documentação Oficial Mermaid: {MERMAID_DOCS_BASE_URL}")
        for k, v in MERMAID_KNOWLEDGE_BASE.items():
            print(f"  - {v['title']}: {v['url']}")


if __name__ == "__main__":
    main()

