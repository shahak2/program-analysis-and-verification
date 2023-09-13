from enum import StrEnum

class STATEMENTS(StrEnum):
    skip = "skip"
    assignment = ":="
    assume = "assume"
    assertion = "assert"
    entry = "entry"

class BaseTransformer():
    def parse_statement(self, statement):
        tokens = statement.split()

        if tokens[0] == STATEMENTS.skip or \
            tokens[0] == STATEMENTS.entry:
            self.parse_skip()
        elif tokens[1] == STATEMENTS.assignment:
            self.parse_assignment(tokens)
        elif tokens[0] == STATEMENTS.assignment:
            self.parse_assume(tokens)
        elif tokens[0] == STATEMENTS.assertion:
            self.parse_assert(tokens)
        else:
            raise SyntaxError(f"Invalid command: {statement}")
        
    def parse_skip(self):
        print("Executing 'skip' command")

    def parse_assignment(self, tokens):
        variable = tokens[0]
        operator = tokens[2]
        value = tokens[3]

        if operator == ':=':
            if value == '?':
                self.parse_assignment_unknown(variable)
            elif value.isdigit() or (value[0] == '-' and value[1:].isdigit()):
                self.parse_assignment_constant(variable, int(value))
            elif value.isdigit() and value[0] == 'j':
                self.parse_assignment_j(variable, int(value[1:]))
            else:
                raise SyntaxError(f"Invalid assignment: {variable} := {value}")
        else:
            raise SyntaxError(f"Invalid assignment operator: {operator}")

    
    def parse_assignment_unknown(self, variable):
        print(f"Assigning '{variable}' to unknown value")

    def parse_assignment_constant(self, variable, value):
        print(f"Assigning '{variable}' to constant {value}")

    def parse_assignment_j(self, variable, j_value):
        print(f"Assigning '{variable}' to j + {j_value}")

    def parse_assume(self, tokens):
        expression = " ".join(tokens[1:])
        print(f"Assuming: {expression}")

    def parse_assert(self, tokens):
        expression = " ".join(tokens[1:])
        print(f"Asserting: {expression}")
       


 
TEST_STATEMENTS = [
    "entry",
    "skip",
    # "n := ?",
    # "i := j + 1",
]

bt = BaseTransformer()
for test in TEST_STATEMENTS:
    bt.parse_statement(test)