import os
import zipfile

import requests


def download_file(url, dest_folder):
    """Baixa um arquivo e salva na pasta de destino."""
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    
    filename = os.path.join(dest_folder, url.split('/')[-1])
    
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
        print(f'📥 Baixado: {filename}')
        return filename
    else:
        print(f'❌ Falha ao baixar: {url}')
        return None

def extract_zip(zip_path, extract_to):
    """Extrai um arquivo ZIP."""
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        print(f'📂 Arquivo extraído: {zip_path}')
    except zipfile.BadZipFile:
        print(f'❌ Erro ao extrair: {zip_path}')

base_url_2023 = "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2023/"
base_url_2024 = "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2024/"
operadoras_url = "https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/Relatorio_cadop.csv"

arquivos_zip = [
    ("1T2023.zip", base_url_2023),
    ("2T2023.zip", base_url_2023),
    ("3T2023.zip", base_url_2023),
    ("4T2023.zip", base_url_2023),
    ("1T2024.zip", base_url_2024),
    ("2T2024.zip", base_url_2024), 
    ("3T2024.zip", base_url_2024),  
    ("4T2024.zip", base_url_2024), 
]

download_folder = "downloads"

for arquivo, url_base in arquivos_zip:
    zip_path = download_file(url_base + arquivo, download_folder)
    if zip_path:
        extract_zip(zip_path, download_folder)

download_file(operadoras_url, download_folder)

print("✅ Downloads concluídos!")
