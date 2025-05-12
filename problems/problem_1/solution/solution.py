import time
import os

class Solution:
    def romanToInt(s: str) -> int:
        conv = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        
        for char in s:
            number+= conv[char]
        return number
    
    


def main():
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"
    
    answers = {"III": 3, "LVIII": 58, "MCMXCIV": 1994}
    tests = ["III", "LVIII", "MCMXCIV"]
    
    for test in tests:
        expected = answers[test]
        result = Solution.romanToInt(test)
        status = f"{GREEN}" if result == expected else f"{RED}"
        
        print(f"{status}Expectation: {expected}  \tResult: {result}{RESET}")
        

    




if __name__ == "__main__":
    os.system("cls")
    start_time = time.perf_counter()
    main()
    elapsed = time.perf_counter() - start_time
    print(f"Runtime: {elapsed:.10f} seconds")
