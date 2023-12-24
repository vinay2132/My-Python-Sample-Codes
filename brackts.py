s = "()"
if(len(s)%2 != 0):
    print('false')
main = []
for i in s:
    main.append(ord(i))
print(main)
if(main[0] == main[0+1]-1):
    print('true')
for i in range(len(main)):
    if(main[i] == main[i+1]-1):
        main.pop(i)
        main.pop(i+1)
        i = i-2
        print('true')
if(len(main)==0):
    print('true')
else:
    print('false')



