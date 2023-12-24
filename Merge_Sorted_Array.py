nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

# merge = []

# for i in range(len(nums1)):
#     if i <= m-1:
#         merge.append(nums1[i])

# for j in range(len(nums2)):
#     if j <= n-1:
#         merge.append(nums2[j])

# nums1.clear()
# for k in range(len(merge)):
#     nums1.append(merge[k])

# nums1.sort()
# print(nums1)

for i in range(m, len(nums1)):
    del nums1[m]

for j in range(len(nums2)):
    if j <= n-1:
        nums1.append(nums2[j])
print(nums1)

