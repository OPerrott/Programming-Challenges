import random
import time
import os

class Solution:
    def fibonacci(n: int) -> list:
        '''
        
        'n' is the variable that stores the number of fibonacci numbers to be outputted.
        
        'n' does not need to be the variable returned so you can change it.
        
        Run the code before starting the problem, to make sure that nothing is wrong.
        If you do have a problem related to running the code, contact 'Tenuous'.
        
        Remove the comments and code here when ready.
        
        Enjoy Problem 2
        
        '''
    
        return n
    
    


def main():
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"
    
    tests = [18, 5, 30]
    
    
    for test in tests:
        result = Solution.fibonacci(test)
        rand = random.randint(2, test-1)
        
        if type(result) == list:
            status=f"{GREEN}" if result[rand] == result[rand-1] + result[rand-2] else f"{RED}"
        else:
            status=f"{RED}" if type(result) == int or str else f"{GREEN}"
            
        print(f"{status}Result: {result}{RESET}")
    

if __name__ == "__main__":
    os.system("cls")
    start_time = time.perf_counter()
    main()
    elapsed = time.perf_counter() - start_time
    print(f"Runtime: {elapsed:.10f} seconds")