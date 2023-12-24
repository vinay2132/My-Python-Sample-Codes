s = "aab"
main = []
temp = []
for i in range(len(s)):
    if i == 0:
        main.append(s[i])
        temp = main
    else:
        for j in range(len(main)+1):
            print(temp,'a')
            print(main,'b')
            print(s[i],'c')
            temp = main
            if s[i] in main:
                main = []
            else:
                print(main)
                main.append(s[i])
if s == "":
    print (0)
if s == " ":
    print (1)
else:
    print (len(temp)) 
