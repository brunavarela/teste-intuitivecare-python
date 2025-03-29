import os

import pandas as pd
import psycopg2
from db_connection import criar_conexao, fechar_conexao


def importar_dados_trimestrais():
    conn = criar_conexao()
    if not conn:
        print("❌ Falha na conexão com o banco de dados.")
        return
    
    cur = conn.cursor()
    
    arquivos_trimestrais = {
        "demonstrativo_contabil_2023": [
            "./downloads/1T2023.csv",
            "./downloads/2T2023.csv",
            "./downloads/3T2023.csv",
            "./downloads/4T2023.csv"
        ],
        "demonstrativo_contabil_2024": [
            "./downloads/1T2024.csv",
            "./downloads/2T2024.csv",
            "./downloads/3T2024.csv",
            "./downloads/4T2024.csv"
        ]
    }

    def corrigir_colunas(df):
        """Remove espaços e aspas extras dos nomes das colunas."""
        df.columns = df.columns.str.strip().str.replace('"', '')
        return df

    for tabela, arquivos in arquivos_trimestrais.items():
        for arquivo in arquivos:
            if not os.path.exists(arquivo):
                print(f"❌ Arquivo não encontrado: {arquivo}")
                continue
            
            print(f"📥 Importando {arquivo} para {tabela}...")
            
            # Carrega o arquivo CSV
            df = pd.read_csv(arquivo, delimiter=';', encoding='latin1')
            df = corrigir_colunas(df)

            # Cria a lista de valores para inserção
            valores = [
                (row['DATA'], row['REG_ANS'], row['CD_CONTA_CONTABIL'], row['DESCRICAO'], row['VL_SALDO_INICIAL'], row['VL_SALDO_FINAL'])
                for _, row in df.iterrows()
            ]

            try:
                # Inserir todas as linhas de uma vez usando executemany
                cur.executemany(
                    f"""INSERT INTO {tabela} (data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
                        VALUES (%s, %s, %s, %s, %s, %s)
                    """, 
                    valores
                )
                conn.commit()
                print(f"✅ {arquivo} importado com sucesso!")
            except Exception as e:
                conn.rollback()
                print(f"❌ Erro ao importar {arquivo}: {e}")

    cur.close()
    conn.close()
    print("✅ Importação concluída!")


if __name__ == "__main__":
    importar_dados_trimestrais()
