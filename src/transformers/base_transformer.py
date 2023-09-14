from consts import *
import transformer_utils as TU

class BaseTransformer():
    def __init__(self):
        self.variable_to_index_mapping = None
    
    def set_variables_to_index_mapping(self,
                                       variable_to_index_mapping: dict):
        self.variable_to_index_mapping = variable_to_index_mapping
        
    def check_transformer_ready(self):
        if not self.is_transformer_ready():
            raise RuntimeError(
                "Cannot use the transformer before setting\
                    a mapping between variables and their indices")
    
    def is_transformer_ready(self):
        return self.variable_to_index_mapping != None
    
    def check_valid_variable(self, variable):
        if not self.is_valid_variable(variable):
            raise RuntimeError(
                f"Cannot use variables that \
                    are not pre-defined: [{variable}]")
            
    def is_valid_variable(self, variable):
        return variable in self.variable_to_index_mapping.keys()
    
    def get_variable_index_in_vector(self, 
                                     variable):
        return self.variable_to_index_mapping[variable]
    
    def get_variable_domain_value(self, 
                                  variable, 
                                  values_vector):
        variable_index = \
            self.get_variable_index_in_vector(variable)
        return values_vector[variable_index]
    
    # Parsing 
    def parse_statement(self, 
                        statement,
                        values_vector):
        self.check_transformer_ready()
        tokens = statement.split()
        original_values = values_vector.copy()
        
        if tokens[0] == STATEMENTS.skip or \
            tokens[0] == STATEMENTS.entry:
            return self.transform_skip_or_entry(original_values)
        
        elif tokens[1] == STATEMENTS.assignment:
            return self.parse_assignment(tokens, 
                                         original_values)
            
        elif tokens[0] == STATEMENTS.assume:
            return self.parse_assume(tokens, 
                                     original_values)
            
        elif tokens[0] == STATEMENTS.assertion:
            return self.parse_assert(tokens, 
                                     original_values)
            
        else:
            raise SyntaxError(
                f"Invalid command: {statement}")
            
    def parse_assignment(self, 
                         tokens, 
                         values_vector):
        assign_to_variable = tokens[0]
        self.check_valid_variable(assign_to_variable)
        
        expression = tokens[2:]
        expression_as_domain_element = \
            self.evaluate_expression_to_domain_element(expression, 
                                                       values_vector)
        
        return self.transform_assignment(assign_to_variable,
                                         expression_as_domain_element,
                                         values_vector)
    
    # Transforms 
    def transform_skip_or_entry(self, 
                                values_vector):
        return values_vector

    def transform_assignment(self,
                             assign_to_variable,
                             expression_as_domain_element,
                             values_vector):
        assign_to_variable_index = \
            self.get_variable_index_in_vector(assign_to_variable)
            
        values_vector[assign_to_variable_index] = \
            expression_as_domain_element
        return values_vector
    
    def evaluate_expression_to_domain_element(self, 
                                              expression, 
                                              values_vector):
        if len(expression) == 1:
            basic_expression = expression[0]
            return self.evaluate_basic_expression(basic_expression,
                                                  values_vector)
        
        expression_variable = expression[0]
        
        left_side_value = \
            self.evaluate_basic_expression(expression_variable,
                                           values_vector)
        
        operation = expression[1]
        
        right_side_const = expression[2]
        
        right_side_value = \
            self.evaluate_basic_expression(right_side_const,
                                           values_vector)
        
        return self.evaluate_expression_by_operator(left_side_value, 
                                                    right_side_value,
                                                    operation)
        
    def evaluate_basic_expression(self, 
                                  basic_expression,
                                  values_vector):
        
        if basic_expression == ASSIGNMENTS_CONSTS.wildcard:
            return self.evaluate_unknown()
        
        elif TU.is_number(basic_expression):
            number_value = TU.extract_integer_value(basic_expression)
            return self.evaluate_constant(number_value)
        
        self.check_valid_variable(basic_expression)
        return self.evaluate_variable(basic_expression,
                                      values_vector)
    
    ######################################################    
    ##########              TODO                ##########
    ######################################################
    
    def parse_assume(self, 
                     tokens,
                     values_vector):
        raise NotImplementedError(
            f"parse_assume function not implemented")

    def parse_assert(self, 
                     tokens,
                     values_vector):
        raise NotImplementedError(
            f"parse_assert function not implemented")
    
    def evaluate_boolean(self):
        pass
    
    ######################################################
    ######################################################
    ######################################################
    
    ### Evaluation Methods to override
    def evaluate_unknown(self):
        raise NotImplementedError(
            f"evaluate_unknown function not implemented")
        
    def evaluate_constant(self, 
                          value: int):
        raise NotImplementedError(
            f"evaluate_constant function not implemented")
        
    def evaluate_variable(self, 
                          variable,
                          values_vector):
        raise NotImplementedError(
            f"evaluate_variable function not implemented")
        
    def evaluate_expression_by_operator(self, 
                                        value1,
                                        value2,
                                        operation):
        raise NotImplementedError(
            f"evaluate_expression_by_operator function not implemented")