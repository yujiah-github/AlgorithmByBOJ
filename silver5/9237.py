import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().strip().split()))
arr.sort()
for i in range(n):
    arr[i] = arr[i] - i
print(max(arr) + 1 + n)