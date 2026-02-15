import math

class Circle:
    def __init__(self, S):
        self.S = S
    def radius(self):
        return math.sqrt(self.S / math.pi)
