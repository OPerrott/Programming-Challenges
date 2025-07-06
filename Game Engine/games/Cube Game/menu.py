from game import Game
import json
import pygame
import sys
import math

class Menu:
    def __init__(self, console_data):
        self.console_data = console_data
        self.window = self.console_data.window

        self.window_width = self.window.get_width()
        self.window_height = self.window.get_height()

        # Controller setup
        pygame.joystick.init()
        self.joystick = pygame.joystick.Joystick(0) if pygame.joystick.get_count() > 0 else None
        if self.joystick:
            self.joystick.init()

        # Game state
        self.shapes_data = self.load_shapes()
        self.shapes = list(self.shapes_data.keys())
        self.options = ["Classic", "Memory", "Timed", "Exit"]

        self.selecting_shape = False
        self.selected_mode = 0
        self.selected_shape_index = 0

        self.hovered_shape = None
        self.menu_rects = []
        self.shape_rects = []

        self.angle_x = 0
        self.angle_y = 0

        self.dragging = False
        self.drag_start_x = 0
        self.using_mouse = False
        self.controller_cooldown = 0

        self.font = pygame.font.SysFont("Arial", 70)

    def load_shapes(self, filepath="Game Engine/games/Cube Game/assets/shapes.json"):
        with open(filepath, "r") as f:
            return json.load(f)

    def rotate_point(self, x, y, z, angle_x, angle_y):
        xz = x * math.cos(angle_y) - z * math.sin(angle_y)
        zz = x * math.sin(angle_y) + z * math.cos(angle_y)
        yz = y * math.cos(angle_x) - zz * math.sin(angle_x)
        zz = y * math.sin(angle_x) + zz * math.cos(angle_x)
        return xz, yz, zz

    def project(self, x, y, z, scale=100, offset_x=400, offset_y=300):
        factor = scale / (z + 5)
        screen_x = int(x * factor + offset_x)
        screen_y = int(y * factor + offset_y)
        return screen_x, screen_y

    def draw_shape(self, surface, shape, angle_x, angle_y, center_x, center_y, scale=80, hovered=False, selected=False):
        if selected:
            color = (0, 255, 0)
        elif hovered:
            color = (255, 100, 100)
        else:
            color = (100, 200, 255)

        vertices = [self.project(*self.rotate_point(*v, angle_x, angle_y), scale=scale * 2,
                                 offset_x=center_x, offset_y=center_y)
                    for v in shape["vertices"]]
        for edge in shape["edges"]:
            pygame.draw.line(surface, color, vertices[edge[0]], vertices[edge[1]], 2)

    def draw_text(self, screen, text, font, y, x=400, selected=False, hovered=False):
        if hovered:
            colour = (255, 100, 100)
        elif selected:
            colour = (255, 255, 0)
        else:
            colour = (255, 255, 255)
        rendered = font.render(text, True, colour)
        rect = rendered.get_rect(center=(x, y))
        screen.blit(rendered, rect)
        return rect

    def render_menu(self):
        self.menu_rects.clear()
        mouse_pos = pygame.mouse.get_pos()
        spacing = self.window_height // (len(self.options) + 1)

        for i, option in enumerate(self.options):
            y = spacing * (i + 1)
            rect = self.draw_text(
                self.window,
                option,
                self.font,
                y,
                self.window_width // 2,
                selected=(i == self.selected_mode and not self.using_mouse),
                hovered=self.using_mouse and pygame.Rect(0, y - 40, self.window_width, 80).collidepoint(mouse_pos)
            )
            self.menu_rects.append(rect)

    def render_shape_selector(self):
        self.draw_text(self.window, self.options[self.selected_mode], self.font,
                       int(self.window_height * 0.1),
                       x=self.window_width // 2, selected=True)

        shape_spacing = int(self.window_width * 0.25)
        start_x = self.window_width // 2 - self.selected_shape_index * shape_spacing
        center_y = int(self.window_height * 0.5)
        self.shape_rects.clear()
        shape_scale = min(self.window_width, self.window_height) // 10

        for i, shape_name in enumerate(self.shapes):
            shape_data = self.shapes_data[shape_name]
            center_x = start_x + i * shape_spacing
            is_selected = (i == self.selected_shape_index)

            rect = pygame.Rect(center_x - 50, center_y - 50, 100, 100)
            self.shape_rects.append((rect, shape_name))
            is_hovered = rect.collidepoint(pygame.mouse.get_pos())

            if is_hovered:
                self.hovered_shape = shape_name

            self.draw_shape(self.window, shape_data, self.angle_x, self.angle_y, center_x, center_y,
                            scale=shape_scale, hovered=is_hovered, selected=is_selected)

        if 0 <= self.selected_shape_index < len(self.shapes):
            label = self.font.render(self.shapes[self.selected_shape_index], True, (255, 255, 255))
            label_rect = label.get_rect(center=(self.window_width // 2, int(self.window_height * 0.85)))
            self.window.blit(label, label_rect)

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self.using_mouse = False
                if not self.selecting_shape:
                    if event.key in [pygame.K_DOWN, pygame.K_s]:
                        self.selected_mode = (self.selected_mode + 1) % len(self.options)
                    elif event.key in [pygame.K_UP, pygame.K_w]:
                        self.selected_mode = (self.selected_mode - 1) % len(self.options)
                    elif event.key == pygame.K_RETURN:
                        if self.selected_mode == len(self.options) - 1:
                            pygame.quit()
                            sys.exit()
                        self.selecting_shape = True
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                else:
                    if event.key == pygame.K_ESCAPE:
                        self.selecting_shape = False
                    elif event.key == pygame.K_LEFT:
                        self.selected_shape_index = max(0, self.selected_shape_index - 1)
                    elif event.key == pygame.K_RIGHT:
                        self.selected_shape_index = min(len(self.shapes) - 1, self.selected_shape_index + 1)
                    elif event.key == pygame.K_RETURN:
                        self.launch_game()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.using_mouse = True
                if event.button == 1:
                    self.dragging = True
                    self.drag_start_x = event.pos[0]

                    if not self.selecting_shape:
                        for i, rect in enumerate(self.menu_rects):
                            if rect.collidepoint(event.pos):
                                if i == len(self.options) - 1:
                                    pygame.quit()
                                    sys.exit()
                                self.selected_mode = i
                                self.selecting_shape = True
                    else:
                        for i, (rect, _) in enumerate(self.shape_rects):
                            if rect.collidepoint(event.pos):
                                self.selected_shape_index = i
                                self.launch_game()

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.dragging = False

            elif event.type == pygame.MOUSEMOTION:
                if not self.dragging:
                    self.using_mouse = True

    def handle_controller_input(self):
        if not self.joystick or self.controller_cooldown > 0:
            return

        axis_y = self.joystick.get_axis(1)
        axis_x = self.joystick.get_axis(0)
        hat_x, hat_y = self.joystick.get_hat(0)

        if not self.selecting_shape:
            if abs(axis_y) > 0.5 or hat_y != 0:
                self.selected_mode = (self.selected_mode + (1 if axis_y > 0 or hat_y < 0 else -1)) % len(self.options)
                self.controller_cooldown = 10
            elif self.joystick.get_button(0):
                if self.selected_mode == len(self.options) - 1:
                    pygame.quit()
                    sys.exit()
                self.selecting_shape = True
                self.controller_cooldown = 10
        else:
            if abs(axis_x) > 0.5 or hat_x != 0:
                delta = 1 if (axis_x > 0 or hat_x > 0) else -1
                self.selected_shape_index = max(0, min(len(self.shapes) - 1, self.selected_shape_index + delta))
                self.controller_cooldown = 10
            elif self.joystick.get_button(1):
                self.selecting_shape = False
                self.controller_cooldown = 10
            elif self.joystick.get_button(0):
                self.launch_game()
                self.controller_cooldown = 10

    def launch_game(self):
        shape_name = self.shapes[self.selected_shape_index]
        mode = ["Classic", "Memory", "Timed"][self.selected_mode]
        game = Game(window=self.window, mode=mode, shape_name=shape_name)
        game.run()  # runs game loop until game over and final score shown
        self.selecting_shape = False  # back to menu after game ends



    def update(self):
        self.angle_x += 0.01
        self.angle_y += 0.01
        self.window.fill((0, 0, 30))

        if self.controller_cooldown > 0:
            self.controller_cooldown -= 1

        if not self.selecting_shape:
            self.render_menu()
        else:
            self.render_shape_selector()

        self.handle_input()
        self.handle_controller_input()

        pygame.display.flip()
