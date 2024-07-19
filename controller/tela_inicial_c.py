import tkinter as tk
from tkinter import ttk
from model.usuario_m import UsuarioModel
from view.tela_inicial_v import TelaInicialView

class TelaInicialController:
    def __init__(self, view:TelaInicialView, model:UsuarioModel):
        self.view = view
        self.model = model
        self.view.desconectado_button.config(command=self.abrir_tela)

    def abrir_tela(self):
        pass
