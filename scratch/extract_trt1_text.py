import pypdf

reader = pypdf.PdfReader('provas_pci/analista-judiciario-tecnologia-da-informacao-trt-1-fcc-2014___prova_a01_tipo_001.pdf')
text = reader.pages[0].extract_text() + "\n" + reader.pages[1].extract_text()
print(text[:2500])

