class Solution:
    def __init__(self):
        self.numbers = [56, 2, 6, 11, 7, 20]
        self.sorted_numbers = []
       
        self.selection_sort() 
        
    def selection_sort(self):
        while self.numbers:
            smallest_num = self.numbers[0]
            
            for num in self.numbers:
                if num <= smallest_num:
                    smallest_num = num
            self.sorted_numbers.append(smallest_num)
            self.numbers.remove(smallest_num)
            
        print(self.sorted_numbers)
        
        
if __name__ == "__main__":
    Solution()