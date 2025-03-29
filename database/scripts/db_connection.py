import psycopg2
from psycopg2 import OperationalError

db_config = {
    'host': 'localhost',   
    'database': 'postgres', 
    'user': 'postgres', 
    'password': 'senha123',
    'port': 5433,
    'options': '-c client_encoding=UTF8'
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
