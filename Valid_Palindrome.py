s = "A man, a plan, a canal: Panama"
s = s.lower()
perfect_string=""
# Iterate over the string using a for loop
for i in s:
# Check if the character in the list is not special
    if i.isalnum():
# If the character is not special, add it to list
        perfect_string += i 

print(perfect_string)

reversed_string = perfect_string[::-1]
print(perfect_string == reversed_string)





