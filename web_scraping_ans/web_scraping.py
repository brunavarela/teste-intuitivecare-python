import requests
import os
import zipfile
from bs4 import BeautifulSoup
import re

URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
SAVE_DIR = "downloads"

os.makedirs(SAVE_DIR, exist_ok=True)

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

pdf_links = []

for link in soup.find_all('a', href=True):
    if re.search(r'(Anexo I|Anexo II)', link.text):  
        pdf_links.append(link['href'])

print("Links encontrados para download:", pdf_links)

def download_pdf(url, filename):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        filepath = os.path.join(SAVE_DIR, filename)
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(f"Baixado: {filename}")
    else:
        print(f"Erro ao baixar {filename} com status: {response.status_code}")

for pdf_link in pdf_links:
    filename = pdf_link.split("/")[-1]
    download_pdf(pdf_link, filename)

zip_filename = 'anexos.zip'
with zipfile.ZipFile(zip_filename, "w") as zipf:
    for file in os.listdir(SAVE_DIR):
        zipf.write(os.path.join(SAVE_DIR, file), arcname=file)

print(f"Arquivos compactados em {zip_filename}")
