class Kv:
    def __init__(self,n):
        self.n=n
    def dict_kv(self):
        d={}
        for i in range(1,self.n+1):
            d[i]=i**2
        return d
    