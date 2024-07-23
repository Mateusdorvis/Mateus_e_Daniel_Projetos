from model import UsuarioModel
from tkinter import messagebox

class LoginController:
    def __init__(self):
        self.model = UsuarioModel()

    def login(self, nome, data_de_nascimento, senha):
        if self.model.verifica_senha(nome, data_de_nascimento, senha):
            messagebox.showinfo("Informação", "Login foi realizado com sucesso!")
        else:
            messagebox.showinfo("Erro", "Credenciais inválidas, tente novamente!")

    def register(self, nome, data_de_nascimento, senha):
        if self.model.cria_usuario(nome, data_de_nascimento, senha):
            messagebox.showinfo("Informação", "Usuário foi criado com sucesso!")
        else:
            messagebox.showinfo("Erro", "Não foi possível criar o usuário, tente novamente!")

    def close(self):
        self.model.fechar_conexao()
