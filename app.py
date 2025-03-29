import psycopg2
from flask import Flask, jsonify, request
from flask_cors import CORS

from database.scripts.db_connection import criar_conexao

app = Flask(__name__)
CORS(app)

def corrigir_encoding(texto):
    """Corrige o encoding do texto para evitar problemas com caracteres especiais."""
    if texto:
        try:
            return texto.encode('latin1').decode('utf-8', errors='replace')
        except Exception as e:
            print(f"Erro ao corrigir encoding: {e}")
            return texto
    return texto

@app.route('/buscar_operadoras', methods=['GET'])
def buscar_operadoras():
    """Busca operadoras no banco de dados usando o termo fornecido na query string."""
    termo_busca = request.args.get('termo')  
    
    if not termo_busca:
        return jsonify({"error": "Termo de busca não fornecido"}), 400
    
    conn = criar_conexao() 
    if not conn:
        return jsonify({"error": "Não foi possível conectar ao banco de dados"}), 500
    
    try:
        cur = conn.cursor()
        query = "SELECT id, razao_social, cnpj, registro_ans FROM operadoras WHERE razao_social ILIKE %s LIMIT 10;"
        cur.execute(query, ('%' + termo_busca + '%',))
        resultados = cur.fetchall()
        
        operadoras = [{
            'id': row[0], 
            'razao_social': corrigir_encoding(row[1]),  
            'cnpj': row[2], 
            'registro_ans': row[3]
        } for row in resultados]

        return jsonify(operadoras)
    except Exception as e:
        print(f"Erro ao buscar operadoras: {e}")
        return jsonify({"error": "Erro ao buscar operadoras"}), 500
    finally:
        cur.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
