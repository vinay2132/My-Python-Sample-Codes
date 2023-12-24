import math
c=int(input("enter:"))
d=[]
temps=0
for i in range(0,c):
    temps=input()
    d.append(temps)
print(d)
#print(max(d))
#print(math.sqrt(c))
temps=0
for i in range(0,c):
   # print(math.sqrt(int(d[i])))
    for j in range (0,int(max(d))):
        if int(math.sqrt(int(d[i])))-math.sqrt(int(d[i]))==0:
            print(int(d[i]))
            temps+=int(d[i])
            break
print(int(temps))
        


   
    
            

