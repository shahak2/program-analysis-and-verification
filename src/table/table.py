
class Table:
    
    def __init__(self, elements):
        self.elements = elements
        
        self.table = {}

    def get_value(self, elem1, elem2):
        assert elem1 in self.elements and elem2 in self.elements, "Invalid elements"

        key = tuple(sorted([elem1, elem2]))
        return self.table[key]
    
    
    def set_relation(self, elem1, elem2, value):
        assert elem1 in self.elements and elem2 in self.elements, "Invalid elements"
        
        key = tuple(sorted([elem1, elem2]))
        self.table[key] = value

    def print_table(self):
        print("\n Table:\n")
        for elem1 in self.elements:
            row = []
            for elem2 in self.elements:
                if elem1 == elem2:
                    row.append("N/A")
                else:
                    result = self.get_value(elem1, elem2)
                    row.append(result)
            print(f" {elem1} | {row}")
        print()





