class Solution:
    def __init__(self):
        self.numbers = [56, 2, 6, 11, 7, 20]
        self.sorted_numbers = []
       
        self.selection_sort() 
        
    def selection_sort(self):
        '''
        Your objective is to make a function that follows the selection sort algorithm.
        
        This is when the smallest number in the list is removed and added to the start.
        In this case you have to move the smallest number to the 'sorted_numbers' list.
                
        Run the code before starting the problem, to make sure that nothing is wrong.
        If you do have a problem related to running the code, contact 'Tenuous'.
        
        Remove the comments and code here when ready.
        
        Enjoy Problem 2 
        '''
        
        print(self.sorted_numbers)
        
        
if __name__ == "__main__":
    Solution()