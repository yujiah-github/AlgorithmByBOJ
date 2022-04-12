import sys
x = int(sys.stdin.readline())
for i in range(x):
    a = list(map(int, sys.stdin.readline().strip().split()))
    a.sort()
    print(a[-3])