from settings import Settings

from tkinter import *   # For the application window
from tkinter import ttk # For the application window

class UI:
    def __init__(self):
        self.draw_display()

    def draw_display(self):
        self.display = Tk()
        self.display.geometry(Settings.display_size(self.display))
        self.display.configure(background='#2b2b2b')
        
        self.display.overrideredirect(True)
        title_bar = Frame(self.display, bg='#2b2b2b', relief='raised', bd=2)
        close_button = Button(self.display, text='X', command=self.display.destroy, bg='white', fg='red')


        title_bar.pack(expand=1, fill='x')
        close_button.pack(side='right')
        
        
        self.display.mainloop()
