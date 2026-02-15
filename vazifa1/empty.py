class Empty:
    def __init__(self,date):
        self.date=date
    def empty_check(self):
        return bool(self.date)  