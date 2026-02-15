class Value_t_f:
    def __init__(self,date):
        self.date=date
    def element_t_f(self,elemet):
        return elemet in self.date.values()