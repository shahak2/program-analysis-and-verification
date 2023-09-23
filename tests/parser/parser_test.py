import sys

SRC_RELATIVE_PATH = "src/"
PARSER_RELATIVE_PATH = SRC_RELATIVE_PATH + 'parser/'
UTILS_RELATIVE_PATH = "utils/"

sys.path.insert(1, UTILS_RELATIVE_PATH)
sys.path.insert(1, PARSER_RELATIVE_PATH)

from parser import Parser
import utils

def parser_tester():
    utils.printMessage("Test 1: language_example.txt")
    
    TESTER_PROGRAM_PATH = SRC_RELATIVE_PATH +\
        "../programs/examples/language_example.txt"
    expected_variables_results = ['n', 'i', 'j']
    
    try:
        p = Parser(TESTER_PROGRAM_PATH)
        assert p.variables == expected_variables_results, \
            "The parsed variables are incorrect"
        assert len(p.program) == 8, \
            "The parsed program is incorrect"
        
        invalid_lines = list(
            filter(
                lambda line: len(line) != 3, p.program.values()))
        if len(invalid_lines) > 0:
            utils.printError(
                f"Invalid lines:\n {invalid_lines}")
            return

    except Exception as e:
        utils.printError(f'{e}')
        return
    utils.printInfo("Program variables:")
    utils.printInfo(p.variables)
    utils.printInfo("Program lines:")
    utils.printInfo(p.program)
    utils.printSuccess("Success!")
    
def run_tests():
    utils.printMessage("Running tests")
    parser_tester()

if __name__ == '__main__':
    utils.printMessage("\n=== Parser Tester ===")
    run_tests()
