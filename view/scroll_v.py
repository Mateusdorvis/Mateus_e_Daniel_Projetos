import tkinter as tk
from tkinter import ttk

class ScrollableFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Cria o widget Canvas com a cor de fundo amarela
        self.canvas = tk.Canvas(self)
        self.canvas.grid(row=0, column=0, sticky='nsew')

        # Cria a barra de rolagem (Scrollbar)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollbar.grid(row=0, column=1, sticky='ns')

        # Configura o Canvas para funcionar com a barra de rolagem
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', self.on_canvas_configure)

        # Cria um frame dentro do Canvas com a cor de fundo vermelha
        self.scrollable_frame = ttk.Frame(self.canvas, style="My.TFrame")
        self.scrollable_frame.bind("<Configure>", self.on_frame_configure)

        # Cria uma janela dentro do Canvas que contém o frame
        self.canvas_window = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Configura pesos das colunas e linhas do grid no ScrollableFrame
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame.grid_rowconfigure(0, weight=1)

        # Configura o layout do ScrollableFrame
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def on_frame_configure(self, event):
        # Atualiza a região de rolagem do Canvas para abranger o frame interno
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event):
        # Redimensiona o frame interno para corresponder à largura do Canvas
        self.canvas.itemconfig(self.canvas_window, width=event.width)

