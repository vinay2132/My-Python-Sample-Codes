a=int(input('enter the value of a:'))
for i in range (1,a+1):
    for j in range (1,a+1):
        if (a%i)==0:
           
            if i*j==a:
                print(i,'*',j,'=',a)