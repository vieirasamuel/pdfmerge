import csv
from fpdf import FPDF
import os

def generate_pdf(cwd):
    pdf = FPDF()
    pdf.add_page('landscape')
    pdf.set_font('Arial', '', 10)
    pdf.set_auto_page_break(auto=True, margin=15)

    with open(os.path.join(cwd, 'relatorio.csv'), mode='r', newline='', encoding='utf8') as csv_file:
        csv_reader = csv.reader(csv_file)
        with pdf.table() as table:
            for line in csv_reader:
                row = table.row()
                for cell in line:
                    row.cell(cell)

    pdf.output(os.path.join(cwd, 'relatorio.pdf'), 'F')
