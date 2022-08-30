import sys

n = int(sys.stdin.readline())
b, r = 0, 0
lst = sys.stdin.readline()
for i in range(n-1):
    f = lst[i]
    if lst[i] == lst[i+1]:
        if i == n-2:
            if lst[i+1] == 'B':
                b += 1
            else:
                r += 1
    else:
        if f == 'B':
            b += 1
        else:
            r += 1
        if i == n-2:
            if lst[i+1] == 'B':
                b += 1
            else:
                r += 1
print(min(b, r)+1)