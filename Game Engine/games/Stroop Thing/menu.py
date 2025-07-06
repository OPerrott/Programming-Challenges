import pygame

class Menu:
    def __init__(self, console_data):
        self.console_data = console_data
        self.window = self.console_data.window


        self.clock = pygame.time.Clock()

        self.run()


    def update(self):
        pygame.draw.rect(self.window, (255, 255, 255), (100, 100, 200, 200))


    def run(self):
        running = True
    
        while running:
            self.window.fill((0, 162, 232))  # clear screen sky colour

            self.update()


            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    ...
                    
            self.clock.tick(60)  # limit to 60 FPS
        
        pygame.quit()