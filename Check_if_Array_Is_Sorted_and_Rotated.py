nums = [3,4,5,1,2]

nums = sorted(nums)
print(nums)

a = 0
temp = 0
for i in range(len(nums)):
    if i == 0:
        a = nums[i]
    else:
        a += 1
    print(a)
    print(nums[i])
    if a != nums[i] and i != 0:
        print("false")
        temp = 1
    break

