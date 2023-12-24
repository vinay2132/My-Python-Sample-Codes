strs = ["dog","racecar","car"]
a = strs[0]
b = strs[1]
x = []
z = []
y = "" 
for i in range(len(a)):
    for j in range(len(b)):
        print(a[i], b[j])
        if(a[i] == b[j]):
            x.append(a[i])
print(y.join(x))
