a=int(input("enter the value:"))
sum=0
for i in range(1,a):
    if a%i==0:
        sum=sum+i
print(sum)
if sum==a:
    print('perfect')
else:
    print('not')
        
  
        
        