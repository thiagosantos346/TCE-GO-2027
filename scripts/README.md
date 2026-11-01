# Arquitetura de Scripts e Ferramental do Projeto

Este diretório centraliza os scripts de automação, auditoria, sanitização e injeção do projeto **TCE-GO 2027**, garantindo conformidade com as diretrizes de governança e alta fidelidade do material.

## Estrutura de Scripts

- **`audit_questions.py`**:
  Audita e gera o relatório estatístico consolidado de questões por módulo e globalmente, calculando os percentuais de questões reais oficiais versus simuladas.
  ```bash
  python scripts/audit_questions.py
  ```

- **`clean_database_artifacts.py`**:
  Sanitiza o banco de dados oficial (`banco_questoes_extraidas.json`), removendo artefatos de paginação, rodapés e cabeçalhos residuais de OCR/PDF sem alterar o conteúdo técnico das questões.
  ```bash
  python scripts/clean_database_artifacts.py
  ```

- **`purge_out_of_scope_questions.py`**:
  Motor de expurgo que remove permanentemente do banco `banco_questoes_extraidas.json` questões fora do escopo de Controle Externo (engenharia civil pesada, mecânica térmica, ciências atuariais, odontologia e biologia).
  ```bash
  python scripts/purge_out_of_scope_questions.py
  ```

- **`rollback_and_audit.py`**:
  Motor de auditoria semântica 1:1 e rollback cirúrgico via Git. Compara cada item frente ao commit base `6a1eac1`, reverte questões intrusas/desconexas e restaura os blocos originais aderentes preservando as questões reais legítimas.
  ```bash
  python scripts/rollback_and_audit.py
  ```

- **`generate_coverage_report.py`**:
  Gera na raiz do projeto o `relatorio_cobertura_questoes.md` consolidando a cobertura real vs. simulada por módulo e arquivo.
  ```bash
  python scripts/generate_coverage_report.py
  ```

- **`mass_injector.py`**:
  *(Atenção: Uso restrito)* Motor de injeção que deve ser utilizado apenas com rigorosa conferência semântica prévia para evitar substituições desconexas.
