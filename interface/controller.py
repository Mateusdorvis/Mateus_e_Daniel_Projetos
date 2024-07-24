import tkinter as tk
from tkinter import ttk
from model import UsuarioModel

class UsuarioController:
    def __init__(self, view, model: UsuarioModel):
        self.view = view
        self.model = model
        self.view.adicionar_button.config(command=self.adicionar_usuario)
        self.carregar_usuarios()

    def adicionar_usuario(self):
        nome = self.view.get_nome()
        data_de_nascimento = self.view.get_data_de_nascimento()
        senha = self.view.get_senha()

        if nome and data_de_nascimento and senha:
            if self.model.inserir_usuario(nome, data_de_nascimento, senha):
                self.view.adicionar_usuario_lista((None, nome, data_de_nascimento, senha))
                self.view.limpar_campos()
            else:
                self.view.mostrar_aviso_entrada()
        else:
            self.view.mostrar_aviso_entrada()

    def carregar_usuarios(self):
        usuarios = self.model.selecionar_usuarios()
        for usuario in usuarios:
            self.view.adicionar_usuario_lista(usuario)
