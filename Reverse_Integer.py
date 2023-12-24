num = 1563847412

reversed_num = 0
temp = 0
temp2 = 0


if num < 0:
    num = -(num)
    temp = 1    

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

temp2 = reversed_num

if temp == 1:
    reversed_num = -(reversed_num)

if temp2 >= 2**31 :
    reversed_num = 0


print(reversed_num)