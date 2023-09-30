from base_transformer import BaseTransformer
from consts import *
from transformer_utils import split_string_by_keywords

BOOLEANS_KEYWORDS = [
    PARITY_CONDITION_CONSTS.odd, 
    PARITY_CONDITION_CONSTS.even
]


class ParityTransformer(BaseTransformer):
    def __init__(self):
        
        super().__init__()
    
    def get_constant_domain_value(value: int):
        if value % 2 == 0:
            return EVEN
        return ODD
    
    def evaluate_unknown(self):
        return BOTTOM
        
    def evaluate_constant(self, 
                          value: int):
        return ParityTransformer.get_constant_domain_value(value)
        
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
        # There are mathematical "tricks" here.
        # Implementation of "value1 +- value2" in Parity Domain.
        if value1 == BOTTOM or value2 == BOTTOM:
            return BOTTOM
        if value1 == TOP or value2 == TOP:
            return TOP
        if value1 == value2:
            return EVEN
        return ODD
    
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
        
        if ParityTransformer.is_not_able_to_validate(variable_value):
            return CANNOT_VALIDATE
        
        if condition_type == PARITY_CONDITION_CONSTS.odd:
            return variable_value == ODD
        
        return variable_value == EVEN
    
    def get_assume_results_by_operator(self, 
                                       left_var,
                                       left_var_value, 
                                       right_var_value, 
                                       operator,
                                       values_vector):
        
        if operator == CONDITION_CONSTS.equal:
                if left_var_value == right_var_value:
                    return values_vector
                if left_var_value == TOP and \
                    (right_var_value == EVEN or right_var_value == ODD):
                    left_var_index = \
                        self.variable_to_index_mapping[left_var]
                    
                    new_values_vector = values_vector.copy()
                    new_values_vector[left_var_index] = right_var_value
                    return new_values_vector

                return self.get_vector_of_bottom_values(
                    len(values_vector))


        # not equal operator
        if left_var_value != right_var_value:
            if operator == CONDITION_CONSTS.not_equal:
                return values_vector

        return self.get_vector_of_bottom_values(
            len(values_vector))
    