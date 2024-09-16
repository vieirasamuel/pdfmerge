from pypdf import PdfWriter

def merge_pdfs(pdfs, dirname):
    merger = PdfWriter()
    for pdf in pdfs:
        merger.append(pdf)
    merger.write(f'{dirname}.pdf')
    merger.close()
