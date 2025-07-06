import pygame
import random
import time
import math
import json
import sys
import os

class PowerUp:
    COLORS = {
        "slow": (255, 215, 0),    # Gold
        "freeze": (0, 255, 255),  # Cyan
        "boost": (0, 255, 0)      # Green
    }

    def __init__(self, index, type_):
        self.index = index
        self.type = type_
        self.active = True
        self.radius = 10
        self.color = self.COLORS.get(type_, (255, 255, 255))

    def draw(self, surface, projected_vertices):
        if self.active:
            pos = projected_vertices[self.index]
            pygame.draw.circle(surface, self.color, pos, self.radius)

    def collided_with(self, cursor_pos, projected_vertices):
        if not self.active:
            return False
        px, py = projected_vertices[self.index]
        dx = px - cursor_pos[0]
        dy = py - cursor_pos[1]
        return (dx**2 + dy**2) ** 0.5 < self.radius + 6


class Game:
    def __init__(self, window, mode="classic", shape_name=None):
        self.window = window
        self.mode = mode
        self.running = True

        self.width, self.height = self.window.get_size()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 36)

        self._setup_shape(shape_name)
        self._init_game_state()

        self.paused = False

        self.level = 1           # Start at level 1
        self.level_up_score = 25  # Score needed to level up

    def load_high_score(self, path="Game Engine/games/Cube Game/assets/highscore.txt"):
        if os.path.exists(path):
            with open(path, "r") as f:
                try:
                    return int(f.read())
                except ValueError:
                    return 0
        return 0

    def save_high_score(self, score, best, path="Game Engine/games/Cube Game/assets/highscore.txt"):
        if score > best:
            with open(path, "w") as f:
                f.write(str(score))

    def rotate_point(self, x, y, z, angle_x, angle_y):
        xz = x * math.cos(angle_y) - z * math.sin(angle_y)
        zz = x * math.sin(angle_y) + z * math.cos(angle_y)
        yz = y * math.cos(angle_x) - zz * math.sin(angle_x)
        zz = y * math.sin(angle_x) + zz * math.cos(angle_x)
        return xz, yz, zz

    def project(self, x, y, z, scale=100, offset_x=None, offset_y=None):
        if offset_x is None:
            offset_x = self.width // 2
        if offset_y is None:
            offset_y = self.height // 2
        factor = scale / (z + 5)
        screen_x = int(x * factor + offset_x)
        screen_y = int(y * factor + offset_y)
        return screen_x, screen_y

    def load_shapes(self, filepath="Game Engine/games/Cube Game/assets/shapes.json"):
        with open(filepath, "r") as f:
            return json.load(f)

    def _setup_shape(self, shape_name):
        self.shapes = self.load_shapes()
        self.shape_name = shape_name or random.choice(list(self.shapes))
        shape_data = self.shapes[self.shape_name]
        scale_map = {
            "cube": 2.5, "pyramid": 2.0, "octahedron": 2.0, "tetrahedron": 1.0,
            "hexagonal_prism": 2.0, "dodecahedron": 2.0, "icosahedron": 2.0, "sphere": 4.0
        }
        scale = scale_map.get(self.shape_name, 1.0)
        self.vertices = [[x * scale, y * scale, z * scale] for x, y, z in shape_data["vertices"]]
        self.edges = shape_data["edges"]

    def _init_game_state(self):
        self.angle_x = 0
        self.angle_y = 0
        self.rotation_speed = 0.01
        self.base_speed = self.rotation_speed

        self.score = 0
        self.level = 1

        self.time_limit = 30  # 30 seconds countdown timer
        self.start_time = time.time()
        self.game_over = False
        self.final_score_displayed = False

        self.target_index = random.randint(1, len(self.vertices) - 1)
        self.target_visible = True
        self.last_target_move = time.time()

        self.powerup = None
        self.next_powerup_time = time.time() + random.randint(10, 20)
        self.powerup_active = False
        self.active_powerup_type = None
        self.powerup_end_time = 0
        self.freeze_target = False

    def update(self):
        if self.paused or self.game_over:
            return

        elapsed = time.time() - self.start_time
        if elapsed >= self.time_limit:
            self.game_over = True
            return

        self._rotate()
        self._handle_target()
        self._handle_powerup()
        self._check_collision()

    def draw(self):
        self.window.fill((0, 0, 20))
        projected = self._project_vertices()

        for edge in self.edges:
            pygame.draw.line(self.window, (200, 200, 255), projected[edge[0]], projected[edge[1]], 2)

        cursor_pos = projected[0]
        if self.target_visible:
            pygame.draw.circle(self.window, (255, 50, 50), projected[self.target_index], 8)
        pygame.draw.circle(self.window, (50, 255, 50), cursor_pos, 6)

        if self.powerup:
            self.powerup.draw(self.window, projected)

        # Draw score and level
        score_surf = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        level_surf = self.font.render(f"Level: {self.level}", True, (255, 255, 255))
        self.window.blit(score_surf, (10, 10))
        self.window.blit(level_surf, (10, 50))

        # Draw timer or final score screen
        if not self.game_over:
            time_left = max(0, int(self.time_limit - (time.time() - self.start_time)))
            timer_surf = self.font.render(f"Time: {time_left}", True, (255, 255, 255))
            self.window.blit(timer_surf, (self.width - 120, 10))
        else:
            # Game over screen with final score centered
            if not self.final_score_displayed:
                self.final_score_text = self.font.render(f"Time's up! Final Score: {self.score}", True, (255, 255, 255))
                self.final_score_rect = self.final_score_text.get_rect(center=(self.width // 2, self.height // 2))
                self.final_score_displayed = True

            self.window.blit(self.final_score_text, self.final_score_rect)

        pygame.display.flip()

    def _project_vertices(self):
        return [self.project(*self.rotate_point(*v, self.angle_x, self.angle_y)) for v in self.vertices]

    def _rotate(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]: self.angle_x -= self.rotation_speed
        if keys[pygame.K_s]: self.angle_x += self.rotation_speed
        if keys[pygame.K_a]: self.angle_y -= self.rotation_speed
        if keys[pygame.K_d]: self.angle_y += self.rotation_speed

    def _handle_target(self):
        now = time.time()
        if not self.freeze_target and now - self.last_target_move > 5:
            previous = self.target_index
            while self.target_index == previous:
                self.target_index = random.randint(1, len(self.vertices) - 1)
            self.last_target_move = now
            self.target_visible = True

    def _handle_powerup(self):
        now = time.time()
        projected = self._project_vertices()
        cursor = projected[0]

        if self.powerup_active and now > self.powerup_end_time:
            self._deactivate_powerup()

        if not self.powerup and now > self.next_powerup_time:
            self._spawn_powerup()

        if self.powerup and self.powerup.collided_with(cursor, projected):
            self._activate_powerup()

    def _spawn_powerup(self):
        index = random.randint(1, len(self.vertices) - 1)
        p_type = random.choice(["slow", "freeze", "boost"])
        self.powerup = PowerUp(index, p_type)
        self.next_powerup_time = time.time() + random.randint(10, 20)

    def _activate_powerup(self):
        now = time.time()
        p_type = self.powerup.type
        self.active_powerup_type = p_type
        self.powerup_active = True
        self.powerup_end_time = now + 5
        self.powerup.active = False

        if p_type == "slow":
            self.rotation_speed = self.base_speed * 0.5
        elif p_type == "freeze":
            self.freeze_target = True
        elif p_type == "boost":
            self.score += 10
            self.powerup_active = False
            self.powerup = None

    def _deactivate_powerup(self):
        if self.active_powerup_type == "slow":
            self.rotation_speed = self.base_speed
        elif self.active_powerup_type == "freeze":
            self.freeze_target = False

        self.powerup_active = False
        self.active_powerup_type = None
        self.powerup = None

    def _check_collision(self):
        if not self.target_visible or self.game_over:
            return

        projected = self._project_vertices()
        target_pos = projected[self.target_index]
        cursor_pos = projected[0]

        dx = cursor_pos[0] - target_pos[0]
        dy = cursor_pos[1] - target_pos[1]
        distance = math.sqrt(dx*dx + dy*dy)

        if distance < 8 + 6:  # target radius + cursor radius
            self.score += 1

            # Increase level & speed every level_up_score points
            if self.score % self.level_up_score == 0:
                self.level += 1
                self.rotation_speed = self.base_speed * (1 + 0.01 * (self.level - 1))

            previous = self.target_index
            while self.target_index == previous:
                self.target_index = random.randint(1, len(self.vertices) - 1)
            self.target_visible = True
            self.last_target_move = time.time()

    def run(self):
        final_score_display_time = 3  # seconds to show final score after time runs out
        final_score_start = None

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.save_high_score(self.score, self.best_score)
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.paused = not self.paused

            if not self.paused:
                self.update()

            # Draw everything including timer or final score
            self.window.fill((0, 0, 20))
            projected = self._project_vertices()

            for edge in self.edges:
                pygame.draw.line(self.window, (200, 200, 255), projected[edge[0]], projected[edge[1]], 2)

            cursor_pos = projected[0]

            if self.target_visible:
                pygame.draw.circle(self.window, (255, 50, 50), projected[self.target_index], 8)
            pygame.draw.circle(self.window, (50, 255, 50), cursor_pos, 6)

            if self.powerup:
                self.powerup.draw(self.window, projected)

            # Draw score and level
            score_surf = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
            level_surf = self.font.render(f"Level: {self.level}", True, (255, 255, 255))
            self.window.blit(score_surf, (10, 10))
            self.window.blit(level_surf, (10, 50))

            # Calculate remaining time
            elapsed = time.time() - self.start_time
            remaining_time = max(0, int(self.time_limit - elapsed))

            if remaining_time > 0:
                # Draw timer
                timer_surf = self.font.render(f"Time: {remaining_time}", True, (255, 255, 255))
                self.window.blit(timer_surf, (self.width - 150, 10))
            else:
                # Time's up, display final score
                if final_score_start is None:
                    final_score_start = time.time()

                final_text = self.font.render(f"Time's up! Final Score: {self.score}", True, (255, 255, 255))
                rect = final_text.get_rect(center=(self.width // 2, self.height // 2))
                self.window.blit(final_text, rect)

                # After showing final score for some time, end game
                if time.time() - final_score_start > final_score_display_time:
                    self.running = False

            pygame.display.flip()
            self.clock.tick(60)


