c=int(input("enter:"))
d=[]
temps=0
for i in range(0,c):
    temps=input()
    d.append(temps)
print(d)
for i in range(0,c):
    a=0
    for j in range(0,c):
        if d[i]==d[j] and i!= j:
            a+=1
        if a%2!=0:
            print(a)
            print(a*int(d[i]))
        break
     
  