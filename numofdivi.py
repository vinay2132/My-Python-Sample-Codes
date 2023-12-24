a=int(input("enter the values"))
c=0
x=0
for j in range(0,a):
    c=0
    for i in range (1,j+1):
        if j%i==0:
            c+=1
        if(c==9):
            x+=1
    print(x)
           
        
                   