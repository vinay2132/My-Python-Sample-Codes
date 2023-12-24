num1 = [1,2]
num2  = [3,4,5]
mearge = []
x = 0

for i in range(len(num1)):
    mearge.append(num1[i])

for j in range(len(num2)):
    mearge.append(num2[j])

mearge.sort()

# x = (len(mearge))/2


# if x.is_integer():
#     print (mearge[int(x)])

# else:
#     print(mearge[int(x)])
print(mearge)

x = (len(mearge))/2

if len(mearge) == 1:
    print(mearge[int(x)])


if len(mearge)%2 != 0:
    print (mearge[int(x)])

if len(mearge)%2 == 0 :
    print((mearge[int(x)]+mearge[int(x-1)])/2)


# print(x)
# print(mearge)