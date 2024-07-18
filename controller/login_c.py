import tkinter as tk
from tkinter import ttk
from model.usuario_m import UsuarioModel
from view.login_v import LoginView

class LoginController:
    def __init__(self, view:LoginView, model:UsuarioModel):
        self.view = view
        self.model = model

    def login_usuario(self):
        pass