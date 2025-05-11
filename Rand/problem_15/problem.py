import time
import os

class Solution:
    def smallestEvenMultiple(n: int) -> int:
        """
                    
            Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.
            
            Run the code before starting the problem, to make sure that nothing is wrong.
            If you do have a problem related to running the code, contact 'Tenuous'.
            
            Remove the comments and code here when ready.
            
            Enjoy Problem 15

        """



def main():
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"
    
    answers = {6: 6, 32: 32, 15: 30}
    tests = [6, 32, 15]
    
    for test in tests:
        expected = answers[test]
        result = Solution.smallestEvenMultiple(n=test)
        status = f"{GREEN}" if result == expected else f"{RED}"
        
        print(f"{status}Expectation: {expected}\t\tResult: {result}{RESET}")
 
if __name__ == "__main__":
    os.system("cls")
    start_time = time.perf_counter()
    main()
    elapsed = time.perf_counter() - start_time
    print(f"Runtime: {elapsed:.10f} seconds")