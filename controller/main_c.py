import tkinter as tk
from tkinter import ttk
from model.usuario_m import UsuarioModel
from view.main_v import MainView
class UsuarioController:
    def __init__(self, view:MainView, model:UsuarioModel):
        self.view = view
        self.model = model
        self.view.login_button.config(command=self.adicionar_usuario)
        self.view.n_login_button.config(command=self.adicionar_usuario)
        self.carregar_usuarios()

    def adicionar_usuario(self):
        nome = self.view.get_nome()
        idade = self.view.get_idade()
        if nome and idade.isdigit():
            self.model.inserir_usuario(nome, int(idade))
            self.view.adicionar_usuario_lista((None,nome, idade))
            self.view.nome_entry.delete(0, tk.END)
            self.view.idade_entry.delete(0, tk.END)
        else:
            self.view.mostrar_aviso_entrada()

    def carregar_usuarios(self):
        usuarios = self.model.selecionar_usuarios()
        for usuario in usuarios:
            self.view.adicionar_usuario_lista(usuario)