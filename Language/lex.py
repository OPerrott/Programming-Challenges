import shlex

class Lex:
    def __init__(self, line):
        self.lexed_line = []
        self.deconstruct_line(line)
        
    def strip_comment(self, line):
        # Remove anything after ';'
        return line.split(';', 1)[0]

    def deconstruct_line(self, line):
        stripped_line = self.strip_comment(line).strip()
        if not stripped_line or stripped_line.endswith(':'):
            self.lexed_line = [stripped_line] if stripped_line else []
        else:
            self.lexed_line = shlex.split(stripped_line)
            
    def __iter__(self):
        return iter(self.lexed_line)
    
    def __getitem__(self, index):
        return self.lexed_line[index]
    
    def __len__(self):
        return len(self.lexed_line)

if __name__ == '__main__':
    lex_line = Lex('dis, "Hello, World" ;ignore this')
    print(list(lex_line))
    print(lex_line[1])
