'''
a=input("enter the value:")
d=a
e=0
sum=0
while a!=0:
    
    b=len(d)
    c=10**(b-1)
    sum=int(int(a)/c)
    
    if sum==0:
        print(1)
        
    else:
        print(sum)
        
    a=int(int(a)%c)
    e=int(int(a)%c)
    d=str(e)
    '''


#outher methors
a=int(input("enter the value"))
b=0
#very imp which converts string to array
r=[int(x) for x in str(a)]

for i in range (0,len(str(a))):
    if r[i]==0:
        r[i]=1
   
    b=b*10+r[i]
print(b)
   


