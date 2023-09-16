import sys

SRC_RELATIVE_PATH = "src/"
TRANSFORMERS_RELATIVE_PATH = SRC_RELATIVE_PATH + "transformers/"

sys.path.insert(1, TRANSFORMERS_RELATIVE_PATH)

import base_domain
from summation_transformer import SummationTransformer


class SummationElement():

    def __init__(self, 
                 low, 
                 high):
        self.low = low
        self.high = high

class SummationDomain(base_domain.BaseDomain):
    def __init__(self):


        DOMAIN = {} # TODO: Decide if and how to use this
        
        super().__init__(DOMAIN)
        self.transformer = SummationTransformer()
    
    def join(self, 
             item1, 
             item2):
        ''' Returns the result for item1 (JOIN) item2'''
        raise NotImplementedError(
            'Join method not implemented')





