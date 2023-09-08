
INVALID_PROGRAM_PATH = ""

class Parser:
    
    
    def __init__(self, program_path = INVALID_PROGRAM_PATH):
        assert program_path != INVALID_PROGRAM_PATH, f"Invalid path to program file: {program_path}."
        
        with open(program_path) as f:
            lines = f.readlines()
            print(lines)
        


    
    def parseVariables(self, variables_line):
        variables = set(variables_line.split(" "))
        pass







