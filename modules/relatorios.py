import tkinter as tk
from utils import reports

def abrir_relatorios():
    relatorios_janela = tk.Toplevel()
    relatorios_janela.title("Relatórios de Vendas e Estoque")

    tk.Button(relatorios_janela, text="Gerar Relatório de Vendas", command=reports.gerar_relatorio_vendas).pack()
    tk.Button(relatorios_janela, text="Gerar Relatório de Estoque", command=reports.gerar_relatorio_estoque).pack()
