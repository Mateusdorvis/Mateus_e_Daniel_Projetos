import tkinter as tk

class Aplicativo:
    def __init__(self, root):
        self.root = root
        self.root.title("Trocar Cor com Hover")

        # Define as cores
        self.cor_normal = "lightblue"
        self.cor_hover = "lightcoral"

        # Cria um botão
        self.botao = tk.Button(self.root, text="Passe o mouse sobre mim", bg=self.cor_normal, relief=tk.RAISED, height=2, width=20)
        self.botao.pack(pady=20)

        # Associa os eventos de hover com as funções
        self.botao.bind("<Enter>", self.entrar)
        self.botao.bind("<Leave>", self.sair)

    def entrar(self, event):
        """Altera a cor do botão quando o mouse entra."""
        self.botao.config(bg=self.cor_hover)

    def sair(self, event):
        """Altera a cor do botão quando o mouse sai."""
        self.botao.config(bg=self.cor_normal)

def main():
    root = tk.Tk()
    app = Aplicativo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
