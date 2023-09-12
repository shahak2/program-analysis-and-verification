import sys
from enum import StrEnum


SRC_RELATIVE_PATH = "src/"
PARITY_DOMAIN_PATH = SRC_RELATIVE_PATH + 'domains/'
TESTS_RELATIVE_PATH = "tests/"


sys.path.insert(1, PARITY_DOMAIN_PATH)
sys.path.insert(1, TESTS_RELATIVE_PATH)

import parity_consts
from parity_domain import ParityDomain
import test_utils


class OPERATIONS(StrEnum):
    meet = "meet"
    join = "join"
    contains = "contains"
    

def test_contains_relations(domain, operation, relations):
    test_utils.printYellow(f"Operation {operation} Valid Test")
    for relation in relations:
        test_utils.printInfo(f'Testing: {relation[0]:7} <=  {relation[1]:7} =  {relation[2]} ')
        assert getattr(domain, operation)(relation[0], relation[1]) == relation[2], "Invalid result"
        
def test_valid_relations(domain, operation, relations, is_symmetric_relation = True):
    test_utils.printYellow(f"Operation {operation} Valid Test")
    for relation in relations:
        test_utils.printInfo(f'Testing: {relation[0]:7} {operation}  {relation[1]:7} =  {relation[2]} ')
        assert getattr(domain, operation)(relation[0], relation[1]) == relation[2], "Invalid result"
        if is_symmetric_relation:
            assert getattr(domain, operation)(relation[1], relation[0]) == relation[2], "Invalid result"

def test_invalid_relations(domain, operation, relations, is_symmetric_relation = True):
    test_utils.printYellow(f"Operation {operation} Invalid Test")
    for relation in relations:
        test_utils.printInfo(f'Testing: {relation[0]:7} {operation}  {relation[1]:7} =  {relation[2]} ')
        assert getattr(domain, operation)(relation[0], relation[1]) != relation[2], "Invalid result"
        if is_symmetric_relation:
            assert getattr(domain, operation)(relation[1], relation[0]) != relation[2], "Invalid result"

         
def parity_domain_tester():
    test_utils.printYellow("Parity Domain Test")
    try:
        parity_d = ParityDomain()
        # CONTAINS
        test_contains_relations(parity_d, 
                                OPERATIONS.contains , 
                                parity_consts.CONTAINS_RELATIONS)
        test_contains_relations(parity_d, 
                                OPERATIONS.contains , 
                                parity_consts.CONTAINS_INVALID_RELATIONS)
        # MEET
        test_valid_relations(parity_d, 
                             OPERATIONS.meet , 
                             parity_consts.MEET_RELATIONS)
        test_invalid_relations(parity_d, 
                               OPERATIONS.meet, 
                               parity_consts.MEET_INVALID_RELATIONS)
        # JOIN
        test_valid_relations(parity_d, 
                             OPERATIONS.join, 
                             parity_consts.JOIN_VALID_RELATIONS)
        test_invalid_relations(parity_d, 
                               OPERATIONS.join, 
                               parity_consts.JOIN_INVALID_RELATIONS)
    except Exception as e:
        test_utils.printError(f'{e}')
        return
    test_utils.printSuccess("All tests Passed!")
    


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
