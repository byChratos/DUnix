import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('900x600')
        self.title('Discord Unix Timestamp Creator')
        self.minsize(300, 200)

if __name__ == '__main__':
    app = App()
    app.mainloop()