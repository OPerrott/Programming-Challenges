import time
import os

class Solution:
    @staticmethod
    def maximumWealth(accounts: list[list[int]]) -> int:
            
        
        """
            
            You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the ith customer has in the jth bank. Return the wealth that the richest customer has.

            A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.
            
            Run the code before starting the problem, to make sure that nothing is wrong.
            If you do have a problem related to running the code, contact 'Tenuous'.
            
            Remove the comments and code here when ready.
            
            Enjoy Problem 14
            
        """

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
