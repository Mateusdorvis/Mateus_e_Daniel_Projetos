import tkinter as tk
class CriarContaView(tk.Frame):
    def __init__(self, parent, controller):
            super().__init__(parent)
            self.create_widgets()

    def create_widgets(self):
            
            self.label_title = tk.Label(self, text="Criar Conta")
            self.label_title.grid(row=0, column=0, columnspan=2, pady=10)

            self.label_usuario = tk.Label(self, text="Usuário:")
            self.label_usuario.grid(row=1, column=0, padx=5, pady=5, sticky="e")

            self.usuario_entry = tk.Entry(self)
            self.usuario_entry.grid(row=1, column=1, padx=5, pady=5)

            self.label_senha = tk.Label(self, text="Senha:")
            self.label_senha.grid(row=2, column=0, padx=5, pady=5, sticky="e")

            self.senha_entry = tk.Entry(self)
            self.senha_entry.grid(row=2, column=1, padx=5, pady=5)

            self.cadastrar_button = tk.Button(self, text="Cadastrar", command=self.criar_conta)
            self.cadastrar_button.grid(row=3, column=0, columnspan=2, pady=10)
            self.voltar_button = tk.Button(self, text="Voltar", command=self.voltar_para_login)
            self.voltar_button.grid(row=4, column=0, columnspan=2, pady=10)

            self.grid_rowconfigure(0, weight=1)
            self.grid_columnconfigure(1, weight=1)

    