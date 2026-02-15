class Add:
    def __init__(self,date):
        self.date=date
    
    def add_k_v(self,key_,value_):
        self.date[key_]=value_
        return self.date
