from lib import *

class Settings:
    def __init__(self):
        
        self.SCREEN_HEIGHT = None
        self.SCREEN_WIDTH = None
        
        self.SCREEN_POSX = None
        self.SCREEN_POSY = None
        
        self.SCREEN_COLOUR = None
        
        self.load_settings()
        
        
    def load_settings(self):
        with open('Data/data.txt', 'r') as file:
            settings = [lines.strip() for lines in file]
            
        for setting in settings:
            print(setting)
            
    
    def display_size(display):
        SCREEN_HEIGHT, SCREEN_WIDTH = display.winfo_screenheight(), display.winfo_screenwidth()
    
        return f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}"

if __name__ == '__main__':
    Settings()