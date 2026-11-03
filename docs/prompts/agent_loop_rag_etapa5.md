# Protocolo de Execução em Loop do Agente — Etapa 5 (RAG 1:1)

Este documento define a especificação normativa e operacional do **Agent Loop** para a realização da **ETAPA 5 (Consulta Semântica Dupla e Injeção RAG 1:1)** nos cadernos de estudo do projeto TCE-GO 2027.

---

## 🎯 Objetivo
Substituir cirurgicamente questões autorais simuladas por questões reais oficiais de concursos anteriores (preferência: FGV, FCC, Cebraspe pós-2022) que possuam **100% de aderência conceitual na mesma disciplina e área técnica de TI**, preservando integralmente as questões simuladas quando não houver correspondente real exato.

---

## 🔄 Protocolo de Execução do Loop (Pasta por Pasta / Caderno por Caderno)

Para cada pasta de módulo dentro de `docs/conhecimentos_especificos_b02_ti/` e para cada caderno (`.md`) da pasta:

### PASSO 1: Leitura e Mapeamento do Caderno Atual
1. Fazer o parsing de todos os blocos de questões presentes no caderno (`### Teste XXX` ao `### Teste YYY`).
2. Mapear o conceito técnico nuclear e a habilidade avaliada em cada teste.

### PASSO 2: Consulta Vetorial com Filtro Rígido de TI (Anti-Contaminação)
1. Realizar as consultas sobre `data/banco_vetorial_rag.db` e `data/banco_questoes_v3.json`.
2. **REGRA DE OURO INVIOLÁVEL:** Nunca confiar cegamente na etiqueta legada `target_materia`. É obrigatório filtrar por cargos legítimos de Tecnologia da Informação:
   ```sql
   WHERE (
       lower(cargo) LIKE '%tecnologia%' OR 
       lower(cargo) LIKE '%informática%' OR 
       lower(cargo) LIKE '%sistemas%' OR 
       lower(cargo) LIKE '%computação%' OR 
       lower(cargo) LIKE '%infraestrutura%' OR 
       lower(cargo) LIKE '%desenvolvimento%' OR
       lower(cargo) LIKE '%dados%' OR
       lower(cargo) LIKE '%ti%'
   )
   ```
3. Confrontar semanticamente o enunciado da questão simulada com os enunciados retornados da área técnica.
4. **Critério de Decisão:**
   - **`TROCA`:** Identificada questão real de TI que aborda rigorosamente o mesmo tópico/objeto técnico.
   - **`FICA`:** Se não houver questão real no banco ou se as existentes forem de tópicos divergentes/irrelevantes, a questão simulada autoral permanece **100% intacta**.

### PASSO 3: Geração do Relatório no Formato Padrão e Registro Persistente
1. Montar a estrutura padronizada contendo:
   - **Cabeçalho:** Arquivo alvo, escopo temático e total de questões.
   - **Tabela de Diagnóstico e Confronto Questão a Questão:** Todos os testes listados individualmente com colunas `[Teste | Conceito no Caderno | Busca no Banco Vetorial RAG | Avaliação Semântica e Decisão (TROCA ou FICA)]`.
   - **Resumo Executivo:** Seções "O que SAI" e "O que FICA".
   - **Seção "O que ENTRA":** Texto integral de cada questão real proposta para substituição (cabeçalho oficial, enunciado completo, alternativas e comentário detalhado com gabarito).
2. Atualizar o arquivo histórico persistente `docs/relatorio_auditoria_cadernos_rag.md` com a nova seção e o sumário.

### PASSO 4: Ponto de Parada e Interação com o Usuário
1. Apresentar o relatório formatado no chat.
2. **PARAR** a chamada de ferramentas e aguardar a validação explícita do usuário (`"sim"`, `"aprovo"` ou ajustes).

### PASSO 5: Pós-Aprovação (Aplicação, Commit & Push)
Assim que o usuário responder confirmando:
1. Aplicar a substituição física no arquivo `.md` do caderno correspondente.
2. Marcar as questões utilizadas no `data/banco_questoes_v3.json` com `status_integracao: "integrada_caderno_XX"`.
3. Atualizar o status da seção no `docs/relatorio_auditoria_cadernos_rag.md` para `"Concluído e sincronizado"`.
4. Executar:
   ```powershell
   git add <caminho_do_caderno> data/banco_questoes_v3.json docs/relatorio_auditoria_cadernos_rag.md
   git commit -m "feat(<materia>): injecao validada 1:1 de questoes reais no caderno XX ..."
   git push origin main
   ```
5. Avançar imediatamente para o próximo caderno da pasta ou para o próximo módulo temático, reiniciando o loop no PASSO 1.

