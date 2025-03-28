import psycopg2
from flask import Flask, jsonify, request

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        dbname="postgres", 
        user="postgres", 
        password="senha123", 
        host="localhost", 
        port="5433",
        options="-c client_encoding=UTF8"
    )
    return conn

@app.route('/buscar_operadoras', methods=['GET'])
def buscar_operadoras():
    termo_busca = request.args.get('termo')  
    
    if not termo_busca:
        return jsonify({"error": "Termo de busca não fornecido"}), 400
    
    conn = get_db_connection()
    cur = conn.cursor()
    
    query = "SELECT id, razao_social, cnpj, registro_ans FROM operadoras WHERE razao_social ILIKE %s LIMIT 10;"
    cur.execute(query, ('%' + termo_busca + '%',))
    
    resultados = cur.fetchall()
    
    def corrigir_encoding(texto):
        if texto:
            try:
                return texto.encode('latin1').decode('utf-8', errors='replace') 
            except Exception as e:
                print(f"Erro ao corrigir encoding: {e}")
                return texto  
        return texto

    operadoras = [{
        'id': row[0], 
        'razao_social': corrigir_encoding(row[1]),  
        'cnpj': row[2], 
        'registro_ans': row[3]
    } for row in resultados]

    cur.close()
    conn.close()
    
    return jsonify(operadoras)

if __name__ == '__main__':
    app.run(debug=True)
