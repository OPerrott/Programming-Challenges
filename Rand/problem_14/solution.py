import time
import os

class Solution:
    @staticmethod
    def maximumWealth(accounts: list[list[int]]) -> int:
        richest_wealth = 0
        for i in range(len(accounts)):
            sum_wealth = sum(accounts[i])
            if sum_wealth > richest_wealth:
                richest_wealth = sum_wealth
        return richest_wealth
    
    

def main():
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"
    
    tests = [
        ([[1,2,3],[3,2,1]], 6),
        ([[1,5],[7,3],[3,5]], 10),
        ([[2,8,7],[7,1,3],[1,9,5]], 17)
    ]
    
    for test, expected in tests:
        result = Solution.maximumWealth(accounts=test)
        status = f"{GREEN}" if result == expected else f"{RED}"
        print(f"{status}Expectation: {expected}\t\tResult: {result}{RESET}")

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    start_time = time.perf_counter()
    main()
    elapsed = time.perf_counter() - start_time
    print(f"Runtime: {elapsed:.10f} seconds")
