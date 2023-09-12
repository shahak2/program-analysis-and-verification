import sys

SRC_RELATIVE_PATH = "src/"
PARITY_DOMAIN_PATH = SRC_RELATIVE_PATH + 'domains/'
TESTS_RELATIVE_PATH = "tests/"

TOP = "TOP"
BOTTOM = "BOTTOM"
ODD = "ODD"
EVEN = "EVEN"

MEET_RELATIONS = [
    (BOTTOM,  TOP,       BOTTOM), 
    (BOTTOM,  EVEN,      BOTTOM), 
    (BOTTOM,  ODD,       BOTTOM),
    (BOTTOM,  BOTTOM,    BOTTOM), 
    (TOP,     EVEN,      EVEN  ), 
    (TOP,     ODD,       ODD   ), 
    (TOP,     TOP,       TOP   ),
    (ODD,     EVEN,      BOTTOM),
    (ODD,     ODD,       ODD   ),
    (EVEN,    EVEN,      EVEN  )
]

MEET_INVALID_RELATIONS = [
    (BOTTOM,  TOP,       EVEN), 
    (ODD,     EVEN,      EVEN), 
    (TOP,     EVEN,      TOP ),
    (TOP,     BOTTOM,    TOP )
]
       
sys.path.insert(1, PARITY_DOMAIN_PATH)
sys.path.insert(1, TESTS_RELATIVE_PATH)

from parity_domain import ParityDomain
import test_utils



def parity_domain_tester():
    
    def parity_contains_tester(parity_d):
        test_utils.printYellow("Contains operation Test")
        assert parity_d.parity_contains(TOP, BOTTOM) == False, "{TOP} <= {BOTTOM} "
        assert parity_d.parity_contains(BOTTOM, TOP) == True, "{TOP} <= {BOTTOM}"
        assert parity_d.parity_contains(EVEN, ODD) == False, "{EVEN} <= {ODD}"
        assert parity_d.parity_contains(BOTTOM, EVEN) == True, "{BOTTOM} <= {EVEN}"
        assert parity_d.parity_contains(TOP, EVEN) == False, "{TOP} <= {EVEN}"
        test_utils.printSuccess("Success!")
    
    def parity_meets_tester(parity_d):
        test_utils.printYellow("Meet operation Test")
        
        for relation in MEET_RELATIONS:
            test_utils.printInfo(f'Testing: {relation[0]:7} (MEET)  {relation[1]:7} =  {relation[2]} ')
            assert parity_d.meet(relation[0], relation[1]) == relation[2], "Error"
            assert parity_d.meet(relation[1], relation[0]) == relation[2], "Error"
                
        for relation in MEET_INVALID_RELATIONS:
            test_utils.printInfo(f'Testing: {relation[0]:7} (MEET)  {relation[1]:7} !=  {relation[2]} ')
            assert parity_d.meet(relation[0], relation[1]) != relation[2], "Error"
            assert parity_d.meet(relation[1], relation[0]) != relation[2], "Error"        
        
            
        test_utils.printSuccess("Success!")
    
    
    test_utils.printYellow("Parity Domain Test")
    try:
        
        parity_d = ParityDomain()
        parity_contains_tester(parity_d)
        parity_meets_tester(parity_d)
       

    except Exception as e:
        test_utils.printError(f'{e}')
        return

    test_utils.printSuccess("All tests Passed!")
    


def summation_domain_tester():
    # TODO: Implement
    test_utils.printInfo(f'summation_domain_tester not Implemented')

def combined_domain_tester():
    # TODO: Implement
    test_utils.printInfo(f'combined_domain_tester not Implemented')

def run_tests():
    parity_domain_tester()
    summation_domain_tester()
    combined_domain_tester()

if __name__ == '__main__':
    test_utils.printYellow("\n=== Abstract Domains Tester ===")
    run_tests()
