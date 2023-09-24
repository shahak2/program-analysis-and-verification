import sys

SRC_RELATIVE_PATH = "src/"
TRANSFORMERS_RELATIVE_PATH = SRC_RELATIVE_PATH + "transformers/"

sys.path.insert(1, TRANSFORMERS_RELATIVE_PATH)

import base_domain
from combined_transformer import CombinedTransformer
from parity_domain import ParityDomain
from summation_domain import SummationDomain
from combined_element import CombinedElement


class CombinedDomain():
    
    def __init__(self):
        
        self.transformer = CombinedTransformer(self)
        
        self.parity_domain= ParityDomain()
        self.summation_domain = SummationDomain()
        
        self.TOP = CombinedElement(self.parity_domain.TOP,
                                   self.summation_domain.TOP)
        
        self.BOTTOM = CombinedElement("BOTTOM", 
                                      "BOTTOM")
    
    def get_parity_values_from_vector(self, 
                                      values_vector: list[CombinedElement]):
        return [combined_ele.parity_element for combined_ele in values_vector]
    
    def get_summation_values_from_vector(self, 
                                         values_vector: list[CombinedElement]):
        return [combined_ele.summation_element for combined_ele in values_vector]
    
    def combine_summation_and_parity_vector(self, 
                                            parity_vector,
                                            summation_vector):
        values_vector = []
        for i in range(0, len(summation_vector)):
            values_vector.append(CombinedElement(parity_vector[i], 
                                                 summation_vector[i]))
        return values_vector
        
    def join(self, 
             item1: CombinedElement, 
             item2: CombinedElement):
        parity_join_result = self.parity_domain.join(item1.parity_element,
                                                     item2.parity_element)
        summation_join_result = self.summation_domain.join(item1.summation_element,
                                                           item2.summation_element)
        
        return CombinedElement(parity_join_result,
                               summation_join_result)

    def meet(self, 
             item1: CombinedElement, 
             item2: CombinedElement):
        parity_meet_result = self.parity_domain.meet(item1.parity_element,
                                                     item2.parity_element)
        summation_meet_result = self.summation_domain.meet(item1.summation_element,
                                                           item2.summation_element)
        
        return CombinedElement(parity_meet_result,
                               summation_meet_result)
    
    def transform(self, 
                  values_vector,
                  statement):
        return self.transformer.parse_statement(statement,
                                                values_vector)
        
    def widen(self,
              item1: CombinedElement, 
              item2: CombinedElement):   
        # Ignores widen in parity domain     
        summation_element1 = item1.summation_element
        summation_element2 = item2.summation_element
        
        summation_widen_result = \
            self.summation_domain.widen(summation_element1, 
                                        summation_element2)
        
        return CombinedElement(item2.parity_element,
                               summation_widen_result)

    def narrow(self, 
              item1: CombinedElement, 
              item2: CombinedElement):
        # Ignores narrow in parity domain 
        summation_element1 = item1.summation_element
        summation_element2 = item2.summation_element
        
        summation_narrow_result = \
            self.summation_domain.narrow(summation_element1, 
                                        summation_element2)
            
        return CombinedElement(item2.parity_element,
                               summation_narrow_result)
    
    def vector_join(self, 
                    values_vector1,
                    values_vector2):
        assert len(values_vector1) == len(values_vector1), \
            "Cannot perform join on vectors with different length!"
        
        vector_length = len(values_vector1)
        result_vector = [None for i in range(0, vector_length)]
        for i in range(0, vector_length):
            result_vector[i] = self.join(values_vector1[i],
                                            values_vector2[i])
        return result_vector
    
    def vector_meet(self, 
                    values_vector1,
                    values_vector2):
        assert len(values_vector1) == len(values_vector1), \
            "Cannot perform meet on vectors with different length!"
        
        vector_length = len(values_vector1)
        result_vector = [None for i in range(0, vector_length)]
        for i in range(0, vector_length):
            result_vector[i] = self.meet(values_vector1[i],
                                         values_vector2[i])
        return result_vector
        
    def vector_widen(self, 
                     values_vector1,
                     values_vector2):
        assert len(values_vector1) == len(values_vector1), \
            "Cannot perform widen on vectors with different length!"
        
        vector_length = len(values_vector1)
        result_vector = [None for i in range(0, vector_length)]
        for i in range(0, vector_length):
            result_vector[i] = self.widen(values_vector1[i],
                                            values_vector2[i])
        return result_vector
        
    def vector_narrow(self, 
                      values_vector1,
                      values_vector2):
        assert len(values_vector1) == len(values_vector1), \
            "Cannot perform narrow on vectors with different length!"
        
        vector_length = len(values_vector1)
        result_vector = [None for i in range(0, vector_length)]
        for i in range(0, vector_length):
            result_vector[i] = self.narrow(values_vector1[i],
                                           values_vector2[i])
        return result_vector
    
    def vectors_join_from_list(self, 
                               vectors_list):
        number_of_vectors = len(vectors_list)
        result_vector = vectors_list[0].copy()
        vectors_length = len(result_vector)
        
        for vector_number in range(1, number_of_vectors):
            
            result_vector = self.vector_join(result_vector, 
                                                vectors_list[vector_number])
        
        return result_vector















