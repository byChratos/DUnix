import tkinter as tk

class App(tk.Tk):

    def __init__(self):
        super().__init__()

        #Colors
        self.dark_grey = '#2b2d31'
        self.light_grey = '#313338'
        self.lighter_grey = '#3a3c40'

        self.green = '#2bbf6c'
        self.dark_green = '#23a55a'
        self.light_green = '#31ea7f'

        self.white = '#dbdee1'

        self.blue = '#4752c4'
        self.light_blue = '#5c6aff'
        self.lighter_blue = '#635cff'



        self.debug_blue = '#323ea8'
        self.debug_red = '#c42142'
        self.debug_pink = '#e37f93'

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

        self.date_label = tk.Label(master=self.date_frame, text='Date', font=("Rubik", round((600/100)*4), "normal"), background=self.light_grey, bd=0, fg=self.white)
        self.date_label.grid(row=0, column=0, padx=8, pady=8)

        #Frame for time input
        self.time_frame = tk.Frame(master=self, bg=self.light_grey, width=(900-40)/2, height=round((600/100)*52-20))
        self.time_frame.grid_propagate(0)
        self.time_frame.grid(row=0, column=1, padx=10, pady=10)

        self.time_label = tk.Label(master=self.time_frame, text='Time', font=("Rubik", round((600/100)*4), "normal"), background=self.light_grey, bd=0, fg=self.white)
        self.time_label.grid(row=0, column=0, padx=8, pady=8)



        #Frame for the argument
        self.arg_frame = tk.Frame(master=self, bg=self.light_grey, width=(900-20), height=round((600/100)*33-20))
        self.arg_frame.grid_propagate(0)
        self.arg_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        #Frame for arg label
        self.arg_label_frame = tk.Frame(master=self.arg_frame, bg=self.light_grey, width=(900-20), height=round(((600/100)*33-20)/3))
        self.arg_label_frame.grid_propagate(0)
        self.arg_label_frame.grid(row=0, column=0, padx=0, pady=0)

        #Arg label
        self.arg_label = tk.Label(master=self.arg_label_frame, text='Type', font=("Rubik", round((600/100)*4), "normal"), background=self.light_grey, bd=0, fg=self.white, justify='left')
        self.arg_label.grid(row=0, column=0, padx=5, pady=5, sticky='wn')

        #Frame for radio button frames
        self.radio_frame = tk.Frame(master=self.arg_frame, bg=self.light_grey, width=(900-40), height=round((600/100)*33-60))
        self.radio_frame.grid_propagate(0)
        self.radio_frame.grid(row=1, column=0, padx=10, pady=0)

        #Arguments:
        #<t:1543392060> default                 28 November 2018 09:01
        #<t:1543392060:t> short time            09:01
        #<t:1543392060:T> long time             09:01:00
        #<t:1543392060:d> short date            28/11/2018
        #<t:1543392060:D> long date             28 November 2018
        #<t:1543392060:f> short datetime        28 November 2018 09:01
        #<t:1543392060:F> long datetime         Wednesday, 28 November 2018 09:01
        #<t:1543392060:R> relative              3 years ago
        #https://gist.github.com/LeviSnoot/d9147767abeef2f770e9ddcd91eb85aa


        #Radio button frames
        self.radio_button_frames = []
        c = 0
        r = 0
        for i in range(8):
            self.radio_button_frames.append(tk.Frame(master=self.radio_frame, padx=0, pady=0, width=(900-40)/4, height=round(((600/100)*33-20)/3), bg=self.green))
            self.radio_button_frames[i].pack_propagate(0)
            if (i==4):
                c = 0
                r = 1
            self.radio_button_frames[i].grid(row=r, column = c, padx=0, pady=0)
            c += 1


        #Radio buttons
        test = [('Default', 'default'), ('Short Time', 't'), ('Long Time', 'T'), ('Short Date', 'd'), ('Long Date', 'D'), ('Short Date/Time', 'f'), ('Long Date/Time', 'F'), ('Relative', 'R')]
        self.buttons = []
        self.selection = tk.StringVar()
        self.selection.set('default')

        #Creation of radio buttons
        i = 0
        for (name, value) in test:
            master = self.radio_button_frames[i]
            self.buttons.append(tk.Radiobutton(master=master, padx=0, pady=0, width=20, font=("Rubik", 12, "normal"), bd=0, text=name, value=value, variable=self.selection, indicatoron=0, bg=self.light_grey, fg=self.white, selectcolor=self.light_blue, activebackground=self.blue, activeforeground=self.white))
            self.buttons[i].pack(fill='both', expand=1)

            self.buttons[i].bind("<Enter>", self.on_enter_radio)
            self.buttons[i].bind("<Leave>", self.on_leave_radio)

            i+=1





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
            self.arg_label_frame.config(width=event.width-20, height=round(((event.height/100)*33-20)/3))

            self.button_frame.config(width=event.width-20, height=round((event.height/100)*15-20))

            self.radio_frame.config(width=event.width-40, height=round(((event.height/100)*33-20)/3*2))

            for frame in self.radio_button_frames:
                frame.config(width=round((event.width-40)/4), height=round(((event.height/100)*33-20)/3))

    #Button hover color
    def on_enter(self, event):
        self.create_button.config(bg=self.light_green)

    #Button change color back to normal
    def on_leave(self, event):
        self.create_button.config(bg=self.green)

    #Radio button hover color
    def on_enter_radio(self, event):
        event.widget['bg'] = self.lighter_grey
        event.widget['selectcolor'] = self.lighter_blue

    #Radio button change color back to normal
    def on_leave_radio(self, event):
        event.widget['bg'] = self.light_grey
        event.widget['selectcolor'] = self.light_blue


    #Create button logic
    def create(self):
        print(self.selection.get())


#Main function
if __name__ == '__main__':
    app = App()
    app.mainloop()