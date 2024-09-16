from directory import get_cwd_dirs, get_cwd_pdfs, get_directory_name
from pdfmerge import merge_pdfs
from pdfgenerator import generate_pdf

print('Iniciando busca pelos diretórios...')
print('Diretórios encontrados:')
dirs = get_cwd_dirs()

for dir in dirs:
    print(dir)
    dirname = get_directory_name(dir)
    generate_pdf(dir)
    pdfs = get_cwd_pdfs(dir)
    merge_pdfs(pdfs, dirname)

print('Execução finalizada.')
input()