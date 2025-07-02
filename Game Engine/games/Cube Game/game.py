import pygame
import random
import time
import sys
from utils import load_high_score, save_high_score, rotate_point, project, load_shapes


class CubeGame:
    def __init__(self, mode="classic", shape_name=None):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption(f"Cube Quest - {mode.title()} Mode")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 36)

        self.mode = mode
        self.running = True

        self.angle_x = 0
        self.angle_y = 0
        self.rotation_speed = 0.03
        self.score = 0
        self.level = 1
        self.best_score = load_high_score()

        self.time_limit = 30 if mode == "timed" else 60
        self.start_time = time.time()

        self.shapes = load_shapes()
        self.shape_name = shape_name or random.choice(list(self.shapes))
        shape = self.shapes[self.shape_name]
        self.vertices = shape["vertices"]
        self.edges = shape["edges"]

        self.target_index = random.randint(1, len(self.vertices) - 1)
        self.target_visible = True
        self.last_target_move = time.time()
        self.target_move_interval = 5
        self.memory_hide_time = 2

        self.hit_flash = 0

    def get_rotated_projected_vertices(self):
        return [project(*rotate_point(*v, self.angle_x, self.angle_y)) for v in self.vertices]

    def move_target(self):
        if time.time() - self.last_target_move > self.target_move_interval:
            prev = self.target_index
            while self.target_index == prev:
                self.target_index = random.randint(1, len(self.vertices) - 1)
            self.last_target_move = time.time()
            self.target_visible = True

    def draw_flash(self):
        if self.hit_flash > 0:
            overlay = pygame.Surface((800, 600))
            overlay.set_alpha(self.hit_flash)
            overlay.fill((255, 255, 255))
            self.screen.blit(overlay, (0, 0))
            self.hit_flash -= 10

    def run(self):
        while self.running:
            self.screen.fill((0, 0, 20))
            elapsed = time.time() - self.start_time
            time_left = max(0, int(self.time_limit - elapsed))

            if time_left <= 0:
                self.running = False
                save_high_score(self.score, self.best_score)
                self.show_game_over()
                break

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]: self.angle_x -= self.rotation_speed
            if keys[pygame.K_s]: self.angle_x += self.rotation_speed
            if keys[pygame.K_a]: self.angle_y -= self.rotation_speed
            if keys[pygame.K_d]: self.angle_y += self.rotation_speed

            self.move_target()
            projected = self.get_rotated_projected_vertices()
            for edge in self.edges:
                pygame.draw.line(self.screen, (200, 200, 255), projected[edge[0]], projected[edge[1]], 2)

            cursor = projected[0]
            target = projected[self.target_index]

            if self.mode == "memory" and time.time() - self.last_target_move > self.memory_hide_time:
                self.target_visible = False

            if self.target_visible:
                pygame.draw.circle(self.screen, (255, 50, 50), target, 8)

            pygame.draw.circle(self.screen, (50, 255, 50), cursor, 6)

            dist = ((cursor[0] - target[0])**2 + (cursor[1] - target[1])**2) ** 0.5
            if dist < 15:
                self.hit_flash = 100
                self.score += max(1, int(15 - dist))
                self.target_index = random.randint(1, len(self.vertices) - 1)
                self.last_target_move = time.time()
                self.target_visible = True
                if self.score % 5 == 0:
                    self.level += 1
                    self.rotation_speed += 0.005
                    self.target_move_interval = max(1.5, self.target_move_interval - 0.3)
                    if self.mode == "timed":
                        self.time_limit += 5

            self.draw_flash()
            self.draw_ui(time_left)
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

    def draw_ui(self, time_left):
        self.screen.blit(self.font.render(f"Shape: {self.shape_name}", True, (180, 180, 255)), (10, 130))
        self.screen.blit(self.font.render(f"Score: {self.score}", True, (255, 255, 255)), (10, 10))
        self.screen.blit(self.font.render(f"Time: {time_left}", True, (255, 255, 255)), (10, 40))
        self.screen.blit(self.font.render(f"Level: {self.level}", True, (255, 255, 255)), (10, 70))
        self.screen.blit(self.font.render(f"Best: {self.best_score}", True, (255, 215, 0)), (10, 100))

    def show_game_over(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.font.render("Game Over", True, (255, 255, 255)), (300, 260))
        self.screen.blit(self.font.render(f"Score: {self.score}", True, (255, 255, 255)), (300, 300))
        pygame.display.flip()
        pygame.time.wait(3000)