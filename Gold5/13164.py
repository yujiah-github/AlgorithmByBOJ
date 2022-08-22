import sys

n, k = map(int, sys.stdin.readline().split())
students = list(map(int, sys.stdin.readline().split()))

array = []
for i in range(1, n):
    array.append(students[i] - students[i-1])

array.sort(reverse=True)
print(sum(array[k-1:]))