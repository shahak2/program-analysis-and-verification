import sys

SRC_RELATIVE_PATH = "src/"
TABLE_RELATIVE_PATH = SRC_RELATIVE_PATH + "table/"

sys.path.insert(1, TABLE_RELATIVE_PATH)

import base_domain
from table import Table

ODD = "ODD"
EVEN = "EVEN"
BOTTOM = "BOTTOM"
TOP = "TOP"

class ParityDomain(base_domain.BaseDomain):
    
    def get_join_table(domain):
        join_table = Table(list(domain))
        JOIN_RELATIONS = [
            (TOP,     EVEN,      TOP    ), 
            (TOP,     ODD,       TOP    ), 
            (TOP,     TOP,       TOP    ),
            (TOP,     BOTTOM,    TOP    ), 
            (BOTTOM,  EVEN,      EVEN   ), 
            (BOTTOM,  ODD,       ODD    ),
            (BOTTOM,  BOTTOM,    BOTTOM ), 
            (ODD,     EVEN,      TOP    ),
            (ODD,     ODD,       ODD    ),
            (EVEN,    EVEN,      EVEN   )
        ]
        
        for relation in JOIN_RELATIONS:
            join_table.set_relation(relation[0], 
                                    relation[1], 
                                    relation[2])
        return join_table  
    
    def get_meet_table(domain):
        meet_table = Table(list(domain))
        MEET_RELATIONS = [
            (BOTTOM,  TOP,       BOTTOM), 
            (BOTTOM,  EVEN,      BOTTOM), 
            (BOTTOM,  ODD,       BOTTOM),
            (BOTTOM,  BOTTOM,    BOTTOM), 
            (TOP,     EVEN,      EVEN  ), 
            (TOP,     ODD,       ODD   ), 
            (TOP,     TOP,       TOP   ),
            (ODD,     EVEN,      BOTTOM),
            (ODD,     ODD,       ODD   ),
            (EVEN,    EVEN,      EVEN  )
        ]
        
        for relation in MEET_RELATIONS:
            meet_table.set_relation(relation[0], 
                                    relation[1], 
                                    relation[2])
        return meet_table
        
    def contains(self, item1, item2):
        ''' Returns true if item1 <= item2. In words, item2 contains item1. '''
        
        self.validate_elements([item1, item2])
        return item1 in self.contains_table[item2]
        
        
    def join(self, item1, item2):
        ''' Returns the result for item1 (JOIN) item2'''
        
        self.validate_elements([item1, item2])
        return self.join_table.get_value(item1, item2)
    
    def meet(self, item1, item2):
        ''' Returns the result for item1 (MEET) item2'''
        
        self.validate_elements([item1, item2])
        return self.meet_table.get_value(item1, item2)
    
    
    def get_contains_table():
        return {
            "ODD": ["BOTTOM", "ODD"],
            "EVEN": ["BOTTOM", "EVEN"],
            "TOP": ["BOTTOM", "ODD", "EVEN"],
            "BOTTOM": []
        }
    
    def __init__(self):
        DOMAIN = {"TOP", "EVEN", "ODD", "BOTTOM"}
        
        self.contains_table = ParityDomain.get_contains_table()
        self.meet_table = ParityDomain.get_meet_table(DOMAIN)
        self.join_table = ParityDomain.get_join_table(DOMAIN)
        super().__init__(DOMAIN)
        
        
        
        
        
        










# # Example usage:
# elements = ["A", "B", "C", "D"]
# my_table = Table(elements)



# # Add relations for element A
# my_table.set_relation("A", "B", 42)
# my_table.set_relation("A", "C", 55)
# my_table.set_relation("A", "D", 12)

# # Add relations for element B
# my_table.set_relation("B", "C", 30)
# my_table.set_relation("B", "D", 18)

# # Add relations for element C
# my_table.set_relation("C", "D", 25)


# my_table.print_table()






