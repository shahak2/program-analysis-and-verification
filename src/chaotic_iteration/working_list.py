from random import sample

class WorkingList():
    def __init__(self, elements, ignore_elements = set()):
        self.elements = set(elements)
        self.ignore_elements = ignore_elements
        
    def pop_random_element(self):
        if self.elements:
            random_element = sample(list(self.elements), 1)[0]
            self.elements.remove(random_element)
        return random_element
    
    def is_empty(self):
        return len(self.elements) == 0
    
    def insert_element(self, element):
        if element in self.ignore_elements:
            return
        self.elements.add(element)
        
    def insert_elements(self, elements):
        for element in elements:
            self.insert_element(element)

    def get_snapshot(self):
        return self.elements.copy()