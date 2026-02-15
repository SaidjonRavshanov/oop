class Cal:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    
    def summma(self):
        return self.x+self.y
    def diff(self):
        return self.x+self.y
    def mul(self):
        return self.x*self.y
    def div(self):
        return self.x/self.y

x=3
y=5
res=Cal(x=x,y=y)
print(res.diff())