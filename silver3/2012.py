import sys

n = int(sys.stdin.readline())
lst = []
for i in range(n):
    lst.append(int(sys.stdin.readline()))
lst.sort()

sum = 0
for i in range(n):
    sum += abs(lst[i] - (i+1))
print(sum)