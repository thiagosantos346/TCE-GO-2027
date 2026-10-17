# -*- coding: utf-8 -*-
import os
import re

ROOT = r"C:\Users\thiag\OneDrive\Desktop\src\TCE-GO-2027"

def inject_questions_into_file(rel_path, injections):
    """
    injections: list of dicts:
      {
        "target_sec": str,
        "theory_supplement": str (optional, to guarantee theoretical sufficiency),
        "question_text": str
      }
    """
    file_path = os.path.join(ROOT, rel_path.replace("/", os.sep))
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    orig_q = re.findall(r"### Questão (\d+)", content)
    if len(orig_q) > 5:
        print(f"{os.path.basename(file_path)} already has {len(orig_q)} questions. Skipping.")
        return
    print(f"\nProcessing {os.path.basename(file_path)}: currently has {len(orig_q)} questions {orig_q}")

    for item in injections:
        target_sec = item["target_sec"]
        supp = item.get("theory_supplement", "")
        q_text = item["question_text"]

        pos = content.find(target_sec)
        actual_len = len(target_sec)
        if pos == -1:
            # Tentar encontrar por número da seção (ex: "### 3.3 ") ou sem backticks
            sec_num_match = re.search(r"###\s+(\d+\.\d+)", target_sec)
            if sec_num_match:
                sec_num = sec_num_match.group(1)
                pattern = rf"\n(###\s+{re.escape(sec_num)}[^\n]+)"
                m = re.search(pattern, content)
                if m:
                    pos = m.start(1)
                    actual_len = len(m.group(1))
            if pos == -1:
                raise ValueError(f"Could not find target section '{target_sec}' in {file_path}")

        # Encontra o fim da subseção teórica (próximo ## ou ### ou fim do arquivo)
        # Procuramos a partir de pos + actual_len
        rest = content[pos + actual_len:]
        # Padrão para achar o próximo cabeçalho de seção (mas não ### Questão)
        match = re.search(r"\n(?=## |\n### (?!Questão)|$)", rest)
        if match:
            insert_idx = pos + actual_len + match.start()
        else:
            insert_idx = len(content)

        block = ""
        if supp:
            block += "\n\n" + supp.strip()
        block += "\n\n" + q_text.strip() + "\n\n---\n"

        content = content[:insert_idx] + block + content[insert_idx:]

    final_q = re.findall(r"### Questão (\d+)", content)
    print(f"Result for {os.path.basename(file_path)}: now has {len(final_q)} questions: {final_q}")

    # Checagens de integridade
    for i in range(1, 6):
        if f"{i:02d}" not in final_q:
            raise AssertionError(f"Questão {i:02d} was lost in {file_path}!")
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Saved {os.path.basename(file_path)} successfully!")

print("Enricher ready.")
