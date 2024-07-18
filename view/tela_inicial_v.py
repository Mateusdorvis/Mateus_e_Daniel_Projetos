import tkinter as tk

class TelaInicialView(tk.Frame):
        def __init__(self, parent):
            super().__init__(parent)
            self.create_widgets()

        def create_widgets(self):
              
            self.titulo_label = tk.Label(self, text="Bem Vindo ao Aplicativo de Jogos!", font=("Arial",12),pady=15)
            self.titulo_label.grid(row=0, column=1, columnspan=3)
        
            self.login_button = tk.Button(self, text="Login",height=1,width=20,pady=20,background="lightgrey")
            self.login_button.grid(row=1, column=1, columnspan=3)

            self.n_login_button = tk.Button(self, text="Permanecer desconectado",height=1,pady=20,background="lightgrey")
            self.n_login_button.grid(row=2, column=1, columnspan=3)

            self.sair_button = tk.Button(self, text="Sair",height=1,pady=20,background="lightgrey")
            self.sair_button.grid(row=3, column=1, columnspan=3)
        

            self.grid_rowconfigure(3, weight=1)
            self.grid_columnconfigure(3, weight=1)
