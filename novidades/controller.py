# controller.py
from view import AplicativoDeJogosView
from model import Model
from datetime import datetime

class AplicativoDeJogosController:
    def __init__(self, root):
        self.model = Model()
        self.view = AplicativoDeJogosView(root)
        self.atualizar_horario()
        self.view.configurar_eventos(self)  # Configura os eventos da view

    def atualizar_horario(self):
        """Atualiza o horário atual no rótulo."""
        now = datetime.now()
        horario = now.strftime("%H:%M:%S")
        self.view.atualizar_horario(horario)
        self.view.root.after(1000, self.atualizar_horario)

    def adicionar_usuario(self, nome, data_de_nascimento, senha):
        """Adiciona um novo usuário ao banco de dados."""
        sucesso = self.model.inserir_usuario(nome, data_de_nascimento, senha)
        if sucesso:
            self.view.mostrar_mensagem("Usuário registrado com sucesso!")
        else:
            self.view.mostrar_mensagem("Erro ao registrar usuário. O nome pode já estar em uso.")

    def listar_usuarios(self):
        """Obtém a lista de usuários e atualiza a View."""
        usuarios = self.model.selecionar_usuarios()
        self.view.exibir_usuarios(usuarios)

    def fechar_conexao(self):
        """Fecha a conexão com o banco de dados."""
        self.model.fechar_conexao()
