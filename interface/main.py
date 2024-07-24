import tkinter as tk
from tkinter import messagebox
from tkinter import Tk
from PIL import Image, ImageTk
from datetime import datetime

root = tk.Tk()
root.title("Aplicativo de Jogos")
root.geometry("700x700")
root.resizable(False, False)
favorito_window = None
login_window = None
info_window = None

def load_images():
    image1 = Image.open("mario.jpg").resize((120, 120))
    photo1 = ImageTk.PhotoImage(image1)

    image2 = Image.open("kingdomrush.jpg").resize((120, 120))
    photo2 = ImageTk.PhotoImage(image2)

    image3 = Image.open("csgo.jpg").resize((120, 120))
    photo3 = ImageTk.PhotoImage(image3)

    image4 = Image.open("bloons.jpg").resize((120, 120))
    photo4 = ImageTk.PhotoImage(image4)

    image5 = Image.open("pacman.jpg").resize((120, 120))
    photo5 = ImageTk.PhotoImage(image5)

    image6 = Image.open("donkeykong.jpg").resize((120, 120))
    photo6 = ImageTk.PhotoImage(image6)

    image7 = Image.open("tetris.jpg").resize((120, 120))
    photo7 = ImageTk.PhotoImage(image7)

    image8 = Image.open("contra.jpg").resize((120, 120))
    photo8 = ImageTk.PhotoImage(image8)

    image9 = Image.open("sonic.jpg").resize((120, 120))
    photo9 = ImageTk.PhotoImage(image9)

    image10 = Image.open("metalslug3.jpg").resize((120, 120))
    photo10 = ImageTk.PhotoImage(image10)

    # Corrigir a atribuição das imagens FPS
    image11 = Image.open("ark.jpg").resize((120, 120))
    photo11 = ImageTk.PhotoImage(image11)

    image12 = Image.open("apexlegends.jpg").resize((120, 120))
    photo12 = ImageTk.PhotoImage(image12)

    image13 = Image.open("dayz.jpg").resize((120, 120))
    photo13 = ImageTk.PhotoImage(image13)

    image14 = Image.open("teamfortress2.jpg").resize((120, 120))
    photo14 = ImageTk.PhotoImage(image14)

    image15 = Image.open("pubg.jpg").resize((120, 120))
    photo15 = ImageTk.PhotoImage(image15)

    return photo1, photo2, photo3, photo4, photo5, photo6, photo7, photo8, photo9, photo10, photo11, photo12, photo13, photo14, photo15

image1, image2, image3, image4, image5, image6, image7, image8, image9, image10, image11, image12, image13, image14, image15 = load_images()

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

    login_titulo = tk.Label(frame_login, text="Login", font=("Arial Black", 12), background="#f0f0d8")
    login_titulo.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 20), sticky="n")

    label_nome = tk.Label(frame_login, text="Nome de Usuário:", font=("Arial Black", 8), background="#f0f0d8")
    label_nome.grid(row=1, column=0, padx=10, pady=10, sticky="e")

    entry_nome = tk.Entry(frame_login)
    entry_nome.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    label_senha = tk.Label(frame_login, text="Senha:", font=("Arial Black", 8), background="#f0f0d8")
    label_senha.grid(row=2, column=0, padx=10, pady=10, sticky="e")

    entry_senha = tk.Entry(frame_login)  
    entry_senha.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    def login():
        usuario = entry_nome.get()
        senha = entry_senha.get()
        messagebox.showinfo("Login", f"Usuário: {usuario}\nSenha: {senha}")
        login_window.destroy()

    login_button = tk.Button(frame_login, text="Login", background="#f0f0d8",command=login)
    login_button.grid(row=3, column=0, columnspan=2, padx=10, pady=(10, 20), sticky="n")

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

    favorito_label = tk.Label(frame_favorito, text="Jogos no Favorito", font=("Arial Black", 9), background="#f0f0d8")
    favorito_label.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="n")

    frame_favorito2 = tk.Frame(frame_favorito, background="#607848")
    frame_favorito2.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    listbox_favorito = tk.Listbox(frame_favorito2, background="#f0f0d8")
    listbox_favorito.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

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
setup()

def entrada_do_mouse(event):
    event.widget.config(bg='#fbcc7a')

def saida_do_mouse(event):
    event.widget.config(bg='#f0f0d8')


frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Cria o Frame secundário
frame_secundario = tk.Frame(frame, background="#789048")
frame_secundario.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

# Cria o Canvas dentro do frame_secundario
canvas = tk.Canvas(frame_secundario, background="#607848")
canvas.grid(row=0, column=0, sticky="nsew")

# Configura o layout do grid interno para frame_secundario
frame_secundario.grid_rowconfigure(0, weight=1)
frame_secundario.grid_columnconfigure(0, weight=1)

# Configura o layout do grid interno para o canvas
canvas.grid_rowconfigure(0, weight=1)
canvas.grid_columnconfigure(0, weight=1)
# Scrolls
scroll_x = tk.Scrollbar(frame, orient="horizontal", command=canvas.xview)
scroll_x.grid(row=1, column=0, sticky="ew")

scroll_y = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
scroll_y.grid(row=0, column=1, sticky="ns")

frame_principal = tk.Frame(canvas, background="#607848")
frame_principal.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

nome_app_label = tk.Label(frame_principal, text="Aplicativo de Jogos", font=("Arial Black", 16), background="#f0f0d8")
nome_app_label.grid(row=0, column=0, columnspan=5, pady=(10, 5), sticky="n")

nome_app_label.bind("<Enter>", entrada_do_mouse)
nome_app_label.bind("<Leave>", saida_do_mouse)

time_label = tk.Label(frame_principal, font=("Arial", 10), background="#f0f0d8")
time_label.grid(row=0, column=4, padx=10, pady=10, sticky="e")


time_label.bind("<Enter>", entrada_do_mouse)
time_label.bind("<Leave>", saida_do_mouse)


def update_time():

    now = datetime.now()
    
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%A, %d %B %Y")

    time_label.config(text=f"{current_date}\n{current_time}")
    
    root.after(1000, update_time)
update_time()

canvas.create_window((0, 0), window=frame_principal, anchor="nw")
canvas.configure(xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

# Título de Jogos em Destaque
label_titulo_destaques = tk.Label(frame_principal, text="Jogos em Destaque", background="#f0f0d8", font=("Arial Black", 9))
label_titulo_destaques.grid(row=0, column=0, padx=5, pady=5, columnspan=5, sticky="nw")


label_titulo_destaques.bind("<Enter>", entrada_do_mouse)
label_titulo_destaques.bind("<Leave>", saida_do_mouse)

#menu
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

# Frame para os jogos em destaque
frame_destaques = tk.Frame(frame_principal, background="#789048")
frame_destaques.grid(row=1, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")

# Super Mario Bros.
label1 = tk.Label(frame_destaques, text="Super Mario World", image=image1, compound="top", font=("Arial", 10))
label1.grid(row=0, column=0, padx=5, pady=5)

label1.bind("<Enter>", entrada_do_mouse)
label1.bind("<Leave>", saida_do_mouse)

button_favoritos1 = tk.Button(frame_destaques, text="Adicionar aos Favoritos", font=("Arial", 7),background="#f0f0d8")
button_favoritos1.grid(row=1, column=0, padx=5, pady=5)

button_favoritos1.bind("<Enter>", entrada_do_mouse)
button_favoritos1.bind("<Leave>", saida_do_mouse)

button_download1 = tk.Button(frame_destaques, text="Download", font=("Arial", 7),background="#f0f0d8")
button_download1.grid(row=2, column=0, padx=5, pady=5)

button_download1.bind("<Enter>", entrada_do_mouse)
button_download1.bind("<Leave>", saida_do_mouse)

# Kingdom Rush
label2 = tk.Label(frame_destaques, text="Kingdom Rush", image=image2, compound="top", font=("Arial", 10))
label2.grid(row=0, column=1, padx=5, pady=5)

label2.bind("<Enter>", entrada_do_mouse)
label2.bind("<Leave>", saida_do_mouse)

button_favoritos2 = tk.Button(frame_destaques, text="Adicionar aos Favoritos", font=("Arial", 7),background="#f0f0d8")
button_favoritos2.grid(row=1, column=1, padx=5, pady=5)

button_favoritos2.bind("<Enter>", entrada_do_mouse)
button_favoritos2.bind("<Leave>", saida_do_mouse)

button_download2 = tk.Button(frame_destaques, text="Download", font=("Arial", 7),background="#f0f0d8")
button_download2.grid(row=2, column=1, padx=5, pady=5)

button_download2.bind("<Enter>", entrada_do_mouse)
button_download2.bind("<Leave>", saida_do_mouse)

# CS:GO
label3 = tk.Label(frame_destaques, text="CS:GO", image=image3, compound="top", font=("Arial", 10))
label3.grid(row=0, column=2, padx=5, pady=5)

label3.bind("<Enter>", entrada_do_mouse)
label3.bind("<Leave>", saida_do_mouse)

button_favoritos3 = tk.Button(frame_destaques, text="Adicionar aos Favoritos", font=("Arial", 7),background="#f0f0d8")
button_favoritos3.grid(row=1, column=2, padx=5, pady=5)

button_favoritos3.bind("<Enter>", entrada_do_mouse)
button_favoritos3.bind("<Leave>", saida_do_mouse)

button_download3 = tk.Button(frame_destaques, text="Download", font=("Arial", 7),background="#f0f0d8")
button_download3.grid(row=2, column=2, padx=5, pady=5)

button_download3.bind("<Enter>", entrada_do_mouse)
button_download3.bind("<Leave>", saida_do_mouse)

# Bloons TD 6
label4 = tk.Label(frame_destaques, text="Bloons TD 6", image=image4, compound="top", font=("Arial", 10))
label4.grid(row=0, column=3, padx=5, pady=5)

label4.bind("<Enter>", entrada_do_mouse)
label4.bind("<Leave>", saida_do_mouse)

button_favoritos4 = tk.Button(frame_destaques, text="Adicionar aos Favoritos", font=("Arial", 7),background="#f0f0d8")
button_favoritos4.grid(row=1, column=3, padx=5, pady=5)

button_favoritos4.bind("<Enter>", entrada_do_mouse)
button_favoritos4.bind("<Leave>", saida_do_mouse)

button_download4 = tk.Button(frame_destaques, text="Download", font=("Arial", 7),background="#f0f0d8")
button_download4.grid(row=2, column=3, padx=5, pady=5)

button_download4.bind("<Enter>", entrada_do_mouse)
button_download4.bind("<Leave>", saida_do_mouse)

# Metal Slug 3
label10 = tk.Label(frame_destaques, text="Metal Slug 3", image=image10, compound="top", font=("Arial", 10))
label10.grid(row=0, column=4, padx=5, pady=5)

label10.bind("<Enter>", entrada_do_mouse)
label10.bind("<Leave>", saida_do_mouse)

button_favoritos10 = tk.Button(frame_destaques, text="Adicionar aos Favoritos", font=("Arial", 7),background="#f0f0d8")
button_favoritos10.grid(row=1, column=4, padx=5, pady=5)

button_favoritos10.bind("<Enter>", entrada_do_mouse)
button_favoritos10.bind("<Leave>", saida_do_mouse)

button_download10 = tk.Button(frame_destaques, text="Download", font=("Arial", 7),background="#f0f0d8")
button_download10.grid(row=2, column=4, padx=5, pady=5)

button_download10.bind("<Enter>", entrada_do_mouse)
button_download10.bind("<Leave>", saida_do_mouse)

# Título de Jogos Retrô
label_titulo_plataforma = tk.Label(frame_principal, text="Jogos Retrô", compound="top", background="#f0f0d8", font=("Arial Black", 9))
label_titulo_plataforma.grid(row=2, column=0, padx=5, pady=5, columnspan=5, sticky="nw")

label_titulo_plataforma.bind("<Enter>", entrada_do_mouse)
label_titulo_plataforma.bind("<Leave>", saida_do_mouse)

# Frame para os jogos retrô
frame_plataforma = tk.Frame(frame_principal, background="#789048")
frame_plataforma.grid(row=3, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")

# Pacman
label5 = tk.Label(frame_plataforma, text="Pacman", image=image5, compound="top", font=("Arial", 10))
label5.grid(row=0, column=0, padx=5, pady=5)

label5.bind("<Enter>", entrada_do_mouse)
label5.bind("<Leave>", saida_do_mouse)

button_favoritos5 = tk.Button(frame_plataforma, text="Adicionar aos Favoritos", font=("Arial", 7),background="#f0f0d8")
button_favoritos5.grid(row=1, column=0, padx=5, pady=5)

button_favoritos5.bind("<Enter>", entrada_do_mouse)
button_favoritos5.bind("<Leave>", saida_do_mouse)

button_download5 = tk.Button(frame_plataforma, text="Download", font=("Arial", 7),background="#f0f0d8")
button_download5.grid(row=2, column=0, padx=5, pady=5)

button_download5.bind("<Enter>", entrada_do_mouse)
button_download5.bind("<Leave>", saida_do_mouse)

# Donkey Kong
label6 = tk.Label(frame_plataforma, text="Donkey Kong Country", image=image6, compound="top", font=("Arial", 9))
label6.grid(row=0, column=1, padx=5, pady=5)

label6.bind("<Enter>", entrada_do_mouse)
label6.bind("<Leave>", saida_do_mouse)

button_favoritos6 = tk.Button(frame_plataforma, text="Adicionar aos Favoritos", font=("Arial", 7),background="#f0f0d8")
button_favoritos6.grid(row=1, column=1, padx=5, pady=5)

button_favoritos6.bind("<Enter>", entrada_do_mouse)
button_favoritos6.bind("<Leave>", saida_do_mouse)

button_download6 = tk.Button(frame_plataforma, text="Download", font=("Arial", 7),background="#f0f0d8")
button_download6.grid(row=2, column=1, padx=5, pady=5)

button_download6.bind("<Enter>", entrada_do_mouse)
button_download6.bind("<Leave>", saida_do_mouse)

# Tetris
label7 = tk.Label(frame_plataforma, text="Tetris", image=image7, compound="top", font=("Arial", 10))
label7.grid(row=0, column=2, padx=5, pady=5)

label7.bind("<Enter>", entrada_do_mouse)
label7.bind("<Leave>", saida_do_mouse)

button_favoritos7 = tk.Button(frame_plataforma, text="Adicionar aos Favoritos", font=("Arial", 7),background="#f0f0d8")
button_favoritos7.grid(row=1, column=2, padx=5, pady=5)

button_favoritos7.bind("<Enter>", entrada_do_mouse)
button_favoritos7.bind("<Leave>", saida_do_mouse)

button_download7 = tk.Button(frame_plataforma, text="Download", font=("Arial", 7),background="#f0f0d8")
button_download7.grid(row=2, column=2, padx=5, pady=5)

button_download7.bind("<Enter>", entrada_do_mouse)
button_download7.bind("<Leave>", saida_do_mouse)

# Contra
label8 = tk.Label(frame_plataforma, text="Contra", image=image8, compound="top", font=("Arial", 10))
label8.grid(row=0, column=3, padx=5, pady=5)

label8.bind("<Enter>", entrada_do_mouse)
label8.bind("<Leave>", saida_do_mouse)

button_favoritos8 = tk.Button(frame_plataforma, text="Adicionar aos Favoritos", font=("Arial", 7),background="#f0f0d8")
button_favoritos8.grid(row=1, column=3, padx=5, pady=5)

button_favoritos8.bind("<Enter>", entrada_do_mouse)
button_favoritos8.bind("<Leave>", saida_do_mouse)

button_download8 = tk.Button(frame_plataforma, text="Download", font=("Arial", 7),background="#f0f0d8")
button_download8.grid(row=2, column=3, padx=5, pady=5)

button_download8.bind("<Enter>", entrada_do_mouse)
button_download8.bind("<Leave>", saida_do_mouse)

# Sonic
label9 = tk.Label(frame_plataforma, text="Sonic", image=image9, compound="top", font=("Arial", 10))
label9.grid(row=0, column=4, padx=5, pady=5)

label9.bind("<Enter>", entrada_do_mouse)
label9.bind("<Leave>", saida_do_mouse)

button_favoritos9 = tk.Button(frame_plataforma, text="Adicionar aos Favoritos", font=("Arial", 7),background="#f0f0d8")
button_favoritos9.grid(row=1, column=4, padx=5, pady=5)

button_favoritos9.bind("<Enter>", entrada_do_mouse)
button_favoritos9.bind("<Leave>", saida_do_mouse)

button_download9 = tk.Button(frame_plataforma, text="Download", font=("Arial", 7),background="#f0f0d8")
button_download9.grid(row=2, column=4, padx=5, pady=5)

button_download9.bind("<Enter>", entrada_do_mouse)
button_download9.bind("<Leave>", saida_do_mouse)

# Título de Jogos FPS
label_titulo_fps = tk.Label(frame_principal, text="Jogos FPS", compound="top", background="#f0f0d8", font=("Arial Black", 9))
label_titulo_fps.grid(row=4, column=0, padx=5, pady=5, columnspan=5, sticky="nw")

label_titulo_fps.bind("<Enter>", entrada_do_mouse)
label_titulo_fps.bind("<Leave>", saida_do_mouse)

# Frame para os jogos FPS
frame_fps = tk.Frame(frame_principal, background="#789048")
frame_fps.grid(row=5, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")

# ARK
label11 = tk.Label(frame_fps, text="ARK: Survival Ascendent", image=image11, compound="top", font=("Arial", 9))
label11.grid(row=0, column=0, padx=5, pady=5)

label11.bind("<Enter>", entrada_do_mouse)
label11.bind("<Leave>", saida_do_mouse)

button_favoritos11 = tk.Button(frame_fps, text="Adicionar aos Favoritos", font=("Arial", 7),background="#f0f0d8")
button_favoritos11.grid(row=1, column=0, padx=5, pady=5)

button_favoritos11.bind("<Enter>", entrada_do_mouse)
button_favoritos11.bind("<Leave>", saida_do_mouse)

button_download11 = tk.Button(frame_fps, text="Download", font=("Arial", 7),background="#f0f0d8")
button_download11.grid(row=2, column=0, padx=5, pady=5)

button_download11.bind("<Enter>", entrada_do_mouse)
button_download11.bind("<Leave>", saida_do_mouse)

# Apex Legends
label12 = tk.Label(frame_fps, text="Apex Legends", image=image12, compound="top", font=("Arial", 10))
label12.grid(row=0, column=1, padx=5, pady=5)

label12.bind("<Enter>", entrada_do_mouse)
label12.bind("<Leave>", saida_do_mouse)

button_favoritos12 = tk.Button(frame_fps, text="Adicionar aos Favoritos", font=("Arial", 7),background="#f0f0d8")
button_favoritos12.grid(row=1, column=1, padx=5, pady=5)

button_favoritos12.bind("<Enter>", entrada_do_mouse)
button_favoritos12.bind("<Leave>", saida_do_mouse)

button_download12 = tk.Button(frame_fps, text="Download", font=("Arial", 7),background="#f0f0d8")
button_download12.grid(row=2, column=1, padx=5, pady=5)

button_download12.bind("<Enter>", entrada_do_mouse)
button_download12.bind("<Leave>", saida_do_mouse)

# DayZ
label13 = tk.Label(frame_fps, text="DayZ", image=image13, compound="top", font=("Arial", 10))
label13.grid(row=0, column=2, padx=5, pady=5)

label13.bind("<Enter>", entrada_do_mouse)
label13.bind("<Leave>", saida_do_mouse)

button_favoritos13 = tk.Button(frame_fps, text="Adicionar aos Favoritos", font=("Arial", 7),background="#f0f0d8")
button_favoritos13.grid(row=1, column=2, padx=5, pady=5)

button_favoritos13.bind("<Enter>", entrada_do_mouse)
button_favoritos13.bind("<Leave>", saida_do_mouse)

button_download13 = tk.Button(frame_fps, text="Download", font=("Arial", 7),background="#f0f0d8")
button_download13.grid(row=2, column=2, padx=5, pady=5)

button_download13.bind("<Enter>", entrada_do_mouse)
button_download13.bind("<Leave>", saida_do_mouse)

# Team Fortress 2
label14 = tk.Label(frame_fps, text="Team Fortress 2", image=image14, compound="top", font=("Arial", 10))
label14.grid(row=0, column=3, padx=5, pady=5)

label14.bind("<Enter>", entrada_do_mouse)
label14.bind("<Leave>", saida_do_mouse)

button_favoritos14 = tk.Button(frame_fps, text="Adicionar aos Favoritos", font=("Arial", 7),background="#f0f0d8")
button_favoritos14.grid(row=1, column=3, padx=5, pady=5)

button_favoritos14.bind("<Enter>", entrada_do_mouse)
button_favoritos14.bind("<Leave>", saida_do_mouse)

button_download14 = tk.Button(frame_fps, text="Download", font=("Arial", 7),background="#f0f0d8")
button_download14.grid(row=2, column=3, padx=5, pady=5)

button_download14.bind("<Enter>", entrada_do_mouse)
button_download14.bind("<Leave>", saida_do_mouse)

# PUBG
label15 = tk.Label(frame_fps, text="PUBG", image=image15, compound="top", font=("Arial", 10))
label15.grid(row=0, column=4, padx=5, pady=5)

label15.bind("<Enter>", entrada_do_mouse)
label15.bind("<Leave>", saida_do_mouse)

button_favoritos15 = tk.Button(frame_fps, text="Adicionar aos Favoritos", font=("Arial", 7),background="#f0f0d8")
button_favoritos15.grid(row=1, column=4, padx=5, pady=5)

button_favoritos15.bind("<Enter>", entrada_do_mouse)
button_favoritos15.bind("<Leave>", saida_do_mouse)

button_download15 = tk.Button(frame_fps, text="Download", font=("Arial", 7),background="#f0f0d8")
button_download15.grid(row=2, column=4, padx=5, pady=5)

button_download15.bind("<Enter>", entrada_do_mouse)
button_download15.bind("<Leave>", saida_do_mouse)

# Configura o layout do grid interno
frame_destaques.grid_rowconfigure(0, weight=1)
frame_destaques.grid_rowconfigure(1, weight=0)
frame_destaques.grid_rowconfigure(2, weight=0)
frame_destaques.grid_columnconfigure(0, weight=1)
frame_destaques.grid_columnconfigure(1, weight=1)
frame_destaques.grid_columnconfigure(2, weight=1)
frame_destaques.grid_columnconfigure(3, weight=1)
frame_destaques.grid_columnconfigure(4, weight=1)

frame_plataforma.grid_rowconfigure(0, weight=1)
frame_plataforma.grid_rowconfigure(1, weight=0)
frame_plataforma.grid_rowconfigure(2, weight=0)
frame_plataforma.grid_columnconfigure(0, weight=1)
frame_plataforma.grid_columnconfigure(1, weight=1)
frame_plataforma.grid_columnconfigure(2, weight=1)
frame_plataforma.grid_columnconfigure(3, weight=1)
frame_plataforma.grid_columnconfigure(4, weight=1)

frame_fps.grid_rowconfigure(0, weight=1)
frame_fps.grid_rowconfigure(1, weight=0)
frame_fps.grid_rowconfigure(2, weight=0)
frame_fps.grid_columnconfigure(0, weight=1)
frame_fps.grid_columnconfigure(1, weight=1)
frame_fps.grid_columnconfigure(2, weight=1)
frame_fps.grid_columnconfigure(3, weight=1)
frame_fps.grid_columnconfigure(4, weight=1)

# Configura o layout do Frame principal
frame_principal.grid_rowconfigure(0, weight=1)
frame_principal.grid_rowconfigure(1, weight=0)
frame_principal.grid_rowconfigure(2, weight=0)
frame_principal.grid_rowconfigure(3, weight=1)
frame_principal.grid_rowconfigure(4, weight=0)
frame_principal.grid_rowconfigure(5, weight=1)
frame_principal.grid_columnconfigure(0, weight=1)
frame_principal.grid_columnconfigure(1, weight=1)
frame_principal.grid_columnconfigure(2, weight=1)
frame_principal.grid_columnconfigure(3, weight=1)
frame_principal.grid_columnconfigure(4, weight=1)

# Ajusta as proporções do Canvas e do Frame
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

# Executa o loop principal do tkinter
if __name__ == "__main__":
    root.mainloop()
