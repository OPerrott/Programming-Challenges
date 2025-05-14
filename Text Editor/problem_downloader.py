from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
from prompt_toolkit.lexers import Lexer
from prompt_toolkit.formatted_text import to_formatted_text
from prompt_toolkit.document import Document
from prompt_toolkit.completion import WordCompleter

from app import App

from tqdm import tqdm 
import requests
import os

commands = {
    "download"  :   "class:download",
    "help"      :   "class:help",
    "view"      :   "class:view",
    "list"      :   "class:list",
    "ls"        :   "class:ls",
    
    "run"       :   "class:run",
    
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
    
    "run"          :   "#00ff00 bold",
    
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

class Main:
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
        
        if command_key == "run":
            self.run()
        
        if command_key == "download":
            Download(self.tokened_command)
        
        if command_key == "cls" or command_key == "clear":
            self.clear()
    
    
    def run(self):
        App()
    
    
      
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
            url = "https://api.github.com/repos/OPerrott/Programming-Challenges/contents/problems"
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
        
        url = f"https://raw.githubusercontent.com/OPerrott/Programming-Challenges/refs/heads/main/problems/{command_value}/resources/description"
        
        response = requests.get(url)

        if response.status_code == 200:
            print(response.text)
        else:
            print(f"Failed to retrieve file \"{command_value}\"")
            
    def clear(self):
        os.system("clear")
       
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
                self.file_name = "description"    
            
            else:
                print(f"Invalid File Name: \"{self.tokened_command[2]}\"")
        
        
        
        
        self.problem()
        self.resources()
        self.solution()
 
    def problem(self):
        folder_url = f"https://api.github.com/repos/OPerrott/Programming-Challenges/contents/problems/{self.folder_name}/code"
        
        get_folder = requests.get(folder_url)
        
        if get_folder.status_code == 200:
            
            problem_num_folder = os.path.join(os.getcwd(), self.folder_name)
            code_folder = os.path.join(problem_num_folder, "code")
            
            os.makedirs(code_folder, exist_ok=True)
            
            files = get_folder.json()
            for file in tqdm(files, desc=f"    Downloading Problem Code", ncols=80):
                
                file_name = file['name']
                file_url = file['download_url']
                
                get_file = requests.get(file_url)
                
                if get_file.status_code == 200:
                    file_path = os.path.join(code_folder, file_name)
                    with open(file_path, "wb") as f:
                        f.write(get_file.content)
            # print("Download Successful!")
        else:
            print(f"Failed to download \"{file_name}\": {get_folder.status_code}")
    
    def resources(self):
        folder_url = f"https://api.github.com/repos/OPerrott/Programming-Challenges/contents/problems/{self.folder_name}/resources"
        
        get_folder = requests.get(folder_url)
        
        files = get_folder.json()
        if get_folder.status_code == 200:
            problem_num_folder = os.path.join(os.getcwd(), self.folder_name)
            resources_folder = os.path.join(problem_num_folder, "resources")
            
            os.makedirs(resources_folder, exist_ok=True)
            
            for file in tqdm(files, desc=f"    Downloading Resources", ncols=80):
                file_name = file['name']
                file_url = file['download_url']
                
                get_file = requests.get(file_url)
                
                if get_file.status_code == 200:
                    file_path = os.path.join(resources_folder, file_name)
                    with open(file_path, "wb") as f:
                        f.write(get_file.content)
            # print("Download Successful!")
        else:
            print(f"Failed download \"{file_name}\": {get_folder.status_code}")
              
    def solution(self):
        folder_url = f"https://api.github.com/repos/OPerrott/Programming-Challenges/contents/problems/{self.folder_name}/solution"
        
        get_folder = requests.get(folder_url)
        
        files = get_folder.json()
        if get_folder.status_code == 200:
            problem_num_folder = os.path.join(os.getcwd(), self.folder_name)
            solution_folder = os.path.join(problem_num_folder, "solution")
            
            os.makedirs(solution_folder, exist_ok=True)
            
            for file in tqdm(files, desc=f"    Downloading Solution", ncols=80):
                file_name = file['name']
                file_url = file['download_url']
                
                get_file = requests.get(file_url)
                
                if get_file.status_code == 200:
                    file_path = os.path.join(solution_folder, file_name)
                    with open(file_path, "wb") as f:
                        f.write(get_file.content)
            # print("Download Successful!")
        else:
            print(f"Failed download \"{file_name}\": {get_folder.status_code}")
                   
if __name__ == '__main__':
    os.system("clear")
    Main()