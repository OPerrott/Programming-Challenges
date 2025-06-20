from utils.file_io import *
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
        
        self.window_settings = File_IO(file_path=self.FILE)["window"][0]
        self.ld_wnd()
    
    
    def ld_wnd(self):
        for setting in self.window_settings:
        
            curr_setting = setting.replace('-', '_')
            if hasattr(Settings_Vars, curr_setting):
                setattr(Settings_Vars, curr_setting, self.window_settings[setting])

        
if __name__=='__main__':
    os.system('cls')
    
    Settings()