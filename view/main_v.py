import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class MainView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()

    def create_widgets(self):
        self.login_button = tk.Button(self, text="Login")
        self.login_button.grid(row=0, column=0, padx=10, pady=5)

        self.n_login_button = ttk.Label(self, text="Permanecer Desconectado")
        self.n_login_button.grid(row=1, column=0, padx=10, pady=5)
    
       
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(1, weight=1)

        
    def mostrar_aviso_entrada(self):
        messagebox.showinfo("Aviso!", "Alguma das entradas não está completa! Verifique novamente!")


