import os

import psycopg2
from dotenv import load_dotenv
from psycopg2 import OperationalError

load_dotenv()

db_config = {
    'host': os.getenv('DB_HOST'),   
    'database': os.getenv('DB_DATABASE'), 
    'user': os.getenv('DB_USER'), 
    'password': os.getenv('DB_PASSWORD'),
    'port': os.getenv('DB_PORT'),
    'options': os.getenv('DB_OPTIONS')
}

def criar_conexao():
    try:
        conn = psycopg2.connect(**db_config)
        print("✅ Conexão com o banco estabelecida com sucesso.")
        return conn
    except OperationalError as e:
        print(f"❌ Erro ao conectar ao banco de dados: {e}")
        return None

def fechar_conexao(conn):
    if conn:
        conn.close()
        print("❌ Conexão com o banco fechada.")
