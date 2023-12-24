a = int(input(" Please Enter the First Value a: "))
b = int(input(" Please Enter the Second Value b: "))
for i in range (a,b+1):

    for j in range(2,i):
       
        if i%j==0 and i!=j:
            break
    else:
        print(i)