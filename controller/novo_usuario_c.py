import tkinter as tk
from tkinter import messagebox
from model.usuario_m import UsuarioModel
from view.register_v import RegisterView

class RegisterController:
    def __init__(self, view: RegisterView, model: UsuarioModel):
        self.view = view
        self.model = model
        self.view.register_button.config(command=self.register_user)

    def register_user(self):
        username = self.view.username_entry.get()
        password = self.view.password_entry.get()
        confirm_password = self.view.confirm_password_entry.get()

        if not username or not password or not confirm_password:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
            return

        if password != confirm_password:
            messagebox.showerror("Erro", "As senhas não correspondem.")
            return

        if self.model.authenticate(username, password):
            messagebox.showerror("Erro", "Nome de usuário já existe.")
            return

        self.model.add_user(username, password)
        messagebox.showinfo("Sucesso", "Usuário registrado com sucesso!")
