import tkinter as tk
from database import db_connection

def abrir_orcamento():
    orcamento_janela = tk.Toplevel()
    orcamento_janela.title("Configuração de Orçamentos")

    tk.Label(orcamento_janela, text="Descrição").grid(row=0, column=0)
    tk.Label(orcamento_janela, text="Preço").grid(row=0, column=1)

    def criar_orcamento(descricao, preco):
        query = '''INSERT INTO orcamentos (descricao, preco) VALUES (?, ?)'''
        db_connection.executar_consulta(query, (descricao, preco))

    # UI para entrada de descrição e preço
