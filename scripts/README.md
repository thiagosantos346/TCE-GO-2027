# Arquitetura de Scripts e Ferramental do Projeto

Este diretório centraliza os scripts de automação, auditoria e injeção do projeto **TCE-GO 2027**, garantindo conformidade com as diretrizes de governança e alta fidelidade do material.

## Estrutura

- **`audit_questions.py`**:
  Audita e gera o relatório completo de cobertura de questões por módulo e globalmente, calculando os percentuais de questões reais oficiais versus questões simuladas.
  ```bash
  python scripts/audit_questions.py
  ```

- **`clean_database_artifacts.py`**:
  Sanitiza o banco de dados oficial (`banco_questoes_extraidas.json`), removendo artefatos de paginação, rodapés e cabeçalhos residuais de OCR/PDF sem alterar o conteúdo técnico das questões.
  ```bash
  python scripts/clean_database_artifacts.py
  ```

- **`mass_injector.py`**:
  Motor de alta precisão que realiza a injeção em massa de questões autênticas oficiais nos guias de estudo markdown (`fontes_de_estudo/`).
  - Identifica blocos de questões simuladas.
  - Seleciona a melhor questão oficial pendente do banco com base no `target_file` e `target_section`.
  - Preserva *ipsis litteris* o enunciado e as alternativas.
  - Gera blocos de comentários analíticos detalhados e gabarito oficial.
  - Atualiza o status no `banco_questoes_extraidas.json` para `"injetada"`.
  ```bash
  # Modo simulação (sem alterações nos arquivos)
  python scripts/mass_injector.py --dry-run

  # Execução definitiva
  python scripts/mass_injector.py
  ```
