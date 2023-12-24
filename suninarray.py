c=int(input("enter:"))
d=[]
temps=0
for i in range(0,c):
    temps=input()
    d.append(temps)
print(d)
temps=0
for i in range(0,c):   
    #print(int(d[i]))
    #temps+=int(d[i])
    temps+=int(d[i])
    #print(temps)
print("sum of num",int(temps))
#print(sum(d))