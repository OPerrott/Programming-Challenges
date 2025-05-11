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
        
        # We want to check the action to be carried out
        if action == "ENCRYPT":
            self.Encrypt()  # If ENCRYPT then we will run the Encrypt function
        elif action == "DECRYPT":
            self.Decrypt()  # If DECRYPT then we will run the Decrypt function
        else:
            print("[ERROR] ACTION NOT FOUND")   # If its anything else, then we will print an error and do nothing
        
        
    
    
    def Encrypt(self):
        with open('problem_5/IMPORTANT_WORK_DATA.txt', 'r') as file: # We want to open the file in read only mode and save it to the variable "file"
            line = [line.strip() for line in file] # We want to loop through the lines in the file and store them in the list "words"
            
            
        converted_lines = []    # List used to store all the encrypted lines
        for word in line:      # We want to loop through each line in
            converted_line = []   # List used to store the 1 encrypted line
            for char in word:   # We want to loop through each character in each word
                conv = self.encr_key[char]  # Compare the character to the dictionary and convert it
                
                if len(converted_line) == 0:    # We want to check if the list converted_line has any elements in it because we want to ammend the string of the first element
                                                # If the list is empty then an error would occur
                    converted_line.append(conv) # We append the converted_line list with the converted character
                else:   # If the converted_line list has an element in it
                    converted_line[0] += conv   # We add the next character to the first element
        
            converted_lines.append(converted_line)  # Append the converted_lines list with the converted line
        
        
        # We want to avoid an embedded list         e.g. ->     [[''], [''], ['']]
        # So we use this for loop to re-add them to the  converted_lines list without it being imbedded
        # We also use "\n" to allow for a new line when we get to the end of a line and need to go to the next one
        converted_lines = [item[0] + '\n' for item in converted_lines]  
        
        
        
        file = open('problem_5/IMPORTANT_WORK_DATA.txt', 'w')   # We want to re-open the file in write mode and saving it to the same variable
        file.writelines(converted_lines)    # We write all the lines from converted_lines to the file, replacing all the old file data
        file.close() # We close the file
        
        
        
    
    # All code below is the same as above but with a different key name
    def Decrypt(self):
        with open('problem_5/IMPORTANT_WORK_DATA.txt', 'r') as file:
            words = [line.strip() for line in file]
             
        converted_lines = []
        for word in words:
            converted_word = []   
            for char in word:
                conv = self.decr_key[char]
                
                if len(converted_word) == 0:
                    converted_word.append(conv)
                else:
                    converted_word[0] += conv
        
            converted_lines.append(converted_word)
        
        
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