import pygame
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bird import *
from pipe import *




class Main:
    def __init__(self, console_data):
                    
        self.console_data = console_data
        self.window = self.console_data.window
        
        pygame.display.set_caption("Flappy Bird")
        
        self.pipe = Pipe(self.window)
        self.bird = Bird(self.window)

        self.clock = pygame.time.Clock()

        self.run()
        

    def run(self):
        running = True
    
        while running:
            self.window.fill((30, 30, 30))  # clear screen with dark gray
            
            self.pipe.update()
            self.bird.update()
            
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.bird.jump()
                    
            self.clock.tick(60)  # limit to 60 FPS
        
        pygame.quit()
        
        
if __name__ == "__main__":
    # Example of starting the game without console_data for testing
    class DummyConsole:
        def __init__(self):
            pygame.init()
            self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    dummy_console = DummyConsole()
    game = Main(dummy_console)