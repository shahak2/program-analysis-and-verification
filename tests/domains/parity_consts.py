from enum import StrEnum

class OPERATIONS(StrEnum):
    meet = "meet"
    join = "join"
    contains = "contains"


TOP = "TOP"
BOTTOM = "BOTTOM"
ODD = "ODD"
EVEN = "EVEN"

CONTAINS_RELATIONS = [
    (BOTTOM,    TOP,    True),
    (BOTTOM,    EVEN,   True),
    (ODD,       TOP,    True),
    (EVEN,      TOP,    True)
]

CONTAINS_INVALID_RELATIONS = [
    (TOP,       BOTTOM, False),
    (EVEN,      ODD,    False),
    (EVEN,      BOTTOM, False),
    (TOP,       EVEN,   False)
]

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

JOIN_VALID_RELATIONS = [
    (TOP,     EVEN,      TOP    ), 
    (TOP,     ODD,       TOP    ), 
    (TOP,     TOP,       TOP    ),
    (TOP,     BOTTOM,    TOP    ), 
    (BOTTOM,  EVEN,      EVEN   ), 
    (BOTTOM,  ODD,       ODD    ),
    (BOTTOM,  BOTTOM,    BOTTOM ), 
    (ODD,     EVEN,      TOP    ),
    (ODD,     ODD,       ODD    ),
    (EVEN,    EVEN,      EVEN   )
]

JOIN_INVALID_RELATIONS = [
    (TOP,     EVEN,      EVEN   ), 
    (TOP,     ODD,       ODD    ), 
    (TOP,     BOTTOM,    BOTTOM )
]

# [(vector1, vector2, expected_results_vector), ...]
VECTOR_JOIN_TESTS = [
    ([TOP, TOP, TOP],       [TOP, TOP, TOP],        [TOP, TOP, TOP] ),
    ([TOP, TOP, TOP],       [BOTTOM, EVEN, ODD],    [TOP, TOP, TOP] ),
    ([EVEN, ODD, BOTTOM],   [BOTTOM, EVEN, ODD],    [EVEN, TOP, ODD])
]





