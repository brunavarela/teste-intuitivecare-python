
# Etapa 1 - Web Scraping

## Objetivo

Nesta etapa, o objetivo foi realizar um web scraping na página da ANS para baixar os arquivos **Anexo I** e **Anexo II** em formato PDF e compactá-los em um único arquivo ZIP.

## Estrutura de Arquivos

-   **main.py**: Código principal que realiza o scraping, baixa os arquivos PDF e os compacta em um arquivo ZIP.
    
-   **downloads/**: Pasta onde os arquivos PDF são salvos após o download.
    
-   **anexos.zip**: Arquivo ZIP contendo os PDFs baixados.

## Como Executar

1.  Instale as dependências:
    
    `pip install -r requirements.txt` 
    
2.  Execute o código:
    
    `python main.py` 
    
    O script vai buscar os links para os PDFs da página, baixar os arquivos e compactá-los em um arquivo ZIP chamado `anexos.zip`.

## Dependências

-   `requests`: Para realizar requisições HTTP e baixar os arquivos.
    
-   `beautifulsoup4`: Para fazer o parsing do HTML e extrair os links dos PDFs.
    
-   `zipfile`: Para compactar os arquivos baixados em um arquivo ZIP.
    

## Exemplo de Saída

Ao executar o código, você verá algo assim no terminal:

`Links  encontrados  para  download: ['https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf', '...'] Baixado: Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf  Baixado: Anexo_I_Rol_2021RN_465.2021_RN627L.2024.xlsx  Baixado: Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf  Arquivos  compactados  em  anexos.zip`