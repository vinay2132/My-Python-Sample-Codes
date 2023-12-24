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
d=0
for i in range (0,a):
   d+=int(c[0][i])
print(d)
for i in range(0,b):
    d+=int(c[a-1][i])
print(d)
for i in range(0,a):
    d+=int(c[i+1][a])