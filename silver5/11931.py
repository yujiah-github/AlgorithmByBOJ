import sys
n = int(sys.stdin.readline())
list = []
for i in range(n):
    x = int(sys.stdin.readline())
    list.append(x)
list.sort(reverse = True)
for i in range(n):
    print(list[i])