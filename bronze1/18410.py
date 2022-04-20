import sys
n, m = map(int, sys.stdin.readline().strip().split())
a = list(map(int, sys.stdin.readline().strip().split()))
b = list(map(int, sys.stdin.readline().strip().split()))
list = []
for i in range(n):
    list.append(a[i])
for i in range(m):
    list.append(b[i])
cnt = n+m
list.sort()
for i in range(cnt):
    print(list[i])