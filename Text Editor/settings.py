from tkinter import *   # For the application window
from tkinter import ttk # For the application window

class Settings:
    def __init__(self):
        
        self.SCREEN_HEIGHT = None
        self.SCREEN_WIDTH = None
        
        self.SCREEN_POSX = None
        self.SCREEN_POSY = None
        
        self.SCREEN_COLOUR = None
        
        self.load_settings()
        
        
    def load_settings(self):
        try:
            with open('Text Editor/Data/data.txt', 'r') as file:
                for line in file:
                    line = line.strip()
                    if not line:    # If the line is empty
                        continue
                    key, value = line.split(':')
                    key = key.strip()
                    value = value.strip()

                    if key == 'DISPLAY_DIMENSIONS':
                        width, height = value.split(',')
                        self.SCREEN_WIDTH = int(width.strip())
                        self.SCREEN_HEIGHT = int (height.strip())
                    elif key == 'DISPLAY_POSITION':
                        x, y = value.split(',')
                        self.SCREEN_POSX = int(x.strip())
                        self.SCREEN_POSY = int(y.strip())
                    elif key == 'DISPLAY_COLOUR':
                        self.SCREEN_COLOUR = value
        except FileNotFoundError:
            print(f"[ERROR] {self.data_file_path} not found!")
        except ValueError:
            print(f'[ERROR] Invalid Format in {self.data_file_path}')
            
    
    def display_size(display):
        SCREEN_HEIGHT, SCREEN_WIDTH = display.winfo_screenheight(), display.winfo_screenwidth()
    
        return f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}"

if __name__ == '__main__':
    Settings()