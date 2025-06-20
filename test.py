import json
import os
import pygame
import sys
import time

pygame.init()
screen_width, screen_height = 1000, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rectangles Editor with Buttons and Inputs")
font = pygame.font.SysFont(None, 24)
small_font = pygame.font.SysFont(None, 20)

JSON_FILE = "rectangles.json"
READ_INTERVAL = 1
SCALE_MARGIN = 10
MIN_SIZE = 20
SIDEBAR_WIDTH = 300
MENU_BG_COLOR = (240, 240, 240)
INPUT_BOX_HEIGHT = 30
BUTTON_HEIGHT = 30
BUTTON_WIDTH = 120
BUTTON_MARGIN = 10

rectangles = {}
last_modified_time = 0
dragging_name = None
resizing = False
offset_x = 0
offset_y = 0
selected_name = None

input_boxes = {}
active_box = None
input_text = ""

colors = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255),
    (255, 255, 0), (255, 0, 255), (0, 255, 255),
    (128, 128, 128), (0, 0, 0), (255, 255, 255)
]
color_index = 0


def load_rectangles():
    global rectangles, last_modified_time
    if os.path.exists(JSON_FILE):
        current_modified = os.path.getmtime(JSON_FILE)
        if current_modified != last_modified_time:
            with open(JSON_FILE, "r") as f:
                data = json.load(f)
                new_rectangles = {}
                for name, info in data.items():
                    x, y = info.get("position", [50, 50])
                    w, h = info.get("size", [80, 60])
                    color = tuple(info.get("color", [255, 0, 0]))
                    new_rectangles[name] = {
                        "rect": pygame.Rect(x, y, w, h),
                        "color": color
                    }
                rectangles = new_rectangles
                last_modified_time = current_modified


def save_rectangles():
    data = {}
    for name, info in rectangles.items():
        rect = info["rect"]
        color = info["color"]
        data[name] = {
            "position": [rect.x, rect.y],
            "size": [rect.width, rect.height],
            "color": list(color)
        }
    with open(JSON_FILE, "w") as f:
        json.dump(data, f, indent=2)


def get_rect_under_mouse(pos):
    for name, info in rectangles.items():
        if info["rect"].collidepoint(pos):
            return name
    return None


def is_on_corner(rect, pos):
    x, y = pos
    return rect.right - SCALE_MARGIN <= x <= rect.right and rect.bottom - SCALE_MARGIN <= y <= rect.bottom


def draw_text(surface, text, pos, font, color=(0, 0, 0)):
    label = font.render(text, True, color)
    surface.blit(label, pos)


class InputBox:
    def __init__(self, rect, text=''):
        self.rect = pygame.Rect(rect)
        self.color_inactive = pygame.Color('gray80')
        self.color_active = pygame.Color('dodgerblue2')
        self.color = self.color_inactive
        self.text = text
        self.txt_surface = small_font.render(text, True, (0, 0, 0))
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                self.active = True
                self.color = self.color_active
            else:
                self.active = False
                self.color = self.color_inactive

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.active = False
                    self.color = self.color_inactive
                    return 'submit'
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    # Limit length to 20 chars
                    if len(self.text) < 20:
                        self.text += event.unicode
                self.txt_surface = small_font.render(self.text, True, (0, 0, 0))
        return None

    def draw(self, screen):
        # Blit the text.
        screen.fill((255, 255, 255), self.rect)
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)


class Button:
    def __init__(self, rect, text, callback):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.callback = callback
        self.hovered = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.hovered:
                self.callback()

    def draw(self, screen):
        color = (180, 180, 180) if self.hovered else (140, 140, 140)
        pygame.draw.rect(screen, color, self.rect)
        draw_text(screen, self.text, (self.rect.x + 10, self.rect.y + 7), small_font, (0, 0, 0))


def cycle_color():
    global color_index
    if selected_name and selected_name in rectangles:
        current_color = rectangles[selected_name]["color"]
        try:
            next_index = (colors.index(current_color) + 1) % len(colors)
        except ValueError:
            next_index = 0
        rectangles[selected_name]["color"] = colors[next_index]
        save_rectangles()


def add_rectangle():
    global color_index, selected_name
    base_name = "rect"
    i = 1
    while f"{base_name}{i}" in rectangles:
        i += 1
    new_name = f"{base_name}{i}"
    rectangles[new_name] = {
        "rect": pygame.Rect(50, 50, 80, 60),
        "color": colors[color_index % len(colors)]
    }
    color_index += 1
    selected_name = new_name
    save_rectangles()


def delete_rectangle():
    global selected_name
    if selected_name and selected_name in rectangles:
        del rectangles[selected_name]
        selected_name = None
        save_rectangles()


def draw_sidebar():
    pygame.draw.rect(screen, MENU_BG_COLOR, (screen_width - SIDEBAR_WIDTH, 0, SIDEBAR_WIDTH, screen_height))
    if selected_name and selected_name in rectangles:
        info = rectangles[selected_name]
        rect = info["rect"]
        color = info["color"]
        sidebar_x = screen_width - SIDEBAR_WIDTH + 10
        y_start = 20

        # Draw labels for input boxes
        labels = ["Name", "X", "Y", "Width", "Height"]
        for i, label in enumerate(labels):
            draw_text(screen, label + ":", (sidebar_x, y_start + i * (INPUT_BOX_HEIGHT + 15)), small_font)

        # Draw color display
        color_rect = pygame.Rect(sidebar_x, y_start + 5 * (INPUT_BOX_HEIGHT + 15), 50, INPUT_BOX_HEIGHT)
        pygame.draw.rect(screen, color, color_rect)
        pygame.draw.rect(screen, (0, 0, 0), color_rect, 2)
        draw_text(screen, "Color:", (sidebar_x, y_start + 5 * (INPUT_BOX_HEIGHT + 15) - 20), small_font)

        # Draw buttons
        for button in buttons:
            button.draw(screen)


load_rectangles()
last_read_time = time.time()
running = True

# Create input boxes for the 5 editable properties
def create_input_boxes():
    global input_boxes
    sidebar_x = screen_width - SIDEBAR_WIDTH + 80
    y_start = 20
    input_boxes = {
        "Name": InputBox((sidebar_x, y_start + 0 * (INPUT_BOX_HEIGHT + 15), 180, INPUT_BOX_HEIGHT)),
        "X": InputBox((sidebar_x, y_start + 1 * (INPUT_BOX_HEIGHT + 15), 180, INPUT_BOX_HEIGHT)),
        "Y": InputBox((sidebar_x, y_start + 2 * (INPUT_BOX_HEIGHT + 15), 180, INPUT_BOX_HEIGHT)),
        "Width": InputBox((sidebar_x, y_start + 3 * (INPUT_BOX_HEIGHT + 15), 180, INPUT_BOX_HEIGHT)),
        "Height": InputBox((sidebar_x, y_start + 4 * (INPUT_BOX_HEIGHT + 15), 180, INPUT_BOX_HEIGHT)),
    }

create_input_boxes()

# Create buttons
buttons = [
    Button((screen_width - SIDEBAR_WIDTH + 10, 20 + 6 * (INPUT_BOX_HEIGHT + 15), BUTTON_WIDTH, BUTTON_HEIGHT), "Change Color", cycle_color),
    Button((screen_width - SIDEBAR_WIDTH + 10, 20 + 7 * (INPUT_BOX_HEIGHT + 15), BUTTON_WIDTH, BUTTON_HEIGHT), "Add Rectangle", add_rectangle),
    Button((screen_width - SIDEBAR_WIDTH + 10, 20 + 8 * (INPUT_BOX_HEIGHT + 15), BUTTON_WIDTH, BUTTON_HEIGHT), "Delete Rectangle", delete_rectangle),
]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle dragging and resizing rectangles
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0] < screen_width - SIDEBAR_WIDTH:
                pos = event.pos
                for name, info in rectangles.items():
                    if is_on_corner(info["rect"], pos):
                        dragging_name = name
                        resizing = True
                        selected_name = name
                        break
                    elif info["rect"].collidepoint(pos):
                        dragging_name = name
                        selected_name = name
                        mouse_x, mouse_y = pos
                        offset_x = info["rect"].x - mouse_x
                        offset_y = info["rect"].y - mouse_y
                        break
            else:
                # Check if clicked any input box or button in sidebar
                for box in input_boxes.values():
                    box.handle_event(event)
                for button in buttons:
                    button.handle_event(event)

        elif event.type == pygame.MOUSEBUTTONUP:
            if dragging_name:
                save_rectangles()
            dragging_name = None
            resizing = False

        elif event.type == pygame.MOUSEMOTION and dragging_name:
            mouse_x, mouse_y = event.pos
            rect = rectangles[dragging_name]["rect"]
            if resizing:
                rect.width = max(MIN_SIZE, mouse_x - rect.x)
                rect.height = max(MIN_SIZE, mouse_y - rect.y)
            else:
                rect.x = mouse_x + offset_x
                rect.y = mouse_y + offset_y

        # Handle input boxes keyboard events
        elif event.type == pygame.KEYDOWN:
            submitted = False
            for key, box in input_boxes.items():
                result = box.handle_event(event)
                if result == 'submit':
                    submitted = True
                    if selected_name not in rectangles:
                        break
                    rect = rectangles[selected_name]["rect"]
                    try:
                        if key == "Name":
                            new_name = box.text.strip()
                            if new_name and new_name != selected_name:
                                # Rename safely
                                if new_name not in rectangles:
                                    rectangles[new_name] = rectangles.pop(selected_name)
                                    selected_name = new_name
                                    input_boxes["Name"].text = new_name
                                    input_boxes["Name"].txt_surface = small_font.render(new_name, True, (0, 0, 0))
                        elif key == "X":
                            rect.x = int(box.text)
                        elif key == "Y":
                            rect.y = int(box.text)
                        elif key == "Width":
                            rect.width = max(MIN_SIZE, int(box.text))
                        elif key == "Height":
                            rect.height = max(MIN_SIZE, int(box.text))
                        save_rectangles()
                    except Exception:
                        pass
            if not submitted:
                # if no input box active, allow shortcuts here
                if event.key == pygame.K_a:
                    add_rectangle()
                elif event.key == pygame.K_d:
                    delete_rectangle()
                elif event.key == pygame.K_c:
                    cycle_color()

    # Periodically reload from file if changed
    if time.time() - last_read_time > READ_INTERVAL:
        load_rectangles()
        last_read_time = time.time()

    screen.fill((255, 255, 255))

    # Draw rectangles
    for name, info in rectangles.items():
        rect = info["rect"]
        color = info["color"]
        pygame.draw.rect(screen, color, rect)
        # Highlight selected rectangle
        if name == selected_name:
            pygame.draw.rect(screen, (0, 0, 0), rect, 3)

    # Update input boxes with selected rectangle data
    if selected_name and selected_name in rectangles:
        info = rectangles[selected_name]
        rect = info["rect"]
        if not any(box.active for box in input_boxes.values()):
            # Only update if no box is being edited to avoid overwriting user input
            input_boxes["Name"].text = selected_name
            input_boxes["Name"].txt_surface = small_font.render(selected_name, True, (0, 0, 0))
            input_boxes["X"].text = str(rect.x)
            input_boxes["X"].txt_surface = small_font.render(str(rect.x), True, (0, 0, 0))
            input_boxes["Y"].text = str(rect.y)
            input_boxes["Y"].txt_surface = small_font.render(str(rect.y), True, (0, 0, 0))
            input_boxes["Width"].text = str(rect.width)
            input_boxes["Width"].txt_surface = small_font.render(str(rect.width), True, (0, 0, 0))
            input_boxes["Height"].text = str(rect.height)
            input_boxes["Height"].txt_surface = small_font.render(str(rect.height), True, (0, 0, 0))
    else:
        # Clear inputs if nothing selected
        if not any(box.active for box in input_boxes.values()):
            for box in input_boxes.values():
                box.text = ""
                box.txt_surface = small_font.render("", True, (0, 0, 0))

    # Draw sidebar background and labels
    draw_sidebar()

    # Draw input boxes
    for box in input_boxes.values():
        box.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
