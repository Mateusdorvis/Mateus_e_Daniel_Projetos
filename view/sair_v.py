import tkinter as tk

class SairView(tk.Frame):
        def __init__(self, parent):
            super().__init__(parent)
            self.create_widgets()

        def create_widgets(self):
              
            self.titulo_label = tk.Label(self, text="Você tem certeza que gostaria de sair? Se sim aperte o botão", font=("Arial Black",8),pady=15,foreground="#d01b2f")
            self.titulo_label.grid(row=0, column=1, columnspan=3)
        
            self.sair_button = tk.Button(self, text="Sair",height=1,width=20,pady=20,background="lightgrey")
            self.sair_button.grid(row=1, column=1, columnspan=3)

            self.grid_rowconfigure(3, weight=1)
            self.grid_columnconfigure(3, weight=1)