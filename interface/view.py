import tkinter as tk
from tkinter import ttk

class UsuarioView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gerenciador de Usuários")

        # Widgets para adicionar um usuário
        self.nome_label = tk.Label(self, text="Nome:")
        self.nome_label.pack()
        self.nome_entry = tk.Entry(self)
        self.nome_entry.pack()

        self.data_de_nascimento_label = tk.Label(self, text="Data de Nascimento:")
        self.data_de_nascimento_label.pack()
        self.data_de_nascimento_entry = tk.Entry(self)
        self.data_de_nascimento_entry.pack()

        self.senha_label = tk.Label(self, text="Senha:")
        self.senha_label.pack()
        self.senha_entry = tk.Entry(self, show="*")
        self.senha_entry.pack()

        self.adicionar_button = tk.Button(self, text="Adicionar")
        self.adicionar_button.pack()

        # Widget para mostrar a lista de usuários
        self.lista_usuarios = ttk.Treeview(self, columns=("id", "nome", "data_de_nascimento", "senha"), show='headings')
        self.lista_usuarios.heading("id", text="ID")
        self.lista_usuarios.heading("nome", text="Nome")
        self.lista_usuarios.heading("data_de_nascimento", text="Data de Nascimento")
        self.lista_usuarios.heading("senha", text="Senha")
        self.lista_usuarios.pack()

    def get_nome(self):
        return self.nome_entry.get()

    def get_data_de_nascimento(self):
        return self.data_de_nascimento_entry.get()

    def get_senha(self):
        return self.senha_entry.get()

    def adicionar_usuario_lista(self, usuario):
        self.lista_usuarios.insert('', 'end', values=usuario)

    def limpar_campos(self):
        self.nome_entry.delete(0, tk.END)
        self.data_de_nascimento_entry.delete(0, tk.END)
        self.senha_entry.delete(0, tk.END)

    def mostrar_aviso_entrada(self):
        tk.messagebox.showwarning("Aviso", "Todos os campos devem ser preenchidos corretamente.")
