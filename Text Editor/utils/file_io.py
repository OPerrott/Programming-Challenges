import json
import os


class File_IO:
    def __init__(self, file_path: str="", action: str="Read", text: str=""):
        self.NAMING_ERROR = f"\033[91m[ERROR] \"{file_path}\" is not a valid file path!\033[0m"
        self.NONE_ERROR = f"\033[91m[ERROR] No file path entered!\033[0m"

        self.action = action
        self.text = text
        
        
        self.file_name=file_path
        self.output=None
        
        self.valid_file() if len(self.file_name)!= 0 else print(self.NONE_ERROR)      # Checks if the file is valid
        

    def valid_file(self):
        valid = os.path.isfile(self.file_name)
        supported_types = ["txt", "json", "csv", "md"]
        
        file_type = self.file_name.find('.')
        if file_type!= -1:  file_type = self.file_name[file_type + 1:]
    
        if valid and file_type in supported_types:
            self.get_file_type(file_type)
        else:
            print(self.NAMING_ERROR)
            
    def get_file_type(self, file_type):
        match file_type, self.action.lower():
            case "txt", "r" | "read":
                self.read_txt()
            case "txt", "w" | "write":
                self.write_txt()
                
            case "json", "r" | "read":
                self.read_json()

    
    def read_txt(self):
        with open(f"{self.file_name}", 'r') as f:
            self.output = f.readlines()
    
    def write_txt(self):
        with open(f"{self.file_name}", 'w') as f:
            f.write(self.text)
        
    def read_json(self):
        with open(f"{self.file_name}", 'r') as f:
            self.output = json.load(f)
    
    def write_json(self):
        ...

                
                
                
                
                
                
                
                
                
                
                
    def __iter__(self):
        return iter(self.output or [])
    
    def __getitem__(self, key):
        if self.output is None:
            raise KeyError(f"No data loaded.")
        return self.output[key]            
        
    def __str__(self):
        return "" if self.output is None else str(self.output)
                

if __name__ == '__main__':
    os.system('cls')