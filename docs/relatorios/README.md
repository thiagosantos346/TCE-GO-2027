# Acervo Oficial de Relatórios Técnicos & Auditorias: TCE-GO 2027

Este diretório concentra todos os relatórios gerenciais, auditorias semânticas RAG e inventários estatísticos gerados no projeto de preparação para o Concurso do TCE-GO 2027.

---

## 🗂️ Relação de Relatórios Disponíveis

| Documento | Descrição e Finalidade | Status |
| :--- | :--- | :---: |
| [Relatório de Cobertura de Questões Reais](./relatorio_cobertura_questoes.md) | Cobertura quantitativa e qualitativa do banco vetorial MCP de questões reais vs. simuladas por módulo e caderno. | 🟢 Atualizado |
| [Relatório de Auditoria e Injeção Semântica RAG](./relatorio_auditoria_cadernos_rag.md) | Registro detalhado da auditoria 1:1 e substituição semântica de questões mantendo aderência ao edital. | 🟢 Atualizado |
| [Relatório Estatístico Consolidado](./relatorio_estatisticas_gerais.md) | Inventário completo de métricas: cadernos, questões, palavras, caracteres, diagramas Mermaid, fórmulas KaTeX e páginas de PDF. | 🟢 Atualizado |

---

## 🔄 Scripts de Geração e Manutenção
- `src/injection/generate_coverage_report.py`: Atualiza o relatório de cobertura a partir do banco oficial V3.
- `src/injection/audit_questions.py`: Executa a auditoria no terminal e valida integridade.
- `src/utils/audit_math_and_diagrams.py`: Audita sintaxe de diagramas Mermaid e fórmulas matemáticas.
- `src/utils/update_all_readmes.py`: Sincroniza tabelas nos READMEs com a base fática.
