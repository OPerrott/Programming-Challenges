from settings import Settings
from ui import UI

from lib import *

class App:
    def __init__(self):
        self.bootup()
        
    def bootup(self):
        UI.draw_display(self)
        
        
if __name__ == '__main__':
    App()