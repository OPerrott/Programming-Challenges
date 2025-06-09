import tkinter
import os


class Main:
    def __init__(self):
        self.run()

    def run(self):
        App()

class Settings:
    def __init__(self):
        self.resolution = "800x200"

        self.settings = {}

        self.read()
    
    def read(self):
        with open(r'Text Editor\Data\data.txt', 'r') as s:
            self.s = s.readlines()

        self.load()
    
    def load(self):
        for setting in self.s:
            setting = setting.strip("\n").split()

            print(setting)



class App(Settings):
    def __init__(self):
        super().__init__()

        self.init_window()
        
    
    def init_window(self):
        self.window = tkinter.Tk()
        self.window.geometry(self.resolution)
        self.window.configure(background='#2B2B2B')

        self.window.mainloop()








if __name__ == "__main__":

    os.system('cls')

    CLASS = input("Which class do you want to test? ")

    if CLASS.lower() == "main" or CLASS.lower() == None:
        Main()
    if CLASS.lower() == "settings":
        Settings()