import sys
import math

SRC_RELATIVE_PATH = "src/"
DOMAINS_PATH = SRC_RELATIVE_PATH + 'domains/'

sys.path.insert(1, DOMAINS_PATH)

from summation_domain import SummationDomain, SummationElement

TOP = SummationElement(-math.inf, math.inf)
BOTTOM = "BOTTOM"

# (element1, element2, expected_result)
SUMMATION_JOIN_RELATIONS = [
    (SummationElement(1, 2),            SummationElement(1, 2),  SummationElement(1, 2)), 
    (SummationElement(3, 4),            SummationElement(1, 2),  SummationElement(1, 4)), 
    (SummationElement(-math.inf, 3),    SummationElement(1, 17), SummationElement(-math.inf, 17))
]

SUMMATION_MEET_RELATIONS = [
    (SummationElement(1, 2),            SummationElement(1, 2), SummationElement(1, 2)), 
    
]

SUMMATION_WIDEN_RELATIONS = [
    (SummationElement(1, 2),            SummationElement(1, 2), SummationElement(1, 2)), 
    
]

SUMMATION_NARROW_RELATIONS = [
    (SummationElement(1, 2),            SummationElement(1, 2), SummationElement(1, 2)), 
    
]


# # [(vector1, vector2, expected_results_vector), ...]
# VECTOR_JOIN_TESTS = [
#     ([TOP, TOP, TOP],       [TOP, TOP, TOP],        [TOP, TOP, TOP] ),
#     ([TOP, TOP, TOP],       [BOTTOM, EVEN, ODD],    [TOP, TOP, TOP] ),
#     ([EVEN, ODD, BOTTOM],   [BOTTOM, EVEN, ODD],    [EVEN, TOP, ODD])
# ]





