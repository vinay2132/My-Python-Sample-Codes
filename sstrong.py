a=int(input("enter the value:"))
e=0
e=a
b=0
sum=1
d=0
while a!=0:
   b=int(a%10)
   for i in range(1,b):
      sum=sum*b
      b-=1
   d=sum+d
   sum=1
   a=int(a/10)  
print(d)
if d==e:
   print("strong")
else:
   print('not')
