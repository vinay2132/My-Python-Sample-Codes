b = int(input(" Please Enter the First Value a: "))
for i in range (0,b+1):
  
    for j in range(2,i):
        
        if i%j!=0 and i==j:
            print(i)
