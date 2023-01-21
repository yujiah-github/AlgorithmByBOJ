cnt = int(input())
numbers = list(map(int, input().split()))
print(min(numbers),max(numbers))

import sys
N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a.sort()
print(a[0], a[-1])