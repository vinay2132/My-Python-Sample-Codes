a = "cbbd"

t = ""
for i in range(len(a)):
    t+=a[i]

    w = ""
    for i in t:
        w = i + w

        if (t == w):
            print("Yes")
            x = t
        else:
             print("No")

print(x)