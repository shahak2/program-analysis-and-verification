import sys

SRC_RELATIVE_PATH = "src/"
TABLE_RELATIVE_PATH = SRC_RELATIVE_PATH + "table/"
TRANSFORMERS_RELATIVE_PATH = SRC_RELATIVE_PATH + "transformers/"

sys.path.insert(1, TABLE_RELATIVE_PATH)
sys.path.insert(1, TRANSFORMERS_RELATIVE_PATH)

import base_domain
from table import Table
from parity_transformer import ParityTransformer

ODD    = "ODD"
EVEN   = "EVEN"
BOTTOM = "BOTTOM"
TOP    = "TOP"

class ParityDomain(base_domain.BaseDomain):
    def __init__(self):
        DOMAIN = {TOP, EVEN, ODD, BOTTOM}
        
        self.contains_table = ParityDomain.get_contains_table()
        self.meet_table = ParityDomain.get_meet_table(DOMAIN)
        self.join_table = ParityDomain.get_join_table(DOMAIN)
        super().__init__(DOMAIN)
        self.transformer = ParityTransformer()
    
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
    
    def get_contains_table():
        return {
            TOP:    [BOTTOM, ODD, EVEN],
            EVEN:   [BOTTOM, EVEN],
            ODD:    [BOTTOM, ODD],
            BOTTOM: []
        }
            
    def contains(self, item1, item2):
        self.validate_elements([item1, item2])
        return item1 in self.contains_table[item2]
          
    def join(self, item1, item2):
        self.validate_elements([item1, item2])
        return self.join_table.get_value(item1, item2)
    
    def meet(self, item1, item2):
        self.validate_elements([item1, item2])
        return self.meet_table.get_value(item1, item2)
    
    def transform(self, 
                  values_vector,
                  statement):
        return self.transformer.parse_statement(statement,
                                                values_vector)