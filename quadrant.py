a=int(input('enter the value of x:'))
b=int (input("enter the value of y:"))
if a>=1 and b!=0:
    if b>=1:
        print("1st")
    else:
        print('4th')
elif a<0 and b!=0:
    if b>=1:
        print('2nd')
    else:
        print('3rd')
elif a==0 and b!=0:
    if b>=1:
        print('on y-axis between 3rd and 4th')
    else:
        print('on y-axis between 1st and 2nd')
elif b==0 and a!=0:
       if a>=1:
            print(' on x-axis between 1st and 3rd')
       else:
            print('on x-axis between 2nd and 4th')
else:
    print('on center as orgine')

