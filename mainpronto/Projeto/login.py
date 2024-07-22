
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os

os.system('cls')
class Novologin:
    def __init__(self):
     self.root = tk.Tk()
     self.root.resizable(False, False)
     self.root.title('Novo Cadastro')
     self.NovoCadastro()
     self.root.mainloop()
    
    
     
    def NovoCadastro(self):
            
     self.label_nome = tk.Label(self.root, text='Digite seu novo nome de usuário :')
     self.label_nome.grid(row=1, column=0, pady=2, padx=2)
    
     self.entry_nome = tk.Entry(self.root)
     self.entry_nome.grid(row=1, column=1, padx=2, pady=2)
     
     
     self.label_datanascimento = tk.Label(self.root, text='Digite sua data de nascimento por completo : (ex. 12/02/2005):')
     self.label_datanascimento.grid(row=2, column=0)
     
     self.entry__datanascimento = tk.Entry(self.root)
     self.entry__datanascimento.grid(row=2, column=1, padx=2, pady=2)
     
     self.label_senha = tk.Label(self.root, text='Digite sua nova senha:')
     self.label_senha.grid(row=3, column=0)
     
     self.entry__senha = tk.Entry(self.root)
     self.entry__senha.grid(row=3, column=1, padx=2, pady=2)
     
    
     #se o botao for clicado ir para outra página
     
     
     
 
        
        
     
    
    
class Cadastro:
    def __init__(self):
     self.root = tk.Tk()
     self.root.resizable(False, False)
     self.root.title('Cadastro')
     self.login()
     self.root.mainloop()
    
    
     
    def login(self):
            
     self.label_nome = tk.Label(self.root, text='Digite seu nome de usuário  cadastrado :')
     self.label_nome.grid(row=1, column=0, pady=2, padx=2)
    
     self.entry_nome = tk.Entry(self.root)
     self.entry_nome.grid(row=1, column=1, padx=2, pady=2)
     
     self.label_senha = tk.Label(self.root, text='Digite sua nova senha:')
     self.label_senha.grid(row=2, column=0)
     
     self.entry__senha = tk.Entry(self.root)
     self.entry__senha.grid(row=2, column=1, padx=2, pady=2)
     
     self.button_ = tk.Button(self.root, text='Enviar', command= lambda : messagebox.showinfo('Login', 'Login  realizado com sucesso !'))
     self.button_.grid(row=3, column=0, pady=4, padx=4)
       
     
     

 