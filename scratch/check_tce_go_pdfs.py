import os
import pypdf

tce_pdfs = [f for f in os.listdir('provas_pci') if 'tce-go' in f.lower() and f.endswith('.pdf') and 'gabarito' not in f.lower()]
print(f"Total de PDFs de provas do TCE-GO: {len(tce_pdfs)}")
for pdf in tce_pdfs:
    print(f"- {pdf}")

