nums = [5,7,7,8,8,8,10]
target = 8
x = []

for i in range(len(nums)):
    if nums[i] == target:
        x.append(i)
    if len(x) > 2:
        x.pop(1)

if len(x) == 0:
    x.append(-1)
    x.append(-1)
    print (x)


if len(x) == 1:
    x.append(x[0])
    print (x)

if len(x) == 2:
    print (x)

# if len(x) > 2:
#     y.append(x[0])
#     y.append(x[-1])
#     print (y)
