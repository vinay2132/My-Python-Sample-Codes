x = 2147395599
a = 0
b = 1

for i in range(x):
    a = i**2
    if x >= a and a != 0 :
        b = i

if  x == 0:
    b = 0

print(b)