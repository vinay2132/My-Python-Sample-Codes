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
for i in range (0,a):
    for j in range(0,b):
        temp+=int(c[i][j])
    break
print(temp)
e+=temp
temp=0
for i in range(a-1,a):
    for j in range(0,b):
        temp+=int(c[i][j])
    break
print(temp)
e+=temp
temp=0
for j in range(0,b):
    for i in range(0,a):
        temp+=int(c[i][j])
    break
print(temp)
e+=temp
temp=0
for j in range(b-1,b):
    for i in range(0,a):
        temp+=int(c[i][j])
    break
print(temp)
e+=temp
print(e)
temp=0
e=int(e)-int(c[0][0])-int(c[0][a-1])-int(c[b-1][0])-int(c[a-1][b-1])
print(e)

