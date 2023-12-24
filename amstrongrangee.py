a=int(input("enter"))
b=int(input("enter the value:"))
sum=0
d=0
j=0
for i in range(a,b+1):
    j=i
    sum=0
    d=0
    while i!=0:
       
        sum=int(i%10)
        d=sum**3+d
       # print(i,",",d)
        i=int(i/10)
    
    if d==j:
        print(d)
