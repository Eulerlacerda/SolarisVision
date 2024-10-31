import tkinter as tk
from database import db_connection

def abrir_estoque():
    estoque_janela = tk.Toplevel()
    estoque_janela.title("Gestão de Estoque")

    # Interface para listar e atualizar itens de estoque
    tk.Label(estoque_janela, text="Código do Produto").grid(row=0, column=0)
    tk.Label(estoque_janela, text="Quantidade").grid(row=0, column=1)
    tk.Label(estoque_janela, text="Modelo").grid(row=0, column=2)
    tk.Label(estoque_janela, text="Fabricante").grid(row=0, column=3)
    tk.Label(estoque_janela, text="Preço").grid(row=0, column=4)

    # Funções de manipulação de dados
    def adicionar_produto(codigo, quantidade, modelo, fabricante, preco):
        query = '''INSERT INTO estoque (codigo, quantidade, modelo, fabricante, preco) VALUES (?, ?, ?, ?, ?)'''
        db_connection.executar_consulta(query, (codigo, quantidade, modelo, fabricante, preco))
        # Atualizar interface para refletir as mudanças

    # Outros elementos de UI para interação com estoque
