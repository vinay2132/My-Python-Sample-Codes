number_map = {
    '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
}

digits = "23"
digit_array = []
x = 0
targe_array = []
temp = []

for i in digits:
    digit_array.append(i)

print(digit_array)

for value, symbol in number_map.items():
    for i in range(len(digit_array)):
        if value == digit_array[i]:
            temp.append(symbol)

print(temp)


