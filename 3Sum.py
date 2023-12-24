num = [-1,0,1,2,-1,-4,-2,-3,3,0,4]

num.sort()

print(num)

targe_array = []
temp_traget_value = []

position_target = []
temp_position_target = []

for i in range(len(num)):
    for j in range(i+1,len(num)):
        for k in range(j+1,len(num)):
            if num[i]+num[j]+num[k] == 0:
                temp_traget_value= []
                temp_position_target = []
                if num[i] == -4 and num[j] == 1 and num[k] == 3:
                    print(num[i]+num[j]+num[k])
                temp_traget_value.append(num[i])
                temp_traget_value.append(num[j])
                temp_traget_value.append(num[k])
                
                print(temp_traget_value)

                temp_position_target.append(i)
                temp_position_target.append(j)   
                temp_position_target.append(k)

                temp_traget_value.sort()
                temp_position_target.sort()

                if temp_traget_value in targe_array : 
                    continue
                elif len(temp_traget_value) == 3 :
                    targe_array.insert(2,temp_traget_value)
                    position_target.insert(2,temp_position_target)
                temp_traget_value= []
                temp_position_target = []

print(targe_array)