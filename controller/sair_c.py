import tkinter as tk
from tkinter import ttk
from model.usuario_m import UsuarioModel
from view.sair_v import SairView

class SairController:
    def __init__(self, view:SairView, model:UsuarioModel, root:tk.Tk):
        self.view = view
        self.model = model
        self.view.sair_button.config(command=quit)
        self.root =root

    def quit(self):
        self.root.destroy()
