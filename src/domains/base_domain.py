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


    
    def transform(self, 
                 statement, 
                 values_vector):
        pass
    
    def join_vector(self, 
                    statement, 
                    values_vector):
        pass
    
    
    
    





