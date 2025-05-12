from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
from prompt_toolkit.lexers import Lexer
from prompt_toolkit.formatted_text import to_formatted_text
from prompt_toolkit.document import Document
from prompt_toolkit.completion import WordCompleter

import requests
import os


commands = {
    "download"  :   "class:download",
    "help"      :   "class:help",
    "view"      :   "class:view",
    "list"      :   "class:list",
    "ls"        :   "class:ls",
    
    "end"       :   "class:end",
    "stop"      :   "class:stop",
    
    "cls"       :   "class:cls",
    "clear"     :   "class:clear"
}

# Define the styles
style = Style.from_dict({
    "download"  :   "#00ff00 bold",
    "help"      :   "#00ff00 bold",
    "view"      :   "#00ff00 bold",
    
    "list"      :   "#00ff00 bold",
    "ls"        :   "#00ff00 bold",
    
    "end"       :   "#00ff00 bold",
    "stop"      :   "#00ff00 bold",  
    
    "cls"       :   "#00ff00 bold",
    "clear"     :   "#00ff00 bold",
})


completer = WordCompleter(commands, ignore_case=True)

# Custom Lexer to color matching words
class CommandLexer(Lexer):
    def lex_document(self, document: Document):
        text = document.text

        def get_line(lineno):
            tokens = []
            for word in text.split():
                style_class = commands.get(word, "")
                tokens.append((style_class, word + " "))
            return to_formatted_text(tokens)
        
        return get_line

class Ollieversal:
    def __init__(self):
        self.running = True   
        
        self.loaded()
               
    def loaded(self):
        while self.running:
            self.command = prompt("% ", lexer=CommandLexer(), completer=completer, style=style)

            self.tokened_command = self.command.split()
            self.check_command()
       
    def check_command(self):
        
        command_key = self.command.split()[0]
                
        if command_key == "stop" or command_key == "end":
            self.running = False
            
        if command_key == "list" or command_key == "ls":
            self.ls()
            
        if command_key == "view":
            self.view()
        
        if command_key == "download":
            Download(self.tokened_command)
        
        if command_key == "cls" or command_key == "clear":
            self.clear()
            
    def ls(self):
        
        ls_commands = ["commands", "problems"]
        
        
        command_value = None
        if len(self.tokened_command) >= 2:
            if self.tokened_command[1] in ls_commands:
                command_value = self.tokened_command[1]
            else:
                print(f"\"{self.tokened_command[1]}\" is invalid!")
                command_value = "Null"
                
            
        if command_value == "commands" or command_value == None:
            for command in commands:
                if command in ["list", "clear", "stop"]:
                    pass
                else:
                    print(f"    {command}")

        if command_value == "problems":
            url = "https://api.github.com/repos/OPerrott/Programming-Challenges/contents"
            response = requests.get(url)
            
            if response.status_code == 200:
                folders = response.json()
                for folder in folders:
                    
                    if ".txt" in folder["name"]:
                        pass
                    else:
                        print(folder["name"])
            else:
                print(f"Failed to list problems: {response.status_code}")
        
    def view(self):
        
        command_value = None
        if len(self.tokened_command) >= 2:
            command_value = self.tokened_command[1]
        else:
            command_value = input("Problem <<< ")
        
        url = f"https://raw.githubusercontent.com/OPerrott/Programming-Challenges/refs/heads/main/{command_value}/description.txt"
        
        response = requests.get(url)

        if response.status_code == 200:
            print(response.text)
        else:
            print(f"Failed to retrieve file \"{command_value}\"")
            
    def clear(self):
        os.system("cls")
       
class Download:
    def __init__(self, tokened_command):
        
        self.tokened_command = tokened_command
        
        self.folder_name = None
        self.file_name = None
        
        self.check_download_type()
        
    def check_download_type(self):
        if len(self.tokened_command) == 1:  # If command == "download"
            self.folder_name = input("Problem <<< ")
            self.file_name = "problem.py"
        elif len(self.tokened_command) == 2:    # If command == "download + folder_name"
            self.folder_name = self.tokened_command[1]
            self.file_name = "problem.py"
        elif len(self.tokened_command) == 3:    # If command == "download + folder_name + file_name"
            
            self.folder_name = self.tokened_command[1]
            
            if self.tokened_command[2] == "problem":
                self.file_name = "problem.py"
            elif self.tokened_command[2] == "solution":
                self.file_name = "solution.py"
            elif self.tokened_command[2] == "description":
                self.file_name = "description.txt"    
            
            else:
                print(f"Invalid File Name: \"{self.tokened_command[2]}\"")
        
        
        self.url = f"https://raw.githubusercontent.com/OPerrott/Programming-Challenges/main/{self.folder_name}/{self.file_name}"
        self.download()
            
    def download(self):
        
        response = requests.get(self.url)

        if response.status_code == 200:
            mkdir = os.path.join(os.getcwd(), self.folder_name)    # Stores the future folder path of the problem

            if not os.path.exists(mkdir):   # Checks if the folder thats going to store the problem already exists
                os.makedirs(mkdir)  #   Makes the folder with appropriate name if the folder doesn't exist

            file_path = os.path.join(mkdir, f"{self.file_name}")   # Stores the future file path of the problem
            with open(file_path, "wb") as problem:
                problem.write(response.content)

            print("Download successful.")
        else:
            print(f"Failed to download file: \"{self.file_name}\"")
        
if __name__ == '__main__':
    os.system("cls")
    Ollieversal()