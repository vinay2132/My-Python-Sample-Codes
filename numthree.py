a=int(input('enter the range:'))
b=0
c=0
for i in range(0,a+1):
    b=i
    if b%10==3 :
        #print(i)
        c+=1
    else:
        while b!=0:
            if b%10==3:
                #print(i)
                c+=1
                break
            else:
                b=int(b/10)
print("the total no of varibles in 3 are",c)


   

        
