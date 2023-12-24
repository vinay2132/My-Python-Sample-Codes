haystack = "leetcode" 
needle = "leex"

x = 0
b = 0

for i in range(len(haystack)):
    for j in range(len(needle)):
        print(haystack[i],needle[j],x,len(needle))
        if haystack[i] == needle[j]:
            x += 1
            # print(haystack[i],needle[j],x,len(needle))
            if x == len(needle):
                b = 1
            break
        if haystack[i] != needle[j]:
            continue

print(b)
