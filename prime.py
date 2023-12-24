a=int(input("enter the value:"))
for i in range(2,a+1):
   
    if a%i==0 and a!=i:
     
        print('not prime')
        break
        
    else:
     
       print('prime')
       break
        