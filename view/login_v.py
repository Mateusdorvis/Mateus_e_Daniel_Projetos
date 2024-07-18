import tkinter as tk

class LoginView(tk.Frame):
        def __init__(self, parent):
            super().__init__(parent)
            self.create_widgets()

        def create_widgets(self):
            self.tela_login_titulo = tk.Label(self, text="Tela de Login", font=("Arial", 12))
            self.tela_login_titulo.grid(row=0, column=1, columnspan=3)
            # Adicione widgets de login aqui