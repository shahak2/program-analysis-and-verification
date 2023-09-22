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