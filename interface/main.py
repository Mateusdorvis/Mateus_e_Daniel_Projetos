import tkinter as tk
from tkinter import messagebox
from tkinter import Tk
from datetime import datetime
from imagens import load_images
from botoes_e_labels import cria_button_fav,entrada_do_mouse,saida_do_mouse,cria_button_download,cria_label_jogo,cria_label_subtitulo,cria_label_titulo
root = tk.Tk()
root.title("Aplicativo de Jogos")
root.geometry("700x700")
root.resizable(False, False)
favorito_window = None
login_window = None
info_window = None

def update_time():

    now = datetime.now()
    
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%A, %d %B %Y")

    time_label.config(text=f"{current_date}\n{current_time}")
    
    root.after(1000, update_time)

def abrir_janela_login():
    global login_window
    
    if login_window and login_window.winfo_exists():
        
        login_window.lift()
        login_window.focus()
        return

    login_window = tk.Toplevel(root)
    login_window.title("Login")
    login_window.geometry("290x200")
    login_window.resizable(False, False)

    frame_login = tk.Frame(login_window, background="#789048")
    frame_login.pack(fill="both", expand=True)

    login_titulo = tk.Label(frame_login, text="Login", font=("Arial Black", 12), background="#cdcfb7")
    login_titulo.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 20), sticky="n")

    login_titulo.bind("<Enter>", entrada_do_mouse)
    login_titulo.bind("<Leave>", saida_do_mouse)

    label_nome = tk.Label(frame_login, text="Nome de Usuário:", font=("Arial Black", 8), background="#cdcfb7")
    label_nome.grid(row=1, column=0, padx=10, pady=10, sticky="e")

    label_nome.bind("<Enter>", entrada_do_mouse)
    label_nome.bind("<Leave>", saida_do_mouse)

    entry_nome = tk.Entry(frame_login)
    entry_nome.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    label_senha = tk.Label(frame_login, text="Senha:", font=("Arial Black", 8), background="#cdcfb7")
    label_senha.grid(row=2, column=0, padx=10, pady=10, sticky="e")

    label_senha.bind("<Enter>", entrada_do_mouse)
    label_senha.bind("<Leave>", saida_do_mouse)

    entry_senha = tk.Entry(frame_login)  
    entry_senha.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    def login():
        usuario = entry_nome.get()
        senha = entry_senha.get()
        messagebox.showinfo("Login", f"Usuário: {usuario}\nSenha: {senha}")
        login_window.destroy()

    login_button = tk.Button(frame_login, text="Login", background="#cdcfb7",command=login)
    login_button.grid(row=3, column=0, columnspan=2, padx=10, pady=(10, 20), sticky="n")

    login_button.bind("<Enter>", entrada_do_mouse)
    login_button.bind("<Leave>", saida_do_mouse)

def abrir_janela_favoritos():
    global favorito_window
    
    # Verifica se a janela 'favorito_window' existe e está visível
    if favorito_window and favorito_window.winfo_exists():
        favorito_window.lift()
        favorito_window.focus()
        return

    # Cria a janela 'favorito_window' se não existir
    favorito_window = tk.Toplevel(root)
    favorito_window.title("Favoritos")
    favorito_window.geometry("300x300")
    favorito_window.resizable(False, False)

    frame_favorito = tk.Frame(favorito_window, background="#789048")
    frame_favorito.pack(fill="both", expand=True)

    favorito_label = tk.Label(frame_favorito, text="Jogos no Favorito", font=("Arial Black", 9), background="#cdcfb7")
    favorito_label.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="n")

    favorito_label.bind("<Enter>", entrada_do_mouse)
    favorito_label.bind("<Leave>", saida_do_mouse)

    

    frame_favorito2 = tk.Frame(frame_favorito, background="#607848")
    frame_favorito2.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    listbox_favorito = tk.Listbox(frame_favorito2, background="#cdcfb7")
    listbox_favorito.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    listbox_favorito.bind("<Enter>", entrada_do_mouse)
    listbox_favorito.bind("<Leave>", saida_do_mouse)

    for item in ["Jogo 1", "Jogo 2", "Jogo 3"]:
        listbox_favorito.insert(tk.END, item)

    frame_favorito.grid_rowconfigure(1, weight=1)
    frame_favorito.grid_columnconfigure(0, weight=1)
    frame_favorito2.grid_rowconfigure(0, weight=1)
    frame_favorito2.grid_columnconfigure(0, weight=1)

def abrir_janela_info():
    global info_window
    
    # Verifica se a janela 'info_window' existe e está visível
    if info_window and info_window.winfo_exists():
        info_window.lift()
        info_window.focus()
        return

    # Cria a janela 'info_window' se não existir
    info_window = tk.Toplevel(root)
    info_window.title("Info")
    info_window.geometry("300x300")
    info_window.resizable(False, False)

    info_frame = tk.Frame(info_window)
    info_frame.pack(fill="both", expand=True)

    info_label = tk.Label(info_frame, text="Informações da Tela", font=("Arial Black", 15))
    info_label.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="n")

    info_label2 = tk.Label(info_frame, text="Tela <F11> Preenche a Tela \n    <ESC> Diminui a Tela", font=("Arial Black", 10))
    info_label2.grid(row=1, column=0, padx=10, pady=(10, 5), sticky="nw")

    info_button = tk.Button(info_frame, text="Voltar", font=("Arial Black", 15), background="#cdcfb7", command=info_window.destroy)
    info_button.grid(row=2, column=0, padx=10, pady=(10, 5), sticky="n")

    info_button.bind("<Enter>", entrada_do_mouse)
    info_button.bind("<Leave>", saida_do_mouse)

    info_frame.grid_rowconfigure(1, weight=1)
    info_frame.grid_columnconfigure(0, weight=1)

def restart():
    root.destroy()
    root = tk.Tk()
    setup()

def tela_cheia(event):
    root.geometry("700x700")
    messagebox.showinfo("Informação", "A Tela foi preenchida.")
    restart()

def desativ_tela_cheia(event):
    root.geometry("500x500")
    messagebox.showinfo("Informação", "A Tela foi diminuida.")
    restart()

def setup():
    """Configura a aplicação e os eventos."""
    root.bind("<F11>", tela_cheia)
    root.bind("<Escape>", desativ_tela_cheia)

def menu():
    menubar = tk.Menu(root)
    root.config(menu=menubar)

    menu = tk.Menu(menubar, tearoff=0)
    menu.add_command(label="Tela", command=lambda: abrir_janela_info())

    conta = tk.Menu(menubar, tearoff=0)

    conta.add_command(label="Favoritos", command=lambda: abrir_janela_favoritos())
    conta.add_command(label="Login", command=lambda: abrir_janela_login())

    menu.add_command(label="Sair", command=root.destroy)
    menubar.add_cascade(label="Configurações", menu=menu)
    menubar.add_cascade(label="Conta", menu=conta)

image1, image2, image3, image4, image5, image6, image7, image8, image9, image10, image11, image12, image13, image14, image15 = load_images()
setup()
menu()

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill=tk.BOTH, expand=True)

frame_secundario = tk.Frame(frame, background="#789048")
frame_secundario.grid(row=0, column=0, sticky="nsew")

canvas = tk.Canvas(frame_secundario, background="#607848")
canvas.grid(row=0, column=0, sticky="nsew")
frame_secundario.grid_rowconfigure(0, weight=1)
frame_secundario.grid_columnconfigure(0, weight=1)

# Scrolls
scroll_x = tk.Scrollbar(frame, orient="horizontal", command=canvas.xview)
scroll_x.grid(row=1, column=0, sticky="ew")

scroll_y = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
scroll_y.grid(row=0, column=1, sticky="ns")

frame_principal = tk.Frame(canvas, background="#607848")
frame_principal.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

canvas.create_window((0, 0), window=frame_principal, anchor="nw")
canvas.configure(xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

label_titulo1 = cria_label_titulo(frame_principal,"Aplicativo de Jogos",0,0,5)

#Label Horário
time_label = tk.Label(frame_principal, font=("Arial", 10), background="#cdcfb7")
time_label.grid(row=0, column=4, padx=10, pady=10, sticky="e")
time_label.bind("<Enter>", entrada_do_mouse)
time_label.bind("<Leave>", saida_do_mouse)

update_time()


#------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Jogos em Destaque
label_subtitulo_destaques = cria_label_subtitulo(frame_principal,"Jogos em Destaque",0,0,5,5)

frame_destaques = tk.Frame(frame_principal, background="#789048")
frame_destaques.grid(row=1, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")

# Super Mario Bros.
label1 = cria_label_jogo(frame_destaques,"Super Mario World",image1,0,0,5,5)
button_favoritos1 = cria_button_fav(frame_destaques,1,0,5,5)
button_download1 = cria_button_download(frame_destaques,2,0,5,5)

# Kingdom Rush
label2 = cria_label_jogo(frame_destaques,"Kingdom Rush",image2,0,1,5,5)
button_favoritos2 = cria_button_fav(frame_destaques,1,1,5,5)
button_download2 = cria_button_download(frame_destaques,2,1,5,5)

# CS:GO
label3 = cria_label_jogo(frame_destaques,"CS:GO",image3,0,2,5,5)
button_favoritos3 = cria_button_fav(frame_destaques,1,2,5,5)
button_download3 = cria_button_download(frame_destaques,2,2,5,5)

# Bloons TD 6
label4 = cria_label_jogo(frame_destaques,"Bloons TD 6",image4,0,3,5,5)
button_favoritos4 = cria_button_fav(frame_destaques,1,3,5,5)
button_download4 = cria_button_download(frame_destaques,2,3,5,5)

# Metal Slug 3
label10 = cria_label_jogo(frame_destaques,"Metal Slug 3",image10,0,4,5,5)
button_favoritos10 = cria_button_fav(frame_destaques,1,4,5,5)
button_download10 = cria_button_download(frame_destaques,2,4,5,5)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Jogos Retrô
label_subtitulo_plataforma = cria_label_subtitulo(frame_principal,"Jogos Retrô",2,0,5,5)

# Frame para os jogos retrô
frame_plataforma = tk.Frame(frame_principal, background="#789048")
frame_plataforma.grid(row=3, column=0,columnspan=5, padx=5, pady=5, sticky="nsew")

# Pacman
label5 = cria_label_jogo(frame_plataforma,"Bloons TD 6",image5,0,0,5,5)
button_favoritos5 = cria_button_fav(frame_plataforma,1,0,5,5)
button_download5 = cria_button_download(frame_plataforma,2,0,5,5)

# Donkey Kong
label6 = cria_label_jogo(frame_plataforma, "Donkey Kong Country", image6, 0, 1, 5, 5)
button_favoritos6 = cria_button_fav(frame_plataforma, 1, 1, 5, 5)
button_download6 = cria_button_download(frame_plataforma, 2, 1, 5, 5)
# Tetris
label7 = cria_label_jogo(frame_plataforma, "Tetris", image7, 0, 2, 5, 5)
button_favoritos7 = cria_button_fav(frame_plataforma, 1, 2, 5, 5)
button_download7 = cria_button_download(frame_plataforma, 2, 2, 5, 5)

# Contra
label8 = cria_label_jogo(frame_plataforma, "Contra", image8, 0, 3, 5, 5)
button_favoritos8 = cria_button_fav(frame_plataforma, 1, 3, 5, 5)
button_download8 = cria_button_download(frame_plataforma, 2, 3, 5, 5)

# Sonic
label9 = cria_label_jogo(frame_plataforma, "Sonic", image9, 0, 4, 5, 5)
button_favoritos9 = cria_button_fav(frame_plataforma, 1, 4, 5, 5)
button_download9 = cria_button_download(frame_plataforma, 2, 4, 5, 5)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Jogos FPS
label_subtitulo_pfps = cria_label_subtitulo(frame_principal,"Jogos FPS",4,0,5,5)
# Frame para os jogos FPS
frame_fps = tk.Frame(frame_principal, background="#789048")
frame_fps.grid(row=5, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")

# ARK
label11 = cria_label_jogo(frame_fps, "ARK: Survival Ascendant", image11, 0, 0, 5, 5)
button_favoritos11 = cria_button_fav(frame_fps, 1, 0, 5, 5)
button_download11 = cria_button_download(frame_fps, 2, 0, 5, 5)

# Apex Legends
label12 = cria_label_jogo(frame_fps, "Apex Legends", image12, 0, 1, 5, 5)
button_favoritos12 = cria_button_fav(frame_fps, 1, 1, 5, 5)
button_download12 = cria_button_download(frame_fps, 2, 1, 5, 5)

# DayZ
label13 = cria_label_jogo(frame_fps, "DayZ", image13, 0, 2, 5, 5)
button_favoritos13 = cria_button_fav(frame_fps, 1, 2, 5, 5)
button_download13 = cria_button_download(frame_fps, 2, 2, 5, 5)

# Team Fortress 2
label14 = cria_label_jogo(frame_fps, "Team Fortress 2", image14, 0, 3, 5, 5)
button_favoritos14 = cria_button_fav(frame_fps, 1, 3, 5, 5)
button_download14 = cria_button_download(frame_fps, 2, 3, 5, 5)

# PUBG
label15 = cria_label_jogo(frame_fps, "PUBG", image15, 0, 4, 5, 5)
button_favoritos15 = cria_button_fav(frame_fps, 1, 4, 5, 5)
button_download15 = cria_button_download(frame_fps, 2, 4, 5, 5)

def configurar_grid(frame, rows, columns):
    # Configura as linhas do grid
    for i in range(rows):
        frame.grid_rowconfigure(i, weight=1 if i == 0 or i == rows - 1 else 0)
    
    # Configura as colunas do grid
    for j in range(columns):
        frame.grid_columnconfigure(j, weight=1)

configurar_grid(frame_destaques, 3, 5)
configurar_grid(frame_plataforma, 3, 5)
configurar_grid(frame_fps, 3, 5)
configurar_grid(frame_principal, 6, 5)
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

if __name__ == "__main__":
    root.mainloop()
