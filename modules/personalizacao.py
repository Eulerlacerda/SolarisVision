import tkinter as tk

def abrir_personalizacao():
    personalizacao_janela = tk.Toplevel()
    personalizacao_janela.title("Personalização Virtual de Óculos")

    tk.Label(personalizacao_janela, text="Experimente Virtualmente").pack()
    # Interface para selecionar armações e visualizar de maneira simulada
