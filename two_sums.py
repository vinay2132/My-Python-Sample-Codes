# nums = [3,2,4,33] 
# target = 6
# for i in range(len(nums)+1):
#     #print(nums[i]+nums[i+1])
#     # while i < len(nums)-1:
#     #     if((nums[i]+nums[i+1]) == target):
#     #         print(i,i+1)
#     #         break;
#     print(i)
#     print(nums[i],nums[i+1])
#     # if((nums[i]+nums[i+1]) == target):
#     #     print(i,i+1)
#     #     break;


nums = [3,2,3]
target = 6
for i in range(len(nums)):
            result = []
            while i < len(nums)-1:
                if(nums[i]+nums[(i+1)%len(nums)] == target):
                    result.append(i) 
                    result.append(i+1) 
                    print(result)
                    # myTuple = (nums[i],nums[(i+1)%len(nums)])
                    # print(myTuple)
                break;
                