a=int(input("enter the value:"))
sum=0
c=0
while a!=0:
    sum=int(a%10)
    c=c*10+sum
    a=int(a/10)
    
print(c)

