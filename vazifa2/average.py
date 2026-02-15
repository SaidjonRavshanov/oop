import math

class Average:
    def __init__(self, a, b):
        self.a, self.b = a, b
    def arithmetic_mean(self):
        return (self.a + self.b) / 2
    def geometric_mean(self):
        return math.sqrt(self.a * self.b)
