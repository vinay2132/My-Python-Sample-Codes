nums = [1,1,1,2]
# x = []

# for i in range(len(nums)):
#     if  i < len(nums) - 2:
#         if nums[i] == nums[i+1]:
#             continue
#     x.append(nums[i])


# if len(x) == 2 and x[0] == x[1]:
#     a = x [0]
#     x = []
#     x.append(a)


# print(x)

x = 0

for i in range(len(nums)):
    if  i < len(nums) - 2 and nums[i] == nums[i+1]:
        continue
    nums[x] = nums[i]
    x = x+1 

print(x)