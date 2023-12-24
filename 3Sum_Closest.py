# nums = [-1,2,1,-4]
# target = 1
# acturla_value = 0
# temp = 0
# nums.sort()

# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         for k in range(j+1,len(nums)):
#             acturla_value = nums[i]+nums[j]+nums[k]
#             if acturla_value < temp:
#                 temp = acturla_value
#             print("temp value")
#             print(temp)
#             print("acturla_value")
#             print(acturla_value)


nums = [-1,2,1,-4]
target = 1
calucated_value = 0
temp = 0

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(j+1,len(nums)):

            calucated_value = nums[i]+nums[j]+nums[k]

            difference = target - calucated_value

            if difference < 0: 
                difference = -difference


            if temp == 0:
                actuall_value = calucated_value
                main_difference = difference
                temp = 1

            elif temp == 1 and difference < main_difference:
                main_difference = difference
                actuall_value = calucated_value

print(calucated_value,difference,actuall_value)
            






            
                



