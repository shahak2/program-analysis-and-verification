
from base_transformer import BaseTransformer

class ParityTransformer(BaseTransformer):
    def __init__(self,
                 variable_to_index_mapping):
        
        super().__init__(variable_to_index_mapping)
    
    
    ### Implement all the needed parent functions