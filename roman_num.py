roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
s = "IV"
a = 0
j = 0
d = 0
sub_string=[]
sub_number = []
for i in s:
    sub_string.append(i)
for j in sub_string:
    sub_number.append(roman[j])
    d += 1
for k in range(len(sub_number)):
    if k+1 != len(sub_number):
        if sub_number[k] >= sub_number[k+1]:
            a += sub_number[k]
            print(sub_number[k],sub_number[k+1])
        else:
            a -= sub_number[k]
            print(sub_number[k],sub_number[k+1],'A')
    
print(a)
print(sub_string)
print(sub_number)