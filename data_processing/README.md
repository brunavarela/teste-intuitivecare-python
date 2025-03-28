
# Etapa 2 - Teste de Transformação de Dados 

## Objetivo

Esta etapa como objetivo realizar a **extração e transformação de dados** do Anexo I do "Rol de Procedimentos e Eventos em Saúde", extraído no **Teste de Web Scraping**.

## Tarefas realizadas

1.  **Extração**: Extrai os dados da tabela contida no PDF (Anexo I) do "Rol de Procedimentos e Eventos em Saúde".
    
2.  **Transformação**: Converte os dados extraídos em um arquivo **CSV**, substituindo as abreviações nas colunas por suas descrições completas.
    
3.  **Armazenamento**: O arquivo CSV resultante é salvo e pode ser utilizado para outras análises ou importação em sistemas de banco de dados.

## Como Executar
    
1.  O código principal está no arquivo `transformacao.py`. Execute-o com o seguinte 		  comando:
    
    `python transformacao.py` 
    
    O código vai gerar um arquivo `requisitos.csv` na pasta `data_processing/`, com os dados extraídos e transformados. Além disso, as mensagens de log indicarão o progresso da extração e transformação.

## Dependências

-   `requests`: Para realizar requisições HTTP e baixar os arquivos.
    
-   `beautifulsoup4`: Para fazer o parsing do HTML e extrair os links dos PDFs.
    
-   `zipfile`: Para compactar os arquivos baixados em um arquivo ZIP.
    
## Resultado Esperado

Após a execução do código, o arquivo `requisitos.csv` será gerado com as seguintes informações:

-   **Cabeçalho**: As colunas incluem `PROCEDIMENTO`, `RN (alteração)`, `VIGÊNCIA`, `OD`, entre outras.
    
-   **Transformação de Abreviações**: As abreviações como `OD` (odontológico), `AMB` (ambulatorial), etc., foram substituídas por descrições completas como `Odonto` e `Ambulatorial`.
    

### Exemplo de conteúdo do CSV:


`PROCEDIMENTO,"RN (alteração)",VIGÊNCIA,OD,Ambulatorial,Hospitalar com Obstetrícia,Hospitalar sem Obstetrícia,Referência,PAC,DUT,SUBGRUPO,GRUPO,CAPÍTULO
ACONSELHAMENTO GENÉTICO,,,,Ambulatorial,Hospitalar com Obstetrícia,Hospitalar sem Obstetrícia,Referência,,,"CONSULTAS, VISITAS HOSPITALARES OU ACOMPANHAMENTO DE PACIENTES",PROCEDIMENTOS GERAIS,PROCEDIMENTOS GERAIS
...` 

## Observações

-   **PDFs**: O código depende de arquivos PDF do Anexo I para extração. Certifique-se de ter os arquivos baixados corretamente antes de rodar o código.
    
-   **Pacotes Necessários**: Este código foi desenvolvido com as bibliotecas `PyPDF2`, `csv` e outras dependências presentes no `requirements.txt`.