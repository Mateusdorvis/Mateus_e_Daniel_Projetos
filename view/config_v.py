import tkinter as tk
from tkinter import ttk
from datetime import datetime

class ConfigView(tk.Frame):
        def __init__(self, parent):
            super().__init__(parent)
            self.create_widgets()

        def create_widgets(self):
              
            self.titulo_label = tk.Label(self, text="Horário: ", font=("Arial",24))
            self.titulo_label.grid(row=0, column=2, columnspan=1)

            self.time_label = ttk.Label(self, font=("Arial", 24))
            self.time_label.grid(row=0, column=3, columnspan=1)


            
        
        # Atualiza o relógio
            self.update_time()
            self.grid_rowconfigure(3, weight=1)
            self.grid_columnconfigure(3, weight=1)
            
        def update_time(self):
            # Obtém o horário atual
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            
            # Atualiza o rótulo com o horário
            self.time_label.config(text=current_time)
            
            # Atualiza o horário a cada 1000 ms (1 segundo)
            self.after(1000, self.update_time)