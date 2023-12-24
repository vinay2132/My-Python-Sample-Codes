s = "abcabcbb"
x=[i for i in s] 
#print(x)
main_list = []
for i in s:
    #print(i)
    if i in main_list:
        print(i,'a')
    else:
        main_list = i

print(main_list)

