import os

import pandas as pd
import psycopg2
from db_connection import criar_conexao, fechar_conexao


def importar_dados_cadastrais():
    conn = criar_conexao()
    if not conn:
        print("❌ Falha na conexão com o banco de dados.")
        return
    
    cur = conn.cursor()
    
    operadoras_path = "./downloads/Relatorio_cadop.csv"
    
    if not os.path.exists(operadoras_path):
        print(f"❌ Arquivo não encontrado: {operadoras_path}")
        return
    
    df = pd.read_csv(operadoras_path, delimiter=';', encoding='latin1')
    print(f"✅ Dados carregados: {df.shape[0]} linhas")
    
    for _, row in df.iterrows():
        cur.execute(
            """INSERT INTO operadoras (
                registro_ans, cnpj, razao_social, nome_fantasia, modalidade, logradouro, numero,
                complemento, bairro, cidade, uf, cep, ddd, telefone, fax, endereco_eletronico, 
                representante, cargo_representante, regiao_comercializacao, data_registro_ans
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            ) ON CONFLICT (registro_ans) DO NOTHING""",
            (
                row['Registro_ANS'], row['CNPJ'], row['Razao_Social'], row['Nome_Fantasia'],
                row['Modalidade'], row['Logradouro'], row['Numero'], row['Complemento'], row['Bairro'],
                row['Cidade'], row['UF'], row['CEP'], row['DDD'], row['Telefone'], row['Fax'],
                row['Endereco_eletronico'], row['Representante'], row['Cargo_Representante'],
                row['Regiao_de_Comercializacao'], row['Data_Registro_ANS']
            )
        )
    
    conn.commit()
    cur.close()
    fechar_conexao(conn)
    print("✅ Dados cadastrais das operadoras importados com sucesso.")

if __name__ == "__main__":
    importar_dados_cadastrais()

