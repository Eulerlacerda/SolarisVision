import sqlite3
import os

def criar_banco_dados():
    db_path = os.path.join(os.path.dirname(__file__), "solaris_vision.db")
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Tabela de estoque
        cursor.execute('''CREATE TABLE IF NOT EXISTS estoque (
                            id INTEGER PRIMARY KEY,
                            codigo TEXT NOT NULL,
                            quantidade INTEGER NOT NULL,
                            modelo TEXT,
                            fabricante TEXT,
                            preco REAL NOT NULL
                          )''')
        
        # Tabela de clientes
        cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                            id INTEGER PRIMARY KEY,
                            nome TEXT NOT NULL,
                            telefone TEXT,
                            endereco TEXT,
                            cpf TEXT UNIQUE,
                            rg TEXT UNIQUE,
                            cidade TEXT,
                            estado TEXT
                          )''')

        # Tabela de consultas
        cursor.execute('''CREATE TABLE IF NOT EXISTS consultas (
                            id INTEGER PRIMARY KEY,
                            data TEXT NOT NULL,
                            horario TEXT NOT NULL,
                            cliente_id INTEGER,
                            FOREIGN KEY (cliente_id) REFERENCES clientes (id)
                          )''')

        # Tabela de tratamentos
        cursor.execute('''CREATE TABLE IF NOT EXISTS tratamentos (
                            id INTEGER PRIMARY KEY,
                            descricao TEXT NOT NULL,
                            data_inicio TEXT,
                            data_fim TEXT,
                            cliente_id INTEGER,
                            FOREIGN KEY (cliente_id) REFERENCES clientes (id)
                          )''')

        # Tabela de notificações
        cursor.execute('''CREATE TABLE IF NOT EXISTS notificacoes (
                            id INTEGER PRIMARY KEY,
                            mensagem TEXT NOT NULL,
                            data_envio TEXT,
                            cliente_id INTEGER,
                            FOREIGN KEY (cliente_id) REFERENCES clientes (id)
                          )''')

        # Adicione mais tabelas conforme a necessidade

        conn.commit()
    except sqlite3.Error as e:
        print(f"Erro ao criar o banco de dados: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    criar_banco_dados()
