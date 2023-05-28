import tkinter as tk

class App(tk.Tk):

    def __init__(self):
        super().__init__()

        #Geometry of window
        self.height = 600
        self.width = 900
        self.geometry('900x600')
        self.minsize(600, 350)

        self.title('Discord Unix Timestamp Creator')
        self.font = ("Rubik", 15, "normal")

        self.bind("<Configure>", self.resize)


        #Frame for Date input
        self.date_frame = tk.Frame(master=self, bg='#333333', width=(900-40)/2, height=280)
        self.date_frame.grid(row=0, column=0, padx=10, pady=10)

        #Frame for Time input
        self.time_frame = tk.Frame(master=self, bg='#333333', width=(900-40)/2, height=280)
        self.time_frame.grid(row=0, column=1, padx=10, pady=10)

        #Frame for the argument
        self.arg_frame = tk.Frame(master=self, bg='#333333', width=(900-20), height=180)
        self.arg_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        #Frame for the "CREATE" Button
        self.button_frame = tk.Frame(master=self, bg='#333333', width=(900-20), height=80)
        self.button_frame.pack_propagate(0)
        self.button_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.create_button = tk.Button(master=self.button_frame, text='Create', command=self.create)
        self.create_button.pack(fill='both', expand=1)

    def create(self):
        print("test")

    #Widget resizing if window resizes
    def resize(self, event):
        if(event.widget == self and (self.width != event.width or self.height != event.height)):
            self.height = event.height
            self.width = event.width

            self.date_frame.config(width=round((event.width-40)/2), height=round((event.height/100)*52-20))
            self.time_frame.config(width=round((event.width-40)/2), height=round((event.height/100)*52-20))
            self.arg_frame.config(width=event.width-20, height=round((event.height/100)*33-20))
            self.button_frame.config(width=event.width-20, height=round((event.height/100)*15-20))


#Main function
if __name__ == '__main__':
    app = App()

    app.mainloop()