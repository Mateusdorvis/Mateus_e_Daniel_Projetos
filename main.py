import tkinter as tk
class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Jogo App")
        self.geometry("400x400")
        

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
