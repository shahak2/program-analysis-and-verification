
SRC_RELATIVE_PATH = "../../src/"
PARSER_RELATIVE_PATH = SRC_RELATIVE_PATH + 'parser/'



import sys
sys.path.insert(1, PARSER_RELATIVE_PATH)
sys.path.insert(1, "../")

from parser import Parser
import test_utils

print(test_utils)

def parser_tester():
    test_utils.printYellow("Test 1: ...")
    
    TESTER_PROGRAM_PATH = SRC_RELATIVE_PATH + "../programs/examples/language_example.txt"
    
    try:
        p = Parser(TESTER_PROGRAM_PATH)
        
    except Exception as e:
        test_utils.printError(f'{e}')
    

def run_tests():
    test_utils.printYellow("Running tests")
    parser_tester()

if __name__ == '__main__':
    test_utils.printYellow("\n=== Parser Tester ===")
    run_tests()
