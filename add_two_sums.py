# l1 = [2,4,3]
# l2 = [5,6,4]
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
sum1  = 0
sum2  = 0

for i in range(len(l1)+1):
    while i < len(l1):
        sum1 += l1[i] * 10**i
        break;

print(sum1)
for i in range(len(l2)+1):
    while i < len(l2):
        sum2 += l2[i] * 10**i
        break;

total = sum1 + sum2
total = str(total)[::-1]
total_list = []

for i in range(len(str(total))):
    total_list.append(int(str(total)[i]))
print(total_list)
