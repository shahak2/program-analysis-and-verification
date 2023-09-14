import sys
from enum import StrEnum

SRC_RELATIVE_PATH = "src/"
PARITY_DOMAIN_PATH = SRC_RELATIVE_PATH + 'domains/'
UTILS_RELATIVE_PATH = "utils/"

sys.path.insert(1, PARITY_DOMAIN_PATH)
sys.path.insert(1, UTILS_RELATIVE_PATH)

import parity_consts
from parity_domain import ParityDomain
import utils

class OPERATIONS(StrEnum):
    meet = "meet"
    join = "join"
    contains = "contains"
    
def test_contains_relations(domain, operation, relations):
    utils.printYellow(f"Operation {operation} Valid Test")
    for relation in relations:
        utils.printInfo(f'Testing: {relation[0]:7} <=  {relation[1]:7} =  {relation[2]} ')
        assert getattr(domain, operation)(relation[0], relation[1]) == relation[2], "Invalid result"
        
def test_valid_relations(domain, operation, relations, is_symmetric_relation = True):
    utils.printYellow(f"Operation {operation} Valid Test")
    for relation in relations:
        utils.printInfo(f'Testing: {relation[0]:7} {operation}  {relation[1]:7} =  {relation[2]} ')
        assert getattr(domain, operation)(relation[0], relation[1]) == relation[2], "Invalid result"
        if is_symmetric_relation:
            assert getattr(domain, operation)(relation[1], relation[0]) == relation[2], "Invalid result"

def test_invalid_relations(domain, operation, relations, is_symmetric_relation = True):
    utils.printYellow(f"Operation {operation} Invalid Test")
    for relation in relations:
        utils.printInfo(f'Testing: {relation[0]:7} {operation}  {relation[1]:7} =  {relation[2]} ')
        assert getattr(domain, operation)(relation[0], relation[1]) != relation[2], "Invalid result"
        if is_symmetric_relation:
            assert getattr(domain, operation)(relation[1], relation[0]) != relation[2], "Invalid result"

def test_vector_join(domain, 
                     test_vectors):
    
    for test_vector in test_vectors:
        assert domain.vector_join(
            test_vector[0], 
            test_vector[1]) == test_vector[2], \
                f"Expected {test_vector[0]} (JOIN) {test_vector[1]} == {test_vector[2]}!"
        
def parity_domain_tester():
    utils.printYellow("Parity Domain Test")
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
        
        # VECTOR JOIN
        test_vector_join(parity_d,
                         parity_consts.VECTOR_JOIN_TESTS)
    except Exception as e:
        utils.printError(f'{e}')
        return
    utils.printSuccess("All tests Passed!")
    


def summation_domain_tester():
    # TODO: Implement
    utils.printError(f'summation_domain_tester not Implemented')

def combined_domain_tester():
    # TODO: Implement
    utils.printError(f'combined_domain_tester not Implemented')

def run_tests():
    parity_domain_tester()
    summation_domain_tester()
    combined_domain_tester()

if __name__ == '__main__':
    utils.printYellow("\n=== Abstract Domains Tester ===")
    run_tests()
