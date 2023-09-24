import sys

from consts import *
from parity_transformer import ParityTransformer
from summation_transformer import SummationTransformer
from transformer_utils import remove_brackets_with_word

SRC_RELATIVE_PATH = "src/"
DOMAINS_RELATIVE_PATH = SRC_RELATIVE_PATH + 'domains/'

sys.path.insert(1, DOMAINS_RELATIVE_PATH)

from combined_element import CombinedElement

BOTTOM = CombinedElement("BOTTOM", 
                         "BOTTOM")

class CombinedTransformer():
    def __init__(self, 
                 domain):
        self.summation_transformer = SummationTransformer(
            domain.summation_domain)
        
        self.parity_transformer = ParityTransformer()
        
        self.domain_interface = domain
    
    def set_variables_to_index_mapping(self,
                                       variable_to_index_mapping: dict):
        self.summation_transformer.set_variables_to_index_mapping(
            variable_to_index_mapping)
        
        self.parity_transformer.set_variables_to_index_mapping(
            variable_to_index_mapping)

    def is_transformer_ready(self):
        return self.summation_transformer.variable_to_index_mapping != None and \
            self.parity_transformer.variable_to_index_mapping != None
    
    def check_transformer_ready(self):
        if not self.is_transformer_ready():
            raise RuntimeError(
                "Cannot use the transformer before setting\
                    a mapping between variables and their indices")
    
    def is_valid_variable(self, variable):
        return variable in self.summation_transformer.variable_to_index_mapping.keys()
    
    def check_valid_variable(self, variable):
        if not self.is_valid_variable(variable):
            raise RuntimeError(
                f"Cannot use variables that \
                    are not pre-defined: [{variable}]")
            
    def get_variable_index_in_vector(self, 
                                     variable):
        return self.summation_transformer.variable_to_index_mapping[variable]
    
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
    

    def is_assertion_statement(self,
                               statement):
        return "assert" in statement

    def is_parity_condition(self, 
                                 statement):
        return "ODD" in statement or "EVEN" in statement

    def is_summation_condition(self, 
                               statement):
        return "SUM" in statement


    def get_summation_assertion(self, 
                                statement):
        assert_without_odd =  \
            remove_brackets_with_word(statement, "ODD")
        
        assert_without_odd_or_even = \
            remove_brackets_with_word(assert_without_odd, "EVEN")
        
        return assert_without_odd_or_even

    def get_parity_assertion(self, 
                             statement):
        assert_without_sum = \
            remove_brackets_with_word(statement, "SUM")
        
        return assert_without_sum


    # Parsing 
    def parse_statement(self, 
                        statement,
                        values_vector: list[CombinedElement]):
        parity_values_vector = \
            self.domain_interface.get_parity_values_from_vector(values_vector)
        
        summation_values_vector = \
            self.domain_interface.get_summation_values_from_vector(values_vector)
        
        if self.is_assertion_statement(statement):
            parity_assertion_res = True
            summation_assertion_res = True
            if self.is_summation_condition(statement):
                summation_assertion_statement = \
                    self.get_summation_assertion(statement)

                summation_assertion_res = \
                    self.summation_transformer.parse_statement(summation_assertion_statement, 
                                                               summation_values_vector)
            if self.is_parity_condition(statement):
                parity_assertion_statement = \
                    self.get_parity_assertion(statement)
                
                parity_assertion_res = \
                      self.parity_transformer.parse_statement(parity_assertion_statement, 
                                                              parity_values_vector)
            
            if parity_assertion_res == CANNOT_VALIDATE and \
                summation_assertion_res == True:
                return CANNOT_VALIDATE
            return parity_assertion_res and summation_assertion_res
                

        parity_result = self.parity_transformer.parse_statement(statement, 
                                                                parity_values_vector)
        
        summation_result = self.summation_transformer.parse_statement(statement, 
                                                                      summation_values_vector)
        
        return self.domain_interface.combine_summation_and_parity_vector(parity_result, 
                                                                         summation_result)
            
