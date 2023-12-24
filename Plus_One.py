digits = [9,9]
for i in range(len(digits)):
    if i == len(digits)-1:
        digits[i] += 1
        if digits[i] > 9:
            digits[i] = 1
            digits.append(0) 

print (digits)

# x = 0
# for i in range(len(digits)):
#     x = digits[i] + (x*10**(len(digits)-2))
# x+= 1
# digits.clear()

# # digits = [int(a) for a in str(x)] 
# a = 0
# y = str(x)
# while a < len(str(x)):
#     digits += y[a]
#     a = a + 1
# print (digits)