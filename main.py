import tkinter as tk
import datetime
import time
from calendar import month_name, monthrange

# ! Change to values depending on what years you want to see in the OptionMenu
# ! YEARS_PAST has to be negative
YEARS_PAST = -15
YEARS_FUTURE = 25

class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.popup_active = False

        self.month_list: list = []
        for month in month_name:
            if month == '':
                continue
            else:
                self.month_list.append(month)

        # * Colors
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




        # * Geometry of window
        self.height = 600
        self.width = 900
        self.geometry('900x600')
        self.minsize(650, 350)

        self.configure(background=self.dark_grey)

        self.title('DUnix Timestamp Generator for Discord')
        self.font = ("Rubik", 15, "bold")

        #Bind resize function for dynamic resizing of widgets
        self.bind("<Configure>", self.resize)
        self.iconbitmap("favicon.ico")
        




        # * Frame for date input
        self.date_frame = tk.Frame(master=self, bg=self.light_grey, width=(900-40)/2, height=round((600/100)*52-20))
        self.date_frame.grid_propagate(0)
        self.date_frame.grid(row=0, column=0, padx=10, pady=10)

        self.date_label = tk.Label(master=self.date_frame, text='Date', font=("Rubik", round((600/100)*4), "normal"), background=self.light_grey, bd=0, fg=self.white)
        self.date_label.grid(row=0, column=0, padx=8, pady=8)


        # ! Day
        self.dayList: list = []
        for i in range(32):
            if i == 0:
                continue
            else:
                self.dayList.append(i)

        menu_width = round((((900-40)/2)-60)/3)

        self.day_frame = tk.Frame(master=self.date_frame, padx=0, pady=0, width=menu_width, height=50, bg=self.light_blue)
        self.day_frame.pack_propagate(0)
        self.day_frame.grid(row=1, column=0, padx=10, pady=10)


        self.day = tk.StringVar()
        self.day_menu = tk.OptionMenu(self.day_frame, self.day, *self.dayList)
        self.day.set("1")

        self.day_menu.config(bg=self.light_blue, fg=self.white, border=0, borderwidth=0, activebackground=self.lighter_blue, activeforeground=self.white, highlightthickness=0, indicatoron=0, font=("Rubik", 12, "normal"), cursor="hand2")

        self.day_menu.pack(fill="both", expand=1)


        # ! Month
        self.month_frame = tk.Frame(master=self.date_frame, padx=0, pady=0, width=menu_width, height=50, bg=self.light_blue)
        self.month_frame.pack_propagate(0)
        self.month_frame.grid(row=1, column=1, padx=10, pady=10)

        self.month = tk.StringVar()
        self.month_menu = tk.OptionMenu(self.month_frame, self.month, *self.month_list, command=self.redoDay)
        self.month.set(self.month_list[0])

        self.month_menu.config(bg=self.light_blue, fg=self.white, border=0, borderwidth=0, activebackground=self.lighter_blue, activeforeground=self.white, highlightthickness=0, indicatoron=0, font=("Rubik", 12, "normal"), cursor="hand2")

        self.month_menu.pack(fill="both", expand=1)

        # ! Year
        self.yearList: list = []
        today = datetime.date.today()
        thisYear = today.year

        for i in range(YEARS_PAST, YEARS_FUTURE):
            # ! appends all years in a range of year years from today (15 years past - 25 years future)
            self.yearList.append(thisYear + i)


        self.year_frame = tk.Frame(master=self.date_frame, padx=0, pady=0, width=menu_width, height=50, bg=self.light_blue)
        self.year_frame.pack_propagate(0)
        self.year_frame.grid(row=1, column=2, padx=10, pady=10)

        self.year = tk.StringVar()
        self.year_menu = tk.OptionMenu(self.year_frame, self.year, *self.yearList, command=self.redoDay)
        self.year.set(thisYear)

        self.year_menu.config(bg=self.light_blue, fg=self.white, border=0, borderwidth=0, activebackground=self.lighter_blue, activeforeground=self.white, highlightthickness=0, indicatoron=0, font=("Rubik", 12, "normal"), cursor="hand2")

        self.year_menu.pack(fill="both", expand=1)





        # * Frame for time input
        self.time_frame = tk.Frame(master=self, bg=self.light_grey, width=(900-40)/2, height=round((600/100)*52-20))
        self.time_frame.grid_propagate(0)
        self.time_frame.grid(row=0, column=1, padx=10, pady=10)

        self.time_label = tk.Label(master=self.time_frame, text='Time', font=("Rubik", round((600/100)*4), "normal"), background=self.light_grey, bd=0, fg=self.white)
        self.time_label.grid(row=0, column=0, padx=8, pady=8)



        # ! Hour
        self.hour_frame = tk.Frame(master=self.time_frame, padx=0, pady=0, width=menu_width, height=50, bg=self.light_blue)
        self.hour_frame.pack_propagate(0)
        self.hour_frame.grid(row=2, column=0, padx=10, pady=10)

        self.hour_list: list = []
        for i in range(24):
            self.hour_list.append(i)

        vcmd_hour = (self.register(self.validate_hour))
        self.hour_entry = tk.Entry(master=self.hour_frame, validate="all", validatecommand=(vcmd_hour, '%P'))
        self.hour_entry.config(bg=self.light_blue, fg=self.white, border=0, borderwidth=0, selectbackground=self.dark_grey, selectforeground=self.white, justify="center", font=("Rubik", 12, "normal"))

        # * Default text
        self.hour_entry.placeholder = "Hour"
        self.hour_entry.insert("end", self.hour_entry.placeholder)

        self.hour_entry.pack(fill="both", expand=1)

        self.hour_entry.bind("<FocusIn>", self.remove_placeholder)
        self.hour_entry.bind("<FocusOut>", self.add_placeholder)

        # ! Minute
        self.minute_frame = tk.Frame(master=self.time_frame, padx=0, pady=0, width=menu_width, height=50, bg=self.light_blue)
        self.minute_frame.pack_propagate(0)
        self.minute_frame.grid(row=2, column=1, padx=10, pady=10)

        self.minute_and_second_list: list = []
        for i in range(60):
            self.minute_and_second_list.append(i)

        vcmd_minute = (self.register(self.validate_minute))
        self.minute_entry = tk.Entry(master=self.minute_frame, validate="all", validatecommand=(vcmd_minute, '%P'))
        self.minute_entry.config(bg=self.light_blue, fg=self.white, border=0, borderwidth=0, selectbackground=self.dark_grey, selectforeground=self.white, justify="center", font=("Rubik", 12, "normal"))

        # * Default text
        self.minute_entry.placeholder = "Minutes"
        self.minute_entry.insert("end", self.minute_entry.placeholder)

        self.minute_entry.pack(fill="both", expand=1)

        self.minute_entry.bind("<FocusIn>", self.remove_placeholder)
        self.minute_entry.bind("<FocusOut>", self.add_placeholder)

        # ! Second
        self.second_frame = tk.Frame(master=self.time_frame, padx=0, pady=0, width=menu_width, height=50, bg=self.light_blue)
        self.second_frame.pack_propagate(0)
        self.second_frame.grid(row=2, column=2, padx=10, pady=10)

        vcmd_second = (self.register(self.validate_second))
        self.second_entry = tk.Entry(master=self.second_frame, validate="all", validatecommand=(vcmd_second, '%P'))
        self.second_entry.config(bg=self.light_blue, fg=self.white, border=0, borderwidth=0, selectbackground=self.dark_grey, selectforeground=self.white, justify="center", font=("Rubik", 12, "normal"))

        # * Default text
        self.second_entry.placeholder = "Seconds"
        self.second_entry.insert("end", self.second_entry.placeholder)

        self.second_entry.pack(fill="both", expand=1)

        self.second_entry.bind("<FocusIn>", self.remove_placeholder)
        self.second_entry.bind("<FocusOut>", self.add_placeholder)


        # * Frame for the argument
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


        # * Radio button frames
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


        # * Radio buttons
        test = [('Default', 'default'), ('Short Time', 't'), ('Long Time', 'T'), ('Short Date', 'd'), ('Long Date', 'D'), ('Short Date/Time', 'f'), ('Long Date/Time', 'F'), ('Relative', 'R')]
        self.buttons = []
        self.selection = tk.StringVar()
        self.selection.set('default')

        # * Creation of radio buttons
        i = 0
        for (name, value) in test:
            master = self.radio_button_frames[i]
            self.buttons.append(tk.Radiobutton(master=master, padx=0, pady=0, width=20, font=("Rubik", 12, "normal"), bd=0, text=name, value=value, variable=self.selection, indicatoron=0, bg=self.light_grey, fg=self.white, selectcolor=self.light_blue, activebackground=self.blue, activeforeground=self.white, cursor="hand2"))
            self.buttons[i].pack(fill='both', expand=1)

            self.buttons[i].bind("<Enter>", self.on_enter_radio)
            self.buttons[i].bind("<Leave>", self.on_leave_radio)

            i+=1





        # * Frame for the "CREATE" button
        self.button_frame = tk.Frame(master=self, bg=self.green, width=(900-20), height=round((600/100)*15-20))
        self.button_frame.pack_propagate(0)
        self.button_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # * Create button
        self.create_button = tk.Button(master=self.button_frame, text='Create', command=self.create, bg=self.green, fg=self.dark_grey, bd=0, activebackground=self.dark_green, activeforeground=self.dark_grey, font=self.font, cursor="hand2")
        self.create_button.pack(fill='both', expand=1)

        #Bind enter and leave events to functions for the hover color change
        self.create_button.bind("<Enter>", self.on_enter)
        self.create_button.bind("<Leave>", self.on_leave)

    def validate_hour(self, P):
        if P == "Hour" or (str.isdigit(P) and (int(P) in self.hour_list)) or P == "":
            return True
        else:
            self.popup("Invalid input for Hour.", "Error")
            return False
        
    def validate_minute(self, P):
        if P == "Minutes" or (str.isdigit(P) and (int(P) in self.minute_and_second_list)) or P == "":
            return True
        else:
            self.popup("Invalid input for Minute", "Error")
            return False
        
    def validate_second(self, P):
        if P == "Seconds" or (str.isdigit(P) and (int(P) in self.minute_and_second_list)) or P == "":
            return True
        else:
            self.popup("Invalid input for Second", "Error")
            return False

    # * Close popup function
    def close_popup(self):
        self.popup_active = False
        self.pp.destroy()

    # * Placeholders for the Entries
    def remove_placeholder(self, event):
            placeholder_text = getattr(event.widget, "placeholder", "")
            if placeholder_text and event.widget.get() == placeholder_text:
                event.widget.delete(0, "end")

    def add_placeholder(self, event):
        placeholder_text = getattr(event.widget, "placeholder", "")
        if placeholder_text and event.widget.get() == "":
            event.widget.insert(0, placeholder_text)

    # * Change the list of days available in the day OptionMenu
    def redoDay(self, selected):
        selected_day = self.day.get()

        # * Clear old day optionMenu
        self.day_menu.pack_forget()
        self.dayList.clear()

        # * Get month and number of days in the month of the currently selected year
        month_number = self.month_list.index(self.month.get()) + 1
        number_of_days_in_month = monthrange(year=int(self.year.get()), month=month_number)[1]

        # * Generate new dayList
        for i in range(number_of_days_in_month + 1):
            if i == 0:
                continue
            else:
                self.dayList.append(i)

        # * Create new optionMenu
        self.day = tk.StringVar()
        self.day_menu = tk.OptionMenu(self.day_frame, self.day, *self.dayList)

        if int(selected_day) in self.dayList:
            self.day.set(selected_day)
        else:
            self.day.set("1")

        self.day_menu.config(bg=self.light_blue, fg=self.white, border=0, borderwidth=0, activebackground=self.lighter_blue, activeforeground=self.white, highlightthickness=0, indicatoron=0, font=("Rubik", 12, "normal"))

        self.day_menu.pack(fill="both", expand=1)

    # * Change hover color on okay button
    def on_enter_okay(self, event):
        event.widget['bg'] = self.lighter_blue

    def on_leave_okay(self, event):
        event.widget['bg'] = self.light_blue

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


            menu_width = round((((event.width-40)/2)-60)/3)
            self.day_frame.config(width=menu_width)
            self.month_frame.config(width=menu_width)
            self.year_frame.config(width=menu_width)

            self.hour_frame.config(width=menu_width)
            self.minute_frame.config(width=menu_width)
            self.second_frame.config(width=menu_width)

    def resize_popup(self, event):
        if(event.widget == self.pp and (self.pp.width != event.width or self.pp.height != event.height)):
            self.pp.height = event.height
            self.pp.width = event.width

            self.pp_button_frame.config(width=event.width)
            self.pp_text_frame.config(width=event.width, height=event.height-50)

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

    def popup(self, text, title):
        if self.popup_active:
            return

        self.popup_active = True

        self.pp = tk.Toplevel()
        self.pp.wm_title(title)
        self.pp.protocol("WM_DELETE_WINDOW", self.close_popup)

        self.pp.iconbitmap("favicon.ico")

        self.pp.bind("<Configure>", self.resize_popup)

        self.pp.height = 150
        self.pp.width = 400
        self.pp.minsize(400, 150)

        self.pp_text_frame = tk.Frame(master=self.pp, width=400, height=100)
        self.pp_text_frame.pack_propagate(0)
        self.pp_text_frame.grid(row=0, column=0)

        self.pp_text_entry = tk.Entry(self.pp_text_frame)
        self.pp_text_entry.insert(0, text)
        self.pp_text_entry.config(state="readonly", readonlybackground=self.light_grey, fg=self.white, font=("Rubik", 12, "normal"), border=0, borderwidth=0, justify="center")
        self.pp_text_entry.pack(fill="both", expand=1)

        self.pp_button_frame = tk.Frame(master=self.pp, width=400, height=50, padx=0, pady=0)
        self.pp_button_frame.pack_propagate(0)
        self.pp_button_frame.grid(row=1, column=0)

        self.pp_b = tk.Button(self.pp_button_frame, text="Okay", command=self.close_popup, border=0, borderwidth=0, bg=self.light_blue, fg=self.white, font=("Rubik", 12, "normal"), activebackground=self.blue, activeforeground=self.white, cursor="hand2")
        self.pp_b.pack(fill="both", expand=1)

        self.pp_b.bind("<Enter>", self.on_enter_okay)
        self.pp_b.bind("<Leave>", self.on_leave_okay)

    #Create button logic
    def create(self):
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

        day = self.day.get()
        month = self.month.get()
        year = self.year.get()

        hour = self.hour_entry.get()
        minute = self.minute_entry.get()
        second = self.second_entry.get()

        if hour == "Hour" or minute == "Minutes" or second == "Seconds" or hour == '' or minute == '' or second == '':
            self.popup("You have to specify Hour, Minutes and Seconds", "Error")
            return

        selection = self.selection.get()

        date_time = datetime.datetime(int(year), self.month_list.index(month)+1, int(day), int(hour), int(minute), int(second))
        unix = str(int(time.mktime(date_time.timetuple())))

        if selection == "default":
            unix_string = f"<t:{unix}>"
        else:
            unix_string = f"<t:{unix}:{selection}>"

        self.popup(f"Your unix timestamp is: {unix_string}", "DUnix")


# * Main function
if __name__ == '__main__':
    app = App()
    app.mainloop()