import sys
lst = []
N = int(sys.stdin.readline())

for i in range(N):
    lst.append(int(sys.stdin.readline()))
    
lst.sort()

for _ in range(N):
    print(lst[_])