from base_transformer import BaseTransformer
from consts import *
from transformer_utils import split_string_by_keywords

BOOLEANS_KEYWORDS = [
    SUMMATION_CONDITION_CONSTS.summation
]


class SummationTransformer(BaseTransformer):
    def __init__(self):
        
        super().__init__()
    
    def evaluate_constant(self, 
                          value: int):
        return value
    
    def evaluate_unknown(self):
        return BOTTOM
        
    
    ##########################################
    ##########################################
    ################## HERE ##################
    ##########################################
    ##########################################

    def evaluate_variable(self,
                          variable,
                          values_vector):
        pass
    
    def evaluate_expression_by_operator(self, 
                                        value1,
                                        value2,
                                        operation):
        pass
    
    def evaluate_booleans(self, 
                          and_conditions_string,
                          values_vector):
        conditions_list = \
            split_string_by_keywords(and_conditions_string,
                                     BOOLEANS_KEYWORDS)
        
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
    
    def evaluate_condition(self, 
                           condition,
                           values_vector):
        
        condition_type, variable = condition.split()
        self.check_valid_variable(variable)
        
        variable_value = \
            self.get_variable_domain_value(variable, 
                                           values_vector)
        
        if SummationTransformer.is_not_able_to_validate(variable_value):
            return CANNOT_VALIDATE
        
        if condition_type == PARITY_CONDITION_CONSTS.odd:
            return variable_value == ODD
        
        return variable_value == EVEN