import tkinter as tk
from tkinter import ttk
from model.usuario_m import UsuarioModel
from view.login_v import LoginView
from tkinter import messagebox

class LoginController:
    def __init__(self, view:LoginView, model:UsuarioModel):
        self.view = view
        self.model = model
        self.view.login_button.config(command=self.login)
        
    def login(self):
        usuario = self.view.usuario_entry.get()
        senha = self.view.senha_entry.get()
        if hasattr(self, 'controller'):
            self.verifica_login(usuario, senha)
    
    def verifica_login(self, usuario, senha):
        if self.model.authenticate(usuario, senha):
            messagebox.showinfo("Login", "Login bem-sucedido!")
        else:
            messagebox.showerror("Login", "Usuário ou senha incorretos.")
     