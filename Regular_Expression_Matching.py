s = "aaa"
p = "a*"


main = s+p
actual_value = 1
for i in range(len(main)):
    
    x = ""
    y = ""

    if i < len(s):
        x = s[i]

    if i< len(p):
        y = p[i]



    if y == '.':
        actual_value = 1
    
    
    if y == '*':
        print(p[i-1])

    elif x != y:
        actual_value = 0
    print("loop done")
    
print (actual_value)
