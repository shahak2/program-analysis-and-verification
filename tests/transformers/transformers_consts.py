import sys
from enum import StrEnum

import math

SRC_RELATIVE_PATH = "src/"
DOMAINS_PATH = SRC_RELATIVE_PATH + 'domains/'

sys.path.insert(1, DOMAINS_PATH)

from summation_element import SummationElement

#################### Parity Testing ####################

# Parity consts
TOP = "TOP"
BOTTOM = "BOTTOM"
ODD = "ODD"
EVEN = "EVEN"
CANNOT_VALIDATE = "Cannot validate"

"""
    PARITY_TESTS: A tuple of (values_vector, statement, expected_result_vector)
"""

PARITY_MOCK_VARIABLES = {"i": 0, "n": 1, "j": 2}

PARITY_TESTS = [
    # Assignments
    ([TOP, BOTTOM, ODD], "entry",       [TOP,      BOTTOM, ODD     ]),
    ([TOP, BOTTOM, ODD], "skip",        [TOP,      BOTTOM, ODD     ]),
    ([TOP, BOTTOM, ODD], "j := ?",      [TOP,      BOTTOM, BOTTOM  ]),
    ([TOP, BOTTOM, ODD], "j := 378",    [TOP,      BOTTOM, EVEN    ]),
    ([TOP, BOTTOM, ODD], "i := n",      [BOTTOM,   BOTTOM, ODD     ]),
    ([TOP, BOTTOM, ODD], "i := n + 1",  [BOTTOM,   BOTTOM, ODD     ]),
    ([TOP, EVEN,   ODD], "i := n - 1",  [ODD,      EVEN,   ODD     ]),
    ([TOP, EVEN,   TOP], "i := j - 1",  [TOP,      EVEN,   TOP     ]),
    
    # Assumptions
    ([TOP,  EVEN,   TOP],   "assume",          [TOP,    EVEN,   TOP   ]),
    ([EVEN, EVEN,   TOP],   "assume(i = n)",   [EVEN,   EVEN,   TOP   ]), # good: vars are equal
    ([TOP,  EVEN,   TOP],   "assume(i = n)",   [BOTTOM, BOTTOM, BOTTOM]), # bad: vars are not equal
    ([EVEN, EVEN,   ODD],   "assume(i != j)",  [EVEN,   EVEN,   ODD   ]), # good: vars are not equal
    ([EVEN, EVEN,   EVEN],  "assume(i != j)",  [BOTTOM, BOTTOM, BOTTOM]), # bad: vars are equal
    ([TOP,  EVEN,   TOP],   "assume(TRUE)",    [TOP,    EVEN,   TOP   ]),
    ([TOP,  EVEN,   TOP],   "assume(FALSE)",   [BOTTOM, BOTTOM, BOTTOM]),
    
    # Assertions
    ([BOTTOM, EVEN,  TOP],  "assert (ODD i ODD j) (EVEN i EVEN j)", CANNOT_VALIDATE),
    ([ODD,    EVEN,  TOP],  "assert (ODD i)",                       True),
    ([EVEN,   EVEN,  TOP],  "assert (ODD i)",                       False),
    ([BOTTOM, EVEN,  TOP],  "assert (ODD i)",                       CANNOT_VALIDATE),
    ([BOTTOM, TOP,   TOP],  "assert (EVEN i) (EVEN j)",             CANNOT_VALIDATE),
    ([EVEN,   TOP,   TOP],  "assert (EVEN i) (EVEN j)",             True),
    ([TOP,    EVEN,  EVEN], "assert (EVEN i) (EVEN j)",             True)
]

PARITY_MOCK_VARIABLES_LONG = {
    "a": 0, 
    "b": 1, 
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5
}

PARITY_TESTS_LONG = [
    ([TOP, BOTTOM, ODD, TOP, BOTTOM, ODD], "entry",      [TOP,      BOTTOM, ODD, TOP, BOTTOM, ODD]),
    ([TOP, BOTTOM, ODD, TOP, BOTTOM, ODD], "a := b",     [BOTTOM,   BOTTOM, ODD, TOP, BOTTOM, ODD]),
    ([TOP, BOTTOM, ODD, TOP, BOTTOM, ODD], "e := f",     [TOP,      BOTTOM, ODD, TOP, ODD,    ODD]),
    ([TOP, BOTTOM, ODD, TOP, BOTTOM, ODD], "e := f + 1", [TOP,      BOTTOM, ODD, TOP, EVEN,   ODD]),
    ([TOP, BOTTOM, ODD, TOP, BOTTOM, ODD], "e := f - 1", [TOP,      BOTTOM, ODD, TOP, EVEN,   ODD]),
]


#################### Summation Testing ####################

SUMMATION_MOCK_VARIABLES = {"a": 0,  "b": 1,  "c": 2}

SUMMATION_TOP = SummationElement(-math.inf, math.inf)

SUMMATION_TESTS = [
    # Assignments
    ([SUMMATION_TOP, BOTTOM, BOTTOM],               "entry",       [SUMMATION_TOP,              BOTTOM,                     BOTTOM]                     ),
    ([SUMMATION_TOP, BOTTOM, BOTTOM],               "skip",        [SUMMATION_TOP,              BOTTOM,                     BOTTOM]                     ),
    ([SUMMATION_TOP, BOTTOM, BOTTOM],               "c := ?",      [SUMMATION_TOP,              BOTTOM,                     BOTTOM]                     ),
    ([SUMMATION_TOP, BOTTOM, BOTTOM],               "c := 378",    [SUMMATION_TOP,              BOTTOM,                     SummationElement(378, 378)] ),
    ([BOTTOM, SUMMATION_TOP, BOTTOM],               "a := b",      [SUMMATION_TOP,              SUMMATION_TOP,              BOTTOM]                     ),
    ([BOTTOM, SUMMATION_TOP, BOTTOM],               "a := b + 1",  [SUMMATION_TOP,              SUMMATION_TOP,              BOTTOM]                     ),
    ([BOTTOM, SummationElement(-3, 5), BOTTOM],     "a := b + 1",  [SummationElement(-2, 6),    SummationElement(-3, 5),    BOTTOM]                     ),
    ([BOTTOM, SummationElement(-3, 5), BOTTOM],     "a := b - 1",  [SummationElement(-4, 4),    SummationElement(-3, 5),    BOTTOM]                     ),
    ([BOTTOM, SUMMATION_TOP, BOTTOM],               "a := b - 1",  [SUMMATION_TOP,              SUMMATION_TOP,              BOTTOM]                     ),
    ([BOTTOM, BOTTOM,   SUMMATION_TOP],             "a := c - 1",  [SUMMATION_TOP,              BOTTOM,                     SUMMATION_TOP]              ),
    
    # # Assumptions
    ([SUMMATION_TOP,            BOTTOM,                      BOTTOM],                    "assume",          [SUMMATION_TOP,             BOTTOM,                     BOTTOM]                 ),
    ([SUMMATION_TOP,            SUMMATION_TOP,               BOTTOM],                    "assume(a = 3)",   [SummationElement(3, 3),    SUMMATION_TOP,              BOTTOM]                 ),
    ([SummationElement(3, 3),   SUMMATION_TOP,               BOTTOM],                    "assume(a != 3)",  [BOTTOM,                    SUMMATION_TOP,              BOTTOM]                 ),
    ([SummationElement(1, 4),   SUMMATION_TOP,               BOTTOM],                    "assume(a != 3)",  [SummationElement(1, 4),    SUMMATION_TOP,              BOTTOM]                 ),
    ([SummationElement(1, 4),   SUMMATION_TOP,               BOTTOM],                    "assume(a = 3)",   [SummationElement(3, 3),    SUMMATION_TOP,              BOTTOM]                 ),
    ([SummationElement(1, 10),  SUMMATION_TOP,               BOTTOM],                    "assume(a != 5)",  [SummationElement(1, 10),   SUMMATION_TOP,              BOTTOM]                 ),
    ([SummationElement(1, 10),  SummationElement(3, 13),     BOTTOM],                    "assume(a = b)",   [SummationElement(3, 10),   SummationElement(3, 10),    BOTTOM]                 ),
    ([SummationElement(1, 3),   SummationElement(6, 9),      SUMMATION_TOP],             "assume(a = b)",   [BOTTOM,                    BOTTOM,                     SUMMATION_TOP]          ),
    ([SummationElement(1, 3),   BOTTOM,                      SUMMATION_TOP],             "assume(a = b)",   [BOTTOM,                    BOTTOM,                     BOTTOM]                 ),
    ([BOTTOM,                   SummationElement(6, 9),      SUMMATION_TOP],             "assume(a = b)",   [BOTTOM,                    BOTTOM,                     BOTTOM]                 ),
    ([SUMMATION_TOP,            SUMMATION_TOP,               BOTTOM],                    "assume(a = b)",   [SUMMATION_TOP,             SUMMATION_TOP,              BOTTOM]                 ), # good: vars are equal
    ([SUMMATION_TOP,            BOTTOM,                      SummationElement(-3, 5)],   "assume(a = b)",   [BOTTOM,                    BOTTOM,                     BOTTOM]                 ), # bad: vars are not equal
    ([SummationElement(-3, 5),  SUMMATION_TOP,               SummationElement(-2, 5)],   "assume(a != c)",  [SummationElement(-3, -3),   SUMMATION_TOP,              SummationElement(-2, 5)]), # good: vars are not equal
    ([SummationElement(-4, -3),  SUMMATION_TOP,               SummationElement(-2, 5)],   "assume(a != c)",  [SummationElement(-4, -3),   SUMMATION_TOP,              SummationElement(-2, 5)]), # good: vars are not equal
    ([SummationElement(-3, 5),  SUMMATION_TOP,               SummationElement(-3, 5)],   "assume(a != c)",  [BOTTOM,                    BOTTOM,                     BOTTOM]                 ), # bad: vars are equal
    ([SummationElement(-3, 5),  SUMMATION_TOP,               SummationElement(-3, 5)],   "assume(TRUE)",    [SummationElement(-3, 5),   SUMMATION_TOP,              SummationElement(-3, 5)]),
    ([SummationElement(-3, 5),  SUMMATION_TOP,               SummationElement(-3, 5)],   "assume(FALSE)",   [BOTTOM,                    BOTTOM,                     BOTTOM]                 ),
    
    # Assertions
    ([BOTTOM,                                BOTTOM,                                 BOTTOM                 ], "assert (SUM a b = SUM b c)",    CANNOT_VALIDATE ),
    ([SummationElement(-3, 5),               SummationElement(-3, 5),                SummationElement(-3, 5)], "assert (SUM a b = SUM b c)",    True            ),
    ([SummationElement(-2, 5),               SummationElement(-3, 5),                SummationElement(-3, 5)], "assert (SUM a b = SUM b c)",    False           ),
    ([SummationElement(-2, 5),               SummationElement(-2, 5),                SummationElement(-3, 5)], "assert (SUM a = SUM b)",        True            ),
    ([SummationElement(-2, 1),               SummationElement(-4, 2),                SummationElement(-3, 5)], "assert (SUM a a = SUM b)",      True            ),
    ([SummationElement(-math.inf, 1),        SummationElement(-math.inf, 1),         SummationElement(-3, 5)], "assert (SUM a = SUM b)",        True            ),
    ([SummationElement(-math.inf, math.inf), SummationElement(-math.inf, 1),         SummationElement(-3, 5)], "assert (SUM a = SUM b)",        False           ),
    ([SummationElement(-math.inf, math.inf), SummationElement(-math.inf, math.inf),  SummationElement(-3, 5)], "assert (SUM a = SUM b)",        True            ),
    ([SummationElement(-math.inf, 1),        SummationElement(-math.inf, 1),         BOTTOM                 ], "assert (SUM a = SUM b)",        True            ),
    ([SummationElement(-math.inf, 1),        BOTTOM,                                 BOTTOM                 ], "assert (SUM a = SUM b)",        CANNOT_VALIDATE ),
    ([BOTTOM,                                SummationElement(-math.inf, 1),         BOTTOM                 ], "assert (SUM a = SUM b)",        CANNOT_VALIDATE )
]