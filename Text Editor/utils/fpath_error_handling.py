import json
import os

RED_TEXT = "\033[91m"
RESET_COLOUR_TEXT = "\033[0m"

ERRORS_FILE_PATH = r"Text Editor\utils\errors.json"

class File_Path_Error_Handling:
    def __init__(self, file_path=None, error_name=None):
        self.read_error_file()
        
        print(RED_TEXT, f"[ERROR] {self.errors[error_name]["Error_Message"].format(file_path)}", RESET_COLOUR_TEXT)
        # FINSH LOGIC FOR ERROR HANDLING
        
    def read_error_file(self):
        with open(ERRORS_FILE_PATH, 'r') as f:
            self.errors = json.load(f)
        

            
    def display_errors(self):
        for error in self.errors:
            print(error)

if __name__ == '__main__':
    os.system('cls')
    
    File_Path_Error_Handling(file_path=r"Text Edi", error_name="NAMING_ERROR")