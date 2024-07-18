import tkinter as tk
from view.menu_v import MenuView
from view.tela_inicial_v import TelaInicialView
from controller.tela_inicial_c import TelaInicialController
from model.usuario_m import UsuarioModel
from controller.login_c import LoginController
from view.login_v import LoginView
from view.sair_v import SairView
from controller.sair_c import SairController
from controller.config_c import ConfigController
from view.config_v import ConfigView
class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplicativo de Jogos")
        self.geometry("400x400")
        MenuView(self).pack(fill=tk.BOTH, expand=True)
        self.switch_frame(LoginView)
        
   
    
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)

        if frame_class == LoginView:
            model =  UsuarioModel()
            LoginController(new_frame, model)
        elif frame_class ==  TelaInicialView:
            model =  UsuarioModel()
            TelaInicialController(new_frame,model)
        elif frame_class ==  ConfigView:
            model =  UsuarioModel()
            ConfigController(new_frame,model)
        elif frame_class ==  SairView:
            model =  UsuarioModel()
            SairController(new_frame,model,root=MainApp)
        


        if hasattr(self, "current_frame"):
            self.current_frame.destroy()
        self.current_frame = new_frame
        self.current_frame.pack(fill=tk.BOTH, expand=True)

    

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()











