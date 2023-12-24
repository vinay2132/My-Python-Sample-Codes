s = "+-212"
x = []
y = 0
temp = 0
res = 0
for i in range(0, len(s)):
    if s[0] == "-":
        temp = 1
    if i < len(s):
        if (s[0] == "+" and (s[1] == '+' or s[1] == '-')) or (s[i] == "-" and (s[1] == '+' or s[1] == '-')) :
            temp = 2
            break
    if s[i].isdigit():
        print(s[i])
        x.append(s[i])

    if s[i].isalpha() == True or s[i] == '.':
        temp = 2
        break

s = [str(i) for i in x]
if len(s) != 0:
    res = int("".join(s))
if res >= ((2**31) - 1) :
    res = ((2**31) - 1)
if temp == 1:
    res = -(res)

if temp == 1 and res == -((2**31) - 1):
    print('a')
    res = ((2**31))

print(res)