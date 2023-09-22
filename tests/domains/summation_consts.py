import sys
import math

SRC_RELATIVE_PATH = "src/"
DOMAINS_PATH = SRC_RELATIVE_PATH + 'domains/'

sys.path.insert(1, DOMAINS_PATH)

from summation_domain import SummationDomain, SummationElement

TOP = SummationElement(-math.inf, math.inf)
BOTTOM = "BOTTOM"
TOP = "TOP"

# (element1, element2, expected_result)
SUMMATION_JOIN_RELATIONS = [
    (SummationElement(1, 2),                SummationElement(1, 2),     SummationElement(1, 2)         ), 
    (SummationElement(3, 4),                SummationElement(1, 2),     SummationElement(1, 4)         ), 
    (SummationElement(-math.inf, 3),        SummationElement(1, 17),    SummationElement(-math.inf, 17))
]

SUMMATION_MEET_RELATIONS = [
    (SummationElement(1, 2),                SummationElement(1, 2),     SummationElement(1, 2)), 
    (SummationElement(-math.inf, math.inf), SummationElement(1, 2),     SummationElement(1, 2)),
    (SummationElement(-math.inf, 1),        SummationElement(1, 2),     SummationElement(1, 1)),
    (SummationElement(1, 1),                SummationElement(2, 2),     BOTTOM                )
]

SUMMATION_WIDEN_RELATIONS = [
    (BOTTOM,                                BOTTOM,                     BOTTOM                                 ), 
    (BOTTOM,                                SummationElement(1, 2),     (SummationElement(1, 2))               ), 
    (SummationElement(1, 2),                SummationElement(1, 2),     (SummationElement(1, 2))               ),
    (SummationElement(1, 2),                SummationElement(2, 3),     (SummationElement(1, 2))               ),
    (SummationElement(1, 2),                SummationElement(0, 3),     (SummationElement(-math.inf, 2))       ),
    (SummationElement(1, 3),                SummationElement(2, 2),     (SummationElement(1, math.inf))        ),
    (SummationElement(1, 3),                SummationElement(0, 2),     (SummationElement(-math.inf, math.inf)))
]

SUMMATION_NARROW_RELATIONS = [
    (SummationElement(1, 2),                BOTTOM,                     SummationElement(1, 2)                 ), 
    (SummationElement(-math.inf, 2),        SummationElement(-3, 4),    SummationElement(-3, 2)                ), 
    (SummationElement(1, math.inf),         SummationElement(-3, 4),    SummationElement(1, 4)                 ), 
    (SummationElement(-math.inf, math.inf), SummationElement(-3, 4),    SummationElement(-3, 4)                )
]







