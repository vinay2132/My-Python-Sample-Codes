nums = [1,2,3,4]
val = 3

x = []

for i in range(len(nums)):
    if nums[i] != val:
        x.append(nums[i])

print(x)