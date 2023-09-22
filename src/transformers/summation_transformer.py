import sys

SRC_RELATIVE_PATH = "src/"
DOMAINS_PATH = SRC_RELATIVE_PATH + 'domains/'

sys.path.insert(1, DOMAINS_PATH)

from consts import *
from base_transformer import BaseTransformer
from summation_element import SummationElement
from transformer_utils import parse_summation_conditions


class SummationTransformer(BaseTransformer):
    def __init__(self):
        
        super().__init__()
    
    def evaluate_constant(self, 
                          value: int):
        return SummationElement(value, value)
    
    def evaluate_unknown(self):
        return BOTTOM

    def evaluate_variable(self,
                          variable,
                          values_vector):
        self.check_valid_variable(variable)
        return self.get_variable_domain_value(variable, 
                                            values_vector)
    
    def evaluate_expression_by_operator(self, 
                                        value1,
                                        value2,
                                        operation):
        if value1 == BOTTOM or value2 == BOTTOM:
            return BOTTOM

        if operation == OPERATIONS.add:
            return value1 + value2
        return value1 - value2

    def evaluate_booleans(self, 
                          and_conditions_string,
                          values_vector):
        conditions_list = \
            parse_summation_conditions(and_conditions_string)
        
        for condition in conditions_list:
            result = self.evaluate_condition(condition, 
                                             values_vector)
            
            if result == CANNOT_VALIDATE:
                return CANNOT_VALIDATE
            
            if not result:
                return False
        
        return True
    
    def is_not_able_to_validate(variable_value):
        return variable_value == BOTTOM
    
    def evaluate_sum(self, 
                     variables, 
                     values_vector):
        
        sum_in_domain = 0
        
        for variable in variables:
            self.check_valid_variable(variable)
            variable_value = \
                self.get_variable_domain_value(variable, 
                                               values_vector)
            if variable_value == BOTTOM:
                return BOTTOM
            sum_in_domain = variable_value + sum_in_domain
            
        return sum_in_domain
    
    def evaluate_condition(self, 
                           condition,
                           values_vector):
        
        left_sum_variables = condition[0]
        left_sum = self.evaluate_sum(left_sum_variables, 
                                     values_vector)
        
        if SummationTransformer.is_not_able_to_validate(left_sum):
            return CANNOT_VALIDATE
        
        right_sum_variables = condition[1]
        right_sum = self.evaluate_sum(right_sum_variables, 
                                      values_vector)
        
        if SummationTransformer.is_not_able_to_validate(right_sum):
            return CANNOT_VALIDATE
        
        return right_sum == left_sum