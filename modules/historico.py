import tkinter as tk
from database import db_connection

def abrir_historico():
    historico_janela = tk.Toplevel()
    historico_janela.title("Histórico de Prescrições e Pedidos")

    tk.Label(historico_janela, text="Nome do Cliente").grid(row=0, column=0)
    tk.Label(historico_janela, text="Prescrição").grid(row=0, column=1)

    def adicionar_prescricao(cliente, prescricao):
        query = '''INSERT INTO historico (cliente, prescricao) VALUES (?, ?)'''
        db_connection.executar_consulta(query, (cliente, prescricao))

    # UI para registrar o histórico
