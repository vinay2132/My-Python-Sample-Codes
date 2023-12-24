a=int(input("enter the num:"))
b=[]
temp=0
x=0
for i in range(0,a):
    temp=input()
    b.append(temp)
print(b)
c=int(input("enter:"))
d=[]
temps=0
for i in range(0,c):
    temps=input()
    d.append(temps)
print(d)
for i in range(0,c):
    x=d[i]
    for j in range(0,b):
        if int(b[j])==x:
            temps=int(b[i])
            b[i]=int(b[i+1])
            b[i+1]=temps
    a-=1
print(b)





# {3, 6, 13, 3, 9, 10, 14, 6, 9, 13}
# {6, 3, 9, 13, 10}
# {6, 6, 3, 3, 9, 9, 13, 13, 10, 14}