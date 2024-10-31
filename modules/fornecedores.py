import tkinter as tk
from database import db_connection

def abrir_fornecedores():
    fornecedores_janela = tk.Toplevel()
    fornecedores_janela.title("Integração com Fornecedores")

    tk.Label(fornecedores_janela, text="Nome do Fornecedor").grid(row=0, column=0)
    tk.Label(fornecedores_janela, text="Status do Pedido").grid(row=0, column=1)

    def registrar_fornecedor(nome, status):
        query = '''INSERT INTO fornecedores (nome, status) VALUES (?, ?)'''
        db_connection.executar_consulta(query, (nome, status))

    # UI para registrar e atualizar fornecedores
