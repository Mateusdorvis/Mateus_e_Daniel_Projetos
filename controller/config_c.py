import tkinter as tk
from tkinter import ttk
from model.usuario_m import UsuarioModel
from view.config_v import ConfigView

class ConfigController:
    def __init__(self, view:ConfigView, model:UsuarioModel):
        self.view = view
        self.model = model