s = "PAYPALISHIRING"
numRows = 3
row = 0 

direction = 'down'
if numRows < 2:
    print(s)

arr = ['' for i in range(numRows)]

for i in s:
    arr[row] += i

    if row == numRows-1:
        direction = 'up'
    elif row == 0:
        direction = 'down'
    if(direction == 'down'):
        row += 1
    else:
        row -= 1
print(''.join(arr))


 
