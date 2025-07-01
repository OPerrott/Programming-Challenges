from data import *
import tkinter as tk
from PIL import ImageTk, Image


def dis(_Line):
    print(_Line[1])
    
def sub(_Line):
    # Try parsing first argument
    try:
        var1 = int(_Line[1].strip(','))
    except ValueError:
        key = _Line[1].strip(',')
        if key in Data.variables:
            var1 = int(Data.variables[key])
        else:
            print(f"[ERROR] {key} is not a valid variable!")
            return

    # Try parsing second argument
    try:
        var2 = int(_Line[2].strip(','))
    except ValueError:
        key = _Line[2].strip(',')
        if key in Data.variables:
            var2 = int(Data.variables[key])
        else:
            print(f"[ERROR] {key} is not a valid variable!")
            return

    result = var1 - var2
    print(result)  # Or return result
    return result
    
def add(_Line): 
    # Try parsing first argument
    try:
        var1 = int(_Line[1].strip(','))
    except ValueError:
        key = _Line[1].strip(',')
        if key in Data.variables:
            var1 = int(Data.variables[key])
        else:
            print(f"[ERROR] {key} is not a valid variable!")
            return

    # Try parsing second argument
    try:
        var2 = int(_Line[2].strip(','))
    except ValueError:
        key = _Line[2].strip(',')
        if key in Data.variables:
            var2 = int(Data.variables[key])
        else:
            print(f"[ERROR] {key} is not a valid variable!")
            return

    result = var1 + var2
    print(result)  # Or return result
    return result

def mul(_Line): 
    # Try parsing first argument
    try:
        var1 = int(_Line[1].strip(','))
    except ValueError:
        key = _Line[1].strip(',')
        if key in Data.variables:
            var1 = int(Data.variables[key])
        else:
            print(f"[ERROR] {key} is not a valid variable!")
            return

    # Try parsing second argument
    try:
        var2 = int(_Line[2].strip(','))
    except ValueError:
        key = _Line[2].strip(',')
        if key in Data.variables:
            var2 = int(Data.variables[key])
        else:
            print(f"[ERROR] {key} is not a valid variable!")
            return

    result = var1 * var2
    print(result)  # Or return result
    return result

def div(_Line): 
    # Try parsing first argument
    try:
        var1 = int(_Line[1].strip(','))
    except ValueError:
        key = _Line[1].strip(',')
        if key in Data.variables:
            var1 = int(Data.variables[key])
        else:
            print(f"[ERROR] {key} is not a valid variable!")
            return

    # Try parsing second argument
    try:
        var2 = int(_Line[2].strip(','))
    except ValueError:
        key = _Line[2].strip(',')
        if key in Data.variables:
            var2 = int(Data.variables[key])
        else:
            print(f"[ERROR] {key} is not a valid variable!")
            return

    result = var1 / var2
    print(result)  # Or return result
    return result

def run(_Line):

    if _Line[1] == "Image":
        window = tk.Tk()
        window.title(f"{_Line[2]}")
        window.geometry("300x300")
        window.configure(background='grey')

        match _Line[2]:
            case "Filip":
                path = "Language/images/Filip.jpg"
            case "Loic":
                path = "Language/images/Loic.jpg"
            case "Josh":
                path = "Language/images/Josh.jpg"
            case "Mica":
                path = "Language/images/Mica.jpg"
            case "Joao":
                path = "Language/images/Joao.jpg"
            case "Oliver":
                path = "Language/images/Oliver.jpg"
            case "Nathan":
                path = "Language/images/Nathan.jpg"
            case "Maja":
                path = "Language/images/Maja.jpg"
            case "Lucas":
                path = "Language/images/Lucas.jpg"
            case _:
                path = "Language/images/Tree.jpg"

        #Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
        img = ImageTk.PhotoImage(Image.open(path))

        #The Label widget is a standard Tkinter widget used to display a text or image on the screen.
        panel = tk.Label(window, image = img)

        #The Pack geometry manager packs widgets in rows or columns.
        panel.pack(side = "bottom", fill = "both", expand = "yes")

        #Start the GUI
        window.mainloop()