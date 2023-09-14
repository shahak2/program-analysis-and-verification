from enum import StrEnum

class STATEMENTS(StrEnum):
    skip = "skip"
    assignment = ":="
    assume = "assume"
    assertion = "assert"
    entry = "entry"

class OPERATIONS(StrEnum):
    add = "+"
    sub = "-"

class ASSIGNMENTS_CONSTS(StrEnum):
    wildcard = "?"
    
      
class BOOLEANS(StrEnum):
    true = "TRUE"
    false = "FALSE"

class NUMBER_CONSTS(StrEnum):
    one = "1"
    
class CONDITION_CONSTS(StrEnum):
    left_bracket = "("
    right_bracket = ")"
    equal = "="
    not_equal = "!="
    
# Parity Consts

ODD    = "ODD"
EVEN   = "EVEN"
BOTTOM = "BOTTOM"
TOP    = "TOP"

class PARITY_CONDITION_CONSTS(StrEnum):
    even = "EVEN"
    ODD = "ODD"
