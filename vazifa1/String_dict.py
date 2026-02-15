class String_dict:
    def __init__(self,str_):
        self.str_=str_
    def str_key_value(self):
        c=0
        d={}
        for i in range(len(self.str_)):
            for j in range(len(self.str_)):
                if self.str_[i]==self.str_[j]:
                    c+=1
            d[self.str_[i]]=c
            c=0
        return d