import tkinter as tk

class LoginView(tk.Frame):
        def __init__(self, parent):
            super().__init__(parent)
            self.create_widgets()

        def create_widgets(self):
            self.label_title = tk.Label(self, text="Tela de Login", font=("Arial", 16))
            self.label_title.pack(pady=10)
            
            self.label_usuario = tk.Label(self, text="Usuário:")
            self.label_usuario.pack(pady=5)
            self.usuario_entry = tk.Entry(self)
            self.usuario_entry.pack(pady=5)
            
            self.label_senha = tk.Label(self, text="Senha:")
            self.label_senha.pack(pady=5)
            self.senha_entry = tk.Entry(self, show="*")
            self.senha_entry.pack(pady=5)
            
            self.login_button = tk.Button(self, text="Login")
            self.login_button.pack(pady=20)

        