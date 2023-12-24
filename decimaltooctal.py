a=int(input("enter the value"))
i=1
c=0
d=0
while a!=0:
    c=a%8
    a=int(a/8)
    d=d+c*i
    i=i*10
print(d)