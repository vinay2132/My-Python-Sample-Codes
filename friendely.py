a=int(input("enter the value:"))
b=int(input("enter the value:"))
suma=0
sumb=0
for i in range(1,a):
    if a%i==0:
        suma=suma+i
print(suma)
for i in range(1,b):
    if b%i==0:
        sumb=sumb+i
print(sumb)
if (a/suma)==(b/sumb):
    print('friendly num')
else:
    print('not friende')