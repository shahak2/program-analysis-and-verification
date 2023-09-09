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
    
    domain = {}
    TOP = "TOP"
    BOTTOM = "BOTTOM"
    
    def __init__(
        self, 
        D,
        contains_op,
        join_op,
        meet_op,
        TOP = "TOP",
        BOTTOM = "BOTTOM"):
        
        BaseDomain.domain = D
        BaseDomain.meet = meet_op
        BaseDomain.join = join_op
        BaseDomain.contains = contains_op
        BaseDomain.TOP = TOP
        BaseDomain.BOTTOM = BOTTOM
        
    def meet(item1, item2):
        raise NameError('Meet method not implemented')

    def join(item1, item2):
        raise NameError('Join method not implemented')
    
    def contains( item1, item2):
        ''' Returns of item1 <= item2. In words, item2 contains item1. '''
        
        raise NameError('Contains method not implemented')
    
    def validate_elements(items):
        invalid_items = set()
        for item in items:
            if item not in BaseDomain.domain:
                invalid_items.add(item)
        if len(invalid_items) > 0:
            raise NameError(f"Elements {invalid_items} not in domain")







