import tkinter as tk
from controller.main_c import MainController

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Jogo")
        self.geometry("300x300")
        self._frame = None
        self.switch_frame(Main)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class Main(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Aplicativo de Jogos", font=("Helvetica", 18, "bold")).pack(
            anchor="center",fill="x"
        )
        tk.Button(
            self, text="Login", command=lambda: master.switch_frame(MainController.login)
        ).pack()
        tk.Button(
            self, text="Permanecer desconectado", command=lambda: master.switch_frame(SemLogin)
        ).pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()

