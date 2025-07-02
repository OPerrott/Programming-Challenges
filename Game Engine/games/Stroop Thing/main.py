import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from menu import Menu
import pygame




class Main:
    def __init__(self, console_data):
        self.console_data = console_data
        self.window = self.console_data.window

        Menu(self)

if __name__ == "__main__":
    # Example of starting the game without console_data for testing
    class DummyConsole:
        def __init__(self):
            pygame.init()
            self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    dummy_console = DummyConsole()
    game = Main(dummy_console)