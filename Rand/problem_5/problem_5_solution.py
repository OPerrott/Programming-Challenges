import time
import os

class Solution:
    def __init__(self, action):   
        
        self.encr_key = {"a": "c", "b": "d", "c": "e", "d": "f", "e": "g", "f": "h",                # Initiate the encrypt key which will be useds to swap the letters
                         "g": "i", "h": "j", "i": "k", "j": "l", "k": "m", "l": "n",
                         "m": "o", "n": "p", "o": "q", "p": "r", "q": "s", "r": "t",
                         "s": "u", "t": "v", "u": "w", "v": "x", "w": "y", "x": "z",
                         "y": "a", "z": "b",
                         "A": "C", "B": "D", "C": "E", "D": "F", "E": "G", "F": "H",
                         "G": "I", "H": "J", "I": "K", "J": "L", "K": "M", "L": "N",
                         "M": "O", "N": "P", "O": "Q", "P": "R", "Q": "S", "R": "T",
                         "S": "U", "T": "V", "U": "W", "V": "X", "W": "Y", "X": "Z",
                         "Y": "A", "Z": "B",
                         " ": "?", "!": "\"", "\"": "!", "$": "%", "%": "$", "*": "(", "(": "*",
                         ")": ",", ",": ")", ".": "#", "@": "]", "&": "-", "^": "=",
                         "1": "3", "2": "4", "3": "5", "4": "6", "5": "7", "6": "8", "7": "9",
                         "8": "0", "9": "1", "0": "2"}
        
        self.decr_key = {"a": "y", "b": "z", "c": "a", "d": "b", "e": "c", "f": "d",                # Initiate the decrypt key which will be used to swap back the letters
                         "g": "e", "h": "f", "i": "g", "j": "h", "k": "i", "l": "j", 
                         "m": "k", "n": "l", "o": "m", "p": "n", "q": "o", "r": "p",
                         "s": "q", "t": "r", "u": "s", "v": "t", "w": "u", "x": "v",
                         "y": "w", "z": "x", 
                         "A": "Y", "B": "Z", "C": "A", "D": "B", "E": "C", "F": "D",
                         "G": "E", "H": "F", "I": "G", "J": "H", "K": "I", "L": "J",
                         "M": "K", "N": "L", "O": "M", "P": "N", "Q": "O", "R": "P",
                         "S": "Q", "T": "R", "U": "S", "V": "T", "W": "U", "X": "V",
                         "Y": "W", "Z": "X",
                         "?": " ", "\"": "!", "!": "\"", "%": "$", "$": "%", "(": "*", "*": "(", ",": ")", ")": ",", "#": ".", "]": "@", "-" : "&", "=": "^",
                         "3": "1", "4": "2", "5": "3", "6": "4", "7": "5", "8": "6", "9": "7", "0": "8", "1": "9", "2": "0"}
        
        
        
        if action == "ENCRYPT":
            self.Encrypt()
        elif action == "DECRYPT":
            self.Decrypt()
        else:
            print("[ERROR] ACTION NOT FOUND")
    
    
    
    def Encrypt(self):
        with open('problem_5/IMPORTANT_WORK_DATA.txt', 'r') as file:
            lines = [lines.strip() for lines in file]
        
        converted_lines = []
        for line in lines:
            converted_line = []
            for char in line:
                conv = self.encr_key[char]
                
                if len(converted_line) == 0:
                    converted_line.append(conv)
                else:
                    converted_line[0] += conv
            converted_lines.append(converted_line)
        
        converted_lines = [item[0] + '\n' for item in converted_lines]
        
        file = open('problem_5/IMPORTANT_WORK_DATA.txt', 'w')
        file.writelines(converted_lines)
        file.close()
        
        
        
        
        
    
    def Decrypt(self):
        with open('problem_5/IMPORTANT_WORK_DATA.txt', 'r') as file:
            lines = [lines.strip() for lines in file]
        
        converted_lines = []
        for line in lines:
            converted_line = []
            for char in line:
                conv = self.decr_key[char]
                
                if len(converted_line) == 0:
                    converted_line.append(conv)
                else:
                    converted_line[0] += conv
            converted_lines.append(converted_line)
        
        converted_lines = [item[0] + '\n' for item in converted_lines]
        
        file = open('problem_5/IMPORTANT_WORK_DATA.txt', 'w')
        file.writelines(converted_lines)
        file.close()
                

        
        
    
if __name__ == "__main__":
    os.system("cls")
    start_time = time.perf_counter()
    #Solution("ENCRYPT")
    Solution("DECRYPT")
    elapsed = time.perf_counter() - start_time
    print(f"Runtime: {elapsed:.10f} seconds")