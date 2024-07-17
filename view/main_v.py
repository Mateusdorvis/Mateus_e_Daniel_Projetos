import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class MainView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()

    def create_widgets(self):
        self.button_login = ttk.Button(self, text="Login")
        self.button_login.grid(row=0, column=0, padx=10, pady=5)

        self.button_login = ttk.Button(self, text="Permanecer desconectado")
        self.button_login.grid(row=1, column=0, padx=10, pady=5)
       
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(1, weight=1)

        
    def mostrar_aviso_entrada(self):
        messagebox.showinfo("Aviso!", "Alguma das entradas não está completa! Verifique novamente!")

    def get_nome(self):
        return self.nome_entry.get()

    def get_idade(self):
        return self.idade_entry.get()
    

    def adicionar_usuario_lista(self, usuario):
        self.usuarios_listbox.insert(tk.END, f"id {usuario[0]} | {usuario[1]} ({usuario[2]} anos)")