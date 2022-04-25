import sys
x = 100
y = 100
n = int(sys.stdin.readline())
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if(a>b):
        y = y - a
    elif(a==b):
        continue
    else:
        x = x - b
print(x)
print(y)