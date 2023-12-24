num = 23

roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

symbols = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

roman_string = ""
a = ""

roman_numeral = ''
for value, symbol in symbols.items():
    while num >= value:
        roman_numeral += symbol
        num -= value

print(roman_numeral)