# from consts import *
from base_transformer import BaseTransformer
from consts import *

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