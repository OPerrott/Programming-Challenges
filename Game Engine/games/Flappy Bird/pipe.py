import pygame

class Pipe:
    def __init__(self, window):
        self.window = window
        
        self.top_x = 500
        self.top_y = 0
        self.top_width = 50
        self.top_height = 100
        
        self.bottom_x = 500
        self.bottom_y = (self.top_y + self.top_height) + 100
        self.bottom_width = 50
        self.bottom_height = 100
        
        
    def draw_pipes(self):
        self.top = pygame.draw.rect(self.window, (0, 128, 0), (self.top_x, self.top_y, self.top_width, self.top_height))
        self.bottom = pygame.draw.rect(self.window, (0, 128, 0), (self.bottom_x, self.bottom_y, self.bottom_width, self.bottom_height))
        
    def move_pipes(self):
        self.top_x -= 3
        self.bottom_x -= 3
    
    def update(self):
        self.draw_pipes()
        self.move_pipes()