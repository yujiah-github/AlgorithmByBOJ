import sys
n, m = map(int, sys.stdin.readline().strip().split())
a = list(map(int, sys.stdin.readline().strip().split()))
b = list(map(int, sys.stdin.readline().strip().split()))
list_sum = []
cnt = n + m
for i in range(n):
    list_sum.append(a[i])
for i in range(m):
    list_sum.append(b[i])
list_sum.sort()
for i in range(cnt):
    print(list_sum[i], end=' ')