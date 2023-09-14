from enum import StrEnum


### Parity Testing

# Parity consts
TOP = "TOP"
BOTTOM = "BOTTOM"
ODD = "ODD"
EVEN = "EVEN"

"""
    PARITY_TESTS: A tuple of (values_vector, statement, expected_result_vector)
"""

PARITY_MOCK_VARIABLES = {
    "i": 0, 
    "n": 1, 
    "j": 2
}

PARITY_TESTS = [
    ([TOP, BOTTOM, ODD], "entry",       [TOP,      BOTTOM, ODD     ]),
    ([TOP, BOTTOM, ODD], "skip",        [TOP,      BOTTOM, ODD     ]),
    ([TOP, BOTTOM, ODD], "j := ?",      [TOP,      BOTTOM, BOTTOM  ]),
    ([TOP, BOTTOM, ODD], "j := 378",    [TOP,      BOTTOM, EVEN    ]),
    ([TOP, BOTTOM, ODD], "i := n",      [BOTTOM,   BOTTOM, ODD     ]),
    ([TOP, BOTTOM, ODD], "i := n + 1",  [BOTTOM,   BOTTOM, ODD     ]),
    ([TOP, EVEN,   ODD], "i := n - 1",  [ODD,      EVEN,   ODD     ]),
    ([TOP, EVEN,   TOP], "i := j - 1",  [TOP,      EVEN,   TOP     ]),
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







