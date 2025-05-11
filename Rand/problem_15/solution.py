import time
import os

class Solution:
    def smallestEvenMultiple(n: int) -> int:
        smallest_num = 0
        count = 1
        while True:
            result = n * count
            if result % 2 == 0:
                smallest_num = result
                break

            count+=1
        return smallest_num



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