nums = [1,3,5,6]
target = 7

x = 0
for i in range(len(nums)):
    if nums[i] == target:
        x = i
    else: 
        if nums[i] < target:
            x = i+1
print (x)
        


