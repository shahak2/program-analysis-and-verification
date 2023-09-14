import re
from consts import *
import transformer_utils as TU


class BaseTransformer():
    def __init__(self):
        self.variable_to_index_mapping = None
    
    def set_variables_to_index_mapping(self,
                                       variable_to_index_mapping: dict):
        self.variable_to_index_mapping = variable_to_index_mapping

    def is_transformer_ready(self):
        return self.variable_to_index_mapping != None
    
    def check_transformer_ready(self):
        if not self.is_transformer_ready():
            raise RuntimeError(
                "Cannot use the transformer before setting\
                    a mapping between variables and their indices")
    
    def is_valid_variable(self, variable):
        return variable in self.variable_to_index_mapping.keys()
    
    def check_valid_variable(self, variable):
        if not self.is_valid_variable(variable):
            raise RuntimeError(
                f"Cannot use variables that \
                    are not pre-defined: [{variable}]")
            
    def get_variable_index_in_vector(self, 
                                     variable):
        return self.variable_to_index_mapping[variable]
    
    def get_variable_domain_value(self, 
                                  variable, 
                                  values_vector):
        variable_index = \
            self.get_variable_index_in_vector(variable)
        return values_vector[variable_index]
    
    def is_assume_split_node(self, 
                             statement):
        return CONDITION_CONSTS.left_bracket not in statement
    
    def get_vector_of_bottom_values(self, 
                                    size):
        return [BOTTOM] * size
        
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
        
        elif STATEMENTS.assume in statement:
            return self.transform_assume(statement, 
                                         original_values)
        elif tokens[0] == STATEMENTS.assertion:
            return self.parse_assert(statement, 
                                     original_values)
        elif tokens[1] == STATEMENTS.assignment:
            return self.parse_assignment(tokens, 
                                         original_values)   
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
    
    def parse_assert(self, 
                     statement,
                     values_vector):
        regex_pattern = r'\((.*?)\)'
        matches = re.findall(regex_pattern, statement)

        or_conditions_list = [match.strip() for match in matches]
        
        for and_conditions_list in or_conditions_list:
            result = self.evaluate_booleans(and_conditions_list,
                                            values_vector)
            if result:
                return True
        
        return False
    
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
    
    def transform_assume(self, 
                         statement, 
                         values_vector):
        
        if self.is_assume_split_node(statement):
            return values_vector
        
        condition_tokens = TU.strip_brackets(statement).split()
        
        if len(condition_tokens) == 1:
            return self.transform_simple_assume(condition_tokens[0], 
                                                values_vector)
        left_var = condition_tokens[0]
        operator = condition_tokens[1]
        right_var = condition_tokens[2]
        
        left_var_value = \
            self.evaluate_expression_to_domain_element(left_var, 
                                                       values_vector)
        right_var_value = \
            self.evaluate_expression_to_domain_element(right_var, 
                                                       values_vector)
        
        return self.get_results_by_operator(left_var_value, 
                                            right_var_value, 
                                            operator,
                                            values_vector)
        
    def get_results_by_operator(self, 
                                left_var_value, 
                                right_var_value, 
                                operator,
                                values_vector):
        
        if left_var_value == right_var_value:
            if operator == CONDITION_CONSTS.equal:
                return values_vector
            elif operator == CONDITION_CONSTS.not_equal:
                return self.get_vector_of_bottom_values(
                    len(values_vector))
            
        if operator == CONDITION_CONSTS.not_equal:
                return values_vector
        
        return self.get_vector_of_bottom_values(
            len(values_vector))
        
    def transform_simple_assume(self, 
                                token, 
                                values_vector):
        
        if token == BOOLEANS.true:
            return values_vector
        return self.get_vector_of_bottom_values(
            len(values_vector))
    
    # General Evaluations
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
    ########### Evaluation Methods to override ###########
    ######################################################
    
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
    
    def evaluate_booleans(self, 
                          and_conditions_list,
                          values_vector):
        raise NotImplementedError(
            f"evaluate_boolean function not implemented")