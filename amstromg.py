a=int(input("enter the value:"))
b=a
sum=0
d=0
while a!=0:     
    sum=int(a%10)
    d=sum**3+d
    a=int(a/10)
print(d)
if b==d:
    print('amstromg')
else:
    print('not')