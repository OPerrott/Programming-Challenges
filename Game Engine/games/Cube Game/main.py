import pygame
import sys
import math
import json
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from game import *
from utils import rotate_point, project

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Cube Quest: Game Modes")
font = pygame.font.SysFont("Arial", 36)
clock = pygame.time.Clock()

menu_rects = []
shapes_data = None
shapes = []

scroll_x = 0
selected = 0
shape_rects = []
hovered_shape = None

def load_shapes(filepath="assets/shapes.json"):
    with open(filepath, "r") as f:
        return json.load(f)

def draw_text(text, y, x=400, selected=False):
    color = (255, 255, 0) if selected else (255, 255, 255)
    scale = 1.1 if selected else 1.0
    rendered = font.render(text, True, color)
    rect = rendered.get_rect(center=(x, y))
    scaled = pygame.transform.scale(rendered, (int(rect.width * scale), int(rect.height * scale)))
    scaled_rect = scaled.get_rect(center=(x, y))
    screen.blit(scaled, scaled_rect)
    return scaled_rect

def draw_shape(surface, shape, angle_x, angle_y, center_x, center_y, scale=80, hovered=False):
    color = (255, 100, 100) if hovered else (100, 200, 255)
    vertices = [project(*rotate_point(*v, angle_x, angle_y), scale=scale, offset_x=center_x, offset_y=center_y)
                for v in shape["vertices"]]
    for edge in shape["edges"]:
        pygame.draw.line(surface, color, vertices[edge[0]], vertices[edge[1]], 2)

def main_menu():
    global shapes_data, shapes, scroll_x, hovered_shape, menu_rects, shape_rects

    shapes_data = load_shapes()
    shapes = list(shapes_data.keys())

    options = ["Classic Mode", "Memory Mode", "Timed Rush", "Stroop Test", "Exit"]
    selecting_shape = False
    selected_mode = 0
    angle_x = angle_y = 0

    dragging = False
    drag_start_x = 0

    using_mouse = False  # Track input device

    while True:
        screen.fill((0, 0, 30))
        mouse_pos = pygame.mouse.get_pos()
        angle_x += 0.01
        angle_y += 0.01

        menu_rects = []
        shape_rects = []
        hovered_shape = None

        hovered_mode = None

        if not selecting_shape:
            for i, option in enumerate(options):
                y = 200 + i * 60
                rect = draw_text(option, y, selected=False)  # draw without selection first
                menu_rects.append(rect)

            # Detect hovered item
            for i, rect in enumerate(menu_rects):
                if rect.collidepoint(mouse_pos):
                    hovered_mode = i
                    break

            # Decide what to highlight based on input device
            if using_mouse:
                # Highlight hovered if any
                for i, option in enumerate(options):
                    y = 200 + i * 60
                    draw_text(option, y, selected=(i == hovered_mode))
            else:
                # Highlight keyboard selection only
                for i, option in enumerate(options):
                    y = 200 + i * 60
                    draw_text(option, y, selected=(i == selected_mode))

        else:
            draw_text(f"{options[selected_mode]}", 80, x=400, selected=True)

            start_x = 100 + scroll_x
            for i, shape_name in enumerate(shapes):
                shape_data = shapes_data[shape_name]
                center_x = start_x + i * 180
                center_y = 300
                draw_shape(screen, shape_data, angle_x, angle_y, center_x, center_y, hovered=False)
                rect = pygame.Rect(center_x - 50, center_y - 50, 100, 100)
                shape_rects.append((rect, shape_name))

                if rect.collidepoint(mouse_pos):
                    draw_shape(screen, shape_data, angle_x, angle_y, center_x, center_y, hovered=True)
                    hovered_shape = shape_name

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                using_mouse = False  # Keyboard used, disable mouse highlight
                if not selecting_shape:
                    if event.key in [pygame.K_DOWN, pygame.K_s]:
                        selected_mode = (selected_mode + 1) % len(options)
                    elif event.key in [pygame.K_UP, pygame.K_w]:
                        selected_mode = (selected_mode - 1) % len(options)
                    elif event.key == pygame.K_RETURN:
                        if selected_mode == len(options) - 1:
                            pygame.quit()
                            sys.exit()
                        selecting_shape = True
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                else:
                    if event.key == pygame.K_ESCAPE:
                        selecting_shape = False
                    elif event.key == pygame.K_LEFT:
                        scroll_x += 40
                    elif event.key == pygame.K_RIGHT:
                        scroll_x -= 40

            elif event.type == pygame.MOUSEBUTTONDOWN:
                using_mouse = True  # Mouse used, enable mouse highlight
                if event.button == 1:
                    dragging = True
                    drag_start_x = event.pos[0]

                    if not selecting_shape:
                        for i, rect in enumerate(menu_rects):
                            if rect.collidepoint(event.pos):
                                if i == len(options) - 1:
                                    pygame.quit()
                                    sys.exit()
                                selected_mode = i
                                selecting_shape = True
                    else:
                        for rect, shape_name in shape_rects:
                            if rect.collidepoint(event.pos):
                                mode = ["classic", "memory", "timed", "stroop"][selected_mode]
                                game = CubeGame(mode=mode, shape_name=shape_name)
                                game.run()

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    dragging = False

            elif event.type == pygame.MOUSEMOTION:
                if not dragging:
                    using_mouse = True  # mouse moved without drag, treat as mouse usage
                if dragging and selecting_shape:
                    dx = event.rel[0]
                    scroll_x += dx

        clock.tick(60)

if __name__ == "__main__":
    main_menu()
