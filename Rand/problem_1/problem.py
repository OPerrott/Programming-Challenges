import time
import os

class Solution:
    def romanToInt(s: str) -> int:
        '''
        
        's' is the variable that stores the Roman Numerals.
        
        's' does not need to be the variable returned so you can change it.
        
        Run the code before starting the problem, to make sure that nothing is wrong.
        If you do have a problem related to running the code, contact 'Tenuous'.
        
        Remove the comments and code here when ready.
        
        Enjoy Problem 1
        
        '''
        
        
        
        
        return s
    
    


def main():
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"
    
    answers = {"III": 3, "LVIII": 58, "MCMXCIV": 1994}
    tests = ["III", "LVIII", "MCMXCIV"]
    
    for test in tests:
        expected = answers[test]
        result = Solution.romanToInt(test)
        status = f"{GREEN}" if result == expected else f"{RED}"
        
        print(f"{status}Expectation: {expected}  \tResult: {result}{RESET}")
        


if __name__ == "__main__":
    os.system("cls")
    start_time = time.perf_counter()
    main()
    elapsed = time.perf_counter() - start_time
    print(f"Runtime: {elapsed:.10f} seconds")