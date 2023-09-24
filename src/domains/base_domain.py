class BaseDomain:
    """  
    Abstract Domain Representation 
    
        D - domain
        contains_op - subseteq 
        join
        meet
        top
        bottom
        transformer - Input:  statement, values_vector
                      Output: parses the statement and performs the relevant 
                              abstract transform on values_vector.
    """
    
    def __init__(self, 
                 D, 
                 TOP = "TOP", 
                 BOTTOM = "BOTTOM"):
        
        self.domain = D
        self.TOP = TOP
        self.BOTTOM = BOTTOM
        self.transformer = None
        
    def join(self, 
             item1, 
             item2):
        ''' Returns the result for item1 (JOIN) item2'''
        raise NotImplementedError(
            'Join method not implemented')
        
    def meet(self, item1, item2):
        ''' Returns the result for item1 (MEET) item2'''
        raise NotImplementedError(
            'Meet method not implemented')
    
    def contains(self, item1, item2):  
        ''' Returns true if item1 <= item2. In words, item2 contains item1. '''     
        raise NotImplementedError(
            'Contains method not implemented')
    
    def validate_elements(self, items):
        invalid_items = set()
        for item in items:
            if item not in self.domain:
                invalid_items.add(item)
        if len(invalid_items) > 0:
            raise NotImplementedError(
                f"Elements {invalid_items} not in domain")

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
    
    def vectors_join_from_list(self, 
                               vectors_list):
        number_of_vectors = len(vectors_list)
        result_vector = vectors_list[0].copy()
        vectors_length = len(result_vector)
        
        for vector_number in range(1, number_of_vectors):
            result_vector = self.vector_join(result_vector, 
                                                vectors_list[vector_number])
        return result_vector
    
    def transform(self, 
                  values_vector,
                  statement):
        return self.transformer.parse_statement(statement,
                                                values_vector)
            
    
    
    
    
    