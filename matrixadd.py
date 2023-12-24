a=int(input("enter the rows:"))
b=int(input("enter the coloms:"))
c=[]
temp=0
for i in range (0,a):
    d =[]
    for j in range (0,b):
        temp=input()
        d.append(temp)
    c.append(d)
for i in range (0,a):
    for j in range (0,b):
        print(c[i][j],end=" ")
    print()
temp=0
e=0
for i in range(0,a):
    temp=0
    for j in range(0,b):
        temp+=int(c[i][j])
    #print(int(temp))
    if temp > e:
        e=0
    else:
        temp==e
print("row max",temp)
temp=0
e=0
for j in range(0,b):
    temp=0
    for i in range(0,a):
        temp+=int(c[i][j])
    #print(int(temp))
    if temp > e:
        e=0
    else:
        temp==e
print("colom max",temp)