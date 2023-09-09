import base_domain

class ParityDomain(base_domain.BaseDomain):        
    
    CONTAINS_TABLE = {
        "ODD": ["BOTTOM", "ODD"],
        "EVEN": ["BOTTOM", "EVEN"],
        "TOP": ["BOTTOM", "ODD", "EVEN"],
        "BOTTOM": []
    }
    
    # MEET_TABLE = {
    #     ("ODD", "EVEN"): [],
    #     ("EVEN", "ODD"): [],
    #     "TOP": [],
    #     "BOTTOM": []
    # }
    
    # JOIN_TABLE = {
    #     "ODD": [],
    #     "EVEN": [],
    #     "TOP": [],
    #     "BOTTOM": []
    # }
        
    def parity_contains(item1, item2):
        ''' Returns true if item1 <= item2. In words, item2 contains item1. '''
        
        super(ParityDomain, ParityDomain).validate_elements([item1, item2])
        return item1 in ParityDomain.CONTAINS_TABLE[item2]
        
        
        
    
    def parity_join(item1, item2):
       super(ParityDomain, ParityDomain).validate_elements([item1, item2])
    
    def parity_meet(item1, item2):
        super(ParityDomain, ParityDomain).validate_elements([item1, item2])
        
    
    def __init__(self):
        D = {"TOP", "EVEN", "ODD", "BOTTOM"}
        
        super().__init__(
            D, 
            ParityDomain.parity_contains, 
            ParityDomain.parity_join, 
            ParityDomain.parity_meet)



# p = ParityDomain()
# ParityDomain.meet("EVEN", "EVEN")
# print(ParityDomain.domain)












