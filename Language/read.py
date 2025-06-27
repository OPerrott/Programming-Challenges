from functions import *
from lex import *
from data import *

class Read:
    def __init__(self, file: str = "Language/fail.gm"):
        
        self.inVars = False
        
        with open(file, 'r') as code:
            lines = code.readlines()

            for line in lines:
                lex_line = Lex(line)
                self.read_line(list(lex_line))
                
                
    def read_line(self, lex_line):
        
        if lex_line == ["vars"]: self.inVars = True
        
        if lex_line == ["}"] and self.inVars: 
            self.inVars = False
        elif self.inVars:
            if lex_line == ["{"] or lex_line == ["vars"] or lex_line == []:
                pass
            else:
                Data.variables[lex_line[0].strip(',')] = lex_line[1]
        
        
        if len(lex_line) !=0:
            match lex_line[0].strip(','):
                case "dis":
                    dis(lex_line)
                case "sub":
                    sub(lex_line)
                case "add":
                    add(lex_line)
                case "mul":
                    mul(lex_line)
                case "div":
                    div(lex_line)
                case "run":
                    run(lex_line)
            
        
        
    