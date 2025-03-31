from db_connection import criar_conexao, fechar_conexao


def query_analitica():
    conn = criar_conexao()
    cur = conn.cursor()
    
    queries = [
        {
            "descricao": "Top 10 operadoras com maiores despesas em eventos/sinistros no último trimestre",
            "sql": """
                SELECT o.registro_ans, o.razao_social, d.cd_conta_contabil, d.descricao, SUM(d.vl_saldo_final) as total_despesa
                FROM operadoras o
                JOIN demonstrativo_contabil_2023 d
                ON o.registro_ans = d.reg_ans
                WHERE d.descricao LIKE '%SINISTROS%'
                AND d.data BETWEEN '2024-10-01' AND '2024-12-31' 
                GROUP BY o.registro_ans, o.razao_social, d.cd_conta_contabil, d.descricao
                ORDER BY total_despesa DESC
                LIMIT 10;
            """
        },
        {
            "descricao": "Top 10 operadoras com maiores despesas em eventos/sinistros no último ano",
            "sql": """
                SELECT o.registro_ans, o.razao_social, d.cd_conta_contabil, d.descricao, SUM(d.vl_saldo_final) as total_despesa
                FROM operadoras o
                JOIN demonstrativo_contabil_2023 d
                ON o.registro_ans = d.reg_ans
                WHERE d.descricao LIKE '%SINISTROS%'
                AND d.data BETWEEN '2024-01-01' AND '2024-12-31'
                GROUP BY o.registro_ans, o.razao_social, d.cd_conta_contabil, d.descricao
                ORDER BY total_despesa DESC
                LIMIT 10;
            """
        }
    ]
    
    for query in queries:
        print(f"Executando: {query['descricao']}")
        try:
            cur.execute(query['sql']) 
            resultados = cur.fetchall()
            if resultados:
                for row in resultados:
                    print(row)
            else:
                print("❌ Nenhum resultado encontrado para esta consulta.")
        except Exception as e:
            print(f"❌ Erro ao executar a query: {e}")
    
    cur.close()  
    conn.close()
    print("Queries analíticas executadas com sucesso.")

if __name__ == "__main__":
    query_analitica()
