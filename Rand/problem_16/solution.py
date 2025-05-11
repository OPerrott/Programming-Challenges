import time
import os

class Solution:
    def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
        
        start_largest_candies = 0
        result = []

        for i in candies:
            if start_largest_candies < i:  start_largest_candies = i

        for i in candies:
            plus_extra_candies = i + extraCandies

            if plus_extra_candies >= start_largest_candies:
                result.append(True)
            else:
                result.append(False)

        return result
    
    




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