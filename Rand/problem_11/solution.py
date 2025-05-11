import time
import os

class Solution:
    def defangIPaddr(address: str) -> str:
        return address.replace(".", "[.]")
    


def main():
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"
    
    answers = {"1.1.1.1": "1[.]1[.]1[.]1", "255.100.50.0": "255[.]100[.]50[.]0"}
    tests = ["1.1.1.1", "255.100.50.0"]
    
    for test in tests:
        expected = answers[test]
        result = Solution.defangIPaddr(address=test)
        status = f"{GREEN}" if result == expected else f"{RED}"
        
        print(f"{status}Expectation: {expected}\t\tResult: {result}{RESET}")
        

    




if __name__ == "__main__":
    os.system("cls")
    start_time = time.perf_counter()
    main()
    elapsed = time.perf_counter() - start_time
    print(f"Runtime: {elapsed:.10f} seconds")