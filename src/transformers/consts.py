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

class BOOLENS(StrEnum):
    add = "TRUE"
    sub = "FALSE"

class BOOLENS(StrEnum):
    add = "TRUE"
    sub = "FALSE"