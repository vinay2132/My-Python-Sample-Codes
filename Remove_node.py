head = [1,2,3,4,5]
n = 2

for i in reversed(head):
    if i == n:
        head.pop()

print(head)