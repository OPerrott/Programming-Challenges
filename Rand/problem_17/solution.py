import time
import os

class Solution:
    def arrayStringsAreEqual(word1: list[str], word2: list[str]) -> bool:
        
        word1 = "".join(word1)
        word2 = "".join(word2)
        return True if word1 == word2 else False

def main():
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"
    
    tests = [
        (["ab", "c"], ["a", "bc"], True),
        (["a", "cb"], ["ab", "c"], False),
        (["abc", "d", "defg"], ["abcddefg"], True)
    ]
    
    for test1, test2, expected in tests:
        result = Solution.arrayStringsAreEqual(test1, test2)
        status = f"{GREEN}" if result == expected else f"{RED}"
        print(f"{status}Expectation: {expected}\t\tResult: {result}{RESET}")

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    start_time = time.perf_counter()
    main()
    elapsed = time.perf_counter() - start_time
    print(f"Runtime: {elapsed:.10f} seconds")