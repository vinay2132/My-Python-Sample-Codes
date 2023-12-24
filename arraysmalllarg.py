a=int(input("enter the num:"))
b=[]
temp=0
for i in range(0,a):
    temp=input()
    b.append(temp)
print(b)
x=0
#print(max(b))
for i in range(0,a):
    if int(x)< int(b[i]):
        x=b[i]
print(x) 