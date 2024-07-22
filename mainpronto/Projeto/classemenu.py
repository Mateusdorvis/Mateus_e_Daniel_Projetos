import tkinter as tk
from tkinter import ttk
from login import Novologin, Cadastro
from janelas import JanelaVerion



    
    
        
        
class Menus(tk.Menu):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.create_menus()
        

    def create_menus(self):
        #submenu do menu configurações
        aparencia = [
        #mudar para modo escuro
         {'label': 'Altenar para modo  escuro.', 'command' : lambda: mudar_cor_de_fundo('black')},
         #mudar para modo normal
         {'label': 'Alternar para modo normal', 'command' : lambda: mudar_cor_de_fundo('white') },
         {'label': 'Mudar a cor de fundo para amarelo', 'command' : lambda: mudar_cor_de_fundo('#f8ca00') }, 
         {'label': 'Mudar a cor de fundo para laranja', 'command' : lambda: mudar_cor_de_fundo('#e97f02') }
         ]
      
        #função que muda cor da tela
        def mudar_cor_de_fundo(cor):
          self.root.quit()
       
        
        #menu configurações
     
        configuracaos = [
         {'label': 'Sair do aplicativo', 'command' : lambda : self.root.quit()},
         {'label': 'Ver versão', 'command' : JanelaVerion}
         ]
        self.menu_opcao = tk.Menu(self, tearoff=0)
        #craição do submenu 
        self.submenu_config_aparencia = tk.Menu(self.menu_opcao, tearoff=0)
        #menu login
        login = [
         {'label': 'Entrar', 'command' : Cadastro },
         {'label': 'Realizar novo cadastro', 'command' : Novologin},
         ]
        self.menu_login = tk.Menu(self, tearoff=0)
        #menu ajuda
        ajuda = [
         {'label': 'Sobre', 'command' : None},
         ]
        self.menu_ajuda = tk.Menu(self, tearoff=0)
        
        def adicionar_comando(menu, elemento):
            for element in elemento:
                menu.add_command(label = element['label'], command = element['command'])
        #add comando no menu configurações
        adicionar_comando(self.menu_opcao, configuracaos)
        #add comando no submenu do menu configurações
        adicionar_comando(self.submenu_config_aparencia, aparencia)
        #add comando no menu login
        adicionar_comando(self.menu_login, login)
        #add comando no menu ajuda
        adicionar_comando(self.menu_ajuda, ajuda)

        def adicionar_no_menu_principal(titulo_menu, menu_a_ser_add, menu_que_add):
          menu_que_add.add_cascade(label= titulo_menu, menu=menu_a_ser_add)
        #adcionar no menu configurações
        adicionar_no_menu_principal('Alternar para modo...', self.submenu_config_aparencia, self.menu_opcao)
        
        adicionar_no_menu_principal('Configurações', self.menu_opcao, self)
        #adcionar no menu principal
        adicionar_no_menu_principal('Login', self.menu_login, self)


        




