#a=input('enter the char:')97 122 65 90
b=input('enter the char:')
a=ord(b)
print(a)
if (a>=97 and a<=122) or (a>=65 and a<=90):
    print('char')
else:
    print('specal')
if a>=97 and a<=122:
    print('lower case')
elif a>=5 and a<=90:
    print('upper case')
else:
    print ('special')

    '''   
internet program
ch = input("Enter a character: ")
if((ch>='a' and ch<= 'z') or (ch>='A' and ch<='Z')):
    print(ch, "is an Alphabet")
else:
    print(ch, "is not an Alphabet") 

'''



