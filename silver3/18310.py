import sys

n = int(sys.stdin.readline())
lst = []
lst = list(map(int, input().rstrip().split()))
lst.sort()
print(lst[(n-1)//2])