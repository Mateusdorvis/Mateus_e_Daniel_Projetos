import tkinter as tk
from view.scroll_v import ScrollableFrame
from Mateus_e_Daniel_Projetos.view.jogos_fps_v import FPSView  # Supondo que você tenha uma view para FPS
from Mateus_e_Daniel_Projetos.view.jogos_tower_defense_v import TowerDefenseView  # Supondo que você tenha uma view para Tower Defense
from view.jogos_idle_v import IdleView  # Supondo que você tenha uma view para Idle
from view.jogos_plataforma_v import PlataformaView  # Supondo que você tenha uma view para Plataforma

class TelaPrincipalView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()
        self.create_menu()  # Adiciona o menu dropdown

    def create_widgets(self):
        # Cria o ScrollableFrame e o posiciona usando grid
        self.scrollable_frame = ScrollableFrame(self)
        self.scrollable_frame.grid(row=1, column=0, columnspan=3, sticky="nsew")
        
        # Adiciona widgets dentro do ScrollableFrame
        self.add_widgets_to_scrollable_frame()

        # Rótulo de título
        self.titulo_label = tk.Label(self, text="Aplicativo de Jogos", font=("Arial", 20))
        self.titulo_label.grid(row=0, column=0, columnspan=3, pady=10, padx=10)

        # Configura o layout do grid principal
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

    def add_widgets_to_scrollable_frame(self):
        # Adiciona widgets ao frame rolável individualmente com menos espaçamento
        widget1 = tk.Label(self.scrollable_frame.scrollable_frame, text="Item 1", bg="lightblue", width=20, height=9, relief="solid")
        widget1.grid(row=0, column=0, padx=5, pady=5)  # Ajustado padx e pady

        widget2 = tk.Label(self.scrollable_frame.scrollable_frame, text="Item 2", bg="lightblue", width=20, height=9, relief="solid")
        widget2.grid(row=0, column=1, padx=5, pady=5)  # Ajustado padx e pady

        widget3 = tk.Label(self.scrollable_frame.scrollable_frame, text="Item 3", bg="lightblue", width=20, height=9, relief="solid")
        widget3.grid(row=1, column=0, padx=5, pady=5)  # Ajustado padx e pady

        widget4 = tk.Label(self.scrollable_frame.scrollable_frame, text="Item 4", bg="lightblue", width=20, height=9, relief="solid")
        widget4.grid(row=1, column=1, padx=5, pady=5)  # Ajustado padx e pady

    def create_menu(self):
        # Cria um botão de menu no canto superior esquerdo
        mb = tk.Menubutton(self, text="Menu", relief=tk.RAISED, background="#88b499")
        mb.menu = self.create_menu_dropdown(mb)
        mb["menu"] = mb.menu
        mb.grid(row=0, column=0, padx=10, pady=10, sticky="nw")  # Posiciona o menu no canto superior esquerdo

    def create_menu_dropdown(self, master):
        menu_dropdown = tk.Menu(master, tearoff=1)
        menu_dropdown.add_command(label="FPS", command=lambda: self.opcao_selecionada("fps"))
        menu_dropdown.add_command(label="Tower Defense", command=lambda: self.opcao_selecionada("tower_defense"))
        menu_dropdown.add_command(label="Idle", command=lambda: self.opcao_selecionada("idle"))
        menu_dropdown.add_command(label="Plataforma", command=lambda: self.opcao_selecionada("plataforma"))
        return menu_dropdown

    def opcao_selecionada(self, opcao):
        if opcao == "fps":
            self.master.switch_frame(FPSView)
            self.master.title("FPS")
        elif opcao == "tower_defense":
            self.master.switch_frame(TowerDefenseView)
            self.master.title("Tower Defense")
        elif opcao == "idle":
            self.master.switch_frame(IdleView)
            self.master.title("Idle")
        elif opcao == "plataforma":
            self.master.switch_frame(PlataformaView)
            self.master.title("Plataforma")

if __name__ == "__main__":
    root = tk.Tk()
    app = TelaPrincipalView(root)
    app.pack(fill=tk.BOTH, expand=True)
    root.mainloop()


