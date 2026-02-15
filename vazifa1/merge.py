class Merge:
    def __init__(self,t1,t2,t3):
        self.t1=t1
        self.t2=t2
        self.t3=t3
    def merge_t(self):
        return self.t1 | self.t2 | self.t3