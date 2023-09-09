
SRC_RELATIVE_PATH = "../../src/"
PARITY_DOMAIN_PATH = SRC_RELATIVE_PATH + 'domains/'
TOP = "TOP"
BOTTOM = "BOTTOM"
ODD = "ODD"
EVEN = "EVEN"
       
import sys

sys.path.insert(1, PARITY_DOMAIN_PATH)
from parity_domain import *

sys.path.insert(1, "../")
import test_utils

def parity_domain_tester():
    test_utils.printYellow("Test 1: Parity Domain")
    
    parity_d = ParityDomain()
    
    try:
       parity_d = ParityDomain()
       print(f'{TOP} contains {BOTTOM}:, {ParityDomain.parity_contains(TOP, BOTTOM)}')
       print(f'{BOTTOM} contains {TOP}:, {ParityDomain.parity_contains(BOTTOM, TOP)}')
       
       
       
       print()

    except Exception as e:
        test_utils.printError(f'{e}')
        return
    
    print()

    test_utils.printSuccess("Success!")
    


def summation_domain_tester():
    # TODO: Implement
    test_utils.printError(f'summation_domain_tester not Implemented')

def combined_domain_tester():
    # TODO: Implement
    test_utils.printError(f'combined_domain_tester not Implemented')

def run_tests():
    parity_domain_tester()
    summation_domain_tester()
    combined_domain_tester()

if __name__ == '__main__':
    test_utils.printYellow("\n=== Abstract Domains Tester ===")
    run_tests()
