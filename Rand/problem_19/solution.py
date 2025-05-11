import os
import time


class Solution:
    def smallerNumbersThanCurrent(nums: list[int]) -> list[int]:
        result = []
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if j!=i and nums[j] < nums[i]:
                    count+=1
            result.append(count)

        return result
    
    
def main():
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"
    
    tests = [
        ([8,1,2,2,3], [4,0,1,1,3]),
        ([6,5,4,8], [2,1,0,3]),
        ([7,7,7,7], [0,0,0,0])
    ]
    
    for test1, expected in tests:
        result = Solution.smallerNumbersThanCurrent(test1)
        status = f"{GREEN}" if result == expected else f"{RED}"
        print(f"{status}Expectation: {expected}   \t\tResult: {result}{RESET}")

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    start_time = time.perf_counter()
    main()
    elapsed = time.perf_counter() - start_time
    print(f"Runtime: {elapsed:.10f} seconds")