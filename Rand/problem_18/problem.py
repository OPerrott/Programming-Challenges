import time
import os

class Solution:
    def sum(num1: int, num2: int) -> int:
        """
                    
            Given two integers num1 and num2, return the sum of the two integers.
            
            Run the code before starting the problem, to make sure that nothing is wrong.
            If you do have a problem related to running the code, contact 'Tenuous'.
            
            Remove the comments and code here when ready.
            
            Enjoy Problem 18

        """



def main():
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"
    
    tests = [
        (5, 2, 7),
        (10, -4, 6),
        (512, -129387, -128875)
    ]
    
    for test1, test2, expected in tests:
        result = Solution.sum(test1, test2)
        status = f"{GREEN}" if result == expected else f"{RED}"
        print(f"{status}Expectation: {expected}   \t\tResult: {result}{RESET}")

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    start_time = time.perf_counter()
    main()
    elapsed = time.perf_counter() - start_time
    print(f"Runtime: {elapsed:.10f} seconds")