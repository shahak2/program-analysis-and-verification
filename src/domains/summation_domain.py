import sys
import math

SRC_RELATIVE_PATH = "src/"
TRANSFORMERS_RELATIVE_PATH = SRC_RELATIVE_PATH + "transformers/"

sys.path.insert(1, TRANSFORMERS_RELATIVE_PATH)

import base_domain
from summation_transformer import SummationTransformer

from summation_element import SummationElement

class SummationDomain(base_domain.BaseDomain):
    def __init__(self):
        # Interval Domain. The DOMAIN is {Integers, Top=[-inf,inf], BOTTOM}.
        DOMAIN = { }
        
        super().__init__(DOMAIN)
        self.transformer = SummationTransformer()
        self.TOP = SummationElement(-math.inf, math.inf)
    
    def join(self, 
             item1, 
             item2):
        if item1 == self.BOTTOM:
            return item2
        if item2 == self.BOTTOM:
            return item1
        
        low = min(item1.low, item2.low)
        high = max(item1.high, item2.high)
        return SummationElement(low, high)
    
    def meet(self, 
             item1, 
             item2):
        if item1 == self.BOTTOM or item2 == self.BOTTOM:
            return self.BOTTOM
        
        low = max(item1.low, item2.low)
        high = min(item1.high, item2.high)
        if low > high:
            return self.BOTTOM
        return SummationElement(low, high)
        
    def widen(self, 
             item1, 
             item2):
        if item1 == self.BOTTOM:
            return item2
        if item2 == self.BOTTOM:
            return item1
        
        low = item1.low if item1.low <= item2.low else -math.inf
        high = item1.high if item1.high <= item2.high else math.inf
        return SummationElement(low, high)

    def narrow(self, 
                item1, 
                item2):
        if item1 == self.BOTTOM:
            return item2
        if item2 == self.BOTTOM:
            return item1
        
        low = item2.low if item1.low == (-math.inf) else item1.low
        high = item2.high if item1.high == math.inf else item1.high
        return SummationElement(low, high)
    
    
    def vectors_widen_from_list(self, 
                               vectors_list):
            number_of_vectors = len(vectors_list)
            result_vector = vectors_list[0].copy()
            vectors_length = len(result_vector)
            
            for vector_number in range(1, number_of_vectors):
                
                result_vector = self.vector_widen(result_vector, 
                                                  vectors_list[vector_number])
            
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