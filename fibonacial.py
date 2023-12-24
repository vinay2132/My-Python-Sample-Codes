dig=int(input('enter the value:'))
a=1
b=1
c=0
for i in range(0,dig):
    if c==0:
        print(b)
        print(a)
        c=1
    else:
        c=a+b
        print(c)
        b=a
        a=c
        





        '''
        1-1(c)
        2-1(c),2(b)
        3-3(b)
        '''
