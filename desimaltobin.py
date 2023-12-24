a=int(input("enter the value"))
i=1
c=0
d=0
while a!=0:
    c=a%2
    a=int(a/2)
    d=d+c*i
    i=i*10
print(d)
    

