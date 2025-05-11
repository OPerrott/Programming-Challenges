import keyboard
import time
import os

class Solution:
    def bruteforce() -> None:
        '''
        
        For this problem you do not have to return anything.
        Your objective is to use the 'keyboard' import to create a brute force program that will be used to find the password of the account with the username "Tenuous".
        
        You should have been given two other files than this one. Those being "passwords.txt" and "login.py".
        "passwords.txt" contains a list the 500 most common passwords.
        "login.py" contains a simple Tkinter application that will simulate a login page. This is what you will be using the brute force program on.
        
        All code completed by the participant must be in this file.  
        
        Run the code before starting the problem, to make sure that nothing is wrong.
        If you do have a problem related to running the code, contact 'Tenuous'.
        
        Remove the comments and code here when ready.
        
        Enjoy Problem 3
        
        '''
    
if __name__ == "__main__":
    os.system("cls")
    start_time = time.perf_counter()
    Solution.bruteforce()
    elapsed = time.perf_counter() - start_time
    print(f"Runtime: {elapsed:.10f} seconds")