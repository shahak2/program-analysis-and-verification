import sys

INVALID_PROGRAM_PATH = ""

SRC_RELATIVE_PATH = "src/"
UTILS_RELATIVE_PATH = 'utils/'

sys.path.insert(1, UTILS_RELATIVE_PATH)

import utils

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
        
        try:
            self.readProgram(program_path)
            self.verifyFormatting()
        except FileNotFoundError:
            utils.printError("The program file was not found.")
            sys.exit(1)
        except PermissionError:
            utils.printError("You don't have permission to access this program file.")
            sys.exit(1)
        except Exception as e:
            utils.printError(f"An error occurred: {e}")
            sys.exit(1)

    def readProgram(self, 
                    program_path):
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
        import re
        lines_results = dict()
        for line_number, line in enumerate(program_lines):
            regex_pattern = r'(L\d+)\s+(.*?)\s+(L\d+)'
            result = re.findall(regex_pattern, line)
            lines_results[line_number] = result[0]
        return lines_results
    
    def parseVariables(self, variables_line):
        variables = list(variables_line.strip().split(" "))
        return variables
    
    def verifyAssumeLineFormat(self, line):
        if "assume" not in line:
            return True
        
        return "assume(" in line
    
    def verifyAssertLineFormat(self, line):
        if "assert" not in line:
            return True
        
        return "assert(" not in line
        
    def verifyLine(self, line):
        return self.verifyAssumeLineFormat(line) and \
            self.verifyAssertLineFormat(line)
        
    def verifyFormatting(self):
        for line in self.program.values():
            statement = line[1]
            if not self.verifyLine(statement):
                utils.printError(f"Invalind line {statement}")
                sys.exit(1)