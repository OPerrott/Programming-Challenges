from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
import subprocess
import pygame
import json
import sys
import os

class GUI:
    def __init__(self, console):
        self.console = console
        
        self.window = self.console.window
        
        surface = pygame.display.get_surface()
        self.width = surface.get_width()
        self.height = surface.get_height()
        
        self.title_lines = [
            "  _____                         _____                      _      ",
            " / ____|                       / ____|                    | |     ",
            "| |  __  __ _ _ __ ___   ___  | |     ___  _ __  ___  ___ | | ___ ",
            "| | |_ |/ _` | '_ ` _ \\ / _ \\ | |    / _ \\| '_ \\/ __|/ _ \\| |/ _ \\",
            "| |__| | (_| | | | | | |  __/ | |___| (_) | | | \\__ \\ (_) | |  __/",
            " \\_____|\\__,_|_| |_| |_|\\___|  \\_____\\___/|_| |_|___/\\___/|_|\\___|"
        ]
        self.title_frame = 0
        self.title_delay = 10  # frames between lines appearing

        self.font = pygame.font.SysFont('Comic Sans MS', 20)
        self.title_font = pygame.font.SysFont('Courier New', 24, bold=True)
        
        self.game_boxes = []  # Will store tuples: (pygame.Rect, game_dir, game_name)

        self.draw_gui()

    def draw_title(self):
        line_spacing = 26
        start_y = 10

        # Show only up to current frame
        lines_to_show = self.title_frame // self.title_delay

        for i, line in enumerate(self.title_lines[:lines_to_show]):
            rendered = self.title_font.render(line, True, (0, 128, 0))
            rect = rendered.get_rect(center=(self.width // 2, start_y + i * line_spacing))
            self.window.blit(rendered, rect)

        # Increment frame counter
        if self.title_frame < len(self.title_lines) * self.title_delay:
            self.title_frame += 1

    def draw_games(self):
        dir_path = Path("Game Engine") / "games"

        games = []
        for game_dir in dir_path.iterdir():
            if game_dir.is_dir():
                config_path = game_dir / "config.json"
                if config_path.exists():
                    try:
                        with open(config_path, "r", encoding="utf-8") as f:
                            config = json.load(f)
                        game_name = config.get("name", game_dir.name)
                        cover_file = config.get("cover", None)
                    except Exception as e:
                        print(f"Error loading config for {game_dir.name}: {e}")
                        game_name = game_dir.name
                        cover_file = "Game Engine-system/resources/textures/Default.png"
                else:
                    game_name = "N/A"
                    cover_file = "Game Engine-system/resources/textures/Default.png"

                games.append((game_name, game_dir, cover_file))

        mouse_pos = pygame.mouse.get_pos()
        base_width = 300
        base_height = 450
        spacing = 50

        total_width = len(games) * (base_width + spacing) - spacing
        start_x = (self.width - total_width) // 2
        y = self.height // 2 - base_height // 2

        self.game_boxes.clear()  # Clear old clickable rects before drawing

        for i, (game_name, game_dir, cover_file) in enumerate(games):
            x = start_x + i * (base_width + spacing)

            rect = pygame.Rect(x, y, base_width, base_height)
            is_hovered = rect.collidepoint(mouse_pos)

            scale = 1.1 if is_hovered else 1.0
            draw_width = int(base_width * scale)
            draw_height = int(base_height * scale)
            draw_x = x - (draw_width - base_width) // 2
            draw_y = y - (draw_height - base_height) // 2
            draw_rect = pygame.Rect(draw_x, draw_y, draw_width, draw_height)

            # Draw the white box with border
            pygame.draw.rect(self.window, (255, 255, 255), draw_rect)
            pygame.draw.rect(self.window, (0, 0, 0), draw_rect, 3)

            # Draw cover art if available
            if cover_file:
                cover_path = game_dir / cover_file
                if cover_path.exists():
                    try:
                        image = pygame.image.load(str(cover_path))
                        image = pygame.transform.smoothscale(image, (draw_width, draw_height))
                        self.window.blit(image, (draw_x, draw_y))
                    except Exception as e:
                        print(f"Error loading image {cover_file} for {game_name}: {e}")

            # Draw game name below the box
            text = self.font.render(game_name, True, (255, 255, 255))
            text_rect = text.get_rect(center=(draw_rect.centerx, draw_rect.bottom + 20))
            self.window.blit(text, text_rect)

            # Store the clickable rect and associated game info
            self.game_boxes.append((draw_rect, game_dir, game_name))

    def handle_click(self, pos):
        """Call this method with the mouse click position (pos) to detect clicks on games."""
        for rect, game_dir, game_name in self.game_boxes:
            if rect.collidepoint(pos):
                print(f"Clicked on game: {game_name} at {game_dir}")

                main_py = game_dir / "main.py"
                if main_py.exists():
                    try:
                        # Launch the game's main.py as a subprocess
                        # Using the same python interpreter that's running the launcher
                        spec = spec_from_file_location("main_module", str(main_py))
                        main_module = module_from_spec(spec)
                        spec.loader.exec_module(main_module)

                        # Now run main_module.Main(window)
                        main_module.Main(self.console)
                    except Exception as e:
                        print(f"Failed to launch {game_name}: {e}")
                else:
                    print(f"No main.py found in {game_dir}")

                break

    def draw_gui(self):
        self.draw_title()
        self.draw_games()
