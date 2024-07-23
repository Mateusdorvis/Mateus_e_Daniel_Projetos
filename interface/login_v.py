import tkinter as tk
from tkinter import messagebox
from login_c import LoginController

class LoginApp:
    def __init__(self, root):
        self.controller = LoginController()
        self.root = root
        self.root.title("Login App")

        # Configurações do Grid
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)
        root.rowconfigure(0, weight=1)
        root.rowconfigure(1, weight=1)
        root.rowconfigure(2, weight=1)
        root.rowconfigure(3, weight=1)
        root.rowconfigure(4, weight=1)

        # Widgets
        self.label_nome = tk.Label(root, text="Nome:")
        self.label_nome.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.entry_nome = tk.Entry(root)
        self.entry_nome.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.label_data = tk.Label(root, text="Data de Nascimento:")
        self.label_data.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.entry_data = tk.Entry(root)
        self.entry_data.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.label_senha = tk.Label(root, text="Senha:")
        self.label_senha.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        self.entry_senha = tk.Entry(root, show='*')
        self.entry_senha.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        # Botões
        self.btn_login = tk.Button(root, text="Login", command=self.login)
        self.btn_login.grid(row=3, column=0, padx=10, pady=10, sticky="e")

        self.btn_register = tk.Button(root, text="Register", command=self.register)
        self.btn_register.grid(row=3, column=1, padx=10, pady=10, sticky="w")

    def login(self):
        nome = self.entry_nome.get()
        data_de_nascimento = self.entry_data.get()
        senha = self.entry_senha.get()
        result = self.controller.login(nome, data_de_nascimento, senha)
        messagebox.showinfo("Informação", result)

    def register(self):
        nome = self.entry_nome.get()
        data_de_nascimento = self.entry_data.get()
        senha = self.entry_senha.get()
        result = self.controller.register(nome, data_de_nascimento, senha)
        messagebox.showinfo("Informação", result)

    def close(self):
        self.controller.close()
        self.root.destroy()

# Criação da interface gráfica
if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
