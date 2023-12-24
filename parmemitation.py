n=int(input("enter the value"))
r=int(input("enter the value"))
sumn=1
sumnr=1
if n>r:
    for i in range (1,n+1):
        sumn=sumn*i
    for j in range (1,(n-r)+1):
        sumnr=sumnr*j
    print(int(sumn/sumnr))
else:
    print("enter correct value")
   