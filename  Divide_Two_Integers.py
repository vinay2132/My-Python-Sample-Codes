dividend = -2147483648
divisor = -1
x = 0

x = dividend/divisor

if x >= ((2**31) - 1) :
    x = ((2**31) - 1)
print(int(x))