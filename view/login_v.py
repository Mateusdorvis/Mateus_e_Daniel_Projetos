import tkinter as tk

class LoginView(tk.Frame):
        def __init__(self, parent):
            super().__init__(parent)
            self.create_widgets()

        def create_widgets(self):
            self.label_title = tk.Label(self, text="Tela de Login", font=("Arial", 20),pady=20)
            self.label_title.grid(row=0, column=1, columnspan=3,sticky="N")
            
            self.label_usuario = tk.Label(self, text="Usuário:",font=("Arial", 15),pady=20)
            self.label_usuario.grid(row=1, column=0, columnspan=3)
            self.usuario_entry = tk.Entry(self,font=("Arial", 15))
            self.usuario_entry.grid(row=1, column=1, columnspan=3)
            
            self.label_senha = tk.Label(self, text="Senha:",font=("Arial", 15))
            self.label_senha.grid(row=2, column=0, columnspan=3)
            self.senha_entry = tk.Entry(self, font=("Arial", 15))
            self.senha_entry.grid(row=2, column=1, columnspan=3)
            
            self.login_button = tk.Button(self, text="Entrar")
            self.login_button.grid(row=3, column=2, columnspan=1)

            self.novaconta_button = tk.Button(self, text="Criar Nova Conta")
            self.novaconta_button.grid(row=3, column=3, columnspan=2)

            self.grid_rowconfigure(3, weight=1)
            self.grid_columnconfigure(3, weight=1)

        