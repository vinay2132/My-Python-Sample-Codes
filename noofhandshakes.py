n=int(input("enter the value"))
r=2
sumn=1
sumnr=1
x=n-r
for i in range(1,n):
    sumn=sumn*n
    n-=1

for j in range(1,x):
    sumnr=sumnr*x
    x-=1

sum=int(sumn/(r*sumnr))
print(sum)