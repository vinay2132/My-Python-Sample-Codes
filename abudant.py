a=int(input('enter the value of a:'))
sum=0
for i in range(1,a):
    if a%i==0:
        sum=sum+i
print(sum)
if a<sum:
    print('abudant')
else:
    print('noot')
   