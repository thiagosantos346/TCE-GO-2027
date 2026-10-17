import os
import re

ROOT = os.getcwd()
dirs = [
    'fontes_de_estudo/conhecimentos_gerais',
    'fontes_de_estudo/conhecimentos_especificos_b02_ti',
    'fontes_de_estudo/conhecimentos_especificos_a01_tecnico_administrativo'
]

total_files = 0
total_questions = 0
total_mermaids = 0
issues = []
files_by_q_count = {}

for d in dirs:
    base = os.path.join(ROOT, d)
    for dp, _, fns in os.walk(base):
        for fn in sorted(fns):
            if fn.endswith('.md') and fn.lower() != 'readme.md':
                p = os.path.join(dp, fn)
                rel = os.path.relpath(p, ROOT).replace('\\', '/')
                total_files += 1
                with open(p, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Contagem de questoes
                qs = re.findall(r'^(?:#{2,4}\s+)?(?:\*\*)?Quest[ãa]o\s+(\d+)', content, re.MULTILINE | re.IGNORECASE)
                q_count = len(qs)
                total_questions += q_count
                files_by_q_count[q_count] = files_by_q_count.get(q_count, 0) + 1

                # Verificar se a contagem esta entre 10 e 15
                if q_count < 10 or q_count > 15:
                    issues.append(f"{rel}: contagem de questoes fora da meta ({q_count})")

                # Verificar sequenciamento
                nums = [int(x) for x in qs]
                expected = list(range(1, q_count + 1))
                if nums != expected:
                    issues.append(f"{rel}: sequenciamento incorreto {nums} vs {expected}")

                # Contagem de gabaritos
                gabs = re.findall(r'>\s*\*\*Gabarito:\s*([A-E])\*\*', content, re.IGNORECASE)
                if len(gabs) != q_count:
                    issues.append(f"{rel}: gabaritos ({len(gabs)}) != questoes ({q_count})")

                # Mermaids
                mm = re.findall(r'```mermaid', content)
                total_mermaids += len(mm)

print("="*65)
print("AUDITORIA GLOBAL DO PROJETO - 100% DAS PASTAS")
print("="*65)
print(f"Total de Arquivos de Conteudo Auditados: {total_files}")
print(f"Total Geral de Questoes Inline Comentadas: {total_questions}")
print(f"Total Geral de Diagramas Mermaid Preservados: {total_mermaids}")
print("\nDistribuicao de questoes por arquivo:")
for c in sorted(files_by_q_count.keys()):
    print(f"  • {files_by_q_count[c]} arquivos com {c} questoes inline")

if issues:
    print(f"\nATENCAO: {len(issues)} problemas encontrados:")
    for iss in issues:
        print("  ✖", iss)
else:
    print("\nRESULTADO DA AUDITORIA: 100% APROVADO! ZERO PROBLEMAS DETECTADOS!")
print("="*65)

