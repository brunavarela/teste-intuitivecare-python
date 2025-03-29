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

operadoras_url = "https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/Relatorio_cadop.csv"
download_folder = "downloads"

download_file(operadoras_url, download_folder)

print("✅ Download e extração do arquivo de operadoras concluídos!")
