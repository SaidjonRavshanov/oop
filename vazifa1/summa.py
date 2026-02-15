class Summa:
    def __init__(self,date):
        self.date=date
    def summa(self):
        s=0
        for i in self.date.values():
            s+=i
        return s   