import csv
import os
import zipfile

import pdfplumber

pdf_path = '../web_scraping_ans/downloads/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf'
csv_filename = 'resultados/rol_de_procedimentos.csv'

abreviacoes = {
    'AMB': 'Seg. Ambulatorial',
    'OD': 'Seg. Odontológica',
    'VIGNCIA': 'VIGÊNCIA'
}

def corrigir_encoding(texto):
    if texto:
        try:
            return texto.encode('latin1').decode('utf-8', errors='ignore')
        except Exception as e:
            print(f"Erro ao corrigir encoding: {e}")
            return texto 
    return texto

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
            row = [corrigir_encoding(cell) for cell in row]  
            row = [abreviacoes.get(cell, cell) for cell in row]  
            writer.writerow(row)

print(f"Dados salvos em {csv_filename}")


def compactar_csv():
    zip_filename = f'Teste_Bruna.zip' 
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        zipf.write(csv_filename, os.path.basename(csv_filename))
    print(f"Arquivo compactado em {zip_filename}")

compactar_csv()
