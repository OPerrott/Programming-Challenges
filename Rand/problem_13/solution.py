'''
    WE NEED TO FIND THE INDEX POSITION OF EACH LETTER OF THE ALPHABET IN REVERSE ORDER. (E.G. a=26, z=1)
    USING ORD() WE CAN FIND THE ASCII VALUE OF EACH LETTER. (E.G. ORD('a')=97, ORD('z')=122)
    
    IF WE SUBTRACT THE ORD() OF THE CHARACTER WE WANT TO FIND THE REVERSE INDEX FOR BY THE ORD() OF 'z',
    WE GET THE INVERSE INDEX OF EACH CHARACTER. (E.G. (122(z)-97(a)=25), (122(z)-122(z)=0)),
    THE ONLY PROBLEM WITH THIS IS THAT THE VALUE IS 1 LESS THAT WHAT WE WANT TO GET, SO WE CAN ADD(1) TO THE VALUE.
    
    WE CAN THEN MULTIPLY THE REVERSE INDEX VALUE BY THE NUMBER OF TIMES WE'VE LOOPED (STARTING FROM ONE),
    THIS WILL GIVE US THE PRODUCT OF THE REVERSE INDEX  
'''




import time
import os

class Solution:
    def reverseDegree(s: str) -> int:
        
        
        loops = 1
        result = 0
        ascii_value_of_z =  ord('z')

        for char in s:
            result += (ascii_value_of_z - ord(char) + 1) * loops
            loops += 1
            
            
        return result
        
    


def main():
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"
    
    answers = {"abc": 148, "zaza": 160, "asxiougasc": 879}
    tests = ["abc", "zaza", "asxiougasc"]
    
    for test in tests:
        expected = answers[test]
        result = Solution.reverseDegree(s=test)
        status = f"{GREEN}" if result == expected else f"{RED}"
        
        print(f"{status}Expectation: {expected}\t\tResult: {result}{RESET}")
 
if __name__ == "__main__":
    os.system("cls")
    start_time = time.perf_counter()
    main()
    elapsed = time.perf_counter() - start_time
    print(f"Runtime: {elapsed:.10f} seconds")