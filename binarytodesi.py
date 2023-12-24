a=int(input("enter the value"))
b=0
sum=0

r=[int(x) for x in str(a)]
print(r)
#for i in range(len(str(a)),0,-1):
for i in range (0,len(str(a))):
   
    if r[i]==1 or r[i]==0:
        b=r[i]*(2**(len(str(a))-i-1))
        
        sum=sum+b
print(sum)



