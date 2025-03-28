import pdfplumber
import csv

pdf_path = '../web_scraping_ans/downloads/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf'
csv_filename = 'resultados/rol_de_procedimentos.csv'

abreviacoes = {
    'AMB': 'Ambulatorial',
    'HCO': 'Hospitalar com Obstetrícia',
    'HSO': 'Hospitalar sem Obstetrícia',
    'REF': 'Referência'
}

with pdfplumber.open(pdf_path) as pdf:
    tables = []
    print(f"Iniciando a extração das tabelas de {len(pdf.pages)} páginas.")

    for page_num, page in enumerate(pdf.pages, start=1):
        print(f"Processando página {page_num}...")
        table = page.extract_table()
        if table:  
            tables.append(table)
        else:
            print(f"Nenhuma tabela encontrada na página {page_num}.")
    print("Extração concluída.")

with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    for table in tables:
        for row in table:
            row = [abreviacoes.get(cell, cell) for cell in row]
            writer.writerow(row)

print(f"Dados salvos em {csv_filename}")