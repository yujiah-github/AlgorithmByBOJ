import sys

lst = []
N = int(sys.stdin.readline())

for i in range(N):
    lst.append(int(sys.stdin.readline()))

lst.sort()
for j in lst:
    print(j)