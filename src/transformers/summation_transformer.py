import sys

SRC_RELATIVE_PATH = "src/"
DOMAINS_PATH = SRC_RELATIVE_PATH + 'domains/'

sys.path.insert(1, DOMAINS_PATH)

from consts import *
import math
from base_transformer import BaseTransformer
from summation_element import SummationElement
import transformer_utils as TU


class SummationTransformer(BaseTransformer):
    def __init__(self, 
                 domain):
        self.domain_interface = domain
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
            TU.parse_summation_conditions(and_conditions_string)
        
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
    
    def get_meet_neutral_vector(vector_length):
        TOP = SummationElement(-math.inf, math.inf)
        return [TOP] * vector_length   
    
    def transform_assume(self, 
                         statement, 
                         values_vector):
        '''
            - case x = c:   perform (values_vector) MEET ([(-inf, inf),...,SummationElement(c,c),...,(-inf, inf)])
            
            - case x != c:  perform (values_vector) MEET ([(-inf, inf),...,SummationElement(-inf,c-1),...,(-inf, inf)])
                                    JOIN
                                    (values_vector) MEET ([(-inf, inf),...,SummationElement(c+1, inf),...,(-inf, inf)])
                                    
            - case x = y:   perform (values_vector) MEET ([(-inf, inf),...,x_index: SummationElement(y.low, y.high),...,y_index: SummationElement(x.low, x.high),...,(-inf, inf)])
            
            - case x != y:  perform (values_vector) MEET ([(-inf, inf),...,x_index: SummationElement(-inf, y.low-1),...,y_index: SummationElement(x.high+1, inf),...,(-inf, inf)])
                                    JOIN
                                    perform (values_vector) MEET ([(-inf, inf),...,x_index: SummationElement(y.high+1, inf),...,y_index: SummationElement(-inf, x.low-1),...,(-inf, inf)])
        '''
        
        
        if self.is_assume_split_node(statement):
            return values_vector
        
        condition_tokens = TU.strip_brackets(statement).split()
        
        if len(condition_tokens) == 1:
            return self.transform_simple_assume(condition_tokens[0], 
                                                values_vector)
        left_var = condition_tokens[0]
        operator = condition_tokens[1]
        right_exp = condition_tokens[2]
        
        self.check_valid_variable(left_var)
        
        if TU.is_number(right_exp):
            number_value = TU.extract_integer_value(right_exp)
            left_var_index = \
                    self.variable_to_index_mapping[left_var]
            if operator == CONDITION_CONSTS.equal:
                meet_vector = values_vector.copy()
                    
                element =  SummationElement(number_value,
                                            number_value)
                
                meet_vector[left_var_index] = element
                
                return self.domain_interface.vector_meet(values_vector,
                                                         meet_vector)
            else:
                meet1_vector = values_vector.copy()
                meet2_vector = values_vector.copy()
                    
                element1 =  SummationElement(-math.inf, 
                                             number_value - 1)
                element2 =  SummationElement(number_value + 1, 
                                             math.inf)
                meet1_vector[left_var_index] = element1
                meet2_vector[left_var_index] = element2
                
                meet1_vector = self.domain_interface.vector_meet(values_vector,
                                                                 meet1_vector)
                meet2_vector = self.domain_interface.vector_meet(values_vector,
                                                                 meet2_vector)
                
                return self.domain_interface.vector_join(meet1_vector, 
                                                         meet2_vector)
        else:
            self.check_valid_variable(right_exp)

            right_var_index = \
                    self.variable_to_index_mapping[right_exp]
            
            left_var_index = \
                    self.variable_to_index_mapping[left_var]
                    
            right_var_value =  \
                    self.evaluate_basic_expression(right_exp, 
                                                   values_vector)
                
            left_var_value =  \
                self.evaluate_basic_expression(left_var, 
                                               values_vector)
                
            if right_var_value == BOTTOM or left_var_value == BOTTOM:
                return self.get_vector_of_bottom_values(
                    len(values_vector))
                    
            if operator == CONDITION_CONSTS.equal:
                meet_vector = \
                    SummationTransformer.get_meet_neutral_vector(
                        len(values_vector))

                meet_vector[left_var_index] = right_var_value
                meet_vector[right_var_index] = left_var_value
                
                return self.domain_interface.vector_meet(values_vector,
                                                         meet_vector)
            else:
                if right_var_value == left_var_value:
                    return self.get_vector_of_bottom_values(
                        len(values_vector))
                    
                meet_vector1 = values_vector.copy()
                meet_vector2 = values_vector.copy()
                    
                meet_vector1[left_var_index] = SummationElement(-math.inf, 
                                                                right_var_value.low - 1)
                
                meet_vector2[left_var_index] = SummationElement(right_var_value.high + 1,
                                                                math.inf)

                meet_vector1 = self.domain_interface.vector_meet(values_vector,
                                                                 meet_vector1)
                meet_vector2 = self.domain_interface.vector_meet(values_vector,
                                                                 meet_vector2)
                
                return self.domain_interface.vector_join(meet_vector1, 
                                                         meet_vector2)
                
        
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
        
        
    def get_assume_results_by_operator(self, 
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