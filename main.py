import tkinter as tk

class App(tk.Tk):

    def __init__(self):
        super().__init__()

        #Geometry of window
        self.height = 600
        self.width = 900
        self.geometry('900x600')
        self.minsize(300, 200)

        self.title('Discord Unix Timestamp Creator')
        self.font = ("Rubik", 15, "normal")

        self.bind("<Configure>", self.resize)


        self.date_frame = tk.Frame(master=self, bg='#333333', width=(900-40)/2)
        self.date_frame.grid(row=0, column=0, padx=10, pady=10)

        self.time_frame = tk.Frame(master=self, bg='#333333', width=(900-40)/2)
        self.time_frame.grid(row=0, column=1, padx=10, pady=10)

    #Widget resizing if window resizes
    def resize(self, event):
        if(event.widget == self and (self.width != event.width or self.height != event.height)):
            self.height = event.height
            self.width = event.width

            self.date_frame.config(width=round((event.width-40)/2))
            self.time_frame.config(width=round((event.width-40)/2))


#Main function
if __name__ == '__main__':
    app = App()

    app.mainloop()