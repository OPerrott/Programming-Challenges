import time
import os

class Solution:
    def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
        
        """
            There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.
            Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.
            Note that multiple kids can have the greatest number of candies.
        
            Run the code before starting the problem, to make sure that nothing is wrong.
            If you do have a problem related to running the code, contact 'Tenuous'.
            
            Remove the comments and code here when ready.
            
            Enjoy Problem 16
        """

def main():
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"
    
    tests = [
        ([2,3,5,1,3], [True, True, True, False, True], 3),
        ([4,2,1,1,2], [True, False, False, False, False], 1),
        ([12,1,12,8,15], [True, False, True, True, True], 10)
    ]
    
    for test, expected, extraCandies in tests:
        result = Solution.kidsWithCandies(test, extraCandies)
        status = f"{GREEN}" if result == expected else f"{RED}"
        print(f"{status}Expectation: {expected}\t\tResult: {result}{RESET}")

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    start_time = time.perf_counter()
    main()
    elapsed = time.perf_counter() - start_time
    print(f"Runtime: {elapsed:.10f} seconds")