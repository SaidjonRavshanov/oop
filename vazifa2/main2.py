from cal import Cal
from uchburchak import Uchburchak
from circle import Circle
from distance import Distance
from triangle_area import Triangle
from average import Average
from radius import Radius
from radius import Radius

#-------------------
#--------1---------
x=3
y=4
res=Cal(x=x,y=y)
print(res.diff())
#-------------------
#--------2---------
k=Uchburchak(3,4)
print(k.peremetr())
print(k.yuza())
#-------------------
#--------3---------
y=Radius(10)
print(y.area_c())
print(y.length_c())
#-------------------
#--------4---------
c=Circle(100)
print(c.radius())
#-------------------
#--------5---------
d=Distance(1,2,3,4)
print(d.distance())
#-------------------
#--------6---------
d=Triangle(6,2,3,4,9,3)
print(d.area())
#-------------------
#--------7---------
d=Average(6,7)
print(d.arithmetic_mean())
print(d.geometric_mean())
