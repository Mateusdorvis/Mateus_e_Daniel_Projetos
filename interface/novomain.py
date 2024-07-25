import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from imagens import load_images
from botoes_e_labels import entrada_do_mouse, saida_do_mouse, cria_button_download, cria_label_jogo, cria_label_subtitulo, cria_label_titulo
from model import UsuarioModel

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicativo de Jogos")
        self.root.geometry("700x700")
        self.root.resizable(True, True)  # Permitir redimensionamento
        self.usuario_model = UsuarioModel()  # Instancia o modelo
        self.setup()
        self.create_widgets()
        self.create_menu()

        # Inicializa variáveis de janela e usuário
        self.login_window = None
        self.favorito_window = None
        self.info_window = None
        self.cadastro_window = None  # Adiciona a variável para a janela de cadastro
        self.usuario_logado = None

        self.root.protocol("WM_DELETE_WINDOW", self.fechar_app)

    def setup(self):
        self.root.bind("<F11>", self.tela_cheia)
        self.root.bind("<Escape>", self.desativ_tela_cheia)
        self.images = load_images()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # Menu Configurações
        menu_configuracoes = tk.Menu(menubar, tearoff=0)
        menu_configuracoes.add_command(label="Tela", command=self.abrir_janela_info)
        menu_configuracoes.add_command(label="Sair", command=self.fechar_app)
        menubar.add_cascade(label="Configurações", menu=menu_configuracoes)

        # Menu Conta
        menu_conta = tk.Menu(menubar, tearoff=0)
        menu_conta.add_command(label="Favoritos", command=self.abrir_janela_favoritos)
        menu_conta.add_command(label="Login", command=self.abrir_janela_login)
        menubar.add_cascade(label="Conta", menu=menu_conta)

    def create_widgets(self):

        frame = tk.Frame(self.root, padx=10, pady=10)
        frame.pack(fill=tk.BOTH, expand=True)

        # Configura o Canvas e as barras de rolagem
        self.canvas = tk.Canvas(frame, background="#607848")
        self.scroll_x = tk.Scrollbar(frame, orient="horizontal", command=self.canvas.xview)
        self.scroll_y = tk.Scrollbar(frame, orient="vertical", command=self.canvas.yview)

        self.canvas.configure(xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)

        # Configura a posição do Canvas e das barras de rolagem
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.scroll_x.grid(row=1, column=0, sticky="ew")
        self.scroll_y.grid(row=0, column=1, sticky="ns")

        # Cria um frame dentro do canvas para acomodar o conteúdo
        self.frame_principal = tk.Frame(self.canvas, background="#607848")
        self.canvas.create_window((0, 0), window=self.frame_principal, anchor="nw")

        # Atualiza a região de rolagem quando o frame principal é redimensionado
        self.frame_principal.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.create_header()
        self.create_game_sections()

        # Configura a expansão do grid
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

    def create_header(self):
        self.label_titulo1 = cria_label_titulo(self.frame_principal, "Aplicativo de Jogos", 0, 0, 5)
        self.time_label = tk.Label(self.frame_principal, font=("Arial", 10), background="#cdcfb7")
        self.time_label.grid(row=0, column=4, padx=10, pady=10, sticky="e")
        self.time_label.bind("<Enter>", entrada_do_mouse)
        self.time_label.bind("<Leave>", saida_do_mouse)
        self.update_time()

    def update_time(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_date = now.strftime("%A, %d %B %Y")
        self.time_label.config(text=f"{current_date}\n{current_time}")
        self.root.after(1000, self.update_time)

    def create_game_sections(self):
        # Jogos em Destaque
        label_subtitulo_destaques = cria_label_subtitulo(self.frame_principal, "Jogos em Destaque", 0, 0, 5, 5)

        frame_destaques = tk.Frame(self.frame_principal, background="#789048")
        frame_destaques.grid(row=1, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")

        # Super Mario Bros.
        label1 = cria_label_jogo(frame_destaques, "Super Mario World", self.images[0], 0, 0, 5, 5)
        self.criar_button_favoritos(frame_destaques, "Super Mario World", 1, 0)
        button_download1 = cria_button_download(frame_destaques, 2, 0, 5, 5)

        # Kingdom Rush
        label2 = cria_label_jogo(frame_destaques, "Kingdom Rush", self.images[1], 0, 1, 5, 5)
        self.criar_button_favoritos(frame_destaques, "Kingdom Rush", 1, 1)
        button_download2 = cria_button_download(frame_destaques, 2, 1, 5, 5)

        # CS:GO
        label3 = cria_label_jogo(frame_destaques, "CS:GO", self.images[2], 0, 2, 5, 5)
        self.criar_button_favoritos(frame_destaques, "CS:GO", 1, 2)
        button_download3 = cria_button_download(frame_destaques, 2, 2, 5, 5)

        # Bloons TD 6
        label4 = cria_label_jogo(frame_destaques, "Bloons TD 6", self.images[3], 0, 3, 5, 5)
        self.criar_button_favoritos(frame_destaques, "Bloons TD 6", 1, 3)
        button_download4 = cria_button_download(frame_destaques, 2, 3, 5, 5)

        # Metal Slug 3
        label10 = cria_label_jogo(frame_destaques, "Metal Slug 3", self.images[9], 0, 4, 5, 5)
        self.criar_button_favoritos(frame_destaques, "Metal Slug 3", 1, 4)
        button_download10 = cria_button_download(frame_destaques, 2, 4, 5, 5)

        # Jogos Retrô
        label_subtitulo_plataforma = cria_label_subtitulo(self.frame_principal, "Jogos Retrô", 2, 0, 5, 5)

        frame_plataforma = tk.Frame(self.frame_principal, background="#789048")
        frame_plataforma.grid(row=3, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")

        # Pacman
        label5 = cria_label_jogo(frame_plataforma, "Pacman", self.images[4], 0, 0, 5, 5)
        self.criar_button_favoritos(frame_plataforma, "Pacman", 1, 0)
        button_download5 = cria_button_download(frame_plataforma, 2, 0, 5, 5)

        # Donkey Kong
        label6 = cria_label_jogo(frame_plataforma, "Donkey Kong Country", self.images[5], 0, 1, 5, 5)
        self.criar_button_favoritos(frame_plataforma, "Donkey Kong Country", 1, 1)
        button_download6 = cria_button_download(frame_plataforma, 2, 1, 5, 5)

        # Tetris
        label7 = cria_label_jogo(frame_plataforma, "Tetris", self.images[6], 0, 2, 5, 5)
        self.criar_button_favoritos(frame_plataforma, "Tetris", 1, 2)
        button_download7 = cria_button_download(frame_plataforma, 2, 2, 5, 5)

        # Contra
        label8 = cria_label_jogo(frame_plataforma, "Contra", self.images[7], 0, 3, 5, 5)
        self.criar_button_favoritos(frame_plataforma, "Contra", 1, 3)
        button_download8 = cria_button_download(frame_plataforma, 2, 3, 5, 5)

        # Streets of Rage
        label9 = cria_label_jogo(frame_plataforma, "Sonic", self.images[8], 0, 4, 5, 5)
        self.criar_button_favoritos(frame_plataforma, "Sonic", 1, 4)
        button_download9 = cria_button_download(frame_plataforma, 2, 4, 5, 5)

        # Jogos FPS
        label_subtitulo_fps = cria_label_subtitulo(self.frame_principal, "Jogos FPS", 4, 0, 5, 5)

        frame_fps = tk.Frame(self.frame_principal, background="#789048")
        frame_fps.grid(row=5, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")


        # ARK
        label11 = cria_label_jogo(frame_fps, "ARK: Survival Ascendant", self.images[10], 0, 0, 5, 5)
        self.criar_button_favoritos(frame_fps,"ARK: Survival Ascendant", 1, 0)
        button_download11 = cria_button_download(frame_fps, 2, 0, 5, 5)

        # Apex Legends
        label12 = cria_label_jogo(frame_fps, "Apex Legends", self.images[11], 0, 1, 5, 5)
        self.criar_button_favoritos(frame_fps,"Apex Legends", 1, 1)
        button_download12 = cria_button_download(frame_fps, 2, 1, 5, 5)

        # DayZ
        label13 = cria_label_jogo(frame_fps, "DayZ", self.images[12], 0, 2, 5, 5)
        self.criar_button_favoritos(frame_fps,"DayZ", 1, 2)
        button_download13 = cria_button_download(frame_fps, 2, 2, 5, 5)

        # Team Fortress 2
        label14 = cria_label_jogo(frame_fps, "Team Fortress 2", self.images[13], 0, 3, 5, 5)
        self.criar_button_favoritos(frame_fps,"Team Fortress 2", 1, 3)
        button_download14 = cria_button_download(frame_fps, 2, 3, 5, 5)

        # PUBG
        label15 = cria_label_jogo(frame_fps, "PUBG", self.images[14], 0, 4, 5, 5)
        self.criar_button_favoritos(frame_fps,"PUBG", 1, 4)
        button_download15 = cria_button_download(frame_fps, 2, 4, 5, 5)

    def criar_button_favoritos(self,parent_frame, jogo, row, column):
        button = tk.Button(parent_frame, text="Favoritar",background="#cdcfb7", command=lambda: self.adicionar_favorito(jogo))
        button.grid(row=row, column=column, padx=5, pady=5)
    

    def adicionar_favorito(self, jogo):
        if not self.usuario_logado:
            messagebox.showwarning("Erro", "Nenhum usuário logado.")
            return
        
        if self.usuario_model.adicionar_favorito(self.usuario_logado, jogo):
            messagebox.showinfo("Favorito", f"{jogo} adicionado aos favoritos.")
            self.atualizar_favoritos()
        else:
            messagebox.showinfo("Favorito", "O jogo já está na lista de favoritos.")
    def abrir_janela_favoritos(self):
        if not self.usuario_logado:
            messagebox.showwarning("Erro", "Nenhum usuário logado.")
            return

        # Verifique se a janela já existe e está aberta
        if hasattr(self, 'favorito_window') and self.favorito_window and self.favorito_window.winfo_exists():
            self.favorito_window.lift()
            self.favorito_window.focus()
            return

        # Crie a janela `Toplevel`
        self.favorito_window = tk.Toplevel(self.root)
        self.favorito_window.title("Favoritos")
        self.favorito_window.geometry("300x400")
        self.favorito_window.resizable(False, False)

        frame_favorito = tk.Frame(self.favorito_window, background="#789048")
        frame_favorito.pack(fill="both", expand=True)

        favorito_label = tk.Label(frame_favorito, text="Meus Favoritos", font=("Arial", 12), background="#cdcfb7")
        favorito_label.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="n")

        frame_lista_botao = tk.Frame(frame_favorito, background="#607848")
        frame_lista_botao.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Crie a listbox como um atributo do objeto principal
        self.listbox_favoritos = tk.Listbox(frame_lista_botao, background="#cdcfb7", selectmode=tk.SINGLE)
        self.listbox_favoritos.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.botao_remover_favorito = tk.Button(frame_lista_botao, text="Remover Favorito", command=self.remover_favorito)
        self.botao_remover_favorito.grid(row=1, column=0, padx=10, pady=(5, 10), sticky="n")

        frame_favorito.grid_rowconfigure(1, weight=1)
        frame_favorito.grid_columnconfigure(0, weight=1)
        frame_lista_botao.grid_rowconfigure(0, weight=1)
        frame_lista_botao.grid_columnconfigure(0, weight=1)

        self.atualizar_favoritos()

        self.favorito_window.protocol("WM_DELETE_WINDOW", self.fechar_janela_favoritos)





    def remover_favorito(self):
        if not self.usuario_logado:
            messagebox.showwarning("Erro", "Nenhum usuário logado.")
            return

        if not hasattr(self, 'listbox_favoritos') or not self.listbox_favoritos.winfo_exists():
            messagebox.showwarning("Erro", "A Listbox de favoritos não está disponível.")
            return

        selecionado = self.listbox_favoritos.curselection()
        if not selecionado:
            messagebox.showwarning("Erro", "Nenhum item selecionado.")
            return

        index = selecionado[0]
        item = self.listbox_favoritos.get(index)
        if self.usuario_model.remover_favorito(self.usuario_logado, item):
            messagebox.showinfo("Remover Favorito", f"{item} removido dos favoritos.")
            self.atualizar_favoritos()  # Atualiza a lista de favoritos após a remoção
        else:
            messagebox.showerror("Erro", "Erro ao remover o jogo dos favoritos.")





    def atualizar_favoritos(self):
        if hasattr(self, 'favorito_window') and self.favorito_window and self.favorito_window.winfo_exists():
            if hasattr(self, 'listbox_favoritos') and self.listbox_favoritos.winfo_exists():
                self.listbox_favoritos.delete(0, tk.END)  # Limpa a lista existente
                favoritos = self.usuario_model.obter_favoritos(self.usuario_logado)
                for fav in favoritos:
                    self.listbox_favoritos.insert(tk.END, fav)

    def fechar_janela_favoritos(self):
        if self.favorito_window:
            self.favorito_window.destroy()
            self.favorito_window = None

    def abrir_janela_info(self):
        # Verifica se a janela 'info_window' existe e está visível
        if self.info_window and self.info_window.winfo_exists():
            self.info_window.lift()
            self.info_window.focus()
            return

        # Cria a janela 'info_window' se não existir
        self.info_window = tk.Toplevel(root)
        self.info_window.title("Info")
        self.info_window.geometry("300x300")
        self.info_window.resizable(False, False)

        info_frame = tk.Frame(self.info_window)
        info_frame.pack(fill="both", expand=True)

        info_label = tk.Label(info_frame, text="Informações da Tela", font=("Arial Black", 15))
        info_label.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="n")

        info_label2 = tk.Label(info_frame, text="Tela <F11> Preenche a Tela \n    <ESC> Diminui a Tela", font=("Arial Black", 10))
        info_label2.grid(row=1, column=0, padx=10, pady=(10, 5), sticky="nw")

        info_button = tk.Button(info_frame, text="Voltar", font=("Arial Black", 15), background="#cdcfb7", command=self.info_window.destroy)
        info_button.grid(row=2, column=0, padx=10, pady=(10, 5), sticky="n")

        info_button.bind("<Enter>", entrada_do_mouse)
        info_button.bind("<Leave>", saida_do_mouse)

        info_frame.grid_rowconfigure(1, weight=1)
        info_frame.grid_columnconfigure(0, weight=1)

    def fechar_janela_info(self):
        if self.info_window:
            self.info_window.destroy()
            self.info_window = None

    def abrir_janela_login(self):
        if self.esta_logado():
            messagebox.showwarning("Aviso", "Você já está logado.")
            return

        if not self.login_window:
            self.login_window = tk.Toplevel(self.root)
            self.login_window.title("Login")
            self.login_window.geometry("300x300")  # Ajustado para acomodar o botão de cadastro
            self.login_window.resizable(False, False)

            tk.Label(self.login_window, text="Login", font=("Arial", 12)).pack(pady=10)

            tk.Label(self.login_window, text="Usuário:").pack(pady=5)
            self.entrada_usuario = tk.Entry(self.login_window)
            self.entrada_usuario.pack(pady=5)

            tk.Label(self.login_window, text="Senha:").pack(pady=5)
            self.entrada_senha = tk.Entry(self.login_window, show="*")
            self.entrada_senha.pack(pady=5)

            # Organize os botões com um frame
            frame_botoes = tk.Frame(self.login_window)
            frame_botoes.pack(pady=10)

            tk.Button(frame_botoes, text="Entrar", command=self.login).pack(side=tk.LEFT, padx=5)
            tk.Button(frame_botoes, text="Cadastrar", command=self.abrir_janela_cadastro).pack(side=tk.LEFT, padx=5)

            self.login_window.protocol("WM_DELETE_WINDOW", self.fechar_janela_login)
        else:
            self.login_window.lift()

    def abrir_janela_cadastro(self):
        if not self.cadastro_window:
            self.cadastro_window = tk.Toplevel(self.root)
            self.cadastro_window.title("Cadastro")
            self.cadastro_window.geometry("300x250")
            self.cadastro_window.resizable(False, False)

            tk.Label(self.cadastro_window, text="Cadastro", font=("Arial", 12)).pack(pady=10)

            tk.Label(self.cadastro_window, text="Usuário:").pack(pady=5)
            self.entrada_usuario_cadastro = tk.Entry(self.cadastro_window)
            self.entrada_usuario_cadastro.pack(pady=5)

            tk.Label(self.cadastro_window, text="Senha:").pack(pady=5)
            self.entrada_senha_cadastro = tk.Entry(self.cadastro_window, show="*")
            self.entrada_senha_cadastro.pack(pady=5)

            tk.Button(self.cadastro_window, text="Cadastrar", command=self.cadastrar_usuario).pack(pady=10)

            self.cadastro_window.protocol("WM_DELETE_WINDOW", self.fechar_janela_cadastro)
        else:
            self.cadastro_window.lift()
    
    def cadastrar_usuario(self):
        usuario = self.entrada_usuario_cadastro.get()
        senha = self.entrada_senha_cadastro.get()

        if not usuario or not senha:
            messagebox.showwarning("Erro", "Preencha todos os campos.")
            return

        if self.usuario_model.criar_usuario(usuario, senha):
            messagebox.showinfo("Cadastro", "Cadastro realizado com sucesso!")
            self.fechar_janela_cadastro()
        else:
            messagebox.showerror("Erro", "Não foi possível realizar o cadastro. Usuário pode já existir.")

    def fechar_janela_cadastro(self):
        if self.cadastro_window:
            self.cadastro_window.destroy()
            self.cadastro_window = None



    def remover_favorito(self):
        if not self.usuario_logado:
            messagebox.showwarning("Erro", "Nenhum usuário logado.")
            return

        selecionado = self.listbox_favoritos.curselection()
        if not selecionado:
            messagebox.showwarning("Erro", "Nenhum jogo selecionado para remover.")
            return

        jogo = self.istbox_favoritos.get(selecionado)
        if self.usuario_model.remover_favorito(self.usuario_logado, jogo):
            messagebox.showinfo("Remover Favorito", f"{jogo} removido dos favoritos.")
            self.atualizar_favoritos()  # Atualiza a lista de favoritos após a remoção
        else:
            messagebox.showerror("Erro", "Erro ao remover o jogo dos favoritos.")



    def login(self):
        usuario = self.entrada_usuario.get()
        senha = self.entrada_senha.get()

        if self.usuario_model.validar_usuario(usuario, senha):
            messagebox.showinfo("Login", "Login realizado com sucesso!")
            self.usuario_logado = usuario  # Armazena o usuário logado
            self.fechar_janela_login()
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos.")

    def esta_logado(self):
        return self.usuario_logado is not None

    def fechar_janela_login(self):
        if self.login_window:
            self.login_window.destroy()
            self.login_window = None


    def tela_cheia(self, event=None):
        self.root.attributes("-fullscreen", True)

    def desativ_tela_cheia(self, event=None):
        self.root.attributes("-fullscreen", False)

    def fechar_app(self):
        resposta = messagebox.askyesno("Confirmar Saída", "Você realmente deseja sair?")
        if resposta:
            self.usuario_model.fechar_conexao()
            self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
