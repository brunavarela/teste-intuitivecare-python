from db_connection import criar_conexao, fechar_conexao


def criar_tabelas():
    conn = criar_conexao()
    if conn:
        cur = conn.cursor()

        tabelas_sql = [
            """
            CREATE TABLE IF NOT EXISTS demonstrativo_contabil_2023 (
                id SERIAL PRIMARY KEY,
                data DATE,
                reg_ans VARCHAR(20),
                cd_conta_contabil VARCHAR(50),
                descricao TEXT,
                vl_saldo_inicial NUMERIC(15,2),
                vl_saldo_final NUMERIC(15,2),
                UNIQUE (reg_ans, data, cd_conta_contabil)  -- Adicionando UNIQUE
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS demonstrativo_contabil_2024 (
                id SERIAL PRIMARY KEY,
                data DATE,
                reg_ans VARCHAR(20),
                cd_conta_contabil VARCHAR(50),
                descricao TEXT,
                vl_saldo_inicial NUMERIC(15,2),
                vl_saldo_final NUMERIC(15,2),
                UNIQUE (reg_ans, data, cd_conta_contabil)  -- Adicionando UNIQUE
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS operadoras (
                id SERIAL PRIMARY KEY,
                registro_ans VARCHAR(20) UNIQUE,
                cnpj VARCHAR(20),
                razao_social TEXT,
                nome_fantasia TEXT,
                modalidade TEXT,
                logradouro TEXT,
                numero VARCHAR(50),
                complemento TEXT,
                bairro TEXT,
                cidade TEXT,
                uf VARCHAR(2),
                cep VARCHAR(10),
                ddd VARCHAR(5),
                telefone VARCHAR(20),
                fax VARCHAR(20),
                endereco_eletronico TEXT,
                representante TEXT,
                cargo_representante TEXT,
                regiao_comercializacao TEXT,
                data_registro_ans DATE
            );
            """
        ]

        # Criar tabelas
        for sql in tabelas_sql:
            cur.execute(sql)

        # Criar índice único para a combinação das colunas reg_ans, data e cd_conta_contabil
        cur.execute(
            """
            CREATE UNIQUE INDEX IF NOT EXISTS unique_reg_ans_data_conta ON demonstrativo_contabil_2023 (reg_ans, data, cd_conta_contabil);
            """
        )

        cur.execute(
            """
            CREATE UNIQUE INDEX IF NOT EXISTS unique_reg_ans_data_conta ON demonstrativo_contabil_2024 (reg_ans, data, cd_conta_contabil);
            """
        )

        conn.commit()
        cur.close()
        fechar_conexao(conn)
        print("✅ Tabelas e índices criados com sucesso.")

# Chame a função de criação de tabelas
criar_tabelas()
