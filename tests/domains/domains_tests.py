import sys
from enum import StrEnum
import math

SRC_RELATIVE_PATH = "src/"
UTILS_RELATIVE_PATH = "utils/"
DOMAINS_PATH = SRC_RELATIVE_PATH + 'domains/'

sys.path.insert(1, DOMAINS_PATH)
sys.path.insert(1, UTILS_RELATIVE_PATH)

from parity_consts import *
from parity_domain import ParityDomain
from summation_domain import SummationDomain, SummationElement
import utils
from summation_consts import *

def test_contains_relations(domain, operation, relations):
    utils.printMessage(f"Operation {operation} validity test")
    for relation in relations:
        utils.printInfo(f'Testing: {relation[0]:7} <=  {relation[1]:7} =  {relation[2]} ')
        assert getattr(domain, operation)(relation[0], relation[1]) == relation[2], "Invalid result"
        
def test_valid_relations(domain, operation, relations, is_symmetric_relation = True):
    utils.printMessage(f"Operation {operation} validity test")
    for relation in relations:
        utils.printInfo(f'Testing: {relation[0]:7} {operation}  {relation[1]:7} =  {relation[2]} ')
        assert getattr(domain, operation)(relation[0], relation[1]) == relation[2], "Invalid result"
        if is_symmetric_relation:
            assert getattr(domain, operation)(relation[1], relation[0]) == relation[2], "Invalid result"

def test_invalid_relations(domain, operation, relations, is_symmetric_relation = True):
    utils.printMessage(f"Operation {operation} invalidity test")
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
    utils.printMessage("Parity Domain Tests")
    try:
        parity_d = ParityDomain()
        # CONTAINS
        test_contains_relations(parity_d, 
                                OPERATIONS.contains , 
                                CONTAINS_RELATIONS)
        test_contains_relations(parity_d, 
                                OPERATIONS.contains , 
                                CONTAINS_INVALID_RELATIONS)
        # MEET
        test_valid_relations(parity_d, 
                             OPERATIONS.meet , 
                             MEET_RELATIONS)
        test_invalid_relations(parity_d, 
                               OPERATIONS.meet, 
                               MEET_INVALID_RELATIONS)
        # JOIN
        test_valid_relations(parity_d, 
                             OPERATIONS.join, 
                             JOIN_VALID_RELATIONS)
        test_invalid_relations(parity_d, 
                               OPERATIONS.join, 
                               JOIN_INVALID_RELATIONS)
        # VECTOR JOIN
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
        
        # JOIN
        for relation in SUMMATION_JOIN_RELATIONS:
            utils.printInfo(f'Testing: {relation[0]} (join) {relation[1]} = {relation[2]} ')
            res = s_domain.join(relation[0], relation[1])
            assert res == relation[2], \
                f"Invalid Result {res} = {relation[2]}"
                
        # MEET
        for relation in SUMMATION_MEET_RELATIONS:
            utils.printInfo(f'Testing: {relation[0]} (meet) {relation[1]} = {relation[2]} ')
            res = s_domain.meet(relation[0], relation[1])
            assert res == relation[2], \
                f"Invalid Result {res} = {relation[2]}"
        
        # WIDEN
        for relation in SUMMATION_WIDEN_RELATIONS:
            utils.printInfo(f'Testing: {relation[0]} (widen) {relation[1]} = {relation[2]} ')
            res = s_domain.widen(relation[0], relation[1])
            assert res == relation[2], \
                f"Invalid Result {res} = {relation[2]}"
                
        # NARROW
        for relation in SUMMATION_NARROW_RELATIONS:
            utils.printInfo(f'Testing: {relation[0]} (narrow) {relation[1]} = {relation[2]} ')
            res = s_domain.narrow(relation[0], relation[1])
            assert res == relation[2], \
                f"Invalid Result {res} = {relation[2]}"
    except Exception as e:
        utils.printError(f'{e}')
        return
    utils.printSuccess("All tests Passed!")

def combined_domain_tester():
    # TODO: Implement
    utils.printError(
        f'combined_domain_tester not Implemented')

def run_tests():
    parity_domain_tester()
    summation_domain_tester()
    combined_domain_tester()

if __name__ == '__main__':
    utils.printMessage(
        "\n=== Abstract Domains Tester ===")
    run_tests()
