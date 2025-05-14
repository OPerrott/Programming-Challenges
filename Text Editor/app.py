from settings import Settings
from ui import UI

from tkinter import *   # For the application window
from tkinter import ttk # For the application window

class App:
    def __init__(self):
        self.bootup()
        
    def bootup(self):
        UI.draw_display(self)
        
        
if __name__ == '__main__':
    App()