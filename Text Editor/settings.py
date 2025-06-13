import json
import os


class Settings_Vars:   
    # FILE LOCATION
    FILE = r"Text Editor\Data\settings.json"
    
    #WINDOW VARIABLES
    WINDOW_WIDTH = None
    WINDOW_HEIGHT = None
    WINDOW_RESOLUTION = None
    WINDOW_POSX = None
    WINDOW_POSY = None
    WINDOW_COLOUR = None
    

class Settings(Settings_Vars):
    def __init__(self):
        super().__init__()
        
        self.settings = {}

        self.read()
    
    def read(self):
        with open(f"{self.FILE}", 'r') as s:
            self.s = json.load(s)

        self.load()
    
    def load(self):
        self.settings = self.s["window"][0]
        
        
        for setting in self.settings:
        
            curr_setting = setting.replace('-', '_')
            if hasattr(Settings_Vars, curr_setting):
                setattr(Settings_Vars, curr_setting, self.settings[setting])

        
if __name__=='__main__':
    os.system('cls')
    
    Settings()