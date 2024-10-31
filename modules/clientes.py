import tkinter as tk
from database import db_connection

def abrir_clientes():
    clientes_janela = tk.Toplevel()
    clientes_janela.title("Gestão de Clientes")

    tk.Label(clientes_janela, text="Nome").grid(row=0, column=0)
    tk.Label(clientes_janela, text="Telefone").grid(row=0, column=1)
    tk.Label(clientes_janela, text="Endereço").grid(row=0, column=2)
    tk.Label(clientes_janela, text="CPF").grid(row=0, column=3)
    tk.Label(clientes_janela, text="RG").grid(row=0, column=4)
    tk.Label(clientes_janela, text="Cidade").grid(row=0, column=5)
    tk.Label(clientes_janela, text="Estado").grid(row=0, column=6)

    # Funções para adicionar e editar dados de clientes
    def cadastrar_cliente(nome, telefone, endereco, cpf, rg, cidade, estado):
        query = '''INSERT INTO clientes (nome, telefone, endereco, cpf, rg, cidade, estado) VALUES (?, ?, ?, ?, ?, ?, ?)'''
        db_connection.executar_consulta(query, (nome, telefone, endereco, cpf, rg, cidade, estado))
        # Atualizar interface com novos dados de clientes

    # Outros elementos de UI para manipulação de clientes
