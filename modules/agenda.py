import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from database import db_connection
from utils import notifications

# Variável global para controlar o tamanho das entradas
LARGURA_ENTRADA = 15  # Tamanho inicial menor

def ajustar_tamanho_entradas(entries, novo_tamanho):
    global LARGURA_ENTRADA
    LARGURA_ENTRADA = novo_tamanho
    for entry in entries.values():
        entry.config(width=LARGURA_ENTRADA)

def abrir_agenda():
    agenda_janela = tk.Toplevel()
    agenda_janela.title("Agenda de Consultas")
    agenda_janela.geometry("500x800")
    agenda_janela.configure(bg='white')

    # Frame para a logo
    logo_frame = tk.Frame(agenda_janela, bg='white')
    logo_frame.pack(pady=20)

    # Carregar e exibir a logo
    try:
        logo_path = "C:/Users/Euler/Documents/logo.png"
        logo_image = Image.open(logo_path)
        logo_image = logo_image.resize((400, 350), Image.LANCZOS)
        logo_photo = ImageTk.PhotoImage(logo_image)
        
        logo_label = tk.Label(logo_frame, image=logo_photo, bg='white')
        logo_label.image = logo_photo
        logo_label.pack()
    except Exception as e:
        print(f"Erro ao carregar a logo: {e}")

    # Frame para conter as entradas e labels
    frame = tk.Frame(agenda_janela, bg='white')
    frame.pack(padx=(10, 30), pady=10, fill=tk.BOTH, expand=True)  # Aumentado o padding direito

    # Cabeçalho e Entradas de dados
    headers = ["Data", "Horário", "Nome", "Contato", "CPF", "Rua", "Nº", "Bairro", "Cidade", "UF", "E-mail"]
    entries = {}

    for i, header in enumerate(headers):
        tk.Label(frame, text=header, anchor="w", bg='white').grid(row=i, column=0, sticky="w", pady=2)
        entry = tk.Entry(frame, width=LARGURA_ENTRADA)
        entry.grid(row=i, column=1, sticky="ew", pady=2, padx=(0, 10))  # Adicionado padding à direita
        entries[header] = entry

    # Configurar a coluna 1 (das entradas) para expandir
    frame.grid_columnconfigure(1, weight=1)

    def marcar_consulta():
        data = entries["Data"].get()
        horario = entries["Horário"].get()
        cliente = entries["Nome"].get()
        contato = entries["Contato"].get()

        if not all([data, horario, cliente, contato]):
            messagebox.showwarning("Dados Inválidos", "Todos os campos devem ser preenchidos!")
            return
        
        query = '''INSERT INTO consultas (data, horario, cliente_id) 
                   VALUES (?, ?, (SELECT id FROM clientes WHERE nome = ? LIMIT 1))'''
        db_connection.executar_consulta(query, (data, horario, cliente))
        
        notifications.enviar_lembrete(contato, f"Consulta agendada para {data} às {horario}")

        messagebox.showinfo("Sucesso", "Consulta agendada com sucesso!")
        agenda_janela.destroy()

    def pesquisar_agendamento():
        # Implemente a lógica de pesquisa aqui
        # Por exemplo, você pode abrir uma nova janela para a pesquisa
        # ou usar os valores das entradas para realizar a pesquisa
        messagebox.showinfo("Pesquisa", "Função de pesquisa de agendamento será implementada aqui.")

    # Frame para os botões
    botoes_frame = tk.Frame(frame, bg='white')
    botoes_frame.grid(row=len(headers), column=0, columnspan=2, pady=10)

    # Botão para Agendar consulta
    marcar_btn = tk.Button(botoes_frame, text="Agendar Consulta", command=marcar_consulta)
    marcar_btn.pack(side=tk.LEFT, padx=5)

    # Botão para pesquisar agendamento
    pesquisar_btn = tk.Button(botoes_frame, text="Pesquisar Agendamento", command=pesquisar_agendamento)
    pesquisar_btn.pack(side=tk.LEFT, padx=5)

    # Função para aumentar o tamanho das entradas
    def aumentar_entradas():
        ajustar_tamanho_entradas(entries, LARGURA_ENTRADA + 5)

    
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sistema Principal")
    
    # Botão para abrir a agenda
    abrir_agenda_btn = tk.Button(root, text="Abrir Agenda", command=abrir_agenda)
    abrir_agenda_btn.pack(pady=20)
    
    root.mainloop()