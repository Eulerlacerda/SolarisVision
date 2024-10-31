import tkinter as tk
from database import db_connection
from utils import notifications

def abrir_fidelidade():
    fidelidade_janela = tk.Toplevel()
    fidelidade_janela.title("Sistema de Fidelidade e Marketing")

    def registrar_fidelidade(cliente, pontos):
        query = '''UPDATE clientes SET pontos = pontos + ? WHERE nome = ?'''
        db_connection.executar_consulta(query, (pontos, cliente))

    def enviar_promo(cliente):
        mensagem = "Promoção exclusiva para você!"
        notifications.enviar_mensagem(cliente, mensagem)

    # UI para gerenciar fidelidade e enviar promoções
