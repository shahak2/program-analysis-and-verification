import re

INVALID_PROGRAM_PATH = ""

class Parser:
    """
        Parser:
            Gets a path to a program text file.
            Sets the fields:
                variables: The set of variables in the program
                program:   A list of tuples: (current label, statement, following label) 
    """
    
    def __init__(self, program_path = INVALID_PROGRAM_PATH):
        assert program_path != INVALID_PROGRAM_PATH, f"Invalid path to program file: {program_path}."
        
        with open(program_path) as f:
            raw_lines = f.readlines()
            lines = list(
                filter(lambda line: line != "", 
                       map(lambda line: line.strip(), raw_lines)))
            
            variables_line = lines[0]
            program = lines[1:]
            
            self.variables = self.parseVariables(variables_line)
            self.program = Parser.splitLabels(program)
    
    def splitLabels(program_lines):
        lines_results = dict()
        for line_number, line in enumerate(program_lines):
            regex_pattern = r'(L\d+)\s+(.*?)\s+(L\d+)'
            result = re.findall(regex_pattern, line)
            lines_results[line_number] = result[0]
        return lines_results
    
    def parseVariables(self, variables_line):
        variables = list(variables_line.strip().split(" "))
        return variables