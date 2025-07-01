from utils.latch_game import Latch
from gui.gui import GUI

import pygame
import sys

class Console:
    def __init__(self):
        pygame.init()

        self.LOADED_GAME = False    
        self.make_window()

        self.gui = GUI(self)  # Create GUI once

        self.latch = None  # Will be assigned later if needed

        self.events()

    def make_window(self):            
        self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        pygame.display.set_caption("Launcher")

    def events(self):
        exit_game = False
        
        while not exit_game:
            self.window.fill((0, 0, 0))

            # Draw GUI elements
            self.gui.draw_gui()

            # If game is not loaded, launch Latch once
            if not self.LOADED_GAME:
                self.latch = Latch(self)
                self.LOADED_GAME = True  # Avoid reinitializing

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left click
                    self.gui.handle_click(event.pos)

            pygame.display.update()

        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    Console()
