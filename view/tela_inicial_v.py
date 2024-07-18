import tkinter as tk

class TelaInicialView(tk.Frame):
        def __init__(self, parent):
            super().__init__(parent)
            self.create_widgets()

        def create_widgets(self):
              
            self.titulo_label = tk.Label(self, text="Bem Vindo ao Aplicativo de Jogos!", font=("Arial",12),pady=15)
            self.titulo_label.grid(row=0, column=1, columnspan=3)
        
            self.desconectado_button = tk.Button(self, text="Permanecer desconectado",height=1,width=20,pady=20,background="lightgrey")
            self.desconectado_button.grid(row=1, column=1, columnspan=3)

            self.grid_rowconfigure(3, weight=1)
            self.grid_columnconfigure(3, weight=1)
