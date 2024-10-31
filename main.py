import tkinter as tk
from PIL import Image, ImageTk  # Biblioteca para abrir e gerenciar imagens no tkinter
from modules import agenda, clientes, estoque, orcamento, vendas, fornecedores, historico, relatorios, fidelidade, personalizacao

# Funções para abrir as seções
def abrir_agenda():
    agenda.abrir_agenda()

def abrir_clientes():
    clientes.abrir_clientes()

def abrir_estoque():
    estoque.abrir_estoque()

def abrir_orcamento():
    orcamento.abrir_orcamento()

def abrir_vendas():
    vendas.abrir_vendas()

def abrir_fornecedores():
    fornecedores.abrir_fornecedores()

def abrir_historico():
    historico.abrir_historico()

def abrir_relatorios():
    relatorios.abrir_relatorios()

def abrir_fidelidade():
    fidelidade.abrir_fidelidade()

def abrir_personalizacao():
    personalizacao.abrir_personalizacao()

def abrir_notificacoes():
    print("Notificações abertas")

def abrir_reports():
    print("Reports abertos")

# Código para inicializar a interface principal
class SolarisVisionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Solaris Vision - Gerenciamento de Ótica")

        # Definir o fundo da janela como branco
        self.root.configure(bg='white')

        # Criar um Frame para os menus na parte superior
        self.menu_frame = tk.Frame(self.root, bg='white')
        self.menu_frame.pack(side=tk.TOP, fill=tk.X)

        # Criar um Frame adicional para centralizar os botões
        self.central_frame = tk.Frame(self.menu_frame, bg='white')
        self.central_frame.pack(expand=True)

        # Criar menus
        self.criar_menus()

        # Adicionar imagem no centro
        self.exibir_logo()

    def exibir_logo(self):
        # Carregar imagem
        logo_path = "C:/Users/Euler/Documents/logo.png"  # Substitua pelo caminho do arquivo da logo
        imagem_logo = Image.open(logo_path)
        imagem_logo = imagem_logo.resize((700, 600), Image.LANCZOS)  # Ajustar o tamanho da imagem

        self.logo = ImageTk.PhotoImage(imagem_logo)

        # Adicionar imagem à tela centralizada
        logo_label = tk.Label(self.root, image=self.logo, bg='white')  # Definir fundo do label como branco
        logo_label.pack(pady=100)  # Centraliza verticalmente com um espaço superior e inferior

    def criar_menus(self):
        # Lista de menus
        menus = [
            ("Agenda", abrir_agenda),
            ("Clientes", abrir_clientes),
            ("Estoque", abrir_estoque),
            ("Orçamento", abrir_orcamento),
            ("Vendas", abrir_vendas),
            ("Fornecedores", abrir_fornecedores),
            ("Histórico", abrir_historico),
            ("Relatórios", abrir_relatorios),
            ("Fidelidade", abrir_fidelidade),
            ("Personalização", abrir_personalizacao),
            ("Notificações", abrir_notificacoes),
            ("Reports", abrir_reports)
        ]

        # Criar botões para cada menu e adicioná-los ao central_frame
        for label, command in menus:
            button = tk.Button(self.central_frame, text=label, command=command, bg='white', borderwidth=1, relief='solid')
            button.pack(side=tk.LEFT, padx=5, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = SolarisVisionApp(root)
    root.mainloop()
