import tkinter as tk
from view.login_v import LoginView
from view.tela_inicial_v import TelaInicialView
from view.sair_v import SairView
from view.config_v import ConfigView
class MenuView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()

    def opcao_selecionada(self, opcao):
        if opcao == "1":
            self.master.switch_frame(LoginView)#switch frame é função do pai
            self.master.title("Login")
        elif opcao == "2":
            self.master.switch_frame(TelaInicialView)
            self.master.title("Permanecer desconectado")
        elif opcao == "3":
            self.master.switch_frame(ConfigView)
            self.master.title("Configurações")
        elif opcao == "4":
            self.master.switch_frame(SairView)
            self.master.title("Sair")

    def criar_menu_dropdown(self, master):
        menu_dropdown = tk.Menu(master, tearoff=1)
        menu_dropdown.add_command(label="Login", command=lambda: self.opcao_selecionada("1"))
        menu_dropdown.add_command(label="Permanecer desconectado", command=lambda: self.opcao_selecionada("2"))
        menu_dropdown.add_command(label="Configurações", command=lambda: self.opcao_selecionada("3"))
        menu_dropdown.add_command(label="Sair", command=lambda: self.opcao_selecionada("4"))
        return menu_dropdown

    def create_widgets(self):
        mb = tk.Menubutton(self, text="Menu", relief=tk.RAISED,background="#88b499")
        mb.menu = self.criar_menu_dropdown(mb)
        mb["menu"] = mb.menu
        mb.pack(anchor="nw", pady=12, padx=12)