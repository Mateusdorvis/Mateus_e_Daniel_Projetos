import tkinter as tk
from tkinter import messagebox
from classemenu import Menus
import os

os.system('cls')

def main():
  root = tk.Tk()
  root.title('Aplicativo de baixar roms jogos')
  menu_pricipal  = Menus(root)
  root.config(menu=menu_pricipal)
  root.mainloop()
    
if  __name__ == '__main__':
  main()

  
 
  
  

   

  