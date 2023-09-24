import sys
from enum import StrEnum
import math

SRC_RELATIVE_PATH = "src/"
UTILS_RELATIVE_PATH = "utils/"
DOMAINS_PATH = SRC_RELATIVE_PATH + 'domains/'

sys.path.insert(1, DOMAINS_PATH)
sys.path.insert(1, UTILS_RELATIVE_PATH)

import utils
from parity_consts import *
from summation_consts import *
from parity_domain import ParityDomain
from combined_domain import CombinedDomain
from summation_domain import SummationDomain


def test_contains_relations(domain, operation, relations):
    utils.printMessage(f"Operation {operation} validity test")
    for relation in relations:
        utils.printInfo(f'Testing: {relation[0]} <= {relation[1]} = {relation[2]} ')
        assert getattr(domain, operation)(relation[0], relation[1]) == relation[2], "Invalid result"
        
def test_valid_relations(domain, operation, relations, is_symmetric_relation = True):
    utils.printMessage(f"Operation {operation} validity test")
    for relation in relations:
        utils.printInfo(f'Testing: {relation[0]} {operation} {relation[1]} = {relation[2]} ')
        assert getattr(domain, operation)(relation[0], relation[1]) == relation[2], "Invalid result"
        if is_symmetric_relation:
            assert getattr(domain, operation)(relation[1], relation[0]) == relation[2], "Invalid result"

def test_invalid_relations(domain, operation, relations, is_symmetric_relation = True):
    utils.printMessage(f"Operation {operation} invalidity test")
    for relation in relations:
        utils.printInfo(f'Testing: {relation[0]} {operation} {relation[1]} = {relation[2]} ')
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
    utils.printMessage("Parity Domain Tests")
    try:
        parity_d = ParityDomain()

        test_contains_relations(parity_d, 
                                OPERATIONS.contains, 
                                CONTAINS_RELATIONS)
        # invalid relations
        test_contains_relations(parity_d, 
                                OPERATIONS.contains, 
                                CONTAINS_INVALID_RELATIONS)

        test_valid_relations(parity_d, 
                             OPERATIONS.meet, 
                             MEET_RELATIONS)
        test_invalid_relations(parity_d, 
                               OPERATIONS.meet, 
                               MEET_INVALID_RELATIONS)

        test_valid_relations(parity_d, 
                             OPERATIONS.join, 
                             JOIN_VALID_RELATIONS)
        test_invalid_relations(parity_d, 
                               OPERATIONS.join, 
                               JOIN_INVALID_RELATIONS)

        test_vector_join(parity_d,
                         VECTOR_JOIN_TESTS)
    except Exception as e:
        utils.printError(f'{e}')
        return
    utils.printSuccess("All tests Passed!")
    
def summation_domain_tester():
    utils.printMessage("Summation Domain Tests")
    try:
        s_domain = SummationDomain()

        test_valid_relations(s_domain, 
                             OPERATIONS.join, 
                             SUMMATION_JOIN_RELATIONS)
        
        test_valid_relations(s_domain, 
                             OPERATIONS.meet, 
                             SUMMATION_MEET_RELATIONS)

        test_valid_relations(s_domain, 
                             OPERATIONS.widen, 
                             SUMMATION_WIDEN_RELATIONS,
                             is_symmetric_relation = False)
        
        test_valid_relations(s_domain, 
                             OPERATIONS.narrow, 
                             SUMMATION_NARROW_RELATIONS,
                             is_symmetric_relation = False)
        
    except Exception as e:
        utils.printError(f'{e}')
        return
    utils.printSuccess("All tests Passed!")

def combined_domain_tester():
    utils.printMessage("Summation Domain Tests")
    try:
        c_domain = CombinedDomain()
        
        # JOIN
        for relation in SUMMATION_JOIN_RELATIONS:
            utils.printInfo(f'Testing: {relation[0]} (join) {relation[1]} = {relation[2]} ')
            res = c_domain.join(relation[0], relation[1])
            assert res == relation[2], \
                f"Invalid Result {res} = {relation[2]}"
                
        # # MEET
        # for relation in SUMMATION_MEET_RELATIONS:
        #     utils.printInfo(f'Testing: {relation[0]} (meet) {relation[1]} = {relation[2]} ')
        #     res = c_domain.meet(relation[0], relation[1])
        #     assert res == relation[2], \
        #         f"Invalid Result {res} = {relation[2]}"
        
        # # WIDEN
        # for relation in SUMMATION_WIDEN_RELATIONS:
        #     utils.printInfo(f'Testing: {relation[0]} (widen) {relation[1]} = {relation[2]} ')
        #     res = c_domain.widen(relation[0], relation[1])
        #     assert res == relation[2], \
        #         f"Invalid Result {res} = {relation[2]}"
                
        # # NARROW
        # for relation in SUMMATION_NARROW_RELATIONS:
        #     utils.printInfo(f'Testing: {relation[0]} (narrow) {relation[1]} = {relation[2]} ')
        #     res = c_domain.narrow(relation[0], relation[1])
        #     assert res == relation[2], \
        #         f"Invalid Result {res} = {relation[2]}"
    except Exception as e:
        utils.printError(f'{e}')
        return
    utils.printSuccess("All tests Passed!")

def run_tests():
    parity_domain_tester()
    summation_domain_tester()
    # combined_domain_tester()

if __name__ == '__main__':
    utils.printMessage(
        "\n=== Abstract Domains Tester ===")
    run_tests()
