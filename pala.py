a=int(input("enter the value:"))
d=a
sum=0
c=0
#same as reverse of the number
while a!=0:
    sum=int(a%10)
    c=c*10+sum
    a=int(a/10)
if d==c:
    print('palandrom')
else:
    print('not')

