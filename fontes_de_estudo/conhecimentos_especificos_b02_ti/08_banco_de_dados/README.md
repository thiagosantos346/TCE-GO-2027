# Plano de Estudos & Fontes Teóricas: Conhecimentos Específicos TI

> **Cargo:** B02 – Técnico de Controle Externo – Especialidade: Tecnologia da Informação  
> **Matéria:** Banco de Dados  
> **Banca Referência:** Fundação Carlos Chagas (FCC)  
> **Status Geral:** 🟡 Em mapeamento de fontes teóricas

---

## 📋 Visão Geral da Ementa Oficial

> *"Modelagem de dados: modelo entidade-relacionamento, normalização e desnormalização. Linguagem SQL; álgebra relacional; transações e propriedades ACID. Índices e otimização de consultas. Procedures, triggers e views. Bancos relacionais: administração e otimização de PostgreSQL e Oracle Database. Bancos de dados NoSQL: modelos orientados a documentos, chave-valor, famílias de colunas (wide-column) e grafos; características, casos de uso e conceitos gerais; tecnologias como MongoDB e Redis. Noções de bancos de dados vetoriais aplicados à IA (embeddings). Replicação, backup e recuperação; alta disponibilidade. Segurança e governança de dados."*

---

## 🗂️ Estrutura Hierárquica dos Tópicos

A matéria foi dividida em 6 módulos temáticos modulares que abrangem desde os modelos conceituais relacionais clássicos até as tecnologias NoSQL e bancos vetoriais modernos:

| # | Módulo / Tópico Principal | Arquivo Markdown | Itens Cobertos do Edital | Status |
|---|---------------------------|------------------|--------------------------|:------:|
| 01 | [Modelagem de Dados, MER e Normalização](./01_modelagem_de_dados_mer_e_normalizacao.md) | `01_modelagem_de_dados_mer_e_normalizacao.md` | MER, Diagrama ER; Álgebra Relacional; Formas Normais (1ª, 2ª, 3ª FN, BCNF) e Desnormalização | ⚪ Aguardando Fontes |
| 02 | [Linguagem SQL e Objetos de Banco](./02_linguagem_sql_ddl_dml_dql_tcl_e_dcl.md) | `02_linguagem_sql_ddl_dml_dql_tcl_e_dcl.md` | DDL, DML, DQL (Joins, CTEs, Window Functions); Views, Procedures, Functions e Triggers | ⚪ Aguardando Fontes |
| 03 | [Transações, Propriedades ACID e Concorrência](./03_transacoes_propriedades_acid_e_concorrencia.md) | `03_transacoes_propriedades_acid_e_concorrencia.md` | ACID; Níveis de Isolamento ANSI; Fenômenos de anomalia; Bloqueios (2PL), MVCC e Deadlocks | ⚪ Aguardando Fontes |
| 04 | [Índices, Otimização, PostgreSQL e Oracle Database](./04_indices_otimizacao_postgresql_e_oracle.md) | `04_indices_otimizacao_postgresql_e_oracle.md` | B-Tree, Hash, Bitmap; Planos de Execução (EXPLAIN); Administração de PostgreSQL e Oracle | ⚪ Aguardando Fontes |
| 05 | [Bancos de Dados NoSQL e Bancos Vetoriais (IA)](./05_bancos_nosql_e_bancos_vetoriais.md) | `05_bancos_nosql_e_bancos_vetoriais.md` | Teorema CAP/BASE; Modelos NoSQL (MongoDB, Redis, Wide-Column, Grafos); Bancos Vetoriais (Embeddings/HNSW) | ⚪ Aguardando Fontes |
| 06 | [Replicação, Alta Disponibilidade, Backup e Segurança](./06_replicacao_alta_disponibilidade_backup_e_seguranca.md) | `06_replicacao_alta_disponibilidade_backup_e_seguranca.md` | Replicação e Failover; Backup e PITR (RPO/RTO); Segurança, Criptografia (TDE) e Governança | ⚪ Aguardando Fontes |

---

## 🎯 Próximos Passos
1. Coletar documentações técnicas oficiais de PostgreSQL 16+ e Oracle Database 19c/23c.
2. Formular tabelas comparativas de operadores da Álgebra Relacional vs. SQL.
3. Reunir questões clássicas e recentes da FCC de bancos relacionais e NoSQL.

