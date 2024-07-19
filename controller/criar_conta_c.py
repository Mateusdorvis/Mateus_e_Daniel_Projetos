import tkinter as tk
from tkinter import messagebox
from model.usuario_m import UsuarioModel
from view.criar_conta_v import CriarContaView

class LoginController:
    def __init__(self, view: CriarContaView, model: UsuarioModel):
        self.view = view
        self.model = model
        self.view.voltar_button.config(command=self.voltar_para_login)
        self.view.cadastrar_button.config(command=self.criar_conta)
    
    
    def criar_conta(self):
        pass

    
    def voltar_para_login(self):
        pass