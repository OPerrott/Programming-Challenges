import time
import os

class Solution:
    def reverseDegree(s: str) -> int:
        """
        
        Given a string s, calculate its reverse degree.

        The reverse degree is calculated as follows:

        1. For each character, multiply its position in the reversed alphabet ('a' = 26, 'b' = 25, ..., 'z' = 1) with its position in the string (1-indexed).
        2. Sum these products for all characters in the string.
        Return the reverse degree of s.
        
        Run the code before starting the problem, to make sure that nothing is wrong.
        If you do have a problem related to running the code, contact 'Tenuous'.
        
        Remove the comments and code here when ready.
        
        Enjoy Problem 13
        
        """
        
        return s
        
    


def main():
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"
    
    answers = {"abc": 148, "zaza": 160, "asxiougasc": 879}
    tests = ["abc", "zaza", "asxiougasc"]
    
    for test in tests:
        expected = answers[test]
        result = Solution.reverseDegree(s=test)
        status = f"{GREEN}" if result == expected else f"{RED}"
        
        print(f"{status}Expectation: {expected}\t\tResult: {result}{RESET}")
 
if __name__ == "__main__":
    os.system("cls")
    start_time = time.perf_counter()
    main()
    elapsed = time.perf_counter() - start_time
    print(f"Runtime: {elapsed:.10f} seconds")