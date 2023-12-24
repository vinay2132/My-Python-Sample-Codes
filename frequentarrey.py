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
d=0
for i in range (0,a):
    if b[i]==b[i+1]:
        c+=1
        if c>d:
            for i in range(0,c):
                b.append(b[i])

        else:
            b.append(b[i+c])
d=c
 
c=0
print(b)




#2,3,2,4,5,12,2,3,3,3,12
#['2', 2, 2, 3, 3, 3, 3, 4, 5, 12, '12']
#3,3,3,3,2,2,2,12,12,4,5