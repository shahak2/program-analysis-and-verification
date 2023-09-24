import sys
import math
from enum import StrEnum

SRC_RELATIVE_PATH = "src/"
DOMAINS_PATH = SRC_RELATIVE_PATH + 'domains/'

sys.path.insert(1, DOMAINS_PATH)

from summation_element import SummationElement
from combined_element import CombinedElement

class PARITY_DOMAIN(StrEnum):
    top = "TOP"
    bottom = "BOTTOM"
    odd = "ODD"
    even = "EVEN"

SUMMATION_TOP = SummationElement(-math.inf, math.inf)
SUMMATION_BOTTOM = "BOTTOM"

# (
    # CombinedElement1, 
    # CombinedElement2, 
    # expected_combined_element_result
# )

COMBINED_JOIN_RELATIONS = [
    (
        CombinedElement(PARITY_DOMAIN.top,      SummationElement(1, 2)),                
        CombinedElement(PARITY_DOMAIN.top,      SummationElement(1, 2)),    
        CombinedElement(PARITY_DOMAIN.top,      SummationElement(1, 2))
    ),
    (
        CombinedElement(PARITY_DOMAIN.odd,      SummationElement(1, 13)),                
        CombinedElement(PARITY_DOMAIN.even,     SummationElement(-1, 2)),    
        CombinedElement(PARITY_DOMAIN.top,      SummationElement(-1, 13))
    ),
    (
        CombinedElement(PARITY_DOMAIN.odd,      SUMMATION_TOP),                
        CombinedElement(PARITY_DOMAIN.bottom,   SummationElement(-1, 2)),    
        CombinedElement(PARITY_DOMAIN.odd,      SUMMATION_TOP)
    ),
    (
        CombinedElement(PARITY_DOMAIN.even,      SUMMATION_BOTTOM),                
        CombinedElement(PARITY_DOMAIN.bottom,    SummationElement(-1, 2)),    
        CombinedElement(PARITY_DOMAIN.even,      SummationElement(-1, 2))
    )
]

COMBINED_MEET_RELATIONS = [

]

COMBINED_WIDEN_RELATIONS = [

]

COMBINED_NARROW_RELATIONS = [

]







