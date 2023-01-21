import sys
T = int(sys.stdin.readline())
for i in range(T):
    a = list(map(int, sys.stdin.readline().strip().split()))
    a.sort()
    print(a[-3])