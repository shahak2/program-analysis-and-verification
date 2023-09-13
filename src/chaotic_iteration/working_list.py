from random import sample

class WorkingList():
    def __init__(self, elements):
        self.elements = set(elements)
        
    def pop_random_element(self):
        if self.elements:
            random_element = sample(list(self.elements), 1)[0]
            self.elements.remove(random_element)
        return random_element
    
    def isEmpty(self):
        return len(self.elements) == 0
    
    def insert_element(self, element):
        self.elements.add(element)
        
    def insert_elements(self, elements):
        for element in elements:
            self.insert_element(element)