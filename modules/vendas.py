import tkinter as tk
from database import db_connection

def abrir_vendas():
    vendas_janela = tk.Toplevel()
    vendas_janela.title("Sistema de Vendas e Faturamento")

    tk.Label(vendas_janela, text="Produto").grid(row=0, column=0)
    tk.Label(vendas_janela, text="Quantidade").grid(row=0, column=1)
    tk.Label(vendas_janela, text="Forma de Pagamento").grid(row=0, column=2)

    def registrar_venda(produto, quantidade, pagamento):
        query = '''INSERT INTO vendas (produto, quantidade, pagamento) VALUES (?, ?, ?)'''
        db_connection.executar_consulta(query, (produto, quantidade, pagamento))

    # UI para registrar a venda e integrar com o sistema de faturamento
