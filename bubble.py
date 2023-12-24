a=int(input("enter the num:"))
b=[]
temp=0
temps=0
for i in range(0,a):
    temp=input()
    b.append(temp)
print(b)
for j in range(0,a-1):
    for i in range (0,len(b)-1):
        if int(b[i])>int(b[i+1]):
            temps=int(b[i])
            b[i]=int(b[i+1])
            b[i+1]=temps
    a-=1
print(b)

#1,4,6,3,2