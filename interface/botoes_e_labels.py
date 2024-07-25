import tkinter as tk
#BOTÕES
def cria_button_fav(parent,row,column,padx,pady):
    button_favoritos = tk.Button(parent, text="Adicionar nos favoritos", font=("Arial", 7),background="#cdcfb7")
    button_favoritos.grid(row=row, column=column, padx=padx, pady=pady)
    button_favoritos.bind("<Enter>", entrada_do_mouse)
    button_favoritos.bind("<Leave>", saida_do_mouse)

def cria_button_download(parent,row,column,padx,pady):
    button_download = tk.Button(parent, text="Download", font=("Arial", 7),background="#cdcfb7")
    button_download.grid(row=row, column=column, padx=padx, pady=pady)
    button_download.bind("<Enter>", entrada_do_mouse)
    button_download.bind("<Leave>", saida_do_mouse)
#LABELS
def cria_label_jogo(parent,text,image,row,column,padx,pady):
    label = tk.Button(parent, text=text, image=image, compound="top", font=("Arial", 10),background="#cdcfb7")
    label.grid(row=row, column=column, padx=padx, pady=pady)
    label.bind("<Enter>", entrada_do_mouse)
    label.bind("<Leave>", saida_do_mouse)

def cria_label_subtitulo(parent,text,row,column,padx,pady):
    label_subtitulo = tk.Label(parent, text=text, compound="top", background="#cdcfb7", font=("Arial Black", 9))
    label_subtitulo.grid(row=row, column=column, padx=padx, pady=pady,columnspan=5, sticky="nw")
    label_subtitulo.bind("<Enter>", entrada_do_mouse)
    label_subtitulo.bind("<Leave>", saida_do_mouse)

def cria_label_titulo(parent,text,row,column,columnspan):
    label_titulo = tk.Label(parent, text=text, font=("Arial Black", 16), background="#cdcfb7")
    label_titulo.grid(row=row, column=column, columnspan=columnspan, pady=(10, 5), sticky="n")
    label_titulo.bind("<Enter>", entrada_do_mouse)
    label_titulo.bind("<Leave>", saida_do_mouse)

def cria_frame(parent,background,columnspan,row,column,padx,pady):
    frame = tk.Frame(parent, background=background)
    frame.grid(row=row, column=column,columnspan=columnspan, padx=padx, pady=pady,sticky="nw")
    frame.bind("<Enter>", entrada_do_mouse)
    frame.bind("<Leave>", saida_do_mouse)

def entrada_do_mouse(event):
    event.widget.config(bg='#d9f4ff')

def saida_do_mouse(event):
    event.widget.config(bg='#cdcfb7')

