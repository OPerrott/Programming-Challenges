import os


files = []



class RnsmWr:
    def __init__(self):
        self.locate_docs_folder()
    
    def locate_docs_folder(self):
        os.chdir("..")

        for folder in os.listdir():
            if folder == 'documents':
                os.chdir("documents")
            else:
                pass
    

if __name__ == "__main__":
    os.system("CLS")
    RnsmWr()