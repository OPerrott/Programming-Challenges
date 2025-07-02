import pygame

class Menu:
    def __init__(self, console_data):
        self.console_data = console_data
        self.window = self.console_data.window


        self.clock = pygame.time.Clock()

        self.run()





    def run(self):
        running = True
    
        while running:
            self.window.fill((0, 162, 232))  # clear screen sky colour

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.bird.jump()
                    
            self.clock.tick(60)  # limit to 60 FPS
        
        pygame.quit()