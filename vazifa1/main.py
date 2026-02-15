from sorting import Sorting
from add import Add
from delete import Delete
from empty import Empty
from kv import Kv
from merge import Merge
from String_dict import String_dict
from summa import Summa
from value import Value_t_f
#------------------------
# ----------1------------- 
dict_={1:4,4:7,2:5,0:10,9:19}   
v=Sorting(dict_)
print(v.sorting_value())
print(v.sorting_key())
#------------------------
#------------2------------
d=Add(dict_)
print(d.add_k_v(10,11))
#------------------------
#----------3------------
t1=v.sorting_value()
t2=v.sorting_key()
t3=d.add_k_v(10,11)

m=Merge(t1,t2,t3)
print(m.merge_t())
#-------------------
#---------4---------
check=Value_t_f(dict_)
print(check.element_t_f(11))
#-------------------
#---------5-----------
k=Kv(8)
print(k.dict_kv())
#---------------------
#--------6------------
h=Summa(dict_)
print(h.summa())
#---------------------
#-------7--------------
r=Delete(dict_)
print(r.key_with_value(4))
#-------------------------
#--------8------------
dict_={}
e=Empty(dict_)
print(e.empty_check())
#-------------------------
#---------9---------
s=String_dict("assalom aleykum")         
print(s.str_key_value())
dict_={1:4,4:7,2:5,0:10}
