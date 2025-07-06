import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from menu import Menu
import pygame




class Main:
    def __init__(self, console_data):
        self.console_data = console_data
        self.window = self.console_data.window
        
        self.menu = Menu(self)
        
        self.run()
        
        
        
    def update(self):
        self.menu.update()
        
        
    def run(self):
        clock = pygame.time.Clock()

        
        running = True
        while running:
            self.window.fill((0, 0, 0))

            self.update()

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    ...
                    
            clock.tick(60)  # limit to 60 FPS

        

if __name__ == "__main__":
    # Example of starting the game without console_data for testing
    class DummyConsole:
        def __init__(self):
            pygame.init()
            self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    dummy_console = DummyConsole()
    game = Main(dummy_console)