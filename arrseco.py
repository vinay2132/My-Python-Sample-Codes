a=int(input("enter the num:"))
b=[]
temp=0
for i in range(0,a):
    temp=input()
    b.append(temp)
print(b)
c=min(b)
b.remove(c)
c=min(b)
print(c)