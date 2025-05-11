import time
import os

class Solution:
    def isPalindrome(x: int) -> bool:
        """
        
        Given an integer x, return true if x is a palindrome, and false otherwise.
        
        Run the code before starting the problem, to make sure that nothing is wrong.
        If you do have a problem related to running the code, contact 'Tenuous'.
        
        Remove the comments and code here when ready.
        
        Enjoy Problem 1
        
        """
        
        return x
        
    


def main():
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"
    
    answers = {121: True, -121: False, 10: False}
    tests = [121, -121, 10]
    
    for test in tests:
        expected = answers[test]
        result = Solution.isPalindrome(x=test)
        status = f"{GREEN}" if result == expected else f"{RED}"
        
        print(f"{status}Expectation: {expected}\t\tResult: {result}{RESET}")
        

    




if __name__ == "__main__":
    os.system("cls")
    start_time = time.perf_counter()
    main()
    elapsed = time.perf_counter() - start_time
    print(f"Runtime: {elapsed:.10f} seconds")