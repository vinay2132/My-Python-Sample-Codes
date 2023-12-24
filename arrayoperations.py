a=["a","b","c"]
print(a)
for i in range(0,len(a)):
    print(a[i])
if "d" in a:
    print('yes')
else:
    print('no')
a.append('xx')
print(a)
a.insert(1,"djf")
print(a)
#dynamically entering the values
b=[]
n=int(input("enter the array length:"))
temp=0
for j in range(0,n):
    temp=input()
    b.append(temp)
print(b)
