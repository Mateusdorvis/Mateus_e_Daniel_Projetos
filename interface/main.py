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

def load_images():
    # Carrega e redimensiona as imagens
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

import tkinter as tk
from tkinter import messagebox

# Variável global para manter a referência da janela de login
login_window = None

def abrir_janela_login():
    global login_window
    
    # Verifica se a janela de login já foi criada
    if login_window and login_window.winfo_exists():
        # Se a janela já estiver aberta, apenas a traz para o topo
        login_window.lift()
        login_window.focus()
        return

    # Cria uma nova janela
    login_window = tk.Toplevel(root)
    login_window.title("Login")
    login_window.geometry("290x200")
    login_window.resizable(False, False)

    # Cria um frame para organizar os widgets com grid
    frame_login = tk.Frame(login_window, background="#789048")
    frame_login.pack(fill="both", expand=True)

    # Título da janela de login
    login_titulo = tk.Label(frame_login, text="Login", font=("Arial Black", 12), background="#f0f0d8")
    login_titulo.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 20), sticky="n")

    # Rótulo e campo para nome de usuário
    label_nome = tk.Label(frame_login, text="Nome de Usuário:", font=("Arial Black", 8), background="#f0f0d8")
    label_nome.grid(row=1, column=0, padx=10, pady=10, sticky="e")

    entry_nome = tk.Entry(frame_login)
    entry_nome.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    # Rótulo e campo para senha
    label_senha = tk.Label(frame_login, text="Senha:",font=("Arial Black", 8), background="#f0f0d8")
    label_senha.grid(row=2, column=0, padx=10, pady=10, sticky="e")

    entry_senha = tk.Entry(frame_login)
    entry_senha.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    # Função para o botão de login
    def login():
        usuario = entry_nome.get()
        senha = entry_senha.get()
        # Aqui você pode adicionar lógica para autenticação
        # Por enquanto, só exibe uma mensagem de sucesso
        messagebox.showinfo("Login", f"Usuário: {usuario}\nSenha: {senha}")
        login_window.destroy()


    # Botões para login e cancelar
    login_button = tk.Button(frame_login, text="Login", background="#f0f0d8",command=login)
    login_button.grid(row=3, column=0, columnspan=2, padx=10, pady=(10, 20), sticky="n")


def abrir_janela_favoritos():
    global favorito_window
    
    # Verifica se a janela de favoritos já foi criada
    if favorito_window and favorito_window.winfo_exists():
        # Se a janela já estiver aberta, apenas a traz para o topo
        favorito_window.lift()
        favorito_window.focus()
        return

    # Cria uma nova janela se não existir uma janela de favoritos
    favorito_window = tk.Toplevel(root)
    favorito_window.title("Favoritos")
    favorito_window.geometry("300x300")
    favorito_window.resizable(False, False)

    # Configura o grid principal da janela
    favorito_window.grid_rowconfigure(0, weight=0)  # Linha 0 para o rótulo
    favorito_window.grid_rowconfigure(1, weight=1)  # Linha 1 para o frame_favorito2
    favorito_window.grid_columnconfigure(0, weight=1)
    favorito_window.grid_columnconfigure(1, weight=1)


    frame_favorito = tk.Canvas(favorito_window, background="#789048")
    frame_favorito.pack(expand="yes", fill="both")

    # Cria o rótulo favorito_label
    favorito_label = tk.Label(frame_favorito, text="Jogos no Favorito", font=("Arial Black", 9), background="#f0f0d8")
    favorito_label.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="n")

    # Cria e configura o frame_favorito2
    frame_favorito2 = tk.Frame(frame_favorito, background="#607848")
    frame_favorito2.grid(row=1, column=0, rowspan=3, padx=10, pady=10, sticky="nsew")

    # Configura o layout interno do frame_favorito para que o frame_favorito2 expanda
    frame_favorito.grid_rowconfigure(1, weight=1)
    frame_favorito.grid_columnconfigure(0, weight=1)

# Cria o Frame principal
frame = tk.Frame(root, background="lightgrey")
frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

canvas = tk.Canvas(frame, background="#607848")
canvas.grid(row=0, column=0, sticky="nsew")

# Scrolls
scroll_x = tk.Scrollbar(frame, orient="horizontal", command=canvas.xview)
scroll_x.grid(row=1, column=0, sticky="ew")

scroll_y = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
scroll_y.grid(row=0, column=1, sticky="ns")

frame_principal = tk.Frame(canvas, background="#607848")
frame_principal.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

nome_app_label = tk.Label(frame_principal, text="Aplicativo de Jogos", font=("Arial Black", 16), background="#f0f0d8")
nome_app_label.grid(row=0, column=0, columnspan=5, pady=(10, 5), sticky="n")

time_label = tk.Label(frame_principal, font=("Arial", 10), background="#f0f0d8")
time_label.grid(row=0, column=4, padx=10, pady=10, sticky="e")

def update_time():
    # Obtém o horário atual
    now = datetime.now()
    
    # Formata o horário e a data
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%A, %d %B %Y")  # Exemplo: "Sunday, 23 July 2024"
    
    # Atualiza o rótulo com a data e o horário
    time_label.config(text=f"{current_date}\n{current_time}")

    # Atualiza o horário a cada 1000 ms (1 segundo)
    root.after(1000, update_time)

# Inicia a atualização do horário
update_time()


canvas.create_window((0, 0), window=frame_principal, anchor="nw")
canvas.configure(xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

# Título de Jogos em Destaque
label_titulo_destaques = tk.Label(frame_principal, text="Jogos em Destaque", background="#f0f0d8", font=("Arial Black", 9))
label_titulo_destaques.grid(row=0, column=0, padx=5, pady=5, columnspan=5, sticky="nw")

#menu
menubar = tk.Menu(root)
root.config(menu=menubar)

menu = tk.Menu(menubar, tearoff=0)
menu.add_command(label="Ativar Tela Cheia", command=lambda: tela_cheia)
menu.add_command(label="Desativar Tela Cheia", command=lambda: desativ_tela_cheia)

conta = tk.Menu(menubar, tearoff=0)

conta.add_command(label="Favoritos", command=lambda: abrir_janela_favoritos())
conta.add_command(label="Login", command=lambda: abrir_janela_login())

menu.add_command(label="Sair", command=root.destroy)
menubar.add_cascade(label="Configurações", menu=menu)
menubar.add_cascade(label="Conta", menu=conta)


def tela_cheia(event):
    root.attributes("-fullscreen", True)
    messagebox.showinfo("Informação", "A opção de Tela é Tela Cheia.")
def desativ_tela_cheia(event):
    root.attributes("-fullscreen", False)
    messagebox.showinfo("Informação", "A opção de Tela é Default.")


# Frame para os jogos em destaque
frame_destaques = tk.Frame(frame_principal, background="#789048")
frame_destaques.grid(row=1, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")

# Super Mario Bros.
label1 = tk.Label(frame_destaques, text="Super Mario Bros.", image=image1, compound="top", font=("Arial", 10))
label1.grid(row=0, column=0, padx=5, pady=5)

button_favoritos1 = tk.Button(frame_destaques, text="Adicionar aos Favoritos", font=("Arial", 7),background="#f0f0d8")
button_favoritos1.grid(row=1, column=0, padx=5, pady=5)

button_download1 = tk.Button(frame_destaques, text="Download", font=("Arial", 7),background="#f0f0d8")
button_download1.grid(row=2, column=0, padx=5, pady=5)

# Kingdom Rush
label2 = tk.Label(frame_destaques, text="Kingdom Rush", image=image2, compound="top", font=("Arial", 10))
label2.grid(row=0, column=1, padx=5, pady=5)

button_favoritos2 = tk.Button(frame_destaques, text="Adicionar aos Favoritos", font=("Arial", 7),background="#f0f0d8")
button_favoritos2.grid(row=1, column=1, padx=5, pady=5)

button_download2 = tk.Button(frame_destaques, text="Download", font=("Arial", 7),background="#f0f0d8")
button_download2.grid(row=2, column=1, padx=5, pady=5)

# CS:GO
label3 = tk.Label(frame_destaques, text="CS:GO", image=image3, compound="top", font=("Arial", 10))
label3.grid(row=0, column=2, padx=5, pady=5)

button_favoritos3 = tk.Button(frame_destaques, text="Adicionar aos Favoritos", font=("Arial", 7),background="#f0f0d8")
button_favoritos3.grid(row=1, column=2, padx=5, pady=5)

button_download3 = tk.Button(frame_destaques, text="Download", font=("Arial", 7),background="#f0f0d8")
button_download3.grid(row=2, column=2, padx=5, pady=5)

# Bloons TD 6
label4 = tk.Label(frame_destaques, text="Bloons TD 6", image=image4, compound="top", font=("Arial", 10))
label4.grid(row=0, column=3, padx=5, pady=5)

button_favoritos4 = tk.Button(frame_destaques, text="Adicionar aos Favoritos", font=("Arial", 7),background="#f0f0d8")
button_favoritos4.grid(row=1, column=3, padx=5, pady=5)

button_download4 = tk.Button(frame_destaques, text="Download", font=("Arial", 7),background="#f0f0d8")
button_download4.grid(row=2, column=3, padx=5, pady=5)

# Metal Slug 3
label10 = tk.Label(frame_destaques, text="Metal Slug 3", image=image10, compound="top", font=("Arial", 10))
label10.grid(row=0, column=4, padx=5, pady=5)

button_favoritos10 = tk.Button(frame_destaques, text="Adicionar aos Favoritos", font=("Arial", 7),background="#f0f0d8")
button_favoritos10.grid(row=1, column=4, padx=5, pady=5)

button_download10 = tk.Button(frame_destaques, text="Download", font=("Arial", 7),background="#f0f0d8")
button_download10.grid(row=2, column=4, padx=5, pady=5)

# Título de Jogos Retrô
label_titulo_plataforma = tk.Label(frame_principal, text="Jogos Retrô", compound="top", background="#f0f0d8", font=("Arial Black", 9))
label_titulo_plataforma.grid(row=2, column=0, padx=5, pady=5, columnspan=5, sticky="nw")

# Frame para os jogos retrô
frame_plataforma = tk.Frame(frame_principal, background="#789048")
frame_plataforma.grid(row=3, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")

# Pacman
label5 = tk.Label(frame_plataforma, text="Pacman", image=image5, compound="top", font=("Arial", 10))
label5.grid(row=0, column=0, padx=5, pady=5)

button_favoritos5 = tk.Button(frame_plataforma, text="Adicionar aos Favoritos", font=("Arial", 7),background="#f0f0d8")
button_favoritos5.grid(row=1, column=0, padx=5, pady=5)

button_download5 = tk.Button(frame_plataforma, text="Download", font=("Arial", 7),background="#f0f0d8")
button_download5.grid(row=2, column=0, padx=5, pady=5)

# Donkey Kong
label6 = tk.Label(frame_plataforma, text="Donkey Kong", image=image6, compound="top", font=("Arial", 10))
label6.grid(row=0, column=1, padx=5, pady=5)

button_favoritos6 = tk.Button(frame_plataforma, text="Adicionar aos Favoritos", font=("Arial", 7),background="#f0f0d8")
button_favoritos6.grid(row=1, column=1, padx=5, pady=5)

button_download6 = tk.Button(frame_plataforma, text="Download", font=("Arial", 7),background="#f0f0d8")
button_download6.grid(row=2, column=1, padx=5, pady=5)

# Tetris
label7 = tk.Label(frame_plataforma, text="Tetris", image=image7, compound="top", font=("Arial", 10))
label7.grid(row=0, column=2, padx=5, pady=5)

button_favoritos7 = tk.Button(frame_plataforma, text="Adicionar aos Favoritos", font=("Arial", 7),background="#f0f0d8")
button_favoritos7.grid(row=1, column=2, padx=5, pady=5)

button_download7 = tk.Button(frame_plataforma, text="Download", font=("Arial", 7),background="#f0f0d8")
button_download7.grid(row=2, column=2, padx=5, pady=5)

# Contra
label8 = tk.Label(frame_plataforma, text="Contra", image=image8, compound="top", font=("Arial", 10))
label8.grid(row=0, column=3, padx=5, pady=5)

button_favoritos8 = tk.Button(frame_plataforma, text="Adicionar aos Favoritos", font=("Arial", 7),background="#f0f0d8")
button_favoritos8.grid(row=1, column=3, padx=5, pady=5)

button_download8 = tk.Button(frame_plataforma, text="Download", font=("Arial", 7),background="#f0f0d8")
button_download8.grid(row=2, column=3, padx=5, pady=5)

# Sonic
label9 = tk.Label(frame_plataforma, text="Sonic", image=image9, compound="top", font=("Arial", 10))
label9.grid(row=0, column=4, padx=5, pady=5)

button_favoritos9 = tk.Button(frame_plataforma, text="Adicionar aos Favoritos", font=("Arial", 7),background="#f0f0d8")
button_favoritos9.grid(row=1, column=4, padx=5, pady=5)

button_download9 = tk.Button(frame_plataforma, text="Download", font=("Arial", 7),background="#f0f0d8")
button_download9.grid(row=2, column=4, padx=5, pady=5)

# Título de Jogos FPS
label_titulo_fps = tk.Label(frame_principal, text="Jogos FPS", compound="top", background="#f0f0d8", font=("Arial Black", 9))
label_titulo_fps.grid(row=4, column=0, padx=5, pady=5, columnspan=5, sticky="nw")

# Frame para os jogos FPS
frame_fps = tk.Frame(frame_principal, background="#789048")
frame_fps.grid(row=5, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")

# ARK
label11 = tk.Label(frame_fps, text="ARK", image=image11, compound="top", font=("Arial", 10))
label11.grid(row=0, column=0, padx=5, pady=5)

button_favoritos11 = tk.Button(frame_fps, text="Adicionar aos Favoritos", font=("Arial", 7),background="#f0f0d8")
button_favoritos11.grid(row=1, column=0, padx=5, pady=5)

button_download11 = tk.Button(frame_fps, text="Download", font=("Arial", 7),background="#f0f0d8")
button_download11.grid(row=2, column=0, padx=5, pady=5)

# Apex Legends
label12 = tk.Label(frame_fps, text="Apex Legends", image=image12, compound="top", font=("Arial", 10))
label12.grid(row=0, column=1, padx=5, pady=5)

button_favoritos12 = tk.Button(frame_fps, text="Adicionar aos Favoritos", font=("Arial", 7),background="#f0f0d8")
button_favoritos12.grid(row=1, column=1, padx=5, pady=5)

button_download12 = tk.Button(frame_fps, text="Download", font=("Arial", 7),background="#f0f0d8")
button_download12.grid(row=2, column=1, padx=5, pady=5)

# DayZ
label13 = tk.Label(frame_fps, text="DayZ", image=image13, compound="top", font=("Arial", 10))
label13.grid(row=0, column=2, padx=5, pady=5)

button_favoritos13 = tk.Button(frame_fps, text="Adicionar aos Favoritos", font=("Arial", 7),background="#f0f0d8")
button_favoritos13.grid(row=1, column=2, padx=5, pady=5)

button_download13 = tk.Button(frame_fps, text="Download", font=("Arial", 7),background="#f0f0d8")
button_download13.grid(row=2, column=2, padx=5, pady=5)

# Team Fortress 2
label14 = tk.Label(frame_fps, text="Team Fortress 2", image=image14, compound="top", font=("Arial", 10))
label14.grid(row=0, column=3, padx=5, pady=5)

button_favoritos14 = tk.Button(frame_fps, text="Adicionar aos Favoritos", font=("Arial", 7),background="#f0f0d8")
button_favoritos14.grid(row=1, column=3, padx=5, pady=5)

button_download14 = tk.Button(frame_fps, text="Download", font=("Arial", 7),background="#f0f0d8")
button_download14.grid(row=2, column=3, padx=5, pady=5)

# PUBG
label15 = tk.Label(frame_fps, text="PUBG", image=image15, compound="top", font=("Arial", 10))
label15.grid(row=0, column=4, padx=5, pady=5)

button_favoritos15 = tk.Button(frame_fps, text="Adicionar aos Favoritos", font=("Arial", 7),background="#f0f0d8")
button_favoritos15.grid(row=1, column=4, padx=5, pady=5)

button_download15 = tk.Button(frame_fps, text="Download", font=("Arial", 7),background="#f0f0d8")
button_download15.grid(row=2, column=4, padx=5, pady=5)

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