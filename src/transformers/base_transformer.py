from consts import *


class BaseTransformer():
    def __init__(self,
                 variable_to_index_mapping,
                 values_vector):
        self.variable_to_index_mapping = variable_to_index_mapping
        self.values_vector = values_vector
    
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
            raise SyntaxError(
                f"Invalid command: {statement}")
        
    def parse_skip(self):
        raise NotImplementedError(
            f"parse_skip function not implemented")

    def parse_assignment(self, tokens):
        assign_to_variable = tokens[0]
        expression = tokens[1:]
        if len(tokens) > 3:
            self.parse_assignment_from_expression(assign_to_variable,
                                                  expression)
        
        else:
            self.parse_assignment_from_expression(assign_to_variable,
                                                  expression)
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

    
    def parse_simple_assignment(self, 
                                assign_to_variable, 
                                expression):
        pass
    
    def parse_assignment_from_expression(self, 
                                         assign_to_variable, 
                                         expression):
        raise NotImplementedError(
            f"parse_assignment_from_expression function not implemented")
    
    def parse_assignment_unknown(self, 
                                 assign_to_variable):
        raise NotImplementedError(
            f"parse_assignment_unknown function not implemented")

    def parse_assignment_constant(self, 
                                  assign_to_variable, 
                                  value):
        raise NotImplementedError(
            f"parse_assignment_constant function not implemented")

    def parse_assignment_from_variable(self, 
                                       assign_to_variable, 
                                       j_value):
        raise NotImplementedError(
            f"parse_assignment_from_variable function not implemented")

    def parse_assume(self, tokens):
        expression = " ".join(tokens[1:])
        expression = " ".join(tokens[1:])
        raise NotImplementedError(
            f"parse_assume function not implemented")

    
    def parse_assert(self, tokens):
        expression = " ".join(tokens[1:])
        print(f"Asserting: {expression}")
        raise NotImplementedError(
            f"parse_assert function not implemented")
       


 
