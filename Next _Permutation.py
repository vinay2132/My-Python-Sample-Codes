nums = [1,1,5]

sorted_array = sorted(nums)

y = [sorted_array]

x = len(sorted_array)

temp  = 0

if sorted_array == nums:
    temp = sorted_array[x-2]
    sorted_array[x-2] = sorted_array[x-1]
    sorted_array[x-1] = temp
nums = sorted_array
nums.append(temp)
print(nums)
print(sorted_array)