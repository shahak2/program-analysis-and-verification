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
    
      
class BOOLENS(StrEnum):
    add = "TRUE"
    sub = "FALSE"

class NUMBER_CONSTS(StrEnum):
    one = "1"
    
# Parity Consts

ODD    = "ODD"
EVEN   = "EVEN"
BOTTOM = "BOTTOM"
TOP    = "TOP"