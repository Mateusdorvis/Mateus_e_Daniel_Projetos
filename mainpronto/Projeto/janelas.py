import tkinter as tk
from tkinter import ttk

#janelas do da barra principal
class JanelaVerion:
    def __init__(self):
     self.principal = tk.Tk()
     self.principal.resizable(False, False)
     self.principal.title('Versão do aplicativo')
     self.show_informacao()
     self.principal.mainloop()
        
    
    def show_informacao(self,):
        self.label_version = tk.Label(self.principal, text='Versão do aplicativo :')
        self.label_version.grid(row=0, column=0)
        self.label_version2 = tk.Label(self.principal, text='Versão: 1.5.0')
        self.label_version2.grid(row=0, column=1)
        
class JanelaRoms:
    pass
    