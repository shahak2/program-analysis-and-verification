BOTTOM = "BOTTOM"

class SummationElement():
    def __init__(self, 
                 low, 
                 high):
        assert low <= high, f"Invalid values: {low} > {high}!"
        self.low = low
        self.high = high
    
    def __repr__(self):
        return f"[{self.low},{self.high}]"

    def __eq__(self, item2):
        if type(item2) != SummationElement:
            return False
        return self.low == item2.low and self.high == item2.high
    
    def __neq__(self, item2):
        return self.low != item2.low or self.high != item2.high
    
    def __add__(self, item2):
        if type(item2) == str and item2 == BOTTOM:
            if item2 == BOTTOM:
                return BOTTOM
            else:
                raise RuntimeError(f"Invalid bottom value {item2}")
        elif type(item2) == int:
            return SummationElement(self.low + item2, self.high + item2)
        else:
            return SummationElement(self.low + item2.low, self.high + item2.high)
    
    def __sub__(self, item2):
        if type(item2) == str:
            if item2 == BOTTOM:
                return BOTTOM
            else:
                raise RuntimeError(f"Invalid const value {item2}")
        elif type(item2) == int:
            return self.__add__(-item2)
        else:
            return SummationElement(self.low - item2.low, self.high - item2.high)