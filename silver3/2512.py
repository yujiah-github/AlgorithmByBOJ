import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
low, high = 0, max(lst)
while low <= high:
    mid = (low + high) // 2
    num = 0
    for i in lst:
        if i >= mid: num += mid
        else: num += i
    if num <= m: low = mid + 1
    else: high = mid - 1
print(high)