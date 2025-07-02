import pygame
import random

class Pipe:
    def __init__(self, window):
        self.window = window
        surface = pygame.display.get_surface()
        self.window_width = surface.get_width()
        self.window_height = surface.get_height()

        self.pipes = []  # list of pipe pairs (top and bottom rects)

        self.pipe_width = 75
        self.pipe_gap = 250  # gap between top and bottom pipes

        self.spawn_delay = 100  # frames to wait between spawning pipes
        self.spawn_timer = 0
        self.pipe_speed = 3

    def generate_pipe(self):
        self.spawn_timer += 1
        if self.spawn_timer >= self.spawn_delay:
            self.spawn_timer = 0
            top_height = random.randint(50, self.window_height // 2)
            bottom_y = top_height + self.pipe_gap
            bottom_height = self.window_height - bottom_y

            pipe_pair = {
                "top": pygame.Rect(self.window_width, 0, self.pipe_width, top_height),
                "bottom": pygame.Rect(self.window_width, bottom_y, self.pipe_width, bottom_height)
            }
            self.pipes.append(pipe_pair)

    def move_pipes(self):
        for pipe_pair in self.pipes:
            pipe_pair["top"].x -= self.pipe_speed
            pipe_pair["bottom"].x -= self.pipe_speed

        # Remove pipes that have gone off-screen
        self.pipes = [p for p in self.pipes if p["top"].right > 0]

    def draw_pipes(self):
        for pipe_pair in self.pipes:
            pygame.draw.rect(self.window, (0, 128, 0), pipe_pair["top"])
            pygame.draw.rect(self.window, (0, 128, 0), pipe_pair["bottom"])

    def update(self):
        self.generate_pipe()
        self.move_pipes()
        self.draw_pipes()