import math
a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
c=int(input("enter the value of c"))
#-b+-sqr(b^2-4ac)/2a
k=0
y=0
x=0
k=(b**2)-(4*a*c)
x=-b+math.sqrt(k)
y=-b-math.sqrt(k)
print(x/(2*a))
print(y/(2*a))
#a=2,b=3,c=4
