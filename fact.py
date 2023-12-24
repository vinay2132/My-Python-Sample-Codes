#factorial
a=int(input("enter the value:"))
sum=1
for i in range (1,a):
    sum=sum*a
    a-=1
    
print(sum)
#leap year
leap=int(input("enter the year:"))
if leap%4==0:
    print('leap')
else:
    print('not')

