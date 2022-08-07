import sys
n = int(sys.stdin.readline())
t = []
p = []
x = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    t.append(a)
    p.append(b)
    x.append(b)
x.append(0)
for i in range(n - 1, -1, -1):
    if t[i] + i > n:
        x[i] = x[i + 1]
    else:
        x[i] = max(x[i + 1], p[i] + x[i + t[i]])
print(x[0])