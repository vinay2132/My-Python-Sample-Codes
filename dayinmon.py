a=int(input("enter the value year"))
b=int(input("enter the value mon"))
c=0
if a%4==0 and b==2:
    c=29
elif b%2==0 and b!=2 :
    if b<=7 :
        c=30
    else:
        c=31
elif b%2!=0 and b!=2:
    if b>7 :
        c=31
    else:
        c=30
else:
    c=28
print("the no of days month",c)
    