
BRA_ASCII = "\u27E8"
KET_ASCII = "\u27E9"

class CombinedElement():
    def __init__(self, 
                 parity_element, 
                 summation_element):
        self.parity_element = parity_element
        self.summation_element = summation_element
        
    def copy(self):
        return CombinedElement(self.parity_element, 
                               self.summation_element)
        
    def __eq__(self, 
               other):
        return self.parity_element == other.parity_element and \
            self.summation_element == other.summation_element
            
    def __repr__(self):
        return f'{BRA_ASCII}{self.parity_element}, {self.summation_element}{KET_ASCII}'