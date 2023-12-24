a=int(input('enter the value of a:'))
b=int (input("enter the value of b:"))
c=int(input("enter the value of c:"))
if a<b:
    big=b
    if big<c:
        print(c)
    else:
        print(big)
else:
    big=a
    if big<c:
        print(c)
    else:
        print(big)


