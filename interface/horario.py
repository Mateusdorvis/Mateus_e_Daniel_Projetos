import datetime

class ConfigView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        # Cria o ScrollableFrame e o posiciona usando grid
        self.scrollable_frame = (self)
        self.scrollable_frame.grid(row=1, column=0, columnspan=2, sticky="nsew")

        # Rótulo de título dentro do ScrollableFrame
        self.titulo_label = tk.Label(self.scrollable_frame.scrollable_frame, text="Horário: ", font=("Arial", 15))
        self.titulo_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Rótulo do horário dentro do ScrollableFrame
        self.time_label = ttk.Label(self.scrollable_frame.scrollable_frame, font=("Arial", 15))
        self.time_label.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Atualiza o relógio
        self.update_time()

        # Configura o layout do grid principal
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def update_time(self):
        # Obtém o horário atual
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        # Atualiza o rótulo com o horário
        self.time_label.config(text=current_time)

        # Atualiza o horário a cada 1000 ms (1 segundo)
        self.after(1000, self.update_time)