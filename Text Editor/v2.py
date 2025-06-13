from settings import *

import tkinter
import os


class Main:
    def __init__(self):
        self.run()

    def run(self):
        Settings()
        App()

class App(Settings_Vars):
    def __init__(self):
        super().__init__()

        self.init_window()
        Graphics(self.window)
        
    
    def init_window(self):
        self.window = tkinter.Tk()
  
        self.window.geometry(f"{Settings_Vars.WINDOW_WIDTH}x{Settings_Vars.WINDOW_HEIGHT}+{Settings_Vars.WINDOW_POSX}+{Settings_Vars.WINDOW_POSY}")
        self.window.configure(background=f"{self.WINDOW_COLOUR}")

        self.window.mainloop()
        print("Test")

class Graphics:
    def __init__(self, window):
        self.window = window
        
        self.cmd_line()
    
    def cmd_line(self):
        self.text = tkinter.Entry(self.window, background="#FFFFFF")
        self.text.place(x=50, y=50)

if __name__ == "__main__":

    os.system('cls')

    Main()