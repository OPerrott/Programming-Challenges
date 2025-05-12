from settings import Settings

from lib import *

class UI:
    def __init__(self):
        self.draw_display()

    def draw_display(self):
        self.display = Tk()
        self.display.geometry(Settings.display_size(self.display))
        self.display.mainloop()