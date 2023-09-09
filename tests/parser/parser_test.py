
SRC_RELATIVE_PATH = "../../src/"
PARSER_RELATIVE_PATH = SRC_RELATIVE_PATH + 'parser/'

import sys
sys.path.insert(1, PARSER_RELATIVE_PATH)
sys.path.insert(1, "../")

from parser import Parser
import test_utils

def parser_tester():
    test_utils.printYellow("Test 1: language_example.txt")
    
    TESTER_PROGRAM_PATH = SRC_RELATIVE_PATH + "../programs/examples/language_example.txt"
    expected_variables_results = {'i', 'j', 'n'}
    
    try:
        p = Parser(TESTER_PROGRAM_PATH)
        assert p.variables == expected_variables_results, "The parsed variables are incorrect"
        assert len(p.program) == 8, "The parsed program is incorrect"
        
        invalid_lines = list(filter(lambda line: len(line) != 3, p.program.values()))
        if len(invalid_lines) > 0:
            test_utils.printError(f"Invalid lines:\n {invalid_lines}")
            return

    except Exception as e:
        test_utils.printError(f'{e}')
        return
    print()
    test_utils.printInfo("Program variables:")
    test_utils.printInfo(p.variables)
    print()
    test_utils.printInfo("Program lines:")
    test_utils.printInfo(p.program)
    test_utils.printSuccess("Success!")
    

def run_tests():
    test_utils.printYellow("Running tests")
    parser_tester()

if __name__ == '__main__':
    test_utils.printYellow("\n=== Parser Tester ===")
    run_tests()
