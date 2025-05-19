from tkinter import *   # For the application window
from tkinter import ttk # For the application window

class App:
    def __init__(self):
        self.bootup()
        
    def bootup(self):
        self.draw_display()

    def draw_display(self):
        self.display = Tk()
        self.display.geometry()
        self.display.configure(background='#00FF00')
        
        self.display.mainloop()        
        
if __name__ == '__main__':
    App()