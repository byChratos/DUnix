import tkinter as tk

class App(tk.Tk):

    def __init__(self):
        super().__init__()

        #Colors
        self.dark_grey = '#2b2d31'
        self.light_grey = '#313338'
        self.green = '#2bbf6c'
        self.dark_green = '#23a55a'
        self.light_green = '#31ea7f'

        #Geometry of window
        self.height = 600
        self.width = 900
        self.geometry('900x600')
        self.minsize(600, 350)

        self.configure(background=self.dark_grey)

        self.title('Discord Unix Timestamp Creator')
        self.font = ("Rubik", 15, "bold")

        #Bind resize function for dynamic resizing of widgets
        self.bind("<Configure>", self.resize)



        #Frame for date input
        self.date_frame = tk.Frame(master=self, bg=self.light_grey, width=(900-40)/2, height=round((600/100)*52-20))
        self.date_frame.grid_propagate(0)
        self.date_frame.grid(row=0, column=0, padx=10, pady=10)

        self.date_label = tk.Label(master=self.date_frame, text='Date', font=("Rubik", round((600/100)*4), "normal"), background=self.light_grey, bd=0, fg='#dbdee1')
        self.date_label.grid(row=0, column=0, padx=8, pady=8)

        #Frame for time input
        self.time_frame = tk.Frame(master=self, bg=self.light_grey, width=(900-40)/2, height=round((600/100)*52-20))
        self.time_frame.grid_propagate(0)
        self.time_frame.grid(row=0, column=1, padx=10, pady=10)

        self.time_label = tk.Label(master=self.time_frame, text='Time', font=("Rubik", round((600/100)*4), "normal"), background=self.light_grey, bd=0, fg='#dbdee1')
        self.time_label.grid(row=0, column=0, padx=8, pady=8)



        #Frame for the argument
        self.arg_frame = tk.Frame(master=self, bg=self.light_grey, width=(900-20), height=round((600/100)*33-20))
        self.arg_frame.grid_propagate(0)
        self.arg_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.arg_label = tk.Label(master=self.arg_frame, text='Type', font=("Rubik", round((600/100)*4), "normal"), background=self.light_grey, bd=0, fg='#dbdee1')
        self.arg_label.grid(row=0, column=0, padx=8, pady=8)




        #Frame for the "CREATE" button
        self.button_frame = tk.Frame(master=self, bg=self.green, width=(900-20), height=round((600/100)*15-20))
        self.button_frame.pack_propagate(0)
        self.button_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        #Create button
        self.create_button = tk.Button(master=self.button_frame, text='Create', command=self.create, bg=self.green, fg=self.dark_grey, bd=0, activebackground=self.dark_green, activeforeground=self.dark_grey, font=self.font)
        self.create_button.pack(fill='both', expand=1)

        #Bind enter and leave events to functions for the hover color change
        self.create_button.bind("<Enter>", self.on_enter)
        self.create_button.bind("<Leave>", self.on_leave)

    #Widget resizing if window resizes
    def resize(self, event):
        if(event.widget == self and (self.width != event.width or self.height != event.height)):
            self.height = event.height
            self.width = event.width

            self.date_label.config(font=("Rubik", round((event.height/100)*4), "normal"))
            self.time_label.config(font=("Rubik", round((event.height/100)*4), "normal"))
            self.arg_label.config(font=("Rubik", round((event.height/100)*4), "normal"))

            self.date_frame.config(width=round((event.width-40)/2), height=round((event.height/100)*52-20))
            self.time_frame.config(width=round((event.width-40)/2), height=round((event.height/100)*52-20))
            self.arg_frame.config(width=event.width-20, height=round((event.height/100)*33-20))
            self.button_frame.config(width=event.width-20, height=round((event.height/100)*15-20))

    #Button hover color
    def on_enter(self, event):
        self.create_button.config(bg=self.light_green)

    #Button change color back to normal
    def on_leave(self, event):
        self.create_button.config(bg=self.green)

    #Create button logic
    def create(self):
        print("test")


#Main function
if __name__ == '__main__':
    app = App()
    app.mainloop()