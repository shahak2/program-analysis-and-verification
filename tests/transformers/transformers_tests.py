import sys
from enum import StrEnum

SRC_RELATIVE_PATH = "src/"
UTILS_RELATIVE_PATH = "utils/"
DOMAINS_PATH = SRC_RELATIVE_PATH + 'domains/'
PARITY_TRANSFORMER_PATH = SRC_RELATIVE_PATH + 'transformers/'


sys.path.insert(1, DOMAINS_PATH)
sys.path.insert(1, UTILS_RELATIVE_PATH)
sys.path.insert(1, PARITY_TRANSFORMER_PATH)

import utils
from parity_transformer import ParityTransformer
from summation_transformer import SummationTransformer
from summation_domain import SummationDomain
from transformers_consts import *

def perform_test(transformer, test):
    values_vector = test[0]
    statement = test[1]
    expected_vector = test[2]
    result = transformer.parse_statement(statement, 
                                         values_vector)
    if result != expected_vector:
        raise RuntimeError(
            f'Test failed for [{statement}]# {values_vector}\
                \n        Expected {expected_vector} == {result}')
    utils.printInfo(
        f'Test passed: [{statement}]# {values_vector} == {result}')


def parity_transformer_tester():
    utils.printMessage("Parity Transformer Test")
    try:
        utils.printMessage("Short vector tests")
        parity_t = ParityTransformer()
        parity_t.set_variables_to_index_mapping(
            PARITY_MOCK_VARIABLES)
        
        
        for test in PARITY_TESTS:
            perform_test(parity_t, 
                         test)
        
        utils.printMessage("Long vector tests")
        parity_t_long = ParityTransformer()
        parity_t_long.set_variables_to_index_mapping(
            PARITY_MOCK_VARIABLES_LONG)
        
        for test in PARITY_TESTS_LONG:
            perform_test(parity_t_long, 
                         test)
        
    except Exception as e:
        utils.printError(f'{e}')
        return
    utils.printSuccess("All tests Passed!")

def summation_transformer_tester():
    utils.printMessage("Summation Transformer Test")
    try:
        
        s_domain = SummationDomain()
        
        summation_t = s_domain.transformer
        summation_t.set_variables_to_index_mapping(
            SUMMATION_MOCK_VARIABLES)
        
        for test in SUMMATION_TESTS:
            perform_test(summation_t, test)
    except Exception as e:
        utils.printError(f'{e}')
        return
    utils.printSuccess("All tests Passed!")
    
    
def run_tests():
    parity_transformer_tester()
    summation_transformer_tester()

if __name__ == '__main__':
    utils.printMessage(
        "\n=== Transformer Tester ===")
    run_tests()
