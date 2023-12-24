nums =[3,9,6]
k =5
x = k
a = []
main_count = 0
count = 0
temp = 0
for i in range(len(nums)):
    k = x
    for j in range(k):
        x = nums[i] + j
        if x in nums and j != 0:
            # print (nums[i])
            # print(j)
            a.append(nums[i])
            count += 1 
            temp = 1
            if temp == 0:
                temp = 1
                main_count = count
            elif main_count < count:
                main_count = count
            k = k-j

print(a)
print(main_count)

# main_count = 0
# for i in range(len(a)):
#     count = a.count(a[i])
#     if main_count < count:
#         main_count = count

# print(main_count)