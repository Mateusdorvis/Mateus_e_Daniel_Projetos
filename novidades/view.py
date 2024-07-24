# view.py
import tkinter as tk
from PIL import Image, ImageTk
from datetime import datetime

class AplicativoDeJogosView:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicativo de Jogos")
        self.root.geometry("700x700")
        self.root.resizable(False, False)
        self.favorito_window = None
        self.login_window = None
        self.info_window = None
        self.carregar_imagens()
        self.criar_interface()
        self.time_label = None
        self.controller = None

    def carregar_imagens(self):
        """Carrega e redimensiona as imagens para os botões e rótulos."""
        imagens = [
            "mario.jpg", "kingdomrush.jpg", "csgo.jpg", "bloons.jpg", "pacman.jpg",
            "donkeykong.jpg", "tetris.jpg", "contra.jpg", "sonic.jpg", "metalslug3.jpg",
            "ark.jpg", "apexlegends.jpg", "dayz.jpg", "teamfortress2.jpg", "pubg.jpg"
        ]
        self.photos = [ImageTk.PhotoImage(Image.open(img).resize((120, 120))) for img in imagens]

    def criar_interface(self):
        """Cria a interface principal do aplicativo."""
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Cria o Frame secundário
        self.frame_secundario = tk.Frame(self.frame, background="#789048")
        self.frame_secundario.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        # Cria o Canvas dentro do frame_secundario
        self.canvas = tk.Canvas(self.frame_secundario, background="#607848")
        self.canvas.grid(row=0, column=0, sticky="nsew")

        # Configura o layout do grid interno para frame_secundario
        self.frame_secundario.grid_rowconfigure(0, weight=1)
        self.frame_secundario.grid_columnconfigure(0, weight=1)

        # Configura o layout do grid interno para o canvas
        self.canvas.grid_rowconfigure(0, weight=1)
        self.canvas.grid_columnconfigure(0, weight=1)

        # Scrolls
        self.scroll_x = tk.Scrollbar(self.frame, orient="horizontal", command=self.canvas.xview)
        self.scroll_x.grid(row=1, column=0, sticky="ew")

        self.scroll_y = tk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        self.scroll_y.grid(row=0, column=1, sticky="ns")

        self.frame_principal = tk.Frame(self.canvas, background="#607848")
        self.frame_principal.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.nome_app_label = tk.Label(self.frame_principal, text="Aplicativo de Jogos", font=("Arial Black", 16), background="#f0f0d8")
        self.nome_app_label.grid(row=0, column=0, columnspan=5, pady=(10, 5), sticky="n")

        self.time_label = tk.Label(self.frame_principal, font=("Arial", 10), background="#f0f0d8")
        self.time_label.grid(row=0, column=4, padx=10, pady=10, sticky="e")

        self.criar_jogos_em_destaque()
        self.criar_jogos_retro()
        self.criar_jogos_fps()

        self.canvas.create_window((0, 0), window=self.frame_principal, anchor="nw")
        self.canvas.configure(xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)

        # Menu
        self.menubar = tk.Menu(self.root)
        self.root.config(menu=self.menubar)

        menu = tk.Menu(self.menubar, tearoff=0)
        menu.add_command(label="Tela", command=self.abrir_janela_info)

        conta = tk.Menu(self.menubar, tearoff=0)
        conta.add_command(label="Favoritos", command=self.abrir_janela_favoritos)
        conta.add_command(label="Login", command=self.abrir_janela_login)

        menu.add_command(label="Sair", command=self.root.destroy)
        self.menubar.add_cascade(label="Configurações", menu=menu)
        self.menubar.add_cascade(label="Conta", menu=conta)

    def criar_jogos_em_destaque(self):
        """Cria a seção de jogos em destaque."""
        label_titulo_destaques = tk.Label(self.frame_principal, text="Jogos em Destaque", background="#f0f0d8", font=("Arial Black", 9))
        label_titulo_destaques.grid(row=0, column=0, padx=5, pady=5, columnspan=5, sticky="nw")

        self.frame_destaques = tk.Frame(self.frame_principal, background="#789048")
        self.frame_destaques.grid(row=1, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")

        jogos = [
            ("Super Mario World", self.photos[0]),
            ("Kingdom Rush", self.photos[1]),
            ("CS:GO", self.photos[2]),
            ("Bloons TD 6", self.photos[3]),
            ("Metal Slug 3", self.photos[9])
        ]

        for index, (nome, img) in enumerate(jogos):
            row = index // 5
            col = index % 5
            tk.Label(self.frame_destaques, text=nome, image=img, compound="top", font=("Arial", 10)).grid(row=row, column=col, padx=5, pady=5)
            tk.Button(self.frame_destaques, text="Adicionar aos Favoritos", font=("Arial", 7), background="#f0f0d8").grid(row=row+1, column=col, padx=5, pady=5)
            tk.Button(self.frame_destaques, text="Download", font=("Arial", 7), background="#f0f0d8").grid(row=row+2, column=col, padx=5, pady=5)

    def criar_jogos_retro(self):
        """Cria a seção de jogos retro."""
        label_titulo_retro = tk.Label(self.frame_principal, text="Jogos Retro", background="#f0f0d8", font=("Arial Black", 9))
        label_titulo_retro.grid(row=2, column=0, padx=5, pady=5, columnspan=5, sticky="nw")

        self.frame_retro = tk.Frame(self.frame_principal, background="#789048")
        self.frame_retro.grid(row=3, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")

        jogos = [
            ("Donkey Kong", self.photos[5]),
            ("Tetris", self.photos[6]),
            ("Contra", self.photos[7]),
            ("Sonic", self.photos[8])
        ]

        for index, (nome, img) in enumerate(jogos):
            row = index // 5
            col = index % 5
            tk.Label(self.frame_retro, text=nome, image=img, compound="top", font=("Arial", 10)).grid(row=row, column=col, padx=5, pady=5)
            tk.Button(self.frame_retro, text="Adicionar aos Favoritos", font=("Arial", 7), background="#f0f0d8").grid(row=row+1, column=col, padx=5, pady=5)
            tk.Button(self.frame_retro, text="Download", font=("Arial", 7), background="#f0f0d8").grid(row=row+2, column=col, padx=5, pady=5)

    def criar_jogos_fps(self):
        """Cria a seção de jogos FPS."""
        label_titulo_fps = tk.Label(self.frame_principal, text="Jogos FPS", background="#f0f0d8", font=("Arial Black", 9))
        label_titulo_fps.grid(row=4, column=0, padx=5, pady=5, columnspan=5, sticky="nw")

        self.frame_fps = tk.Frame(self.frame_principal, background="#789048")
        self.frame_fps.grid(row=5, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")

        jogos = [
            ("ARK", self.photos[10]),
            ("Apex Legends", self.photos[11]),
            ("DayZ", self.photos[12]),
            ("Team Fortress 2", self.photos[13]),
            ("PUBG", self.photos[14])
        ]

        for index, (nome, img) in enumerate(jogos):
            row = index // 5
            col = index % 5
            tk.Label(self.frame_fps, text=nome, image=img, compound="top", font=("Arial", 10)).grid(row=row, column=col, padx=5, pady=5)
            tk.Button(self.frame_fps, text="Adicionar aos Favoritos", font=("Arial", 7), background="#f0f0d8").grid(row=row+1, column=col, padx=5, pady=5)
            tk.Button(self.frame_fps, text="Download", font=("Arial", 7), background="#f0f0d8").grid(row=row+2, column=col, padx=5, pady=5)

    def atualizar_horario(self, horario):
        """Atualiza o horário atual no rótulo."""
        self.time_label.config(text=horario)

    def configurar_eventos(self, controller):
        """Configura os eventos da view com base no controller."""
        self.controller = controller

    def abrir_janela_favoritos(self):
        """Abre a janela de favoritos."""
        if self.favorito_window:
            self.favorito_window.lift()
            return

        self.favorito_window = tk.Toplevel(self.root)
        self.favorito_window.title("Favoritos")
        self.favorito_window.geometry("400x400")
        self.favorito_window.resizable(False, False)

        tk.Label(self.favorito_window, text="Jogos Favoritos", font=("Arial Black", 12)).pack(pady=10)

    def abrir_janela_login(self):
        """Abre a janela de login."""
        if self.login_window:
            self.login_window.lift()
            return

        self.login_window = tk.Toplevel(self.root)
        self.login_window.title("Login")
        self.login_window.geometry("300x200")
        self.login_window.resizable(False, False)

        tk.Label(self.login_window, text="Login", font=("Arial Black", 12)).pack(pady=10)
        tk.Label(self.login_window, text="Usuário").pack(pady=5)
        self.usuario_entry = tk.Entry(self.login_window)
        self.usuario_entry.pack(pady=5)
        tk.Label(self.login_window, text="Senha").pack(pady=5)
        self.senha_entry = tk.Entry(self.login_window, show="*")
        self.senha_entry.pack(pady=5)
        tk.Button(self.login_window, text="Entrar", command=self.realizar_login).pack(pady=10)

    def realizar_login(self):
        """Realiza o login do usuário."""
        nome = self.usuario_entry.get()
        senha = self.senha_entry.get()
        # Implementar lógica de autenticação
        print(f"Login: {nome}, Senha: {senha}")

    def abrir_janela_info(self):
        """Abre a janela de informações sobre o aplicativo."""
        if self.info_window:
            self.info_window.lift()
            return

        self.info_window = tk.Toplevel(self.root)
        self.info_window.title("Informações")
        self.info_window.geometry("300x200")
        self.info_window.resizable(False, False)

        tk.Label(self.info_window, text="Informações do Aplicativo", font=("Arial Black", 12)).pack(pady=10)
        tk.Label(self.info_window, text="Versão 1.0").pack(pady=10)
        tk.Label(self.info_window, text="Desenvolvedor: Seu Nome").pack(pady=10)

    def mostrar_mensagem(self, mensagem):
        """Exibe uma mensagem em uma caixa de diálogo."""
        tk.messagebox.showinfo("Info", mensagem)

    def exibir_usuarios(self, usuarios):
        """Exibe uma lista de usuários."""
        if not usuarios:
            self.mostrar_mensagem("Nenhum usuário encontrado.")
            return

        usuario_window = tk.Toplevel(self.root)
        usuario_window.title("Usuários")
        usuario_window.geometry("300x400")
        
        tk.Label(usuario_window, text="Lista de Usuários", font=("Arial Black", 12)).pack(pady=10)
        
        for usuario in usuarios:
            tk.Label(usuario_window, text=f"ID: {usuario[0]}, Nome: {usuario[1]}, Data de Nascimento: {usuario[2]}").pack(pady=5)
