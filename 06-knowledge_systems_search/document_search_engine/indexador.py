import os
from whoosh.fields import Schema, TEXT, ID
from whoosh.index import create_in
from pdfquery import PDFQuery
import shutil

schema = Schema(title=ID(stored=True), content=TEXT)

if os.path.exists("indexdir"):
    shutil.rmtree("indexdir")
os.mkdir("indexdir")

ix = create_in("indexdir", schema)
writer = ix.writer()

pdf_folder = "pdfs"

for filename in os.listdir(pdf_folder):
    if filename.endswith(".pdf"):
        path = os.path.join(pdf_folder, filename)
        try:
            pdf = PDFQuery(path)
            pdf.load()
            text_elements = pdf.pq('LTTextLineHorizontal')
            full_text = "\n".join([t.text for t in text_elements if t.text])

            writer.add_document(title=filename, content=full_text)
            print(f"Indexado: {filename}")
        except Exception as e:
            print(f"Error procesando {filename}: {e}")

writer.commit()
print("Indexación completa.")
