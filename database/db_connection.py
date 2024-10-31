import sqlite3
import os

# Defina o caminho do banco de dados
DB_PATH = 'C:/Users/Euler/Documents/SolarisVision/database/solaris_vision.db'

def conectar_db():
    """Conecta ao banco de dados SQLite e retorna a conexão."""
    try:
        # Verifica se o diretório existe, se não, cria
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
        
        conn = sqlite3.connect(DB_PATH)
        return conn
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def executar_consulta(query, parametros=None):
    """Executa uma consulta SQL no banco de dados.

    Args:
        query (str): A consulta SQL a ser executada.
        parametros (tuple, optional): Os parâmetros a serem usados na consulta.

    Returns:
        bool: True se a operação foi bem-sucedida, False caso contrário.
        result: Resultado da consulta, se aplicável.
    """
    conn = conectar_db()
    if conn is not None:
        cursor = conn.cursor()
        try:
            if parametros:
                cursor.execute(query, parametros)
            else:
                cursor.execute(query)
            
            if query.strip().upper().startswith("SELECT"):
                result = cursor.fetchall()
                conn.commit()
                print("Consulta realizada com sucesso.")
                return True, result
            else:
                conn.commit()
                print("Operação realizada com sucesso.")
                return True, None
        except sqlite3.Error as e:
            print(f"Erro ao executar a consulta: {e}")
            return False, None
        finally:
            cursor.close()
            conn.close()
    else:
        print("Não foi possível executar a consulta, pois a conexão falhou.")
        return False, None

def criar_tabela_consultas():
    """Cria a tabela de consultas se ela não existir."""
    query = """
    CREATE TABLE IF NOT EXISTS consultas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data TEXT NOT NULL,
        horario TEXT NOT NULL,
        cliente TEXT NOT NULL
    )
    """
    sucesso, _ = executar_consulta(query)
    if sucesso:
        print("Tabela 'consultas' criada ou já existente.")
    else:
        print("Erro ao criar a tabela 'consultas'.")

# Chama a função para criar a tabela quando o módulo é importado
criar_tabela_consultas()