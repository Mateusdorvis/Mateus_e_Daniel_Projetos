import tkinter as tk

class NovoUsuarioView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        self.titulo = tk.Label(self, text="Registrar Novo Usuário", font=("Arial", 16))
        self.titulo.pack(pady=10)
        
        self.label_usuario = tk.Label(self, text="Nome de Usuário:")
        self.label_usuario.pack(pady=5)
        self.usuario_entry = tk.Entry(self)
        self.usuario_entry.pack(pady=5)
        
        self.label_senha = tk.Label(self, text="Senha antiga:")
        self.label_senha.pack(pady=5)
        self.senha_entry = tk.Entry(self)
        self.senha_entry.pack(pady=5)
        
        self.confirma_senha = tk.Label(self, text="Confirmar Senha:")
        self.confirma_senha.pack(pady=5)
        self.confirm_password_entry = tk.Entry(self)
        self.confirm_password_entry.pack(pady=5)
        
        self.register_button = tk.Button(self, text="Registrar")
        self.register_button.pack(pady=20)
