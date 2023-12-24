s = "   fly me   to   the moon  "
reverse_str = []
a = len(s)
while a > 0:
    reverse_str += s[a-1]
    a = a - 1
print (reverse_str)

x  = 0

for i in range(len(reverse_str)) :
    if reverse_str[i] != ' ':
         print(reverse_str[i])
         x+=1
    else :
        if x == 0:
            continue 
        else:
            break

print (x)

