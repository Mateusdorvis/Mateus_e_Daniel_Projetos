import tkinter as tk
from tkinter import messagebox
from model.usuario_m import UsuarioModel
from view.login_v import LoginView

class LoginController:
    def __init__(self, view: LoginView, model: UsuarioModel):
        self.view = view
        self.model = model
        self.view.login_button.config(command=self.login)
        
    def login(self):
        usuario = self.view.usuario_entry.get()
        senha = self.view.senha_entry.get()
        self.verifica_login(usuario, senha)
    
    def verifica_login(self, usuario, senha):
        if self.model.verifica_senha(usuario, senha):
            messagebox.showinfo("Login", "Login bem-sucedido!")
        else:
            messagebox.showerror("Login", "Usuário ou senha incorretos.")

     