# -*- coding: utf-8 -*-
with open("scratch/enrich_module_11.py", "r", encoding="utf-8") as f:
    text = f.read()

# Fix File 11/02 anchors
p1_old = 'p1 = "### 1.2 O Modelo de Informação e Árvore DIT"'
p1_new = 'p1 = "### 1.2 O Protocolo LDAP: Portas Padrão e Arquitetura TCP/IP"'
text = text.replace(p1_old, p1_new)

p2_old = 'p2 = "## 3. Componentes Estruturais e Operações de Diretório"'
p2_new = 'p2 = "### 2.2 Tipos e Escopos de Grupos no AD DS"'
text = text.replace(p2_old, p2_new)

p3_old = 'p3 = "### 3.2 Tipos de Grupos e seus Escopos"'
p3_new = 'p3 = "### 3.2 Sites, Sub-redes e Otimização de Replicação Física"'
text = text.replace(p3_old, p3_new)

p4_old = 'p4 = "### 3.3 Funções FSMO (Flexible Single Master Operations)"'
p4_new = 'p4 = "### 3.3 Catálogo Global (Global Catalog - GC)"'
text = text.replace(p4_old, p4_new)

with open("scratch/enrich_module_11.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Patch applied to enrich_module_11.py!")
