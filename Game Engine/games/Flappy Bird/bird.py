import pygame

class Bird:
    def __init__(self, window):
        self.window = window
        
        self.x = 100
        self.y = 300
        
        self.radius = 25
        self.color = (128, 0, 128)
        
        self.vy = 0              # vertical velocity
        self.gravity = 1         # gravity acceleration
        self.jump_strength = -15 # initial jump velocity (negative is up)
        
        self.max_jumps = 2_147_483_647       # allow double jump
        self.jumps_made = 0      # jumps done since last ground
        
    def jump(self):
        if self.jumps_made < self.max_jumps:
            self.vy = self.jump_strength
            self.jumps_made += 1
    
    def draw_bird(self):
        pygame.draw.circle(self.window, self.color, (self.x, int(self.y)), self.radius)
        
    def update(self):
        # Apply velocity to position
        self.y += self.vy
        
        # Apply gravity
        self.vy += self.gravity
        
        # Floor collision check (ground)
        ground_level = self.window.get_height() - self.radius
        if self.y > ground_level:
            self.y = ground_level
            self.vy = 0
            self.jumps_made = 0  # reset jump count on ground
            
        self.draw_bird()
