import json


class Data:
    def __init__(self):
        self.WINDOW_WIDTH = None
        self.WINDOW_HEIGHT = None
        
        self.WINDOW_POSX = None
        self.WINDOW_POSY = None
        self.WINDOW_POS = self.WINDOW_POSX, self.WINDOW_POSY
    
    def LOAD_WINDOW_DATA(self):
        with open('App Editor\Data\window.json', 'r') as file:
            WindowData = json.load(file)
        
        

    
    




if __name__ == '__main__':
    Data()



with open('App Editor\Data\window.json', 'r') as file:
    data = json.load(file)
    
# Access the first window config
window = data["window"][0]

# Read existing position
pos_x = window["WINDOW-POSX"]
pos_y = window["WINDOW-POSY"]

# Set "WINDOW-POS" to [x, y]
window["WINDOW-POS"] = [pos_x, pos_y]

with open('App Editor\Data\window.json', 'w') as file:
    json.dump(data, file, indent=4)