import requests

class Solution:
    def __init__(self):
        
        self.get_html()
        
        
        
    def get_html(self):
        x = requests.get('https://youtube.com')
        print(x.text)
        
        
        
if __name__ == "__main__":
    Solution()