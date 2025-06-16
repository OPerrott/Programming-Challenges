from core.settings import *
from utils.colour_format import *
from gui.colours import *

import tkinter
import os


class Window:
    def __init__(self):
        self.run()

    def run(self):
        Settings()
        App()

class App(Settings_Vars):
    def __init__(self):
        super().__init__()

        self.init_window()
        
    
    def init_window(self):
        self.window = tkinter.Tk()
  
        self.window.geometry(f"{Settings_Vars.WINDOW_WIDTH}x{Settings_Vars.WINDOW_HEIGHT}+{Settings_Vars.WINDOW_POSX}+{Settings_Vars.WINDOW_POSY}")
        self.window.configure(background=f"{self.WINDOW_COLOUR}")
        
        
        Graphics(self.window)

        self.window.mainloop()
    

class Graphics:
    def __init__(self, window):
        self.window = window
        
        self.cmd_line()
        
    def calculate_offset(self):
        ...
    
    
    def cmd_line(self):
        self.window.update_idletasks()

        self.calculate_offset()
        
        displayed: bool = True
        
        width: int = self.window.winfo_width()# - width_offset
        height: int = 20 #self.window.winfo_height() - height_offset                                     # Default height=20
        posx: int = 0                                      # Default posx=0
        posy: int = self.window.winfo_height() - height
        
        background: str = Colour_Format("#2B2B2B")
        foreground: str = Colour_Format(WHITE)
        
        border_width: int = 0
        
        submit_key: str = "<Return>"
        
        clear_command: bool = True                            # Default clear_command=True

        if displayed == True:
            
            self.command = tkinter.Entry(self.window, background=background, foreground=foreground, borderwidth=border_width)
            
            # Resize Element If Window Resized
            def update_position(event):
                self.command.place(width=width, height=height, x=posx, y=posy)
                
            self.window.bind("<Configure>", update_position)
            
            
        self.command.bind(submit_key, lambda event: 
        (
            Command_Line(self.command.get()),
            
            self.command.delete(0, tkinter.END) if clear_command else None
        ))

    

class Command_Line:
    def __init__(self, command):
        print(command)

if __name__ == "__main__":

    os.system('cls')

    Window()