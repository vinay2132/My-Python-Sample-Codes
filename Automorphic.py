a=int(input("enter the value:"))
if ((a**2)%10)==a:
    print('automorphic')
else:
    print('not')
#harched number
b=int(input("enter the value:"))
d=b
sum=0
c=0
while b!=0:
    sum=int(b%10)
    c=sum+c
    b=int(b/10)
print(c)
if (d%c)==0:
    print('harched')
else:
    print('not')

