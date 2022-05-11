import sys
n = int(sys.stdin.readline())
for i in range(1, n+1):
    a,b = map(int, sys.stdin.readline().split())
    sum = a+b
    print("Case #{0}: {1} + {2} = {3}".format(i, a, b, sum))