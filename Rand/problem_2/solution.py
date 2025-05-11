import random
import time
import os

class Solution:
    def fibonacci(n: int) -> list:
        fib = [0, 1]
        iterations = n
        
        for i in range(2, iterations):
            next_fib = fib[i-2] + fib[i-1]
            fib.append(next_fib)
            
        return fib
    
    


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
    
    
    
'''

prev_num = 0
next_num = 0

for i in range(0, n):
    
    if i == 0:
        print(0)
    if i == 1:
        print(1)
        prev_num = 1
    else:
        result = prev_num + next_num
        print(result)
        next_num = prev_num
        prev_num = result
'''