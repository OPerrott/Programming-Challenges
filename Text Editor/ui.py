from settings import Settings

from tkinter import *   # For the application window
from tkinter import ttk # For the application window

import os

class UI:
    def __init__(self):
        self.draw_display()

    def draw_display(self):
        self.display = Tk()
        self.display.geometry(Settings.display_size(self.display))
        self.display.configure(background='#2b2b2b')
        
        self.display.mainloop()



if __name__ == '__main__':
    os.system('clear')

    UI()