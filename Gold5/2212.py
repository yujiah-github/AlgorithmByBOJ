import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
n = sorted(list(map(int, sys.stdin.readline().split())))

if K >= N:
    print(0)
    sys.exit()

dist = []
for i in range(1, n):
    dist.append(n[i] - n[i-1])

dist.sort(reverse=True)
for _ in range(n-1):
    dist.pop(0)

print(sum(dist))