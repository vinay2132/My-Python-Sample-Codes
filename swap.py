a=int(input('enter the value of a:'))
b=int (input("enter the value of b:"))
#using teemp variable 
temp=a
a=b
b=temp
print(a)
print(b)
#not using teemp(possinble only in python)

a=a+b
b=a-b
a=a-b
print(a)
print(b)
#special in python
x=int(input('enter the value of a:'))
y=int (input("enter the value of b:"))
x, y = y, x
print( x, y) 


