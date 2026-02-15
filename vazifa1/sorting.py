class Sorting:
    def __init__(self,data):
        self.data=data

    def sort_key_value(self,x):
        items=list(self.data.items())
        n=len(items)
        
        for i in range(n):
            for j in range(0, n - i - 1):
                if items[j][x] > items[j + 1][x]:
                    items[j], items[j + 1] = items[j + 1], items[j]
        return dict(items)   
       
    def sorting_value(self):
        return self.sort_key_value(1)
    def sorting_key(self):
        return self.sort_key_value(0)             
