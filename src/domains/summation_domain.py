import sys
import math

SRC_RELATIVE_PATH = "src/"
TRANSFORMERS_RELATIVE_PATH = SRC_RELATIVE_PATH + "transformers/"

sys.path.insert(1, TRANSFORMERS_RELATIVE_PATH)

import base_domain
from summation_transformer import SummationTransformer


class SummationElement():
    def __init__(self, 
                 low, 
                 high):
        assert low <= high, f"Invalid values: {low} > {high}!"
        self.low = low
        self.high = high
    
    def __repr__(self):
        return f"[{self.low},{self.high}]"

    def __eq__(self, item2):
        return self.low == item2.low and self.high == item2.high
    
    def __neq__(self, item2):
        return self.low != item2.low or self.high != item2.high

class SummationDomain(base_domain.BaseDomain):
    def __init__(self):
        # Interval Domain. The DOMAIN is {Integers, Top=[-inf,inf], Bottom}.
        DOMAIN = {
            "TOP": SummationElement(-math.inf, math.inf),
            "BOTTOM": "BOTTOM"
        }
        
        super().__init__(DOMAIN)
        self.transformer = SummationTransformer()
    
    def join(self, 
             item1, 
             item2):
        low = min(item1.low, item2.low)
        high = max(item1.high, item2.high)
        return SummationElement(low, high)
    
    def meet(self, 
             item1, 
             item2):
        low = max(item1.low, item2.low)
        high = min(item1.high, item2.high)
        if low > high:
            return self.domain.BOTTOM
        return SummationElement(low, high)
        
    def widen(self, 
             item1, 
             item2):
        if item1 == self.domain.BOTTOM:
            return item2
        if item2 == self.domain.BOTTOM:
            return item1
        
        low = item1.low if item1.low <= item2.low else -math.inf
        high = item1.high if item1.high <= item2.high else math.inf
        return SummationElement(low, high)

    def narrow(self, 
                item1, 
                item2):
        
        if item1 == self.domain.BOTTOM:
            return item2
        if item2 == self.domain.BOTTOM:
            return item1
        
        low = item1.low if item1.low <= item2.low else -math.inf
        high = item1.high if item1.high <= item2.high else math.inf
        return SummationElement(low, high)