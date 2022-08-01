import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
a.sort(reverse=True)
sum = a[0]
for i in range(1,n):
    sum += (a[i]/2)
print('%g'%sum)