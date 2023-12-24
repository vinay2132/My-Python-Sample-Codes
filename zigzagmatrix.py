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
    break
e+=temp        
print(int(e))
for i in range(a-1,a):
    temp=0
    for j in range(0,b):
        temp+=int(c[i][j])
    break
e+=temp       
print(int(e))
temp=0
if a%2!=0:
    f=int(a/2)
    #f+=1
    temp=int(c[f][f])
    e+=temp
    print(int(e))
 


   






    