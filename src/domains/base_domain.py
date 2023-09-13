class BaseDomain:
    """  
    Abstract Domain Representation 
    
        D - domain
        contains_op - subseteq 
        join
        meet
        top
        bottom
    
    """
    def __init__(self, 
                 D, 
                 TOP = "TOP", 
                 BOTTOM = "BOTTOM"):
        
        self.domain = D
        self.TOP = TOP
        self.BOTTOM = BOTTOM
        
    def meet(self, item1, item2):
        raise NameError('Meet method not implemented')

    def join(self, item1, item2):
        raise NameError('Join method not implemented')
    
    def contains(self, item1, item2):       
        raise NameError('Contains method not implemented')
    
    def validate_elements(self, items):
        invalid_items = set()
        for item in items:
            if item not in self.domain:
                invalid_items.add(item)
        if len(invalid_items) > 0:
            raise NameError(f"Elements {invalid_items} not in domain")

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
        
    def transform(self, 
                  statement, 
                  values_vector):
        pass
    
    
    
    