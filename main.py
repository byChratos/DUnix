import customtkinter as ctk

ctk.set_appearance_mode('system')
ctk.set_default_color_theme('blue')

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.my_font = ctk.CTkFont(family="SF UI Text", size=12, weight='bold')

        self.geometry('900x600')
        self.title('Discord Unix Timestamp Creator')
        self.minsize(300, 200)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.button = ctk.CTkButton(self, text="Create", command=self.button_callback, font=self.my_font, text_color='white', fg_color='#2ea043', hover_color='#38c653')
        self.button.grid(row=1, column=0, padx=30, pady=10, sticky="nsew")

    def button_callback(self):
        print('button pressed')

if __name__ == '__main__':
    app = App()
    app.mainloop()