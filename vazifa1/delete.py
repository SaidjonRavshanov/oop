class Delete:
    def __init__(self,date):
        self.date=date
    def key_with_value(self,key):
        
        del self.date[key]
        return self.date